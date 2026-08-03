# Fantasy Football Knowledge Base — Schema

This vault follows Andrej Karpathy's
[llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern. You (Claude) own the wiki layer. The human curates sources and asks
questions; you do the summarizing, cross-referencing, and maintenance.

**What this wiki is for:** answering real fantasy football decisions — draft
picks, waiver claims, trade evaluations, start/sit — by comparing players across
scoring formats, grounded in what specific trusted analysts actually said, with
dates and citations. It curates expert opinion; it does not originate advice.

---

## Three layers

| Layer | Path | Rule |
|---|---|---|
| **Raw** | `raw/transcripts/<show>/` (awaiting ingestion)<br>`raw/ingested/<show>/` (done) | **Contents immutable.** Never edit or delete a transcript. The *only* permitted change is relocating it between these two trees on ingestion. |
| **Wiki** | `wiki/` | Yours entirely. Create, update, cross-link, keep consistent. |
| **Schema** | `CLAUDE.md` (this file) | Conventions and workflows. |

The two raw trees give an at-a-glance work queue: anything in
`raw/transcripts/` still needs ingesting. `scripts/state.json` remains the
authoritative record; `scripts/verify_integrity.py` reconciles the two and
repairs drift.

Plus two maintained files at the root:

- **`index.md`** — catalog of every wiki page with a one-line summary, grouped
  by category. This is the retrieval entry point: consult it before drilling
  into pages.
- **`log.md`** — append-only chronological record. Never rewrite past entries.

### Wiki layout

```
wiki/
├── players/      one page per NFL player
├── experts/      one page per tracked analyst
├── concepts/     strategy/scheme pages (Zero RB, alignment, etc.)
├── formats/      Best Ball / Dynasty / Redraft (Standard)
├── sources/      one summary page per ingested episode + SOURCE_CATALOG.md
├── synthesis/    filed answers to recurring questions (see "Query")
└── _templates/   starting shapes for each page type
```

---

## Tracked experts

- [[Chris Harris]] — Harris Fantasy Football Podcast
- [[Matt Harmon]] — Reception Perception: The Show (WR charting)
- [[Matt Waldman]] — Matt Waldman's RSP Cast (film-based scouting, dynasty)

Only ingest takes from these three unless asked to add another. Podcasts
frequently feature co-hosts and guests (e.g. Bob Harris, James Koh, Jeff
Erickson) — attribute their views to them by name and note they are not tracked
experts; never silently merge a guest's opinion into a tracked expert's.

## Format priority

[[Best Ball]] (highest) > [[Dynasty]] > [[Redraft (Standard)]] (lowest). When a
take is format-specific, tag it (`[Best Ball]`, `[Dynasty]`) and cross-post to
the relevant `wiki/formats/` page. Don't force a tag on general takes.

---

## Core rules

1. **Atomic pages.** One page per entity. No catch-all pages.
2. **Source-grounded.** Every claim cites the source page it came from, with
   expert + date. No unsourced assertions.
3. **Opinion, not fact.** Frame as "According to [[Expert]] ([[Source]],
   YYYY-MM-DD) [Format]: ..." — never state a take as settled truth in the
   wiki's own voice.
4. **Chronological order wins.** Bullets in a page's "Expert Takes" run oldest →
   newest, so the last bullet is the most current view. When takes conflict, the
   newer one reflects better information (injuries, camp reports, depth-chart
   moves); an older take must never be written so as to supersede a newer one.
   If ingesting out of order, insert at the correct date position rather than
   appending.
5. **Append, don't overwrite.** A contradicting new take is added alongside the
   old one, not in place of it. How opinion shifted is itself valuable.
6. **Idempotent.** Before creating a page, search for an existing one under
   synonyms/nicknames ("CMC" vs "Christian McCaffrey"). Update in place.
