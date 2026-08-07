#!/usr/bin/env python3
"""
Tests for wiki_update.py --page-append / --expert-source against a synthetic
vault. Ordering is the whole point of these: rule 4 (chronological Expert Takes)
used to depend on an agent reading the page and choosing a spot, and moving that
into code is only an improvement if the code actually gets it right -- including
the out-of-order case, which is the one a human reviewer would never notice.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent / "wiki_update.py"
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp(prefix="wutest-"))
fails = 0


def build():
    if ROOT.exists():
        shutil.rmtree(ROOT)
    (ROOT / "scripts").mkdir(parents=True)
    for d in ("players", "concepts", "experts", "sources", "_templates", "formats"):
        (ROOT / "wiki" / d).mkdir(parents=True)
    shutil.copy(SRC, ROOT / "scripts" / "wiki_update.py")
    (ROOT / "index.md").write_text("---\ntype: index\ntags: [index]\n---\n\n### Wide Receivers\n")
    (ROOT / "log.md").write_text("---\ntype: log\ntags: [log]\n---\n")
    (ROOT / "wiki" / "_templates" / "player.md").write_text(
        "---\ntype: player\nteam: \nposition: \ntags: [player]\n---\n\n"
        "# {{Player Name}}\n\n## Expert Takes\n<!-- comment -->\n- \n\n## Related Concepts\n\n")
    (ROOT / "wiki" / "_templates" / "concept.md").write_text(
        "---\ntype: concept\ntags: [concept]\n---\n\n# {{Concept Name}}\n\n"
        "## Definition\n\n## Expert Takes\n- \n\n## Related\n")
    # existing player page with two takes
    (ROOT / "wiki" / "players" / "Existing.md").write_text(
        "---\ntype: player\nteam: KC\nposition: WR\ntags: [player]\n---\n\n"
        "# Existing\n\n## Expert Takes\n\n"
        "- 2024-01-01 — oldest take\n"
        "- 2024-06-01 — newest take\n\n"
        "## Related Concepts\n- [[Already There]]\n")
    # concept page using dated ### subsections
    (ROOT / "wiki" / "concepts" / "Sub.md").write_text(
        "---\ntype: concept\ntags: [concept]\n---\n\n# Sub\n\n## Expert Takes\n\n"
        "### First case (2024-01-05)\nprose\n\n"
        "### Later case (2024-07-05)\nprose\n\n## Related\n")
    (ROOT / "wiki" / "experts" / "Matt Waldman.md").write_text(
        "---\ntype: expert\noutlet: RSP\ntags: [expert]\n---\n\n# Matt Waldman\n\n"
        "## Sources\n- [[Old Source]] — older\n")


def run(*args, expect=0):
    r = subprocess.run(["/usr/bin/python3", str(ROOT / "scripts" / "wiki_update.py"), *args],
                       capture_output=True, text=True)
    if r.returncode != expect:
        print(f"     cmd exited {r.returncode} (wanted {expect}): {r.stdout}{r.stderr}")
    return r


def check(label, cond, extra=""):
    global fails
    fails += not cond
    print(f"{'ok  ' if cond else 'FAIL'} {label}")
    if not cond and extra:
        print("     " + extra.replace("\n", "\n     "))


def takes(page, sub="players"):
    t = (ROOT / "wiki" / sub / f"{page}.md").read_text()
    body = t.split("## Expert Takes", 1)[1].split("\n## ", 1)[0]
    return [l for l in body.split("\n") if l.startswith("- ") or l.startswith("### ")]


build()

# --- ordering -------------------------------------------------------------
run("--page-append", "player", "Existing", "2024-03-01", "middle take")
got = takes("Existing")
check("middle date lands between existing takes",
      [l.split(" — ")[0] for l in got] == ["- 2024-01-01", "- 2024-03-01", "- 2024-06-01"],
      "\n".join(got))

run("--page-append", "player", "Existing", "2024-09-01", "future take")
check("newest date lands last", takes("Existing")[-1].startswith("- 2024-09-01"),
      "\n".join(takes("Existing")))

run("--page-append", "player", "Existing", "2023-01-01", "ancient take")
check("oldest date lands first", takes("Existing")[0].startswith("- 2023-01-01"),
      "\n".join(takes("Existing")))

# --- idempotency ----------------------------------------------------------
before = (ROOT / "wiki" / "players" / "Existing.md").read_text()
run("--page-append", "player", "Existing", "2024-03-01", "middle take")
check("identical bullet is a no-op",
      before == (ROOT / "wiki" / "players" / "Existing.md").read_text())

# --- creation -------------------------------------------------------------
run("--page-append", "player", "Fresh", "2024-05-05", "first take",
    "--frontmatter", json.dumps({"team": "BUF", "position": "WR"}),
    "--related", "Some Concept")
fresh = (ROOT / "wiki" / "players" / "Fresh.md").read_text()
check("new page gets frontmatter", "team: BUF" in fresh and "position: WR" in fresh, fresh)
check("new page titled correctly", "# Fresh" in fresh)
check("template placeholder bullet removed", "\n- \n" not in fresh, fresh)
check("new page has its bullet", "- 2024-05-05 — first take" in fresh)
check("related link added", "- [[Some Concept]]" in fresh)

r = run("--page-append", "player", "NoFm", "2024-05-05", "take", expect=1)
check("new player page without frontmatter is refused",
      not (ROOT / "wiki" / "players" / "NoFm.md").exists() and "required" in r.stdout + r.stderr)

# --- list frontmatter renders as YAML, not Python repr ---------------------
run("--page-append", "concept", "Tagged", "2024-05-05", "take",
    "--frontmatter", json.dumps({"tags": ["concept", "scheme", "alignment"]}))
tagged = (ROOT / "wiki" / "concepts" / "Tagged.md").read_text()
check("list frontmatter emits a YAML flow sequence",
      "tags: [concept, scheme, alignment]" in tagged, tagged.split("---")[1])
check("no Python repr quotes in frontmatter", "'" not in tagged.split("---")[1], tagged)

# --- related dedup --------------------------------------------------------
run("--page-append", "player", "Existing", "2024-04-04", "take", "--related", "Already There")
check("related link not duplicated",
      (ROOT / "wiki" / "players" / "Existing.md").read_text().count("[[Already There]]") == 1)

# --- concept pages with dated subsections ---------------------------------
run("--page-append", "concept", "Sub", "2024-04-01", "between the subsections")
got = takes("Sub", "concepts")
check("bullet ordered against dated ### anchors",
      got == ["### First case (2024-01-05)", "- 2024-04-01 — between the subsections",
              "### Later case (2024-07-05)"], "\n".join(got))

# --- expert sources are newest-first --------------------------------------
run("--expert-source", "Matt Waldman", "New Source", "newer")
lines = [l for l in (ROOT / "wiki" / "experts" / "Matt Waldman.md").read_text().split("\n")
         if l.startswith("- [[")]
check("expert source prepended (section is newest-first)",
      lines[0].startswith("- [[New Source]]"), "\n".join(lines))
r = run("--expert-source", "Nobody", "S", "n", expect=1)
check("unknown expert refused", "Tracked experts only" in r.stdout + r.stderr)

shutil.rmtree(ROOT, ignore_errors=True)
print(f"\n{'FAILED' if fails else 'all passed'} ({fails} failure(s))")
sys.exit(1 if fails else 0)
