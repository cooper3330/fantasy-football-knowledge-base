#!/usr/bin/env python3
"""
Prints a ready-to-paste subagent prompt for the next transcript(s) to ingest.

Why this exists: every ingest subagent starts cold and would otherwise spend
tokens rediscovering the same things — what the schema says, which pages already
exist, who the co-hosts are, what the naming conventions are. That cost is paid
once per episode and *grows as the wiki grows*, which is exactly backwards.

This script computes all of it with zero LLM tokens and inlines it into the
prompt, so the agent's very first action can be reading its transcript.

Usage:
  ingest_manifest.py                 # prompt for the next transcript
  ingest_manifest.py --count 3       # one prompt covering the next 3 (cheaper)
  ingest_manifest.py --list          # just show the queue, no prompt
"""

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE = REPO / "scripts" / "state.json"

CO_HOSTS = """- *Feel It or F**k It* -> BOB HARRIS (NOT tracked; NOT the same person as tracked expert Chris Harris)
- *Film and Theory*      -> ADAM HARSTAD (NOT tracked)
- *Going Deep*           -> BRANDON ANGELO (**IS** a tracked expert -- link as [[Brandon Angelo]], do not label him untracked)"""


def load_queue():
    s = json.loads(STATE.read_text())
    eps = [v for v in s["episodes"].values() if v.get("status") == "fetched"]
    eps.sort(key=lambda v: (v.get("pub_date") or "", v.get("title") or ""))
    return eps


def inventory():
    def names(d):
        p = REPO / "wiki" / d
        return sorted(f.stem for f in p.glob("*.md")) if p.exists() else []
    return {k: names(k) for k in ("players", "concepts", "experts", "sources")}


def build_prompt(eps, inv):
    inv_players = ", ".join(inv["players"]) or "(none yet)"
    inv_concepts = "\n".join(f"  - {c}" for c in inv["concepts"]) or "  (none yet)"
    n = len(eps)
    plural = "these transcripts IN ORDER" if n > 1 else "this transcript"
    files = "\n".join(f"  {i}. {e['staged_path']}" for i, e in enumerate(eps, 1))

    return f"""You are ingesting {plural} into the Obsidian LLM-wiki at {REPO}.

STEP 0 -- Read {REPO}/CLAUDE.md in full. It is the authoritative schema. Follow it exactly.

TRANSCRIPT{"S" if n > 1 else ""} (process strictly in this order, oldest first):
{files}

Each transcript's RSS guid (needed for the state.json update) is in its own front matter.

--- PRE-COMPUTED CONTEXT (do NOT spend tool calls rediscovering this) ---

CO-HOST ATTRIBUTION:
{CO_HOSTS}

EXISTING CONCEPT PAGES -- merge into these rather than creating near-duplicates:
{inv_concepts}

EXISTING PLAYER PAGES -- check this list before creating any player page, so you
update rather than duplicate, and never create a variant spelling of an existing page:
{inv_players}

--- END PRE-COMPUTED CONTEXT ---

KEY REMINDERS:
- Whisper ASR: no speaker labels (infer from context), drifting capitalization
  (cosmetic only, content is accurate), and frequently garbled proper nouns.
  Normalize EVERY name to its correct real-world spelling. Never create a page
  under a garbled ASR spelling.
- These are older episodes; it is now August 2026. Mark stale player pages using
  the established convention -- see wiki/players/DeAndre Hopkins.md for the
  blockquote format, and use a "(YYYY takes, stale)" marker on the index.md line.
- Create a player page ONLY for a substantive evaluative take. Catalogue passing
  mentions under a "Not given pages" section in the source summary so nothing is
  silently lost.
- Prefer merging into existing concept pages over proliferating near-duplicates.

MUST DO for EACH transcript (per CLAUDE.md ingest steps):
 1. Source summary page in wiki/sources/ (SUMMARY only -- never copy transcript text).
 2. Create/update player, concept, format pages with dated attributed bullets in
    correct chronological position.
 3. Update the relevant wiki/experts/ page(s).
 4. Row in wiki/sources/SOURCE_CATALOG.md.
 5. Update index.md -- for BOTH new pages AND existing pages whose headline view changed.
 6. Append to log.md with a note of what materially changed.
 7. Finalize IN THIS ORDER: (a) status "ingested" in scripts/state.json,
    (b) move transcript to raw/ingested/<show>/, (c) update staged_path.
 8. Run `python3 scripts/verify_integrity.py` and confirm OK.

DO NOT run any git commands. Do not modify transcript contents.

Report concisely: pages created, pages updated/merged, what materially changed,
names normalized, and the verify_integrity output."""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=1,
                    help="episodes per agent; >1 amortizes fixed overhead")
    ap.add_argument("--list", action="store_true", help="show the queue only")
    args = ap.parse_args()

    queue = load_queue()
    if not queue:
        print("Nothing awaiting ingestion.")
        return

    if args.list:
        print(f"{len(queue)} awaiting ingestion. Next 15:\n")
        for e in queue[:15]:
            print(f"  {e.get('pub_date')} | {e.get('show','?')[:28]:28} | {e.get('title','?')[:50]}")
        return

    inv = inventory()
    batch = queue[: args.count]
    print(build_prompt(batch, inv))
    print(f"\n{'=' * 70}", flush=True)
    print(f"queue: {len(queue)} awaiting | this prompt covers {len(batch)}")
    print(f"wiki: {len(inv['players'])} players, {len(inv['concepts'])} concepts, "
          f"{len(inv['sources'])} sources")


if __name__ == "__main__":
    main()
