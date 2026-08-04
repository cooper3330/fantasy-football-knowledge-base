---
type: log
tags: [log]
---

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
agent independently produced the correct spelling. Unlinked the `Travis Etienne` wikilink
(a conditional passing mention in the Tank Bigsby page, no substantive take —
per the rule that pages come only from real evaluative takes). Zero dangling
links, zero duplicate players, chronological order verified.

## [2026-08-03] pipeline | Fixed state.json race between drain and ingestion
The transcript drain and wiki ingestion both mutate scripts/state.json, and the
drain held an in-memory copy for the whole run while rewriting the entire file
after every episode — so a concurrent ingestion's changes would be silently
reverted, re-marking `ingested` episodes as `fetched`. Added scripts/state_io.py
(exclusive flock + re-read + atomic temp-file rename) and routed both writers
through it. Verified with a simulated race: a concurrent change now survives a
stale writer. Two bugs were caught by that test rather than in production — a
kwargs/positional `guid` collision that would have crashed the drain on its
first episode, and its non-fix in the function body instead of the signature.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Adam's 2023 Post-Rookie-Year Prospect Model: RSP Film and Theory with Adam Harstad (2024-01-11)
*RSP Film and Theory* with **Adam Harstad** (not tracked). Entire episode is
Harstad's [[Post-Rookie-Year Receiver Model]] (new concept page) — a
touchdown-adjusted yards-per-route-run + usage-rate score — applied to the
full 2023 rookie WR class. Created 4 player pages ([[Cedric Tillman]],
[[Tyler Scott]], [[Jonathan Mingo]], [[Demario Douglas]]) and updated 13
existing rookie-WR pages. **What materially changed:** (1) [[Rashee Rice]] —
Waldman names this his single biggest 2023 pre-draft miss (had him 44th
overall) and now sees real Tyreek-Hill-level upside, though the
manufactured-role downside case (independently echoed by Matt Harmon) is
equally live. (2) [[Dontayvion Wicks]] — the model's single biggest
buy-vs-market-price in the class; Waldman upgrades him from a hold to an
active trade target. (3) The season-long [[Drake London]] vs. [[Zay Flowers]]
debate is closed decisively toward London. (4) [[Puka Nacua]]'s rookie season
scores as the single best in the model's 2006-2023 sample, expanding
Harstad's historic "big four" to a "big five" — Waldman notes, for
calibration, that his own pre-draft grade on Nacua was a modest hit (31st),
not a bold call. (5) [[Tank Dell]] lands in a historically bust-free score
bucket alongside Mike Evans and Julio Jones, though size/durability and the
[[Nico Collins]] role-difficulty argument keep Waldman's personal ranking of
him below that bucket's other names. One bottom-tier rookie WR's name could
not be confidently resolved from the ASR transcript ("Xavier Gibson," likely
Xavier Hutchinson) — no page created, flagged in the source summary for
manual review. Also logged two further self-admitted Waldman track-record
items: Kayshon Boutte (miss, no page) and the Nacua calibration note, both
on [[Matt Waldman]]'s expert page.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — The Safest RB in the Draft, the Sleeper Miscast as a Gadget, the Keon Coleman Rollercoaster, and Penix and Punishment (2024-01-11, Going Deep)
*Going Deep* with [[Brandon Angelo]] (tracked). The second of two episodes
both dated 2024-01-11 — filenames disambiguated as "(Post-Rookie Model)" and
"(Going Deep - Draft Prospects)" per the existing 2023-12-21 naming
precedent. Entirely pre-draft 2024 prospect scouting. Created 4 player pages:
[[Blake Corum]] (RB, Michigan — Angelo's "safest RB in the class" case, built
on [[Pace Control and Movement Intellect]] rather than measurables),
[[Michael Penix Jr.]] (QB, Washington — outlook dominated by injury history;
both hosts want a Jordan-Love-style bench runway), [[Keon Coleman]] (WR,
Florida State — the title "rollercoaster," public perception overcorrecting
from athletic-freak to overrated; real scheme-dependency risk), and
[[Ainias Smith]] (WR/RB, Texas A&M — the "sleeper miscast as a gadget," ASR
name normalized from "Aniah/Anais/Elias Smith"). **What materially changed:**
(1) [[Treylon Burks]]'s outlook takes a real hit — "his injury ship has kind
of sailed," a genuine downgrade from the "talent to be mined" framing three
weeks prior. (2) [[Pace Control and Movement Intellect]] gains a new,
explicitly named mechanism — "compensatory skill" — via a Frank
Gore/Devin Singletary/Adrian Peterson discussion, plus the clearest single
statement yet of why slower processors read plays better ("the faster you
play, the faster you need to process the information"). (3)
[[Player Development and Coachability]] gains a QB-durability angle: young
quarterbacks who take a physical beating either recover with a veteran
runway (Steve Young, Terry Bradshaw, Jim Plunkett) or don't (Trent Edwards,
Carson Strong), and coaches should proactively pull back playing time before
a beaten-up young QB starts "seeing ghosts." An extended Vrabel/Belichick
coaching-carousel discussion was **not** ingested as wiki content, aside from
the Burks aside — no fantasy-relevant player claim otherwise at stake.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It, guest Daniel Harms (2024-01-15)
*Feel It or F**k It* with guest **Daniel Harms** (Football Guys/NFL33.com —
not tracked), filling in for Bob Harris. Episode's RSS title says "1.8.24"
but internal references confirm a 2024-01-15 publish date (a week after
[[Matt Waldman's RSP Cast - 2024-01-08]]); flagged as a likely upstream title
typo in the source summary. Created 10 player pages spanning current NFL
players ([[Michael Gallup]], [[De'Von Achane]], [[Tua Tagovailoa]]) and 2024
draft prospects ([[Drake Maye]], [[Bo Nix]], [[Brian Thomas Jr.]],
[[Ricky Pearsall]], [[Braelon Allen]], [[Troy Franklin]], [[Caleb Williams]]).
**What materially changed:** (1) [[Tony Pollard]] — a real one-week reversal;
both Waldman and Harms flip from "real rebound odds" to skeptical, citing a
lack of vision in condensed spaces and lost explosiveness. (2)
[[Travis Kelce]] — Harms pushes back hard on Waldman's own January 1 decline
read, attributing the down year to two specific injuries rather than
decline; recorded as a live, unresolved disagreement per rule 9 rather than
flattened into one view. (3) [[Rashee Rice]] gets its most detailed positive
read yet from a Chiefs-focused analyst, reinforcing the reversal already
logged from the 2024-01-11 Post-Rookie Model episode. (4) [[Keon Coleman]]
gets independent third-source corroboration of the [[Brandon Angelo]]/Waldman
take from four days earlier, plus a new mechanism (Jordan Travis's injury,
not Coleman's play, explains his softened draft stock). ASR normalizations:
Drake May → [[Drake Maye]], Ricky Purcell → [[Ricky Pearsall]], Braylon Allen
→ [[Braelon Allen]]. An extended Chicago Bears coaching-security/Fields-vs-
Williams speculation thread was mostly **not** ingested as wiki content, aside
from one sentence of situational context logged on [[Caleb Williams]]'s page.

## [2026-08-03] ingest | Reception Perception: The Show — Wild Card Weekend Recap (2024-01-16)
**First [[Matt Harmon]] episode ingested into this wiki.** Everything prior
was Matt Waldman's RSP Cast; Harmon has his own expert page, populated here
for the first time (Background/Philosophy/Track Record were previously
empty). Co-host **James Koh** (not tracked, distinct from Matt Waldman's
co-hosts) attributed by name throughout — ASR renders his name as "James
Go"/"James Gov"/"James Coe," normalized to James Koh. Raw/ingested paths for
this show are `raw/transcripts/reception-perception/` and
`raw/ingested/reception-perception/`, not `rsp-cast/`. A Wild Card recap
episode — game-recap content is low-durability by nature, so ingestion
favored evaluation reads over play-by-play. Created 1 player page
([[Jared Goff]]) and 1 concept page ([[Reception Perception Methodology]],
capturing Harmon's durable WR-charting framework — success rate vs.
press/man/zone, route-type and alignment splits, the 3-game-to-8-game
sampling process, and the cross-class "stacked board" tier system).
**What materially changed:** (1) [[Jordan Love]] gets the strongest praise of
any quarterback logged in this wiki to date — Harmon says he wouldn't take
10 other QBs over him given age/contract, ranking him above [[Dak Prescott]],
Trevor Lawrence and Jalen Hurts. (2) [[Tua Tagovailoa]] gets the harshest read
yet ("straight up bad"), benchmarked directly against new page
[[Jared Goff]] — Harmon pegs Tua's ceiling just below Goff's, itself outside
a top-12 QB conversation. (3) [[Cooper Kupp]]'s decline case sharpens
considerably: Harmon puts 50/50 odds that ankle-injury-driven explosiveness
loss is permanent, directly citing Reception Perception's own man-coverage
separation data showing [[Puka Nacua]] now out-separates him. (4)
[[Nico Collins]] gets a specific redraft ADP forecast (waiver-wire price to
2nd/3rd round) off a Wild Card-clinic performance alongside [[C.J. Stroud]].
(5) [[Joe Flacco]]'s outlook shifts from "starter competition" to "likely
veteran-backup market" after Cleveland's Wild Card exit. Not ingested as wiki
content: a lengthy Cowboys/Belichick/Vrabel/Deion-Sanders coaching-carousel
discussion (no fantasy-relevant player claim at stake).

## [2026-08-03] pipeline | Concurrent transcript drain note
A transcript drain is running alongside this ingest batch, continuing to add
new Reception Perception episodes under `raw/transcripts/reception-perception/`
(now running well past January 2024 into 2025). These are out of scope for
this ingest and were left untouched; only the three transcripts explicitly
assigned were processed, oldest-first, per rule 4.

## [2026-08-03] ingest | Reception Perception: The Show — College Standouts & NFL Divisional Round Preview (2024-01-18)
Second [[Matt Harmon]] episode, with co-host **James Koh** (not tracked; ASR
"James Coe" normalized). Two halves: early (3-game-sample, explicitly
non-final) 2024 draft-prospect charting on the consensus top three receiver
prospects, and a betting-heavy Divisional Round preview. Created 3 player
pages ([[Rome Odunze]] — ASR "Romo Dunze"/"Romo Dunzey" normalized to his
real name; [[John Metchie III]] — ASR "John Mechie" normalized;
[[Xavier Hutchinson]]) and substantially expanded the
[[Reception Perception Methodology]] concept page with the fullest on-air
demonstration yet of Harmon's charting metrics (press/curl-route success
rates, alignment share) and his cross-class "stacked board" tier system.
**What materially changed:** (1) Harmon's charting independently corroborates
the existing Waldman/Angelo pre-draft reads on [[Marvin Harrison Jr.]] (elite
press-coverage separator, ceiling still ahead of pro-readiness) and
[[Malik Nabers]] (ranked 3rd of the elite trio in separation/contested-catch/
hands despite the "60 to zero" deceleration praise) — a second, independent
data source agreeing with the RSP Cast's earlier read, not a new
disagreement. (2) [[Ja'Marr Chase]] and [[Drake London]] both gain a durable
pedigree marker: one of only five receivers (with Chris Olave, DeVonta
Smith, Garrett Wilson — not tracked) ever to earn Harmon's tier-one "stacked
board" grade. (3) [[Nico Collins]] gets a specific role-difficulty mechanism
(cover-6 in-breaking route data against elite linebackers) reinforcing his
2024-01-16 breakout read, while [[Noah Brown]]'s IR placement and
[[Xavier Hutchinson]]'s limited usage leave Houston's receiver room
dangerously thin behind Collins going into a tougher Baltimore defense.
(4) [[Stefon Diggs]] picks up a real, new role-dilution mechanism — Buffalo
hiding him in the slot specifically to dodge opposing CB1s — not present in
his prior entries. Per the low-durability guidance for game-recap/preview
content, most of the divisional-round betting-line and prop material was
**not** ingested; only matchup mechanisms with forward-looking evaluative
content were kept (see the source page's "Not given pages" list for the
full skip list: Josh Allen, Patrick Mahomes, Baker Mayfield, Robert Woods).

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 1.22.24 (2024-01-22)
Back to [[Matt Waldman]]'s RSP Cast with co-host **Bob Harris** (not tracked,
not [[Chris Harris]]) after the two-episode Reception Perception detour.
Divisional Round wrap plus Conference Championship preview, then a distinct
second half of Waldman's own first detailed 2024 QB prospect reads. Created
4 player pages ([[Rashad Bateman]], [[Chris Godwin]], [[Jayden Daniels]],
[[J.J. McCarthy]]). **What materially changed:** (1) [[Jordan Love]] gets a
detailed defense of his Divisional Round pick-six moment as rookie-starter
growing pains, plus a "top five QB production" claim for his final month of
2023 comparable to [[Lamar Jackson]]'s — reinforces Harmon's independent
praise from the prior two episodes with a second, differently-reasoned
source. (2) [[Brock Purdy]] gets a specific, actionable redraft claim: early
ECR ranks him outside the top-12 quarterbacks, which Waldman calls "a
mistake" he intends to exploit. (3) [[Devin Singletary]] reverses hard from
the December 2023 "feeling it" read to no longer being Houston's presumptive
2024 starter — a real reversal, not corroboration, kept alongside the old
take per rule 5. (4) [[Khalil Shakir]] is now explicitly rated above both
[[Gabe Davis]] and [[Stefon Diggs]] on Buffalo's depth chart. (5) Real,
if vague, smoke reported around [[Stefon Diggs]] and the Bills organization
— "there's got to be more to that story" — logged as a live, unresolved
signal rather than a firm claim. (6) On the three 2024 QB prospects Waldman
now grades himself for the first time, two are live disagreements with
guest Daniel Harms's 2024-01-15 reads rather than confirmations: more
bullish than Harms on [[Bo Nix]], more skeptical than Harms on
[[Drake Maye]] — both logged per rule 9 without picking a winner. (7)
[[Michael Penix Jr.]] downgrades from the 2024-01-11 bench-runway framing to
a "journeyman starter" grade. The [[Matt Waldman]] expert page also picks up
its first detailed description of the Rookie Scouting Portfolio product
itself (19th year, $21.95, pre/post-draft two-part structure) from Waldman's
own on-air description. ASR normalizations: none required beyond standard
name-drift cleanup (no new garbled names introduced this episode beyond
already-normalized ones).

## [2026-08-03] ingest | Reception Perception: The Show — Some Fun Games in the Divisional Round (2024-01-23)
Third [[Matt Harmon]] episode, with co-host **James Koh** (not tracked). A
Divisional Round recap across all four games, heavier on free-agency/team-
building mechanics than the two prior episodes; coaching-carousel speculation
(McDermott's job security, a hypothetical Ben Johnson pitch) was not ingested
per the low-durability guidance. No new player pages — all 18 touched pages
already existed. **What materially changed:** (1) [[Stefon Diggs]] gets the
fullest injury theory yet (unreported oblique/back injury since ~Week 10)
behind a steep 2nd-half production collapse, plus real trade/restructure
mechanics ($32M dead cap rules out a cut). (2) Green Bay's WR hierarchy gets
its clearest ranking yet — Harmon picks [[Jayden Reed]] as the receiver with
the best odds to become a true number one (an explicit Amon-Ra St. Brown
comp), [[Dontayvion Wicks]] second, [[Romeo Doubs]] a clear fourth, and
[[Christian Watson]]'s case downgraded to resting on size/speed alone with no
route-running argument behind it. (3) [[Brock Purdy]] gets a direct, on-record
disagreement between experts: Waldman calls him "exposed as nothing other
than what he is" (a good QB) after the Divisional Round win, Harmon calls the
same game "a bad game" and grades him "top 20," not elite-tier — logged as an
open disagreement per rule 9, not flattened. (4) [[Mike Evans]] and [[Baker Mayfield]] both get free-agency mechanics (dollar figures, suitor teams,
Detroit's cap space/culture fit for Evans). (5) [[John Metchie III]] gets a
real downgrade — "has proven nothing to this point in his career" — after a
Wild Card flash three episodes prior. (6) [[Aaron Jones]] gets "criminally
underrated" praise alongside a durability concern and a call for Green Bay to
draft a real RB2. (7) [[C.J. Stroud]] gets his first real bad-game caveat in
this wiki (confused, no counterpunch once Nico Collins was taken away), framed
as a structural Baltimore-scheme problem rather than a talent verdict.
[[Nico Collins]], [[Devin Singletary]], [[Gabe Davis]], [[Khalil Shakir]],
[[Noah Brown]] and [[Jared Goff]] get reinforcing/corroborating updates. No
new ASR name garbles this episode.

## [2026-08-03] ingest | Reception Perception: The Show — Head Coaching News & Conference Championship Breakdowns (2024-01-25)
Fourth [[Matt Harmon]] episode, with co-host **James Koh** (not tracked). Two
halves: a head-coaching carousel roundup (Atlanta's open search, Chargers/
Harbaugh, Titans hiring Brian Callahan, Raiders retaining Antonio Pierce plus
hiring Tom Telesco as GM, Patriots promoting Gerard Mayo) and a Conference
Championship preview. Per the low-durability guidance, almost none of the
coaching material was ingested — no specific player's role was tied to any of
these hires in the episode. The one exception: unconfirmed chatter that Ben
Johnson is close to taking the Washington HC job, logged on [[Jared Goff]]'s
page (explicitly flagged as rumor) since it bears directly on his
already-open "what happens once Ben Johnson leaves Detroit" question. No new
player pages — all 10 touched pages already existed. **What materially
changed:** (1) the fullest head-to-head receiver-ranking exercise in this
wiki — Harmon explicitly ranks the five receivers remaining in the playoffs:
[[Brandon Aiyuk]] #1 ("best pure receiver," expects 100 yards vs. Detroit's
league-worst secondary), [[Amon-Ra St. Brown]] #2 overall but #1 by team
value ("in a runaway"), [[Deebo Samuel]] #3 ("a true game wrecker"),
[[Zay Flowers]] #4 (real "superstar tier" future upside flagged, but a tough
outside-alignment AFC Championship matchup), [[Rashee Rice]] #5/last ("the
most limited of these five," capped at a Cooper-Kupp-archetype ceiling
despite Puka-Nacua-range rookie efficiency). (2) [[Isiah Pacheco]] gets his
first real bell-cow question logged, plus a live offensive-line injury risk
(Joe Thuney) ahead of the AFC Championship. (3) [[Jared Goff]] gets a
Shanahan-history/blitz-vulnerability note ahead of a game both hosts expect
Detroit to lose comfortably. (4) [[Brock Purdy]] and [[Christian McCaffrey]]
get direct matchup-specific reinforcements of prior reads.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 1.29.24 (2024-01-29)
*Feel It or F**k It* with **Bob Harris** (not tracked; not [[Chris Harris]]).
Conference Championship wrap plus a Senior Bowl/Shrine Game prospect
quick-hitters segment. Created 11 new player pages: [[Jameson Williams]]
(WR, DET — real but hedged optimism, an explicit "Gabe Davis factor"
overdraft warning), two current stars who'd never gotten their own page
despite plenty of prior mentions — [[Patrick Mahomes]] (specific 2024
redraft value call) and [[Jalen Hurts]] (introduced via a Lamar Jackson
value comparison, Kellen Moore OC hire flagged as a live variable) — and
eight 2024 draft prospects from the Senior Bowl/Shrine Game: [[Jabari Small]], [[Blake Watson]], [[Jonathan Brooks]] (RB); [[Malik Washington]],
[[Xavier Legette]], [[Malachi Corley]], [[Javon Baker]] (WR); [[Spencer Rattler]] (QB). **What materially changed:** (1) [[Lamar Jackson]] gets a
detailed, personal defense of his AFC Championship performance plus a
concrete 2024 redraft value call — expected to supplant [[Patrick Mahomes]]
at QB2 (maybe QB1), with the receiver-room injury context (Rashad Bateman,
Odell Beckham Jr., Mark Andrews/Isaiah Likely, lost J.K. Dobbins) offered as
the reason for expected year-two growth under Todd Monken. (2) [[Brock Purdy]] gets a direct rebuttal to Harmon's 2024-01-23 "bad game" critique —
Waldman frames his doubters as chasing the wrong (loud, obvious) QB traits
and credits a stacked supporting cast, while flagging real front-office
skittishness risk if SF doesn't win the Super Bowl. (3) [[Jared Goff]]'s Ben
Johnson/Washington rumor firms up further ("baked into the cake"); Waldman
separately states a general "we overrate coordinators" philosophy as
context. (4) [[Travis Kelce]] and [[Sam LaPorta]] both get reinforcing
updates. (5) [[Ricky Pearsall]] gets independent third-source
corroboration of the existing Puka-Nacua-comp sleeper case. No ASR
normalizations required beyond the standing Jameson Williams "Jamison
Williams" garble, resolved per rule 7.

## [2026-08-03] ingest | Reception Perception: The Show — Conference Championship Review & More Coaching Hires (2024-01-30)
Fifth [[Matt Harmon]] episode, with co-host **James Koh** (not tracked).
Conference Championship recap plus several coordinator hires, filtered per
the low-durability-on-coaching-churn-alone standard: only hires tied to a
specific player's role were ingested. One new player page: [[Bryce Young]]
(QB, CAR — extended evaluation: real physical limitations mean an
accuracy/processing-only path to success, rookie year explicitly not
treated as a settled verdict given a nonfunctional supporting cast). **What
materially changed:** (1) [[Lamar Jackson]] gets Harmon's most critical read
in this wiki yet — 3 turnover-worthy throws, a near-total abandonment of the
run game (563rd-of-568 games league-wide in design-run rate), an open
"are playoff losses mounting" question — a harder-nosed counterweight to
Waldman's more forgiving 2024-01-29 post-game read, while Harmon still calls
him a top-three QB outright. (2) Atlanta's new OC hire (Zach Robinson, ex-
Rams) gets graded as a probable scheme unlock for [[Bijan Robinson]]
(man/gap run fit) and [[Drake London]] (Nacua/Kupp-style in-breaking
routes), with [[Tyler Allgeier]] expected to stay involved as a
complementary piece. (3) Tampa Bay loses OC Dave Canales to Carolina's HC
job — reopens the scheme outlook for [[Baker Mayfield]], [[Mike Evans]]
(credited for "unleashing" him) and [[Chris Godwin]] (whose 2023 alignment
misuse Harmon calls "a gigantic mistake," only fixed by Week 14-15). (4)
Philadelphia's Kellen Moore hire for [[Jalen Hurts]] gets its first actual
grade — "definitely an upgrade" but "something left to be desired," with a
specific structural worry about his shotgun-exclusive usage. (5)
[[Patrick Mahomes]], [[Travis Kelce]], [[Zay Flowers]], [[Rashad Bateman]]
and [[Jameson Williams]] get reinforcing/corroborating updates — notably
Bateman played all of 2023 healthy per Harmon, a partial complication of
Waldman's "always hurt" framing from the prior episode. No new ASR name
garbles this episode.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — 2024 Sr. Bowl Fallout and Fave Developmental Picks: Going Deep with Brandon Angelo (2024-02-01)
A dense, prospect-only *Going Deep* episode covering Senior Bowl/Shrine Game
week — both hosts tracked, no untracked guest this time. Twelve new
2024-draft-prospect pages: [[Roman Wilson]], [[Devontez Walker]],
[[Brendan Rice]], [[J. Michael Sturdivant]] (WR); [[Ray Davis]],
[[Dylan Laube]], [[Deshaun Fenwick]], [[Mario Anderson]] (RB);
[[Tanner Mordecai]], [[Jack Plummer]], [[Joe Milton III]] (QB); and
[[Brevyn Spann-Ford]] (TE), the episode's most detailed single breakdown —
a documented technique-improvement arc from a lost-looking 2022 blocker to
a competent one by late 2023. **What materially changed:** (1) A genuine
live disagreement opens on [[Bo Nix]] — Angelo downgrades him hard after
watching him throw at the Senior Bowl ("Mitch Trubisky syndrome"), landing
much closer to guest Daniel Harms's prior skepticism than to Waldman's own
bullish 2024-01-22 read, a real 3-way split. (2) [[Drake Maye]] gets
Waldman's promised re-watch, and skepticism holds — a new Jake Locker comp
plus a structural North-Carolina-QB-archetype risk (Trubisky/Howell/Maye)
flagged independent of individual talent; see
[[Scouting Bias and Player Archetypes]]. (3) [[J.J. McCarthy]] gets a
significant new grade, benchmarked explicitly against Will Levis's rookie
year (both hosts admit they had Levis ungraded pre-draft). (4)
[[Devontez Walker]] gets a real stock disagreement logged — outside buzz
near the late first round vs. Angelo's own late-Day-3 grade, which he's
sticking with. (5) [[Michael Penix Jr.]] gets an updated, medical-contingent
draft-range call (top-20/25 if he checks out). (6) [[Xavier Legette]] gets
tempered after live reps looked less dominant than his frame suggested.
[[Ricky Pearsall]], [[Malachi Corley]] and [[Spencer Rattler]] get
reinforcing updates. A biographical aside on [[Brandon Angelo]] himself —
a former Big Ten sprinter who raced [[Tyreek Hill]] twice as a
high-schooler — is logged on his expert page. ASR note: normalized several
garbled prospect names ("Dylan Lobby" → [[Dylan Laube]], "Sean Fenwick" →
[[Deshaun Fenwick]], "Brevin Spanford"/"Reverend Spanford" →
[[Brevyn Spann-Ford]], "Michael and[erson]" → [[Mario Anderson]], moderate
confidence); one injured prospect referred to as "Rashan Rashin Ali" could
not be confidently resolved and was omitted per rule 7 rather than guessed.

## [2026-08-03] ingest | Reception Perception: The Show — Arthur Smith to Pittsburgh, Seahawks Personnel & Senior Bowl Takes (2024-02-01)
Sixth [[Matt Harmon]] episode, with co-host **James Koh** (not tracked); same
publish date as the RSP Cast episode above but a different show. Seven new
pages: [[George Pickens]], [[Diontae Johnson]] (WR, PIT — both charted
beneficiaries of the Arthur Smith hire), [[Najee Harris]], [[Jaylen Warren]]
(RB, PIT), [[Ladd McConkey]] (WR, Georgia prospect — the strongest of three
early-charted 2024 receivers this episode), [[Tyler Lockett]] (WR, SEA) and
[[Terry McLaurin]] (WR, WAS). **What materially changed:** (1) Arthur
Smith's hire in Pittsburgh gets this wiki's fullest durable-coaching-move
case study — Harmon backs a process-over-results defense with actual
charted route-tree data ([[George Pickens]]'s 7.7%/10.7% dig/slant rate
under Matt Canada vs. [[Drake London]]'s 16.6%/24.5% under Smith), directly
projecting more middle-of-field volume for Pickens and Diontae Johnson; see
[[Scheme vs Talent]]. (2) The standing "what happens once Ben Johnson
leaves Detroit" question, open since mid-January, is **resolved** — Johnson
turned down every head-coaching job including Washington and is staying as
Lions OC — updating [[Jared Goff]] (a sharper "he can't take you much
further" follow-up plus a Detroit X-receiver need, floating a long-shot
[[Tee Higgins]] trade scenario) and [[Jameson Williams]] (Harmon's most
technically critical read yet: "shaky hands," not a "go up and get it"
guy). (3) Mike McDonald's move from Baltimore DC to Seattle HC reopens
[[Jaxon Smith-Njigba]]'s role outlook (a "more premier role" floated) and
puts [[Tyler Lockett]]'s roster spot in real doubt. (4) Early 3-game RP
charting on [[Brian Thomas Jr.]] and [[Keon Coleman]] (the latter a real
downgrade, with an explicit Treylon Burks bust comp) plus a new page for
[[Ladd McConkey]] (previously dismissed only in passing, now the strongest
of the three). (5) [[Quentin Johnston]] revisited as the standing
scheme-fit cautionary tale — now described as one of the worst RP rookie
seasons ever. No new ASR name garbles beyond the standing "Lad
McConkey"/"Deontay Johnson"/"Jalen Warren" garbles, resolved per rule 7 on
their respective new pages.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — The NFL Hall of Fame (And Our Picks for the '24 Class) (2024-02-02)
*RSP Film and Theory* with co-host Adam Harstad (not tracked). Entire episode
is a Pro Football Hall of Fame nominee/institution discussion for the Class
of 2024 — no current NFL players, prospects, or fantasy news, and per the
DURABILITY JUDGEMENT no player pages were created for any retired candidate
(Andre Johnson, Fred Taylor, Patrick Willis, Antonio Gates, etc.). **What
materially changed:** two general evaluation frameworks logged against
existing concept pages as reinforcing, cross-context restatements — (1)
Harstad's peak-vs-longevity career-value heuristic (league-average baseline,
not replacement baseline) plus his RB/middle-linebacker
shortest-career-most-forgivable wear-and-tear point, added to
[[Aging Curves and Career Longevity]]; (2) Harstad's generalized "transcend
the system" test, explicitly self-identified as "the Brock Purdy discussion"
applied to Andre Johnson, added to [[Scheme vs Talent]]. No player, expert
stance, or index headline changes. No name garbles requiring normalization —
all names discussed (Eric Allen, Torry Holt, Andre Johnson, Fred Taylor,
etc.) are retired players outside this wiki's tracked scope.

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 2.5.24 (2024-02-05)
*Feel It or F**k It* with **Bob Harris** (not tracked; not [[Chris Harris]]),
Super Bowl LVIII week. Seven new pages, the most of any episode logged so
far: [[Brian Robinson Jr.]] and [[Tyjae Spears]] (RB, coaching/personnel-
change value calls), four tight ends — [[Brycen Hopkins]], [[Pat Freiermuth]], [[Kyle Pitts]], [[Brock Bowers]] (2024 prospect) — and
[[Desmond Ridder]] (QB, ATL), created because his play is the explicit
mechanism Waldman uses to explain Atlanta's 2023 passing-game struggles.
**What materially changed:** (1) Cliff Kingsbury's move to Washington OC
opens both a positive redraft case for [[Brian Robinson Jr.]] (James Connor/
Arizona comp) and a new landing-spot risk on [[Caleb Williams]] if Washington
trades up to 1.01 — "the worst end of Caleb Williams to start his career,"
more Kyler-Murray-esque than structured. (2) [[Derrick Henry]] gets an
explicit [Best Ball] ADP value call — 7th/8th round is a market miss on a
2023 RB12 — plus a repeated Ravens landing-spot wish-cast. (3) The Arthur-
Smith-to-Pittsburgh case study on [[Scheme vs Talent]] gets its specific
mechanism: [[Desmond Ridder]]'s inability to read the field dynamically
forced Atlanta's 2023 offense into simplified, static routes, which Waldman
argues explains the [[Bijan Robinson]]/[[Drake London]]/[[Kyle Pitts]] usage
complaints better than a talent or scheme-quality read — and raises a fresh
usage worry for [[Pat Freiermuth]] in Pittsburgh (an explicit Kyle-Pitts-
underuse comparison). (4) [[Drake Maye]] and [[Bo Nix]] both get reinforcing,
more detailed passes on standing reads rather than reversals; Nix's bullish
update (published after Angelo's 2024-02-01 Senior Bowl downgrade) does not
address that critique, so the three-way split stands. (5) A new concept page,
[[Quarterback Processing and Confidence]], captures Waldman's durable "why
teams miss on quarterbacks" framework (processing as confidence/intuition,
not academic study; Alex Smith as the cautionary over-processed example) —
also logged as a new philosophy bullet on the [[Matt Waldman]] expert page.
(6) [[Pace Control and Movement Intellect]] picks up a reinforcing "teams
overrate speed" restatement of its existing compensatory-skill mechanism.
ASR normalizations: "TyJay Spears" → [[Tyjae Spears]], "Brightson"/"Bryson
Hopkins" → [[Brycen Hopkins]], "Hayward" → Connor Heyward (no page, passing
mention), "Desmond Ritter" → [[Desmond Ridder]] (also corrected on the
[[Drake Maye]] page, where this same garble was carried over uncorrected
from an earlier ingest batch as a Waldman-coined comp name).

## [2026-08-03] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It Post-Super Bowl Edition (2024-02-12)
*Feel It or F**k It* with **Bob Harris** (not tracked; not [[Chris Harris]]).
Super Bowl LVIII recap plus a rookie-RB segment and a veteran-QB/WR
free-agency quick-hitter run. Seven new pages: two 2024 RB prospects
([[Daijun Edwards]], [[George Holani]]) and five veterans ([[Davante Adams]], [[Kirk Cousins]], [[Daniel Jones]], [[Ryan Tannehill]], [[Aaron Rodgers]]).
**What materially changed:** (1) [[Isiah Pacheco]]'s two Super Bowl fumbles
are read by both hosts as a 2024 buying opportunity, not a red flag — Kansas
City never benched him, a "top-10 running back" call with concrete
[Best Ball] ADP (round 2-3 turn), explicitly mirroring the Gabe Davis
last-thing-you-saw bias in the opposite (underrated) direction. (2)
[[Rashee Rice]] gets the actual Gabe-Davis-effect downgrade instead — a real
[Best Ball] ADP fall, undrafted deep into Waldman's own current mock,
"not reliably valuable for top-five-round" picks. (3) [[Travis Kelce]]'s
diminished role is reframed as a supporting-cast problem, not decline —
he'd be "a dominant player once again" with one more real KC weapon. (4)
[[Patrick Mahomes]] gets Waldman's fullest playing-style statement yet, "a
wiser Brett Favre." (5) [[Dylan Laube]] gets Waldman's own tape-based
follow-up (not just relayed buzz), confirming the [[Austin Ekeler]] archetype
comp. (6) The [[Matt Waldman]] expert page picks up a new Track Record Notes
entry — a Jed York report that Shanahan privately called [[Brock Purdy]] the
49ers' best QB pre-2022 is cited as validation of Waldman's own pre-draft RSP
grade, supplied directly to Purdy's QB coach at the time. ASR normalizations:
"Dajon Edwards" → [[Daijun Edwards]], "Devontae Adams" → [[Davante Adams]]
(same garble as an unrelated joke in the 2024-02-05 episode, now resolved
with an actual evaluative take attached).

All three assigned transcripts (2024-02-02, 2024-02-05, 2024-02-12) are now
fully ingested. `python3 scripts/verify_integrity.py` confirms state and disk
agree; a wiki-wide grep for split `[[...]]` wikilinks across every file
touched in this batch came back clean.

## [2026-08-04] lint | YAML frontmatter standardized across all pages

Made frontmatter a checkable standard rather than a convention held only by
imitation of `wiki/_templates/`.

Audit found the 206 entity pages already fully conformant — 158/158 players with
`type`/`team`/`position`/`tags`, 22/22 sources with the full 8-key block, no
placeholder or malformed values anywhere. The gaps were the three maintained
non-entity files, which had none: `index.md` (now `type: index`), `log.md`
(`type: log`), and `wiki/sources/SOURCE_CATALOG.md` (`type: catalog`). All 213
pages now pass.

The larger gap was enforcement: `CLAUDE.md` had never documented frontmatter as a
requirement, so nothing but pattern-matching kept it consistent. Added a "Page
frontmatter" section with the required-keys table per type, and added
`scripts/lint_frontmatter.py` — checks block present and closed, required keys
present and non-empty, `type:` matching the folder, base tag present in `tags`,
position in QB/RB/WR/TE, dates as YYYY-MM-DD. Report-only with no `--fix`, since
repairing a missing `team:` or `date:` would mean inventing it.

Wired into the places pages get made: the ingest prompt from
`ingest_manifest.py` now inlines the per-type key list and step 8 runs the lint
alongside `verify_integrity.py`, and `run_daily_check.sh` runs it post-ingest so
the unattended path can't drift unnoticed. Also established `aliases` as a legal
optional key — the right home for the nickname/ASR-variant problem in rule 6.

## [2026-08-04] ingest | Reception Perception: The Show — Chiefs Take Down 49ers for Super Bowl LVIII

Matt Harmon's season-closing episode (with James Koh). Super Bowl LVIII recap
plus offseason outlook for both rosters — the last episode before the show's
week off. Nothing here reverses a prior headline view; it mostly deepens two
existing threads and opens one new one. (1) The [[Brock Purdy]]/[[Patrick Mahomes]]
processing-growth comparison gets its fullest statement yet — Harmon
explicitly frames Mahomes as having already completed the pre/post-snap
processing catch-up that Purdy (comped to [[Jared Goff]]/new page [[Kirk Cousins]])
still has ahead of him; logged on both player pages and on
[[Quarterback Processing and Confidence]]. (2) [[Deebo Samuel]]'s man-vs-zone
weakness gets a live game confirmation independent of Waldman's December read
— Chiefs press coverage held him to 3-for-33 on 11 targets. (3) New: a San
Francisco pass-catcher roster crunch flagged for the first time — not all
three of Deebo, [[Brandon Aiyuk]] and new page [[George Kittle]] survive past
2024 on the cap sheet — plus a first age-window caveat on [[Christian McCaffrey]]
for 2025 ([[Aging Curves and Career Longevity]]). Kansas City's
receiver rebuild produces two more new pages — [[Marquise Brown]] (rejected as
a fit, "another zone-beating type") and [[Skyy Moore]] (Harmon: outside-WR
usage was a "mis-evaluation," expects him traded) — plus a second landing-spot
mention for prospect [[Brian Thomas Jr.]]. [[Rashee Rice]] gets a pointer to a
separate Harmon YouTube mailbag comparing his rookie year to [[Amon-Ra St. Brown]]'s,
logged on [[Post-Rookie-Year Receiver Model]].

`python3 scripts/verify_integrity.py` and `python3 scripts/lint_frontmatter.py`
both clean after this ingest.

## [2026-08-04] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: Never Too Early to Draft Edition (w/ Bob Harris)

The season's first true redraft-cycle episode, a week after the Super Bowl —
dense with veteran free-agent market calls and the first round of 2024 QB
prospect verdicts. Nine new player pages: [[Joe Mixon]], [[Alvin Kamara]],
[[Derek Carr]], [[Justin Fields]], [[Justin Herbert]], [[Rashid Shaheed]],
[[Russell Wilson]], [[Jerry Jeudy]], [[Courtland Sutton]]. Headline shifts:
(1) [[Derrick Henry]]'s redraft price keeps sliding earlier — fifth round now,
a "huge steal" per Waldman, worth a third-round pick on talent alone, with
Chargers/Dallas/Philadelphia added to his standing Ravens wish-cast. (2)
[[Caleb Williams]] gets an explicit "hell no" verdict that all three of
Williams/[[Drake Maye]]/[[Jayden Daniels]] hit their draft capital — only one
"most likely" does, and it's Williams, with a Jay Cutler/Jeff George bust
comp attached. (3) [[Michael Penix Jr.]] reverses back to Waldman's top
outlier-QB pick just three weeks after being downgraded to "journeyman
starter." (4) [[Baker Mayfield]]'s Tampa OC question resolves (Liam Coen
hired) but his 2024 outlook is now explicitly conditioned on both
[[Mike Evans]] and [[Chris Godwin]] staying, with Evans's free-agency
deadline reportedly already passed. (5) [[Stefon Diggs]] gets Waldman's
fullest "blip, not a cliff" defense yet, reframing 2023's decline as a
Buffalo scheme/pecking-order issue rather than an age cliff.

`python3 scripts/verify_integrity.py` and `python3 scripts/lint_frontmatter.py`
both clean after this ingest.

## [2026-08-04] ingest | Matt Waldman's RSP Cast — Going Deep with Brandon Angelo and Matt Waldman: The 2024 RB Class Edition

Resumed ingest: a prior agent was killed mid-run by a server error after
writing dated 2024-02-22 bullets to seven pages ([[Blake Corum]],
[[Blake Watson]], [[Daijun Edwards]], [[George Holani]], [[Jonathan Brooks]],
[[Pace Control and Movement Intellect]], [[Prospect Pro-Readiness vs Ceiling]])
but before creating the source summary page or finalizing state. This pass
verified those seven bullets were accurate and complete, then finished the
rest of the episode without duplicating them. A full 2024 running-back-class
episode — ten new prospect pages ([[Cody Schrader]], [[Kendall Milton]],
[[Kimani Vidal]], [[Will Shipley]], [[Rasheen Ali]], [[Jaylen Wright]],
[[Dillon Johnson]], [[Trey Benson]], [[Bucky Irving]], [[Marshawn Lloyd]]).
Headline shifts: (1) [[Dylan Laube]] jumps from "underrated small-school
riser" to Angelo's explicit top-5-back-in-class grade, built on real outside/
boundary receiving skill, with Waldman ranking him almost even with
[[Blake Corum]]. (2) [[Braelon Allen]] gets a second independent
competitiveness knock from Angelo plus a "Wisconsin curse" development-runway
framing from Waldman (Jonathan Taylor/Melvin Gordon precedent, an explicit
wish for a multi-year [[Derrick Henry]] understudy role, Baltimore as the
dream fit) — see [[Player Development and Coachability]]. (3) [[Marshawn Lloyd]]
is the episode's clearest bust-risk case: ball security, outside-bounce
tendencies, and a perception both hosts think is inflated by a handful of
Caleb Williams option-pitch highlight plays — logged as a new instance on
[[Scouting Bias and Player Archetypes]] alongside a general note on why ball
security is treated as unpredictable rather than a fixed trait.

`python3 scripts/verify_integrity.py` and `python3 scripts/lint_frontmatter.py`
both clean after this ingest.

## [2024-02-26] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: Fantasy Drafts in February, the NFL Combine, and QB Metrics
Waldman/Bob Harris (not tracked). Nine new player pages (A.J. Brown, Khalil Herbert, Roschon Johnson, Javonte Williams, Samaje Perine, DeMarcus Robinson, Jahan Dotson, Matthew Stafford, Joe Burrow). New durable concept page NFL Combine and Pro Day Skepticism (combine value concentrated in small-school/unknown prospects, not blue-chips; historical Alex Smith pro-day-gaming anecdote; RAS as secondary reference only). Dynasty edge: Waldman takes Ja'Marr Chase "ever so slightly" over Justin Jefferson today on Burrow's QB certainty. Grouped health-not-decline read on Tony Pollard/Austin Ekeler/Travis Kelce's poor 2023 shows. Terry McLaurin sharpened to "solid WR2, not a true WR1" with a detailed poor-hand-technique critique. Normalized ASR garbles: "Roshon Johnson" -> Roschon Johnson, "Samajay Piran" -> Samaje Perine, "Jahan Dawson" -> Jahan Dotson, "Chad Ryder" -> Chad Reuter (not tracked).

## [2024-02-27] ingest | Reception Perception: The Show — Tee Higgins & Mike Evans, Marvin Harrison Jr. & Bieniemy Picks College Ball
Higgins charted to a career-worst 2023 (RP success rates), still tagged/top-20 but no proof as WR1 without Chase. Evans charted to a career-best 2023 under new route tree, ~$18M+/yr free-agent value. Harrison Jr. now skipping combine AND pro day (no agent) — added to index. Harmon gives top-10 grades to Harrison/Nabers/Odunze without ranking them, betting landing spot decides outcomes.
