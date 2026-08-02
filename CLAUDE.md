# Fantasy Football Knowledge Base — Wiki Operating Instructions

This repo is a self-maintaining wiki, in the spirit of Andrej Karpathy's "LLM wiki"
approach: a vault of small, atomic, densely cross-linked markdown notes that Claude
builds and updates as new source material (podcast/media transcripts and appearances
from select fantasy football experts) comes in. The human mostly feeds in source
material; Claude does the writing, linking, and organizing.

## Structure

- `Home.md` — vault entry point
- `Experts.md`, `Players.md`, `Concepts.md`, `Sources.md` — top-level Maps of Content
  (MOCs) linking into each folder below
- `Experts/` — one note per analyst/host: their philosophy, known biases, track
  record, links to their takes
- `Players/` — one note per NFL player, aggregating dated, attributed takes over time
- `Concepts/` — strategy/scheme notes (e.g. Zero RB, streaming defense, positional
  scarcity, dynasty rebuild timing)
- `Formats/` — the formats actually played: [[Best Ball]], [[Dynasty]],
  [[Redraft (Standard)]], in that priority order (see `Formats.md`)
- `Sources/` — one note per ingested transcript/appearance, with front matter
- `_templates/` — starting shape for each note type

## Tracked experts (as of this writing)

- [[Chris Harris]] — Harris Football Podcast
- [[Matt Waldman]] — Rookie Scouting Portfolio (dynasty/prospect focus)
- [[Matt Harmon]] — Yahoo Sports

Only ingest takes from these tracked experts unless the user explicitly asks
to add another. If asked to add one, create their `Experts/<Name>.md` note
and link it from `Experts.md` before ingesting their content.

## Format priority

The wiki owner plays, in order of importance: [[Best Ball]] (highest) >
[[Dynasty]] > [[Redraft (Standard)]] (lowest). When a source's advice is
format-specific, tag the bullet with the format(s) it applies to, e.g.
`[Best Ball]` or `[Dynasty]`, and cross-post to the relevant `Formats/*.md`
note's "Expert Takes" section as well as the player/concept note. If a take
isn't format-specific, don't force a tag — leave it general.

## Core rules

1. **Atomic notes.** One file per entity. Don't merge players, don't create
   catch-all notes.
2. **Source-grounded.** Every claim in a Player/Concept note must cite the
   `[[Source]]` it came from, with expert + date. No unsourced assertions.
3. **Opinion, not fact.** Fantasy advice is subjective and time-sensitive. Frame
   claims as "According to [[Expert Name]] ([[Source Note]], YYYY-MM-DD)
   [Format if applicable]: ..." — never state an expert's take as settled truth
   in the wiki's own voice.
4. **Chronological order wins.** Within a note's "Expert Takes", bullets are
   ordered oldest → newest, so the last bullet is always the most current view.
   Recency carries weight: when takes conflict, the newer one reflects better
   information (injuries, camp reports, depth-chart moves), and an older take
   must never be written in a way that supersedes or overwrites a newer one.
   Keep both, dated, in order. See the ingestion-order rule below.
5. **Append, don't overwrite.** When a new source contradicts or updates an old
   take (e.g. after an injury or role change), add the new dated entry alongside
   the old one rather than deleting it. The history of how opinion shifted is
   valuable — don't erase it.
