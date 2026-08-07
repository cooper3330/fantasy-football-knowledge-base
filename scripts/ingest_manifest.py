#!/usr/bin/env python3
"""
Prints a ready-to-paste subagent prompt for the next transcript(s) to ingest.

Why this exists: every ingest subagent starts cold and would otherwise spend
tokens rediscovering the same things — what the schema says, which pages already
exist, who the co-hosts are, what the naming conventions are. That cost is paid
once per episode and *grows as the wiki grows*, which is exactly backwards.

This script computes all of it with zero LLM tokens and inlines it into the
prompt, so the agent's very first action can be reading its transcript.

Do NOT raise --count above 1. Batching looks cheaper -- it amortizes the fixed
overhead this script exists to precompute -- but that overhead is ~3k tokens
while a batched agent carries every finished episode's transcript and pages in
context through the remaining ones. Measured from agent transcripts, 3-per-agent
cost 1.8x per episode versus one. See CLAUDE.md "Model and batch size".

Usage:
  ingest_manifest.py                 # prompt for the next transcript
  ingest_manifest.py --list          # just show the queue, no prompt
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE = REPO / "scripts" / "state.json"

CORE_SCHEMA = """These are the rules that govern every page you write. They are
extracted from CLAUDE.md; you do NOT need to open it.

 1. ATOMIC. One page per entity. No catch-all pages.
 2. SOURCED. Every claim cites its source page, with expert + date. Nothing unsourced.
 3. OPINION, NOT FACT. Write "According to [[Expert]] ([[Source]], YYYY-MM-DD)
    [Format]: ..." Never assert a take as settled truth in the wiki's own voice.
 4. CHRONOLOGICAL. Bullets in "Expert Takes" run oldest -> newest, so the last
    bullet is the current view. Insert at the correct date position; never let an
    older take be written so as to supersede a newer one.
 5. APPEND, DON'T OVERWRITE. A contradicting take goes alongside the old one.
    How opinion shifted is itself the value.
 6. IDEMPOTENT. Search for an existing page under synonyms/nicknames before
    creating one ("CMC" vs "Christian McCaffrey"). Update in place.
 7. NORMALIZE NAMES. ASR garbles proper nouns. Resolve to the correct real-world
    spelling. NEVER create a page under a garbled spelling.
 8. DENSE LINKING. [[wikilinks]] for every player, expert, concept and format.
 9. DISAGREEMENT IS SIGNAL. Record both takes. Don't pick a winner or average them.
10. FILE NAMING. Filename = the exact display name used in wikilinks.

FORMAT PRIORITY: [[Best Ball]] > [[Dynasty]] > [[Redraft (Standard)]]. Tag
format-specific takes `[Best Ball]` / `[Dynasty]` and cross-post to the relevant
wiki/formats/ page. Don't force a tag onto a general take.

NEVER: modify anything under raw/ (contents are immutable); fabricate takes,
quotes or stats; merge experts into an unattributed "consensus"; generate your
own rankings or predictions. You curate what experts said."""

FRONTMATTER = """EVERY page you create or touch must open with a YAML frontmatter block.
`tags` always contains the page's own type; no required key may be left blank.

  players/    type: player     + team, position (QB|RB|WR|TE), tags: [player]
  concepts/   type: concept    + tags: [concept, ...]
  experts/    type: expert     + outlet, tags: [expert]
  formats/    type: format     + priority, tags: [format]
  sources/    type: source     + expert, show, episode, date (YYYY-MM-DD), guid, raw, tags: [source]

Optional anywhere: `aliases: [CMC]` -- use it for nicknames and common ASR
mangles so the alternate spelling resolves to the canonical page.
index.md, log.md and SOURCE_CATALOG.md already have theirs; do not strip it when
appending to them."""

CO_HOSTS = """By show:
- *Matt Waldman's RSP Cast* -> MATT WALDMAN (tracked). Rotating co-hosts:
    - *Feel It or F**k It* -> BOB HARRIS   (NOT tracked; NOT the same person as tracked expert Chris Harris)
    - *Film and Theory*    -> ADAM HARSTAD (NOT tracked)
    - *Going Deep*         -> BRANDON ANGELO (**IS** tracked -- link [[Brandon Angelo]], never label him untracked)
- *Reception Perception: The Show* -> MATT HARMON (tracked) with JAMES KOH (co-host, NOT tracked)
- *Harris Fantasy Football Podcast* -> CHRIS HARRIS (tracked), frequent rotating guests (NOT tracked)