7. **Normalize proper nouns.** Transcripts are ASR output and garble names —
   observed: "Malik neighbors" (Nabers), "Romo Dunze" (Rome Odunze), "Jameer
   Gibbs" (Jahmyr Gibbs), "Debo Samuel" (Deebo Samuel), "Dijon Stribling"
   (De'Zhaun Stribling), "about Wall" (Matt Waldman). Always resolve to the
   correct real-world spelling before creating or updating a page. **Never
   create a page under a garbled spelling.**
8. **Dense linking.** `[[wikilinks]]` for every player, expert, concept, and
   format mention.
9. **Disagreement is signal.** When experts differ, record both takes. Don't
   pick a winner or average them.
10. **File naming.** Filename = exact display name used in wikilinks, e.g.
    `wiki/players/Christian McCaffrey.md`.

---

## Operation: ingest

Triggered when transcripts sit in `raw/transcripts/` with status `fetched` in
`scripts/state.json`.

**Always process oldest-first.** Filenames are date-prefixed, so sorting by
filename gives the correct order. See rule 4 — this is what makes the
chronological invariant hold.

For each transcript:

1. Read it from `raw/transcripts/<show>/`. **Never edit its contents.**
2. Note: transcripts have **no speaker labels**. Infer speakers from context
   (introductions, how they address each other, subject matter). Capitalization
   and punctuation drift mid-episode — this is cosmetic, content is accurate.
3. Create `wiki/sources/<Show> - <YYYY-MM-DD>.md` — a summary page: what was
   covered, who spoke, and links to every entity page the episode touched. This
   is a *summary*, not a copy; the full text stays in `raw/`.
4. Extract distinct, attributable claims. For each, create or update the
   relevant `wiki/players/`, `wiki/concepts/`, or `wiki/formats/` page with a
   dated bullet citing the source. **A single episode may touch 10–15 pages.**
5. Update `wiki/experts/<Expert>.md` with the new source, and any shift in their
   overall stance or known biases.
6. Update `wiki/sources/SOURCE_CATALOG.md` with a row for the episode.
7. Update `index.md` (see "Index maintenance"), for **both**:
   - every page newly created in this ingest, and
   - every existing page whose **headline view materially changed** — an injury,
     a role or depth-chart shift, a big ranking move, a notable reversal. The
     index line must reflect the *current* view, not the view from whenever the
     page was created. A stale index line is worse than none, because it is what
     gets read during a live draft.

   Don't rewrite an index line for a minor corroborating take that doesn't move
   the headline.
8. Append to `log.md`: `## [YYYY-MM-DD] ingest | <Show> — <Episode Title>`.
   Include a one-line note of what materially changed (e.g. "Pearsall knee
   concern — cratered to ~WR70"), so `log.md` is scannable for *what shifted*,
   not just *what was processed*.
9. **Finalize, strictly in this order** — the order matters so an interruption
   is always recoverable:
   a. Set the episode's `status` to `ingested` in `scripts/state.json`.
   b. Move the transcript `raw/transcripts/<show>/<file>` →
      `raw/ingested/<show>/<file>`.
   c. Update that episode's `staged_path` in `state.json` to the new location.

   If you are interrupted between these, nothing is lost: the transcript exists
   in one tree or the other, and `scripts/verify_integrity.py` will detect and
   repair the mismatch. Run it if anything looks inconsistent:

   ```bash
   python3 scripts/verify_integrity.py          # report
   python3 scripts/verify_integrity.py --fix    # repair
   ```

   **Never delete a transcript.** Moving between the two raw trees is the only
   permitted relocation.

## Operation: query

When asked a fantasy question (draft, waiver, trade, start/sit):

1. Consult `index.md` first, then read the relevant pages.
2. Answer with citations — expert, date, format. Surface disagreement between
   experts rather than flattening it. Weight recency (rule 4).
3. **If the answer is durable and likely to be asked again, file it** as a page
   in `wiki/synthesis/` (e.g. "Best Ball WR Targets 2026", "Dynasty RB Tiers"),
   add it to `index.md`, and log it. This is the point of the pattern: valuable
   answers accumulate as wiki pages instead of disappearing into chat.
4. Append to `log.md`: `## [YYYY-MM-DD] query | <question>`.

Synthesis pages are **derived**, not authoritative — they must cite the player
pages behind them and note the date they were last refreshed, since player
opinion moves.

## Operation: lint

A periodic health pass. Check for:

- **Contradictions** — a page asserting two incompatible things without dates.
- **Stale claims** — a synthesis page built on takes that have since been
  superseded; an injury/role note overtaken by later reporting.
- **Orphan pages** — pages nothing links to, or missing from `index.md`.
- **Missing cross-references** — a player mentioned in prose without a wikilink,
  or an expert page not listing a source it clearly informed.
- **Garbled names** — pages created under ASR spellings (rule 7), or duplicates
  of the same player under two spellings.
- **Gaps** — a tracked expert with no recent sources; a format page with no takes.
- **Stale index lines** — an `index.md` summary that no longer matches its page's
  most recent take. Spot-check by comparing each index line against the last
  bullet on the page it points to.
- **Raw/state drift** — run `python3 scripts/verify_integrity.py`. It checks that
  every transcript is on disk, in the tree its status implies, referenced by
  state, with no duplicates or orphans.

Append findings to `log.md` as `## [YYYY-MM-DD] lint | <scope>` with what was
fixed.

---

## Index maintenance

`index.md` is the retrieval layer — keep it accurate or retrieval degrades.

- Every wiki page appears exactly once, under its category.
- Each entry is **one line**: the wikilink plus a short summary that helps decide
  whether to open the page. For players, lead with position/team and the current
  headline view.
- Keep player entries grouped by position (QB / RB / WR / TE).
- Update it in the same pass — never defer — in **both** cases:
  - a page was **created**, and
  - an existing page's **headline view materially changed** (see ingest step 7).
    The line must describe the current view, not the view at creation time.
- Mark clearly when a page's takes are old enough to be untrustworthy, e.g.
  *(2023 takes, stale)*. During a live draft the index line is often all that
  gets read, so an unqualified stale summary actively misleads.

## What NOT to do

- Don't modify, move, or delete anything under `raw/`.
- Don't fabricate takes, quotes, or stats not present in the source.
- Don't merge multiple experts into an unattributed "consensus".
- Don't generate the wiki's own rankings or predictions — curate what experts
  said. Synthesis pages may *organize* expert views; they may not invent new ones.
- Don't run git commands during ingestion. A separate weekly job handles backup.

---

## Pipeline (transcript acquisition)

`scripts/check_new_episodes.py` reads each show's public RSS feed and writes
transcripts into `raw/transcripts/<show>/`, transcribing locally with
`whisper.cpp`. It never touches git and never calls a paid API. See `README.md`
for architecture, setup, and the researched-and-rejected alternatives.

State (`scripts/state.json`, keyed by RSS guid): `pending` → `fetched` →
`ingested`. You set `ingested`; the script sets the other two.

Backlog draining is a separate, one-time operation (`scripts/drain_backlog.sh`).
The daily job is **currently paused** while the back catalog is transcribed and
ingested.
