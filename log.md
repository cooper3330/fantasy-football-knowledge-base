# Operation Log

Append-only chronological record of wiki operations. Newest entries at the
bottom. Format: `## [YYYY-MM-DD] <operation> | <subject>`.

Operations:
- **ingest** — a raw source was read and woven into the wiki
- **query** — a question was answered from the wiki (and, if durable, filed to `wiki/synthesis/`)
- **lint** — a health pass for contradictions, stale claims, orphans, gaps
- **pipeline** — transcription/backlog/infrastructure events

Never rewrite or delete past entries. Append only.

---

## [2026-08-01] pipeline | Wiki scaffolded
Initial vault structure created for three tracked experts (Chris Harris, Matt
Harmon, Matt Waldman) across Best Ball / Dynasty / Redraft formats.

## [2026-08-02] pipeline | Transcript source moved to local Whisper
Replaced a dependency on Apple Podcasts' local transcript cache (which stalled,
then began failing outright on macOS TCC authorization) with public RSS feeds +
local `whisper.cpp` transcription. Free, offline, ~24× realtime. Researched and
rejected: Spotify (no API access), YouTube (Chris Harris absent; Reception
Perception posts only segments), Taddy/Rephonic/Podscribe (cost), Podcast Index
(pass-through only), paid ASR (strictly worse than free local).

## [2026-08-02] pipeline | Backlog drain — 150 episodes
Two batches (50 + 100) transcribed locally, 150/150 succeeded, zero failures.
Covers Dec 2023 – Oct 2024. ~5.3 hours total at ~2.1 min/episode.

## [2026-08-02] pipeline | Reset Apple-derived wiki notes
The first 7 episodes had been ingested from Apple TTML transcripts, out of
chronological order (they are the newest episodes). Removed all wiki content
derived from them and returned those episodes to `pending` so every source is
processed identically — Whisper transcript, chronological order. Prior state
tagged `pre-reindex-apple-transcripts`.

## [2026-08-03] pipeline | Restructured to Karpathy llm-wiki pattern
Reorganized into the three-layer pattern: immutable `raw/` sources, LLM-owned
`wiki/`, and `CLAUDE.md` schema. Added `index.md` (page catalog) and this
`log.md`. Added `wiki/synthesis/` for filed query answers supporting draft and
waiver decisions. All 154 transcripts preserved and verified byte-identical
(1,614,588 words). Prior state tagged `pre-karpathy-restructure`.

