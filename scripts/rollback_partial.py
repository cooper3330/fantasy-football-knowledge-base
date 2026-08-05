#!/usr/bin/env python3
"""
Undo the writes an ingest agent left behind when it died before finalizing.

Run this when scripts/partial_write_check.py reports a partial write. Dry-run by
default; pass --apply to execute.

  python3 scripts/rollback_partial.py --guid '<guid>'
  python3 scripts/rollback_partial.py --guid '<guid>' --apply

What it does, per page the checker attributes to the episode:

  - the episode's own source page          -> delete
  - a page created solely by this episode  -> delete
    ("solely" = untracked at HEAD, and every dated bullet on it is this
    episode's date; a page an earlier episode created and this one merely
    appended to is stripped, not deleted)
  - anything else                          -> strip the lines citing the date

Lines that are not dated bullets are reported for review rather than removed --
a stripped section heading can orphan the prose beneath it, and that judgement
is not one to automate.

state.json is left alone on purpose: it already says `fetched`, which is correct
once the writes are gone, and the episode goes back to the head of the queue.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from partial_write_check import REPO, analyze  # noqa: E402

BULLET = re.compile(r"^\s*-\s*(\d{4}-\d{2}-\d{2})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guid", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    r = analyze(args.guid)
    if r is None:
        print(f"{args.guid}: not a `fetched` episode -- nothing to roll back.")
        return 0
    pdate = r["pdate"]
    if not r["ours"] and not r["unaccounted"]:
        print(f"{args.guid} ({pdate}): clean, nothing to roll back.")
        return 0

    tracked = set(subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, check=True).stdout.splitlines())

    delete = [(p, "source page for this episode") for p in r["ours"]]
    strip, review = [], []
    for p, lines in r["unaccounted"]:
        text = p.read_text(errors="ignore")
        rel = str(p.relative_to(REPO))
        dates = [m.group(1) for m in (BULLET.match(l) for l in text.splitlines()) if m]
        citing = [l for l in text.splitlines() if pdate in l]
        non_bullet = [l for l in citing if not BULLET.match(l)]
        if dates and set(dates) == {pdate} and rel not in tracked:
            delete.append((p, f"untracked, all {len(dates)} bullet(s) from this episode"))
            continue
        strip.append((p, len(citing), len(dates) - len([d for d in dates if d == pdate])))
        if non_bullet:
            review.append((p, non_bullet))

    print(f"{'APPLYING' if args.apply else 'DRY RUN'} -- rollback of {args.guid} ({pdate})\n")
    print(f"DELETE ({len(delete)}):")
    for p, why in delete:
        print(f"  {p.relative_to(REPO)}  [{why}]")
    print(f"\nSTRIP ({len(strip)}):")
    for p, n, keep in strip:
        print(f"  {p.relative_to(REPO)}  -{n} line(s), {keep} dated bullet(s) retained")
    if review:
        print(f"\nNOT DATED BULLETS -- review these by hand ({len(review)} page(s)):")
        for p, lines in review:
            for l in lines[:3]:
                print(f"  {p.relative_to(REPO)}: {l.strip()[:110]}")

    if not args.apply:
        print("\nre-run with --apply to execute")
        return 0

    for p, _ in delete:
        p.unlink()
    for p, _, _ in strip:
        kept = [l for l in p.read_text(errors="ignore").splitlines(keepends=True)
                if pdate not in l]
        p.write_text("".join(kept))
    print(f"\ndone: {len(delete)} deleted, {len(strip)} stripped")
    print("re-run scripts/partial_write_check.py to confirm clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
