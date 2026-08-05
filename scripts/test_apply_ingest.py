#!/usr/bin/env python3
"""
Tests for apply_ingest.py against a synthetic vault.

The property that matters most here is VALIDATE-THEN-WRITE: a rejected plan must
leave the vault byte-for-byte unchanged. Ingest v2 moves the whole write phase
behind one script, so a partial application would be exactly the failure this
pipeline has already been bitten by twice -- except caused by our own code
instead of a dying agent. Every rejection case below asserts a clean tree, not
just a non-zero exit.
"""
import json
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp(prefix="aitest-"))
GUID = "test-guid-1"
DATE = "2024-05-01"
fails = 0


def build():
    if ROOT.exists():
        shutil.rmtree(ROOT)
    (ROOT / "scripts").mkdir(parents=True)
    for d in ("players", "concepts", "experts", "sources", "formats", "_templates"):
        (ROOT / "wiki" / d).mkdir(parents=True)
    (ROOT / "raw" / "transcripts" / "rsp-cast").mkdir(parents=True)
    (ROOT / "raw" / "ingested" / "rsp-cast").mkdir(parents=True)
    for s in ("apply_ingest.py", "wiki_update.py", "state_io.py", "verify_integrity.py"):
        shutil.copy(SCRIPTS / s, ROOT / "scripts" / s)

    tr = "raw/transcripts/rsp-cast/2024-05-01-test.md"
    (ROOT / tr).write_text("transcript body")
    (ROOT / "scripts" / "state.json").write_text(json.dumps({"episodes": {
        GUID: {"guid": GUID, "status": "fetched", "pub_date": DATE,
               "title": "Test Episode", "show": "rsp-cast", "staged_path": tr},
        "done-guid": {"guid": "done-guid", "status": "ingested", "pub_date": DATE,
                      "title": "Done", "show": "rsp-cast", "staged_path": tr},
    }}))
    (ROOT / "wiki" / "_templates" / "player.md").write_text(
        "---\ntype: player\nteam: \nposition: \ntags: [player]\n---\n\n"
        "# {{Player Name}}\n\n## Expert Takes\n- \n\n## Related Concepts\n\n")
    (ROOT / "wiki" / "_templates" / "concept.md").write_text(
        "---\ntype: concept\ntags: [concept]\n---\n\n# {{Concept Name}}\n\n"
        "## Definition\n\n## Expert Takes\n- \n\n## Related\n")
    (ROOT / "wiki" / "experts" / "Matt Waldman.md").write_text(
        "---\ntype: expert\noutlet: RSP\ntags: [expert]\n---\n\n# Matt Waldman\n\n"
        "## Sources\n- [[Old]] — older\n")
    (ROOT / "wiki" / "players" / "Existing.md").write_text(
        "---\ntype: player\nteam: KC\nposition: WR\ntags: [player]\n---\n\n"
        "# Existing\n\n## Expert Takes\n- 2024-01-01 — old take\n\n## Related Concepts\n")
    (ROOT / "index.md").write_text(
        "---\ntype: index\ntags: [index]\n---\n\n## Players\n### Wide Receivers\n\n## Concepts\n")
    (ROOT / "log.md").write_text("---\ntype: log\ntags: [log]\n---\n")
    (ROOT / "wiki" / "sources" / "SOURCE_CATALOG.md").write_text(
        "---\ntype: catalog\ntags: [catalog]\n---\n\n| Date | Expert | Episode | Page |\n"
        "|---|---|---|---|\n| 2024-01-01 | [[Matt Waldman]] | Old | [[Old]] |\n")


def good_plan(**over):
    p = {
        "guid": GUID,
        "source": {"page": "Test Source - 2024-05-01", "expert": "Matt Waldman",
                   "show": "Matt Waldman's RSP Cast", "episode": "Test Episode",
                   "body": "## Summary\nStuff happened.\n"},
        "pages": [
            {"name": "Existing", "kind": "player", "bullet": "According to [[Matt Waldman]] ([[Test Source - 2024-05-01]]): a new take",
             "index": "WR, KC — headline view"},
            {"name": "Fresh", "kind": "player", "bullet": "According to [[Matt Waldman]] ([[Test Source - 2024-05-01]]): first take",
             "frontmatter": {"team": "BUF", "position": "WR"},
             "related": ["Some Concept"]},
        ],
        "experts": [{"name": "Matt Waldman", "note": "test episode"}],
        "log": "What changed.",
    }
    p.update(over)
    return p


def snapshot():
    h = {}
    for p in sorted(ROOT.rglob("*")):
        # plan.json is written by run() after the baseline is taken, and the lock
        # file is scratch -- neither is vault content.
        if p.is_file() and p.name not in (".state.lock", "plan.json"):
            h[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return h


def run(plan, *extra):
    (ROOT / "plan.json").write_text(json.dumps(plan))
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "apply_ingest.py"),
         str(ROOT / "plan.json"), *extra], capture_output=True, text=True)


def check(label, cond, extra=""):
    global fails
    fails += not cond
    print(f"{'ok  ' if cond else 'FAIL'} {label}")
    if not cond and extra:
        print("     " + str(extra)[:500].replace("\n", "\n     "))


