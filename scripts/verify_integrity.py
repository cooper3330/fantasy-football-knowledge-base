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

Usage:
  verify_integrity.py            # report only (safe, read-only)
  verify_integrity.py --fix      # repair what can be repaired safely
"""

import argparse
import json
import sys
from collections import defaultdict
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

    # 2. orphans on disk
    for name, p in on_disk.items():
        if name not in referenced:
            problems.append(f"ORPHAN     {p.relative_to(REPO_ROOT)} (not referenced by state)")

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
    for kind, src, dst, guid in repairs:
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