Guests seen so far, all NOT tracked: Daniel Harms, Jeff Erickson, Cecil Lammey, Dwain McFarland, JJ Zachariason."""


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
    # Only meaningful for a multi-episode prompt, which is no longer the default
    # (see the module docstring). Emitting it for n == 1 just burns context.
    ordering = "" if n == 1 else (
        "PROCESS ONE TRANSCRIPT COMPLETELY BEFORE STARTING THE NEXT. Do not read all\n"
        "transcripts up front -- finish all 6 steps below for transcript 1 (including the\n"
        "file move and state.json update), then move on to transcript 2. This keeps each\n"
        "transcript's context clean and means an interruption loses at most one episode.\n\n")

    return f"""You are ingesting {plural} into the Obsidian LLM-wiki at {REPO}.

TRANSCRIPT{"S" if n > 1 else ""} (process strictly in this order, oldest first):
{files}

Each transcript's RSS guid (needed for the state.json update) is in its own front matter.

--- PRE-COMPUTED CONTEXT (do NOT spend tool calls rediscovering this) ---

THE SCHEMA:
{CORE_SCHEMA}

REQUIRED PAGE FRONTMATTER:
{FRONTMATTER}

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

{ordering}!! NEVER OPEN index.md, log.md OR SOURCE_CATALOG.md !!
Those three files are large and grow with every episode; reading one to append a
line is the single most expensive mistake you can make here. Do NOT Read, Grep,
Edit or Write them. Use scripts/wiki_update.py, which needs only your delta:

  # one call per page that is NEW or whose HEADLINE VIEW materially changed
  # (injury, role/depth-chart shift, big ranking move, notable reversal).
  # Insert-or-replace, keyed on page name -- safe to call twice. Max 25 words:
  # lead with position/team and the current view, detail stays on the page.
  python3 scripts/wiki_update.py --index-set "Jahmyr Gibbs" "RB, DET — Waldman's 2024 RB1 over Bijan on price, not talent"

  python3 scripts/wiki_update.py --catalog-row 2024-02-26 "Matt Waldman" "Feel It Or F@#k It: Feb Drafts" "Matt Waldman's RSP Cast - 2024-02-26"

  python3 scripts/wiki_update.py --log-append <<'ENTRY'
## [YYYY-MM-DD] ingest | <Show> — <Episode Title>
<what materially CHANGED -- not just what was processed>
ENTRY

Do not skip --index-set for a minor corroborating take that doesn't move the
headline. A stale index line is worse than none: it is what gets read mid-draft.

BE SPARING WITH TOOL CALLS. Every call re-sends your whole context, so call
count is a direct multiplier on cost. Don't re-read a file you just wrote, don't
verify an edit that already succeeded, and don't read a page you are creating
from scratch.

MUST DO for EACH transcript:
 1. Source summary page in wiki/sources/ (SUMMARY only -- never copy transcript text).
 2. Create/update player, concept, format pages with dated attributed bullets in
    correct chronological position.
 3. Update the relevant wiki/experts/ page(s).
 4. Catalog row + index lines + log entry, all via wiki_update.py as above.
 5. Finalize IN THIS ORDER -- use the locked helpers, never hand-edit
    state.json (a transcript drain may be writing the same file concurrently):
      a. python3 scripts/state_io.py --guid "<guid>" --status ingested
      b. python3 scripts/verify_integrity.py --fix

    Step (b) does the relocation: setting the status makes the transcript's
    position inconsistent with it, and --fix moves the file to
    raw/ingested/<show>/ and syncs staged_path in one locked operation.

    Do NOT try to `mv` the transcript yourself. raw/ is deny-listed against
    edits so the whole tree is immutable to you, and a shell mv of a file under
    it is refused -- correctly, since that same rule is what stops a transcript
    being altered. --fix is the supported relocation path, not a workaround.
 6. Run BOTH checks and confirm both are OK before reporting done:
      python3 scripts/verify_integrity.py
      python3 scripts/lint_frontmatter.py

HARD CONSTRAINTS -- these are not style preferences:
- DO NOT run ANY git command, for any reason. Not `git mv`, not `git add`, not
  `git status`. Use plain `mv` to move transcripts. The orchestrator handles all
  version control; an agent touching git can stage or destroy work it cannot see.
- DO NOT modify the contents of any transcript under raw/.

