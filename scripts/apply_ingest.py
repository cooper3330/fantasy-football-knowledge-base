#!/usr/bin/env python3
"""
Applies an ingest plan (JSON) to the wiki. Phase B of ingest v2 -- see
docs/ingest-v2-plan.md.

WHY: an ingest agent used to interleave reading and writing across ~66 turns.
Measured across 12 agents, output tokens were 47.6% of cost at 4.5% of volume --
the agent was re-reasoning over an ever-growing context on every one of those
turns. But the write half is entirely mechanical: where a bullet goes is a
function of its date, a new page is a filled-in template, and the catalog row and
log header are derivable from the episode. None of that needs a model.

So phase A (LLM) reads the transcript and emits one plan. This applies it for
zero tokens.

  python3 scripts/apply_ingest.py plan.json --dry-run   # validate only
  python3 scripts/apply_ingest.py plan.json

VALIDATE-THEN-WRITE is the whole safety design. Every check runs against the
entire plan before a single file is touched, so a malformed plan costs nothing
and leaves no half-ingested episode behind. State is finalized LAST, so an
interruption always leaves the episode `fetched` -- which
scripts/partial_write_check.py detects and scripts/rollback_partial.py undoes.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state_io                                                    # noqa: E402
import wiki_update as wu                                           # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "wiki" / "sources"
VALID_KINDS = ("player", "concept", "format")
POSITIONS = ("QB", "RB", "WR", "TE")


# Filename-hostile characters. A colon is the one that actually shows up: shows
# are titled "Reception Perception: The Show", and an agent naming the source page
# after the show verbatim produces a filename that macOS renders with a slash and
# that diverges from the five existing pages for the same show. Deterministic to
# fix, so it is fixed rather than rejected -- same reasoning as stamping the date.
FS_UNSAFE = {":": "", "/": "-", "\\": "-", "|": "-", "*": "", "?": "", '"': "'",
             "<": "", ">": ""}


def normalize_source_page(name):
    for bad, good in FS_UNSAFE.items():
        name = name.replace(bad, good)
    return " ".join(name.split())


def normalize(plan):
    """Rewrite the plan in place where the fix is mechanical. Returns notes."""
    notes = []
    raw = ((plan.get("source") or {}).get("page") or "").strip()
    clean = normalize_source_page(raw)
    if raw and clean != raw:
        # Replace across the whole plan, not just source.page: the bullets cite
        # this name as a wikilink and would otherwise point at a file that does
        # not exist.
        plan.update(json.loads(json.dumps(plan).replace(raw, clean)))
        notes.append(f"source page name {raw!r} -> {clean!r}")
    return notes


def validate(plan):
    """Every problem with the plan, as a list. Empty list means safe to apply."""
    errs = []

    def need(obj, key, where):
        v = obj.get(key)
        if not v or (isinstance(v, str) and not v.strip()):
            errs.append(f"{where}: missing or empty {key!r}")
            return None
        return v

    guid = need(plan, "guid", "plan")
    ep = {}
    if guid:
        state = state_io.read_state()
        ep = state["episodes"].get(guid) or {}
        if not ep:
            errs.append(f"plan: guid {guid!r} is not in state.json")
        elif ep.get("status") != "fetched":
            errs.append(f"plan: episode status is {ep.get('status')!r}, expected "
                        f"'fetched'. Already ingested? Re-applying would duplicate.")

    src = plan.get("source") or {}
    if not src:
        errs.append("plan: missing 'source' block")
    else:
        for k in ("page", "expert", "show", "episode", "body"):
            need(src, k, "source")
        expert = src.get("expert")
        if expert and not (REPO / "wiki" / "experts" / f"{expert}.md").exists():
            errs.append(f"source: {expert!r} has no expert page. Only tracked "
                        f"experts get one; a guest is attributed inline.")
        page = src.get("page")
        if page and (SOURCES / f"{page}.md").exists():
            errs.append(f"source: wiki/sources/{page}.md already exists -- this "
                        f"episode looks already ingested.")

    pages = plan.get("pages")
    if not isinstance(pages, list) or not pages:
        errs.append("plan: 'pages' must be a non-empty list")
        pages = []
    seen = set()
    for i, p in enumerate(pages):
        where = f"pages[{i}]"
        name = need(p, "name", where)
        bullet = need(p, "bullet", where)
        # Rule 2: every claim cites its source page. It is also load-bearing for
        # partial_write_check.py, which decides whether a dated mention belongs to
        # a known episode by resolving exactly this wikilink.
        if bullet and src.get("page") and f"[[{src['page']}]]" not in bullet:
            errs.append(f"{where}: bullet does not cite [[{src['page']}]]")
        # Anchored to the start on purpose: a bullet may legitimately mention a
        # date mid-sentence when cross-referencing an earlier take. What is wrong
        # is the agent formatting its own bullet prefix.
        if bullet and re.match(r"\s*(-\s*)?\d{4}-\d{2}-\d{2}\s*[—-]", bullet):
            errs.append(f"{where}: bullet carries its own date prefix; the applier "
                        f"stamps {ep.get('pub_date')} and orders it")
        elif bullet and bullet.lstrip().startswith("- "):
            errs.append(f"{where}: bullet must not start with '- '")
        kind = p.get("kind")
        if kind not in VALID_KINDS:
            errs.append(f"{where}: kind {kind!r} not in {VALID_KINDS}")
            continue
        if not name:
            continue
        if (kind, name) in seen:
            errs.append(f"{where}: duplicate entry for {kind}/{name} -- merge the "
                        f"two bullets into one, the wiki takes one take per "
                        f"episode per page")
        seen.add((kind, name))
        path = wu.page_path(kind, name)
        if not path.exists():
            fm = p.get("frontmatter") or {}
            missing = [k for k in wu.KIND_REQUIRED.get(kind, ()) if not fm.get(k)]
            if missing:
                errs.append(f"{where}: {name} is new; frontmatter {missing} required")
            if kind == "player" and fm.get("position") and fm["position"] not in POSITIONS:
                errs.append(f"{where}: position {fm['position']!r} not in {POSITIONS}")
        idx = p.get("index")
        if idx and len(idx.split()) > wu.MAX_INDEX_WORDS:
            errs.append(f"{where}: index summary is {len(idx.split())} words, "
                        f"limit {wu.MAX_INDEX_WORDS}")

    for i, e in enumerate(plan.get("experts") or []):
        name = (e or {}).get("name")
        if not name:
            errs.append(f"experts[{i}]: missing 'name'")
        elif not (REPO / "wiki" / "experts" / f"{name}.md").exists():
            errs.append(f"experts[{i}]: no expert page for {name!r}")

    need(plan, "log", "plan")
    return errs, ep


def build_source_page(plan, ep):
    src = plan["source"]
    date = ep.get("pub_date", "")
    raw = ep.get("staged_path", "")
    fm = ["---", "type: source", f"expert: {src['expert']}", f"show: {src['show']}",
          f'episode: "{src["episode"]}"', f"date: {date}", f"guid: {plan['guid']}",
          f"raw: {raw}", "tags: [source]", "---", ""]
    return "\n".join(fm) + "\n" + src["body"].strip() + "\n"


def apply(plan, ep):
    guid = plan["guid"]
    src = plan["source"]
    date = ep["pub_date"]

    path = SOURCES / f"{src['page']}.md"
    path.write_text(build_source_page(plan, ep), encoding="utf-8")
    print(f"source: wrote {path.relative_to(REPO)}")

    created = updated = 0
    for p in plan["pages"]:
        was_new = wu.page_append(p["kind"], p["name"], date, p["bullet"],
                                 p.get("frontmatter"), p.get("related") or [])
        created += bool(was_new)
        updated += not was_new

    for p in plan["pages"]:
        if p.get("index"):
            wu.index_set(p["name"], p["index"])

    for e in plan.get("experts") or []:
        note = e.get("note") or f"*{src['show']}* — {src['episode']}"
        wu.expert_source(e["name"], src["page"], note)

    wu.catalog_row(date, src["expert"], src["episode"], src["page"])
    wu.log_append(f"## [{date}] ingest | {src['show']} — {src['episode']}\n"
                  f"{plan['log'].strip()}")

    # Finalize LAST, and in this order: setting the status makes the transcript's
    # position inconsistent with it, and --fix is what relocates it. Anything that
    # dies before here leaves the episode `fetched` and therefore recoverable.
    state_io.update_episode(guid, status="ingested")
    print(f"state: {guid} -> ingested")
    subprocess.run([sys.executable, str(REPO / "scripts" / "verify_integrity.py"),
                    "--fix"], check=False)
    return created, updated


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", type=Path)
    ap.add_argument("--dry-run", action="store_true",
                    help="validate and report; touch nothing")
    args = ap.parse_args()

    if not args.plan.exists():
        sys.exit(f"error: no plan at {args.plan}. Phase A produced nothing -- "
                 f"nothing was written, so the episode is safe to retry.")
    try:
        plan = json.loads(args.plan.read_text())
    except json.JSONDecodeError as e:
        sys.exit(f"error: {args.plan} is not valid JSON: {e}")

    for note in normalize(plan):
        print(f"normalized: {note}")
    errs, ep = validate(plan)
    if errs:
        print(f"plan REJECTED -- {len(errs)} problem(s), nothing written:\n")
        for e in errs:
            print(f"  - {e}")
        return 2

    n = len(plan["pages"])
    if args.dry_run:
        print(f"plan OK: {n} page(s), source {plan['source']['page']!r}, "
              f"{len(plan.get('experts') or [])} expert update(s), "
              f"{sum(1 for p in plan['pages'] if p.get('index'))} index line(s).")
        return 0

    created, updated = apply(plan, ep)
    print(f"\napplied: {created} page(s) created, {updated} updated, "
          f"source + catalog + log + state done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
