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

### Page frontmatter

**Every page — without exception — opens with a YAML frontmatter block.** This is
what makes the vault queryable as data rather than prose: Obsidian tag search and
Dataview both key off it. A page without frontmatter is invisible to every query
that isn't full-text search.

Copy the shape from `wiki/_templates/<type>.md`. Required keys by type:

| Location | `type:` | Required keys |
|---|---|---|
| `wiki/players/` | `player` | `type`, `team`, `position`, `tags` |
| `wiki/experts/` | `expert` | `type`, `outlet`, `tags` |
| `wiki/concepts/` | `concept` | `type`, `tags` |
| `wiki/formats/` | `format` | `type`, `priority`, `tags` |
| `wiki/sources/` | `source` | `type`, `expert`, `show`, `episode`, `date`, `guid`, `raw`, `tags` |
| `wiki/synthesis/` | `synthesis` | `type`, `question`, `formats`, `last_refreshed`, `tags` |
| `index.md` | `index` | `type`, `tags` |
| `log.md` | `log` | `type`, `tags` |
| `wiki/sources/SOURCE_CATALOG.md` | `catalog` | `type`, `tags` |

Rules that apply everywhere:

- `tags` always contains the page's own type as a tag (a `player` page is tagged
  `[player]`), so `type:` and tag search can never disagree. Add further tags
  after it: `[player, prospect]`, `[concept, evaluation, scheme]`.
- `position` is one of `QB` / `RB` / `WR` / `TE`.
- `date` and `last_refreshed` are `YYYY-MM-DD`.
- No required key is left blank on a real page. Templates ship blank; pages don't.
- `aliases` is optional but legal anywhere, and is the right home for the
  nickname problem in rule 6 — `aliases: [CMC]` on the Christian McCaffrey page.

Verify with:

```bash
python3 scripts/lint_frontmatter.py
```

It is report-only by design and has no `--fix`: filling in a missing `team:` or
`date:` means knowing the source, and inventing one would violate "don't
fabricate". Fix what it reports by hand.

---

## Tracked experts

- [[Chris Harris]] — Harris Fantasy Football Podcast
- [[Matt Harmon]] — Reception Perception: The Show (WR charting)
- [[Matt Waldman]] — Matt Waldman's RSP Cast (film-based scouting, dynasty)
- [[Brandon Angelo]] — *Going Deep* co-host on the RSP Cast. **Evaluation and
  theory, not rankings** — his value is mostly in the concept layer, and his
  frameworks outlive the specific players he applies them to.

Only ingest takes from these four unless asked to add another. Podcasts
frequently feature other co-hosts and guests — **Bob Harris** (*Feel It or
F**k It*), **Adam Harstad** (*Film and Theory*), James Koh, Jeff Erickson,
Cecil Lammey — who are **not** tracked. Attribute their views to them by name
and note they are not tracked experts; never silently merge a guest's opinion
into a tracked expert's.