Report concisely: pages created, pages updated/merged, what materially changed,
names normalized, and the verify_integrity output."""


def build_extract_prompt(ep, inv, plan_out):
    """Phase A of ingest v2 -- see docs/ingest-v2-plan.md.

    The agent reads the transcript and emits ONE plan file. It writes no wiki
    pages, runs no scripts and finalizes nothing; scripts/apply_ingest.py does
    all of that for zero tokens. Cost is turns x context, and this collapses ~66
    turns of interleaved read/edit into a handful.
    """
    inv_players = ", ".join(inv["players"]) or "(none yet)"
    inv_concepts = "\n".join(f"  - {c}" for c in inv["concepts"]) or "  (none yet)"
    # Source pages already on disk for THIS episode's date. A show sometimes
    # publishes twice in a day, and two other shows routinely publish on the same
    # date, so `<Show> - <date>` is not unique. The applier rejects a plan whose
    # source.page collides with an existing page; surfacing the collisions here
    # lets the agent pick a distinguishing suffix instead of getting rejected.
    same_day = sorted(s for s in inv["sources"] if (ep.get("pub_date") or "") in s)
    same_day_block = ("\n".join(f"  - {s}" for s in same_day)
                      if same_day else "  (none — the plain name is free)")
    return f"""Read one podcast transcript and produce ONE JSON plan describing every
wiki change it justifies. You do not edit the wiki -- a script applies your plan.

TRANSCRIPT: {ep['staged_path']}
GUID:       {ep['guid']}
DATE:       {ep.get('pub_date')}
WRITE YOUR PLAN TO: {plan_out}

Read the transcript, then Write the plan. That is the whole job. Do not create or
edit any wiki page, do not run any script, do not touch state.json, do not move
the transcript -- apply_ingest.py does all of it after you exit.

SOURCE PAGES ALREADY ON DISK FOR {ep.get('pub_date')} -- your `source.page` MUST NOT
match any of these. If your episode's plain name "<Show> - {ep.get('pub_date')}"
appears below, another episode already took it, so disambiguate with a short
parenthetical drawn from THIS episode's title or segment, exactly as the existing
ones do -- e.g. "Matt Waldman's RSP Cast - {ep.get('pub_date')} (Evaluation vs. Valuation)":
{same_day_block}

--- PRE-COMPUTED CONTEXT (do NOT spend tool calls rediscovering this) ---

THE SCHEMA:
{CORE_SCHEMA}

REQUIRED PAGE FRONTMATTER:
{FRONTMATTER}

CO-HOST ATTRIBUTION:
{CO_HOSTS}

EXISTING CONCEPT PAGES -- merge into these rather than creating near-duplicates:
{inv_concepts}

EXISTING PLAYER PAGES -- these already exist, so your bullet updates them rather
than creating anything. Never write a variant spelling of a name on this list:
{inv_players}

--- END PRE-COMPUTED CONTEXT ---

PLAN FORMAT -- valid JSON, exactly these keys:

{{
  "guid": "{ep['guid']}",
  "source": {{
    "page": "<Show> - {ep.get('pub_date')}",
    "expert": "<the TRACKED expert whose show this is>",
    "show": "<show name>",
    "episode": "<episode title>",
    "body": "## Summary\\n<what was covered, who spoke>\\n\\n## Pages touched\\n<wikilinks>\\n\\n## Not given pages\\n<passing mentions, so nothing is silently lost>"
  }},
  "pages": [
    {{
      "name": "Keon Coleman",
      "kind": "player",
      "frontmatter": {{"team": "BUF", "position": "WR"}},
      "bullet": "According to [[Matt Waldman]] ([[<the source.page value above>]]) [Dynasty]: ...",
      "related": ["Scouting Bias and Player Archetypes"],
      "index": "WR, BUF — boom/bust outside; needs an anticipatory QB"
    }}
  ],
  "experts": [{{"name": "Matt Waldman", "note": "<one line on this episode>"}}],
  "log": "<what materially CHANGED -- not a list of what was processed>"
}}

RULES FOR THE PLAN -- the applier rejects the whole plan if any is broken, and
tells you which, so getting these right first time saves a retry:

- OUTPUT STRICTLY VALID JSON. The single most common way this fails is an
  unescaped double quote inside a string value -- analysts constantly use quoted
  phrases, and writing `a "tier-two" receiver` inside a JSON string breaks it.
  Use SINGLE quotes for any quoted phrase inside `bullet`, `body`, `note` and
  `index` -- `a 'tier-two' receiver`. Never a raw `"` inside a string value.
  Newlines inside a string must be written as \\n, never a literal line break.
- DO NOT put a date in `bullet`. The script stamps every bullet with {ep.get('pub_date')}
  and inserts it at the correct chronological position. Start the bullet at
  "According to ..." -- no leading "- ", no date, no em dash.
- EVERY bullet must cite the source page as a wikilink -- `([[<your source.page
  value>]])` -- in the usual position, right after the expert's name. This is
  rule 2, and it is also what lets a half-applied episode be detected later, so
  the applier rejects any bullet missing it.
