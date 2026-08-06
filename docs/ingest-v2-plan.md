# Ingest v2 — extract once, apply mechanically

Status: **shipped and default** (2026-08-05). Measured result at the bottom.

## Why

Measured across 12 ingest agents on 2026-08-04/05 (`scripts/agent_cost.py --headless`):

| component | % of volume | % of cost |
|---|---:|---:|
| cache read | 82.3% | 17.4% |
| cache write | 13.2% | 35.0% |
| **output** | **4.5%** | **47.6%** |

Output tokens are weighted 5× base input, so half the spend is generation — and the
agents persist only ~130 tokens of visible text per episode while billing ~274,000
output tokens. The remainder is reasoning: **~4,134 tokens of thinking per turn,
66 turns per episode**.

Every optimization before this one (tool restriction, model pinning, killing the
3-per-agent batching) attacked context size. Context is 17% of cost. The lever
that matters is **turns**, because each turn pays to re-reason over everything.

Context composition of a representative agent, 164k peak:

```
prompt (manifest)   22k
transcript          17k
wiki page reads     46k   <-- removable
agent's own writes  25k
```

Cost per episode today: **2.88M cost units** (1.0 = one base input token).
495 episodes remain. At today's rate that is ~1.4B.

## What changes

Today one agent interleaves reading and writing across ~66 turns:

```
read transcript -> read page -> edit page -> read page -> edit page -> ... x25
```

Every page read stays in context permanently and is re-reasoned over on every
later turn. Split it:

- **Phase A (LLM, ~6 turns).** Read the transcript. Emit one JSON plan
  describing every page, bullet, index line and log entry. Write nothing else.
- **Phase B (`scripts/apply_ingest.py`, zero tokens).** Validate the plan, then
  apply it: create/update pages, insert bullets in date order, update
  index/catalog/log, finalize state.

Projection: ~6 turns at ~39k context instead of 66 at ~76k → **~300k cost units
per episode**, an ~90% cut. This is arithmetic on measured inputs, not a measured
result; it gets validated on 3 episodes before it becomes the default.

## Why the writes can be mechanical

Everything the agent currently does by hand in the write phase is deterministic:

| today (agent, costs turns) | v2 (script, free) |
|---|---|
| Read page to find where the bullet goes | parse dates in `## Expert Takes`, insert in order |
| Prepend `- YYYY-MM-DD — ` correctly | script stamps the episode date — rule 4 becomes unbreakable |
| Copy the template for a new page | script fills the template |
| One `--index-set` Bash call per page | one field per page in the plan |
| `--catalog-row`, `--log-append` | derived from the plan's `source` block |
| `state_io.py` then `verify_integrity.py --fix` | script, in the right order |

The judgement — what was said, who said it, whether it matters — stays with the
model. Only the clerical work moves.

## Plan JSON

Phase A writes exactly one of these.

```jsonc
{
  "guid": "https://mattwaldmanrsp.com/?p=50029",
  "source": {
    "page": "Feel It Or F@#k It - 2024-04-16",   // filename stem in wiki/sources/
    "expert": "Matt Waldman",                     // must be a tracked expert
    "show": "Matt Waldman's RSP Cast",
    "episode": "Feel It Or F@#k It: 4.16.24",
    "body": "## Summary\n...\n\n## Pages touched\n..."
  },
  "pages": [
    {
      "name": "Keon Coleman",
      "kind": "player",                     // player | concept | format
      "frontmatter": {"team": "BUF", "position": "WR"},  // required iff page is new
      "bullet": "According to [[Matt Waldman]] [Dynasty]: ...",  // NO leading "- date —"
      "related": ["Scouting Bias and Player Archetypes"],        // optional
      "index": "WR, BUF — boom/bust outside role; needs an anticipatory QB"  // optional
    }
  ],
  "experts": [
    {"name": "Matt Waldman", "note": "optional stance/bias shift"}
  ],
  "log": "What materially changed. Not a list of what was processed."
}
```

Design decisions worth stating:

- **The agent never writes the date.** The script stamps every bullet with the
  episode's `pub_date` from `state.json`. Rule 4 stops being something an agent
  can get wrong.
- **`index` is optional and per-page**, not a separate call. Present only when the
  page is new or its headline view moved. Insert-or-replace keyed on page name, so
  a second call is harmless.
- **Catalog row and log header are derived**, not supplied. The agent writes only
  the "what changed" body.
