#!/usr/bin/env python3
"""Regression test for scripts/partial_write_check.py against a synthetic vault.

Covers the three cases that have actually bitten:
  A. true positive, agent died BEFORE writing its source page
  B. true positive, agent died AFTER writing its source page (the miss)
  C. false positive shape: another show published the same day (the cry-wolf)
"""
import json
import tempfile
import shutil
import subprocess
import sys
from pathlib import Path

SRC = Path("/Users/kylecooper/dev/fantasy-football-knowledge-base/scripts/partial_write_check.py")
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp(prefix="pwtest-"))

OURS = "guid-ours"
THEIRS = "guid-theirs"
DATE = "2024-04-11"


def build(case):
    if ROOT.exists():
        shutil.rmtree(ROOT)
    (ROOT / "scripts").mkdir(parents=True)
    (ROOT / "wiki" / "sources").mkdir(parents=True)
    for d in ("players", "concepts", "formats", "experts"):
        (ROOT / "wiki" / d).mkdir(parents=True)
    shutil.copy(SRC, ROOT / "scripts" / "partial_write_check.py")

    state = {"episodes": {
        OURS:   {"guid": OURS,   "status": "fetched",  "pub_date": DATE, "title": "Ours"},
        THEIRS: {"guid": THEIRS, "status": "ingested", "pub_date": DATE, "title": "Theirs"},
    }}
    (ROOT / "scripts" / "state.json").write_text(json.dumps(state))

    def source(name, guid):
        (ROOT / "wiki" / "sources" / f"{name}.md").write_text(
            f"---\ntype: source\nguid: {guid}\ndate: {DATE}\ntags: [source]\n---\n# {name}\n")

    if case == "A":            # bullets, no source page yet
        (ROOT / "wiki" / "players" / "P.md").write_text(
            f"# P\n- {DATE} - According to [[X]] on [[Ours - {DATE}]]: take.\n")
    elif case == "B":          # bullets AND source page
        source(f"Ours - {DATE}", OURS)
        (ROOT / "wiki" / "players" / "P.md").write_text(
            f"# P\n- {DATE} - According to [[X]] on [[Ours - {DATE}]]: take.\n")
    elif case == "C":          # other show same day, incl. both brittle shapes
        source(f"Theirs - {DATE}", THEIRS)
        (ROOT / "wiki" / "players" / "P.md").write_text(
            f"# P\n## A case ({DATE})\n"
            f"- **Open {DATE} read:** see [[SomePlayer]]\n"
            f"- {DATE} - per [[Theirs - {DATE}]]: take.\n")
    elif case == "D":          # nothing written at all
        source(f"Theirs - {DATE}", THEIRS)


EXPECT = {"A": 2, "B": 2, "C": 0, "D": 0}
fails = 0
for case, want in EXPECT.items():
    build(case)
    r = subprocess.run(["/usr/bin/python3", str(ROOT / "scripts" / "partial_write_check.py"),
                        "--guid", OURS], capture_output=True, text=True)
    ok = r.returncode == want
    fails += not ok
    label = {2: "PARTIAL", 0: "clean"}
    print(f"{'ok  ' if ok else 'FAIL'} case {case}: want {label[want]:8} got {label.get(r.returncode, r.returncode)}")
    if not ok and r.stdout:
        print("     " + r.stdout.strip().replace("\n", "\n     "))
shutil.rmtree(ROOT, ignore_errors=True)
sys.exit(1 if fails else 0)
