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

## [2026-08-03] pipeline | Brandon Angelo promoted to tracked expert
Added [[Brandon Angelo]] (*Going Deep* co-host) as the fourth tracked expert —
evaluation-and-theory focused rather than rankings, so his value concentrates in
the concept layer. Rewrote 33 existing attributions across 28 files that had
labelled him "not a tracked expert". Corrected provenance is preserved: the
RB movement-skill framework and the pro-readiness-vs-ceiling framework are his.

## [2026-08-03] pipeline | Subagent ingestion protocol documented + cost tooling
CLAUDE.md now specifies one-subagent-per-transcript with fresh context, strictly
sequential (shared-file writes and rule 4 both forbid parallelism), verify and
commit between each. Added scripts/ingest_manifest.py, which precomputes the
page inventory and co-host roster into a ready-made agent prompt so agents stop
rediscovering the wiki on every run — a cost that otherwise grows as the wiki
grows. Measured baseline: ~126k tokens/episode, ~18.9M for the remaining 150.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 1.1.24 (2024-01-01)
Looser New Year's-week *Feel It or F**k It* with **Bob Harris** (not tracked;
not [[Chris Harris]]), covering ~20 players' 2024 redraft outlook. Created 14
player pages (QB: [[Anthony Richardson]], [[Joe Flacco]]; RB:
[[Kenneth Walker III]], [[Kyren Williams]], [[Raheem Mostert]],
[[James Connor]], [[Aaron Jones]], [[Zamir White]]; WR: [[CeeDee Lamb]],
[[Tyreek Hill]], [[Mike Evans]], [[Stefon Diggs]], [[Cooper Kupp]]; TE:
[[Travis Kelce]]) and 1 concept page ([[Injury-Agnostic Roster Construction]]).
**What materially changed:** (1) the 2024 #1-overall debate splits the hosts —
Waldman ranks [[Christian McCaffrey]] 1st, [[CeeDee Lamb]] 2nd, [[Tyreek Hill]]
3rd; Bob Harris takes Lamb over McCaffrey and Hill over Lamb — recorded as
disagreement, not flattened. (2) [[Scheme vs Talent]] gains two fresh 2024
cases: Cleveland's turnaround credited to O-line coach Tom Cable and
Stefanski's scheme more than to [[Joe Flacco]] himself, and [[Kyren Williams]]
graded explicitly as sub-top-10 talent producing top-10 output off the Rams'
line — with [[Derrick Henry]] joining via free agency flagged as the risk to
that read. (3) [[Derrick Henry]]'s own 2024 valuation is now "dead zone" round,
not low-end RB1, with a hoped-for Ravens landing spot. (4) [[Lamar Jackson]]
and [[Brock Purdy]]/[[C.J. Stroud]] get updated, materially unchanged headline
views (Jackson still unqualified QB1 despite the scheme-dependency label;
Purdy still edges Stroud). Index markers advanced from *(2023 takes, stale)*
to *(2024 takes, stale)* on all five updated player pages. ASR normalizations
included Kyron Williams→Kyren Williams, Ken Walker→Kenneth Walker III, Stefan
Diggs→Stefon Diggs, Cooper Cup→Cooper Kupp, Travis Kelsey→Travis Kelce, Brandon
Ayoub→Brandon Aiyuk, Devon Achan→De'Von Achane, Raheem Moser→Raheem Mostert.
## [2026-08-03] ingest | Matt Waldman's RSP Cast — Favorite 2023 NFL Storylines and 2023 Rookie Review (2024-01-04)
*RSP Film and Theory* with **Adam Harstad** (not tracked), a season-recap plus
full 2023 rookie-class review. Created 18 player pages (QB: [[Jordan Love]],
[[Dak Prescott]]; RB: [[Tank Bigsby]], [[Kendre Miller]], [[Chase Brown]]; WR:
[[Quentin Johnston]], [[Jaxon Smith-Njigba]], [[Zay Flowers]], [[Puka Nacua]],
[[Tank Dell]], [[Nico Collins]], [[Josh Downs]], [[Marvin Mims Jr.]],
[[Jalen Hyatt]], [[Rashee Rice]]; TE: [[Dalton Kincaid]], [[Luke Musgrave]],
[[Tucker Kraft]]) and 1 concept page ([[Role Difficulty and Replaceability]],
Harstad's "prefer the guy doing the harder thing" heuristic, applied to
Nico Collins/Tank Dell and to Rashee Rice's Mahomes-inflated role).
**What materially changed:** (1) Waldman gives an explicit personal 2023
rookie-WR tier (JSN, Addison, Nacua, Reed, Flowers, with Dell just outside),
recorded on [[Jordan Addison]] and [[Jayden Reed]] as updates — Reed in
particular gets "I wouldn't trade him for any of them," a real elevation.
(2) [[Quentin Johnston]] enters as the class's clearest bust risk, with a
specific catch-point mechanism rather than a vague "hasn't produced" read.
(3) [[Brock Purdy]] gets a durable, checkable career-arc forecast (comped to
early Brady/Warner/Wilson/Roethlisberger) — logged on [[Matt Waldman]]'s
expert page as an open prediction. (4) [[Dalton Kincaid]] vs [[Sam LaPorta]]:
Waldman explicitly keeps Kincaid ranked above LaPorta long-term despite
LaPorta clearly outproducing him as a rookie — also logged as a trackable
stated-preference-against-results item on Waldman's expert page.
(5) [[Lamar Jackson]] and [[Joe Flacco]] get reinforcing updates (Beckham
"best offense" quote, Flacco's on-film progression). A lengthy Bill
Belichick/Bill Walsh coaching-legacy debate and a "wins above .500" coaching
statistic aside were **not** ingested as wiki content — no fantasy-relevant
player claim was at stake. ASR normalizations included Jackson Smith and
Jigba→Jaxon Smith-Njigba, Riles Garrett→Myles Garrett, Kinkade→Kincaid, Rishi
Rice→Rashee Rice, Skymore→Skyy Moore.
## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 1.8.24 (2024-01-08)
Week 18 wrap with **Bob Harris** (not tracked; not [[Chris Harris]]). A fast
sweep across four crowded team situations. Created 16 player pages (RB:
[[Tony Pollard]], [[Michael Carter]], [[Austin Ekeler]], [[Josh Jacobs]],
[[Jordan Mason]], [[Elijah Mitchell]], [[Tyler Allgeier]]; WR: [[Gabe Davis]],
[[Khalil Shakir]], [[Drake London]], [[Michael Wilson]], [[Wan'Dale Robinson]],
[[Ronnie Bell]], [[Dontayvion Wicks]], [[Romeo Doubs]], [[Christian Watson]])
and 1 concept page ([[Healthy Enough to Play vs. Healthy Enough to Perform]],
a [[Brandon Angelo]] framework relayed by Waldman even though Angelo wasn't a
co-host this episode — logged on Angelo's own expert page since he's tracked).
**What materially changed:** (1) [[Michael Wilson]] graduates from a "not
given" one-liner in the 2024-01-04 episode to a full evaluative take now that
there's enough substance (route-running comp, health-contingent 2024 range).
(2) [[James Connor]]'s "toast" skepticism is reframed as a second-contract
finance story rather than a talent decline — a real nuance, not just
repetition. (3) [[Josh Jacobs]] vs. [[Zamir White]] recorded as a direct,
explicit comparison rather than two independent reads. (4) Buffalo's passing
game (Kincaid/Shakir/Cook) and Green Bay's receiver room (Wicks/Doubs/Watson/
Reed) each get an explicit "who gets squeezed out" argument. (5) One RB
question's ASR transcription could not be confidently resolved to a real
player name — no page was created rather than guess, and it's flagged in the
source summary for manual review. ASR normalizations included Mother
Tucker→Tucker Kraft (a filler-phrase/name collision), Amari DiMarcato→Emari
DeMercado, Javante Williams→Javonte Williams, one dale robinson→Wan'Dale
Robinson, Ekler→Ekeler.

## [2026-08-03] lint | Name consistency and dangling links after batch 5-7
Fixed "Austin Ekler" -> [[Austin Ekeler]] across 10 files. Notable: the error
originated with the earlier Opus-class single-episode agents; the Sonnet batch
agent independently produced the correct spelling. Unlinked [[Travis Etienne]]
(a conditional passing mention in the Tank Bigsby page, no substantive take —
per the rule that pages come only from real evaluative takes). Zero dangling
links, zero duplicate players, chronological order verified.