6. **Idempotent ingestion.** Before creating a note, search for an existing one,
   including under likely synonyms/nicknames (e.g. "CMC" vs "Christian
   McCaffrey"). Update in place; don't duplicate.
7. **Dense linking.** Use `[[wikilinks]]` liberally — every player mention, expert
   mention, and named concept should link to its note.
8. **Disagreement is signal.** When experts differ, record both takes rather than
   picking a winner or silently averaging them.
9. **File naming.** Filename = exact display name used in wikilinks (Obsidian
   resolves links by filename), e.g. `Players/Christian McCaffrey.md`,
   `Concepts/Zero RB.md`.

## Automated ingestion queue (`Sources/_inbox/`)

`scripts/check_new_episodes.py` reads each tracked show's public RSS feed and
stages a plain-text transcript at
`Sources/_inbox/<date>-<show-slug>-<title-slug>.md`, marking it `fetched` in
`scripts/state.json` (keyed by RSS `<guid>`). Tracked shows:

- **Reception Perception: The Show** ([[Matt Harmon]]) — only `[FULL EPISODE]`
  releases; clips are filtered out.
- **Harris Fantasy Football Podcast** ([[Chris Harris]]) — every episode.
- **Matt Waldman's RSP Cast** ([[Matt Waldman]]) — every episode.

Each staged file records how its transcript was produced in the
`transcript_source` front-matter field:

- **`whisper`** — local speech-to-text via `whisper.cpp` (`large-v3-turbo`) on
  the episode's public MP3 enclosure. Free, offline, no API key, ~24× realtime
  on this Mac. **This is the path for effectively every episode.**
- **`feed-transcript`** — a `<podcast:transcript>` tag on the RSS item.
  Disabled by default (`PREFER_FEED_TRANSCRIPTS = False`): the only such
  transcripts here are 8 RSP Cast episodes from a 2024 Blubrry trial whose ASR
  is measurably worse than Whisper's. Used automatically only if an episode has
  a transcript tag but no audio enclosure.

The script never touches git and never calls a paid API.

At the start of any session (and always as part of the daily scheduled task),
check `Sources/_inbox/` for staged files.

**Always ingest in strict chronological order, oldest episode first.** Staged
filenames are date-prefixed (`YYYY-MM-DD-<show>-<title>.md`), so sorting by
filename gives the correct order. This is not a nicety — expert opinion on a
player evolves (injuries, depth-chart changes, camp reports), and each
`Players/` note accumulates dated takes in file order. Ingesting oldest-first
means a more current take always lands *after* an older one, so the note reads
chronologically and a stale opinion can never appear to supersede a fresher
one. If you ever ingest out of order, insert the bullet in its correct
date position rather than appending it to the end.

For each staged file:

1. Treat its content as a new transcript — apply the full ingestion workflow
   below (steps 2–5), using the front matter already present (expert, show,
   date) instead of re-deriving it.
2. **No speaker labels.** Neither transcript source provides diarization.
   Infer who's speaking from context (introductions, how they refer to each
   other, subject matter). Most episodes are a consistent host pairing — see
   the relevant `Sources/` notes for who hosts what.
3. **Expect ASR errors on proper nouns**, especially player names. Observed
   examples: "Malik neighbors" (Nabers), "Romo Dunze" (Rome Odunze), "Jameer
   Gibbs" (Jahmyr Gibbs), "Debo Samuel" (Deebo Samuel), "Dijon Stribling"
   (De'Zhaun Stribling). Always normalize to the correct real-world spelling
   before creating or updating a `Players/` note, and check for an existing
   note under the correct spelling first (rule 6, idempotent ingestion). Never
   create a player note under a garbled ASR spelling.
4. Once fully ingested (the source note is created/updated and all extracted
   claims are woven into Player/Concept/Expert notes), move the file out of
   `Sources/_inbox/` into its permanent home per step 1 below, delete the
   staging copy, and update its entry in `scripts/state.json` to
   `"status": "ingested"`.

Whisper output has inconsistent capitalization/punctuation on long episodes
(a known long-form drift; content accuracy is unaffected). Don't treat
lowercase passages as lower-confidence — they're as accurate as the rest.

Episodes the pipeline fails to transcribe are logged to
`Sources/_needs-attention.md` by the script itself (not by you) and retried on
every run — that file is just visibility into what's stuck.

A separate, independent weekly scheduled task handles `git add`/`commit`/`push`
for the whole repo. Never run git commands as part of ingestion — the two are
intentionally decoupled.

## Ingesting a new transcript

When given a new podcast/media transcript, or a link/summary of one (including
from `Sources/_inbox/` above):

1. Create `Sources/<Show> - <YYYY-MM-DD> - <Expert>.md` from
   `_templates/Source.md`, filling in front matter (expert, show, episode, date,
   url) and a brief summary.
2. Add a row to `Sources.md`.
3. Pull out distinct, player- or concept-specific claims. For each:
   - Find or create the relevant `Players/<Name>.md` or `Concepts/<Name>.md`
     (from the matching template).
   - Append a dated bullet under "Expert Takes" citing the source and expert,
     tagged with a format per the "Format priority" section below when the
     take is format-specific.
   - Link back to the source note.
4. Update/create `Experts/<Expert>.md` with a link to the new source and, if
   their overall stance shifted, a short note on that.
5. Make sure the `Players.md` / `Concepts.md` / `Experts.md` MOCs link to any
   newly created notes.

## What NOT to do

- Don't fabricate takes, quotes, or stats not present in the source material.
- Don't collapse multiple experts' views into one unattributed "consensus" bullet.
- Don't generate the wiki's own rankings or predictions — it curates what experts
  said, it doesn't originate advice.