- **`frontmatter` is required exactly when the page does not exist.** Supplying it
  for an existing page is ignored, not an error — the agent cannot see the page and
  should not be punished for guessing wrong about whether it exists.

## Failure handling

The existing safety net still applies and is the reason this is safe to stage:

- Phase B **validates the entire plan before writing anything** — unknown expert,
  missing frontmatter on a new page, bad date, malformed JSON all fail with a
  non-zero exit and zero disk changes.
- If phase B dies mid-write anyway, `scripts/partial_write_check.py` detects it
  before the next run and `scripts/rollback_partial.py` undoes it. Both already
  exist and are tested.
- State is finalized **last**, so an interruption always leaves the episode
  `fetched` — recoverable, never silently half-done.

Phase A failing is cheap: no plan file, nothing written, the queue head is
unchanged and the stall guard stops the run.

## Staging

Each step lands and is committed independently. Steps 1–2 are useful on their own
even if step 3 is abandoned.

1. **`wiki_update.py --page-append`** — chronological insertion, page creation from
   template, related-links merge, idempotency. This is opportunity #2 standalone:
   it removes the 46k/episode of page reads from the *current* pipeline without
   touching the architecture.
2. **`apply_ingest.py` + tests** — the whole plan applier, driven from a
   hand-written plan fixture. No LLM involved, so it can be tested exhaustively.
3. **`ingest_manifest.py --mode extract` + `.claude/agents/extract.md`** — the
   phase A prompt and a Read+Write-only agent.
4. **`run_daily_check.sh`** — `INGEST_MODE=extract|legacy`, defaulting to `legacy`
   until validated, so rollback is one env var.
5. **Validate on 3 episodes**, measure against the 2.88M baseline, spot-check page
   quality, then flip the default and update `CLAUDE.md`.

## What could go wrong

- **Plan quality drops because the agent can't see existing pages.** It currently
  reads a page mostly to find the insertion point and to judge whether the index
  line moved; the first is now automatic and the second is a judgement it can make
  from its own take. The `extract` agent keeps `Read`, so it can still open a page
  when it genuinely needs to — it is simply no longer forced to.
- **One large JSON hits an output ceiling.** A 15-page plan is ~9k tokens. Headroom
  is fine, but validation failure is explicit rather than silent truncation.
- **Near-duplicate pages.** Unchanged risk: the manifest already inlines the full
  page inventory, which is what prevents this today.

## Measurement

Same instrument as the baseline, so the numbers are comparable:

```bash
python3 scripts/agent_cost.py --headless --since 2026-08-05
```

Success is cost per episode materially under 2.88M with `lint_frontmatter.py` and
`verify_integrity.py` clean and no drop in bullets-per-episode or pages-touched.

## Result (2026-08-05)

Four episodes applied end-to-end, plus a two-episode A/B that ran extract over
transcripts legacy had already ingested and compared plans without applying them.

| | legacy | extract |
|---|---:|---:|
| turns/episode | 66 | **5** |
| cost units/episode | 2,880k | **346k** |
| output tokens/episode | 274k | 46k |
| tool calls | ~63 | 2 (one Read, one Write) |
| wall clock | ~5 min | ~100 s |

**88% cheaper.** Across the remaining 345 episodes that is ~119M cost units
instead of ~994M.

Two things the projection got wrong, both found by measuring rather than assuming:

- **Coverage was never the problem; depth was.** The first four episodes averaged
  10 bullets against legacy's 21, which looked like a serious regression. The A/B
  on identical transcripts showed page coverage at 0.84× and 1.00× — the gap was
  episode content. What was real was bullet *length*, at 0.58–0.67× of legacy,
  i.e. ~0.57× content volume. Stating depth as a requirement in the prompt brought
  that to **1.09×**, at the cost of raising cost/episode from ~198k to ~346k.
  Worth it: this wiki's value is showing how a view moved over time.
- **A rejected plan is cheap and clean, but avoidable rejections are not free.**
  One plan was rejected for omitting frontmatter on a page the agent assumed
  existed. Nothing was written and the tree stayed clean — but the prompt had told
  it to omit frontmatter for known pages, turning a safe default into a guess.
  Now it always supplies it.

Also fixed along the way: agents naming a source page after the show verbatim
("Reception Perception: The Show") produced a filename macOS renders with a slash
and that diverged from existing pages for the same show. The applier now strips
filename-hostile characters and rewrites the citations in the same pass.