⚠️ **Bob Harris ≠ [[Chris Harris]].** Different people. Bob Harris co-hosts the
RSP Cast and is not tracked; Chris Harris hosts the Harris Fantasy Football
Podcast and is tracked. Never conflate them.

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
   (De'Zhaun Stribling), "about Wall" (Matt Waldman), "Alexander Madison"
   (Alexander Mattison). Always resolve to the
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

### Delegate to subagents — one transcript per agent

A transcript is 10–20k words and ingestion touches 10–15 pages. Doing several
in one context degrades quality on the later ones. **Spawn one subagent per
transcript**, each with a fresh context.

Run `python3 scripts/ingest_manifest.py` first — it prints a ready-made
subagent prompt for the next transcript, with the current page inventory and
co-host roster already inlined. This exists so the agent doesn't burn tokens
rediscovering the wiki's contents on every run.

**Rules for orchestrating:**

1. **Strictly sequential — never parallel.** Sequential is about *write
   ordering*, not context isolation; separate agents already have separate
   contexts however they are scheduled (see "Model and batch size"). Three
   things break under concurrency, and none of them is fixed by more isolation:

   - Rule 4 requires episode N ingested before N+1, so bullets land in
     chronological order on the player pages they share.
   - Two episodes usually touch overlapping player pages. Those pages are
     edited read-modify-write with no lock, so simultaneous agents silently
     drop one of the two takes.
   - `wiki_update.py` is **not** locked (unlike `state_io.py`, which is), so
     concurrent `--index-set` or `--log-append` calls can interleave and
     corrupt `index.md` or `log.md`.

   Run N episodes per run by looping the invocation, never by fanning out.
2. **Verify between each** — run `python3 scripts/verify_integrity.py` and
   confirm the transcript moved to `raw/ingested/`.
3. **Checkpoint-commit between episodes** so a failure never costs more than one
   episode. This is the orchestrator's job and is *not* part of ingestion — see
   "What NOT to do". Skip it when running unattended/headless; the weekly backup
   job covers that path.
4. **On agent failure, check for partial writes** before retrying: if
   `verify_integrity` is OK and `git status` is clean, nothing was written and
   the retry is safe. This has been exercised — a mid-run API failure left no
   partial state.
5. Agents must **not** run git commands; the orchestrator commits.

### Model and batch size (cost)

Ingestion is the most expensive thing this wiki does. Two settings control it:

- **Always spawn ingest agents with `model: "claude-sonnet-5"`, `effort: medium`.**
  Extraction against a schema this explicit does not need a frontier model, and
  the prompt already names every step, so it is not reasoning-heavy either.
  Model is the single biggest cost lever in the pipeline and effort is the
  second — do not default to the parent model. Pin the full model ID rather than
  the `sonnet` alias: the alias tracks the latest Sonnet, so a release would
  silently change ingest cost and output shape mid-backlog.
- **One transcript per agent** (`ingest_manifest.py --count 1`, the default).

**Per *agent*, not per *run*.** These are different limits and only the first
one is capped. Ingesting several episodes in a single run is fine — and is what
`run_daily_check.sh` does, `INGEST_PER_RUN` episodes at a time — provided each
gets its **own agent invocation**. A separate `claude -p` is a separate process
with a fresh session: no `--continue`, no `--resume`, so it starts with an empty
context and carries nothing from the episode before it. That is full isolation,
and it is the thing `--count 3` failed to provide.

The loop has two requirements that are easy to get wrong:

- **Regenerate the manifest every iteration.** Hoisting `ingest_manifest.py`
  out of the loop re-ingests the same episode N times, and freezes the page
  inventory — so agent N can't see that agent N-1 just created
  `wiki/players/Brock Bowers.md` and will create a near-duplicate.
- **Guard against a stalled queue.** If an agent dies or finishes without
  setting `status: ingested`, the queue head is unchanged and the next
  iteration hands the identical transcript to a fresh agent. Unattended, that
  spends the whole run failing on one poison episode. Compare the head guid
  before and after and stop the run if it didn't move.

⚠️ **This reverses the previous "batch 3 per agent" rule, which was wrong.**
That rule optimized the fixed overhead — schema, page inventory, conventions —
which is real but tiny (~3k tokens). What it missed is that an agent's cost is
dominated by *context re-sent on every turn*: cost ≈ turns × average context.
Batching makes both terms worse, because episode 1's transcript and every page
it touched stay in context for the whole of episodes 2 and 3.

Measured from agent transcripts (`cache_read + cache_creation + output`):

| Run | Tokens per episode |
|---|---:|
| Batched 3/agent, old write path | 25.9M |
| Single episode, old write path | 14.1M |
| Single episode, script write path | **9.1M** |

Batching cost **1.8× per episode**. Saving 3k of fixed overhead by spending
~12M on carried context is a bad trade by four orders of magnitude.

- **Spawn with `subagent_type: "ingest"`** (`.claude/agents/ingest.md`), which
  restricts the agent to Read, Write, Edit and Bash. An unrestricted agent
  starts at ~44.6k tokens of context before it does any work — only ~2.8k of
  that is the prompt; the rest is the system prompt plus tool schemas for
  browsers, computer-use, mail, calendar and simulators that an ingest agent
  never touches. That constant is re-read on every turn, so at 77 turns it is
  ~3.2M tokens, roughly 38% of all cache reads.

  Agent definitions are loaded when a session starts, so a newly added or edited
  one only takes effect in the next session.

### Measuring cost

Do not tune against the token total in tool output. It excludes cached input —
~92% of what an agent consumes — so a run reported as "149k" really moved 9.1M.

```bash
python3 scripts/agent_cost.py                     # all agents, newest first
python3 scripts/agent_cost.py --agent <agentId>   # one run
```

It reads `~/.claude/projects/<project>/<session>/subagents/agent-*.jsonl` and
weights components by price (cache write 1.25×, cache read 0.10×, output 5×),
because raw volume misleads: cache writes are ~7% of tokens but ~42% of cost.

Two numbers to watch:

- **turns × context** is the whole cost model. Fewer turns, smaller context.
  There is no third lever — cache hit rate is already ~93% and has no knob.
- **cache rebuilt Nx** — 1.0× means the cache was built once. Observed runs sit
  at 4–5.5×, meaning it expired mid-run and every rebuild was charged at the
  write rate. Shorter runs cross fewer expiries, so cutting turns pays twice.

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
6. Update `index.md`, `SOURCE_CATALOG.md` and `log.md` — **never by opening
   them.** See "Shared files: write through the script" below. Index lines are
   required for **both**:
   - every page newly created in this ingest, and
   - every existing page whose **headline view materially changed** — an injury,
     a role or depth-chart shift, a big ranking move, a notable reversal. The
     index line must reflect the *current* view, not the view from whenever the
     page was created. A stale index line is worse than none, because it is what
     gets read during a live draft.

   Don't rewrite an index line for a minor corroborating take that doesn't move
   the headline. The log entry is
   `## [YYYY-MM-DD] ingest | <Show> — <Episode Title>` plus a note of what
   materially changed (e.g. "Pearsall knee concern — cratered to ~WR70"), so
   `log.md` is scannable for *what shifted*, not just *what was processed*.
9. **Finalize, strictly in this order** — the order matters so an interruption
   is always recoverable:
   a. Set the episode's `status` to `ingested` — **use the locked helper, never
      hand-edit the JSON**, because a transcript drain may be writing the same
      file concurrently:
      ```bash
      python3 scripts/state_io.py --guid "<guid>" --status ingested
      ```
   b. Relocate the transcript and sync `staged_path`, in one operation:
      ```bash
      python3 scripts/verify_integrity.py --fix
      ```
      Setting the status in (a) makes the file's position inconsistent with it;
      `--fix` moves `raw/transcripts/<show>/<file>` → `raw/ingested/<show>/<file>`
      and updates `staged_path` to match.

   **Agents must not `mv` the transcript themselves.** `raw/**` is deny-listed
   against edits (`.claude/settings.json`), which is what makes transcript
   contents immutable in practice rather than only by instruction — and that
   same rule refuses a shell `mv` of anything under `raw/`. This was found the
   hard way: two ingest runs had their `mv` blocked and fell back to `--fix`.
   Rather than weaken the immutability rule to permit a move, `--fix` *is* the
   supported relocation path. It is idempotent, locked, and self-verifying.

   If you are interrupted mid-finalize, nothing is lost: the transcript exists
   in one tree or the other, and the same command repairs the mismatch.

   ```bash
   python3 scripts/verify_integrity.py          # report
   python3 scripts/verify_integrity.py --fix    # repair
   ```

   **Never delete a transcript.** Moving between the two raw trees is the only
   permitted relocation.

### Shared files: write through the script

`index.md`, `log.md` and `wiki/sources/SOURCE_CATALOG.md` are **append targets,
not reading material**. An ingest agent must never Read, Grep, Edit or Write
them directly.

The reason is cost. The Edit tool requires reading a file before editing it, so
appending one line to `log.md` charges you for all of `log.md`. Measured at 25
episodes ingested, those three files were **~29,800 tokens per episode — about
half of an episode's entire unique token spend** — purely to append a handful of
lines. They also grow ~570 tokens *each* per episode: extrapolated across the
backlog they pass 170k tokens apiece, at which point an agent cannot open them
at all and ingestion stops working.

`scripts/wiki_update.py` takes only the delta, so the cost is ~zero and stays
flat however large the files get:

```bash
# insert-or-replace an index line, keyed on page name (safe to call twice).
# Routed to the right section automatically from the page's own frontmatter.
python3 scripts/wiki_update.py --index-set "Jahmyr Gibbs" "RB, DET — Waldman's 2024 RB1 over Bijan on price"

python3 scripts/wiki_update.py --catalog-row 2024-02-26 "Matt Waldman" "<episode>" "<summary page>"

python3 scripts/wiki_update.py --log-append <<'ENTRY'
## [2024-02-26] ingest | Show — Title
What materially changed.
ENTRY
```

Index summaries are capped at **25 words** and the script rejects longer ones.
The index is scanned mid-draft and re-read by every query, so a line has to be
scannable: lead with position/team and the current headline view, and leave the
detail on the page itself.

Because `--index-set` is keyed on the page name, an index line cannot fork into
two competing entries — which is what used to make stale index lines possible.

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
- **Split wikilinks** — a `[[Player\nName]]` broken across a line break by text
  wrapping. These silently fail to resolve and are easy to miss. Check with:
  `grep -Pzo '\[\[[^\]]*\n[^\]]*\]\]' **/*.md`. Check `log.md` too, not just `wiki/`.
- **Stale index lines** — an `index.md` summary that no longer matches its page's
  most recent take. Spot-check by comparing each index line against the last
  bullet on the page it points to.
- **Over-long index lines** — run `python3 scripts/wiki_update.py --check-index`.
  Entries over 25 words make the index unscannable during a draft and inflate
  every query that reads it.
- **Frontmatter drift** — run `python3 scripts/lint_frontmatter.py`. It checks
  every page against its type's schema (see "Page frontmatter"): block present
  and closed, required keys present and non-empty, `type:` matching the folder,
  base tag present, valid position and date formats.
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
- **Don't run git commands as part of ingestion.** Ingestion itself — every one
  of the 8 steps — never touches git. This holds for ingest subagents and for
  the headless daily job without exception.

  The one deliberate exception is *checkpointing*, and it is not part of
  ingestion: a human-facing orchestrator driving a long interactive batch may
  commit **between** episodes so that a failure costs at most one episode and
  leaves an obvious rollback point. That is a decision about the run, not a step
  in the workflow. It proved its worth when two mid-batch API failures needed
  verifying against a known-clean tree.

  Automated backup remains the separate weekly `launchd` job. Ingestion and git
  stay independent processes.

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