## [2026-08-03] pipeline | Physical separation of ingested transcripts
Split the raw layer into `raw/transcripts/` (awaiting ingestion) and
`raw/ingested/` (done), so the folder itself is a visible work queue rather than
requiring a `state.json` query. Transcript *contents* remain immutable; the only
permitted change is this one relocation. Added `scripts/verify_integrity.py` to
reconcile state against disk — detects missing files, wrong tree, stale paths,
duplicate basenames, and orphans, with `--fix` to repair. Verified it catches and
repairs a simulated half-completed move.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — What Is Happening to NFL Careers? (2023-12-14)
Concept-heavy Film & Theory episode with guest Adam Harstad (not a tracked
expert; attributed by name). Key finding: 30+ production has collapsed
league-wide since ~2017 — 30+ share of 1,000-yard receiving seasons fell from a
stable ~33% to 7.7% — with no established cause. Created 3 concept pages
([[Aging Curves and Career Longevity]], [[Start Your Best Players]],
[[Scouting Bias and Player Archetypes]]) and 2 player pages. Materially changes
the [[Dynasty]] baseline: historical age curves overvalue older players.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It or F@#k It 12.18.23 (2023-12-18)
Rapid-fire Week 15 hot-take episode with co-host **Bob Harris** (not a tracked
expert, and not [[Chris Harris]] — attributed by name throughout). Created 22
player pages, 3 concept pages ([[Weak Quarterback Play and Receiver Value]],
[[Zone vs Man Route Running]], [[Scheme vs Talent]]), and cross-posted to
[[Best Ball]] and [[Redraft (Standard)]], which had no takes before this.
**What materially changed:** Waldman flips his own 2024 RB market call —
vindicated on [[Jahmyr Gibbs]] over [[Bijan Robinson]] (RB9 vs RB11), he now
pounds the table for *Robinson* because the premium moved to Gibbs; recorded as
a track-record note and a philosophy signal on [[Matt Waldman]] (he prices
players, not just ranks them). [[Christian McCaffrey]] locked as the
unqualified 2024 1.01 at age 28, which bounds the 12-14 aging-curve finding to
replacement-level players rather than elite ones. New durable framework: route
running vs speed, and the man/zone split, as Waldman's primary WR sorting
question. ASR name normalizations included Jalen→Jordan Addison, Jameer→Jahmyr
Gibbs, Brandon Iuk→Brandon Aiyuk, Trey→Tre Tucker, Miko→Nico Collins,
Traylon→Treylon Burks.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — The Cyclical Nature of Talent vs. Scheme + NIL (2023-12-21)
*RSP Film and Theory* with co-host **Adam Harstad** (not a tracked expert;
attributed by name — a different co-host from Bob Harris on the *Feel It or
F**k It* shows). Almost entirely conceptual. Created 3 concept pages
([[Running Back Size and Movement Skills]],
[[League Trend Cycles and Market Inefficiency]],
[[NIL and Player Development]]) and 5 player pages
([[Lamar Jackson]], [[Brock Purdy]], [[Deebo Samuel]], [[Derrick Henry]],
[[Saquon Barkley]]). **What materially changed:** the episode's title thread was
merged into the existing [[Scheme vs Talent]] page rather than duplicated — it
now carries the league-wide swing between talent-centric and scheme-centric
eras (Dec 2023 read: talent-centric, so atypical builds get used), and
Harstad's rejection of "system quarterback" as a label, with Peyton Manning as
the reductio. New disagreement recorded: Waldman calls [[Lamar Jackson]] more
scheme-dependent than [[Brock Purdy]] against a unanimous Footballguys staff —
logged as an open, checkable prediction on his expert page. New durable RB
framework (change of direction in tight space, with a claimed ~205–215 lb
ceiling on the trait) now sits under [[Christian McCaffrey]], [[Jahmyr Gibbs]]
and [[James Cook]]; [[Saquon Barkley]] enters as the counter-example. Waldman
track record expanded: he rebuilt his WR system after the Hakeem Butler miss
(A.J. Brown / Jefferson / Olave / Reed as claimed post-rebuild hits), so his
pre-2019 receiver calls should be weighted differently. ASR normalizations
included Debo→Deebo Samuel, Eckler→Ekler, Keyshawn→Deuce Vaughn, work
done→Warrick Dunn, Cordell/Paris→Cordarrelle Patterson, Hawkinson→Hockenson,
Munkin→Todd Monken, Marlon Roll→Myron Rolle.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Going Deep: Pacing/Control of Elite Movers + Harrison Jr. vs Nabers (2023-12-21)
*Going Deep* with co-host **Brandon Angelo** (not a tracked expert; attributed by
name — a third co-host, distinct from Adam Harstad and Bob Harris). **Second
episode dated 2023-12-21**, filed as
[[Matt Waldman's RSP Cast - 2023-12-21 (Pacing and Control)]] so it doesn't
collide with the *Film and Theory* page. It was recorded **first** — the Film
and Theory episode credits "a point raised by Brandon Angelo on *Going Deep* the
night before" — so its bullets were inserted *above* the Film and Theory bullets
on every shared page rather than appended.
Created 10 player pages ([[Malik Nabers]], [[Marvin Harrison Jr.]],
[[Breece Hall]], [[Nick Chubb]], [[David Montgomery]], [[Isiah Pacheco]],
[[Drew Lock]], [[Gardner Minshew]], [[Sam LaPorta]], [[Kyler Murray]]) and 3
concept pages ([[Pace Control and Movement Intellect]],
[[Prospect Pro-Readiness vs Ceiling]],
[[Player Development and Coachability]]).
**What materially changed:** (1) The provenance of the RB size argument is now
correct — [[Running Back Size and Movement Skills]] was *updated, not
duplicated*, with an origin block showing the ~205–215 lb ceiling claim is
**Angelo's**, stated on film over a James Cook clip, and [[Nick Chubb]] enters
as an explicit counter-example that bounds the rule. (2) [[Derrick Henry]]
picks up his first real fantasy knock in this wiki: once a defense keys him,
"you're not fixing it mid-game," and the tackle-difficulty comparison inverts
toward the small movers — his index line was rewritten. (3) New rookie-draft
framework: pro-readiness graded separately from ceiling, with both hosts on
[[Malik Nabers]] over [[Marvin Harrison Jr.]] "by a healthy margin" against
industry consensus — logged as an open, checkable call on [[Matt Waldman]]'s
page, along with Waldman's three-item receiver technique checklist (release
work, catch-window selection, overhand vs underhand attack position).
(4) [[Bijan Robinson]] gains a usage mechanism — "a rhythm runner who gets
better with the more touches he gets" against Atlanta's scheme-over-personnel
approach. (5) The NIL/one-and-done material was merged into the existing
[[NIL and Player Development]] rather than given a new page; the
coachability/organizational half was split out as its own concept, anchored by
Waldman's [[Sam LaPorta]] floor scenario and the long [[Drew Lock]] case study.
ASR normalizations included Malik Neighbors→Malik Nabers, Margaret/Mark Richard
Jr.→Marvin Harrison Jr., Bruce Hall→Breece Hall, Isaiah→Isiah Pacheco, Robert
Sala→Robert Saleh, Drew Locke→Drew Lock, Chad Rider→Chad Reuter, Cecil
Lammy→Cecil Lammey, Sigmund Blum→Sigmund Bloom, Blinkoff→Biletnikoff.
