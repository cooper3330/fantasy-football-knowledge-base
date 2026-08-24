#!/usr/bin/env python3
"""Tests for scripts/state_io.py -- the locked read-modify-write for state.json.

Focus: the create= flag and the invariant that every episode row carries its own
value['guid'] equal to its dict key. Both are what bug 1 (first-seen episodes
could not be inserted) and bug 2 (inserted rows had no 'guid' field, so
run_daily_check.next_guid saw an empty queue) turned on. Run directly:

    python3 scripts/test_state_io.py
"""

import importlib.util
import json
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "state_io", str(Path(__file__).resolve().parent / "state_io.py"))
state_io = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state_io)

fails = 0


def check(label, cond, extra=""):
    global fails
    print(f"{'ok  ' if cond else 'FAIL'} {label}")
    if not cond:
        fails += 1
        if extra:
            print(f"       {extra}")


def fresh(seed=None):
    """Point state_io at a throwaway state file and return its path."""
    tmp = Path(tempfile.mkdtemp())
    state_io.STATE_PATH = tmp / "state.json"
    state_io.LOCK_PATH = tmp / ".state.lock"
    state_io.STATE_PATH.write_text(json.dumps({"episodes": seed or {}}))
    return state_io.STATE_PATH


def rows(path):
    return json.loads(path.read_text())["episodes"]


# --- create=True inserts a first-seen episode (bug 1) ----------------------
p = fresh()
state_io.update_episode("G1", create=True, status="fetched", title="T")
check("create=True inserts an unknown guid", "G1" in rows(p))

# --- the inserted row carries value['guid'] == key (bug 2) -----------------
check("insert stamps value['guid'] equal to the key",
      rows(p)["G1"].get("guid") == "G1", rows(p)["G1"])

# --- create=False (default) still raises for an unknown guid ---------------
fresh()
try:
    state_io.update_episode("MISSING", status="ingested")
    check("create=False raises on unknown guid", False, "no error raised")
except KeyError:
    check("create=False raises on unknown guid", True)

# --- a plain update self-heals a row that drifted without a guid -----------
p = fresh({"G2": {"status": "fetched", "title": "old"}})  # note: no 'guid' field
check("precondition: seeded row has no guid", "guid" not in rows(p)["G2"])
state_io.update_episode("G2", status="fetched")
check("plain update self-heals the missing value['guid']",
      rows(p)["G2"].get("guid") == "G2", rows(p)["G2"])

# --- the splatted-dict guid never overwrites the key -----------------------
p = fresh()
state_io.update_episode("K", create=True, guid="WRONG", status="fetched")
check("a 'guid' passed in fields cannot override the key",
      rows(p)["K"].get("guid") == "K", rows(p)["K"])

# --- None-valued fields are ignored, not written ---------------------------
p = fresh({"G3": {"guid": "G3", "status": "fetched", "staged_path": "a.md"}})
state_io.update_episode("G3", status="ingested", staged_path=None)
row = rows(p)["G3"]
check("None fields are ignored (staged_path preserved)",
      row["status"] == "ingested" and row["staged_path"] == "a.md", row)

# --- idempotency: applying the same update twice converges -----------------
p = fresh()
state_io.update_episode("G4", create=True, status="fetched", title="T")
first = dict(rows(p)["G4"])
state_io.update_episode("G4", create=True, status="fetched", title="T")
check("repeated identical update is idempotent", rows(p)["G4"] == first)

print(f"\n{'FAILED' if fails else 'all passed'} ({fails} failure(s))")
raise SystemExit(1 if fails else 0)