# --- rejection cases: must exit 2 AND leave the tree untouched --------------
REJECT = [
    ("unknown guid", good_plan(guid="nope")),
    ("already-ingested episode", good_plan(guid="done-guid")),
    ("new page missing frontmatter", good_plan(pages=[
        {"name": "NoFm", "kind": "player", "bullet": "take ([[Test Source - 2024-05-01]])"}])),
    ("bad position", good_plan(pages=[
        {"name": "BadPos", "kind": "player", "bullet": "t ([[Test Source - 2024-05-01]])",
         "frontmatter": {"team": "KC", "position": "FB"}}])),
    ("over-long index line", good_plan(pages=[
        {"name": "Existing", "kind": "player", "bullet": "t ([[Test Source - 2024-05-01]])",
         "index": " ".join(["word"] * 26)}])),
    ("duplicate page entries", good_plan(pages=[
        {"name": "Existing", "kind": "player", "bullet": "one ([[Test Source - 2024-05-01]])"},
        {"name": "Existing", "kind": "player", "bullet": "two ([[Test Source - 2024-05-01]])"}])),
    ("untracked expert", good_plan(experts=[{"name": "Bob Harris"}])),
    ("bad kind", good_plan(pages=[{"name": "X", "kind": "team", "bullet": "t ([[Test Source - 2024-05-01]])"}])),
    ("empty pages list", good_plan(pages=[])),
    ("missing log", good_plan(log="")),
    ("bullet without source citation", good_plan(pages=[
        {"name": "Existing", "kind": "player", "bullet": "uncited take"}])),
    ("bullet with its own date prefix", good_plan(pages=[
        {"name": "Existing", "kind": "player",
         "bullet": "2024-05-01 — According to [[Matt Waldman]] ([[Test Source - 2024-05-01]]): x"}])),
]
for label, plan in REJECT:
    build()
    before = snapshot()
    r = run(plan)
    check(f"reject: {label}",
          r.returncode == 2 and snapshot() == before,
          f"rc={r.returncode}\n{r.stdout}{r.stderr}")

# --- source page name normalization ----------------------------------------
build()
colon = good_plan()
colon["source"]["page"] = "Test: Source - 2024-05-01"
for pg in colon["pages"]:
    pg["bullet"] = pg["bullet"].replace("[[Test Source - 2024-05-01]]",
                                        "[[Test: Source - 2024-05-01]]")
r = run(colon)
check("colon stripped from source page name",
      r.returncode == 0 and (ROOT / "wiki" / "sources" / "Test Source - 2024-05-01.md").exists(),
      f"rc={r.returncode}\n{r.stdout}{r.stderr}")
check("citations rewritten to the normalized name",
      "[[Test Source - 2024-05-01]]" in (ROOT / "wiki" / "players" / "Existing.md").read_text()
      and "[[Test:" not in (ROOT / "wiki" / "players" / "Existing.md").read_text())

# --- dry run writes nothing -------------------------------------------------
build()
before = snapshot()
r = run(good_plan(), "--dry-run")
check("dry-run validates without writing",
      r.returncode == 0 and snapshot() == before and "plan OK" in r.stdout,
      f"rc={r.returncode}\n{r.stdout}{r.stderr}")

# --- happy path -------------------------------------------------------------
build()
r = run(good_plan())
check("valid plan applies", r.returncode == 0, f"rc={r.returncode}\n{r.stdout}{r.stderr}")

src = ROOT / "wiki" / "sources" / "Test Source - 2024-05-01.md"
check("source page written", src.exists())
if src.exists():
    t = src.read_text()
    check("source frontmatter carries guid + raw + date",
          f"guid: {GUID}" in t and "raw: raw/" in t and f"date: {DATE}" in t, t[:300])

existing = (ROOT / "wiki" / "players" / "Existing.md").read_text()
check("bullet appended with script-stamped date",
      f"- {DATE} — According to [[Matt Waldman]] ([[Test Source - 2024-05-01]]): a new take" in existing, existing)
check("bullet ordered after the older one",
      existing.index("2024-01-01") < existing.index(DATE))

fresh = ROOT / "wiki" / "players" / "Fresh.md"
check("new page created from template", fresh.exists())
if fresh.exists():
    check("new page frontmatter filled", "team: BUF" in fresh.read_text())

check("index line added", "[[Existing]] — WR, KC — headline view" in (ROOT / "index.md").read_text(),
      (ROOT / "index.md").read_text())
check("no index line for page that omitted one",
      "[[Fresh]]" not in (ROOT / "index.md").read_text())
check("catalog row added",
      f"| {DATE} |" in (ROOT / "wiki" / "sources" / "SOURCE_CATALOG.md").read_text())
log = (ROOT / "log.md").read_text()
check("log entry has derived header + body",
      f"## [{DATE}] ingest | Matt Waldman's RSP Cast — Test Episode" in log
      and "What changed." in log, log)
check("expert source prepended",
      (ROOT / "wiki" / "experts" / "Matt Waldman.md").read_text()
      .split("## Sources\n")[1].startswith("- [[Test Source"))
st = json.loads((ROOT / "scripts" / "state.json").read_text())
check("state finalized to ingested", st["episodes"][GUID]["status"] == "ingested")

# --- re-applying the same plan is refused ----------------------------------
r = run(good_plan())
check("re-applying an applied plan is refused", r.returncode == 2, r.stdout)

shutil.rmtree(ROOT, ignore_errors=True)
print(f"\n{'FAILED' if fails else 'all passed'} ({fails} failure(s))")
sys.exit(1 if fails else 0)
