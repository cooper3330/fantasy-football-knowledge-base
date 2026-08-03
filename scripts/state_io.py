#!/usr/bin/env python3
"""
Concurrency-safe read/modify/write for scripts/state.json.

Why this exists: the transcript drain and wiki ingestion both mutate state.json
and can run at the same time. The drain holds state in memory for hours while
writing the whole file after every episode, so without coordination its stale
copy silently reverts whatever ingestion did in the meantime -- reverting an
`ingested` episode to `fetched` and causing it to be re-ingested.

Every writer must go through update_episode(), which takes an exclusive file
lock, re-reads from disk, applies only its own change, and writes atomically.

CLI (for ingest agents, which shouldn't hand-edit the JSON):

  # mark ingested and record the new location, in one locked operation
  python3 scripts/state_io.py --guid "<guid>" --status ingested \\
      --staged-path raw/ingested/rsp-cast/<file>.md

  python3 scripts/state_io.py --show "<guid>"
"""

import argparse
import fcntl
import json
import os
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE_PATH = REPO / "scripts" / "state.json"
LOCK_PATH = REPO / "scripts" / ".state.lock"


class _Lock:
    """Exclusive advisory lock held across a read/modify/write cycle."""

    def __init__(self, timeout=120):
        self.timeout = timeout
        self.fh = None

    def __enter__(self):
        self.fh = open(LOCK_PATH, "w")
        import time
        deadline = time.time() + self.timeout
        while True:
            try:
                fcntl.flock(self.fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except BlockingIOError:
                if time.time() > deadline:
                    raise TimeoutError(
                        f"could not acquire state lock within {self.timeout}s; "
                        "another writer may be stuck")
                time.sleep(0.2)

    def __exit__(self, *exc):
        fcntl.flock(self.fh, fcntl.LOCK_UN)
        self.fh.close()


def _read():
    return json.loads(STATE_PATH.read_text())


def _write_atomic(state):
    """Write via temp file + rename so a crash can't leave truncated JSON."""
    payload = json.dumps(state, indent=2, sort_keys=True) + "\n"
    fd, tmp = tempfile.mkstemp(dir=str(STATE_PATH.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(payload)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, STATE_PATH)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def update_episode(_guid, **fields):
    """Apply `fields` to one episode under an exclusive lock.

    Re-reads from disk inside the lock, so a caller holding a stale copy of the
    rest of state.json cannot clobber another process's concurrent changes.
    """
    with _Lock():
        state = _read()
        eps = state.setdefault("episodes", {})
        if _guid not in eps:
            raise KeyError(f"guid not found in state: {_guid}")
        # The positional parameter is named `_guid` (not `guid`) on purpose:
        # callers commonly splat a whole episode dict, which carries its own
        # 'guid' key. A parameter named `guid` would collide at call time --
        # before the function body could strip it.
        fields.pop("guid", None)
        eps[_guid].update({k: v for k, v in fields.items() if v is not None})
        _write_atomic(state)
        return eps[_guid]


def read_state():
    """Consistent snapshot for readers."""
    with _Lock():
        return _read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guid", required=True)
    ap.add_argument("--status", choices=["pending", "fetched", "ingested"])
    ap.add_argument("--staged-path")
    ap.add_argument("--show", action="store_true", help="print the episode and exit")
    args = ap.parse_args()

    if args.show:
        ep = read_state()["episodes"].get(args.guid)
        print(json.dumps(ep, indent=2) if ep else f"not found: {args.guid}")
        return 0

    if not args.status and not args.staged_path:
        print("nothing to change; pass --status and/or --staged-path", file=sys.stderr)
        return 1

    ep = update_episode(args.guid, status=args.status, staged_path=args.staged_path)
    print(f"updated: {ep.get('title','?')[:60]}")
    print(f"  status={ep.get('status')}  staged_path={ep.get('staged_path')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
