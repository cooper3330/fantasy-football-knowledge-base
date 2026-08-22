#!/usr/bin/env python3
"""
Reconciles scripts/state.json against what is actually on disk under raw/.

Transcripts physically move from raw/transcripts/<show>/ to raw/ingested/<show>/
when they are ingested. Any move is a chance for state and disk to drift -- this
script detects that drift and can repair the recoverable cases.

Checks:
  1. Every fetched/ingested episode in state has a transcript file on disk.
  2. Every transcript file on disk is referenced by state.
  3. Files are in the folder their status implies:
       status 'fetched'  -> raw/transcripts/<show>/
       status 'ingested' -> raw/ingested/<show>/
  4. No duplicate basenames across the two trees (a half-completed move).
  5. staged_path in state matches the file's real location.

An ORPHAN transcript -- a file on disk with no state row -- is repairable when
its own frontmatter carries everything a state row needs (guid, show, expert).
That happens when the drain wrote the transcript but crashed before persisting
its state row (see scripts/state_io.py's create= note). --fix adopts such a file
back into state, deriving status from which tree it sits in. An orphan whose
frontmatter is missing or malformed is reported but not adopted -- there is
nothing safe to reconstruct the row from.

Usage:
  verify_integrity.py            # report only (safe, read-only)
  verify_integrity.py --fix      # repair what can be repaired safely
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = REPO_ROOT / "scripts" / "state.json"
PENDING_ROOT = REPO_ROOT / "raw" / "transcripts"
INGESTED_ROOT = REPO_ROOT / "raw" / "ingested"

SUBDIR = {"rp": "reception-perception", "harris": "harris-football", "rsp": "rsp-cast"}


def show_subdir_from_name(name):
    """Derive the show subdir from a date-prefixed filename's slug segment."""
    parts = name.split("-")
    if len(parts) >= 4:
        slug = parts[3]
        return SUBDIR.get(slug)
    return None


def expected_dir(status, name):
    sub = show_subdir_from_name(name)
    if sub is None:
        return None
    root = INGESTED_ROOT if status == "ingested" else PENDING_ROOT
    return root / sub


def parse_frontmatter(path):
    """Return (frontmatter dict, clean title) for a staged transcript.

    Reads only the leading YAML block and the first `# ` heading -- both written
    by check_new_episodes.stage_transcript, so an adoptable orphan always has
    them. Returns (None, None) if there is no frontmatter block to trust.
    """
    text = path.read_text(errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip()
    hm = re.search(r"^#\s+(.+)$", text[m.end():], re.M)
    title = hm.group(1).strip() if hm else fm.get("show")
    return fm, title


def orphan_state_row(path, fm, title):
    """Reconstruct the state row for an adoptable orphan, or None if it lacks
    the fields a row can't be invented without. Status comes from the tree the
    file sits in: ingested tree -> 'ingested', otherwise 'fetched'."""
    guid = fm.get("guid") if fm else None
    if not (guid and fm.get("show") and fm.get("expert")):
        return None
    status = "ingested" if INGESTED_ROOT in path.parents else "fetched"
    today = date.today().isoformat()
    return {
        "title": title,
        "show": fm["show"],
        "expert": fm["expert"],
        "pub_date": fm.get("date"),
        "guid": guid,
        "status": status,
        "transcript_source": fm.get("transcript_source"),
        "staged_path": str(path.relative_to(REPO_ROOT)),
        "first_seen": today,
        "last_checked": today,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="repair safely-repairable drift")
    args = ap.parse_args()

    state = json.loads(STATE_PATH.read_text())
    episodes = state.get("episodes", {})

    on_disk = {}
    dupes = defaultdict(list)
    for root in (PENDING_ROOT, INGESTED_ROOT):
        for p in root.rglob("*.md"):
            if p.name.startswith("_"):
                continue
            dupes[p.name].append(p)
            on_disk[p.name] = p

    problems = []
    repairs = []

    # 4. duplicate basenames across trees -> a move that half-happened
    for name, paths in dupes.items():
        if len(paths) > 1:
            problems.append(f"DUPLICATE  {name}\n           " +
                            "\n           ".join(str(p.relative_to(REPO_ROOT)) for p in paths))

    referenced = set()
    for guid, v in episodes.items():
        status = v.get("status")
        if status not in ("fetched", "ingested"):
            continue
        sp = v.get("staged_path")
        name = Path(sp).name if sp else None

        # 1. file must exist somewhere
        if not name or name not in on_disk:
            problems.append(f"MISSING    [{status}] {v.get('title','?')[:50]} -> {sp}")
            continue
        referenced.add(name)

        actual = on_disk[name]
        exp_dir = expected_dir(status, name)

        # 3. right folder for its status
        if exp_dir and actual.parent != exp_dir:
            rel_actual = actual.relative_to(REPO_ROOT)
            rel_exp = (exp_dir / name).relative_to(REPO_ROOT)
            problems.append(f"MISPLACED  [{status}] {rel_actual}\n           should be {rel_exp}")
            repairs.append(("move", actual, exp_dir / name, guid))
            continue

        # 5. staged_path accuracy
        rel = str(actual.relative_to(REPO_ROOT))
        if sp != rel:
            problems.append(f"STALE PATH [{status}] state says {sp}\n           actual     {rel}")
            repairs.append(("path", None, actual, guid))

    # 2. orphans on disk -- adopt back into state when the file's own
    #    frontmatter carries a reconstructable row; otherwise just report.
    guid_by_guid = {v.get("guid") for v in episodes.values()}
    for name, p in on_disk.items():
        if name in referenced:
            continue
        rel = p.relative_to(REPO_ROOT)
        fm, title = parse_frontmatter(p)
        row = orphan_state_row(p, fm, title) if fm else None
        if row and row["guid"] not in episodes and row["guid"] not in guid_by_guid:
            problems.append(f"ORPHAN     {rel} (no state row; adoptable -> '{row['status']}')")
            repairs.append(("adopt", None, p, row["guid"], row))
        else:
            why = "frontmatter missing/incomplete" if not row else "guid already in state"
            problems.append(f"ORPHAN     {rel} (not referenced by state; NOT adoptable — {why})")

    if not problems:
        n_p = sum(1 for v in episodes.values() if v.get("status") == "fetched")
        n_i = sum(1 for v in episodes.values() if v.get("status") == "ingested")
        print(f"OK  state and disk agree.")
        print(f"    awaiting ingestion: {n_p}   ingested: {n_i}   files on disk: {len(on_disk)}")
        return 0

    print(f"{len(problems)} problem(s) found:\n")
    for p in problems:
        print("  " + p)

    if not args.fix:
        print(f"\n{len(repairs)} of these are auto-repairable. Re-run with --fix to apply.")
        return 1

    print(f"\nApplying {len(repairs)} repair(s)...")
    for repair in repairs:
        kind = repair[0]
        if kind == "adopt":
            _, _, path, guid, row = repair
            episodes[guid] = row
            print(f"  adopt  {path.name} -> {row['status']}")
            continue
        _, src, dst, guid = repair
        if kind == "move":
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
            episodes[guid]["staged_path"] = str(dst.relative_to(REPO_ROOT))
            print(f"  moved  {src.name} -> {dst.parent.name}/")
        else:
            episodes[guid]["staged_path"] = str(dst.relative_to(REPO_ROOT))
            print(f"  path   {dst.name}")

    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    print("\nRepairs applied. Re-run without --fix to confirm.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