- `kind` is one of player | concept | format.
- ALWAYS include `frontmatter` on every player page entry -- team + position
  (QB|RB|WR|TE). It is used when the page is new and ignored when it already
  exists, so including it is always safe and omitting it is fatal: a page you
  believed existed but doesn't gets the whole plan rejected. Don't try to
  remember which is which. Same for concepts (no required keys) and formats
  (`priority`).
- ONE entry per page. If an episode says three things about a player, write ONE
  bullet covering all three, not three entries.
- BULLET DEPTH IS THE PRODUCT. This wiki exists to show how an analyst's view of
  a player evolved, so a thin bullet is close to worthless a year later. Aim for
  90-150 words per substantive bullet, and carry the specifics that make it
  re-readable: the actual numbers quoted (percentages, snap/target shares,
  measurables), named player comps, the REASON behind the take, the stated risk
  or caveat, the format tag, and any disagreement between the hosts. Do not
  compress a detailed segment into one sentence -- if the episode spent five
  minutes on a player, the bullet should show it. Short bullets are correct only
  for genuinely brief mentions.
- `index` is OPTIONAL. Include it only when the page is NEW or its HEADLINE view
  materially moved (injury, role/depth-chart shift, big ranking move, reversal).
  HARD max 25 words -- count them. The applier trims anything longer from the
  tail, so you lose your own nuance; keep it tight and lead with position/team.
  Omit it entirely for a minor corroborating take.
- `experts` lists only TRACKED experts. A guest's or untracked co-host's view is
  attributed inline in the bullet, never given an expert page.
- Create a player page ONLY for a substantive evaluative take. Catalogue passing
  mentions under "## Not given pages" in the source body.

KEY REMINDERS:
- Whisper ASR: no speaker labels (infer from context), drifting capitalization
  (cosmetic), frequently garbled proper nouns. Normalize EVERY name to its correct
  real-world spelling. Never write a garbled ASR spelling into the plan.
- These are older episodes; it is now August 2026. Note staleness in the `index`
  line where it matters, e.g. "(2024 takes, stale)".
- Quote and attribute faithfully. Never fabricate a take, quote or stat. Where
  experts disagree, record both in the bullet -- don't pick a winner.

BE SPARING WITH TOOL CALLS. Every call re-sends your whole context. You should
need one Read for the transcript and one Write for the plan. You may Read an
existing wiki page if you genuinely need its current stance, but you do not need
to read one to place a bullet -- the script handles ordering.

NEVER: run a git command; modify anything under raw/; open index.md, log.md or
SOURCE_CATALOG.md."""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=1,
                    help="episodes per agent (default 1). Do NOT raise this: an "
                         "agent's cost is turns x context, and a batched agent "
                         "carries episode 1 through episodes 2-3. Measured at "
                         "1.8x per episode. See CLAUDE.md 'Model and batch size'.")
    ap.add_argument("--list", action="store_true", help="show the queue only")
    ap.add_argument("--mode", choices=["legacy", "extract"], default="legacy",
                    help="legacy: the agent writes the wiki itself. extract: the "
                         "agent emits a plan and apply_ingest.py writes it "
                         "(ingest v2 -- see docs/ingest-v2-plan.md)")
    ap.add_argument("--plan-out", help="with --mode extract: where the agent writes its plan")
    ap.add_argument("--guid", help="build the prompt for THIS specific episode "
                    "rather than the queue head. Lets the orchestrator skip past "
                    "an episode that failed earlier in the run -- safe because the "
                    "applier inserts bullets by date, so processing order no longer "
                    "affects chronology.")
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
    if args.guid:
        batch = [e for e in queue if e.get("guid") == args.guid]
        if not batch:
            sys.exit(f"error: {args.guid} is not an episode awaiting ingestion")
    else:
        batch = queue[: args.count]
    if args.mode == "extract":
        if len(batch) != 1:
            sys.exit("error: --mode extract handles one episode per agent")
        if not args.plan_out:
            sys.exit("error: --mode extract requires --plan-out")
        print(build_extract_prompt(batch[0], inv, args.plan_out))
    else:
        print(build_prompt(batch, inv))
    # Footer goes to stderr so callers can pipe stdout straight into an agent:
    #   claude -p "$(ingest_manifest.py --count 3)" --model sonnet
    # Without this split the diagnostics land inside the prompt itself.
    print(f"\n{'=' * 70}", file=sys.stderr)
    print(f"queue: {len(queue)} awaiting | this prompt covers {len(batch)}",
          file=sys.stderr)
    print(f"wiki: {len(inv['players'])} players, {len(inv['concepts'])} concepts, "
          f"{len(inv['sources'])} sources", file=sys.stderr)


if __name__ == "__main__":
    main()
