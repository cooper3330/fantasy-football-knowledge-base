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
    ("duplicate page entries", good_plan(pages=[
        {"name": "Existing", "kind": "player", "bullet": "one ([[Test Source - 2024-05-01]])"},
        {"name": "Existing", "kind": "player", "bullet": "two ([[Test Source - 2024-05-01]])"}])),
    ("untracked expert", good_plan(experts=[{"name": "Bob Harris"}])),
    ("bad kind", good_plan(pages=[{"name": "X", "kind": "team", "bullet": "t ([[Test Source - 2024-05-01]])"}])),
    ("empty pages list", good_plan(pages=[])),
    ("no_content with non-empty pages", good_plan(no_content=True)),
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

# --- over-long index line is trimmed, not rejected --------------------------
build()
long_idx = good_plan(pages=[
    {"name": "Existing", "kind": "player",
     "bullet": "According to [[Matt Waldman]] ([[Test Source - 2024-05-01]]): x",
     "index": "WR, KC — " + " ".join(["word"] * 30) + " (2024 takes, stale)"}])
r = run(long_idx)
check("over-long index line applies (trimmed, not rejected)", r.returncode == 0,
      f"rc={r.returncode}\n{r.stdout}{r.stderr}")
import re as _re
idxline = [l for l in (ROOT / "index.md").read_text().split("\n") if "[[Existing]]" in l]
if idxline:
    summ = idxline[0].split("]]", 1)[1].lstrip(" —-")
    check("trimmed index within word cap", len(summ.split()) <= 25, f"{len(summ.split())}: {summ}")
    check("staleness parenthetical preserved through trim", "(2024 takes, stale)" in idxline[0], idxline[0])
else:
    check("trimmed index line present", False, "no [[Existing]] index line")

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

# --- no-content (promo/administrative) episode ------------------------------
# A subscriber reminder / "no show today" clip: empty pages, no_content flag.
# Records only the source page + catalog + log + state; writes no player pages,
# no index lines, no expert-source entries.
build()
idx_before = (ROOT / "index.md").read_text()
r = run(good_plan(no_content=True, pages=[], experts=[]))
check("no_content plan applies", r.returncode == 0, f"rc={r.returncode}\n{r.stdout}{r.stderr}")
check("no_content wrote the source page",
      (ROOT / "wiki" / "sources" / "Test Source - 2024-05-01.md").exists())
check("no_content created no new player page",
      not (ROOT / "wiki" / "players" / "Fresh.md").exists())
check("no_content left index.md untouched",
      (ROOT / "index.md").read_text() == idx_before)
check("no_content still catalogs the episode",
      f"| {DATE} |" in (ROOT / "wiki" / "sources" / "SOURCE_CATALOG.md").read_text())
check("no_content still logs the episode",
      f"## [{DATE}] ingest |" in (ROOT / "log.md").read_text())
stnc = json.loads((ROOT / "scripts" / "state.json").read_text())
check("no_content finalized state to ingested",
      stnc["episodes"][GUID]["status"] == "ingested")

# --- aliases: a plan that uses an alias must land on the canonical page -------
# Regression for the Lane / Meyers / Brissett splits: an agent heard "Jacoby
# Brissette", the page existed as "Jacoby Brissett", and a second page was created
# beside it. `aliases:` in frontmatter is the wiki's record of which spellings are
# one page; the applier must honour it. Here "Existing" carries two aliases.
SRC = "[[Test Source - 2024-05-01]]"


def alias_vault():
    build()
    ex = ROOT / "wiki" / "players" / "Existing.md"
    ex.write_text(ex.read_text().replace("tags: [player]\n---",
                                         "aliases: [Existng, Existing Guy]\ntags: [player]\n---", 1))
    (ROOT / "wiki" / "concepts" / "Real Concept.md").write_text(
        "---\ntype: concept\naliases: [Concept Alias]\ntags: [concept]\n---\n\n"
        "# Real Concept\n\n## Expert Takes\n- \n\n## Related\n")
    return ex


def one_page_plan(name, bullet, **extra):
    page = {"name": name, "kind": "player", "bullet": bullet, **extra}
    return good_plan(pages=[page], experts=[])


ex = alias_vault()
r = run(one_page_plan("Existng", f"According to [[Matt Waldman]] ({SRC}): via alias"))
check("alias page name applies", r.returncode == 0, f"rc={r.returncode}\n{r.stdout}{r.stderr}")
check("alias page name reported as normalized",
      "'Existng' is an alias of 'Existing'" in r.stdout, r.stdout)
check("take landed on the canonical page", "via alias" in ex.read_text())
check("no page created under the alias spelling",
      not (ROOT / "wiki" / "players" / "Existng.md").exists())

alias_vault()
r = run(one_page_plan("Existing", f"According to [[Matt Waldman]] ({SRC}): beat [[Existing Guy]] and [[Existing Guy|him]]"))
body = ex.read_text()
check("[[alias]] link rewritten to canonical", "beat [[Existing]] and [[Existing|him]]" in body, body)
check("link rewrite keeps the |display text", "[[Existing|him]]" in body)
check("no link to the alias spelling survives", "[[Existing Guy" not in body)

alias_vault()
r = run(one_page_plan("Existing", f"According to [[Matt Waldman]] ({SRC}): people call him Existng and Existing Guy"))
check("alias in PROSE is left exactly as the expert said it",
      "people call him Existng and Existing Guy" in ex.read_text())

alias_vault()
r = run(one_page_plan("Existing", f"According to [[Matt Waldman]] ({SRC}): x", related=["Concept Alias"]))
check("related alias resolves to the canonical concept",
      "[[Real Concept]]" in ex.read_text() and "[[Concept Alias]]" not in ex.read_text(), ex.read_text())

alias_vault()
before = snapshot()
r = run(good_plan(pages=[
    {"name": "Existing", "kind": "player", "bullet": f"one ({SRC})"},
    {"name": "Existng", "kind": "player", "bullet": f"two ({SRC})"}], experts=[]))
check("alias + canonical in one plan is rejected as a duplicate",
      r.returncode == 2 and "duplicate entry" in r.stdout, f"rc={r.returncode}\n{r.stdout}")
check("...and the rejected plan left the vault untouched", snapshot() == before)

# A page that really exists under the alias's spelling must NOT be redirected.
alias_vault()
(ROOT / "wiki" / "players" / "Existng.md").write_text(
    "---\ntype: player\nteam: BUF\nposition: WR\ntags: [player]\n---\n\n# Existng\n\n"
    "## Expert Takes\n- 2024-01-01 — a different player\n\n## Related Concepts\n")
r = run(one_page_plan("Existng", f"According to [[Matt Waldman]] ({SRC}): stays put"))
check("an existing page named like an alias is never redirected",
      "stays put" in (ROOT / "wiki" / "players" / "Existng.md").read_text()
      and "stays put" not in ex.read_text(), r.stdout)

# A genuinely new name is untouched by the alias machinery.
alias_vault()
r = run(one_page_plan("Brand New", f"According to [[Matt Waldman]] ({SRC}): first",
                      frontmatter={"team": "BUF", "position": "WR"}))
check("a name that is not an alias is created as before",
      r.returncode == 0 and (ROOT / "wiki" / "players" / "Brand New.md").exists(), r.stdout)

shutil.rmtree(ROOT, ignore_errors=True)
print(f"\n{'FAILED' if fails else 'all passed'} ({fails} failure(s))")
sys.exit(1 if fails else 0)
