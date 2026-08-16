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

## [2024-02-29] ingest | Reception Perception: The Show — Wide Receiver Prospects & the State of the Falcons
Harmon absent; James Koh hosted solo with guests Eric Froton (NBC Sports) and Kevin Knight (Falcoholic), neither tracked. New prospect pages: Adonai Mitchell, Xavier Worthy, Ja'Lynn Polk. Falcons context added to Bijan Robinson, Kyle Pitts, Desmond Ridder, Justin Fields, Kirk Cousins, Michael Penix Jr., J.J. McCarthy, Malik Nabers, Rome Odunze. Xavier Legette flagged as group's likeliest bust risk.

## [2024-03-01] ingest | Matt Waldman's RSP Cast — Combine 40 Times in Perspective and the "Big Four" '24 RB Free Agents
Harstad's 40-time measurement-validity framework and Angelo's timing-system standard-deviation estimate (0.24-0.3s) added to NFL Combine and Pro Day Skepticism, applied to Quentin Johnston. Harstad's aging-cliff research (RB decline ~33-40% vs 50% at WR) added to Aging Curves and Career Longevity. Big Four FA RB roundtable: Waldman & Harstad both rank Josh Jacobs top bet; Henry highest upside/highest risk (RYOE flat '21-'23); Pollard's pre/post-Carolina-game splits show no real recovery, undercutting his own excuse.

## [2024-03-04] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: NFL Combine Fallout, and Free Agent/Rookie QB Fits
Combine skepticism (Marvin Harrison Jr., Xavier Worthy flaw flagged, RB workout-speed methodology). Mike Evans's Tampa Bay re-sign (2yr/$52M) now official. New pages: Kenny Pickett, Michael Pittman Jr. QB free-agency/draft-fit sweep across Caleb Williams, Bo Nix, J.J. McCarthy, Justin Fields, Kirk Cousins, Baker Mayfield, Michael Penix Jr. Kimani Vidal confirmed top-10 RB by Waldman.

## [2024-03-05] ingest | Reception Perception: The Show — Mike Evans Stays in Tampa & Levels of Wide Receiver Need
Mike Evans re-signs Tampa 2yr/$52M; Harmon's fresh 2023 RP charting shows career-best man/press/zone success rates, confirming the 2022 dip was scheme misuse (Byron Leftwich) not decline. New page: D.J. Moore. League-wide WR need buckets (critical/substantial/justifiable pursuit) touched ~20 players/teams, incl. dynasty landing-spot caution on Malik Nabers, Marvin Harrison Jr. and Rome Odunze, and a Harmon/Koh disagreement on the Colts (Michael Pittman Jr.) and Lions.

## [2024-03-07] ingest | Reception Perception: The Show — Calvin Ridley, Marquise Brown & Tee Higgins Breakdown
New page: Calvin Ridley (RP charting: still green vs. man/zone, press-coverage drop, Jaguars' static X-only usage/thin route tree faulted). Marquise Brown and Tee Higgins updated with fresh charting (both down 2023s read as deployment/injury-driven, not talent decline). Nico Collins updated: Harmon would take him over Higgins straight-up.

## [2024-03-08] ingest | Matt Waldman's RSP Cast — 2024 NFL Draft QB Class A-T: Matt Waldman's RSP Solo Cast
Solo cast, full alphabetical 2024 QB class sweep (20 QBs). 10 new depth-prospect pages (Austin Reed, Brennan Armstrong, Carter Bradley, Devin Leary, Emory Jones, Gunner Watson, Jordan Travis, Keaton Slovis, Michael Pratt, Sam Hartman). Updated Caleb Williams, Bo Nix, Drake Maye, Jayden Daniels, Joe Milton III, Michael Penix Jr., Spencer Rattler (resolved man/zone split), Tanner Mordecai, Jack Plummer. Dynasty page got a rookie-QB-strategy bullet (Williams is 2024's only true priority pick). Quarterback Processing and Confidence and Scouting Bias and Player Archetypes concept pages extended with Waldman's box-score-accuracy and age-as-scouting-filter critiques.

## [2024-03-11] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 3.11.24
Russell Wilson signed with Steelers (team updated, superstar-upside read with Pickens); Jerry Jeudy traded Denver→Cleveland (team updated; new pages Amari Cooper, David Njoku, Deshaun Watson); Tee Higgins requested trade from Bengals (Waldman: very good WR2, not WR1); Michael Pittman Jr. signed 3yr/$71.5M extension, upgraded to low-end WR1 grade; new pages Rachaad White, Mike Williams, Tyler Harrell; FA landing-spot predictions for Josh Jacobs (Raiders), Saquon Barkley (Texans), Tony Pollard (Eagles), Calvin Ridley (pushback on Panthers fit).

## [2024-03-12] ingest | Reception Perception: The Show — Hot Start in Free Agency: Kirk Cousins, Michael Pittman, Saquon Barkley & Josh Jacobs
Kirk Cousins signs with Atlanta (4yr/$180M) — big projected boost for Drake London. Michael Pittman Jr.'s team-friendly Colts deal draws a top-10 WR breakout call from Harmon. Saquon Barkley to Philadelphia, Josh Jacobs to Green Bay, Aaron Jones released by GB. New page: Jacoby Brissett (Harmon's preferred Minnesota bridge QB post-Cousins).

## [2024-03-14] ingest | Reception Perception: The Show — Free Agency Continued: Breaking Calvin Ridley News, Diontae, Russ, Jeudy & Gabe Davis
Diontae Johnson traded PIT→CAR (light return, Harmon: fleeced); Jerry Jeudy traded DEN→CLE (5th/6th swap); Calvin Ridley signs 4yr/$92M with TEN; Gabe Davis signs 3yr/$39M with JAX (poor 2023 grade, bottom-5 WR room); Russell Wilson signs w/ PIT (Harmon skeptical of ceiling). New pages: Elijah Moore, Christian Kirk, Will Levis, Darnell Mooney.

## [2024-03-16] ingest | Matt Waldman's RSP Cast — 2024 NFL Draft WR Class A-Z: Matt Waldman's RSP Solo Cast
Full A-Z sweep of the 2024 WR draft class (54 prospects). Updated 20 existing prospect/veteran pages (Adonai Mitchell, Ainias Smith, Brendan Rice, Brian Thomas Jr., Devontez Walker, Ja'Lynn Polk, Javon Baker, Jaxon Smith-Njigba, Keon Coleman, Ladd McConkey, Malachi Corley, Malik Nabers, Malik Washington, Marvin Harrison Jr., Ricky Pearsall, Roman Wilson, Rome Odunze, Troy Franklin, Xavier Legette, Xavier Worthy, Tee Higgins). Created 10 new prospect pages (Anthony Gould, Bub Means, Jalen McMillan, Jermaine Burton, Johnny Wilson, Joshua Cephus, Kobe Hudson, Luke McCaffrey, Ryan Flournoy, Xavier Weaver). Added receiver career-longevity data (13% of 2008-17 draftees reach 3+ yrs top-36 production) to Aging Curves and Career Longevity, and a grading-tiers/scheme-fit worked example to Prospect Pro-Readiness vs Ceiling. No headline reversals — mostly new/corroborating scouting detail.

## [2024-03-19] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 3.19.24
Free-agency reaction week: Fields (PIT), Pickett (PHI), Keenan Allen (CHI), Diontae Johnson (CAR) trades finalized; Henry (BAL), Barkley (PHI, reversing Waldman's own Houston prediction), Jacobs (GB), Mixon (HOU), Ekeler (WASH), Pollard (TEN), Cousins (ATL) signings finalized. New pages: DeAndre Swift, Sam Darnold, Sam Howell, Alexander Madison, Zach Moss, Michael Thomas.

## [2024-03-19] ingest | Reception Perception: The Show — Weekend Receiver News: Keenan Allen Joins Bears & Bills Add Curtis Samuel
New page: Curtis Samuel (BUF signing, charted case his production is QB-suppressed not talent-limited). Keenan Allen traded to Chicago, paired with D.J. Moore — Harmon's charted read: role-narrowed, not declining. Justin Fields traded to Pittsburgh for a 6th; hosts split on value. Chargers' post-trade WR room (Palmer/Johnston) called among NFL's worst.

## [2024-03-21] ingest | Reception Perception: The Show — Marquise Brown to KC, Jerry Jeudy Charting & New Falcons WR Room
Marquise Brown signs 1yr/$7M with KC — Harmon: zone-beater ("Mahomes discount"), man coverage declining year over year (73.6%→62.6%→59%), projected flanker/slot. Jerry Jeudy's official RP profile confirms zone-coverage plateau/decline (8th percentile) — Harmon argues flanker fit over slot; skeptical of Cleveland's "distressed asset" WR strategy. Desmond Ridder traded ATL→ARI for Rondale Moore (new page: "not a real receiver," gadget player) after Falcons signed Kirk Cousins. Falcons WR room: Drake London X-receiver evaluation, Darnell Mooney projected vertical-slot/flanker role.

## [2024-03-23] ingest | Matt Waldman's RSP Cast — 2024 RSP RB A-W Solo Cast
Waldman's annual RB-class hit-rate framework (1-3 sustained starters per class is normal) drives an explicit dynasty rookie-draft recommendation to prioritize WR/QB over RB and trade for veteran backs later (logged to Dynasty). Updated 19 existing 2024 RB prospect pages with fresh scouting detail (no headline reversals); created 13 new prospect pages (Aidan Robbins, Audric Estime, Isaac Guerendo, Isaiah Davis, Jalen White, Jase McClellan, Montrell Johnson, Tyrone Tracy Jr., Miyan Williams, Frank Gore Jr., Emani Bailey, Dylan McDuffie, Michael Wiley). Names normalized: Aiden Robinson/Robbins -> Aidan Robbins; Audrick Estime -> Audric Estime; Isaac Garendo -> Isaac Guerendo; Jason McClellan -> Jase McClellan; Myan Williams -> Miyan Williams; Amani Bailey -> Emani Bailey; Dylan Lobby -> Dylan Laube; Dylan Johnson -> Dillon Johnson (existing page, reconfirmed).

## [2024-03-25] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 3.25.24
New pages: Ja'Tavion Sanders (TE, ASR "Getavian Sanders"), Aidan O'Connell, Geno Smith, Gus Edwards, Ben Sinnott (ASR "Ben Sanat"), Jack Westover, Zach Wilson. Waldman prefers Michael Penix Jr. over J.J. McCarthy and Drake Maye for Washington/New England; reaffirms Penix/Caleb Williams as the class's top-two QBs. Giants roster-construction critique (should've paid Saquon Barkley, not Daniel Jones). Gus Edwards flagged as underrated best-ball value on Greg Roman scheme history.

## [2024-03-26] ingest | Reception Perception: The Show — Breaking Down the Top 3 Wide Receiver Prospects
Full RP profiles for Marvin Harrison Jr., Rome Odunze and Malik Nabers go live; Harmon now leans Odunze as his class WR1 over Harrison, keeps Nabers third on zone-coverage concerns. Mike Williams signs with Jets to pair with Garrett Wilson. New pages: Garrett Wilson, Odell Beckham Jr., Xavier Gipson.

## [2026-08-04] lint | post-ingest cleanup of 2024-03-01..2024-03-19 batch
Renamed "Alexander Madison" -> [[Alexander Mattison]] (ASR garble, rule 7) and
fixed all 5 referring pages plus both index lines; recorded the garble as an
alias so it resolves instead of being recreated. Removed the partial write left
by the session-limit failure on the 2024-03-19 RSP episode (7 orphan pages, 35
bullets) before re-ingesting it cleanly.

## [2024-03-28] ingest | Matt Waldman's RSP Cast — Going Deep with Brandon Angelo and Matt Waldman: If We Were NFL GMs…
GM-exercise episode: do-not-draft calls on Adonai Mitchell, Devontez Walker, Braelon Allen, Drake Maye; high-floor picks Malik Washington, Jermaine Burton, Dylan Laube, Blake Watson, Luke McCaffrey, Dillon Johnson, Ben Sinnott; flag picks Javon Baker (Angelo) and Keon Coleman (Waldman); problem-solver picks Blake Corum, Jonathan Brooks, Caleb Williams. Extended Pace Control/Problem Solver and Prospect Pro-Readiness frameworks.

## [2024-03-28] ingest | Reception Perception: The Show — The Worst Wide Receiver Depth Charts Out There
Ranked NFL's worst WR rooms (Giants/Chargers/Patriots/Cardinals disaster tier; Chargers named single worst). New pages: Greg Dortch, Darius Slayton, Zay Jones, Josh Palmer, Allen Lazard. Harmon wobbles back toward Marvin Harrison Jr. as class WR1 for Arizona fit, two days after leaning Odunze; Odunze/Harrison/Nabers explosive-play stats compared. Harmon/Koh disagree on Keenan Allen vs. D.J. Moore target share in a hypothetical Bears rookie-QB offense.

## [2024-03-30] ingest | Matt Waldman's RSP Cast — 2024 RSP TE A-Z Solo Cast
Solo TE class sweep (22 prospects). 16 new prospect pages created (A.J. Barner, A.J. Stogner, Baylor Cupp, Cade Stover, Dallin Holker, Devin Culp, Eric All, Isaac Rex, Jaheim Bell, Jared Wiley, McCallan Castles, Tanner McLaughlin, Theo Johnson, Tip Reiman, Trey Knox, Zach Hines). Brock Bowers and Cade Stover named the class's most pro-ready TEs; Ben Sinnott upgraded relative to Michael Mayer hype. Updated historical rookie-TE production context on Sam LaPorta, Dalton Kincaid, Kyle Pitts (Ditka's 1961 record still stands, LaPorta came within 0.3 pts). Names normalized: Shaheen Bell to Jaheim Bell, Kate Stover to Cade Stover, McAllen Castles to McCallan Castles, Train Knocks to Trey Knox, Tip Rehman/Ryman to Tip Reiman.

## [2024-04-01] ingest | Matt Waldman's RSP Cast (Feel It or F**k It) — Feel It Or F@#k It: 4.1.24
RSP release-day rapid-fire episode; no headline reversals — reinforces existing pre-draft reads on Brock Bowers (1.5-PPR top-3 pick, chance at Ditka's rookie TE record), Blake Corum (safest RB, scheme-versatile), J.J. McCarthy (red-zone/backed-up decision-making flaw), Michael Penix Jr. (top-tier talent, injury/runway risk), Ricky Pearsall vs. Ladd McConkey (Pearsall graded slightly ahead), Marshawn Lloyd, Ray Davis, Bucky Irving, Blake Watson, Tip Reiman, Cade Stover, Caleb Williams.

## [2024-04-02] ingest | Reception Perception: The Show — Brian Thomas Jr. & Ladd McConkey Profiles
Harmon's finished full-sample profiles supersede early 2024-02-01 reads: Brian Thomas Jr. graded a clear tier-two prospect (WR4), median outcome a "faster Tee Higgins" vertical WR2, not a lock true WR1. Ladd McConkey confirmed as a flanker (not slot) with elite zone/out-route grades but weak vs press; Harmon rates him roughly equal to Thomas overall.

## [2024-04-04] ingest | Reception Perception: The Show — Stefon Diggs is a Texan & Keon Coleman Breakdown
Diggs traded BUF->HOU; Harmon's charting shows real downfield-separation decline (not injury-driven), diminished underneath role behind Collins/Dell. New page Josh Allen. Tank Dell durability risk flagged. Full Keon Coleman breakdown: bad man-coverage charting, Day 2 not Rd 1 grade; new historical study added to Reception Perception Methodology / Scouting Bias and Player Archetypes; GPS-vs-40 note added to NFL Combine and Pro Day Skepticism.

## [2024-04-08] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 4.8.24
New pages: Drake Maye vs. McCarthy/Williams pocket-movement takes (Maye page existed, updated), Travis Etienne Jr., Trevor Lawrence, Dalton Schultz. Headline shifts: C.J. Stroud rising with 3 startable WRs after Diggs trade; Josh Jacobs into top-10 RBs at Green Bay; Jordan Love a QB9 Best Ball bargain; Dalton Kincaid/Khalil Shakir bargain reads in Buffalo; Diggs flagged as Houston's biggest age-cliff gamble.

## [2024-04-09] ingest | Reception Perception: The Show — Roman Wilson & Ricky Pearsall Breakdowns
Full-sample RP profiles: Harmon well below consensus on Roman Wilson (weak man/zone separation, early Day 3 grade); well above consensus on Ricky Pearsall (87th pct vs man, rated above Jordan Addison's profile).

## [2024-04-11] ingest | Reception Perception: The Show — Adonai Mitchell & Free Agent WR's Remaining
Adonai Mitchell full RP profile (true X, strong man/press vs. weak zone, DeAndre Hopkins/George Pickens comps); new pages D.J. Chark, Hunter Renfrow, Tyler Boyd, Marquez Valdes-Scantling; free-agent WR buy/sell touched Beckham, Rice, Marquise Brown, Gallup.

## [2024-04-11] ingest | Matt Waldman's RSP Cast — Going Deep with Brandon Angelo and Matt Waldman: Fave Evals, Coach-Killer Candidates, and High-End Career Outcomes
New concept page Coach Killer Prospects: Drake Maye, J.J. McCarthy and Jayden Daniels all named 2024 coach-killer QB candidates. New pages DeVonta Smith, Javon Baker, Marshawn Lloyd, Jonathan Brooks, Keon Coleman index refresh with high-end career-outcome comps (Troy Franklin/DJ Chark, Xavier Worthy/DeSean Jackson, Keon Coleman/Tee Higgins & Anquan Boldin). Small-school-vs-big-school RB draft-capital bias (Kimani Vidal vs Marshawn Lloyd).

## [2024-04-15] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 4.15.24 (with Bob Harris)
Tee Higgins dropped his Bengals trade request (staying in 2024). New page Trey Lance (Cowboys backup QB outlook). Bryce Young upgraded to real 2024 upside (O-line, Diontae Johnson, Dave Canales). Geno Smith downgraded from "wins in a cakewalk" to genuine competition with Sam Howell/Ryan Grubb. Also touched: Tony Pollard/Tyjae Spears (Titans 1A/1B), C.J. Stroud (QB1 pushback), Joe Burrow (best-ball value), Brandon Aiyuk/CeeDee Lamb (contract situations), Tua Tagovailoa, Michael Penix Jr./Aidan O'Connell/Gardner Minshew (Raiders QB competition), Diontae Johnson/Adam Thielen, A.J. Brown/DeVonta Smith (Eagles extension context).

## [2024-04-16] ingest | Reception Perception: The Show — Big News for Big Names & Xavier Worthy Breakdown
Aiyuk pegged as Harmon's dynasty WR8 and a must-re-sign X-receiver; DeVonta Smith's rookie-year film cited as proof of true-WR1 status alongside his new extension; Rashee Rice's felony charges tied to Chiefs reportedly prioritizing WR early in the draft; extensive Xavier Worthy prospect breakdown -- graded priority 2nd-round talent (not Round 1) due to press-coverage, contested-catch and drop-rate red flags despite record 4.21 combine speed.

## [2024-04-18] ingest | Reception Perception: The Show — Xavier Legette & Troy Franklin Breakdowns
New RP profiles added evaluative depth on 2024 WR prospects Xavier Legette (Round 2, Deebo/Alshon-hybrid deployment, higher ceiling/lower floor) and Troy Franklin (Round 2, Jordan Addison-style lid-lifter role, drop concerns); corroborating comparative RP data also added to Keon Coleman and Jordan Addison pages.

## [2024-04-22] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 4.22.24: An RSP Cast with Bob Harris and Matt Waldman
Pre-draft speculation episode: added landing-spot and current best-ball/dynasty ADP value takes across ~20 players, including disagreement on DeVonta Smith vs. Jaylen Waddle, skepticism on Puka Nacua repeating / Cooper Kupp rebounding, Sam Darnold skepticism next to Justin Jefferson, and Denver/New England rookie-QB scenarios (Nix, Penix, McCarthy, Maye). New pages created for J.K. Dobbins, Chuba Hubbard, Miles Sanders, and Kayshon Boutte.

## [2024-04-23] ingest | Matt Waldman's RSP Cast — Caleb Williams, Brock Purdy, and Anthony Richardson – QB Therapy with Will Hewlett
Trainer Will Hewlett (guest, untracked) gave detailed pre-draft evaluations elevating Caleb Williams (unmatched velocity variance and T-spine rotation, 'as pro-ready as anyone I've worked with') and Anthony Richardson ('favorite QB since Mahomes,' worth #1 overall on traits); Waldman pushed back on the 'raw' Richardson label and revisited Drew Lock's coachability struggles as a cautionary scouting lesson.

## [2026-08-05] refactor | ingest v2 — extract then apply
Ingest split into an LLM extraction phase emitting one JSON plan and a
mechanical applier (scripts/apply_ingest.py). 66 turns -> 5, 2.88M -> 346k cost
units per episode (88% lower), at 1.09x legacy content volume measured by A/B on
identical transcripts. Bullet dates are now stamped by the applier from
state.json, so rule 4 cannot be violated by an agent. See docs/ingest-v2-plan.md.

## [2024-04-23] ingest | Matt Waldman's RSP Cast — Evaluation vs. Valuation, '24 NFL Draft Faves, and Risks: Matt Waldman's RSP Scout Talk with NFL.com's Chad Reuter
New pre-draft dynasty pages: Ben Sinnott (TE2, top-50 grade), Blake Corum (safest RB in class, Ray Rice ceiling comp), Michael Penix Jr. (top-3-4 talent but Round 2 value given four-year injury pattern), Adonai Mitchell (George Pickens comp, Round 2 not Round 1 valuation). Brock Bowers take reinforced: Waldman rates him a top-of-draft talent regardless of landing spot.

## [2024-04-23] ingest | Reception Perception: The Show — Ja'Lynn Polk, Jalen McMillan & Javon Baker
Added RP pre-draft profiles for Ja'Lynn Polk, Jalen McMillan, Javon Baker and a shorter Troy Franklin comparison; Harmon grades Polk (Day 2/priority-R2) and Baker (elite downfield success despite poor testing) well above McMillan (Day 3, slot-only red flags) and Franklin (bumped from priority-R2 to Day 2).

## [2024-04-25] ingest | Reception Perception: The Show — 2024 Wide Receiver Class Superlatives
Reception Perception's full pre-draft 2024 WR class superlatives: Harrison Jr. and Odunze crowned best route runner/best contested-catch winner; Burton rated a talent-RB4 sleeper with real character risk; McConkey's 44% success rate vs. press flagged as capping his X projection (ranked below Pearsall); Legette and Franklin named Harmon's two toughest evaluations in the class.

## [2024-04-29] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 4.29.24: An RSP Cast with Bob Harris and Matt Waldman
Post-draft landing-spot reactions across the 2024 rookie class: Waldman keeps Malik Nabers atop his rookie WR board despite the Giants' QB uncertainty, rates Marvin Harrison Jr. best 2024 opportunity but Rome Odunze better 3-year outlook, and publicly disputes Matt Harmon's charting that Keon Coleman is a slot-only prospect. Also: Blake Corum projected to overtake Kyren Williams as soon as 2024; Cade Stover called best-landed rookie TE; Ricky Pearsall's value gated on a Deebo Samuel/Brandon Aiyuk trade.

## [2024-04-30] ingest | Reception Perception: The Show — Day 1 Wide Receiver Landing Spots
2024 NFL Draft landing-spot analysis for the full first-round WR class: Rome Odunze (CHI), Marvin Harrison Jr. (ARI), Malik Nabers (NYG), Brian Thomas Jr. (JAX), Xavier Worthy (KC), Ricky Pearsall (SF), Xavier Legette (CAR) -- each given projected role, target-share estimate, and RSP man/zone/press grades against their new team's context.

## [2024-05-02] ingest | Matt Waldman's RSP Cast — 2024 Post-Draft Landing Spot Breakdown: Going Deep with Brandon Angelo
Post-draft landing-spot ingest: new pages for Jalen Coker and concept Scheme vs Talent; major rookie fit/role calls added across ~23 existing rookie pages including underrated Bo Nix, Ja'Lynn Polk, Jermaine Burton, Michael Penix Jr., Kimani Vidal; overrated-by-fit concerns on Brian Thomas Jr., Ricky Pearsall, Roman Wilson; host disagreement on Malachi Corley (gadget risk vs. centerpiece upside).

## [2024-05-02] ingest | Reception Perception: The Show — Day 2 & 3 Wide Receiver Landing Spots
Ingested Reception Perception's Day 2/3 WR landing-spot episode: post-draft team-fit takes added for Keon Coleman (BUF), Ladd McConkey (LAC), Ja'Lynn Polk & Javon Baker (NE), Adonai Mitchell (IND), Jermaine Burton (CIN), Troy Franklin (DEN), and Malik Washington (MIA), with Harmon/Koh disagreeing on Coleman's and Polk's draft-slot value.

## [2024-05-06] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 5.6.24: An RSP Cast with Bob Harris and Matt Waldman
Chubb detailed at 50/50 return odds (second same-knee 3-ligament tear); Cousins flagged for Week 1 accuracy/velocity risk from leg-torque injury; new pages for Eric Gray, Trey Palmer, Chase Claypool, Kadarius Toney, Dameon Pierce, Drew Lock; Chargers/Giants/Texans backfield and WR battles updated; McMillan projected immediate WR3 over Palmer; Aiyuk pegged 80/20 to leave SF in 2025, boosting Pearsall.

## [2024-05-07] ingest | Reception Perception: The Show — Are These Rookies Going Over or Under Their Yardage Lines?
First rookie-WR season-long over/under episode: Harmon/Koh graded all 8 top rookie WRs against betting lines, comped Nabers to Waddle's rookie profile, faded Worthy hard vs. Marquise Brown/Rashee Rice on the Chiefs' talent tier, and flagged Diontae Johnson (not Legette/Thielen) as Carolina's new top target-getter.

## [2024-05-09] ingest | Reception Perception: The Show — Breaking Down Some Receiver Rooms
Rashad Bateman got a contract extension through 2026 and Harmon renewed his bullish take (~600 yards, Keenan Allen mold). New pages for Isaiah Likely, Jalen Tolbert, Chris Olave and A.T. Perry. Ainias Smith emerged as Harmon's favorite for Philadelphia's WR3/slot job. Treylon Burks's outlook dimmed further as Tennessee pursues Tyler Boyd, with trade speculation raised. Jameson Williams skepticism reaffirmed on both film quality and offensive-ecosystem role (5th option at best).

## [2024-05-13] ingest | Matt Waldman's RSP Cast — Feel It Or F@#k It: 5.13.24: An RSP Cast with Bob Harris and Matt Waldman
New rookie-QB pecking order laid out: Waldman buys Caleb Williams/Jayden Daniels/J.J. McCarthy/Bo Nix as Week 1-ish starters, fades Drake Maye; flags real risk Kirk Cousins's Achilles limits accuracy (not just availability), projecting Michael Penix Jr. could start by Week 7-8; buying Kyren Williams and Rachaad White dips, dismissing Corum/Irving as real threats; Rashee Rice legal exposure (4-8 games or a season) reshuffling KC WR value toward Xavier Worthy.

## [2024-05-14] ingest | Reception Perception: The Show — Bears & Eagles Dive w/ Adam Rank & Chris Long
Adam Rank (guest, not tracked) breaks down the Bears' offense: strong evaluation of Rome Odunze and DJ Moore, 4,000-yard passing guarantee for Caleb Williams, and a full account of why Justin Fields' Bears failure was organizational rather than talent-based, now traded to Pittsburgh. Chris Long (guest, not tracked) ties the Saquon Barkley signing to reducing Jalen Hurts' rushing workload and gives an extended framework on RB/DL aging driven by injury timing and usage rather than raw age.

## [2024-05-17] ingest | Matt Waldman's RSP Cast — 2024 NFL Rookie Dynasty Draft Thoughts: Going Deep with Brandon Angelo
Rookie dynasty draft-season takes: Jermaine Burton and Tyrone Tracy Jr. named biggest 2025 WR/RB risers; Michael Penix Jr. reached for as insurance given Kirk Cousins' age/Achilles; Deebo Samuel framed as increasingly scheme-dependent/trade-candidate behind McCaffrey and Pearsall in SF; Trey Benson and Marshawn Lloyd projected to sizzle in camp but fizzle as rookies on processing-speed concerns; Blake Watson emerges as a dark-horse Denver backfield riser over Audric Estime and Javonte Williams.

## [2024-05-20] ingest | Matt Waldman's RSP Cast — Feel It or F–It 5.20.24: An RSP Cast with Jagger May and Matt Waldman
Michael Mayer's dynasty outlook cratered to a short-yardage 2-3 target/game role after Brock Bowers' arrival; Waldman disclosed selling his own Quentin Johnston shares to draft Javon Baker; Deuce Vaughn and Malik Willis both flagged as unlikely to have fantasy-relevant 2024 roles.

## [2024-05-21] ingest | Reception Perception: The Show — Second Year Guys: Tank Dell & Dontayvion Wicks
Tank Dell and Dontayvion Wicks both get full rookie-season RP charting breakdowns from Matt Harmon -- Dell graded as an elite outbreaking/dig-route separator despite sub-180lb size, Wicks compared by Matt LaFleur to Davante Adams as a route runner and flagged as Harmon's 2024 Packers sleeper over Romeo Doubs and Christian Watson.

## [2024-05-23] ingest | Reception Perception: The Show — Second Year Guys: Josh Downs & Quentin Johnston
Josh Downs (IND) confirmed as an elite man-coverage/off-script slot receiver via RP charting, with a Sterling Shepherd career comp. Quentin Johnston (LAC) charted as a historically bad rookie WR (top-5 worst success rate vs. man ever recorded); Harmon casts doubt on him earning a clear 2024 role under new Chargers coaching staff.

## [2024-05-29] ingest | Reception Perception: The Show — Puka Nacua & Zay Flowers Breakdown + Malik Washington Addition in Miami
Nico Collins signed a ~$24M/yr extension; RP profile data used to rebut the 'Stroud-dependent' narrative. Puka Nacua and Zay Flowers rookie profiles detailed with year-two outlooks benchmarked against Jefferson/Chase. Rookie Malik Washington (MIA, 6th round) evaluated as a slot fit behind Hill/Waddle.

## [2024-05-30] ingest | Reception Perception: The Show — Jayden Reed & Jordan Addison + Eagles Draft a Gem?
Jayden Reed and Jordan Addison get full 2023 Reception Perception rookie profiles from Matt Harmon (Reed: strong man/press numbers, role risk flagged; Addison: weak vs. press, projected capable No. 2 not WR1). New page for Eagles rookie Aeneas Smith (Curtis Samuel comp, projected slot role). Dontayvion Wicks flagged as a breakout threat to Reed's target share.

## [2024-06-03] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 6.3.24: An RSP Cast with Bob Harris and Matt Waldman
Ingested 2024-06-03 RSP Cast Feel It or F-It episode: Waldman lays out detailed target/yardage projections for Houston's Collins/Diggs/Dell and Green Bay's Reed/Wicks/Watson receiver rooms, ranks Deebo Samuel below Aiyuk as a 'gadget player' vs. true X receiver, prefers Malik Nabers over Marvin Harrison Jr. '10 times out of 9' despite the ADP gap, projects Derrick Henry for a heavy ~250-carry Ravens workload, and stakes out Anthony Richardson as a top-5 personal QB ranking with real top-3 fantasy QB upside.

## [2024-06-04] ingest | Reception Perception: The Show — The Beefy Jameson Williams Episode We All Need
Jameson Williams: RP profile split reveals week-15-on success rates (67% man/85% zone) far stronger than full-season marks (57%/72%), with target ceiling projected at ~100 (5-6/game); comps range from Corey Coleman-bust to Gabe Davis-median to Brandon Cooks-ceiling. Jahan Dotson: 2023 profile shows across-the-board route decline tied to fewer deep routes/more slot usage; Harmon maintains 'rock solid WR2' ceiling view, not a McLaurin-mantle successor.

## [2024-06-06] ingest | Reception Perception: The Show — We Love Nico Collins & Where George Pickens Does Best
Nico Collins: RP charting shows a historic year-3 jump (77.6% vs. man, 82.5% vs. press, 94th/96th percentile) -- Harmon argues major fantasy sites still have him underranked relative to Underdog Best Ball ADP. George Pickens: improved press/man success rates year 2 but zone coverage and target-share ceiling (20.8%, capped near Mike Evans range per Harmon) remain concerns; co-host disagreement over whether his deep-route-heavy usage should be trimmed.

## [2024-06-10] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 6.10.24: An RSP Cast with Bob Harris and Matt Waldman
Ingested a rapid-fire projections episode: Waldman set explicit 2024 point projections for a large slate (CMC, Bijan, Lamb, Hall, Barkley, Gibbs, Jacobs, Swift, Nabers, Harrison Jr., Kupp/Nacua/Robinson, Harris/Warren) and took a strong Nabers-over-Harrison Jr. stance on price; new pages created for Calvin Austin III and Denzel Mims as Steelers WR2 sleeper candidates.

## [2024-06-11] ingest | Reception Perception: The Show — Ja'Marr Chase, Christian Watson & Malachi Corley
Matt Harmon's RP charting: Chase projected for expanded slot role and 1,600+ yard/double-digit-TD ceiling if Burrow stays healthy; Watson pegged as a touchdown-dependent 'elevated MVS' who needs role catering, not a true No. 1; Jets rookie Malachi Corley evaluated as an elite create-a-touch YAC talent (Deebo Samuel comp rejected) projected for a slot/gadget WR3 role.

## [2024-06-13] ingest | Reception Perception: The Show — Amon-Ra, Garrett Wilson & Brenden Rice
Detailed RP charting takes added for Amon-Ra St. Brown and Garrett Wilson (both 'superstar, not quite elite' per Harmon); new sleeper-tier evaluation filed for rookie Brendan Rice; Chargers WR room role breakdown added across McConkey, Johnston, Palmer and Chark pages.

## [2024-06-18] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 6.17.24: An RSP Cast with Bob Harris and Matt Waldman
Marquise Brown clarified as de facto Chiefs WR1 with Rice suspended; Tee Higgins framed as likely traded/gone after 2024 given Bengals cap crunch with Chase; Jonathan Brooks confirmed not camp-ready post-ACL with PUP expected; Nick Chubb take split between Waldman (still RB40, trusts recovery) and untracked Bob Harris (fade at 28); new pages created for DK Metcalf and Jameis Winston.

## [2024-06-18] ingest | Reception Perception: The Show — T-Law Gets Paid, Chris Olave Profile & Rookie Roundup on Devontez Walker
Chris Olave: detailed 2024 projection (92/1,200 median, 107/1,600 ceiling) and 'very good WR1, not yet superstar' tier placement from Harmon, plus scheme-mismatch diagnosis under Carr. Devontez Walker: new page-worthy take -- worst RP man-coverage score Harmon has charted in 4+ years, buried behind five Ravens pass catchers. Added supporting takes on Kamara's uncertain role under new OC, Bateman's ideal slot usage, A.T. Perry as a 'sacrificial X' candidate, and Tee Higgins/Trevor Lawrence contract context from co-host James Koh.

## [2024-06-20] ingest | Reception Perception: The Show — First-time NFL Offensive Coordinators
Drake London projected to 1,300 yards by Matt Harmon on expected McVay-tree scheme shift and inside alignment; Diontae Johnson (traded PIT->CAR) flagged as a scheme-fit bounce-back with career-best 2023 efficiency; new pages created for Chigoziem Okonkwo (TE, TEN) projected back to in-line role; Xavier Legette projected to a Deebo Samuel-lite motion role rather than outside X; JSN expected to pass Tyler Lockett in Seattle's new vertical Ryan Grubb scheme.

## [2024-06-25] ingest | Reception Perception: The Show — Team-by-Team Offensive Schemes Continued
Reception Perception team-by-team OC preview: A.T. Perry emerges as Saints' likely X-receiver over Bub Means; Harmon predicts Kellen Moore could move A.J. Brown into the slot over DeVonta Smith; George Pickens' route tree flagged as a scheme mismatch with Arthur Smith's in-breaking concepts; Terry McLaurin's outlook boosted by expected RPO-heavy usage under Kliff Kingsbury; Zach Ertz downgraded to placeholder as rookie Ben Sinnott (comped to Kittle/Juszczyk) is groomed for immediate role; Brandon Aiyuk-to-Steelers rumor read as contract leverage, Harmon expects him to stay in SF.

## [2024-06-27] ingest | Reception Perception: The Show — Choose Your Fighters: Wide Receiver Battles
No major ranking or role changes -- a historical-comp exercise. Harmon reaffirmed Nico Collins/Brandon Aiyuk as 'tier-two superstar' peers (still prefers Aiyuk overall), gave slight statistical edges to retired comps Eric Decker over Zay Flowers and DeSean Jackson over George Pickens, and picked Puka Nacua over Emmanuel Sanders as the better long-term player.

## [2024-07-01] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 7.1.24: An RSP Cast with Bob Harris and Matt Waldman
Added 23 player pages/updates from a 2024-07-01 preseason ADP review: notably a Josh Allen QB1-overall disagreement (Bob Harris confident, Waldman skeptical pending WR development), Waldman ranking Breece Hall/Bijan Robinson ahead of Jahmyr Gibbs/Jonathan Taylor for RB1-overall threat to McCaffrey, and new pages for Rhamondre Stevenson and Kendre Miller.

## [2024-07-02] ingest | Reception Perception: The Show — DeVonta Smith & Rashee Rice Profiles
Harmon downgrades DeVonta Smith to a 'tier-three/bottom-tier-two' receiver after a 2023 statistical dip and projects Kellen Moore will deploy him at boundary/X with A.J. Brown in motion. Rashee Rice's rookie role is detailed as a near-total reversal from his poor SMU man/zone profile, comped to Juju Smith-Schuster and Jarvis Landry with Amon-Ra St. Brown as the growth ceiling; Marquise Brown and Xavier Worthy are framed as space-clearers for Rice, with Worthy's hands flagged as a risk.

## [2024-07-04] ingest | Matt Waldman's RSP Cast — Sleeper WRs for the 2024 NFL/Fantasy Season: Going Deep with Brandon Angelo and Matt Waldman
Ingested Going Deep sleeper-WR episode (Waldman/Angelo). New pages: Brandin Cooks, Andrei Iosivas, Charlie Jones, Parker Washington, Casey Washington, Evan Engram. Notable calls: hosts expect Cincinnati to move on from Tee Higgins (walk or midseason trade), opening volume for Burton/Iosivas/Jones; Angelo prefers Roman Wilson over Calvin Austin III in Arthur Smith's scheme; Waldman names Parker Washington (not Brian Thomas Jr.) as most ready to start in Jacksonville; Michael Thomas landing-spot speculation (Jets/Bengals/Steelers/Falcons).

## [2024-07-05] ingest | Reception Perception: The Show — Jaylen Waddle & Demario Douglas Profiles
Waddle: RP data shows a career-best press-coverage jump (65.7% rookie to 72% in 2023), reinforcing his boundary/X role over Tyreek Hill, though Harmon keeps him a tier below Diggs/Ayuk. Douglas: rookie profile graded stronger vs. man than zone (atypical for his route tree) with a muddled 2024 role behind new draftees Polk/Baker and vets Bourne/Smith-Schuster. New page: Ja'Lynn Polk gets an early scouting projection from untracked co-host James Koh as the Maye-friendly intermediate complement to Douglas.

## [2024-07-08] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 7.8.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman/Harris called both Kyren Williams and Blake Corum overrated at current ADP, likening the Rams backfield to the Priest Holmes-Larry Johnson dynamic; Waldman reversed his prior Fantasy Football Expo skepticism to bullish on Calvin Austin III; flagged Michael Carter as a sleeper over Trey Benson behind James Conner in Arizona; added new pages for Taysom Hill and Zach Charbonnet.

## [2024-07-09] ingest | Reception Perception: The Show — The Jets Are Betting On Aaron Rodgers...Again
Harmon/Coe's AFC East WR room previews: Buffalo's WR room seen as fumbled around Curtis Samuel (best man-beater) with Keon Coleman's poor man-press profile projecting him to slot; Miami's Waddle/Hill flexibility boosted by OBJ and Malik Washington adds; new Kendrick Bourne page created for New England's ACL-recovery X question with Baker/Polk as rookie hopes; Jets room flagged as almost entirely dependent on a 30-year-old, ACL-recovering Mike Williams staying healthy, with Garrett Wilson given a 1,700-yard high-side ceiling and 2,000-yard-upside company.

## [2024-07-11] ingest | Reception Perception: The Show — Which AFC South Team Has The Best WR Room?
Reception Perception AFC South WR-room breakdown: Diggs flagged with real 2023 decline concentrated on deep routes (age-cliff risk) but projected into a reduced 3rd/4th-down role behind Nico Collins and Tank Dell; Nico Collins confirmed as Harmon's top Houston WR with a 1,750-yard upside case; Adonai Mitchell and Alec Pierce added as new pages (rookie evaluation and 'disappointment so far' respectively); Treylon Burks reaffirmed as a likely cut/trade candidate.

## [2024-07-12] ingest | Matt Waldman's RSP Cast — JJ Zachariason and the Late-Round Draft Guide
Established 2024 draft-season stances across ~20 players: JJ Zachariason (guest) introduced the 'running back dead zone' and 'pocket passer trap' concepts; notable takes include fading Josh Jacobs/Kyren Williams for backfield-mate risk, high-conviction bets on Jonathan Brooks, De'Von Achane and Tyjae Spears (over Tony Pollard), a tempered/fade-if-pricier stance on Jayden Daniels, and Waldman's WR40-range value case for DeAndre Hopkins and comp of Malik Nabers to Marvin Harrison Jr.

## [2024-07-15] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 7.15.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman revealed Ladd McConkey as a top-15 fantasy WR and detailed the Herbert/Greg Roman scheme fit; called Michael Mayer the likely Raiders TE2 over a boom/bust Brock Bowers on blocking-role reporting; went all-in on Brian Robinson Jr. over Austin Ekeler in Washington (Harris disagreed); cautiously bullish on a Russell Wilson Pittsburgh rebound against Cecil Lammey's counter-take; explained Rachaad White's low YPC as scheme (duo blocking), not talent; added new prospect evaluations for Ashton Jeanty, Trevor Etienne and Ollie Gordon II.

## [2024-07-16] ingest | Reception Perception: The Show — Diving Into the NFC East Offenses
NFC East WR/TE room breakdown: Harmon's charting numbers on rookie Malik Nabers (tier-one, WR3 in class) and Jalen Tolbert; explicit 2024 target projections for CeeDee Lamb (180, room for 190-200), Brandon Cooks (86.25) and Tolbert (56); target-share bounce-back calls for Terry McLaurin and Jahan Dotson under new Washington OC Kliff Kingsbury; A.J. Brown given a 1,800-2,000-yard range under new OC Kellen Moore; Ben Sinnott's role flagged as unresolved (Kittle-to-Juszczyk GM comp) with Washington projected toward heavier 12-personnel usage alongside Zach Ertz.

## [2024-07-18] ingest | Reception Perception: The Show — Breaking Down Offensive Lines w/ Brandon Thorn
Added detailed cross-referenced OL/WR-room takes for six offenses (WAS, GB, LAC, LAR, BUF, NO, TEN) from Matt Harmon's episode with guest OL analyst Brandon Thorn. Notable headline moves: Quentin Johnston's rookie separation graded among the worst Harmon has ever charted; Cooper Kupp's man-coverage ability declined post-injury even as zone success (83.3%) stayed strong; Chris Olave's ceiling (top-10-12) is paired with a serious floor risk if Saints RT Ryan Ramczyk's knee keeps him out; Calvin Ridley needs a route-diet shift off comeback/X routes to be maximized in Tennessee; new concept page 'Scheme vs Talent' bullet added synthesizing the episode's throughline.

## [2024-07-22] ingest | Matt Waldman's RSP Cast — Feel It or F–It 7.22.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman prefers Aiyuk stay in SF (timing-route fit; Washington/New England would 'ruin' him) and says trade Deebo instead; Aiyuk's Underdog ADP already 12 to 16 and he is buying the dip, same plan on CeeDee Lamb (his WR2) as the holdout gets loud. Denver backfield reordered: Javonte Williams on the roster bubble as the only back Payton didn't pick, Jaleel McLaughlin the buy at RB50, Estime the power/goal-line piece. Mixon given 75-80% odds of RB1 production on Slowik workhorse volume despite worst breakaway rate among top-12 backs. Jordan Love called underpriced at QB10 (21.1 PPG over the final eight games). Isaiah Likely value quantified: 85-90% starter if Andrews is hurt, only ~15% standalone. New pages: Jaleel McLaughlin, Clyde Edwards-Helaire.

## [2024-07-23] ingest | Reception Perception: The Show — AFC North Breakdown
Amari Cooper elevated to a genuine No. 1 X in Harmon's view (career-best Cleveland charting) but flagged for an age-30 holdout; Jerry Jeudy downgraded to an inconsistent No. 3 on an 8th-percentile zone success rate, with Harmon and Koh both rating Elijah Moore ahead of him; Rashad Bateman established as Harmon's Baltimore breakout bet on late-2023 separation, capped by snap share; Tee Higgins moved below consensus at WR13 among under-25s with a transportability caveat Koh rejected outright; Ja'Marr Chase's slot usage projected to hit a career high with Boyd gone and Burton taking outside snaps.

## [2024-07-25] ingest | Reception Perception: The Show — NFC South Breakdown
Diontae Johnson reframed as an elite RP separator whose per-target knocks trace to 88%+ X usage under Matt Canada — now Carolina's clear No. 1 read under Canales. Chris Godwin confirmed moving back to the slot after a misused 39%-slot 2023, framed as a bounce-back. Chris Olave set at a year-three fork: McLaurin/Lockett plateau vs a Diggs-style leap. Michael Gallup retired (reserve/retired list), becoming Harmon's case study for post-ACL confidence loss. Xavier Legette splits the hosts — Harmon cautious on a raw fifth-year-breakout archetype, Koh bullish on contested catch. New pages for A.T. Perry, Bub Means and Jalen McMillan; Atlanta's room called bottom-10 outside Drake London.

## [2024-07-29] ingest | Matt Waldman's RSP Cast — Dwain McFarland and Matt Waldman RSP Cast: Digging into the 2024 Fantasy Draft Prospects
Waldman's new RSP hands/tracking study moved Garrett Wilson down from a top-five board slot to low-end WR1/high-end WR2 (Diontae Johnson as the floor comp). De'Von Achane recorded as a disagreement — Waldman 6.0 YPC, McFarland 5.0 with RB13 at conservative usage and RB4 at a 50% carry share. New concepts: Play Caller Cheat Codes (play action +26%, motion +55%, 2-WR sets +29% PPR per route) and Catch Technique and Ball Tracking. Both hosts bought the Bryce Young rebound over Will Levis; Waldman stayed under market on Calvin Ridley and Xavier Legette; McFarland graded Jonathan Brooks over Jahmyr Gibbs as a prospect.

## [2024-07-29] ingest | Matt Waldman's RSP Cast — Feel It or F-It 7.29.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman lowered [[Garrett Wilson]] from a top-five WR to WR2/low-end WR1 on ball-tracking lapses with Rodgers demanding contested wins. [[Ladd McConkey]] opened camp as the Chargers' depth-chart WR1 and Waldman ranks him a top-10 WR at a WR3 price; Bob Harris prefers [[Josh Palmer]] on cost alone. [[Chase Brown]] moved ahead of [[Zach Moss]] in fantasy value (22.05 mph, Lieberman offseason, first-team reps). [[Keon Coleman]] faded to 'fourth option at best' with a Gabe Davis-style ceiling. [[Kirk Cousins]] skipping the preseason made [[Michael Penix Jr.]] a dynasty stash and first waiver call. [[Nick Chubb]] parsed as a best-ball round-10 dart only, with contact work unlikely all camp. New pages: [[Jordan Whittington]] (Deebo comp rejected), [[Hendon Hooker]] (near-pulled plug), [[Deneric Prince]] (camp reps aren't a depth-chart move).

## [2024-07-30] ingest | Reception Perception: The Show — NFC North Breakdown
Harmon promoted [[D.J. Moore]] from tier three to tier two ('superstar No. 1') and raised [[Rome Odunze]]'s odds to lead the Bears in yards from under 10% to ~35% on Caleb Williams off-script rapport. [[Dontayvion Wicks]] named his bold pick to lead Green Bay in receiving yards on a 72.2% man success rate, with [[Jayden Reed]] the projected top target earner but carrying two-WR-set snap risk. Split verdict on [[Jameson Williams]]: terrible full-season charting vs above-average final five games, so 'buying-ish' only, with usage as an on-the-line X the stated concern. [[Justin Jefferson]] framed as a live 200-target / 40%+ first-read-share candidate behind a thin Minnesota depth chart; [[Jordan Addison]] capped at top-30 with off-field availability risk; [[Christian Watson]]'s man (26th pct) and press (8th pct) scores flagged as boom-bust WR3 territory.

## [2024-08-01] ingest | Reception Perception: The Show — AFC West Breakdown
Harmon ranks AFC West receiver rooms Raiders > Chiefs > Chargers > Broncos. Ladd McConkey established as a full-field separator (85th vs man) and projected Chargers target leader over Josh Palmer; Quentin Johnston cratered — 1st/2nd percentile rookie charting vs man/zone/press, star ship 'sailed', possible WR4. Marvin Mims Jr. graded second-worst vs man and press among charted rookies; Troy Franklin flagged as a 176-lb low-volume stretch piece; Josh Reynolds named Harmon's bet for Denver WR2. Rashee Rice moved up to Harmon's chain-mover with ~105-catch upside and a suspension read as 2025 not 2024, while Koh pegs Marquise Brown for the Chiefs target/yard lead — disagreement recorded. Davante Adams held at top-three NFL receiver but with vertical routes declining; Harmon takes Marvin Harrison Jr. over him on 2024 yards on Raiders volume, Koh disagrees. New pages: Jakobi Meyers, Josh Reynolds.

## [2024-08-05] ingest | Matt Waldman's RSP Cast — Feel It or F–It 8.5.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman reshuffles the Rams receivers on camp news — Kupp raised back to a top-15 WR (WR16) and called the better value at WR23 ADP, Nacua dropped to WR17 on a week-to-week knee tweak plus a 32% target decline once Kupp played. Garrett Wilson cut from fourth overall to WR11 on Rodgers-timing reports. New pages: Justice Hill (reserve behind Derrick Henry but not the handcuff to own) and the concept Training Camp Report Skepticism. Waldman buying J.K. Dobbins at RB47 with top-six upside while Bob Harris prefers Gus Edwards; Achane framed as a fantasy lead back who will not lead in touches; Herbert defended as a high-end QB2 against the no-passing consensus; Breece Hall taken over Bijan by a narrow margin on Rodgers making him a primary red-zone read.

## [2024-08-06] ingest | Reception Perception: The Show — NFC West Breakdown
Aiyuk elevated to a top-six/seventh receiver on a 96/91/97 percentile man/zone/press RP sweep — one of only nine such seasons ever charted — with Harmon setting a first-and-a-third as the trade floor. Kupp's man success rate cratered 70.6% to 65.2% with dig 76%→59%: Harmon calls it a warning sign, Koh calls it a cliff, and both agree the No. 1 role has passed to Nacua, who Harmon tiers as good-everywhere/elite-nowhere with 1,400 yards possibly his apex. Metcalf dropped out of Harmon's top 15; Lockett moved out of the superstar tier; JSN moved up as a possible Seattle catch leader. New camp riser: Jordan Whittington as the Rams' Kupp-archetype contingency.

## [2024-08-08] ingest | Reception Perception: The Show — Let's Talk About Some Obscure Wide Receivers
Hopkins knee injury (out 4-6 weeks, age 32) — Harmon flags the aging-curve warning and moves Calvin Ridley up as Tennessee's likeliest leading receiver, with Treylon Burks explicitly ruled out as an X replacement. Xavier Legette cratered: foot injury, second-team reps, WR4 behind a rising Jonathan Mingo; Koh calls his rookie production season over. Darius Slayton onto the roster bubble as Jalen Hyatt runs ahead. Johnny Wilson emerges as a genuine outside-X candidate in Philadelphia on Harmon's charting (71.4% vs man, 88.9% outside), and Andrei Iosivas as the possible full-time Bengals slot. New concept material on sacrificial X roles and post-rookie-year patience.

## [2024-08-12] ingest | Matt Waldman's RSP Cast — 2024 NFL Preseason Risers, Fallers, and Curiosities: Matt Waldman's RSP Solo Cast
Waldman moved Achane above Mostert and raised Kupp on a projected 2-4 week Nacua ramp; Javonte Williams up to low-end starter after weight loss; Olave and DK Metcalf bumped on scheme. Reversal on Jerry Jeudy — no longer believes in him, prefers Cedric Tillman. Held firm negative on Marshawn Lloyd and Tyrone Tracy Jr. as preseason-hype traps, backed by a new six-year ball-security study (~90% of top-60 RBs beat one fumble per 60 college touches). New pages: A.J. Dillon, Olamide Zaccheaus, Ball Security and Fumble Rate Grading.

## [2024-08-19] ingest | Matt Waldman's RSP Cast — Feel It or F–It 8.19.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman's preseason-discount framework hardened: preseason ~ college football (vanilla coverage, personnel churn), so camp risers move to a waiver-wire watch list rather than draft boards — Dillon Johnson, Kimani Vidal, Jalen Nailor (new), Xavier Weaver, Jordan Whittington, George Holani, Deneric Prince. Zach Charbonnet cooled hard: beat reporting says nobody plays if Kenneth Walker III is healthy, and Waldman's own RSP correlation data flagged his hit rate as weaker than his grade. Xavier Worthy split — best-ball spike weeks yes, WR2 no, because two-high shells capped Tyreek Hill in the same offense. Caleb Williams: feels top-12 upside, rejects the QB15 ADP. Rome Odunze called the best value of the Nabers/Harrison rookie tier. Malik Nabers' Daniel Jones concern dismissed via A.J. Brown/Adam Thielen precedent. Gardner Minshew named Raiders starter over Aidan O'Connell, which Waldman frames as the right developmental call. Drake Maye: sit him, footwork not automatic for Van Pelt's timing. Jayden Daniels tagged RG3 2.0 with slide-avoidance and processing risk, least upside of the Richardson/Murray/Daniels trio but fairly priced. Ray Davis promoted to a must-draft backup. Rashee Rice's suspension may not land in 2024. New pages: Jalen Nailor, Tyson Bagent, Sione Vaki.

## [2024-08-22] ingest | Matt Waldman's RSP Cast — Preseason Buzz & Regular Season Predictions: Going Deep with Brandon Angelo and Matt Waldman
Preseason fade/buy list from Waldman and Angelo. Waldman goes all-in against Jayden Daniels (slow processor, Mariota comp, durability) and prefers Bo Nix on games played; Angelo fades Jameson Williams as a 'Will Fuller minus' dart throw. Buys: Ray Davis to Buffalo's clear No. 2 and goal-line role, Michael Penix Jr. (Atlanta resting him read as a hedge on Cousins' sub-12-month Achilles), Malik Nabers and Xavier Worthy as first-splash rookies, Brock Bowers over Jakobi Meyers in the Raiders pecking order. Taysom Hill named the round-12+ league winner off a new [[Tight End Value in Condensed Formations]] framework; Khalil Shakir a 1,000-yard call with Keon Coleman 'not there yet'. New devy pages for Cam Ward, Jordan Lyle, Kyle Monangai and Jacory Croskey-Merritt.

## [2024-08-26] ingest | Matt Waldman's RSP Cast — Feel It or F–It 8.26.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman's late-August reaction show. Nick Chubb cratered — not worth a 10th-round pick, second reconstruction of the same knee, may miss more than four games. Deshaun Watson projection cut 14 games to 9 with Jameis Winston at 8. Anthony Richardson buy-the-dip after the joint-practice panic (0.45 fantasy pts/snap in 2023 vs Josh Allen's 0.36). Waldman a hard bear on Jayden Daniels as a year-one fantasy starter, with Bob Harris (untracked) arguing the Kyler-under-Kingsbury rushing floor — disagreement recorded on both sides. Drake Maye projected ~9 starts with high INT/sack rate; Bo Nix a starter but not a fantasy factor. Jahan Dotson downgraded to waiver-watch post-trade; new pages for Dallas Goedert (buy at TE10) and JuJu Smith-Schuster. Brandon Aiyuk down on 49ers-environment risk. Breece Hall named RB2 overall, a step ahead of Bijan, though Bijan called the safer of the two.

## [2024-08-27] ingest | Reception Perception: The Show — What Do We Think of These Rookie Quarterbacks?
Rookie-QB checkpoint hosted by James Koh with guest Derek Klassen (neither tracked; Harmon absent). New pages: Tim Patrick (Denver WR2 after two years out, ahead of Marvin Mims) and Trey McBride. Material moves: Jahan Dotson traded out of Washington for a third, leaving the room Klassen/Koh call the NFL's worst behind Terry McLaurin; Luke McCaffrey outside Washington's top four with Klassen saying his draft capital was name recognition; Bo Nix named Denver starter with a Minshew-to-Dalton realistic range and college-hash accuracy caveat; Marvin Mims buried; Klassen names Geno Smith his surprise (30+ TDs) and Jalen Hurts his disappointment (Kellen Moore progressions plus post-Kelce protection calls); bullish Kyler Murray bounce-back case; Caleb Williams projected ~4,285 yards by Koh.

## [2024-08-29] ingest | Reception Perception: The Show — Diving Deep Into Some Wide Receiver Rooms
Cut-day fallout reshaped several receiver rooms: Tim Patrick released by Denver and onto Detroit's practice squad, Kadarius Toney cut and unsigned with Harmon saying he never had real route-running traits, JuJu Smith-Schuster back in KC as a redundant profile to Rashee Rice, Noah Brown cut by Houston and signed in Washington, Jahan Dotson traded to Philadelphia (Harmon: solid non-star, better in the slot). New page for Tyquan Thornton, reported NE starting X but not a long-term starter with Harmon expecting Javon Baker to pass him by Week 10-11. Harmon softened his flat 'no' on Rashee Rice playing outside, flagged Terry McLaurin at 29 charting below his peak, and warned Minnesota's Sam Darnold season could go lost-at-sea with Hockenson on PUP.

## [2024-09-02] ingest | Matt Waldman's RSP Cast — Feel It or F–It 9.2.24: An RSP Cast with Bob Harris and Matt Waldman
Week 1 news and verdicts. Clyde Edwards-Helaire to the NFI list for four games (PTSD), elevating Samaje Perine and capping Isiah Pacheco at RB2/low-end RB1. Waldman moved Brian Robinson Jr. up to a top-15-20 back on gap-scheme and passing-down fit. New pages for Carson Steele, Dyami Brown, Rico Dowdle, Ezekiel Elliott and Dalvin Cook, plus a new FAAB Budget Allocation Strategy concept (cap single bids near 50%). Waldman called Xavier Worthy the rookie WR people will wish they drafted and Caleb Williams a top-five QB if the Bears line holds; Jonathan Mingo flagged as a second-year bounce-back after working with Steve Smith, with Xavier Legette pushed to 2025 as a manufactured-touch player. Both hosts expect Jameis Winston to start over Deshaun Watson in Cleveland by midseason. Waldman fades all 49ers and Cowboys reserve backs as rentable, not draftable.

## [2024-09-03] ingest | Reception Perception: The Show — 2024 NFL Season Hot Takes!
Ricky Pearsall shot in the chest and, per Harmon, headed for a redshirt rookie year (shoulder injury the real cause). Ja'Marr Chase holdout — zero practices, Week 1 in doubt, slot-expansion plan shelved; Tee Higgins elevated to CIN WR1 and unlikely to return in 2025. Harmon hot takes: Zay Flowers 1,200+ yards, Brian Thomas Jr. rookie WR2 in yards, Nico Collins to lead NFL in receiving TDs, JSN to lead Seattle, Rome Odunze Chicago's fantasy WR1. Harmon cratered on the Rams — neither Kupp nor Nacua a top-12 fantasy WR. DK Metcalf declared peaked at top-10-to-15; Tyquan Thornton's X role called a camp mirage. Koh (untracked) countered with Jordan Whittington, Javon Baker 1,000 yards and Sam Darnold to the playoffs, which Harmon rebutted with EPA data.

## [2024-09-05] ingest | Reception Perception: The Show — All Rise: Week 1 is Upon Us
Harmon's Week 1 2024 preview: [[Nico Collins]] named his highest-conviction receiver with an NFL touchdown-lead call; [[Ja'Marr Chase]] expected to sit or barely play Week 1 with [[Andrei Iosivas]] elevated into the Boyd slot vacancy; [[Jermaine Burton]] flagged as a possible healthy scratch on professionalism reporting while Harmon keeps his dynasty rank; [[Adonai Mitchell]] moving beyond a pure X role with [[Josh Downs]] injured; [[Jayden Reed]] called a top-20 talent capped only by the Packers rotation, with [[Christian Watson]] framed as a less-is-more part-timer; [[Stefon Diggs]] projected to a backside third-down role on deep-route decline. Harmon and Koh split on Buffalo's target leader ([[Khalil Shakir]] vs [[Curtis Samuel]]) and on whether Diggs can play the slot. New concept page: Sacrificial X Receiver.

## [2024-09-05] ingest | Matt Waldman's RSP Cast — Hot Start, Cold Finish Predictions and '25 NFL Draft Prospects: Going Deep with Brandon Angelo and Matt Waldman
Waldman doubles down on Marvin Harrison Jr. at ~950 yards/WR35-36 vs a WR15 ADP, citing Kyler Murray's one top-24 receiver in three top-12 seasons. Angelo reverses on Adonai Mitchell — slot role with Josh Downs hurt makes him a possible home run. New pages: Sean Tucker (best cutback runner in Tampa's zone shift), Tez Johnson, Nicholas Singleton, Dean Connors. Xavier Worthy, Bucky Irving and Jayden Daniels flagged as hot-start/cold-finish; Perine caps Pacheco's ceiling. New RSP ball-security data: only ~3% of elite fantasy RBs graded below an adequate college ball-security tier.

## [2024-09-05] ingest | Matt Waldman's RSP Cast — Managing September, Kickoffs, Kyler, and Where You Fantasy GMs F–d Up While We Were Gone: RSP Film and Theory with Adam Harstad
Waldman opened the 2024 season down on [[Marvin Harrison Jr.]] as a top-15 pick — projects ~900 yards / ~WR36 — on the grounds that [[Kyler Murray]] has supported only one top-24 receiver ([[DeAndre Hopkins]], WR4) across three healthy seasons and plays off-script by design. New concept pages capture Adam Harstad's (untracked) dynasty framework: 'nobody has needs in June' talent-over-need drafting, bench spots as information options, FAAB dumped early rather than optimized, and the four-week ADP-vs-production parity mark. Kickoff rule change page added — Harstad models a 50-60% return rate versus 22% in 2023, reviving return scoring. [[Christopher Brooks]] filed as a talent-without-opportunity Packers stash with named triggers.

## [2024-09-09] ingest | Matt Waldman's RSP Cast — Feel It or F-It 9.9.24: An RSP Cast with Bob Harris and Matt Waldman
Week 1 2024 reaction. Marvin Harrison Jr. reframed as a WR35-40 redraft asset on team fit, with Kyler Murray graded a 'fantasy points black hole' who supports only one of Harrison/McBride weekly. Kirk Cousins's job called insecure by end of September on lost velocity and an all-pistol game plan, with Michael Penix Jr. the natural fit for Pitts/London back-shoulder work. Isaiah Likely a must-add on Baltimore's jump to 53% two-TE sets, but Waldman rejects the 'washed' verdict on Mark Andrews outright. J.K. Dobbins promoted to must-start over Gus Edwards on passing-down usage; Zamir White benched after Waldman lost the week-one utilization argument to Alexander Mattison. Quentin Johnston's role fixed to underneath routes; Keon Coleman led Bills targets while Dalton Kincaid was shut out.

## [2024-09-10] ingest | Reception Perception: The Show — Week 1 Recap!
Puka Nacua to short-term IR with a new, more significant PCL injury — out 4+ games, Rams outside receiver role now open (DeMarcus Robinson vertical-only, Tyler Johnson a possible flash, Jordan Whittington the tough-player candidate). Cooper Kupp's 21 targets reframed by Harmon as 2022-Rams volume, slot-only at 31. Jameson Williams' first 100-yard game plus 42.9% first-read share raises his standing and nudges Amon-Ra St. Brown's ceiling down slightly. Caleb Williams (3/13 past 2.5s, zero completions beyond 15 air yards) and Jayden Daniels (2.35s time to throw, errant placement) both cratered in debut; Terry McLaurin logged zero pre-snap motions under Kingsbury. Brian Thomas Jr. and Ladd McConkey established as their teams' top targets; Alec Pierce upgraded from presumed zero given Richardson's deep-ball willingness.

## [2024-09-11] ingest | Matt Waldman's RSP Cast — Emerging College Football Stars and Backups to Know: RSP/Campus to Canton Podcast with Felix Sharpe
Six new devy/college pages created — Cam Ward reframed from day-three projection to Heisman-level riser on a big downfield-accuracy jump (56%/26% in 2022 to 73%/75% in 2024), plus true freshmen Jeremiah Smith and Ryan Williams as top devy assets, Sire Gaines as Jeanty's projected successor, Darian Mensah, and Tahj Brooks. Waldman quantified his ball-security threshold: only 3% of sub-threshold college backs ever reach elite fantasy production, 10% reach RB1/RB2. Guest Felix Sharpe attributed inline, not tracked.

## [2024-09-12] ingest | Matt Waldman's RSP Cast — Week 1 Developments, Identifying Worthwhile Trades, the Argument for Ed Reed's All-Time Greatness: RSP Film and Theory with Adam Harstad and Matt Waldman
Week 1 2024 reactions: Baker Mayfield materially upgraded (now climbing dirty pockets, has audible freedom; Waldman top-12 QB, Harstad top-10 to 15 ceiling). Quentin Johnston's role reworked to underneath/across-the-field, Bateman-type usage. Brian Thomas Jr. flagged as a likely Jaguars primary receiver by end of 2024-2025 on nuanced man/zone route work. Tank Bigsby capped at RB2 — cleaner, but the same player as at Auburn. Derek Carr swung back to 'interesting' on one 59-yard bomb to Rashid Shaheed. Jayden Daniels framed as a rushing/garbage-time fantasy QB who may suppress his own receivers. New concept page Win-Win Trade Construction from Harstad's Dynasty in Theory framework, including counting a freed roster spot as trade value.

## [2024-09-12] ingest | Reception Perception: The Show — Week 2 Storylines & Preview
Cousins' Achilles/pistol mismatch reframed Atlanta — Harmon keeps Drake London's arrow up on deployment while raising Michael Penix Jr. 2024 playing odds from ~5% to 30-40%. Marvin Harrison Jr.'s one-catch debut charted as a 92.2%-on-the-line, curl-heavy deployment problem rather than a talent problem. Tyler Lockett cut to 52% of snaps and off the field in 2WR sets, with Jaxon Smith-Njigba positioned for the leap; Harmon labels Lockett declining, not washed. Bryce Young downgraded to 'not physically talented enough to create,' capping Diontae Johnson at volume without production. Houston's Collins/Diggs/Dell roles validated as predicted ('wheels up'). Joe Burrow moved to show-me status.

## [2024-09-16] ingest | Matt Waldman's RSP Cast — Feel It or F-It 9.16.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman reversed his Marvin Harrison Jr. fade — start him now, with man coverage still the open question and his 900-950 yard projection possibly too low; Nabers stays his class WR1 on man-coverage skill. Pacheco to IR (fractured fibula) puts Perine ahead of Carson Steele in KC with an outside add expected. Miami's pass catchers each drop a tier under Skylar Thompson (Hill low-WR1/high-WR2, Waddle WR3, Achane gains dump-offs). Kincaid marked down to a flat-route/YAC coverage-priority role at 7.3 PPG; Bowers's TE3 start called as expected. Fields holds the Pittsburgh job while winning; Bryce Young judged both bad and badly situated, with Carolina expected to draft a QB. Eric All's dynasty buy window closing; Kamara revived by Kubiak's scheme.

## [2024-09-17] ingest | Reception Perception: The Show — Week 2 Takeaways!
Bryce Young benched for Andy Dalton — Harmon calls the trade up one of the worst in NFL history and sees a deadline trade as plausible. Caleb Williams cratering (0.2 rating beyond 10 air yards, 42% Texans blitz rate); Harmon puts blame on Shane Waldron and the interior line, not the rookie. Rome Odunze charting well but playing through an MCL injury. Quentin Johnston: Harmon partially reverses his 'worst receiver I charted in 2023' stance, now a useful functional receiver on coaching design. New Orleans scheme shift under Clint Kubiak (75% under center, 74% motion, Carr's play-action rate from last to 51.2%) lifts Carr, Shaheed, Olave and Kamara — Olave flagged as a buy at WR48. Colts room recalibrated: Alec Pierce a capped but real vertical role player, Pittman downgraded to inconsistent, Downs's absence called a big deal.

## [2024-09-19] ingest | Reception Perception: The Show — Fixing Struggling Offenses & Wide Receiver Buy or Sell
Harmon reverses on Jameson Williams — explicitly takes the L on his fifth-option offseason take after JMo posted a team-high 34.5% first-read share; Sam LaPorta's crashed 19.9% to 8.6%. George Pickens upgraded to best film of his career with a D.J. Moore year-three RP breakout comp. Alec Pierce sold at his top-six pace but bought as Richardson's downfield locked-in target, pushing Michael Pittman Jr. down to a likely fantasy disappointment. Courtland Sutton and the whole Denver passing game sold rest-of-season; Cleveland's receivers (Cooper, Jeudy, Elijah Moore) capped by Deshaun Watson at 31st in dropback success. Tank Dell bought long term with a patience caveat: post-injury plus an offseason shooting. DeAndre Hopkins on a torn MCL; Ja'Lynn Polk and Javon Baker flagged as the Patriots' unused answers.

## [2024-09-19] ingest | Matt Waldman's RSP Cast — Fran Tarkenton, Patrick Mahomes, and Skylar Thompson: RSP Film and Theory with Adam Harstad and Matt Waldman
Skylar Thompson jumps from roster flotsam to the Dolphins' starter on the Tua injury — Waldman reveals he was his top-graded QB in the 2022 class with second/third-round grades from other scouts, and frames him as a high-ceiling/low-floor swing worth a bench spot; Harstad claimed him over Andy Dalton and dropped Bryce Young for him, so Young's dynasty stock craters (no 2024 path back past Dalton). Chiefs backfield split: Waldman recommends Samaje Perine (passing game, red zone) while Harstad took Carson Steele as the higher-variance dart, and both still call the injured Isiah Pacheco the most valuable Chiefs back if he returns by ~Week 12 because the fantasy playoff weeks dominate. Two new concepts filed: Fantasy Playoff Week Value Weighting (Harstad's model: one guaranteed regular-season win ≈ +2% title odds, driven by bye leverage) and Roster Longevity as Talent Signal (surviving roster competition, not rookie flashes, is the late-round indicator). Tarkenton/Mahomes segment added an in-structure-vs-off-script framework, with Kyler Murray named the modern Tarkenton comp over Mahomes. New page: Keaontay Ingram.

## [2024-09-20] ingest | Matt Waldman's RSP Cast — Progress Reports on the 2023 and 2024 Rookie QB Classes in the NFL: Matt Waldman's RSP Scout Talk
Waldman's QB evaluation framework formalized as a new concept page (18-30 games to know a passer; windows at 6-8, 6-20, 15-30 games). Headline moves: Bryce Young — Waldman says bench him, scheme mismatch not height, and rejects Cosell's archetype argument; Will Levis — talent acknowledged but reckless key-moment decisions, would bench on principle, 'career could drown'; Jayden Daniels — 37% of passes behind the LOS vs 11% NFL average, correctly slow-rolled and rated ahead of Bo Nix for fantasy; Caleb Williams — scheme isn't hiding him, self-corrects; Skylar Thompson elevated to monitor status via Harstad's three-year-roster-survival signal.

## [2024-09-23] ingest | Matt Waldman's RSP Cast — Feel It or F–It 9.23.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman's Week 3 verdicts: Goedert's 10-catch game called circumstantial (A.J. Brown/Smith out) but top-12 TE upside retained; Calvin Austin III upgraded to a 'permanent high' with WR4 upside regardless of Fields-or-Wilson; Jauan Jennings validated as real while Deebo/Kittle are out after 11-175-3; Bucky Irving's rush share climbed 37.5%→56.3% but Waldman stopped short of declaring Rachaad White done; Jordan Mason endorsed as a starter for 60% of the league; Kyren Williams's role reframed around the Rams' 44.6% 12-personnel shift; Drake London and Kyle Pitts downgraded to 'long season' pending Penix. New pages for KaVontae Turpin, Jake Ferguson and Jauan Jennings. Concept layer gained Waldman's coaches-don't-develop-players position (25-30% credit for the Darnold/Mayfield turnarounds) and his 'defenses haven't scouted him yet' caution on Malik Willis.

## [2024-09-25] ingest | Matt Waldman's RSP Cast — Kalel Mullings and Justin Joly: RSP-Campus2Canton Podcast with Felix Sharpe and Matt Waldman
Kalel Mullings, Justin Joly, Nate Frazier, Carson Beck, Jalen Milroe and Quinshon Judkins added as new devy/college pages. Mullings overtakes Donovan Edwards as Michigan's lead interior back (17 forced missed tackles to five), with Edwards recast as a miscast space back. Waldman elevates Jordan Mason to 'could start for 60% of NFL teams', and tempers the Jayden Daniels hype (37% of throws at/behind the LOS, zero passes thrown moving left) while defending Bo Nix as more than an RPO dump-off passer.

## [2024-09-25] ingest | Reception Perception: The Show — Week 3 Takeaways!
Reception Perception Week 3 2024 recap. Terry McLaurin alignment story — 81% of Jayden Daniels' completions went right while McLaurin stayed left; he asked to flip and it produced the game-winner. Adonai Mitchell cratered to an 11% snap share (two routes) behind Alec Pierce once Josh Downs returned. Harmon flipped 180 on the Bears situation while defending Rome Odunze's charting (Wk2 dip attributed to a sprained MCL). Malik Nabers charted as a natural WR with a Garrett Wilson rookie-year route comp. Xavier Legette gets a runway with Thielen on IR but Harmon warns against boundary-X usage, comping Treylon Burks. New pages: Andy Dalton, plus concepts Receiver Alignment and Quarterback Field-Side Bias and Veteran Quarterback Value in Two-High Era.

## [2024-09-26] ingest | Reception Perception: The Show — Bring on Week 4!
Harmon reversed his Week 1 skepticism on Marvin Harrison Jr. ('looks like a star already'); Tank Dell downgraded — charting shows he is not the rookie-year separator post-injury; DeVonta Smith concussed, leaving Jahan Dotson a stopgap Harmon caps at 'functional third receiver'; Xavier Worthy recast as a gadget player miscast outside with the Tyreek Hill comp rejected; Travis Kelce flagged sluggish at 35 with no YAC; Brandon Aiyuk named a buy-low (out of football shape after the holdout, not declining) while Jauan Jennings surged; Khalil Shakir added as a stud power slot. New concept page: Yards After Catch Receiver Archetype.

## [2024-09-26] ingest | Matt Waldman's RSP Cast — Win-Now Trades, Jayden Daniels, and QB Value in Rookie Draft: RSP Film and Theory with Adam Harstad and Matt Waldman
Jayden Daniels reframed: Waldman says early production is scheme-manufactured (37% of throws at/behind the LOS vs 11% league average, non-progression reads) — a season-long starter but not a top-5 QB, with defenses expected to clamp the schemed looks by weeks 4-6; Harstad dissents on draft-capital grounds and slots him 5th-6th in a redone rookie draft. Terry McLaurin capped at WR41 on Kingsbury-offense concerns, backed by Kyler Murray never supporting a WR better than WR26 outside one DeAndre Hopkins season. Two new concept pages from Harstad's modeling: Win-Now Trade Timing (buy when chasing a bye, not the last playoff spot) and Draft Capital as Quarterback Hit Rate Proxy.

## [2024-09-30] ingest | Matt Waldman's RSP Cast — Feel It or F–It 9.30.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman's Sept RSP dynasty update projects Malik Nabers for 208 targets (would break Marvin Harrison Sr.'s record). Rashee Rice ACL fallout: Waldman rejects Xavier Worthy as the simple next man up and points to Travis Kelce plus Noah Gray (new page); Kareem Hunt (new page) leapfrogs Carson Steele, who fell to third up after a fumble. Christian Watson to IR — Dontayvion Wicks promoted to frontline starter. Jonathan Taylor high ankle sprain, Sermon/Goodson stopgaps. Daniels called elite fantasy production but not an elite QB, with regression flagged for Week 7-8; Bears defended on Caleb Williams. Chase Brown takes lead work from Zach Moss; Hubbard holds off Brooks all year; Breece Hall reaffirmed top-3-or-better; Kyler Murray downgraded hard (would take Goff).

## [2024-10-01] ingest | Reception Perception: The Show — Week 4 Takeaways + Rookie Roundup!
Harmon's elite-receiver tiering laid out explicitly: Jefferson/Hill/Adams/Brown/Lamb tier one, Chase and Aiyuk demoted to 'tier one and a half', Nico Collins argued into the group on 94th-percentile man-coverage charting plus a league-leading yardage total against the NFL's heaviest two-high diet. Garrett Wilson explicitly denied the leap. Jayden Reed elevated to possible top-12 receiver as his rookie-profile contested-catch flaw appears fixed; Christian Watson high ankle sprain clears the Green Bay room and hands Dontayvion Wicks a full-time outside role. Rashee Rice seriously injured, likely IR, shifting Kansas City routes to Xavier Worthy — whom Harmon still says cannot beat press at 165 lbs. Jordan Whittington's snaps spiked to 56 with Nacua out.

## [2024-10-03] ingest | Reception Perception: The Show — Davante Adams Forecast + Re-Evaluating The 2022 WR Class
Davante Adams filed a trade preference — Harmon still grades him a coverage-dictating alpha (85th/90th/91st percentile vs man/zone/press) but sees no clean landing spot, and flags target-efficiency risk for Brock Bowers without him. New pages for Mack Hollins. Keon Coleman's outlook cut: 3.8% slot rate, 81% on-line snaps, not beating press man; Curtis Samuel at a team-low 35% snaps and likely still turf-toe limited. 2022 WR class re-evaluated — Wilson the only one with a real year-two RP jump and Harmon's pick to reach elite, Olave and London flat year over year, Dotson regressed and written off, Jameson Williams reframed as a durable but volatile play-action role player.

## [2024-10-03] ingest | Matt Waldman's RSP Cast — The State of NFL Offenses, Roy Green, Daryl Lamonica, and Harstad's Razor: RSP Film and Theory with Adam Harstad and Matt Waldman
Waldman split the 2024 rookie QBs on situation rather than talent — Jayden Daniels 'inflated' by a heavily schemed one-to-two-read offense (supports about one receiver, i.e. Terry McLaurin), Caleb Williams 'deflated' and the only QB in the class he thinks could survive Chicago's line and progression demands. New concept pages for Harstad's Razor (assume selection bias first) and Rushing Quarterbacks and Receiver Support, where Waldman's 20%-of-rushing-yardage line is directly contested by Harstad, who says use rush attempts because yards make it circular (2022 Jalen Hurts looked like a passer only because A.J. Brown arrived). Harstad also argues offense isn't actually down — points per drive is third-best since 2016 — the change is collapsed RB targets becoming carries and scrambles, and he predicts the touchback moves to the 35, which would revive Cordarrelle Patterson's return value. Odell Beckham Jr. downgraded to playing out the string with shot knees.

## [2024-10-07] ingest | Matt Waldman's RSP Cast — Feel It or F--It 10.7.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman concedes Brock Bowers is the best receiving tight end in football and names it a landing-spot evaluation error; Kirk Cousins' Achilles concern dropped after a 500-yard game; Kyle Pitts marked down to a low-end TE1; Romeo Doubs benched for skipping practice, Packers exit odds up; Bucky Irving and Rachaad White both graded flex-level with the talent referendum rejected; Blake Corum's snap bump read as the Ronnie Rivers role, not a Kyren Williams takeover; Aiyuk's rapport with Purdy restored post-holdout; new pages for Justice Hill and Charlie Kolar; Waldman disagrees with Matt Harmon on Nico Collins' tier.

## [2024-10-08] ingest | Reception Perception: The Show — Week 5 Takeaways!
Pickens' Steelers standing cratered — 59% snap rate, Freiermuth's pointed quote, Harmon would trade him before the deadline. Wicks' 34% catch rate and 0% contested catch rate now outweigh elite RP separation grades, though Harmon calls it fixable confidence/tracking rather than hands. Keon Coleman reframed as a pure X (3.9% slot) whose usage Harmon thinks harms his development, with Kincaid capped at 65% of snaps under Joe Brady. Brian Thomas Jr. upgraded from slow-ramp projection to possible class-leading producer, ahead of Odunze and maybe Harrison Jr.

## [2024-10-10] ingest | Reception Perception: The Show — Nico Out, Drake Starting & Garrett Wilson ROS
Nico Collins to IR — Harmon says Houston has no downfield perimeter X left (Diggs no longer vertical, Dell below his 2023 charting post-injury, Hutchinson a Lazard-type big slot miscast outside). Garrett Wilson's 22-target game reframed as an indictment of Hackett: 62% nine/slant/out, almost nothing to the intermediate middle. Aaron Rodgers downgraded to a late-career Roethlisberger profile — immobile, must be perfect pre-snap, fooled by Minnesota and Denver. Drake Maye named starter; Harmon more bullish than consensus and wants Ja'Lynn Polk moved to flanker (83.9% vs zone, 64.7% vs man). Pickens at 59% of snaps on a blocking-effort theory from Koh. Harmon defends Marvin Harrison Jr.'s usage as the hardest X role in the league; buys Jalen Tolbert's breakout partially (87.8% zone, 73.7% man, Marvin Jones comp).

## [2024-10-10] ingest | Matt Waldman's RSP Cast — Rashee Rice, Emerging TEs, and 2025 NFL Draft RBs: Going Deep with Brandon Angelo and Matt Waldman
Rashee Rice reframed — Angelo says the under-reported hamstring tendon rupture, not the LCL, is the injury that matters: 16-18 months to full performance and possible permanent loss of the YAC trait; hold rather than sell into a weak market. Tank Bigsby flagged as a sell-into-the-peak matchup RB3 by both hosts, with Travis Etienne Jr. described as declining and never having developed through-contact skills. Josh Allen's 9-for-30 game read as hero-ball regression, with Dalton Kincaid and Keon Coleman called miscast. Mark Andrews written down as no longer a 1,000-yard tight end, elevating Charlie Kolar and Isaiah Likely. New pages for Travis Hunter and Brenton Strange; Ashton Jeanty established as the hosts' 2025 RB1 with Nicholas Singleton second.

## [2024-10-10] ingest | Matt Waldman's RSP Cast — Regression Candidates, Exuberance-Pessimism, and Problematic Figures: RSP Film and Theory with Adam Harstad and Matt Waldman
Regression episode: Harstad's YPC-as-noise framework marks [[Breece Hall]] (3.0 YPC vs 4.8 career) as a clear positive-regression buy and [[Saquon Barkley]]/[[Derrick Henry]]/[[J.K. Dobbins]] as unsustainable at ~6.0; [[Gus Edwards]] cited as the extreme case (top-10 all-time to last in league). Waldman fades [[Tank Bigsby]] as fool's gold with a sell-before-the-Packers-game window and prefers [[Rico Dowdle]]; contradicts the industry on [[Adonai Mitchell]] (drops, slipped routes) in favour of [[Alec Pierce]]. [[Marvin Harrison Jr.]] cut to low-end WR2/high-end WR3; [[Amari Cooper]] up on the Winston takeover; [[Wan'Dale Robinson]] and [[Jameson Williams]] flagged for usage regression. New concepts: [[Yards Per Carry as Noise]], [[Irrational Exuberance and Title Odds]] (Harstad publicly reverses his own 10-year-old calculated-pessimism piece), [[Separating the Player from the Person]].

## [2024-10-14] ingest | Matt Waldman's RSP Cast — Feel It or F--It 10.14.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman reversed on [[Kimani Vidal]] (was dismissive; now the clear [[J.K. Dobbins]] handcuff once [[Gus Edwards]] hit IR). [[Sean Tucker]] moved from third-back curiosity to expected [[Rachaad White]] timeshare after White's suspected midfoot sprain. [[Michael Pittman Jr.]] flagged as playing hurt through an IR rumor with [[Alec Pierce]] tipped to inherit his role. [[DK Metcalf]] downgraded on ball-attack technique. New page: [[Devaughn Vele]] (deep dynasty stash, young-Tim-Patrick comp). Waldman stayed cool on [[Caleb Williams]]' London game ('super hyperbolic') and said 'f--k it' for now on [[Drake Maye]]'s debut; bullish dynasty add on [[Bo Nix]].

## [2024-10-15] ingest | Reception Perception: The Show — Veterans Balling Out, Ravens on Fire & Drake Maye's First Start
Godwin reframed as a healthy, man-beating power slot on career-best efficiency (81% catch rate, 3rd in first downs per route run); Tank Dell downgraded behind Diggs — Harmon says he is not close to his rookie explosiveness; Diggs installed as Houston's WR1 with Collins out. Zay Flowers' usage materially shifted from screens to real intermediate/outbreaking routes, and Harmon calls Baltimore the most varied passing offense of the Lamar era (Koh dissents on EPA). Drake Maye's first start beat expectations; Polk's role and hands questioned, Boutte emerges as a possible vertical X. Will Levis called season-sinking, cratering Calvin Ridley's value despite a 44% air-yards share. New page: Sterling Shepard (real WR3/flanker role in Tampa).

## [2024-10-17] ingest | Reception Perception: The Show — Remaining Pieces in Cleveland & Vegas + Doubs/Slayton Temperature Check
Post-trade-deadline receiver-room reshuffle. Harmon backs [[Cedric Tillman]] — not [[Jerry Jeudy]] — as Cleveland's X after the Amari Cooper trade (Courtland Sutton comp, 80.6% curl success rate); Jeudy stays capped by an 8th-percentile zone success rate that rules out the slot. [[Jakobi Meyers]] is not a No. 1: targets nearly doubled without Davante Adams while his catch rate fell from 82.4% to 57.9%, and Harmon floated a trade. [[Brock Bowers]] gets huge volume but loses the coverage Adams bent. [[Romeo Doubs]] confirmed as the league's best sacrificial X (18% target rate on team-leading routes). [[Jordan Whittington]] surfaced as the NFL leader in team success rate when targeted (73.9%), with his role squeezed by [[Cooper Kupp]]'s Week 7-8 return. Two new concepts filed: [[Targets Versus Team Points Rule]] and [[Slot to Outside Conversion Risk]].

## [2024-10-17] ingest | Matt Waldman's RSP Cast — Writing, Craft, and Content in the Fantasy Industry: RSP Film and Theory with Adam Harstad
Non-football craft episode — no player or ranking movement. Adds four process/industry concept pages: Writing Craft in the Fantasy Industry, Feedback Scarcity and Analyst Development, Deliberate Rest and Creative Productivity, and Analyst Incentive Alignment and Audience Trust. Materially, it documents Waldman's own production constraints (RSP: ~1,100 pages edited in a month, perfection traded for deadline) and his and Adam Harstad's disclosure rules — Harstad routes his Pro Football Reference affiliate revenue to charity; Waldman takes no ads or gambling affiliates — which is context for weighting both analysts' recommendations elsewhere in the wiki.

## [2024-10-21] ingest | Matt Waldman's RSP Cast — Feel It or F--It 10.21.24: An RSP Cast with Bob Harris and Matt Waldman
Steelers QB change validated — Waldman calls Wilson's 3 TD/264 yd debut an easy layup, lifting Pickens, Calvin Austin III (his WR2) and Darnell Washington (new page) while Fields' bad down-and-distance is the stated reason he sat. Tank Bigsby flipped to sell-high after 26-118-2; Etienne still the better pass catcher. New concept 'Fantasy Quarterback Value vs NFL Quarterback Quality' — Mahomes is not a good fantasy QB (no top-10 week since Wk12 2023), Maye is a better fantasy than real QB, Richardson still holdable on rushing upside and job security. Watson's Achilles ends his season; Winston expected to start with a Flacco-run possible. Kareem Hunt moved ahead of Pacheco ('flash without a lot of substance'). Breece Hall named best open-field runner over Barkley and Gibbs. McCaffrey and Chubb both flagged for ramp-up risk. Marcus Mariota page created — scheme and matchup, not player.

## [2024-10-22] ingest | Reception Perception: The Show — Week 7 Takeaways!
Brandon Aiyuk feared torn ACL / multi-ligament knee — Harmon calls him the one 49ers WR they could not lose, cratering the team's man-coverage answer and elevating Ricky Pearsall (83.8% routes, ~50% success vs man) and Jauan Jennings (top-10 EPA/target, Koh's top waiver add). Xavier Worthy's charting turns sharply negative: 45.5% vs man, 25% vs press, near the bottom five in RP history. Cedric Tillman installed as Cleveland's outside X and plausibly already better than Jerry Jeudy. Romeo Doubs sold as Green Bay's best (Jayden Reed still is) but bought as most reliable and primary X. New concepts: Post-Bye Rookie Bump, Quarterback-Receiver Chemistry.

## [2024-10-23] ingest | Matt Waldman's RSP Cast — Matt Waldman and Felix Sharpe's RSP-C2C Podcast: Isaac Brown, Nick Marsh, Carson Beck and Anthony Richardson
Waldman buys the dip on Carson Beck after a 3-INT/56% game vs Texas — still his QB1, blames the loss of Bowers/McConkey rather than the player — and issues a strong Anthony Richardson buy (dynasty) / hold (redraft), arguing 'inexperienced, not raw' and that his first nine games match three MVP-caliber QBs. New campus pages: Isaac Brown (Louisville true-freshman RB, 8.3 YPC, C2C must-add), Nick Marsh (Michigan State freshman boundary WR, 3rd among FR in yards) and Aidan Chiles, whose preseason downgrade was situational and is partly reversed by Marsh's emergence. New concept: Recruiting Star Ratings and Early Breakout Age.

## [2024-10-24] ingest | Matt Waldman's RSP Cast — Brock Bowers vs. History, Trading Across Leagues, and Critiquing Alarmist Film Analysis: RSP Film and Theory with Adam Harstad
Brock Bowers evaluated against the historical rookie-TE field — Waldman puts him above LaPorta and Pitts with Jordan Reed as the best comp, but flags Raiders usage as an extension of the run game post-Davante Adams as a real cap on his ceiling. Waldman issues a dynasty buy-low on Anthony Richardson, arguing his nine-game profile matches Lamar-tier comps and that footwork critiques (Orlovsky) target the wrong developmental variables. New concept page for Adam Harstad's cross-league dynasty portfolio trading (many leagues, one team), with Waldman recording a philosophical disagreement in favor of concentration over diversification. Aging Curves page gains Harstad's random-walk argument, applied to Derrick Henry's declining YPC.

## [2024-10-24] ingest | Reception Perception: The Show — Nuk Traded, Bucs in Shambles & is BTJ the Best Rookie?
Godwin out for the year (dislocated ankle) — Tampa target hierarchy reshuffled to Shepard/Otten over McMillan. Hopkins traded to KC: still an on-line X (81.9%) with 80% slant success but 59.3% vs man and dead downfield; Worthy reframed as an ancillary slot piece who cannot beat press (3 targets, 0 catches, 1 INT on 27 press routes). BTJ elevated to a 'maybe' best rookie in the class on 77.3% man / 80% press, gated on a 68.6% zone rate. Jameson Williams suspended two games — Tim Patrick promoted to Lions WR2 favorite. Tennessee post-trade ranked the worst pass-catching room in the NFL, with Ridley and Levis both downgraded.

## [2024-10-28] ingest | Matt Waldman's RSP Cast — Feel It or F–It 10.28.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman defended Anthony Richardson's development (five of eight disputed passes charted as catchable drops; judge him against the Allen/Newton/Jackson/Elway/Favre archetype, not the box score) while conceding the fantasy season is a bust. Jameis Winston reframed as 'evolved to daring' and a clear upgrade on Deshaun Watson. Post-Amari-Cooper Browns order set: Njoku safest, Elijah Moore highest floor, Tillman highest ceiling (25%/22% target share), Jeudy biggest variable. Cade Otten moved ahead of Kyle Pitts for the rest of the season. Christian Kirk out for the year lifts Parker Washington to WR3/WR4 range. New pages: Adam Trautman, Rakim Jarrett, Nick Westbrook-Ikhine, plus the concept 'Mining Bad Offenses' (skim the surface of bad offenses, dig deep only on high-scoring ones). Waldman declared running back by committee dead for 2024.

## [2024-10-29] ingest | Reception Perception: The Show — Week 8 Breakdown!
Jacksonville's receiver room collapsed — Christian Kirk out for the season (broken collarbone), Brian Thomas Jr. out 2-4 weeks, Gabe Davis promoted to a volatile top-outside role against a brutal schedule. Harmon named Josh Downs the best receiver on the Colts over Michael Pittman Jr., and formalized a slot framework where ~80% success vs zone is the baseline but man-coverage success (McConkey 77.3%) is the ceiling unlock. DeAndre Hopkins lined up outside on 90.9% of his Chiefs debut snaps, contradicting Andy Reid's Rashee Rice slot framing; expect a December ramp. Cedric Tillman inherits Amari Cooper's X role and is Harmon's likely Browns lead WR ROS with Jameis Winston named starter. New: undrafted Panthers WR Jalen Coker charted as a power-slot candidate (81.1% vs zone, 69% vs man).

## [2024-10-31] ingest | Matt Waldman's RSP Cast — Anthony Richardson, Jameis Winston, Russell Wilson, Diontae Johnson, and Bo Nix: Going Deep with Brandon Angelo and Matt Waldman
Richardson benched for Flacco — Waldman/Angelo treat it as an org failure, not a talent verdict, and reframe him by archetype (Elway/Bradshaw/Allen/Newton/Jackson). Michael Pittman Jr. graded unplayable through a back injury. Jameis Winston takes over Cleveland after Watson's ruptured Achilles: Cedric Tillman emerges as primary target, Elijah Moore projected to outplay Jeudy, Njoku finally getting contested targets. Russell Wilson over Fields in Pittsburgh lifts Najee Harris (best career stretch) and Calvin Austin III. Diontae Johnson traded to Baltimore for a fifth — Waldman expects a break-glass playoff weapon, limited near-term fantasy value; Zay Flowers's role unaffected. Jalen Coker flagged as a dynasty waiver add and possible 2025 Panthers WR1. Bo Nix QB3 for October.

## [2024-10-31] ingest | Matt Waldman's RSP Cast — Tapping Out, Archetypes and Modeling, Tips on Analysis to Trust: RSP Film and Theory with Adam Harstad and Matt Waldman
Anthony Richardson reframed: Waldman defends the tap-out and argues he should be modeled only against the physical-freak QB archetype (Elway/Bradshaw/Newton/Allen), not a raw StatHead list; Harstad discounts the benching as a signal since QBs develop on the bench. Drake London's 2023 dynasty panic revisited — Harstad's 55-45 hold has him at WR5 vs Zay Flowers' WR16, though he still gives Flowers 40-45% long term. Three new concept pages on modeling discipline: comps as voodoo with p-hacking risk, confidence vs certainty, and being right for the wrong reasons.

## [2024-10-31] ingest | Reception Perception: The Show — Trades, Benchings & Patrick Peterson Joins!
Diontae Johnson traded to Baltimore — Harmon likes the separator/man-beater fit (Ravens face Cover 1 at 8th-highest rate) but doubts the deployment puzzle with Flowers and Andrews all working 10-15 yards; Bateman stays the 93.8 percent outside X. Carolina now has no target-earning X: Legette at risk of being forced there, Coker elevated as a Godwin-build power slot, Thielen labelled a progress stopper. Anthony Richardson benched for Joe Flacco — Harmon reversed from skeptical to supportive, calling the tap-out a symptom not a disease; Josh Downs is the clear beneficiary (Lockett-type), Pittman visibly diminished by his back injury. Stefon Diggs out for the season: Tank Dell (8.76 aDOT, not trusted deep) slides to X and Xavier Hutchinson becomes the Lazard-type flanker. New concept page from Patrick Peterson on why shutdown corners stopped travelling and why the slot's unrestricted route tree defeats even elite corners; Peterson named Ladd McConkey the most underrated receiver in the game.

## [2024-11-04] ingest | Matt Waldman's RSP Cast — Feel It or F–It 11.4.24: An RSP Cast with Bob Harris and Matt Waldman
Colts QB change dominates — Waldman reads the Anthony Richardson benching as owner-driven and reversible, and calls Flacco a lower-ceiling stopgap; Michael Pittman Jr. flagged as shouldn't-be-playing hurt. Jayden Reed elevated to Packers WR1 with elite-route-runner upside. C.J. Stroud downgraded to a fade until Nico Collins returns. Tank Bigsby warned as RB3/RB4 until the fantasy playoffs; Brenton Strange's zero-target game blamed on Jaguars coaching.

## [2024-11-05] ingest | Reception Perception: The Show — Week 9 Breakdown & Real or Mirage?
Chris Olave suffers a fourth known career concussion and is expected to hit IR — Harmon still rates him a top young receiver but the injury pattern now dominates the page. Terry McLaurin upgraded to a career-best season on Jayden Daniels chemistry (10% TD rate, 2.32 YPRR, 70% catch rate). DJ Moore's slump called real, with no deep chemistry with Caleb Williams (27% catch rate, 56.0 rating on 20+ air yard targets). Keenan Allen moved to 'at the aging cliff.' Jaxon Smith-Njigba's Week 9 slot-vertical usage flagged as a possible unlock. Quentin Johnston reclassified from bust to useful X under Harbaugh, production still a mirage. Cedric Tillman added as a real starting-X breakout with a Courtland Sutton comp.

## [2024-11-07] ingest | Matt Waldman's RSP Cast — Generalists vs. Specialists, Optimal Development Behavior, Politics and Sport, and Suggestions about Politics: RSP Film and Theory with Adam Harstad and Matt Waldman
Theory-heavy Film and Theory episode; no rankings moved. New concept pages for multi-sport athletic transfer (generalist-then-specialist development) and the 80-90% deliberate-practice development band, plus a Politics and Sport history page from Adam Harstad (untracked). Waldman's evaluation caution recorded on Mahomes (shortstop movement traits), Anthony Richardson (single-drop mechanics over-read) and Derrick Henry (unfamiliar camp footwork drill misread as bad feet); Rookie QB windows now carries the intermittent-development argument.

## [2024-11-11] ingest | Matt Waldman's RSP Cast — Feel It or F–It 11.11.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman names [[Joe Burrow]] the NFL's best QB and [[Ja'Marr Chase]] his clear WR1 over [[Justin Jefferson]]. [[Mark Andrews]] recovered from TE29 (Wk 6) to TE8 on a first 20% target share — usage, not decline. [[Christian McCaffrey]] took 13 of 15 carries in his return, effectively ending the [[Jordan Mason]] split. [[Bo Nix]] moves toward best rookie QB while [[Jayden Daniels]] dips to QB10 over three weeks (comp% 68 to 58). [[Chuba Hubbard]]'s four-year extension does NOT change Waldman's Bijan/Gibbs-tier read on [[Jonathan Brooks]]. [[Dalton Kincaid]] downgraded on Josh Allen fit plus a knee injury; [[Marquez Valdes-Scantling]]'s spike week discounted 50-55%; [[Anthony Richardson]] benching called pure optics. Two new concept pages: Quarterback Pressure and Career Trajectory, Resilience and Coach-GM Fit.

## [2024-11-12] ingest | Reception Perception: The Show — Poor Quarterback Play & Big Week 10 Performances
Week 10 2024 reaction. Harmon declares the Jets, Bears and Giants offenses cooked for 2024 — Rodgers questions shift to whether he shuts himself down, Daniel Jones benching read as imminent off the injury-guarantee leak. Caleb Williams post-bye regression framed as a coaching/O-line ruination blueprint, not a bust call; 3rd in NFL sack rate. Bryce Young cited as a benching that worked, informing the Anthony Richardson call (Flacco worse by EPA/drop-back). Big role shift: Jauan Jennings named San Francisco's full-time X (75% wide vs prior 50-50), which Harmon buys and which frees Ricky Pearsall into the flanker/slot option-route role. Sells on the MVS and Metchie Week 10 spikes, with Koh dissenting to a tentative Metchie buy on role. Stroud's ugly outside/pressure splits attributed to Nico Collins's absence.
New pages: Jalen Coker.

## [2024-11-14] ingest | Reception Perception: The Show — 2024 Rookie Round-Up!
Reception Perception 2024 rookie report charting lands: Ladd McConkey vaults to Harmon's top rookie dynasty riser (class-best 75.8% vs man, 83% contested); Xavier Worthy cratered (40% vs press, 33% contested, 100% down on first contact) with Keon Coleman now rated ahead of him; Marvin Harrison Jr. reframed as an in-breaking technician miscast at ISO X, zero catches in space in four games; Malik Nabers the class's best performer but sub-average vs zone. New pages: Will Dissly (third in Chargers first-read share).

## [2024-11-14] ingest | Matt Waldman's RSP Cast — Caleb Williams, Drew Lock, Trey Lance, Resilience and Detroit: Going Deep with Brandon Angelo and Matt Waldman
Bears offense reframed as organizational failure, not a Caleb Williams talent verdict — Angelo blames Poles/Eberflus/Waldron, expects Thomas Brown to restore accountability. D.J. Moore's stock cut: miscast at X, called a shell of himself, seen leaving the field mid-play; Rome Odunze named Chicago's best separator and pushed for outside snaps. Giants QB change lands — Drew Lock over Daniel Jones, with Malik Nabers projected for a vertical/contested target bump (Waldman comps him to Tim Patrick plus Jerry Jeudy with more speed and better hands) and Singletary favored over Tyrone Tracy Jr. on passing downs. Waldman brands Daniel Jones's draft capital fraudulent (the Cutcliffe myth) and comps him to Trubisky. New brakes on Jayden Daniels via the RG3 8.59 AY/A parallel; C.J. Stroud's regression attributed to lost pass protection, not talent. Angelo says most GMs would now take Malik Willis over Will Levis.

## [2024-11-14] ingest | Matt Waldman's RSP Cast — We (Still) Probably Think about Age the Wrong Way and Dented Cans: RSP Film and Theory with Adam Harstad and Matt Waldman
Age-cliff framework recorded over the conventional age curve (careers fluctuate around a peak, then fall off abruptly; population curve is ecological fallacy). New concept pages: Dented Cans. Waldman flipped public on best receiver — Ja'Marr Chase now his No. 1 over Justin Jefferson, while Harstad moved the opposite way to Jefferson. Jaylen Waddle flagged as the headline 2024 buy-low (367 yards in 9 games, WR57-60, skills intact); Rhamondre Stevenson, Trevor Lawrence, Javonte Williams and Khalil Herbert added as dented cans. Kyler Murray is an explicit host disagreement: Harstad says the buy window has closed at QB7, Waldman calls him overrated and doubts he can support both Trey McBride and Marvin Harrison Jr. DK Metcalf downgraded to bottom-of-top-15 skill, behind Jaylen Waddle for both hosts.

## [2024-11-18] ingest | Matt Waldman's RSP Cast — Feel It or F–It 11.18.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman flips positive on [[Bo Nix]] (best rookie QB; QB4 since wk5) and formalizes his game-management/bandwidth framework for why the industry missed. [[Anthony Richardson]] goes back into his lineups as a swing-for-the-fences streamer. [[Jayden Daniels]] downgraded — the slide to QB17 since wk7 is pinned on slow second/third reads and refusal to climb pockets, not the rib injury. [[Michael Penix Jr.]] named a dynasty-only buy-low. New pages: [[Tommy DeVito]] (named Giants starter over Drew Lock) and concept [[Quarterback Game Management and Bandwidth]]. [[J.K. Dobbins]] projected top-12 for 2025 with top-5 upside; [[Ladd McConkey]] believed to be playing hurt for ~six games; [[Quentin Johnston]] written off as a ball-tracker; [[Marshawn Lloyd]] flagged for fumbles with [[Christopher Brooks]] as the better bet.

## [2024-11-20] ingest | Reception Perception: The Show — Week 11 Takeaways!
Deebo Samuel downgraded — Koh's YAC per reception decline 12.3 (2020) to 8.86 (2024), Harmon expects him squeezed out of SF in 2025 and a trade candidate. Jaxon Smith-Njigba's post-bye breakout validated: man-coverage YPRR 1.98 to 2.39, air yards per target 6.2 to 9.8, Keenan Allen upside comp. Jauan Jennings promoted to legitimate perimeter starter (45% first-read target share, YPRR near Nico Collins/A.J. Brown) but capped below No. 1. Ja'Lynn Polk cratered — misdeployed as a vertical X (84.9% outside), drops and coaching-staff friction; Kayshon Boutte leads NE routes (96.3%) with Harmon unconvinced. Malik Nabers' outlook dims with Tommy DeVito starting. New concept pages: none — merged into Slot to Outside Conversion Risk and Yards After Catch Receiver Archetype.

## [2024-11-21] ingest | Reception Perception: The Show — Temperature Check in CLE, LA & DEN + Disappointing WR Seasons
Harmon ranks 2024's non-injury WR disappointments least-to-most: Marvin Harrison Jr. (hard PhD-level X role, not disappointing on film), Calvin Ridley, Jordan Addison (no year-two jump; 'solid number two' is his level), Tank Dell (lost explosive separation post-injury, aDOT 14.3 to 10.19), Jaylen Waddle (never the designed target; Jonnu Smith absorbing usage), DJ Moore most disappointing and miscast at X. Puka Nacua credited with a second-year level jump as the intentional first read. Bo Nix, Courtland Sutton (30% target share since Week 8) and the Denver offense upgraded after poor September film; Marvin Mims Jr. recast as a gadget piece; Troy Franklin lacking Nix chemistry. Cleveland's Tillman/Moore/Jeudy all made relevant by Jameis Winston, with Harmon caveating a statistical inflation effect. New pages: Jonnu Smith, Devaughn Vele, plus concepts Sacrificial X Receiver and Role Difficulty and Replaceability.

## [2024-11-22] ingest | Matt Waldman's RSP Cast — How to Find Waiver Gems and 'The' Dented Can for 2025: RSP Film and Theory with Adam Harstad and Matt Waldman
Named [[Chris Olave]] 'the' dented can for 2025 — Harstad's No. 1 dynasty buy, 7th-best rookie season since 2008, argued via four uncorrelated processes all loving him despite a sub-top-20 dynasty price. New concepts: [[Waiver Wire Archetypes and Organizational Support]] (waivers ≈5% of starts; hunt highly drafted backup QBs and organization-backed backup RBs) and [[Serial Correlation in Player Evaluation]]. New page [[Jerome Ford]] (Harstad cooling). Waldman moving off [[Skylar Thompson]] and [[Tyler Goodson]]; [[Christopher Brooks]] elevated to top backup-RB add; [[Malik Washington]] preferred over Ezukanma in Miami; [[Michael Penix Jr.]] and [[Tyler Allgeier]] flagged as next-August roster-crunch buys; Harstad updated his [[Derek Carr]] teammate prior downward after the Olave hospital ball.

## [2024-11-25] ingest | Matt Waldman's RSP Cast — Feel It or F–It 11.25.24: An RSP Cast with Bob Harris and Matt Waldman
Bryce Young reversal — Waldman says the Chiefs game shut the door on Carolina drafting a QB in 2025. Caleb Williams projected up to top-12 (possibly top-5) QB scoring under Thomas Brown after a 28-point week. Nick Chubb reframed as a good NFL back but bad fantasy play and a future buy-low, with Barkley cast as 'Chubb in a good offense.' Anthony Richardson held as a Superflex QB2 on upside with his job secure over Flacco. Jonnu Smith established as Miami's true No. 1 pass-game weapon, demoting Waddle/Hill to co-star roles. Rome Odunze ranked No. 2 rookie WR on film, ahead of Marvin Harrison Jr. and Ladd McConkey. Pacheco expected to return on a sparing ramp with Hunt staying lead. New page: David Moore.

## [2024-11-26] ingest | Reception Perception: The Show — Week 12 Breakdown: Real or Mirage?
Harmon buys the [[Jaxon Smith-Njigba]] breakout as a real usage change (schemed into space on in-breakers, Lockett de-emphasized) and reverses upward on [[Bryce Young]] as a functional NFL starter. He publicly walks back his early-season dynasty ranking of [[Jayden Reed]] — good starter, not tier two — blaming Green Bay's last-in-NFL neutral pass rate rather than skill, while Koh argues the sub-70% snap share is misuse. New charting on [[Devaughn Vele]] (64% slot, 52.3% vs man, Tim Patrick comp, 27-year-old rookie). [[Ja'Tavion Sanders]] carted off with a neck injury; [[Deebo Samuel]] cratered to 0.75 YPRR in a broken SF offense; [[Dontayvion Wicks]]' role collapsed on drops and mental errors.

## [2024-11-29] ingest | Reception Perception: The Show — Surprising 2024 Stud Receivers!
Adonai Mitchell charted: elite vs press (84.2%) but 72% vs zone, worst-in-class with Brian Thomas Jr.; Harmon says X-receiver misused in slot, WR1 upside only by year three and likely blocked — Dontayvion Wicks comp accepted. George Pickens 'graduated' to a true WR1 in Harmon's eyes, a reversal of his earlier skepticism. Courtland Sutton reframed from cut/trade candidate to perfect Payton X on slants and digs with Bo Nix. Darnell Mooney's Atlanta breakout explained as inverted usage vs his Bears role; Harmon still calls Drake London the better receiver. Terry McLaurin's efficiency spike (71% catch rate, 14.4 air yards/target) credited to Jayden Daniels. JSN now Geno Smith's first read under pressure. New pages: Quarterback-Receiver Chemistry and Zone vs Man Route Running takes; MVS flagged as NFL leader in YPRR since Week 8 on 61 routes.

## [2024-12-02] ingest | Matt Waldman's RSP Cast — Feel It or F–It 12.2.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman on the Week 13 Feel It or F-It: McCaffrey out for the year reframes the RB stash board — new page for Sincere McCormick (LV speculative starter), Kareem Hunt downgraded to hold-only after Pacheco's return looked healthy, Christopher Brooks named the Jacobs handcuff over Marshawn Lloyd. Alec Pierce called his single best candidate for a league-winning playoff week; Westbrook-Ikhine's TD rate endorsed rather than faded. Ladd McConkey knee injury with Josh Palmer the volume beneficiary. Underrated/overrated: Jayden Reed underrated as ideal WR3 in a Deebo-style role, James Cook underrated in the RB1 tier, Stroud slightly overrated (young Matt Ryan mold, QB8-15), Kyler Murray fairly rated in fantasy but overrated in reality, Marvin Harrison Jr. slightly overrated on a catch-technique ceiling near WR12-15. Kirk Cousins fading (6 INT, 0 TD in three games) with Penix a superflex stash.

## [2024-12-03] ingest | Reception Perception: The Show — Week 13 Takeaways & 2024 Rookie Receiver Class Re-rank
Harmon re-ranks the 2024 rookie WR class at Week 13: Nabers 1, Harrison 2, McConkey 3 (close with Harrison), Odunze 4 over Brian Thomas Jr. on consistency despite BTJ's 2.0+ YPRR and Odunze's ~1.2. Big drop to Coleman (best of the rest, startable) and Legette; Pearsall gets the incomplete grade but the highest true upside; Xavier Worthy dismissed as not an impactful player. Polk and McMillan called disasters. Harmon publicly reverses on Bryce Young — pocket comfort and downfield eyes that did not exist as a rookie, credit to Dave Canales. Kirk Cousins declared cooked (0 TD / 6 INT in three losses, suspected leg issue). C.J. Stroud defended as a victim of a bottom-five OL and lost weapons but flagged for developing bad habits; QB26 in PPG. D.J. Moore rejuvenated under Thomas Brown (10 targets, 88 yards per game over three).

## [2024-12-05] ingest | Reception Perception: The Show — Jeudy Revenge Masterclass, WR/CB Matchups & Impending Free Agents
Jerry Jeudy re-rated after a record 9-235-1 game vs Denver — Harmon apologized for the start/sit miss and credits Stefanski's flanker role, while keeping his 8th-percentile-vs-zone criticism. Diontae Johnson suspended for refusing to enter a game; Harmon calls his free agent value torched. Mike Williams declared 'pretty much over'. Elijah Moore reframed as a vertical slot and a Meyers-priced bargain. Deshaun Watson written off as a starter. New concept page: Wide Receiver Free Agency Contract Tiers.

## [2024-12-05] ingest | Matt Waldman's RSP Cast — The RB Workload Myth and QB Crime and Punishment: RSP Film and Theory with Adam Harstad and Matt Waldman
Harstad's age-controlled workload argument now on the record: career/college carries do not predict decline, and heavy volume is a coaches' preference reveal — reframes [[Ashton Jeanty]]'s 700-plus college carries as a non-issue and the [[Josh Jacobs]]/[[Rhamondre Stevenson]] dynasty swap as a market error. Only replicated effect is short-term (30-carry close games, [[Joe Mixon]] Week 1). New concept pages for the workload myth and for QB slide-rule weaponization ([[Patrick Mahomes]] fake slides). [[Trevor Lawrence]] hit: both hosts back the ejection, Harstad calls the three-game ban PR-driven.

## [2024-12-09] ingest | Matt Waldman's RSP Cast — Feel It or F–It 12.9.24: An RSP Cast with Bob Harris and Matt Waldman
Marvin Harrison Jr. — Waldman says WR28 finish is exactly his pre-draft projection; contested-catch technique flaw called unlikely to be fixed, and Kyler Murray seen as a hard cap on his ceiling. Bryce Young reversed upward: Waldman 'feels it' on future star after the post-benching run. Kirk Cousins declared cooked (likely playing hurt, age-related recovery), with Penix held back for on-ramp/optics reasons. New concept page: Fantasy Black Hole Quarterbacks.

## [2024-12-10] ingest | Reception Perception: The Show — Week 14 Performances & #1 Receiver Questions
Harmon walks back his [[Jayden Reed]] dynasty-superstar push (zero games over 70% snaps in six weeks, 57th in targets); makes the tier-one case for [[Puka Nacua]] (2nd in YPRR vs both man and zone, hands leap at the catch point); reconsiders [[Jordan Addison]] as more than a classic No. 2 amid a 116-yard-per-game month; declares [[Jaxon Smith-Njigba]] over [[DK Metcalf]], [[Khalil Shakir]] over [[Amari Cooper]] and [[Jauan Jennings]] over [[Deebo Samuel]] as team No. 1s, keeps [[Drake London]] over [[Darnell Mooney]]; calls it the end of the line for [[Tyler Lockett]]; [[T.J. Hockenson]] emerges as Minnesota's man-coverage answer.

## [2024-12-12] ingest | Matt Waldman's RSP Cast — Bryce Young, Chase Brown, Sincere McCormick, and Top Technicians in the 2025 NFL Draft Class: Going Deep with Brandon Angelo and Matt Waldman
Bryce Young flipped to an emphatic dynasty buy from both Waldman and Angelo after the post-benching run — Angelo 'pushing the chips in'. Chase Brown established as a back-end RB1 with a ~98% snap share flagged to regress to 75-25. Sincere McCormick upgraded from waiver flier to likely Raiders starter (gap-scheme fit, best-back-vs-KC data point). New pages: Cam Skattebo (David Montgomery comp), Savion Williams (route-craft sleeper), Tetairoa McMillan (lone size ball-winner in a class both hosts call weak), and a new concept, Two-Way Player Routine and Snap Acclimation, for Angelo's Travis Hunter argument.

## [2024-12-12] ingest | Reception Perception: The Show — Ja'Marr Chase is Special, Philly Offense & Patrick Peterson Joins!
Chase reframed as the lone elite producer in a down WR year, with the leap attributed to deployment (32% slot vs 24.8% prior high, 6.7 YAC/rec) rather than pure talent; A.J. Brown's headline flips to career-best efficiency on collapsed volume (no double-digit target game since week one, 6.2 targets/game since). Hurts logged as a hyper-specific thrower whose offense bends to him; Barkley recorded as masking Philadelphia's design problems. Patrick Peterson (guest, untracked) added corner-side takes on Nico Collins vs Ramsey, aging-curve technique decay, and DK Metcalf as the combine-skepticism case.

## [2024-12-16] ingest | Matt Waldman's RSP Cast — Feel It or F–It 12.16.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman's contested-catch case against Marvin Harrison Jr. hardened into a stated ceiling (Tee Higgins-type without improvement). New page for San Jose State WR Nick Nash (Jauan Jennings comp, possible top-5 class grade). Injury shifts: Nick Chubb out for the season with a broken foot (Jerome Ford leads, 2025 split expected), David Montgomery out indefinitely with an MCL (Jahmyr Gibbs the play, Sione Vaki the cheap stash), Jaylen Waddle hurt (Malik Washington on the radar). Waldman: Ja'Marr Chase is the AFC North's best player and trading him would be indefensible; Tee Higgins is an excellent WR2 propped up by Chase and Burrow and should stay. Calvin Austin III named his pick to lead Pittsburgh's WRs in 2025 over a not-ready Roman Wilson; Tank Bigsby's odds of being Jacksonville's 2025 lead back called 'really low.'

## [2024-12-17] ingest | Reception Perception: The Show — Week 15 Takeaways!
Harmon calls Jalen Coker a dynasty buy after Week 15 showed him playing flanker (46.5% slot, 86% snaps), not slot-only — and says Carolina is misusing Xavier Legette at X. Tyreek Hill questioned as possibly no longer the same player at 30+; Tua graded at his worst under McDaniel (3-of-10 beyond 10 air yards, 3 INTs). Jerry Jeudy's 44th-to-4th yardage jump credited to the Winston effect and judged fragile. Sam Howell judged backup-level and a bad Seattle fit; A.J. Brown's first double-digit target game since Week 1. Harmon retracts his offseason Diontae Johnson-to-Carolina fit call.

## [2024-12-19] ingest | Reception Perception: The Show — Cousins & Jameis Benched + Week 16 WR/CB Matchups!
Cousins benched for Penix — Harmon backs it on a dead-last intermediate-EPA profile and says it neutered Drake London's Nacua-style middle-of-field role; Penix's charting (88% outs, 63% corners, below-average digs/curls/slants) points London and Mooney toward deeper out-breakers. Jeudy downgraded hard: Winston-era ~1,900-yard pace ends with DTR (minus 1.03 air yards/attempt) starting. Harmon calls the Deebo–49ers relationship over and puts Jauan Jennings clearly ahead of him. Guerendo added a hamstring DNP on a chronic-hamstring history after a 77% snap week. New concept material on quarterback-dependent receiver roles, alignment vs coverage, and corner travel tradeoffs.

## [2024-12-19] ingest | Matt Waldman's RSP Cast — NFL QB Lunacy (An Attempt to Appeal to Your Sanity): RSP Film and Theory with Adam Harstad and Matt Waldman
Kirk Cousins benched in Atlanta after 8 INT / 0 TD in four weeks — Waldman ties it to the post-Achilles velocity loss Brandon Angelo flagged pre-season, and the shrunken playbook. Michael Penix Jr. takes over: boom-bust QB2, boundary arm talent rivaling Caleb Williams, lifting Drake London and Kyle Pitts while Darnell Mooney (foot/Achilles, limited in practice) loses timing-route work. New concept page Multiple Quarterback Investment captures Adam Harstad's 50%-to-75% split-the-bet argument; Bryce Young's post-benching play cited as evidence benching aids development.

## [2024-12-23] ingest | Matt Waldman's RSP Cast — Feel It or F–It 12.23.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman reversed toward [[Bryce Young]] — projects him as one of the NFL's smartest pre-snap QBs within two years after the Chiefs/Cardinals tape. [[Marvin Harrison Jr.]] downgraded to a WR2/WR3 whose 2024 draft price may be his career peak value unless he reworks ball tracking and contested-catch technique. [[Kyle Pitts]] written off against [[Brock Bowers]] as the comp he failed to become. [[Jaylen Warren]] out-touched [[Najee Harris]] and is framed as a coming free-agent lead-back candidate; Najee's option not exercised. [[Chuba Hubbard]] credited as a rare multi-facet improver with [[Jonathan Brooks]] lost to a second ACL. Waldman now believes [[Saquon Barkley]] breaks Dickerson's 2,105-yard record, rates [[Jonathan Taylor]] as close to or equal in talent, and says [[Sam Darnold]] should stay in Minnesota or risk becoming Derek Carr part two. New concept page: Content Creator Audience and Paying Dues.

## [2024-12-24] ingest | Reception Perception: The Show — Tank Dell Injury, Penix Debut and Christmas Wish List
Tank Dell's second major leg injury in two years (dislocated kneecap, possible ACL/multi-ligament) — Harmon doubts the rookie-year player returns and calls 2024 a lost year regardless; Houston's post-Dell, post-Diggs WR room reduced to Nico Collins and nothing. Diontae Johnson released and fitted by Harmon as a flanker opposite Collins in Houston. New page: Michael Penix Jr. debut graded well (0 sacks on ~50% pressure rate, 43.8% of throws 10+ air yards vs Cousins' sub-35%), lifting Mooney/London outlooks. Amari Cooper cratered to 6th on the Bills in routes; Xavier Worthy upgraded via a partial Harmon walk-back; Hopkins reframed as a matchup-only piece. Garrett Wilson trade-request reporting logged; D.J. Moore read as burned out.

## [2024-12-30] ingest | Matt Waldman's RSP Cast — Feel It or F–It 12.30.24: An RSP Cast with Bob Harris and Matt Waldman
Waldman reframes [[C.J. Stroud]]'s down year as offensive line and receiver attrition rather than a true sophomore slump, with Bob Harris (untracked) flagging him as a double-digit-round 2025 rebound buy; [[Caleb Williams]] defended as a scheme/protection casualty who was QB6 from Week 11 under Thomas Brown. [[Ladd McConkey]] confirmed as no fluke with a projected future 1,500-yard season; [[Xavier Worthy]] graded a tier below Tyreek Hill and three-to-four tiers above Mecole Hardman; [[George Pickens]] downgraded to a 'diluted Tee Higgins' with Diontae Johnson trajectory risk. [[Kyler Murray]] called skilled but not good, capping [[Trey McBride]] (1,000 yards, 104 catches, no TDs until Week 17). New pages: [[Ameer Abdullah]], [[Sophomore Slump]]. [[Michael Penix Jr.]] and the Atlanta passing game named an underrated 2025 draft value.

## [2024-12-31] ingest | Reception Perception: The Show — Week 17 Takeaways!
Harmon reversed on two prior negatives: [[Marvin Mims Jr.]] (deployment as speed slot/backfield now fits his profile; 334 yards since Week 12, year-three breakout watch) and [[Adam Thielen]] (11.4 air yards per target, highest since 2020 — no longer empty calories). [[Brian Thomas Jr.]] elevated to 'already a superstar' despite a 34% target share inflated by Jaguars injuries. [[Xavier Legette]] cratered — X-receiver move going poorly, catch-point and confidence issues. [[Jerry Jeudy]] and [[Calvin Ridley]] classed as fine-but-fakey volume; [[Malik Nabers]] fantastic but not yet A.J. Brown. Green Bay verdict: no true No. 1, with Harmon capping [[Jayden Reed]] as a WR2 while Koh blames a snap share that never reaches 80%. [[Troy Franklin]] written down hard.

## [2025-01-06] ingest | Matt Waldman's RSP Cast — Feel It or F–It 1.6.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's coaching-carousel read reframes several quarterbacks: [[Caleb Williams]] endorsed as having survived a wrecked Bears situation (would happily start him), [[Trevor Lawrence]] placed above [[Geno Smith]]/[[Sam Darnold]] and far above the [[Daniel Jones]]/David Carr tier, [[Drake Maye]] graded below the other rookies but improving with accuracy/reads to fix. Indianapolis continuity around [[Anthony Richardson]] endorsed with drops and OL as the real problems. [[Tyreek Hill]] exit talk dismissed as post-game venting; McDaniel criticized for trusting only [[Tua Tagovailoa]]. [[Trey McBride]] argued to be Bowers-level talent held back by his QB situation.

## [2025-01-07] ingest | Reception Perception: The Show — 2024 Regular Season Comes to a Close
Tyreek Hill declares himself gone from Miami — Harmon sees a real age-31 step back in explosive separation and would be surprised if his RP numbers held peak; Washington/Rams/Denver named likeliest fits, plus a speculative Deebo-for-Tyreek swap. Quentin Johnston upgraded from unplayable to useful WR3 after a 13-catch, 186-yard finale and 8-TD season; Marvin Mims similarly reclassified as useful. Drake London's ceiling raised on Penix's downfield willingness (100 catches, 1,271 yards). Jalen McMillan called one of the season's most improved but touchdown-driven and a WR3, not WR2. New page: Jacob Cowing (slot-only, poor Shanahan fit).

## [2025-01-09] ingest | Reception Perception: The Show — 2024 NFL Season Wide Receiver Awards
Harmon's 2024 WR awards: [[Ja'Marr Chase]] best overall (triple crown, now a top-five route runner), [[Brian Thomas Jr.]] best rookie over [[Ladd McConkey]] with a tier-one ceiling by mid-2025, [[Jaxon Smith-Njigba]] most improved (bottom-of-tier-two, led NFL vs man from week 11). [[Puka Nacua]] tier-one and now creating his own plays. Two reversals: Harmon recants calling [[Alec Pierce]] worse than a sacrificial X, and Koh recants his Nacua-ceiling worry. [[Jayden Reed]] flagged as elite-efficiency but slot-pigeonholed with a 14.7% drop rate; [[Rome Odunze]]'s poor efficiency blamed on the Bears environment, not talent; [[Chris Godwin]] would have won best underneath but for injury; [[George Pickens]] disqualified from most improved over his sour finish; [[Tee Higgins]] best ball winner with Harmon arguing for a Cincinnati re-signing.

## [2025-01-13] ingest | Matt Waldman's RSP Cast — Feel It or F–It 1.13.25: An RSP Cast with Matt Harmon and Matt Waldman
2024 rookie WR class post-season review. Harmon reorders the class top: Brian Thomas Jr. now his best rookie by year's end, McConkey locked as Chargers' primary target for 2-3 years, Nabers discounted for 'empty calorie' volume. Marvin Harrison Jr. downgraded to a tier-two ceiling on contested-catch technique plus Kyler Murray. Ja'Lynn Polk cratered — worst rookie season in Harstad's model, blamed on being played out of position at X. Jermaine Burton declared radioactive on character. Jordan Addison upgraded from run-of-the-mill No.2 to needle-moving No.2. Tyreek Hill flagged as declining, Harmon would sell now. New under-the-radar 2025 names: Jalen Coker, Ricky Pearsall, Malik Washington, Javon Baker. New concept page for Harstad's rookie YPRR model.

## [2025-01-14] ingest | Reception Perception: The Show — Wild Card Weekend Recap!
Harmon's wild card recap: [[Ladd McConkey]] elevated to a no-weakness WR1 on 81.4% of LAC playoff passing yards; [[Quentin Johnston]] reframed from 'functional' to high-variance splash player Harmon won't rank top-35; [[George Pickens]] floated as a trade candidate Pittsburgh may be better off without, with Harmon warning he could be a net negative for a young QB; [[Romeo Doubs]] suffered another concussion, flagged as a major forward concern; Harmon calls for Green Bay to narrow the rotation and feature [[Jayden Reed]]. New concept page: Volatile Splash Receivers vs Metronome Consistency.

## [2025-01-16] ingest | Reception Perception: The Show — Divisional Round Preview!
Diontae Johnson cratered — cut by Houston, fourth team in a calendar year, Harmon calls him the biggest red flag in a weak 2025 WR free-agent class and would not be surprised if he is out of the league. Cooper Kupp declared off the map with Puka Nacua the Rams' alpha. Zay Flowers knee injury may cost him the divisional game and Harmon rates him good-not-great, not a true alpha. Nico Collins established as a capital-A alpha and top-five WR. New concept page Alpha Receiver vs Committee Pass Catchers records Harmon and Koh both taking the alpha build; Harmon expects Tee Higgins to be tagged again and DK Metcalf to stay in Seattle.

## [2025-01-20] ingest | Matt Waldman's RSP Cast — Feel It or F--It 1.20.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's franchise-building order set: Caleb Williams over Jayden Daniels (Chicago's 68 sacks read as context, not verdict); Nabers over Brian Thomas Jr. and McConkey on an environment adjustment; Bowers narrowly over McBride. C.J. Stroud reframed — both seasons outliers, Matt Ryan-esque mover undone by interior pressure. Trevor Lawrence's ceiling declared 97% offensive line; Drake Maye same prescription. New 2025 draft prices: Olave rounds 5-6 (low WR2/high WR3), Mixon and Kyren Williams as RB1s, Kupp as a Thielen-style WR3 (Bob Harris dissents, goes younger), Kelce only at low-end TE1 / high-end TE2. George Pickens expected out of Pittsburgh; Roman Wilson doubted as the successor. Waldman would keep Rodgers with the Jets and start Russell Wilson over Justin Fields.

## [2025-01-21] ingest | Reception Perception: The Show — Divisional Round Recap!
Harmon flips Baltimore's tight end room — Mark Andrews framed as a 2025 cut candidate with real drop issues, Isaiah Likely as a player he will draft 'too high' if Andrews leaves. Houston's offense diagnosed as a protection failure (51.2% pressure vs KC, league-high 55% vs stunts) rather than a Stroud problem; Tank Dell downgraded to 'gravy', Harmon and Koh split on whether Diggs returns. Cooper Kupp declared gone from LA and no longer mattering, with Nacua the bona fide No. 1 and Stafford's possible retirement the Rams' X factor. Rome Odunze X-vs-power-slot debate opened (Harmon: Allen Robinson type; Koh: perfect X). Kyler Murray labelled undeveloped with 'coach killer vibes'.

## [2025-01-23] ingest | Matt Waldman's RSP Cast — 2024 & 2025 NFL WR Draft Classes: Going Deep with Brandon Angelo and Matt Waldman
2025 WR class first pass: Waldman and Angelo both flag Tetairoa McMillan as overhyped (route running between tiers, Mike Williams niche) and Luther Burden III as closer-yet-farther-away; Matthew Golden installed as the safest 2025 WR and Jalen Royals as most under-bought. Travis Hunter is the only day-one primary starter, contingent on offensive snap share. Class depth cratered versus 2024 — 20 players scored 85-plus last year, ~6 this year. From the 2024 class: Xavier Legette written off as a tertiary splash type; Jermaine Burton written off off-field; Malik Washington, Rome Odunze and Ricky Pearsall named as 500-plus-yard gainers, with Washington the buy-before-the-Tyreek-news dynasty call. Marvin Harrison Jr. downgraded to limbo pending a Kyler Murray replacement. New pages for Luther Burden III, Matthew Golden, Jalen Royals, Andrew Armstrong, Konata Mumpfield, Isaiah Bond, LaJohntay Wester and Shedeur Sanders.

## [2025-01-23] ingest | Reception Perception: The Show — Coaching Carousel Continues & Conference Championships on Deck!
Harmon tiered the complementary WR2s (DeVonta Smith 1, Tee Higgins 2, Jaylen Waddle 3, Jordan Addison 4), floated JSN as possibly the best of the group and put Jameson Williams at the bottom on scheme-dependence with Ben Johnson gone; Odell Beckham Jr. cut from his dynasty rankings entirely. Amari Cooper and DeAndre Hopkins deadline trades declared busts (zero divisional-round yards); James Cook's receiving work eroding to Ty Johnson; Keon Coleman boxed in as a pure outside receiver; Drake Maye upgraded by the McDaniels OC hire.

## [2025-01-27] ingest | Matt Waldman's RSP Cast — Feel It or F–It 1.27.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's 2025 offseason bounce-back verdicts land: [[Christian McCaffrey]] faded (Achilles + age-29 cliff, out of R2), [[Kirk Cousins]] faded, [[Tyreek Hill]] downgraded from WR1 to 'has value' with two-high era capping his ceiling and off the NGS speed leaderboard. [[Chuba Hubbard]] cleared of one-year-wonder status but priced at a premium; [[Bucky Irving]] and [[Chase Brown]] both flagged as likely overdrafts (RB15-20, not RB1). [[Caleb Williams]] named Waldman's most productive second-year QB of the 2024 class under Ben Johnson. [[Jonathan Brooks]] stock cratered on injury. [[Dalton Kincaid]]'s down year attributed to usage, not talent, with [[Keon Coleman]] the receiver Josh Allen already trusts to win boundary balls.

## [2025-01-28] ingest | Reception Perception: The Show — Conference Championship Recap!
Buffalo receiver room reframed: Harmon declares Keon Coleman will never be the perimeter X and would be better in a Mack Hollins power/blocking role; Amari Cooper reduced to sub-nine-air-yard decoy usage. New concept pages for Tight End as Number One Read (Kincaid's first-round trade-up called a clear miss by Koh), Coaching Talent Elevation (McDermott questioned, Reid and Quinn credited) and Rushing Ecosystem and Running Back Weaponization. A.J. Brown established as league-best at 4.27 YPRR over Puka Nacua's sub-4.00. Chris Godwin named Harmon's preferred Washington free agent fit next to Terry McLaurin, with the knee injury as caveat; Zach Ertz's 16-target NFC title game framed as a losing distribution.

## [2025-01-30] ingest | Reception Perception: The Show — New Faces in New Places
Harmon's first extended Travis Hunter take — leans cornerback with a 12-snap offensive package, not a true NFL WR1, against Daniel Jeremiah's receiver-first view. C.J. Stroud's sophomore slump reframed as offensive line (league-worst blown blocks, 217 sack yards lost to stunts, only 2 of 24 sacks on the QB) plus a stale Slowik scheme, with top-10 upside intact if empowered in the gun. Seattle's Klint Kubiak hire moved several pages: JSN breakout case (Koh's Shaheed comp) vs Harmon's slot-usage caveat, Kenneth Walker as an under-center/outside-zone fit, Geno Smith a good drop-back match but floated as a Carroll trade target to Las Vegas, Tyler Lockett's era declared over, and DK Metcalf recast as a Shanahan X on in-breakers despite a 'Tarzan, plays like Jane' catch-point knock. New concept page for Shanahan system fit vs quarterback empowerment. Hosts expect no Stafford trade — he retires before joining a rebuild.

## [2025-02-03] ingest | Matt Waldman's RSP Cast — Feel It or F–It 2.3.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman set 2025 offseason quarterback prices: Baker Mayfield a buy at QB9-12 after a QB5 finish, Mahomes downgraded to a late QB1 pending Rashee Rice's recovery, Jalen Hurts a late-round-QB argument rather than a top-three lock. Sam Darnold's 2024 called a peak year that likely does not travel. Brian Thomas Jr. elevated to firm first-round pick on Liam Coen's slot praise. Out on Will Levis (processing, not mechanics) and Jermaine Burton after Duke Tobin's public callout. Tee Higgins reaffirmed as a WR2 archetype likely tagged; Kenneth Walker III boosted by Klint Kubiak's arrival; no concern over Detroit's brain drain for Jared Goff.

## [2025-02-04] ingest | Reception Perception: The Show — Coaching Changes Continue As Super Bowl Week Begins
Tank Dell cratered — Harmon's charting says the rookie-year player is likely gone for good and he would not be surprised by zero games in 2025; Houston pass game reframed around Nico Collins at ~160 targets plus role players. Chip Kelly's Raiders established as a rushing ecosystem worth drafting from, but Zamir White flagged as a poor scheme fit and possible cut. Brock Bowers and Jakobi Meyers given the Jordan Matthews / Jeremy Kerley first-read role. New page: Emeka Egbuka (Ohio State WR, uncharted). Harmon separates McVay's adaptable system from the Shanahan tree and wants C.J. Stroud given Stafford-style latitude under Nick Caley.

## [2025-02-05] ingest | Reception Perception: The Show — Cooper Kupp Landing Spots & Super Bowl LIX Preview
Cooper Kupp's Rams tenure effectively over — Harmon expects a release over a trade ($22.2M dead cap) and caps his remaining role at a 70-80% interior blocker-slot, no X; Jacksonville/Houston/New England the fits he likes. Xavier Worthy reframed as KC's most-used receiver (87.9% postseason route rate) and a man-coverage quick-hitter, not a zone beater. DeAndre Hopkins marginalized to 36.4% routes and one playoff catch; Isiah Pacheco phased out into a four-man committee behind Kareem Hunt (~55% snaps). Rashee Rice's 2025 availability flagged as doubly uncertain (suspension plus complicated injury).

## [2025-02-10] ingest | Matt Waldman's RSP Cast — Feel It or F–It 2.10.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's post-Super Bowl offseason board: [[Saquon Barkley]] stays odds-on RB1 but explicitly conditional on landing spots, with [[Breece Hall]] or [[Nick Chubb]] behind a good line able to join him — Chubb reframed as a top-12 back with 1,300-1,400-yard bell-cow upside if he leaves Cleveland. [[Jalen Hurts]] graded 'very good, verging on great' and possibly underpriced at QB4-5. [[Travis Kelce]] downgraded in absolute terms (700-900 yards, 4-6 TDs, an Antonio Gates comp) but flagged as a perennial ADP bargain; [[Davante Adams]] split into NFL WR1 capability vs fantasy WR2 value. [[Rome Odunze]] value up on a likely Keenan Allen exit plus Ben Johnson. New role framing — [[Tee Higgins]] as an elite WR2 who does not run WR1 routes ('baker, not chef'), [[Terry McLaurin]] as the chef. Buy prices set on [[A.J. Brown]] (mid-2nd), [[Tyreek Hill]] (3rd), [[Trey McBride]] (TE2, 3rd), [[Adam Thielen]] (post-round-12). [[Justin Fields]] held below Darnold and Winston and not a starter yet; [[Sam Darnold]] worth franchising to buy time on [[J.J. McCarthy]], who is not ready.

## [2025-02-11] ingest | Reception Perception: The Show — Super Bowl LIX Recap!
Kelce — Harmon says he should retire, two years into decline, $17M cap save if cut. Worthy — 157-yard Super Bowl line graded as garbage-time noise, though Harmon now calls him KC's best healthy skill player. Pacheco — future questioned after losing postseason snaps to Kareem Hunt. Rashee Rice — injury return plus suspension risk, and Harmon says he isn't the X receiver KC lacks. Hurts tier split: Koh top-five elite vs Harmon top 10-12.

## [2025-02-13] ingest | Matt Waldman's RSP Cast — 2025 NFL RB Draft Class Review: Going Deep with Brandon Angelo and Matt Waldman
2025 RB class review (Waldman + Angelo). Ashton Jeanty established as the consensus class RB1 (MJD ceiling, healthy J.K. Dobbins median). TreVeyon Henderson flagged as miscast — plus-athlete Kyren Williams, not a Gibbs. Thirteen new prospect pages created (Kaleb Johnson, Brashard Smith, Devin Neal, Woody Marks, TreVeyon Henderson, Omarion Hampton, Jarquez Hunter, Damien Martinez, Phil Mafah, Jordan James, RJ Harvey, Jaydon Blue, LeQuint Allen). New concept pages for Angelo's draft-round rookie touch-share data and for contact mitigation as the durability trait.

## [2025-02-13] ingest | Reception Perception: The Show — NFC East Wide Receiver Preview
Harmon's post-Super-Bowl NFC East preview: Malik Nabers moved up to a stated top-10-NFL ceiling and best after-catch prospect charted since 2021, with a call for a lid lifter alongside him; Terry McLaurin priced at roughly $30-31M/yr between A.J. Brown and Amon-Ra St. Brown, with Koh arguing for a cheaper three-year deal; Brandin Cooks written off as 'closer to done'; Jahan Dotson re-framed as a vertical slot with residual upside after a no-ramp-up 0.56 YPRR season; Luke McCaffrey downgraded on draft capital but flagged as a cheap dynasty throw-in on decent power-slot RP data. New concept pages for slot snap allocation, lid lifters and paying the quarterback.

## [2025-02-17] ingest | Matt Waldman's RSP Cast — Feel It or F–It 2.17.25: An RSP Cast with Bob Harris and Matt Waldman
First 2025 Underdog ADP reaction. Waldman fades pre-draft rookie RB pricing wholesale — [[Omarion Hampton]] 'criminally overpriced' at RB19, [[TreVeyon Henderson]] rejected as a Gibbs comp, [[Quinshon Judkins]] called the class's safest back but faded on price — and would take [[J.K. Dobbins]] over all of them except [[Ashton Jeanty]]. [[Kenneth Walker III]] jumps to a buy at RB18 on the Klint Kubiak fit; [[T.J. Hockenson]] reversed from feel to fade mid-segment over J.J. McCarthy uncertainty; [[Jahmyr Gibbs]] framed as 'Tony Pollard syndrome' against Footballguys' 1.01 projection; [[Michael Penix Jr.]] flagged as the QB2 value at QB19; [[Kyle Pitts]] still a buy at TE18 on the Penix fit. New pages: [[Tyler Warren]].

## [2025-02-19] ingest | Reception Perception: The Show — Veterans on the Move & NFC North WR Preview!
Deebo Samuel granted trade permission — Harmon sees no remaining 49ers role, Washington the cleanest fit; rush YPC collapsed to 3.2. Tyler Lockett reframed from free agent to retirement candidate. Evan Engram and Christian Kirk flagged as Jacksonville cap cuts, with Coen/Whipple ties possibly saving Kirk. Christian Watson's late-season ACL puts him outside Green Bay's 2025 plans. D.J. Moore called a screaming bounce-back on Ben Johnson motion/slot usage; Rome Odunze's slot split (1.55 vs 0.97 YPRR) added. Davante Adams expected to be cut by the Jets. New pages for prospects Tre Harris (Ole Miss, Alec Pierce comp) and Emeka Egbuka.

## [2025-02-21] ingest | Reception Perception: The Show — NFC South Wide Receiver Preview
Godwin — Harmon predicts a Tampa re-signing and grades him 83.7% vs zone / 75.2% vs man. Olave — availability now the headline risk (four known concussions in three years) despite a strong Kellen Moore scheme fit. Shaheed — meniscus tear, four-to-six-month return. Legette — role change to X blamed for a back-half collapse and four drops; Harmon undecided. Jalen Coker — new page, 2nd among rookies in YPRR vs man and graded above Legette. McMillan — 2.55 YPRR vs man from week 12 on, projected as a very good WR3. Kyle Pitts — called an offseason trade candidate. Baker Mayfield — Koh reverses to calling him a genuine talent elevator.

## [2025-02-24] ingest | Matt Waldman's RSP Cast — Feel It or F–It 2.24.25: An RSP Cast with Dwain McFarland and Matt Waldman
2025 pre-combine rookie class reset. Waldman goes on record below consensus on Tetairoa McMillan (possession/big-slot, poor vs tight man) and Tyler Warren ('if Warren's Brock Bowers, I'm John Coltrane'), and names Tahj Brooks as his Le'Veon Bell comp and likely top-ten RB grade. Travis Hunter graded an early-round fantasy draft killer because Waldman expects cornerback to win out. Kyle McCord written off on nine interceptable passes vs Pitt; Will Howard called a 'Josh Allen starter kit' with bad instructions; Jalen Milroe defended against hand-size and fumble knocks. New pages for Dylan Sampson, Will Howard, Kyle McCord, Jackson Dart, Harold Fannin Jr., Colston Loveland, Jayden Higgins and Xavier Restrepo, plus a new Prospect Model Grade vs Rank concept capturing guest Dwain McFarland's rookie supermodel (0.58/0.70/0.75 correlations, 60th-percentile threshold). Documented disagreement on Savion Williams: Waldman 12th at an 81.4 score, McFarland's model 51st percentile.

## [2025-02-26] ingest | Reception Perception: The Show — NFC West Wide Receiver Preview
Aiyuk's health becomes the 49ers' single point of failure — Harmon won't assume he's ready and floats PUP, with Pearsall explicitly not an X candidate. Kupp confirmed gone from LA and downgraded to 42nd in first downs per route run (Keenan Allen 48th); Nacua led the NFL at 17.7%. Harrison Jr. reframed as a deployment problem, not a talent one (79.2% outside, sacrificial-X route tree). Metcalf called plateaued as a good-not-elite X, while Smith-Njigba is named Seattle's best receiver with slot rate projected 77% toward 50/50. Lockett's release called all but certain; Kyler Murray given a hard ceiling.

## [2025-02-27] ingest | Matt Waldman's RSP Cast — 2025 NFL QB Draft Class Review: Going Deep with Brandon Angelo and Matt Waldman
2025 QB class established: Waldman and Angelo both put Cam Ward alone at QB1 with a sizable gap; Waldman elevates Jalen Milroe as the only challenger (Marino-like release, best QB runner since Lamar) and names Kurtis Rourke as an off-consensus starter candidate despite a season played on a re-torn ACL. Shedeur Sanders capped at a Tannehill tier by Angelo, with Waldman undecided on the starter projection. New pages for Tyler Shough (Angelo's Minshew-plus bridge starter bet) and Kurtis Rourke. Kyle McCord downgraded on charting — nine bad throws vs Pitt, repeated red-zone arm arrogance; Jackson Dart split into good-inside-20 / disaster-past-25. New concept page Neurologic Recovery and Movement Inventory captures Angelo's argument that post-surgical recovery is a neurologic problem, not a structural one.

## [2025-02-28] ingest | Reception Perception: The Show — AFC East Wide Receiver Preview
Harmon's AFC East preview moved several headline views: Davante Adams recast as a likely cap casualty and still the best available X despite a clear step down (~75% success vs man); Tyreek Hill now more likely than not to stay in Miami after a broad efficiency collapse (1.79 YPRR from 3.85) that Harmon reads as a real, if small, decline; Jaylen Waddle cratered to a career-low 1.56 YPRR and was deprioritized behind Jonnu Smith despite a 28.3M/yr deal; Keon Coleman formally labeled a sacrificial X (17.6% target rate, no outside separation) with the slot path blocked by Khalil Shakir's extension; Amari Cooper's Bills trade written off as a 'nothing burger'; Ja'Lynn Polk's 0.35 YPRR rookie year blamed jointly on the player and a misfit X deployment; Javon Baker deemed unchartable at ~40 routes. New pages: Drake Maye stance on OL-over-WR team building, Jonnu Smith, Malik Washington, Mack Hollins, Dalton Kincaid archetype misfit.

## [2025-03-03] ingest | Matt Waldman's RSP Cast — Feel It or F–It 3.3.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's pre-RSP 2025 board takes shape: Mason Taylor installed as his TE1 (new page) narrowly over Colston Loveland, with consensus TE1 Tyler Warren downgraded to 'most overvalued tight end in the class' on a Mike Gesicki comp, and Elijah Arroyo (new page) added as the upside alternative. Tetairoa McMillan cut down on separation concerns to a Mike Williams ceiling, outside the top 20-30 receivers he'd draft. Tahj Brooks and Andrew Armstrong named his two predicted draft-position outperformers. Cam Ward preferred over Shedeur Sanders as an immediate starter; Sanders best served sitting behind Rodgers in New York. Deebo Samuel's trade to Washington read as a strong Kingsbury scheme fit with health risk; Jayden Daniels held sober (QB1 and QB15 both in range) with Josh Allen as Waldman's QB1; Travis Kelce's return called a price problem, not a talent problem.

## [2025-03-05] ingest | Reception Perception: The Show — Latest NFL News & AFC North WR Preview!
Deebo Samuel traded to Washington — Harmon's partial 2024 charting shows man and zone success rates both falling and four straight years of declining YAC; graded a gadget/screen piece, not a true number two. Davante Adams released by the Jets — past peak but still one of the only true X receivers on the market, Chargers named the best fit and New England the biggest bag. Tee Higgins tagged a second time (~$26M) with 85-90% odds he stays but tag-and-trade live; Ja'Marr Chase talks stalled on ownership cash despite public highest-paid-non-QB commitments. George Pickens flagged as a real 2025 trade candidate with Pittsburgh 'not thrilled'. Jermaine Burton may not make Cincinnati's roster. Cedric Tillman upgraded on true-X flashes with a Courtland Sutton comp. New concept pages seeded on aging curves, committee receiver rooms and the YAC archetype.

## [2025-03-07] ingest | Reception Perception: The Show — AFC South Wide Receiver Preview
AFC South WR preview. [[Tank Dell]] out for all of 2025 after a multi-ligament knee tear (ACL/MCL/LCL/meniscus, multiple surgeries) — cratered. [[Christian Kirk]] released/traded out of Jacksonville, opening the slot for [[Parker Washington]]. [[Brian Thomas Jr.]] moved up to a tier-one, lead-the-NFL-in-targets projection with a [[Nico Collins]] ceiling comp. [[Stefon Diggs]] a 31-year-old free agent off a Week 8 ACL tear, PUP candidate. Harmon named [[Josh Downs]] the best receiver on the Colts and partially walked back his 'worse than a sacrificial X' line on [[Alec Pierce]], while blaming the failed slot experiment for [[Adonai Mitchell]]'s rocky rookie year. [[Matthew Golden]] disputed as the class's top receiver despite the 4.29.

## [2025-03-10] ingest | Matt Waldman's RSP Cast — Feel It or F–It 3.10.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman reversed UP on Harold Fannin Jr. post-Combine (Sam LaPorta shuttle/three-cone comp; slow 4.71 forty dismissed as noise) — now possibly a top-three TE in the class. Savion Williams re-scoped as a potential starting-caliber RB convert (Cordarrelle Patterson comp). Free agency moves: DK Metcalf to PIT faded as a non-elite WR2 in a run-first offense; George Pickens predicted to be traded out of Pittsburgh; Geno Smith to LV lifts Brock Bowers and Jakobi Meyers; Davante Adams to LAR judged additive rather than a cap on Puka Nacua, with Brandon Angelo's durability concern on Nacua the real risk; Christian Kirk to HOU as an upgrade on the rehabbing Tank Dell (Bob Harris: a year away); Ertz re-signed over Ben Sinnott in WAS; Gesicki at TE27 called a crazy value; Sean Tucker flagged as a free square at RB106. New pages: Mike Gesicki, Thomas Fidone, and the concept Offensive Line Investment and Skill Player Value.

## [2025-03-12] ingest | Reception Perception: The Show — Free Agency Off to a Hot Start!
Harmon's charted 2024 profile drops DK Metcalf to a career-low 71.3% success rate vs zone (10th pct) and 40% contested catch rate — he declares Metcalf plateaued and closer to WR28-30 than top five, even while liking the Arthur Smith in-breaker fit. George Pickens flagged as a likely trade with no second contract coming in Pittsburgh. Davante Adams to the Rams endorsed as a home-run fit and named the best charted WR of the RP era in graceful decline (zone 84.4% to 77%), with Cooper Kupp downgraded to a player who can no longer win outside or vs man. Puka Nacua's value explicitly defended. QB carousel: Geno Smith to LV (Harmon defends, Koh calls it a Raiders overpay), Darnold to SEA as a mild downgrade, Fields to NYJ as a bridge with the Garrett Wilson reunion unresolved.

## [2025-03-13] ingest | Reception Perception: The Show — Free Agency Continued: Kupp, Nuk, Godwin, Colts & More
Kupp released and reframed as a declining slot-only WR3 (106th in EPA/target); Hopkins to Baltimore charted better than expected but as a narrow-route third receiver, not a fantasy factor; Godwin re-signed on a discount with career-best charted 2024 (83.7% vs zone); Daniel Jones to Indianapolis splits the hosts — Koh expects him to beat Anthony Richardson, Harmon expects a split season and a fired staff — with Josh Downs the one Colts pass catcher Harmon likes in that world; Kirk to Houston liked, but Tunsil trade raises real C.J. Stroud protection concerns; sacrificial-X market wave (Slayton, Palmer, Dyami Brown, Hollins, MVS) with Brian Thomas Jr. getting slot reps in Jacksonville.

## [2025-03-18] ingest | Matt Waldman's RSP Cast — 2025 NFL Draft TE Class B-T: Matt Waldman's RSP Solo Cast
Waldman's 2025 pre-draft TE class board takes shape: Colston Loveland named his TE1 and, with Mason Taylor, the most pro-ready to handle a prototype role — which Waldman frames as a risk, not a compliment. Harold Fannin Jr. defended against the 40-time backlash (agility and GPS speed in NFL starter tiers, LaPorta comp). Tyler Warren graded a raw blocker with a Tucker Kraft-style play-action/red-zone path to early production. Jackson Hawes called the class's best inline blocker despite sitting near the bottom of the RSP board; Luke Lachey flagged as a tweener whose RSP grade likely exceeds NFL valuation. Nineteen new TE prospect pages created. Dynasty guidance: no 2025 TE in the first five rookie picks outside 1.5 PPR.

## [2025-03-18] ingest | Matt Waldman's RSP Cast — Feel It or F–It 3.17.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman downgrades [[C.J. Stroud]] toward QB2 after the Tunsil teardown and [[Tank Dell]]'s ACL; declares [[Daniel Jones]] staged optics with [[Anthony Richardson]] winning the Colts job easily; calls [[Najee Harris]] a career-year bet in LAC while [[Jaylen Warren]] inherits PIT volume; [[Jalen McMillan]] a loser to [[Chris Godwin]]'s return; [[DeAndre Swift]] expected to cede work to an early rookie back; [[Luther Burden III]] named class WR1 over [[Matthew Golden]]/[[Tetairoa McMillan]] with the gadget-usage model concern dismissed; [[Ashton Jeanty]] endorsed at 6 as a Carroll-fit Lynch archetype. New pages: [[Daniel Jackson]], [[Tai Felton]].

## [2025-03-19] ingest | Reception Perception: The Show — Deals Done in Cincinnati & How 'Bout a Kupp of Coffee in Seattle
Cooper Kupp cratered — Harmon calls his 2024 charting a disaster-level profile (3rd percentile vs man and press, slants down to 64.7%), 86.9% of snaps off the line, a slot-only role player in severe decline after Seattle's 3yr/$45M deal. Jaxon Smith-Njigba pushed up: Harmon reads the signing as Seattle betting he moves outside and is confident he can, over Koh's objection that JSN is not a matchup dictator. Ja'Marr Chase becomes the highest-paid non-QB in NFL history ($40.25M AAV) but Harmon would still take Justin Jefferson to start a franchise; Tee Higgins re-signed at ~$29M AAV, framed as taking a discount to remain the league's best No. 2. Marquez Valdes-Scantling added as Seattle's sacrificial X. Travis Hunter: Harmon charted him as a receiver and thinks the tide is turning toward full-time WR.

## [2025-03-21] ingest | Reception Perception: The Show — Stefon Diggs Visits NE, Gallup to Washington & Teams That Still Need WR Help
Diggs profile charted: RP decline confined to nines (47.1%) and digs, out-breaking routes still above average — Harmon wants a 60/40 flanker-slot, but flags age-31 ACL and expects a one-year incentive deal, with unsigned status read as a medical red flag. Gallup un-retires to WAS as a possible true-X fit for Daniels. Jakobi Meyers reframed as badly underpaid and a possible Raiders trade candidate. McConkey pushed toward 60/40 rather than slot-only; Quentin Johnston capped at ~3 targets a game as an off-line YAC flanker. Legette declared a move-around perimeter piece, not an X, after his post-bye X reps produced his worst games. New concept page on X receiver scarcity in the modern NFL.

## [2025-03-24] ingest | Matt Waldman's RSP Cast — 2025 NFL Draft WR Class A-Z: Matt Waldman's RSP Solo Cast
Waldman rejects the 'bad 2025 WR class' consensus — expects the normal 4-5 starter-production hits, with 38 prospects graded 80+ (vs 25 in 2024, 22 in 2023); [Dynasty] advises rebuilders trade 2025 rookie picks for earlier 2026/27 picks. Emeka Egbuka downgraded to role-limited flanker/slot, explicitly not in Puka Nacua's neighborhood, with Chad Reuter (untracked) recorded as disagreeing. Tetairoa McMillan would grade elite at the catch point but for clap attacks; Jayden Higgins called the class's best pass catcher but for hand strength; Tez Johnson's 154-pound size panic pushed back on via Gerald McNeil. Savion Williams and Luther Burden III named the two best open-field ball carriers in the class. Ten new prospect pages plus four new concepts (WR class success baseline, having skills vs being skilled, whiteboard players, Claypool-Galladay production privilege).

## [2025-03-24] ingest | Matt Waldman's RSP Cast — Feel It or F**k It 3.24.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman pushed back on the 2025 RB class as a 2017 repeat (expects 4-6 multi-year starters, most drafted day three) and reframed the WR class as short on primaries but deep in WR2-WR4 career types. Big ADP moves: Chris Godwin at WR33 called a true WR13 buy; Michael Pittman Jr. at WR53 a strong buy on the 2024 back-fracture excuse; Malik Nabers a top-five-overall pick with Jameis Winston force-feeding him. Rookie fades: Omarion Hampton at RB17 (B-back, long runway to speed), Tyler Warren at TE8 (Tucker Kraft comp, not Bowers), with Colston Loveland preferred at pick 129. New page: Marcus Yarns. Waldman warmed on TreVeyon Henderson as a 'deluxe DeAndre Swift'.

## [2025-03-26] ingest | Reception Perception: The Show — Aaron Rodgers, Jameis the Giant & First Batch of Rookie Profiles!
First 2025 RP rookie profiles land: Harmon grades [[Tetairoa McMillan]] tier two (not tier one) with elite comeback/dig separation but a 48.7% nine-route rate; [[Matthew Golden]] a tier-three late-first with sub-70% press success; [[Emeka Egbuka]] a first-round-worthy power slot whose 83.6% vs-zone would have led the 2024 class, with an Amon-Ra St. Brown ceiling. New concept page Power Slot Receiver Archetype. Free agency: Harmon says [[Jameis Winston]]'s 2yr/$8M means no 17-start season, capping the [[Malik Nabers]] spike; [[Brandin Cooks]] downgraded to WR3-at-best in New Orleans; Harmon predicts a pre-draft [[George Pickens]] trade.

## [2025-03-28] ingest | Reception Perception: The Show — Russ and Diggs Find New Homes & Cory Kinnan Talkin' Quarterbacks!
Malik Nabers' outlook downgraded on fit — Harmon says Russell Wilson's dead short-middle game strands Nabers' elite slant/dig charting; Stefon Diggs lands in New England and Harmon rejects the slot-only label, projecting him as their only man-beating flanker with a Week 5-6 full-health caveat. Cory Kinnan's QB charting inverts Cam Ward (42% deep, ~76% intermediate/82% middle — an intermediate passer, not a deep-ball artist), puts Shedeur Sanders in a Goff/Geno tier, calls Jackson Dart a third-round lottery ticket despite first-round buzz, and takes Jalen Milroe as a picks-33-50 upside shot with a very low floor.

## [2025-03-31] ingest | Matt Waldman's RSP Cast — 2025 NFL Draft QB Class C-W: Matt Waldman's RSP Solo Cast
Waldman's 2025 QB class solo cast: class graded deeper but weaker at the top than 2024, no Caleb Williams-tier prospect, ~1-2 of eight viable options expected to hit. New pages for Dillon Gabriel, Max Brosmer, Quinn Ewers, Seth Henigan and Hunter Dekkers. Jalen Milroe named the class's best pocket player with the most compact release in several classes; Kurtis Rourke emerges as Waldman's most compelling prospect after playing 2024 on a torn ACL; Kyle McCord flagged as a possible bust-out for doubling down on bad leverage reads; Cam Ward's fragmented drop footwork argues for a bench year; Shedeur Sanders pegged as a Geno Smith/Baker Mayfield-archetype distributor, not a dynamic athlete. New concepts: RSP Quarterback Charting Methodology and Prospect Age and the Raw Label. Dynasty stance: spend rookie capital on RB/WR and trade for a proven QB rather than stockpile this class.

## [2025-04-02] ingest | Reception Perception: The Show — Travis Hunter & Luther Burden Charts
Travis Hunter established as Harmon's highest-ever charted receiver prospect (92/97/97 percentile vs man/zone/press, all-green route chart, prime Odell Beckham Jr. comp) with the two-way deployment question unresolved. Luther Burden III positioned as the class's widest range of outcomes — highest non-Hunter ceiling, sub-80% zone success rate, 82.9% slot usage and reported work-ethic concerns; Aiyuk comp endorsed as the conditional path. McMillan and Egbuka downgraded to non-alpha tier a tear-and-a-half below Hunter.

## [2025-04-03] ingest | Matt Waldman's RSP Cast — 2025 NFL Draft Listener Questions: Going Deep with Brandon Angelo and Matt Waldman
Pre-draft listener Q&A splits the hosts on [[Isaiah Bond]] — Waldman near [[Matthew Golden]], Angelo below a 10th-percentile grade on effort plus league-wide off-field reports that could drop him to day three. [[Travis Hunter]] graded as Angelo's best WR prospect since 2019 and Waldman's class WR2, yet both keep [[Ashton Jeanty]] at 1.01 pre-draft on role uncertainty. [[Omarion Hampton]]'s stock argued down on second-level processing, with [[Damien Martinez]] and [[Tahj Brooks]] promoted as round-four rookie-draft value; [[TreVeyon Henderson]] named Angelo's 1.02 over [[Quinshon Judkins]]. [[Jalen Milroe]] elevated to Waldman's preferred QB of the class over [[Cam Ward]]. New pages: Kelly Akharaiyi (Waldman's lone-wolf UDFA sleeper) and Bhayshul Tuten (big-play traits, fumble-threshold red flag).

## [2025-04-04] ingest | Reception Perception: The Show — Dallas Gets Their Backup & Jayden Higgins Breakdown
Jayden Higgins graded a tier-five, good-day-two prospect by Harmon: prototypical X measurables (6-4, 215, 4.43, 6-7 wingspan) but 15th percentile vs man and 16th vs press, best deployed as a big slot/condensed flanker rather than boundary X — explicit Keon Coleman comp and Michael Pittman Jr. deployment blueprint. Harmon downgrades his historical Quentin Johnston grade from tier three to tier four. George Pickens' 2025 Steelers retention framed as contingent on landing Aaron Rodgers, otherwise a trade for draft capital. Joe Milton III traded to Dallas — Harmon dismissive, co-host Koh bullish on the tools.

## [2025-04-07] ingest | Matt Waldman's RSP Cast — Feel It or F–It 4.7.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's 2025 pre-draft class positions land: Luther Burden III named best receiver in the class and explicitly above Marvin Harrison Jr. outside the pure-X role; Tyler Warren cut down from Brock Bowers comps to a perennial low-end TE1 with poor hand placement as a blocker; Shedeur Sanders installed as the safest QB with Cam Ward the lowest floor and Jalen Milroe the highest ceiling; Mason Taylor elevated as the under-discussed TE with a Mark Andrews-style fit; Xavier Restrepo tagged overrated behind Daniel Jackson. New pages: Bru McCoy, Lan Larison. Also a Giants segment endorsing Ashton Jeanty over an early QB.

## [2025-04-08] ingest | Reception Perception: The Show — Julio Jones Retires, More Tutu Incoming & Jaylin Noel Chart!
Jaylin Noel jumps to a fringe top-five WR in Harmon's 2025 class (94% dig, 74.1% vs man, 23 bench reps) against a 76th consensus board rank, graded in the Ladd McConkey/Ricky Pearsall tier with a Josh Downs career comp. New page for Julio Jones on his retirement, with his 2016 Shanahan-X charting (86.2% zone / 76.3% man). Isaiah Bond flagged with serious character concerns that could drop him to day three. Tutu Atwell reframed as a $10M going-rate WR3 the Rams may still upgrade; Harmon uses the same contract tiers to defend Emeka Egbuka against the 'only a number two' knock. Harmon prefers Noel to teammate Jayden Higgins.

## [2025-04-11] ingest | Reception Perception: The Show — Tre Harris & Jack Bech Profiles + Cory Kinnan Back On!
Harmon's 2025 pre-draft charting: Tre Harris established as a volatile straight-line X (56% go/curl/screen, sub-8% out-breaking, Terrace Marshall statistical twin) with a second-round grade and a developmental year one; Jack Bech elevated to one of Harmon's favorite prospects in the class — best contested-catch rate, zero drops, 15% first-contact rate, 91st-percentile vs press — with the 72.4% outside-right alignment as the lone red flag and Jacksonville at 36 the named fit. Guest Cory Kinnan rejected the Gruden Josh Allen comp on Will Howard for Mason Rudolph and would not draft Quinn Ewers at all, citing three injuries in three years and lost arm drive in a QB-friendly Sarkisian scheme.

## [2025-04-14] ingest | Matt Waldman's RSP Cast — Feel It or F–It 4.15.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman defends Luther Burden III as his WR1 and articulates the RSP-vs-Reception Perception split (techniques projected vs results counted). New prospect pages: Kyle Williams (slightly overrated 4.40 riser, day-three value), plus first substantive grades on Jayden Higgins (WR6, scarce true X), Elic Ayomanor (overrated at the catch point, WR4/5 projection), Cam Skattebo (top-3 RB likely drafted despite headbutting pass pro), Arian Smith (correctable drops), Jaylin Noel (discount Matthew Golden) and Jaylin Lane (Mecole Hardman comp). Waldman takes Najee Harris over Omarion Hampton, calling Hampton a volume runner disguised as a big-play runner. Derek Carr's Saints tenure likely over on a shoulder surgery report; Rodgers still expected in Pittsburgh. New concepts: Scouting Sizzle Reels and Front Office Override, Pre-Draft Misinformation Season.

## [2025-04-16] ingest | Reception Perception: The Show — Kyle Williams, Isaiah Bond & Jalen Royals Charts!
Kyle Williams established as Harmon's favorite of the day-two group — natural separator, 66.7% in-space rate and 44% down-on-first-contact, priority second-round grade, expected to be drafted higher than consensus. Isaiah Bond split: elite vertical/dig charting (69.2% nine, 80.8% dig) against a 59% curl rate, 24th-percentile zone score and confirmed character red flags plus a sexual assault arrest, pushing him toward day three. Jalen Royals downgraded to 13th of 14 charted receivers on 84.6% left-outside deployment and a hitch-heavy Utah State route tree. New pages: Tory Horton (late-prep riser ranked ahead of Royals), plus concepts Elijah Moore Rule and Manufactured Touches vs Natural Separation. Harmon reiterates Rashee Rice as Reception Perception's biggest miss and the reason for humility on limited-deployment prospects.

## [2025-04-18] ingest | Reception Perception: The Show — Xavier Restrepo Profile & QB Prospect Roundup w/ Cory Kinnan!
Restrepo charted as a pure 'pop gun slot' — elite slants/flats/corners, 30th-percentile vs man, 4.8 pro day; Harmon sees no clean NFL landing spot and a PPR-scam outcome at best. Guest Cory Kinnan pushed back hard on Tyler Shough's first-round buzz (contact-averse, no anticipation, 33% dig success), called Dillon Gabriel a routine-dependent backup, and made the upside case for new page Riley Leonard (Josh McCown comp). New concept page on quarterback height and pocket sight lines.

## [2025-04-21] ingest | Matt Waldman's RSP Cast — Feel It or F–It 4.21.25: An RSP Cast with Bob Harris and Matt Waldman
Pre-draft Day 3 sweep from Waldman: new pages for Jacolby George, Xavier Guillory, Jordan Moore and Chimere Dike; Ja'Corey Brooks reframed as a top-7-board talent gated entirely by catch-point hands; Tez Johnson's 154-pound weigh-in called overblown; Terrance Ferguson explicitly held back post-combine as a schemed-up producer while Cam Skattebo is flagged to rise into Waldman's top five RBs; Jaylin Lane dismissed (Mecole Hardman, clap-catcher). Dynasty stance added: trade out of the 2025 rookie draft without a top-five pick. New concept 'Existing Roster Talent and Prospect Opportunity' — depth-chart grades as the overlooked input Waldman will add to the RSP grading key.

## [2025-04-21] ingest | Matt Waldman's RSP Cast — RSP Film & Data on the 2025 NFL Draft with Dwain McFarland and Matt Waldman
Waldman's 2025 pre-draft board mapped against Dwain McFarland's supermodel. Tyler Warren cratered to Waldman's TE5 (Michael Mayer/Tucker Kraft comp) with the no-draft-capital model dropping him 24 spots; Luther Burden III elevated to a 93 RSP score and top-2 WR with an independent Aiyuk comp from Waldman, Harmon and McFarland; Tetairoa McMillan split — model's WR1 vs Waldman's WR5, WR1 ceiling only from the slot; Jack Bech self-flagged as Waldman's likeliest overrate (86 would fall to 82 on four and a half points); Kyle Williams near-elite separator capped by remedial hands; Jaydon Blue kept out of the top 10 purely on a 1-per-45.5 fumble rate. New concept page: Draft Capital Removal Model Delta.

## [2025-04-22] ingest | Reception Perception: The Show — 2025 Rookie Class Draft Superlatives!
Harmon's pre-draft 2025 WR superlatives: Tory Horton named top sleeper (94th-pct press, class-best 38.5% TPRR, but one-side-of-field air-raid usage) and Andrew Armstrong best deep sleeper despite turning 25 as a rookie — both new pages. Jayden Higgins flagged as the class's riskiest WR, Harmon explicitly below consensus and worried he gets miscast as an X. Jaylin Noel edges Jack Bech as best route runner on zone feel; Bech better vs press. Travis Hunter reframed as best separator, not best route runner, with a 950-1,000-yard rookie ceiling if he lands in Cleveland's shaky QB/OL situation. Burden's gadget label rejected.

## [2025-04-24] ingest | Matt Waldman's RSP Cast — 2025 Draft Weekend Predictions and Fits: Going Deep with Brandon Angelo and Matt Waldman
Draft-eve RSP Cast: Waldman and Angelo both move well below consensus on Omarion Hampton (Waldman ~3C, Angelo RB4-5; James Robinson/Latavius Murray comps, poor processor) and on Tetairoa McMillan (Waldman WR5, Angelo flags McShay's effort reporting and says he is not a WR1 now). Waldman flips the Jalen Milroe narrative — he expects him to go HIGHER, reading anonymous-scout quotes once written about Mahomes, Hurts and Lamar Jackson as pre-draft misinformation. New: Waldman's explicit methodological contrast with Reception Perception (result-driven separation vs process/craft on film). Ashton Jeanty remains his RB1 but Jacksonville and especially Dallas are called awful landing spots on offensive line. Class-context call: 12 graded RB starters, only two or three backs in rounds 1-3, and multiple day-three double-dips, which discounts 2025 rookie RB draft capital.

## [2025-04-28] ingest | Reception Perception: The Show — Analyzing The Top-5 WR's Landing Spots
Post-draft WR landing spots: Harmon keeps [[Brian Thomas Jr.]] ahead of [[Travis Hunter]] for 2025 and dynasty despite Hunter's unlimited ceiling; [[Tetairoa McMillan]] to CAR moves [[Xavier Legette]] off the X (the alignment Harmon blames for his rookie collapse) and squeezes [[Jalen Coker]] behind [[Adam Thielen]], who Harmon says could be traded; [[Emeka Egbuka]] lands in [[Chris Godwin]]'s role, capping year-one value but strong in dynasty, and confirms [[Jalen McMillan]] as a schemed-open stretch player; [[Matthew Golden]] framed as [[Christian Watson]]'s vertical/in-breaker replacement in GB, with Koh unconvinced given weak man/press marks; [[Jayden Higgins]] rises sharply post-draft as a HOU power slot, and Harmon says [[Jaylin Noel]] (74% vs man, Josh Downs comp) may just be better.

## [2025-04-28] ingest | Matt Waldman's RSP Cast — Feel It or F–It 4.28.25: An RSP Cast with Bob Harris and Matt Waldman
Post-draft landing spots. Luther Burden III becomes Waldman's top dynasty WR of the class (Ben Johnson slot, more athletic Amon-Ra comp). Harold Fannin Jr. jumps to TE3 in 1.5PPR with Njoku's deal expiring; Tyler Warren stays TE4. Rashee Rice flagged via Brandon Angelo as possibly never regaining pre-injury athleticism, with Jalen Royals drafted as the same-skill insurance. RJ Harvey called a market overshoot against Derek Brown's RB3 ranking. Omarion Hampton reframed as a Gus Edwards-type timeshare rather than a Najee Harris replacement. Brashard Smith, Jordan James, Kyle Monangai and Mario Anderson added as late-round backs to monitor; Kurtis Rourke and Jalen Milroe named the only two QBs Waldman would draft. Shedeur Sanders slide attributed to athletic/arm limits plus family-interference risk, not to talent — new concept page Player Family Interference and Draft Risk.

## [2025-04-29] ingest | Reception Perception: The Show — Analyzing Landing Spots For Round 2 & 3 Pass Catchers
Round 2-3 pass catchers get landing-spot evaluations. New page: Pat Bryant (DEN, Tim Patrick comp, no speed). Luther Burden III — Harmon endorses the Chicago coaching fit while rejecting the Amon-Ra St. Brown comp; better vs man (71.2%) than zone. D.J. Moore flagged as on notice under Ben Johnson with Burden overlapping his skill set. Tre Harris installed as the Chargers' X, moving Quentin Johnston to flanker. Kyle Williams comped to young Stefon Diggs and preferred to Jayden Higgins. Isaac TeSlaa called a huge Detroit bet with no clear position. Savion Williams graded as a gadget-only weapon; Harmon argues Jayden Reed should be freed from that role.

## [2025-05-05] ingest | Matt Waldman's RSP Cast — Feel It or F–It 5.5.25: An RSP Cast with Bob Harris and Matt Waldman
Chicago's rebuilt offense re-rated across the board — Waldman calls Caleb Williams a league-winning value at QB8 and D.J. Moore underpriced at WR18, while flagging DeAndre Swift (RB32) as a wait-until-July buy pending a veteran addition. New rookie evaluations: Kaleb Johnson as the safest RB in the 2025 class, Harold Fannin Jr. as class TE3 and a TE35 free square, Kyle Williams as a boom/bust hands risk (WR1 upside or the next Tyquan Thornton), Jaydon Blue as the likeliest Dallas lead back over Javonte Williams, Kyle Monangai as the sleeper Bears back. Christian McCaffrey feeling it at RB5 on unrestricted practice, though Waldman prefers Derrick Henry a pick later. Shedeur Sanders given ~30% odds of starting (Bob Harris argued higher). New concept page: Rookie Pick Accumulation and Trading Out.

## [2025-05-07] ingest | Reception Perception: The Show — Breaking Down Some Post-Draft Signings
Amari Cooper's stock cratered on Harmon's charting — 23rd percentile vs man, 34th vs zone, 29th vs press, with the curl and nine routes gone — amid Dallas reunion rumors. Diontae Johnson signed to Cleveland at the $1.17M vet minimum with zero guaranteed money, Harmon projecting a first-time slot role behind Cedric Tillman at X. Elijah Moore to Buffalo liked as football, dismissed as fantasy in a crowded room. Hunter Renfrow back from an ulcerative colitis year off but both hosts doubt he makes Carolina's 53. New pages: Robert Woods (PIT, locker-room signing) and the concept Tight End as X Receiver Experiment, which reframes Kyle Pitts, Dalton Kincaid and the Elijah Arroyo report as one repeated failure mode.

## [2025-05-09] ingest | Reception Perception: The Show — Pickens to Dallas & Day 3 Receivers We Like!
George Pickens moves to Dallas — Harmon reframes his outlook as a boundary-X fit with Dak Prescott that frees CeeDee Lamb to the slot, with a stated range from best No. 2 receiver in the league to suspended by Week 6; Pittsburgh's room downgraded to an Arthur Smith orbit around DK Metcalf with Rudolph/Howard at QB. Five new rookie/UDFA pages created (Chimere Dike, Elic Ayomanor, Xavier Restrepo, KeAndre Lambert-Smith, Elijah Badger) plus updated evaluations on Dont'e Thornton Jr., Jalen Royals, Tory Horton and Andrew Armstrong. Horton is the headline dynasty mover: Harmon's priority second-round grade against a fifth-round landing spot, already drafted in the fourth round of rookie drafts.

## [2025-05-12] ingest | Matt Waldman's RSP Cast — Feel It or F–It 5.12.25: An RSP Cast with Bob Harris and Matt Waldman
Derek Carr retired — Waldman refuses to move Chris Olave up ('the bombing is over, you still have the cleanup') and pins Rashid Shaheed's WR55 price as correct lottery-ticket value. George Pickens traded to Dallas: Waldman says 'fuck it' on the Cowboys, comping him to MVS with better hands, worse routes and a bad attitude, while CeeDee Lamb stays set-and-forget and Dak Prescott becomes a QB18 value. Tyler Shough tabbed as the Saints' hope but not ready ('remedial Jay Cutler'). Roman Wilson's year-two leap buzz dismissed as May leak season. Joe Flacco endorsed as Cleveland's Week 1 starter, lifting Jerry Jeudy at WR38. Tre Harris gets the dynasty edge over Quentin Johnston, who is reported on the roster bubble. Matthew Golden framed as Green Bay's future top-two starter with the Christian Watson era over. Woody Marks capped at RB3 behind Joe Mixon.

## [2025-05-14] ingest | Reception Perception: The Show — Last Year's Big 3 Ended Up Being the Big 4
Harmon's post-rookie-year charting reframes the 2024 WR class as a big four. Marvin Harrison Jr.: separation defended as good (73/81/76 man/zone/press) but catch-point physicality flagged as the real issue (58.3% contested) plus a static 80/80 X role, only four in-space catches all season, and a Kyler Murray height/sight-line concern — Harmon admits he should not have ranked him top-20. Nabers named the highest-ceiling rookie of the class. Odunze defended as an environment/hierarchy victim with 87th-percentile press marks; Harmon now wants him as Chicago's full-time X with D.J. Moore moved to flanker/slot. Brian Thomas Jr. elevated into the top group on a 93rd-percentile press mark shared with Chase, Jefferson, Lamb, Hill and Beckham.

## [2025-05-15] ingest | Matt Waldman's RSP Cast — 2025 Fantasy Rookie Draft Day Values & A Peek at 2026: Going Deep with Brandon Angelo and Matt Waldman
Rookie-draft value episode: Luther Burden III becomes Waldman's top rookie value outside Ashton Jeanty (board 102 vs ~206 ADP) and both hosts hand him the Amon-Ra St. Brown role in Ben Johnson's offense — D.J. Moore's Bears role called finished on effort grounds. Harold Fannin Jr. jumps to a late-first 1.5-PPR tight end ahead of Tyler Warren and Colston Loveland, with Terrance Ferguson faded as a low-end linear athlete into 'Higbee syndrome'. Angelo's Rashee Rice concern reframed: not whether the knee looks good in September but whether KC affords him bandwidth to survive volume/contact/fatigue by week 10, with Kirk Cousins 2024 as the completed case. New value flags on Kyle Williams, Pat Bryant, Jaylin Noel, Tahj Brooks, Jaydon Blue, Savion Williams, Jalen Royals and Jacory Croskey-Merritt; Matthew Golden downgraded to a Brandin Cooks horizontal profile. First 2026 pages created: LaNorris Sellers (Angelo's QB1), Cade Klubnik, John Mateer, Eli Stowers, KC Concepcion, Jordyn Tyson, Antonio Williams, plus Nyck Harbor and Evan Stewart on the do-not-draft list. Two new concepts: Year Two Value and Vacating Veterans, and Usage as Evidence of Ability (Waldman's counter to Steve Smith's usage heuristic).

## [2025-05-16] ingest | Reception Perception: The Show — Second-Year Receivers Breakdown Continued
McConkey moved up materially — Harmon says 'you're not high enough' after a 98th-percentile 84.4% press success rate and better outside than slot YPRR, pushing him toward top-10 league receiver and above his own Tyler Lockett comp. Legette's headline flipped negative: 17th-percentile vs press, contested-catch rate down from 81.8% as a prospect to 60% with a 13.5% drop rate, with the cause diagnosed as being pinned at X after the Diontae Johnson trade — Tetairoa McMillan taking the X job is the stated fix, and Harmon and Koh disagree on whether coaching or scheme is the answer. Pearsall upgraded on a first-four vs last-four split (57.1% to 75% vs press) plus Kupp-type option/outbreaking usage; both hosts call him a round-11 bargain over Jennings and a rehabbing Aiyuk. Tre Harris slotted on the straight-line X ladder between Alec Pierce and DK Metcalf. Deebo Samuel's 2024 man success rate is the third-lowest Harmon has ever charted.

## [2025-05-19] ingest | Matt Waldman's RSP Cast — Feel It or F–It 5.19.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's 2025 ADP stances land: Brock Purdy re-rated as a top-10/12 quarterback after the $265M extension (buy after QB7) with Dak Prescott at QB16 as the paired value; George Kittle called the value of the elite TE tier on a tight-end aging argument; Dallas backfield preference flips to Jaydon Blue over Javonte Williams on offensive-line risk, with Blue vs Bhayshul Tuten split ~50/50 as best-ball darts; George Pickens installed as Dallas's true X (915 yards projected) without cutting CeeDee Lamb's projected 176 targets; Derrick Henry backed for another top-five season at 31-32 post-extension; Miami's offense flagged as systematically underpriced (Tua QB22, Jonnu Smith TE17 after a TE4 finish); Brandon Aiyuk downgraded to a wait-for-clarity avoid with recovery possibly taking all year, pushing Jauan Jennings and Ricky Pearsall up. New pages: Jaydon Blue.

## [2025-05-20] ingest | Matt Waldman's RSP Cast — 2025 Fantasy Drafts with JJ Zachariason
Zachariason's 2024 RB health finding (top-24 healthiest in ~15 years) sets up an expected 2025 RB ADP overcorrection; Goff flagged as the pocket-passer-trap fade with Purdy as 'discount Burrow'; Davante Adams elevated to WR10-11 on Rams target concentration; Waddle rehabilitated as a 2024 outlier; Fannin Jr. called a can't-lose dynasty buy post-Combine fade; Odunze reframed as a possible falling knife (traded for the 1.08) while Waldman still projects 100+ targets; Nacua carries an elevated injury-risk flag from Angelo. New concept pages for directional correctness, ambiguous backfields and RB health regression.

## [2025-05-21] ingest | Reception Perception: The Show — Chris Olave Future & 2nd-Year Receivers Continued
Harmon's second-year charting continues: [[Jalen Coker]] elevated to his single deepest sleeper in the league (70%+ man/press success as a UDFA, 88% slant rate, [[Jakobi Meyers]] comp) and judged to have outplayed [[Xavier Legette]]; [[Keon Coleman]] cratered — non-separating X with a 60% contested rate, best-case comps [[Romeo Doubs]] and Devante Parker, big-slot conversion only a theory; [[Xavier Worthy]] repositioned as a horizontal quick-game weapon who Harmon still ranks behind [[Rashee Rice]] in Kansas City; [[Chris Olave]] defended as underrated (12th in YPRR since 2022) and not worth a second-round pick to New Orleans despite concussions and Pittsburgh trade interest.

## [2025-05-23] ingest | Reception Perception: The Show — These 2024 Rookies Took a Ride on the Struggle Bus
Harmon concedes a major evaluation miss on Ja'Lynn Polk — contested catch rate 80%+ to 20%, drop rate 10.7%, worst blocker charted in the class, and buried behind Diggs/Hollins/Douglas/Kyle Williams; Harmon would already take rookie Kyle Williams over him. Adonai Mitchell graded the most extreme pure-X profile Harmon has charted (90%+ slants/outs, 14th-percentile vs zone, down on first contact 100% of the time) and is unlikely to fully displace Alec Pierce before year three. Jalen McMillan's championship-winning TD finish reframed as Liam Coen scheme, not separation — capped as a future WR3 behind Emeka Egbuka. Harmon also retracts his 'worse than a sacrificial X' line on Pierce.

## [2025-05-26] ingest | Matt Waldman's RSP Cast — Feel It or F–It 5.26.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman fades the 'historic season premium' — takes [[Jalen Hurts]] over [[Jayden Daniels]] at QB3 and passes on [[Brock Bowers]]; expects a year-two pressure test for Daniels. Detroit coordinator change judged non-fatal: [[Amon-Ra St. Brown]] and [[Jahmyr Gibbs]] fine, [[David Montgomery]] a value at RB24, [[Sam LaPorta]]'s second half the real baseline, [[Jameson Williams]] still a field-stretching WR4. [[Isaac TeSlaa]] cratered — bad fit, 4th/5th option, fails the Claypool-Golladay test, though a dynasty like. [[Tetairoa McMillan]] fade at WR22 (prefers Hunter, D.J. Moore, Adams). [[Deebo Samuel]] framed as a Kingsbury catch-and-run fit that frees [[Terry McLaurin]] rather than a WR1. [[Nick Chubb]] projected as a midseason injury replacement, [[J.K. Dobbins]] a late-preseason Bears signing. New page: [[Efton Chism III]] (Patriots UDFA, Edelman comp called hype).

## [2025-05-28] ingest | Reception Perception: The Show — WR Free Agent Team Matches & Team Needs, Sleepers
Harmon's alignment survey moved several headline views: Rashad Bateman flagged at a near-league-low 7.7% slot rate on 444 routes and argued to be misused; Jaylen Waddle's decline reframed as role (Miami's de facto X, no layups) rather than ability; Tre Tucker exposed as a 639-route sacrificial X with 23 slot snaps; Malik Nabers pushed toward a 35% slot rate for posts/digs; Jerry Jeudy's 2024 usage fix (34.6% slot, down from 75/49/54%) endorsed as permanent; Allen Lazard called a non-NFL player without Rodgers; Malachi Corley judged likely sunk as an overdrafted created-touches player; Harmon high on Jameson Williams for 2025 while Koh fears the Ben Johnson-to-John Morton drop-off. Amari Cooper, Keenan Allen and Gabe Davis all still unsigned on May 27 with landing-spot fits proposed.

## [2025-05-30] ingest | Reception Perception: The Show — Dynasty Wide Receiver Rankings!
Harmon's dynasty WR board: [[Puka Nacua]] leads tier two and is being eyed for tier one after year-two charting (led NFL in YPRR, first downs, successful plays and targets per route run); [[A.J. Brown]] dropped to tier three on age-28 plus low Eagles passing volume despite tier-one NFL talent; [[Tyreek Hill]] marked a sell at tier five ('no thanks') on decline and off-field issues; [[Diontae Johnson]] effectively written off after a vet-minimum Browns deal and skipped OTAs; [[Jayden Reed]] held off-consensus high on talent but capped by a ~62% snap share, with an explicit threat to drop him a tier at midseason; [[Travis Hunter]] unusually high for a rookie at tier three; new pages for [[Jordan Whittington]] and [[Terrance Ferguson]] as Rams sleepers.

## [2025-06-02] ingest | Matt Waldman's RSP Cast — Feel It or F–It 6.2.25: An RSP Cast with Bob Harris and Matt Waldman
Texans pass-catcher and backfield hierarchy set: Waldman puts Nico Collins 8th-9th on his board with a ~140-target/1,400-yard/10-TD projection, calls Christian Kirk a great pick at WR60 ADP, and ranks Jayden Higgins clearly over Jaylin Noel in dynasty and redraft. Joe Mixon age/carry concerns dismissed outright (~1,400 yards, 14 TD at RB16). Treylon Burks moved to an outright dynasty sell — Waldman doesn't expect him on the roster all year. Marvin Harrison Jr. downgraded to a boom/bust big-play archetype with a sub-60% catch rate, not a year-two leap; Larry Fitzgerald's mentorship comments called lip service. Kyler Murray held at QB13-14 versus a QB9 ADP on the unrepaired knee. Stefon Diggs faded on the ACL rather than the off-field noise. Jayden Daniels' production endorsed but the QB3 price rejected. Waldman takes Aaron Rodgers over Kirk Cousins for Pittsburgh's QB1.

## [2025-06-04] ingest | Reception Perception: The Show — Running Through the Early Camp Reports!
Pearsall hamstring — out until training camp, Harmon calls the market reaction overdone but Koh flags the complex-offense risk. New page for Jordan Watkins (SF 4th-rounder, spiky production) as the possible Pearsall fill-in. Diggs release chatter contradicted by national reporting; Harmon expects him to stay as a veteran stabilizer. Arizona hinting at moving Marvin Harrison Jr. off the line, raising Michael Wilson to a year-three sleeper. Christian Watson ahead of ACL schedule, putting Romeo Doubs and Dontayvion Wicks on the trade block. Raiders 'remain amorphous' plan backed by Bowers/Meyers wide-alignment charting, with Dont'e Thornton Jr. as the needed lid lifter and Tre Tucker written off.

## [2025-06-05] ingest | Matt Waldman's RSP Cast — Pickens in Dallas, An RB and QB Rotting on the Vine, and Potential Late-Round WR Gems: Going Deep with Brandon Angelo and Matt Waldman
Breece Hall downgraded hard — Waldman has a top-five NFL talent outside his own top 15–20 in a two-back Jets system with a weak line and a non-check-down QB; recast as a dynasty buy-low on an exit. D.J. Moore's stock cut in Chicago (Burden/Loveland picks read as Ben Johnson moving on; Angelo would swap Moore plus a pick for Hall). George Pickens repositioned as a Dallas WR2 freed from top corners. Justin Herbert capped by the Harbaugh/Roman run-first scheme, with Tre Harris faded year one and Quentin Johnston defended as a slot fit. New pages: Jimmy Horn Jr.; Kyle Williams, Konata Mumpfield, Isaiah Neyor and Mason Taylor given real evaluative takes.

## [2025-06-06] ingest | Reception Perception: The Show — Amon-Ra Injury, Colts QB Situation & Over/Unders!
Colts pass-catcher hierarchy reordered — Harmon puts Josh Downs above Michael Pittman Jr. as the likely team leader in catches and yards and goes under 80/950/5.5 on Pittman; Anthony Richardson flagged with a flare-up in the same shoulder he had surgery on in 2023 and Daniel Jones named the likely Week 1 starter, with rookie Riley Leonard a live dark horse. Alec Pierce's 22.3 YPR reframed as Richardson-specific and unlikely to repeat. Amon-Ra St. Brown's knee cleanup discounted as a non-event. Rashad Bateman's 3yr/$37M extension endorsed (over 50 rec, over 6.5 TD, under on repeating 16.8 YPR). George Pickens projected for a touchdown spike in Dallas. New pages: Training Camp Report Skepticism bullet and Quarterback-Receiver Chemistry bullet on charting-vs-quarterback-willingness.

## [2025-06-09] ingest | Matt Waldman's RSP Cast — Feel It or F–It 6.9.25: An RSP Cast with Bob Harris and Matt Waldman
Rodgers-to-Pittsburgh resolved: Waldman lifts [[Pat Freiermuth]] to a projected top-12 TE with double-digit TD upside and calls [[Calvin Austin III]] a WR3 with WR2 upside, while capping [[DK Metcalf]] as a mid-WR2 (route-running limits, sub-60% catch rate when Seattle moved him around). Kansas City: fades [[Rashee Rice]] at WR20 on limb-durability grounds relayed from [[Brandon Angelo]] and makes [[Xavier Worthy]] the KC pick at WR24 with a projected team-leading ~1,100 yards. Jacksonville backfield split — [[Travis Etienne Jr.]] the buy at RB38, [[Bhayshul Tuten]] faded on ball security, [[Tank Bigsby]] 'on his way out'. [[Travis Hunter]] a buy at WR29 despite two-way usage ambiguity; [[Parker Washington]] flagged as a contested-catch sleeper. New fades: [[Tetairoa McMillan]] at WR24 redraft and [[Marquise Brown]] at WR58; new buys: [[Isiah Pacheco]] at RB29 and [[Sam Darnold]] at QB28.

## [2025-06-11] ingest | Reception Perception: The Show — Breaking Down a Couple of Stars Looking To Go Super
Harmon promotes Puka Nacua into his six-man tier-one of NFL receivers (6th, behind Chase/Jefferson/Lamb/Brown/Collins) on a year-two profile showing 80.5% vs press and a contested-catch jump from ~64% to 80%+ — vertical game the lone weakness. Jaxon Smith-Njigba's 2024 breakout validated (WR10, 4.96 YPRR vs man from Week 10 on) and Harmon's concern about a move outside behind Cooper Kupp is 'close to zero'; Kupp reframed as near slot-exclusive. New concept page on condensed formations blurring slot/outside roles.

## [2025-06-13] ingest | Reception Perception: The Show — An Underused Receiver & an Underrated Receiver
Josh Downs re-rated sharply upward — Harmon calls him possibly the most underrated WR in the NFL, 90th pct vs man / 92nd vs zone (top-30 all time), Tyler Lockett comp, 8th in first downs per route run out wide; only knock is tackle-breaking. Jayden Reed's profile reframed: not a gadget receiver (22% post-route rate, 2nd highest in RP history; 2nd in NFL post-route yards) but flat year-one-to-year-two success rates and a 12.8% drop rate, and Harmon walked back his in-season dynasty ranking boost. Both capped by near-zero snaps in one/two-WR sets (Reed 7 routes, Downs 16 over two seasons). Adonai Mitchell downgraded to X-only developmental piece with a 2026 breakout window; Alec Pierce cast as the sacrificial X; Daniel Jones named the Colts' likely full-season starter.

## [2025-06-16] ingest | Matt Waldman's RSP Cast — Feel It or F–It 6.16.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's overall RB1 is Christian McCaffrey with the Achilles apparently behind him; he takes Bijan Robinson at 3 over Saquon Barkley at 2 on workload security, reading the A.J. Dillon signing as deliberate volume relief in Philadelphia. Ashton Jeanty's top-10 ADP called premature (Lynch/Reggie Bush blend, ~230 carries) with a real Mostert timeshare. J.K. Dobbins established as Denver's legitimate 1A over RJ Harvey but expected to stay mispriced as an RB3; Joe Mixon's lingering walking boot opens an even-split scenario with Nick Chubb in Houston. DeAndre Swift moved up to RB24 after the feared Chicago RB addition never came, with rookie Kyle Monangai at RB32. Jauan Jennings flagged as a WR37 steal over Ricky Pearsall. New pages for the Raiders dynasty darts and the Chip Kelly coaching-fit argument.

## [2025-06-23] ingest | Matt Waldman's RSP Cast — Feel It or F–It 6.23.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman reversed his own post-draft bump on RJ Harvey back to his pre-draft placement now that J.K. Dobbins is Denver's clear No. 1. Travis Kelce called a bargain and possible top-five TE on ~800-900 yards / 8-10 TDs after weight loss; DeAndre Hopkins backed for 8-12 TDs against the Footballguys pecking order. Joe Mixon's camp availability in doubt, making Nick Chubb a post-round-12 flier. Tyjae Spears' three-way-split talk rejected. Dont'e Thornton Jr. capped as a post-round-15 pick only. New pages: Cole Kmet (deep-league depth, never a matchup threat) and the concept Off-Script Play Creation and Pocket Climbing, which frames the Kyler Murray / Baker Mayfield critique.

## [2025-06-25] ingest | Reception Perception: The Show — Quarterback Check-In With Cory Kinnan
Reception Perception QB check-in reframes four receiver situations: Harmon's new charting has DK Metcalf at a career-worst 10th-percentile success rate vs zone and warns the Rodgers timing/rapport requirement may not survive the pairing (Kinnan: floor is low, nine-to-ten win team). Garrett Wilson graded elite anyway (77.6% man / 78.6% press) in an offense where 47.9% of his routes were go-or-slant — Harmon expects Engstrand to lower his degree of difficulty even though neither host trusts Justin Fields' post-snap eyes. Colts framed as 'Minshew minimum' with Daniel Jones presumed week-one starter and Anthony Richardson's back pain confirmed chronic — Kinnan says it's now or never in Indy and predicts an eventual Vikings landing. Bryce Young moved from non-functional to functional: best middle-of-field short QB per Harmon, but still can't drive the ball; Jalen Coker named Kinnan's favorite deep sleeper league-wide, blocked by Thielen; Legette written down to manufactured-touch-only.

## [2025-06-27] ingest | Reception Perception: The Show — Young Receiver Rooms w/ Matt Waldman!
Luther Burden III materially upgraded — Waldman would have slotted him near Brian Thomas Jr. in the 2024 class and projects ~120 targets, rejecting the gadget label; Harmon's charting shows the lowest man-coverage rate he has ever charted but 90.9% success on outs. Chicago reframed as a near-even three-way split (Moore's 2024 blamed on an out-of-position split end role; Odunze capped at ~100 targets as X, Harmon disagreeing and staying most bullish). Ladd McConkey elevated to 98th-percentile-vs-press, 100-120 catch upside, with a new injury-mechanics caveat from Brandon Angelo about how he falls. Marvin Mims Jr. charted as a near-pure gadget (24.4% screen rate, 30.7% backfield alignment, 6th-lowest man success). Dontayvion Wicks downgraded — 2nd-highest drop rate in RP history, weak vs zone, fighting for WR3. New concept page: Rising Receiver Skill Baseline and Analyst Granularity.

## [2025-06-30] ingest | Matt Waldman's RSP Cast — Feel It or F–It 6.30.25: An RSP Cast with Bob Harris and Matt Waldman
Jonnu Smith traded to Pittsburgh mid-recording — Waldman recut the Steelers and Dolphins pass games: Freiermuth capped at 60-70 targets in a two-TE Arthur Smith split, Calvin Austin/Robert Woods/Roman Wilson faded (Bob Harris dissenting on Austin), and Malik Washington promoted as Waldman's new favorite late flier. Bucky Irving downgraded as overpriced with red-zone TDs judged scheme-aided and Sean Tucker named the value; Dyami Brown demoted to Jacksonville's fifth option; Isaiah Neyor added as an active dynasty buy off a would-have-been top-12 RSP grade; J.J. McCarthy moved up toward top-12 QB (Bob Harris says reachy); Mahomes decline narrative rejected; Saquon volume trimmed but still ~1,800 yards/15 TDs.

## [2025-07-07] ingest | Matt Waldman's RSP Cast — Feel It or F–It 7.7.25: An RSP Cast with Bob Harris and Matt Waldman
Waldman's late-round board firms up: Sean Tucker (RB82) named the back he won't leave a draft without and Jacory Croskey-Merritt (RB81) a must-have stash; Harold Fannin Jr. upgraded from an Isaiah Likely one-week wonder to a possible LaPorta-like slot option, with Njoku capped near TE5 as a linear athlete. Tyler Lockett revalued upward as a real threat for the Titans' target lead (Harris still has Ridley WR1). A.J. Dillon reframed as the closeout back who caps Will Shipley, whose price has risen past Harris's interest. Post-trade Steelers: Freiermuth projected 50/550/8-10 TDs, Calvin Austin III held at WR3 value. Jermaine Burton's maturity 180 restores dynasty interest. Hosts split on the Raiders backfield — Waldman believes Carroll's split talk, Harris does not.

## [2025-07-09] ingest | Reception Perception: The Show — Breaking Down George Pickens & Garrett Wilson!
Harmon's charting flips George Pickens' 2024 from a down year to a career best (career-high 72.8% vs man, 77.6% vs press) and makes him a bullish Dallas X and Tee Higgins comp, with 19th-percentile zone and loafing as the standing caveats. Garrett Wilson graded 94th percentile vs man with a first-ever 70% contested catch rate; Harmon blames the Jets' nine/slant tree (dig rate 17.8% as rookie to 7.5%, slot 33% to 20.5%) and names OC Tanner Engstrand a bigger year-four lever than Justin Fields. New concept context on RP benchmarks (70/80/75) and Detroit vs Jets formation width.

## [2025-07-10] ingest | Matt Waldman's RSP Cast — Going Deep with Brandon Angelo and Matt Waldman: Training Camp Narratives, Overwrought ADPs, Either/Or Options
Joe Mixon downgraded hard — Angelo reads the July boot as post-season ankle ligament surgery and puts him on a do-not-draft list at RB1 cost, with Nick Chubb elevated as the cheap 15th-round beneficiary. Colston Loveland's grade-three AC joint dislocation reframed as a ramp to midseason, making Mason Taylor the better short-term rookie TE. Tyreek Hill named the top-30 ADP fade (comped to Calvin Ridley) and Bucky Irving faded on unsustainable 5.4 YPC plus Wirfs' PUP risk. New role calls: Sean Tucker as a must-have late-round back on Licht/Bowles drumbeats and Rachaad White's exit signal, Damien Martinez as an off-ADP Seattle stash, Xavier Restrepo as Angelo's likely Titans slot starter by midseason, and Waldman's contrarian red-zone touchdown case for DeAndre Hopkins in Baltimore. Names normalized from ASR: Kyle Monangai, Dont'e Thornton Jr., Isaiah Neyor, Rome Odunze, Cole Kmet, Deebo Samuel, Pat Freiermuth, Dameon Pierce, Bhayshul Tuten, Breece Hall, Chigoziem Okonkwo, Kyren Williams, LeQuint Allen, Xavier Restrepo.

## [2025-07-11] ingest | Reception Perception: The Show — Breaking Down Jameson Williams, Drake London & Dontayvion Wicks
Harmon reverses on Dontayvion Wicks — every charting split declined in year two, contested catch rate 71.4% to 25%, 15.4% drop rate (2nd in RP history); now an ideal WR4, not a breakout. Drake London elevated to top-10 WR on an 87th-percentile press score, record 27% dig usage and a slot-heavy Zac Robinson role; Harmon floats him leading the NFL in targets. Jameson Williams capped as a very good WR2 (65.7% vs man, still under the 70% threshold) and flagged as a major regression candidate post-Ben Johnson, with Sam LaPorta the likely beneficiary. New pages for Isaac TeSlaa (possible Detroit sacrificial X) and Michael Penix Jr.

## [2025-07-16] ingest | Reception Perception: The Show — Latest NFL News & Profile Breakdowns
Harmon's charting moves three profiles: Quentin Johnston upgraded from unplayable to a fine WR3 on tripled in-space usage (hands still bad, 11.9% drops); Marvin Mims Jr. reframed as a record-setting manufactured-touch role player (RP-record 30.7% backfield snaps, first-percentile vs man) with the college separation not translating; Cedric Tillman flagged as an underpriced startable X outside WR60. Deebo Samuel cratered — fourth-worst man-coverage success rate Harmon has ever charted. Terry McLaurin contract standoff and the leaguewide second-round holdout (Tre Harris, Luther Burden III) added as rep-loss risks; new concept page for the holdout.

## [2025-07-18] ingest | Reception Perception: The Show — A Surprise Retirement, Legal Updates & 2 Profile Breakdowns!
Mike Williams retires, gutting the Chargers' X spot and putting Quentin Johnston back at risk of the role while Tre Harris holds out. Jordan Addison pled guilty to a lesser DUI (1-3 game projection) and Rashee Rice was sentenced (5-7 game projection), reshaping the Vikings and Chiefs target trees; Harmon flags Jalen Royals as the Rice-comp beneficiary and denies Xavier Worthy can play Rice's role. Chris Olave becomes Harmon's headline buy — 84% dig success at 20% participation, top-15 in every per-route efficiency metric, cheap outside the top 50. Khalil Shakir charted as a near-optimally used slot with a ~110-target ceiling. Harmon now waffling between Jefferson and CeeDee Lamb at WR2.

## [2025-07-21] ingest | Matt Waldman's RSP Cast — Feel It or F–It 7.21.25: An RSP Cast with Bob Harris and Matt Waldman
Judkins arrest reshuffles the Cleveland backfield — Waldman keeps him as a discounted back-end starter but says single-league drafters should pass; Ford (up 33 ADP spots) becomes the likely early-season lead back and Sampson (up 38) gets a bump Waldman calls overdone. Waldman fades Omarion Hampton at RB16 and defends Najee Harris (eye injury read as superficial). Arroyo capped at TE15-20 redraft despite Fant's release; Barner keeps the underneath role. Diggs and Rice both downgraded on weekly-punishment rehab risk (Rice held at WR66, suspension pending). Savion Williams named the dynasty sleeper; Breece Hall a dynasty buy-low. Jayden Daniels drops out of Waldman's top five if McLaurin is traded. Garrett Wilson's extension panned on a blunt Justin Fields verdict. New pages: Noah Fant, Justyn Ross.

## [2025-07-23] ingest | Reception Perception: The Show — NFC West WR Division Preview
Aging tells sharpened: Davante Adams flagged as genuinely declining (zone success 84.4%→77%, 37th pct) with the Allen Robinson precedent, though press/man held and Harmon projects him as the Rams' primary X; Cooper Kupp cratered to slot-only in Seattle (man 75.2%→50.5%, zone→76%) and per Harmon cannot play X at all. Brandon Aiyuk downgraded — multi-ligament knee tear, no timeline, possibly not himself until 2026 — with DeMarcus Robinson's three-game DUI suspension removing the fallback X; Ricky Pearsall elevated to Harmon's best breakout bet conditional on camp reps. Marvin Harrison Jr.'s problem framed as deployment not talent (80.4% snaps on the line, a group of four league-wide) plus Kyler Murray's 3% dig rate at 50% success. Jaxon Smith-Njigba pushed outside as Seattle's alpha; Tory Horton added as a 94th-percentile-vs-press fifth-rounder with a one-side-of-field flag; both hosts killed the Elijah Arroyo X-receiver talk. Matthew Stafford back injury noted, Rams rated 7.5/10 combustible (Harmon) versus Koh's 9/10 for the 49ers.

## [2025-07-25] ingest | Reception Perception: The Show — AFC West WR Division Preview
Harmon's AFC West preview moved several headline views: Ladd McConkey elevated to fringe top-10 NFL WR (98th-pct press, 6th-best in RP history); Xavier Worthy recast as the required vertical winner with a 16th-pct press mark rather than a Rashee Rice slot replacement; Jalen Royals added as Harmon's Rice insurance on a Zachariason data comp; Pat Bryant named Denver's likeliest WR2 as a power slot despite the worst slant success rate Harmon has charted, with Marvin Mims Jr. downgraded to gadget/situational (1st-pct vs man); Jack Bech argued out of the slot-only box (91st-pct vs press) and Tre Tucker written off entirely in Las Vegas; Quentin Johnston reframed with a Jerry Jeudy off-the-line usage comp.

## [2025-07-28] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 7.28.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman reverses on Jacksonville — now sees [[Tank Bigsby]] as the back the team keeps, with three org sources naming him Week 1 starter and [[Travis Etienne Jr.]] a possible trade/cut. [[Travis Hunter]] expectations lowered to scheme/gadget role, sub-900 receiving yards. [[Nick Chubb]] jumps to a live 1,100-yard bet after [[Joe Mixon]] lands on NFI with the foot. [[Anthony Richardson]] installed as Waldman's best ball QB3 at QB29 ADP ('free square'). [[Adonai Mitchell]] drops diagnosed as technique ('clap attack') vs [[Keon Coleman]]'s focus-based drops. [[Dillon Gabriel]] called a mispick, Purdy comp rejected. [[Oronde Gadsden II]] named the one rookie Waldman would admit whiffing on if camp buzz translates. New: [[Kyle Monangai]], [[Isaiah Neyor]], [[Parker Washington]] takes.

## [2025-07-30] ingest | Reception Perception: The Show — NFC South WR Division Preview
Harmon launched RP running back charting: TreVeyon Henderson grades as his worst zone runner but a good man/gap fit in New England, while Omarion Hampton is only average in man/gap and an awkward Chargers scheme fit (Waldman reportedly shares the concern). Chris Olave reframed as underrated — elite man/zone/press rates held through the concussion-hit season — but Tyler Shough's 33.3% dig and 20% post charting is flagged as a poor fit for Olave and Rashid Shaheed. Darnell Mooney's shoulder injury (out several weeks) leaves Atlanta with no second answer and breaks their all-slot motion scheme. Drake London called a possible tier-one graduate. Emeka Egbuka called a possible top rookie receiver with an Amon-Ra St. Brown data comp, with an explicit Rome Odunze-style blocked-by-veterans caveat; Chris Godwin tagged a slow-start candidate after not practicing in team drills.

## [2025-08-01] ingest | Reception Perception: The Show — AFC South WR Division Preview
Harmon graduates Nico Collins into his top five NFL receivers (77.5% vs man, 82.3% vs press, contested catch 75% to 81.3%) and predicts his extreme on-line X usage finally breaks as Jayden Higgins absorbs X snaps. New breakout call: Calvin Ridley as a Terry McLaurin-style QB-driven leap on the Cam Ward route-profile overlay, plus a zillion targets since Tennessee has no other X. Adonai Mitchell narrowed to X-only after a 14th-percentile zone mark when moved. Brian Thomas Jr. one zone-coverage step (38th pct, improving to ~77%) from Harmon's elite 75/80/80 tier; Travis Hunter gets a prime Odell Beckham Jr. comp with two-way usage as the caveat. Jaylin Noel graded a Josh Downs-level steal but blocked on the depth chart. Tyler Lockett written down to a declining slot piece.

## [2025-08-04] ingest | Matt Waldman's RSP Cast — Feel It Or F**k It 8.4.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman rejects the camp-report panic on Omarion Hampton and Nick Chubb, but volunteers his own charting doubt that Hampton is a true breakaway back. Chicago revalued: Caleb Williams backed as a QB12-13 with Ben Johnson, Kyle Monangai flagged as Waldman's single biggest ranking outlier and expected clear No. 2 over Roschon Johnson, Burden and D.J. Moore up / Rome Odunze down on the sacrificial-X role. Pat Freiermuth called a major value — predicted to lead Pittsburgh in TDs with 10+ scores at a TE24 price. Noah Fant cut by Seattle and written off in Cincinnati. Khalil Shakir's high ankle sprain expected to slow him 2-4 games. Waldman and Bob Harris disagree openly on Seattle: committee (Waldman) vs Walker featured role (Harris, citing Greg Bell and Mike Clay's 68%/19% carry split). Jayden Daniels held just outside the top five and would drop out of the top 10 if Terry McLaurin were traded, which Waldman says won't happen. Dillon Gabriel judged not a starting-caliber candidate right now.

## [2025-08-06] ingest | Reception Perception: The Show — AFC East WR Division Preview
Tyreek Hill downgraded on charting decline (75.8% to 67.3% vs man, press under 80% for the first time since 2016) with Harmon betting against a rebound at 31. Jaylen Waddle reframed as a miscast on-line WR2 who needs role catering, not a fallen WR1. Ja'Lynn Polk conceded as a Harmon miss and now a roster long shot, with Kayshon Boutte the likely Patriots X. Khalil Shakir week to week on a high ankle sprain, opening a Bills roster path for Elijah Moore. Keon Coleman locked at X on a third-percentile man score, projected volatile. Justin Fields' benching risk flagged despite QB1 ADP; Garrett Wilson's target-share upside capped by run-heavy comps.

## [2025-08-07] ingest | Matt Waldman's RSP Cast — Weapon RBs, Rookie Risers/Fallers, Young Vets Emerging: Going Deep w/ Brandon Angelo & Matt Waldman
Angelo's weapon-back framework formalized on the concept layer: slot-aligned RBs create spacing and neuter blitzes without gaining targets, with Waldman dissenting on the fantasy implication. Achane downgraded to sacrificial-lamb usage with Waddle the named beneficiary (Angelo predicts Waddle overtakes Hill). Chase Brown's late-2024 touch spike rejected by both hosts; Tahj Brooks projected into cold-weather red-zone work. Rookie risers: Croskey-Merritt (most talented back in Washington's room), Kyle Monangai (threatens Roschon Johnson's goal-line role), Isaac TeSlaa; Tyler Shough the clear faller with the job apparently Rattler's to lose. Rashee Rice's injury reframed as multifactorial LCL-plus-hamstring, with Angelo not expecting true form until the playoffs. Adonai Mitchell a stated Angelo reversal from his pre-draft view. Jayden Daniels falls to the back of Waldman's QB top ten if McLaurin is gone.

## [2025-08-08] ingest | Reception Perception: The Show — NFC East WR Division Preview
Deebo Samuel cratered — 39.7% success rate vs man in 2024, third lowest Harmon has ever charted, with his zone beating also down from mid-80s to 76.3%. George Pickens elevated to Harmon's most-mispriced-player pick on a career-best 72.8% vs man. Terry McLaurin's holdout plus a 72.3% left-outside alignment rate flagged as a structural cap and possible aging signal. Malik Nabers carries a mysterious toe injury and a camp shoulder issue; Harmon ranks him ~WR8-9 while co-host James Koh keeps him outside the top 10 and calls the Giants a bottom-five room. DeVonta Smith's slot rate jumped to 46% with 95th-percentile man success. New pages: Jaylin Lane.

## [2025-08-11] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 8.11.2025: An RSP Podcast with Dave Kluge and Matt Waldman
Chargers backfield reframed — Waldman's ophthalmology-informed read has Omarion Hampton back by week 1-2, Kluge moving him to top of round 3, while Waldman holds a 50-50 split and calls the round-11 fall of Najee Harris an overcorrection; Rashawn Slater's injury shaves 10-15% off Chargers rushing projections. Harold Fannin Jr. jumped to a genuine late-round target after being deployed as a full-time slot receiver (six snaps, four different routes) — Njoku contrasted as a linear athlete. T.J. Hockenson cratered on zero first-team targets with J.J. McCarthy, who Waldman may drop again on conflicting Minnesota camp reports. Keenan Allen called badly mispriced at rounds 12-14 (27.2% target share, reunion with Herbert). Kyle Monangai named Waldman's top-25/30 outlier over Roschon Johnson. Kluge reversed his old top-five view of Kyler Murray. New concept-layer material on why QB-turned-analysts aren't definitive on film.

## [2025-08-13] ingest | Harris Fantasy Football Podcast — ADP Surprises For 2025 & Brock Bowers Profile
Harris publishes his VBD case against early tight ends (4 of 24 first-three-round TEs beat ADP in a decade, none from round one) and applies it to Brock Bowers — great player, wrong price. James Cook's hold-in ends with $30M guaranteed and Harris expects his ADP back inside round two. New concept pages for value-based drafting at tight end and the flattened late-round quarterback market. Guest Dave Kluge flags Alvin Kamara (RB17 too low), Travis Hunter (first-team offense only in preseason), Demario Douglas (100+ target projection at WR70) and Keenan Allen as mispriced; Harris fades De'Von Achane, Ashton Jeanty and Garrett Wilson relative to market and calls Omarion Hampton in round four his biggest surprise.

## [2025-08-13] ingest | Reception Perception: The Show — AFC North WR Division Preview
Reception Perception AFC North preview. Ja'Marr Chase's career-high 32.3% slot rate and doubled motion usage documented as the cause of the 17/17 season. Jerry Jeudy downgraded — league-leading 712 routes called unrepeatable, Harmon prefers undrafted Cedric Tillman (Gallup floor, Courtland Sutton ceiling) at cost. DK Metcalf logged his worst charted season (career-low 69.2% vs man, 40% contested); Harmon expects slant/go spikes with Rodgers, not consistency. Pittsburgh named the worst WR cast in the NFL. Rashad Bateman is Harmon's favorite division bet (77.8% first-down/TD rate, 7.7% slot). Zay Flowers held at high-end WR2 pending contested-catch improvement. Hosts split on Mark Andrews: Koh says done, Harmon says declining but not finished. New pages: Jermaine Burton, Roman Wilson, Diontae Johnson update.

## [2025-08-14] ingest | Harris Fantasy Football Podcast — Flag Players 10 Thru 6 & Offenses We Might Be Wrong About
Harris revealed 2025 flag players 10-6: Jaylen Wright (15th-rd Achane hedge), Michael Pittman Jr. (10th-rd, 'punishment beyond punishment'), Justin Herbert (10th-rd, rejects the too-run-heavy narrative), Tank Bigsby (11th-rd, better tape than Etienne), and Joe Mixon for a record fifth time (ADP 71 despite RB9/game — buy in the sixth unless surgery news drops). Big movers elsewhere: Matthew Stafford's back flagged as unpriced risk under Puka Nacua and Davante Adams, with a stated Labor Day practice-status decision point; De'Von Achane downgraded on checkdown-dependent production at an early-2nd price; Jaydon Blue panned off Texas tape while Javonte Williams gets a quiet Cowboys-lead-back case; Bloom vs Harris disagreement recorded on Dak Prescott, George Pickens, Jordan Mason and where to draft Justin Jefferson. Normalized ASR garbles including Jalen Wright, Alexander Madison, Bashul Tootin, Caleb Johnson, Roma Dunze, Javante Williams, Sigmund Blum.

## [2025-08-15] ingest | Harris Fantasy Football Podcast — Flag Players 5 Thru 1 & Frag Players For 2025
Godwin cratered outside the top 40 WR on a PUP leak (misses four games); Rashee Rice lowered to WR32 with suspension now expected mid-season, not Week 1; TreVeyon Henderson raised to RB28 on joint-practice speed reports, ahead of Rhamondre Stevenson; Josh Downs hamstring flagged for a further drop; Judkins battery charge dismissed, Browns signing expected. Harris's flag list closed with Addison, Hubbard (RB14 vs RB18 ADP), Pearsall, Smith-Njigba and Josh Jacobs at #1 — with the twist of ranking Jacobs in the first but telling drafters to wait until the second. Cousin Josh's frag list: Swift, Worthy, Kaleb Johnson, Mayfield and Brock Bowers at #1, plus a reversal off last year's #1 frag Kyren Williams, whom he is now bullish on.

## [2025-08-15] ingest | Reception Perception: The Show — NFC North WR Division Preview
Harmon's NFC North preview moves several headline views: Amon-Ra St. Brown gets his strongest conviction of the series (over 1,075.5 yards, 1,231 projection, 51% outside alignment, four straight years of improving man/press marks); Rome Odunze is named Chicago's most productive receiver on the strength of an 87th-percentile press rate and a settled X role, with D.J. Moore projected down toward ~900 on a hierarchy shift; Matthew Golden is flagged as a top ADP value while being graded a very good No. 2 rather than a true No. 1, with a real drop history. Injury/role shifts: Jayden Reed in a boot with Week 1 in doubt, Christian Watson likely PUP, Jordan Addison suspended three games (T.J. Hockenson elevated as a PPR target hog), Rondale Moore out for the season opening a lane for Tai Felton. Jameson Williams downgraded to a lean-under with Ben Johnson gone. Harmon publicly walks back the sacrificial-X framing as an industry over-correction.

## [2025-08-15] ingest | Matt Waldman's RSP Cast — What You Didn't Know about NFL Training Camp and the Preseason: RSP Scout Talk with Matt Waldman and Dan Hatman
Waldman + Dan Hatman (Scouting Academy, untracked guest) on camp/preseason evidence quality. Kyle Williams downgraded from minicamp darling to dropping passes and fading, on the Romeo Doubs curve; Luther Burden held despite Olamide Zaccheaus running with the ones, with Waldman reading Zaccheaus as a versatile placeholder; Kyle Monangai gains Ben Johnson's stated pass-pro trust and may take Roschon Johnson's goal-line work; Tomlin publicly wants Kaleb Johnson to think less. New concepts: Draft Capital Rep Allocation Bias, Rookie On-Ramp and Development Runway, Positional Versatility and Roster Redundancy, Speed of Instinct and Overthinking, Playing Experience and Evaluation Blind Spots. New 2026 RB prospect pages: DeMond Claiborne, Kaytron Allen, Noah Whittington; Isaac Brown now ranked above Bucky Irving by Waldman.

## [2025-08-18] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 8.18.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman defended [[Nick Chubb]] as a de facto Texans starter for 3-4 weeks with [[Joe Mixon]] hurt, arguing camp reporting cannot see subtle power backs. [[Jackson Dart]] held behind [[Russell Wilson]] on sub-25-yard accuracy, with a projected weeks 5-7 takeover if the Giants lose. [[Breece Hall]] moved to an emphatic dynasty buy-low after the revelation he played 2024 through a knee injury; [[Isaiah Bond]] became a dynasty buy over [[Jack Bech]] and [[Tre Harris]] after his no-bill and Browns signing; [[Quinshon Judkins]] endorsed as the best Cleveland back at an RB39 price. New pages: [[Jimmy Garoppolo]]. [[Luther Burden III]] trimmed 10-15 targets as [[Olamide Zaccheaus]] is expected to open ahead of him, and [[Rome Odunze]] capped at ~120 targets against a 140 consensus. [[Troy Franklin]] rising on blocking-earned snaps; [[Tory Horton]] framed as a best ball dart, not a Seattle starter; [[Trey Lance]] a deep dynasty stash; [[Matthew Stafford]]'s back flagged on opaque team messaging.

## [2025-08-18] ingest | Harris Fantasy Football Podcast — Five Busts For 2025
Harris reverses his Joe Mixon flag-player call four days later on a leaked 'not a lock for Week 1' report — RB16 to RB25 std/RB27 PPR. First-ever Mike Evans fade after a decade of buying him: outside his top 24 WRs against a third-round ADP. Bust calls added on Bo Nix, RJ Harvey, Brock Bowers (cost, not talent) and Xavier Worthy (3-of-18 on deep targets); Rotoworld guest Patrick Doherty (untracked) busts James Cook, Tyreek Hill, Baker Mayfield, Garrett Wilson and Kaleb Johnson. Terry McLaurin rank cut coming this week on the holdout; De'Von Achane pulled muscle flagged; Doherty expects a heavy Rashee Rice suspension.

## [2025-08-19] ingest | Harris Fantasy Football Podcast — Previewing The Rookies For 2025
Waldman's mid-August rookie repricing: Tetairoa McMillan cut to sub-800 yards as a zone-only winner who will struggle vs press man (explicit disagreement with Matt Harmon's charting); TreVeyon Henderson's third-round price called a mistake with a Stevenson split; Omarion Hampton projected into a near-even split with a healthy Najee Harris, whose eye injury Waldman argues is a routine hyphema on a 5-6 week timeline; Kaleb Johnson held as a late-sixth fantasy starter against bust calls from two untracked guests; Jacory Croskey-Merritt elevated to top sleeper ('Aaron Jones starter kit') with Chris Harris preferring Ekeler if JCM's price spikes; Luther Burden III backed through a rough August into a three-way Bears split; rookie TE order set as Loveland > Mason Taylor > Tyler Warren.

## [2025-08-20] ingest | Reception Perception: The Show — Daniel Jones Starts, McMillan Hurt & Ranking #2 Receivers
Colts QB change dismissed — Harmon sees no fantasy ceiling for Downs/Pittman/Mitchell under Daniel Jones, and worries RPO targets funnel to Tyler Warren. Jalen McMillan to IR possibly past week nine and Chris Godwin still not jogging, so Emeka Egbuka bumped up in dynasty and redraft as the week one WR2. New number-two receiver ranking: DeVonta Smith 1, Godwin 2, Tee Higgins 3, Jaylen Waddle 4, tier drop to George Pickens, Jameson Williams, Jordan Addison. Pickens and Waddle flagged as buy-lows; Malik Nabers flagged for durability.

## [2025-08-20] ingest | Harris Fantasy Football Podcast — Safe Players To Draft In 2025
Brian Robinson Jr. reportedly on his way out of Washington — Croskey-Merritt and Ekeler bump, Harris awaiting the official transaction before moving ranks. Colts name Daniel Jones over Anthony Richardson; Harris uses it to indict rushing-QB-first analysis and reaffirm Joe Burrow as his only early QB. New high-floor board for 2025: Josh Jacobs named Harris's number one flag player (first-round value at mid-second), Chuba Hubbard a flag player rated early third, Kyren Williams's new contract kills the disposable-back bear case, DeVonta Smith and Zay Flowers both rated a round above market. New concept page High Floor Picks and Draft Risk Balancing.

## [2025-08-21] ingest | Harris Fantasy Football Podcast — Super-Deep Sleepers Part 1
Harris dropped [[Terry McLaurin]] from a third- to a fourth-round pick on holdout conditioning risk and pushed [[Brian Robinson Jr.]] deep in the ranks as a likely cut, moving [[Jacory Croskey-Merritt]] into the top 100. A leak that [[Najee Harris]] will miss Week 1 with possible NFI cratered him outside the top 100 to an 11th-round stash and bumped [[Omarion Hampton]] near the top of round 4 — though Harris cited [[Matt Waldman]]'s prospect skepticism and won't pay a second-round price. He deliberately did NOT move Seattle ([[Kenneth Walker III]] still a top-20 RB, [[Zach Charbonnet]] noise read as coach speak) or Cleveland ([[Quinshon Judkins]] still unsigned). Super-deep sleepers part one added or updated flyer takes on [[Cam Ward]], [[Tahj Brooks]], new page [[DJ Giddens]], [[Efton Chism III]], [[Ollie Gordon II]], [[Jalen Coker]], [[Elic Ayomanor]], [[Jordan James]], [[Roman Wilson]] and [[Adonai Mitchell]].

## [2025-08-22] ingest | Harris Fantasy Football Podcast — Super-Deep Sleepers Part 2 & Preseason Baggy Awards
Harris publicly reversed on Christian McCaffrey as the 1.01 — 36 games missed since 2020 and his 202-pound workload research now argue against, though he still calls a late-1st/early-2nd a live league-winner. Jaylen Wright limped off practice with beat reporters saying it wasn't minor, which would push Ollie Gordon II from super-deep stash to draftable in standard leagues behind an already-dinged De'Von Achane. Joe Mixon repriced from second-rounder to round 6-7 with Week 1 availability doubtful. Darnell Mooney's shoulder has cost him all camp, opening the Falcons X job to Casey Washington with the ones. New page for Keaton Mitchell (third straight super-deep listing, now blocked in pass pro behind Justice Hill). Guest Cousin Josh (untracked) named D.J. Moore biggest trash bag, Garrett Wilson stealth bust, and Davante Adams his 2025 LVP on age/new-team/Stafford risk; Harris confirmed he has not drafted Garrett Wilson in a single draft.

## [2025-08-22] ingest | Reception Perception: The Show — Ted Nguyen & Dr. Deepak Chona Join!
Guest-hosted RP episode (no Matt Harmon takes). Injury analyst Dr. Deepak Chona's model reframes several ADPs: Christian McCaffrey graded 2x average RB injury risk at 29 and priced below his top-12 ADP; Brandon Aiyuk's ACL+MCL pushed to a ~week 6 return with a six-game ramp, trustworthy only from week 12; Chris Godwin's undisclosed second ankle surgery downgraded him to 'anything he gives is a bonus' (~week 8); Puka Nacua and Davante Adams both downgraded on Matthew Stafford's suspected herniated disc; Stefon Diggs optimistic (clean ACL, week one, full trust week 5); Malik Nabers' chronic turf toe called 'pause, not stop'; De'Von Achane still projected to play week one. Ted Nguyen reframed Minnesota as a run-heavy bootleg offense under J.J. McCarthy (Hockenson up, Jefferson/Addison fewer deep looks) and the Raiders' slot logjam as fatal to Jack Bech's rookie year, with Dont'e Thornton Jr. and Tre Tucker starting outside purely as lid-lifters. Ricky Pearsall's stock up sharply on camp and Purdy chemistry; Jauan Jennings absent with a calf amid contract whispers; Amari Cooper possibly out of the league.

## [2025-08-25] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 8.25.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman declared [[Dalton Kincaid]]'s Buffalo career effectively dead on scheme fit (wants an Atlanta/Penix trade) while feeling the WR48 price on [[Keon Coleman]]; [[Terry McLaurin]] signed 3yr/$96M-max but Waldman flags elevated soft-tissue risk from the holdout and still prefers Sutton/D.J. Moore at the price. Hosts split on [[Dont'e Thornton Jr.]] — Bob Harris buys the camp buzz, Waldman calls him a best-ball-only sacrificial X. New pages: [[Chris Rodriguez Jr.]]. [[Mason Taylor]] named Waldman's likeliest rookie TE reception leader over Warren/Loveland; [[Omarion Hampton]] called overpriced at RB14 on an expected even split with [[Najee Harris]]; [[Harold Fannin Jr.]] pushed to the top of waiver watch lists; [[Isaac TeSlaa]] flagged overhyped as a Claypool-Galladay beneficiary type.

## [2025-08-25] ingest | Harris Fantasy Football Podcast — Late-Round Players We Love For 2025
Cutdown-week ranks moves: Terry McLaurin cut to WR18/late-4th and Jauan Jennings down ~a round on contract hold-ins; Brian Robinson Jr. traded to SF and named RB2 behind McCaffrey, becoming a top-100 must-handcuff while Isaac Guerendo cratered to deep flyer; Jaylen Wright week-to-week and off the flag list with Ollie Gordon II raised alongside him. Late-round targets with guest JJ Zachariason (not tracked): Austin Ekeler (Harris #1, ~pick 133), Bhayshul Tuten (JJ #1), Brandon Aiyuk ACL stash, Keenan Allen, Ray Davis, Keon Coleman, Jaydon Blue, Drake Maye, Rashid Shaheed. Jacory Croskey-Merritt ruled ineligible because real drafts have him in the 7th, ahead of ADP.

## [2025-08-26] ingest | Harris Fantasy Football Podcast — Players We Might Be Wrong About!
Joe Mixon to NFI, out 4+ games — cut to ~8th round, with Nick Chubb up to rounds 10-11, Woody Marks into PPR relevance above Dameon Pierce. Terry McLaurin signs, bumped back to WR15 but not to pre-August level (Aiyuk slow-start risk). Tyjae Spears possible IR. Amari Cooper signed by Raiders as a 12th-round dart amid Jakobi Meyers' trade request. Harris names Xavier Worthy his No.1 bust while guest Ben Gretch is back in; opposite-side splits also recorded on Brock Bowers (Harris: only 4 of 24 first-three-round TEs beat ADP on VBD) and Ricky Pearsall (Gretch: 14% TPRR vs Jennings' 26%; Harris paying up, ADP 62-114 by platform). New concept-layer detail on early-TE value-based drafting and on analyst uncertainty.

## [2025-08-27] ingest | Harris Fantasy Football Podcast — Handicapping The NFL In 2025 & Cutdown Day
Brian Robinson Jr. traded to SF and named RB2 behind McCaffrey — Harris makes him a mandatory top-100 CMC handcuff and reverts the 'bathtub on wheels' label, retracting 'better James Conner'; Guerendo pushed out of the handcuff role. Tyler Shough loses the Saints job to Spencer Rattler (Harris: damning for the pick). Aiyuk to PUP, Spears and MarShawn Lloyd to IR, Najee Harris and Isaiah Likely avoid PUP, Godwin avoids an injury designation but Harris does not move him up. Adam Thielen traded back to MIN — Harris drops him, likes Addison's cheaper cost, and moves Jalen Coker up out of super-deep-sleeper range. Harris grades Achane below a second-round fantasy player, calls Pickens overdrafted in the fourth, and sets a hard top-six QB tier.

## [2025-08-27] ingest | Reception Perception: The Show — Plenty of Receiver News & Notable Cuts
Pearsall installed as Harmon's top NFL breakout (100th-pctile vs press over final four games) as the SF room collapsed to injuries/suspensions; Tory Horton moved up boards after the MVS cut opened Seattle's perimeter X job; Amari Cooper charted into clear decline and signed by LV, capping Dont'e Thornton Jr.'s camp hype; Jakobi Meyers trade request leaves Jack Bech blocked; McLaurin signed 3yr/$96M but flagged for holdout slow-start risk via Lamb/Aiyuk data; Diontae Johnson, Malachi Corley and Hunter Renfrow cut, with Renfrow's release clearing the Carolina slot for Jalen Coker. New concept page: Contract Holdout Slow Starts.

## [2025-08-28] ingest | Harris Fantasy Football Podcast — Total Listener Request!
Rashee Rice suspension confirmed at six games served from Week 1, opening a defined window for Xavier Worthy and Marquise Brown. Injury moves: Jayden Reed's foot pushes him to Harris's middle rounds, Jaylen Wright out Week 1 with Jeff Wilson re-signed, Isaiah Likely and Cade Otten vague timelines, Achane's calf called precautionary. New Keenan Allen page stance: top-50 flanker/bye-week piece with Herbert. Bucky Irving split — guest Denny Carter takes him in round two, Harris fears a 55/35 committee with Rachaad White. Harris and Carter disagree on Pearsall vs Egbuka. Kyle Williams downgraded by both after a quiet camp. Five new concept pages: automated draft grades, Category 1 vs 2, legendary upside, same-team stacking, auction nomination.

## [2025-08-29] ingest | Reception Perception: The Show — RP Favorites Gaining Steam & Early Rookie Playing Time
Reception Perception fallout from late-August moves: Thielen trade makes Jalen Coker Carolina's named starting slot (Harmon's 'National Jalen Coker Day') and opens slot work for Legette; Tetairoa McMillan walked into a full-time X with a Marvin Harrison Jr. rookie-role warning; Isaac TeSlaa becomes Detroit WR3 after the Tim Patrick trade, with Koh arguing that hurts Jameson Williams; Malik Washington wins Miami's WR3 job, weakening Harmon's Waddle move-around thesis; Harmon reverses the draft-capital prior on Higgins vs Noel with Xavier Hutchinson ahead of both; Devaughn Vele traded to New Orleans, opening Denver power-slot work for Pat Bryant; Jayden Reed diagnosed with a Jones fracture he plans to play through, pushing Harmon toward Matthew Golden (over 700.5 yards, ~850 projection).

## [2025-08-29] ingest | Harris Fantasy Football Podcast — Risk Factors For The First Three Rounds & Almanac Update!
Joe Mixon placed on the NFI list — out at least four games, cut from flag-player status in the fourth-round range to a round-eight target with the flag kept planted. Christian McCaffrey rated the draft's riskiest pick by Harris (8/10) against guest Jeff Bell's 3. Tyreek Hill drew the exercise's only 10 (Bell, on Harstad's receiver-nosedive model) with Harris at 9. Mike Evans onto Bell's bust list on price and first visible film decline. De'Von Achane framed as needing Miami's offense to stay broken. Harris recanted his 2024 Derrick Henry age-cliff alarm and conceded his Brock Bowers 8 was roster-build risk, not player risk.

## [2025-09-01] ingest | Matt Waldman's RSP Cast — Feel It Or F–It 9.1.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman moved [[Kayshon Boutte]] up his rankings and now expects him to outproduce [[Stefon Diggs]], whose expected volume drops to ~4-6 targets/game. [[Jalen Coker]] out up to six weeks with a quad, which is the only reason [[Hunter Renfrow]] is back in Carolina — Waldman sees no starter value in Renfrow. [[Caleb Williams]] repriced upward to a QB10 against a QB14 ADP under Ben Johnson. Waldman rebutted the 'Goff struggles under pressure' stat with his own splits. Miami backfield thinned to [[Ollie Gordon II]] as the only healthy active back with [[De'Von Achane]] unseen and [[Jaylen Wright]] out to September/October. [[George Holani]] beat out [[Damien Martinez]] in Seattle. New pages: [[Beaux Collins]], [[Payne Durham]].

## [2025-09-02] ingest | Harris Fantasy Football Podcast — My Most Drafted Players & Week 1 Waivers
Harris audits which July camp storylines actually moved the market: TreVeyon Henderson surged to a 4th-round ADP while Rhamondre Stevenson cratered outside the top 100; Colston Loveland climbed all August to ~TE11/12; Cooper Kupp barely held the top 100 despite a healthy camp; Ricky Pearsall never got the expected helium and still went 7th-8th. Week 1 injury flags added for Najee Harris (eye, may play, ranked low), Darnell Mooney, Isaiah Likely (foot surgery, off PUP but unusable), Cade Otton (leg) and Jauan Jennings (calf or contract). Miami's backfield collapsed to Achane plus rookie Ollie Gordon II. New waiver-tier pages for Kyle Monangai, Woody Marks, Chris Rodriguez Jr. and Roman Wilson; Cedric Tillman is the #1 add for both Harris and guest Brandon Funston on the Flacco bump. Harris disputes Jeff Bell's downside-only case on Tyreek Hill, and a sustained talent-vs-volume disagreement with Funston over Xavier Legette and Demario Douglas is filed to Usage as Evidence of Ability.

## [2025-09-03] ingest | Reception Perception: The Show — 2025 NFL Season Bold Predictions!
Reception Perception 2025 bold predictions. New headline stances: Egbuka called for 100 catches and the Bucs reception lead; Bateman projected to outproduce Zay Flowers; JSN top-five receiving yards (Harmon rejects the slot-only framing, cites 4.96 YPRR vs man from Week 10 on); Marvin Harrison Jr. over Trey McBride with 2024's low catch rate blamed on boundary usage; Penix to lead the NFL in passing yards. Koh side: Trevor Lawrence top-five QB, BTJ top-five WR, Pittman career-high 1,200+, Kenneth Walker III top-five scrimmage yards (Harmon says top-three is live), Rome Odunze 1,200+. Jalen Coker to short-term IR days after the Thielen trade — role risk up. Harmon charted the whole Jacksonville backfield: Etienne clearly first, Tuten the outside-zone unknown, Bigsby written off on pass protection. Gabe Davis to the Bills practice squad, called a nothing burger.

## [2025-09-03] ingest | Harris Fantasy Football Podcast — Week 1 Ranks & Snarkbag
Harris and guest Andy Behrens (untracked) make the VBD/scarcity case that Ja'Marr Chase is the wrong 1.01 in redraft despite being right in best ball. Xavier Worthy jumps to Behrens WR15 for Week 1 (vs WR30 season-long) on a ~6-week Rashee Rice runway; Rachaad White back at practice from the groin issue and back inside both hosts' top 40 after a 13th-round ADP; Bhayshul Tuten corrected onto the board at RB19 but still behind a Bigsby/Etienne split; Stefon Diggs cratered on ACL-return and age-33 skepticism (Harris WR42, Behrens WR35, both fine starting zero Patriots); Walker held clearly ahead of Charbonnet against the camp reports; TreVeyon Henderson confirmed as Behrens's flag plant with Patriots-offense downside.

## [2025-09-04] ingest | Harris Fantasy Football Podcast — Preseason Huggy Awards & Previewing DALvPHI
Jauan Jennings' hold-in resolved ($3M added for 2025) and he is active Week 1, but Harris warns of an Aiyuk-style usage ramp and ranked him accordingly; same slow-start risk flagged for Terry McLaurin, whose August hold-in cost draft stock. Harris cooled on Ricky Pearsall after a beat report questioned the No. 1 role, calling the hipster consensus overextended. New concept takes: hard skepticism of pre-Week-1 depth charts and coach-speak, and a detailed rejection of the Brian Schottenheimer-unlocks-Dallas narrative behind George Pickens. Josh Jacobs repeats as Harris's preseason fantasy MVP; Javonte Williams named bounce-back candidate at a 10th-round price.

## [2025-09-04] ingest | Matt Waldman's RSP Cast — Sequences, Signal, and the Steelers Offense: RSP Film & Theory with Adam Harstad and Matt Waldman
Steelers offense re-rated upward: Waldman says the market gave up on Aaron Rodgers too soon and calls Pittsburgh sneaky, with Freiermuth the only pass catcher he trusts conceptually and DK Metcalf (Jordy Nelson comp, Seattle film-study frustration story) and Calvin Austin III as the swing factors; Jaylen Warren named starter on pass-pro and adjustment ability. Caleb Williams held at low-end QB1 with top-five upside against Jason Wood's bad-preseason worry. Five new concept pages from Adam Harstad's framework: sequencing as noise, the optimal fumble rate never being zero, retread coaches and culture, Payton-style defined roles, and the aging-QB cliff as selection bias. Bhayshul Tuten flagged as the back whose early fumbles would actually matter.

## [2025-09-04] ingest | Matt Waldman's RSP Cast — Top Rookie Receivers & RB Depth Chart Surprises: Going Deep with Brandon Angelo & Matt Waldman
Rookie WR tiers reordered for Week 1 2025: Waldman/Angelo fade Tetairoa McMillan against his 1,100-yard consensus (release package, Harrison Jr. comp) and elevate Matthew Golden to the preferred rookie WR at cost after Jayden Reed's Jones fracture and Christian Watson's ACL rehab; Travis Hunter confirmed in the Chris Godwin role. Chicago: Luther Burden III third on the depth chart on a deliberate 4-6 week on-ramp but called the team's most dangerous receiver, D.J. Moore recast as a Deebo-type run-game extension, Odunze the target-share winner, Ben Johnson-Caleb Williams friction reports dismissed (Waldman: ~4,000/31, QB13). Pittsburgh: Warren extended and named lead back, Kaleb Johnson limited to low red zone. Washington: Ekeler projected to lead work, Rodriguez short yardage, Croskey-Merritt ~6 rounds overpriced but the 2026 starter.

## [2025-09-05] ingest | Reception Perception: The Show — News & Early Season Buy or Sell
Jayden Reed's Jones fracture reframed as likely season-altering — Harmon skeptical of the 'pain issue' label and expects IR/surgery, with Dontayvion Wicks quietly bought as the slot fill-in. Amari Cooper retired 10 days after signing with Las Vegas, making Dont'e Thornton Jr. the favorite at X (Harmon still selling, MVS-with-hands ceiling). Christian Kirk's hamstring opened Houston's WR2 job, where Harmon argues Jaylin Noel may be better than Jayden Higgins despite the capital gap. Harmon buys Xavier Legette post-Thielen and sells the Joe Flacco fantasy bump (0.9 adjusted YPA under pressure, last of 36 QBs). New concepts: Jones Fracture Receiver Recovery Outcomes, Draft Capital Zombies and Non-Linear Prospect Outcomes.

## [2025-09-05] ingest | Harris Fantasy Football Podcast — Things That Are Freaking Us Out For Week 1 & DALvPHI Review
Christian McCaffrey surfaced with a calf strain two days before Week 1 — Harris' No. 1 terror, Brian Robinson Jr. flagged as 'the handcuff of all handcuffs' and a must-add if free; Harris and Erickson would both trade CMC for Josh Jacobs. Christian Kirk out Week 1 with a hamstring (possibly longer) and Harris says don't chase the Houston replacements. Amari Cooper retired after a ten-day Raiders return. Jaydon Blue a healthy Week 1 scratch — camp hype dismissed as generic. Will Shipley left the opener with a rib injury; Harris says Barkley still has no rosterable handcuff. CeeDee Lamb charged with three drops but held as a buy; George Pickens' 3-30 line explained by two interference calls, not a role loss. Harris pushed back on the pass-heavy Dallas consensus (27 attempts to 22 rushes) and added a new bear case that Nabers and Brian Thomas Jr. lose volume as their offenses get functional.

## [2025-09-08] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 9.8.2025: An RSP Podcast with Bob Harris and Matt Waldman
Week 1 2025 reactions. Keon Coleman upgraded — Waldman calls him 'Tee Higgins with better running ability' and declares the separation concern moot in Buffalo's inside/outside role. Michael Penix Jr. endorsed hard on command vs Tampa's blitz/man. ADP fades: Kenneth Walker III (Charbonnet split, Darnold doubt), Ashton Jeanty (rookie-LT comp, bad situation), TreVeyon Henderson (Mr. Outside only). Omarion Hampton's Week 1 workload reframed as Najee Harris conditioning, not a role win. Harold Fannin Jr. elevated to possible top-12 TE (LaPorta clone). Kayshon Boutte becomes a weekly start and a Waldman dynasty buy. Russell Wilson given two-to-three games before Jackson Dart; Joe Flacco expected to start all season. Noah Fant reversal to positive. Dalton Kincaid and Kyle Pitts capped by usage. New concept material on missed-August reps (A.J. Brown won zero routes vs Dallas per Fantasy Points charting).

## [2025-09-08] ingest | Harris Fantasy Football Podcast — Week 1 Film Review - What Really Happened?
Week 1 2025 film review reshuffles several backfields: Kareem Hunt takes third down and short yardage from Isiah Pacheco; Zach Charbonnet out-snaps Kenneth Walker III 29-20 and steals the goal line; Kenneth Gainwell opens as Pittsburgh's starter with Kaleb Johnson at two offensive snaps; Harris reverses his August fade of Bucky Irving after an 18-3 touch edge. Keon Coleman lifted in the ranks after alpha flashes. Drake Maye called terrible and not a 1QB starter; Russell Wilson called horrendous with Jackson Dart shots on TV. Injuries: Brock Bowers knee (expects Week 2), George Kittle hamstring, Drake London shoulder, Xavier Worthy out on play three. Terry McLaurin out-targeted 10-4 by Deebo Samuel post-hold-in, with the Aiyuk precedent cited. New pages: Kenneth Gainwell and the concept Run-Pass Mix as a Lazy Fade Argument.

## [2025-09-09] ingest | Reception Perception: The Show — NFL Week 1 Reactions: Fluke or for Real?
A.J. Brown flagged as not performance-ready after Harmon's Week 1 charting (44% success vs man, decoy usage) with Jahan Dotson elevated as a real third option in Philadelphia. Garrett Wilson's role materially changed — 36.4% slot rate under Tanner Engstrand after three seasons of rising boundary-X usage — lifting Justin Fields' outlook. Keon Coleman shows charted improvement on curls/digs but Harmon calls his 8-112-1 fluky and separation still weak (Courtland Sutton path). Omarion Hampton's man-gap fit questioned on a ~80% snap share; Brian Thomas Jr.'s dud pinned on Trevor Lawrence accuracy (sub-45% catchable rate); Houston rookies Jayden Higgins and Jaylin Noel buried at 11 routes each.

## [2025-09-09] ingest | Harris Fantasy Football Podcast — Week 2 Waivers & More W1 Film Review
Week 1 2025 film fallout: Travis Etienne Jr. confirmed as Liam Coen's clear lead back (39 snaps) and Tank Bigsby traded to Philadelphia as Saquon Barkley's closest handcuff; Quinshon Judkins avoids suspension and returns Week 2 over Dylan Sampson; Harold Fannin Jr. out-produced David Njoku 7-63 to 3-37, a blow to Njoku's fantasy case; RJ Harvey lost the Denver backfield 37-27 in snaps to J.K. Dobbins; Tua Tagovailoa graded the worst QB of the week and Harris retracted his own contrarian Dolphins take; Caleb Williams mixed (comped to a more mobile Geno Smith); Vikings backfield a true 28-23 Mason/Jones split. Waiver headline adds: Marquise Brown (joint No. 1, volume until Rashee Rice returns), Cedric Tillman, Quentin Johnston, Juwan Johnson (new page), Romeo Doubs, Kenneth Gainwell, LeQuint Allen.

## [2025-09-11] ingest | Reception Perception: The Show — 49ers' Injuries, Rookie Report Cards & Player Props!
49ers offense gutted — Kittle to IR, Jennings MRI, Purdy shoulder/toe with Mac Jones possibly starting; Harmon still calls Pearsall a 10-target player and calls McCaffrey's Week 1 workload 'injury malpractice'. Emeka Egbuka jumps from best-slot-in-league ceiling to possible future engine of the Tampa offense. Rome Odunze charted as Ben Johnson's lead dog (70.6% outside, 81.8% vs man) while Caleb Williams drew a Kyler Murray comp after one 10+ yard throw over the middle. Xavier Legette bear case hardens; Matthew Golden capped by Green Bay's rotation; Christian Watson extended but Harmon doubts the speed returns. Harmon replaced rest-of-season rankings with the weekly RP Notebook.

## [2025-09-11] ingest | Harris Fantasy Football Podcast — Biggest Week 2 Lineup Quandaries & WASvGB Preview
49ers offense gutted — Purdy out 2-5 weeks (turf toe), Kittle on IR a month, Aiyuk out to ~Wk6; Pearsall cut to ~WR30 on the Mac Jones takeover, with Harris framing all three as buy-low rather than sell. Keon Coleman is the big riser (11 targets, Allen's red-zone preference): ~WR54 at draft to ~WR37. Tyreek Hill splits the hosts — Kluge cut him to WR31 and would accept benching him, Harris keeps him top-20 and blames the situation not the player. Bo Nix declared droppable by Kluge. Seattle backfield flipped: Charbonnet now level with or ahead of Kenneth Walker III. Tucker Kraft rose past Andrews and Hockenson; Dallas Goedert pulled from Kluge's ranks on health. Deebo Samuel fade reversed; Croskey-Merritt hype tempered.

## [2025-09-12] ingest | Harris Fantasy Football Podcast — Players We've Already Changed Our Minds On & Thursday Night Injuries!
Austin Ekeler torn Achilles — season over, WAS backfield opens to Jacory Croskey-Merritt (Harris ranks him WAS RB1 for Week 3 but is unimpressed). Jayden Reed broke his collarbone — IR stash only. Harris rank moves: Waddle WR28 to WR44, Pacheco RB21 to RB34, Murray QB13 to QB8, Zay Flowers WR19 to WR10. Keenan Allen upgraded from bench stash to flex; Javonte Williams and Travis Etienne Jr. moved up; Tucker Kraft installed as GB TE1 over Dallas Goedert; Matthew Golden fading with no role even after Reed's injury; Jayden Daniels got zero designed runs vs Green Bay.

## [2025-09-15] ingest | Matt Waldman's RSP Cast — Feel It Or F–It 9.15.2025: An RSP Podcast with Bob Harris and Matt Waldman
Burrow out ~3 months (turf toe, surgery) — Cincinnati collapses to a Chase-only offense, Higgins downgraded to touchdown-dependent. Skattebo called the uncontested Giants lead back by mid-October. Hockenson's 2025 value written off on McCarthy/line. Pickens labeled overrated on route pacing (~900-yard projection) with Turpin at 750-850. Henderson split: redraft fade, dynasty buy, Pollard comp; Stevenson defended as underrated. Ekeler out for the year opens Croskey-Merritt (RB2 ceiling). Waldman abandoned his own 'need August to be ready' theory after Judkins.

## [2025-09-15] ingest | Harris Fantasy Football Podcast — Week 2 Game Reviews!
Harris pumps the brakes on TreVeyon Henderson (16 snaps, 5 touches, 2 holds, blitz-pickup failures) and calls Kaleb Johnson near-unusable after his kick-return blunder; Kenneth Walker III reasserted over Charbonnet (105 vs 10 rushing yards) and stays rated ahead; Troy Franklin passes Marvin Mims Jr. in Denver; RJ Harvey supplemental behind Dobbins; Xavier Legette declared cuttable while Tetairoa McMillan climbs Harris's ranks; Brock Bowers knee uncertain with Harris distrusting Pete Carroll. Harmon: Bills receiver room is a rotation by design (Coleman/Palmer 62.1% routes), do not start Hockenson while J.J. McCarthy struggles, Drake London a buy-low, A.J. Brown not winning route-by-route, and deep concern over the Chiefs' role-catered receivers and Reid's short-route design.

## [2025-09-16] ingest | Reception Perception: The Show — Week 2 Buy/Sell & Panic Meter!
Brian Thomas Jr. downgraded on process — Harmon's fresh charting ties his Week 2 collapse to a 38th-percentile zone success rate and refusal to work the middle, with Trevor Lawrence's inconsistent accuracy sharing blame (Baker/Odell comp). Troy Franklin spikes to a team-high 87.5% route share on a move from outside X to ~60% slot; Harmon tepidly buys. Xavier Legette craters — 15 targets for 8 total yards, last in Y/RR among second-year WRs. A.J. Brown concern level 'pretty high' behind first-time play caller Kevin Patullo. Rashee Rice and Isaiah Pacheco flagged as post-injury athleticism risks in an atrophying Kansas City offense. New concept: Pre-Snap Complexity and Operational Lag.

## [2025-09-16] ingest | Harris Fantasy Football Podcast — Week 3 Waivers & More W2 Game Film
Joe Burrow out ~3 months after toe surgery — Bengals downgraded across the board (Chase, Higgins, Chase Brown) with Jake Browning starting. Mark Andrews declared a must-bench/possible must-drop. Omarion Hampton benched after a fumble in Wk2, Najee Harris closed the game. Cam Skattebo overtook Tyrone Tracy Jr. in second-half Giants snaps. Quinshon Judkins named Harris's top Browns back despite trailing snap counts. Nick Chubb 'patently does not have the juice'; Woody Marks the stash behind him. Waiver board: Daniel Jones #1 (Harris) / Kayshon Boutte #1 (Daigle, disputed by Harris), with Troy Franklin and Elic Ayomanor agreed by both.

## [2025-09-18] ingest | Reception Perception: The Show — Big Bounce-Backs, Big Alignment Shifts & Big 3rd Year Breakouts
Harmon calls Zay Flowers and Jaxon Smith-Njigba live third-year leaps (both top-10 capable; JSN the more sustainable) — Flowers upgraded from underrated to charting-backed alpha. D.J. Moore reframed as a likely mid-season trade chip who hasn't bought into Caleb Williams, with Rome Odunze breaking out ahead of him and Luther Burden the intended replacement. Tyreek Hill downgraded to declining (26th in targets per route run) and also a trade candidate. Big alignment moves recorded: Nacua to 65% slot, CeeDee Lamb to 65% outside, Jeudy to 81% outside as Cleveland's X in 50% 12 personnel. Two new concepts filed on the six-game bust window and on receiver buy-in / addition by subtraction.

## [2025-09-18] ingest | Matt Waldman's RSP Cast — Fantasy Is Weird, Brian Thomas Panic, and Ashton Jeanty Is the Next Trent Richardson: RSP Film & Theory with Adam Harstad & Matt Waldman
Brian Thomas Jr. — Waldman's contested-catch film study rejects the 'soft'/alligator-arm panic, pinning two of five middle-of-field misses largely on Trevor Lawrence placement. Ashton Jeanty — Waldman and Harstad both reject the 'next Trent Richardson' label; Harstad's study puts ~98% of high-workload/low-YPC rookie backs on star paths, and reduced pass-pro/short-yardage/two-minute roles read as normal ramp-up. Tyler Warren — hot start flagged as one-read schemed usage, Waldman expects a dip in ~8 weeks. D.J. Moore and DeAndre Swift — Waldman expects Ben Johnson to shrink both roles (Moore scheme misfit and freelance routes; Swift last in yards after contact behind the league's best before-contact blocking). Two new concept pages: Explanatory Models That Predict Nothing, Toughness Narratives and Salience Bias.

## [2025-09-18] ingest | Harris Fantasy Football Podcast — Hardest To Rank Players For Week 3
Week 3 start/sit movement: Rhamondre Stevenson passes rookie TreVeyon Henderson in Pianowski's ranks (Henderson a bench candidate despite 3rd-4th round cost); Cam Skattebo (new page) overtakes Tyrone Tracy Jr. in the Giants backfield, RB32 vs RB38, with Skattebo Harris's goal-line pick; Calvin Ridley slides to ~WR32 with Pianowski questioning whether he's even Tennessee's best WR; Keon Coleman's week-1 hype deflates to WR45 but Pianowski bumps him above Jaylen Waddle on air; Joe Mixon still on NFI with no ramp-up, realistic return pushed to ~week 7, Woody Marks the speculative beneficiary; A.J. Brown held top-20 despite zero Eagles reaching 10 targets; Terry McLaurin a buy-low despite the Mariota downgrade.

## [2025-09-18] ingest | Matt Waldman's RSP Cast — The Listener Q&A Show: Going Deep with Brandon Angelo & Matt Waldman
Bears usage shift recorded: Rome Odunze to near-every-down first-read role (19%→33% first-read share), DJ Moore's effort and off-script route running flagged by both hosts, Luther Burden III expected to get snaps by mid-October. DeAndre Swift indicted as worst-efficiency back behind the league's best yards-before-contact line. Daniel Jones's start called scheme-driven and unsustainable, with Tyler Warren and Tucker Kraft classed as schemed first-read tight ends rather than Kittle-tier matchup players. Michael Penix Jr. named Waldman's standout second-year QB. New dynasty buy-lows: Rhamondre Stevenson (cheap, better than New England shows) and Matthew Golden (WR1 finish expected). Tyreek Hill flagged as a likely Miami trade-out, opening Malik Washington. Two new concept pages: Yards Before Contact vs Rushing Efficiency Delta, Anonymous Sourcing and Disgruntled Former Staff.

## [2025-09-19] ingest | Harris Fantasy Football Podcast — Five Players Who Are Blowing Our Minds So Far
Harris flipped several week-3 headline views: Brian Thomas Jr.'s 5-of-19 start called a market overreaction and a buy low (wrist injury to monitor); Daniel Jones named his single most surprising player in the NFL yet still only QB27 in his ranks; Tetairoa McMillan promoted to WR15 with a specific scouting profile (elite hands, limited speed, straight-line/zone-settle route wins); A.J. Brown dropped to WR18 but labelled a buy low against guest Josh Fisch's structural Eagles pass-volume bearishness; Travis Etienne Jr. re-rated to 2023 form after Tank Bigsby was traded, narrowing Bhayshul Tuten's path (LeQuint Allen owns third downs); Bears offense pinned on Caleb Williams (28th in EPA), dragging Colston Loveland down. New pages for Ollie Gordon II (Miami short-yardage/goal-line role) with Jaylen Wright written off after zero snaps while active. Injury moves: Zach Charbonnet (foot, likely out — Kenneth Walker III back as lead), Xavier Worthy returning through a reported torn labrum as a high-risk play.

## [2025-09-22] ingest | Matt Waldman's RSP Cast — Feel It Or F–It 9.15.2025: An RSP FPodcast with Bob Harris and Matt Waldman
Cam Skattebo declared the Giants lead back (Tyrone Tracy Jr. shoulder x-rays); Travis Kelce called done as an elite fantasy producer; Tetairoa McMillan downgraded below WR2 talent for now — loses vs. press man, being schemed open; Harold Fannin Jr.'s role called locked in as a low-end TE1; Isaiah Pacheco flagged as no better than post-injury 2024 with Brashard Smith deemed too small to take over; Waldman rejects Ryan Clark's Trent Richardson comp on Ashton Jeanty; Chris Godwin and KaVontae Turpin flagged as adds.

## [2025-09-22] ingest | Harris Fantasy Football Podcast — Week 3 Game Reviews
Week 3 injury cascade: Najee Harris ruptured Achilles (out for year) hands the Chargers backfield to Omarion Hampton; James Conner broken ankle hands Arizona to Trey Benson; Tyrone Tracy stinger opened the door for Cam Skattebo. New England's Stevenson and Gibson both fumbled themselves out of the game — Harris expects TreVeyon Henderson to take over. CeeDee Lamb high ankle sprain (Harris expects at least one missed game) and Alec Pierce concussion. Downgrades: Calvin Ridley re-priced WR40-48 by guest Patrick Doherty, Ja'Marr Chase to WR5-8 with Browning at QB, Travis Kelce 'looks slow,' RJ Harvey losing work to J.K. Dobbins. Upgrades: Quentin Johnston as the Chargers' revelation, Quinshon Judkins as a clear lead back, Daniel Jones capped at a QB12 ceiling.

## [2025-09-23] ingest | Reception Perception: The Show — NFL Week 3 Takeaways!
Mike Evans hamstring (multi-week) pushes Tampa volume to Emeka Egbuka and Sterling Shepard. CeeDee Lamb high ankle sprain — George Pickens forced to pure X (2.6% slot) and Harmon stays skeptical, calling him a number two; Jake Ferguson's target load spikes. Harmon's Denver charting confirms a real Quentin Johnston Year 3 leap (slant 20.4%/dig 18.5% route rates, 87.5% success vs zone) while insisting Ladd McConkey's down per-route metrics are teammate-driven, not decline. Malik Nabers cratered by Russell Wilson's limited menu (20.9 air yards/target). Koh's charting has Ashton Jeanty at 54.5% unblocked-defender and ~55% loaded-box rates, prompting a new concept page on run-game context and tipped plays. New pages: Loaded Boxes and Unblocked Defender Rate.

## [2025-09-23] ingest | Harris Fantasy Football Podcast — Week 4 Waivers & More W3 Game Film
Harris reversed onto Mark Andrews as a startable TE after Baltimore's deliberate first-drive targeting; Terry McLaurin strained a quad on a wrongly overturned TD; Mike Evans pulled a hamstring and exited. Ashton Jeanty flagged as a bad start (2 third-down snaps to Zamir White's 10, 'not first round yet'); Rico Dowdle's fourth-quarter hot hand became Harris's first 'uh-oh' on Chuba Hubbard; Michael Penix Jr. benched for Cousins after a 30-0 shutout, though Harris expects him to keep the job. Travis Hunter's 45 defensive snaps named as the reason he is unstartable. Waiver board established with Scott Fish: Chris Rodriguez Jr., Ollie Gordon II, Woody Marks, Elic Ayomanor, Oronde Gadsden II, Tyjae Spears; new page for Jeremy McNichols as the Washington third-down back.

## [2025-09-25] ingest | Reception Perception: The Show — Figuring Out the Raiders, Rookie Breakouts & A Familiar Name in Indy
Harmon's first-ever Tre Tucker chart makes him a full-time 95%-route outside speed player and a workable zone beater; Jack Bech argued onto the field as the Raiders' missing chain-mover. Ashton Jeanty defended against Ryan Clark/Chris Sims criticism on environment grounds — record 32% unblocked defender rate, ~40% loaded boxes, 101% of yards after contact. Tory Horton upgraded to a real starter (85% out wide, path to Seattle WR2); Cooper Kupp downgraded to an underneath-only role behind a leaping JSN. Travis Hunter's 2025 expectations tamped down after Liam Coen capped him at the F/slot, with Parker Washington absorbing outside snaps. Harmon partly reverses his Josh Downs-over-Michael Pittman Jr. offseason stance. Luther Burden III still WR4 at 31% route participation despite a 101-yard game.

## [2025-09-25] ingest | Harris Fantasy Football Podcast — Key Week 4 Start-Sit Decisions & Previewing SEAvARI
Week 4 start-sit: Croskey-Merritt established as Washington's snap/route leader in a rotation (hold-your-nose flex); Brian Thomas Jr. held at WR11 despite drops, contact-shyness and a wrist issue — both hosts say start him; Trey Benson elevated to mid-RB2 on ~87% snaps with Conner out, Harris cooler with a Mostert comp; Skattebo now a near-every-league starter with Tracy out; Rhamondre Stevenson expected in the doghouse after two more fumbles, opening TreVeyon Henderson's first-team reps; Marvin Harrison Jr. cratered to a WR28/WR30 coin flip with hope deferred to year three; Kelce called 'pretty washed' by Gretch and startable-over by Cade Otten; Jeanty heading toward the bust label.

## [2025-09-26] ingest | Harris Fantasy Football Podcast — Five Players To Trade For
Harris reverses on [[Bucky Irving]] (admits he was 'too low', now rates him above [[De'Von Achane]] on tape) and on [[Tetairoa McMillan]]. [[Brian Thomas Jr.]] named the biggest panic-sell buy in fantasy despite 7 catches on 25 targets; [[Jordan Addison]] a buy-very-low outside Fantasy Pros' top 100 post-suspension. Cardinals backfield clarified — [[Trey Benson]] rough debut without [[James Conner]], [[Emari Demercado]] owns third downs (12 snaps to 2) and the two-minute drill. Injuries: [[Terry McLaurin]] 'doesn't need surgery right now' read as bad, unlikely week 4; [[Davante Adams]] hamstring in danger of missing; [[Colston Loveland]] may miss with a hip. New concepts on the running-back trade premium, buy-low/panic-sell windows and retrofitted personality narratives; target-concentration data (36 ten-target games in 96) added to [[Alpha Receiver vs Committee Pass Catchers]].

## [2025-09-29] ingest | Matt Waldman's RSP Cast — Feel It Or F–It 9.29.2025: An RSP Podcast with Bob Harris and Matt Waldman
Brock Bowers downgraded — limping in a large knee brace, Waldman expects 4-6 weeks of misery and possible season-trajectory change. Ladd McConkey panic called warranted: Chargers hierarchy now includes a fixed-up Quentin Johnston, Keenan Allen and Oronde Gadsden II. Omarion Hampton flagged as a dynasty sell-high on best-case usage with Najee Harris out; Waldman softens but does not reverse his talent gap vs Jeanty. Jeanty's breakout partly credited to Chicago nickel personnel. Terry McLaurin week to week with a high quad injury, lifting Luke McCaffrey. Brian Thomas Jr. wrist declared a non-issue; the Lawrence deep-route chemistry is the real problem. Cedric Tillman's hamstring opens the door for Isaiah Bond. Kyle Pitts finally used downfield and on red-zone play action.

## [2025-09-29] ingest | Harris Fantasy Football Podcast — Week 4 Game Reviews
Malik Nabers knee injury vs LAC, feared season-ending — Harris sees no startable Giants WR without him. Lamar Jackson exits with a hamstring (part pout, part hamstring) and Baltimore falls to 1-3, with Eisenberg lowering Derrick Henry expectations on negative scripts. Ashton Jeanty breaks out for two TDs and Harris calls the buy-low window shut. Xavier Worthy used as a genuine deep threat (4 targets 20+ air yards) and Harris abandons his bust take; Eisenberg calls Mahomes top-3 ROS while Harris says starter-but-not-top-3. Omarion Hampton becomes the Chargers bell cow (49 snaps) with Najee Harris out; Cam Skattebo takes over the Giants backfield at 52 snaps but 0-for-4 inside the five. Jaylen Warren surprise inactive, Gainwell one-week fill-in. Joe Alt high ankle sprain craters the Chargers line — Harris warns September may be the passing game's high-water mark for Herbert and McConkey. Puka Nacua declared the number one receiver in fantasy; Davante Adams explicitly not the Rams WR1. Bryce Young a hopelessly bad outing, benched for Dalton. New England backfield still a 28/14/9 three-way split — Henderson did not get the job.

## [2025-09-30] ingest | Reception Perception: The Show — Week 4 Was a Wild One
Nabers ACL — out for 2025, Giants WR room called bereft. JSN leapt to true X (78.6% outside) and moved up Harmon's dynasty ranks into tier two. Nacua argued as dynasty WR1 on a 2,100-yard pace. A.J. Brown downgraded: 'stuck' on routes, no longer the man-coverage No. 1. McConkey expectations cut as Quentin Johnston 'is legit' and Keenan Allen holds up. Pickens shows WR1 ceiling from 96.7% outside. D.J. Moore floated as a Giants trade candidate after being bypassed by Odunze.

## [2025-09-30] ingest | Harris Fantasy Football Podcast — Week 5 Waivers & More W4 Game Film
Tyreek Hill dislocated his knee and is out for the season — Waddle hiked in ranks, Darren Waller (new page) and Malik Washington become waiver targets, Achane the biggest beneficiary. Woody Marks is Harris and Erickson's unanimous #1 Week 5 add (38-26 snap edge on Nick Chubb, passing-down role) with Joe Mixon reported 'not close' to returning. Harris rejects top-10 rest-of-season talk on Quinshon Judkins (found-money RB2) and calls Michael Penix Jr. benching chatter dumb. Calvin Ridley now droppable (drops, chemistry, possible effort issues). Cedric Tillman hamstring, out multiple weeks. Harris and Erickson split on Kendre Miller's handcuff tier vs Tyjae Spears; Blake Corum affirmed a top-five handcuff. Bijan Robinson declared the clear 1.01 in a hypothetical redraft.

## [2025-10-02] ingest | Matt Waldman's RSP Cast — QB Performances, Offensive Struggles, and Backfield Developments: Going Deep with Brandon Angelo & Matt Waldman
Cam Ward downgraded on situation, not talent — no drop plan under Callahan, Angelo expects him fired first. A.J. Brown and Saquon Barkley neutered by first-time play caller Patullo (Goedert out-targeting Brown 8-2). Dillon Gabriel graded reserve/C-tier bridge starter, a rung below Shedeur Sanders and not Cleveland's 2026 QB; Isaiah Bond and Harold Fannin Jr. flagged as the Browns' real playmakers. Woody Marks projected as Houston's touch leader over Nick Chubb, who slips to a short-yardage Jamaal Williams role. Brian Thomas Jr.'s deep trait cratered by Trevor Lawrence (zero 20+ yard completions in four games, Lawrence 1-of-10 deep); Travis Hunter misused as a part-time slot F. Cam Skattebo named the Giants' best offensive player. Kenneth Gainwell capped at 600-800 yards with a possible post-bye 50/50 split with Jaylen Warren.

## [2025-10-02] ingest | Harris Fantasy Football Podcast — Week 5 Start & Sit Decisions Plus SFvLAR Preview
Trey Benson to IR (meniscus scope, 4-6 weeks) — Arizona backfield collapses to an emergency Michael Carter / Emari Demercado committee Harris rates as unproven. Bucky Irving dropped from Harris's ranks entirely on a walking-boot foot injury; Rachaad White up to RB22. Woody Marks established as the waiver add of the week, ranked ahead of Chase Brown by both hosts. Harris reversed his summer fade of Javonte Williams. Ashton Jeanty's buy-low window declared closed. New concept pages: Hot Dog Quarterbacks (guest Jeff Bell's coinage, applied to Justin Fields at QB2/QB8).

## [2025-10-02] ingest | Reception Perception: The Show — Xavier Worthy Returns + Why is Top WR Production Trending Down?
Xavier Worthy's role clarified after Week 4 charting — vertical/quick-out player at a 70.7% route share, decoy value creating scores for JuJu Smith-Schuster and Marquise Brown; Harmon and Koh both flag Rashee Rice ramp-up risk on the Tank Dell precedent. Marquise Brown downgraded to intermediate-only zone beater with little pop left; Tyquan Thornton bought as a real third/fourth receiver. Josh Downs' outlook capped by Indianapolis' 12 personnel with Tyler Warren — Harmon files him under the Elijah Moore Rule. New concepts: Twelve Personnel Rise and Slot Receiver Playing Time, Wide Receiver Injury Rate Trend. Jackson Dart hype rejected — 111 passing yards, fantasy value is rushing only.

## [2025-10-03] ingest | Harris Fantasy Football Podcast — Five Players To Trade Away, SFvsLAR Review & W5 Injuries
Harris's headline in-season stance crystallizes: trade away all quarterbacks except Josh Allen (QB3-to-QB13 gap ~4 ppg), sell Bowers/McBride at their FantasyPros top-20-overall price, and pay the 'running back tax' to acquire backs. New pages for Mac Jones (career game against a passive Rams two-high plan, 42 of 49 attempts vs two-high, still not a fantasy starter per Harris) and Hunter Henry (sell-high TE9). Injury moves: Chuba Hubbard out W5 (calf) with Rico Dowdle up the ranks, Bucky Irving exotic foot injury, Brock Bowers hobbled on the W1 knee, Taysom Hill PUP-eligible. Drake London flagged as an overpriced sell at FantasyPros 11th overall (Harris) while guest Josh Van Blank would buy him — disagreement recorded. Chase Brown marked a buy-low after the Bengals' MNF collapse.

## [2025-10-06] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 10.6.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman fades TreVeyon Henderson outright ('roster clogger' per Bob Harris) and rejects a Woody Marks takeover — Houston and New England stay splits. Kincaid upgraded on intermediate/over-the-middle usage; Stefon Diggs graded fully back from the ACL at WR2 value with WR1 upside. Puka Nacua split into a top-3-5 fantasy WR but not a Chase-class route runner (scheme-dependent on McVay). New pages: Kendrick Bourne (SF passing-game answer while Mac Jones starts). Marvin Harrison Jr.'s ceiling tied to moving on from Kyler Murray; Darren Waller's snaps doubled but drew zero second-half targets.

## [2025-10-06] ingest | Harris Fantasy Football Podcast — Week 5 Game Film Review
Diggs 10-146 revenge game — Harris moves him into all lineups; Judkins to 'RB1 neighborhood' after 110 yards vs MIN; Croskey-Merritt cleared as a startable lead back in Washington; Antonio Gibson knee injury (likely out a while) with Henderson still third; Omarion Hampton ankle exit; Woody Marks 7-24 dud and Chubb starts, backfield unresolved; Hockenson downgraded to default top-12 only; Godwin's rank cut after a drop and vanishing targets; Brian Thomas Jr. labeled one of the year's biggest busts with Worthy ranked ahead of him.

## [2025-10-07] ingest | Reception Perception: The Show — NFL Week 5 Takeaways!
Harmon's charting flips [[Emeka Egbuka]] from projected slot dirty-worker to on-the-line outside WR1 in Tampa (4th in NFL yards, 89.5% dig success, his OROY favorite); [[Jaxon Smith-Njigba]] elevated to top-10 NFL WR. [[A.J. Brown]] materially downgraded — man-coverage success rate off four straight 96th-percentile seasons, slot rate down to ~15%, chronic knee drainage, trade/decline risk and a stated dynasty sell window. [[Stefon Diggs]] re-rated upward as a capped-snap but high-caliber WR1 post-ACL; [[Chris Olave]] labelled a PPR scam despite a role Harmon likes; [[Spencer Rattler]] and [[Courtland Sutton]] given credit. New concept page on digs and deep overs versus cover two.

## [2025-10-07] ingest | Harris Fantasy Football Podcast — Week 6 Waivers & More W5 Game Reviews
Xavier Worthy downgraded — Harris calls his own top-10 Week 4 rank 'a very bad call', with Worthy on a bad ankle and used as a partial decoy; outside Mahomes and Kelce he sees no must-start Chief until Rashee Rice returns Week 7. Omarion Hampton to IR (ankle, 4+ weeks) makes Kimani Vidal and new page Hassan Haskins the top Week 6 waiver adds, with a ~$15 contingency-bid framework. Michael Carter confirmed as Arizona's lead back with Conner out for the year and Benson scoped; Emari Demercado stays third-down and cost managers a game with a goal-line celebration fumble. Rico Dowdle 200+ rushing yards with Hubbard out. Elic Ayomanor's bye-week-emergency case answered with 'a resounding no'; Darius Slayton hamstrung and never a Nabers replacement in Harris' view. Trevor Lawrence unchanged and unimpressive despite a two-rushing-TD box score; Ashton Jeanty back to underwhelming with the Maurice Jones-Drew comp walked back.

## [2025-10-09] ingest | Reception Perception: The Show — Deebo Resurgence, Waddle sans Tyreek + Rookie's Rising
Deebo Samuel resurgence attributed to a jump from ~25% career slot rate to 64% under Kingsbury (PPR WR7, 6th in receptions vs zone); Waddle becomes Miami's focal point post-Tyreek with a season-high 24% slot rate; Harmon charts Jack Bech's 52%-snap promotion and calls the Raiders' handling a mistake, formalizing his shift toward the power-slot zone-beater archetype over press-man X types; Jerry Jeudy miscast as Cleveland's X (slot rate 50%-35%-15%, 15.6% drop rate); Jameson Williams reduced to a 19.4 aDOT deep decoy under John Morton while Isaac TeSlaa's snaps rise; Travis Hunter's best NFL receiving game to date; Adonai Mitchell benched to six snaps.

## [2025-10-09] ingest | Harris Fantasy Football Podcast — Tough Start & Sit Decisions For Week 6 Plus A Snarkbag!
Chris Harris moved off [[A.J. Brown]] for the first time — ranked WR23 and explicitly allowed sitting him, blaming Kevin Patullo's play calling (Waldman dissents, still starts him). Waldman dropped [[Derrick Henry]] to flex/near-bench without Lamar Jackson vs. the Rams (Harris RB19). [[Mason Taylor]] elevated to low-end TE1 on Justin Fields' 37% career tight-end target rate. [[Jackson Dart]] downgraded on charting: one accurate throw past 25 yards as a pro; Harris QB26. Contrarian [[DeAndre Hopkins]] start from Waldman that Harris openly disputed. Three concept pages: [[Post-Bye Rookie Bump]] extended, plus new [[Fantasy Points Allowed and Opponent Context]] and [[Wide Receiver Positional Flatness]].

## [2025-10-09] ingest | Matt Waldman's RSP Cast — What You Value, You Measure & Dynasty Rebuilds: RSP Film & Theory w/Adam Harstad & Matt Waldman
Two new concept frameworks from Harstad via the RSP Cast: Goodhart's Law (a good measure dies once it becomes a target — drops, size thresholds, SPARQ, Parcells' checklist) and a full dynasty rebuild model built on ~20%/yr roster value decay, 'don't lose value,' rookie picks as the only safe store, and a 1-2 year rebuild cap. New page on positional stockpiling: cuts variance and upside, needs a liquid trade market. Dented-can buys named: Javonte Williams, J.K. Dobbins, Fournette as the precedent. Prescott preferred over Cam Ward in a rebuild; Ward flagged as unproven. Waldman re-litigated Dalvin Cook's compensatory factors and the Josh Allen/Lamar Jackson evaluation reversal.

## [2025-10-10] ingest | Harris Fantasy Football Podcast — Hot & Cold Starts We Don't Want To Trade Plus PHI v NYG Madness
Cam Skattebo takes over the Giants backfield (3 goal-line TDs, 112 yards on 21 touches) with Tyrone Tracy Jr. down to four touches; Harris still won't rank Jackson Dart as a QB1 despite three straight 50-yard rushing games. Chris Godwin's fibula re-injury (same bone as last year, feared long-term) solidifies Emeka Egbuka, and Harris flips to Behrens's hold. Javonte Williams (RB2 standard/RB4 PPR, 17-of-19 receiving) and Mahomes (QB2) named firm holds; Harris turns active seller on George Pickens ahead of CeeDee Lamb's return, and fades buy-lows on Pollard, Swift, Higgins and McConkey. Brock Bowers unranked for Week 6 on a sprained knee. Eagles offense flagged as a possible second-half fantasy drag.

## [2025-10-13] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 10.13.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman declares Drake Maye's leap already made (3 pressured deep TDs vs NO) and Kayshon Boutte a provisional add now that Maye is trusting him; Romeo Doubs upgraded to Green Bay's best receiver with catch-point issues fixed, Tucker Kraft to weekly start but schemed-open rather than Kittle-level; Rachaad White defended as underrated but only until Bucky Irving returns; Quinshon Judkins declared RB1 talent on a non-RB1 team and not an RB1 this year; Xavier Legette called a bust and Justin Fields a garbage-time compiler after minus-10 net passing yards; Kimani Vidal defended but his 124-yard day discounted for Miami, becoming the case study for the new Sunday Morning Insider Reports and Fantasy Noise concept.

## [2025-11-03] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 11.3.2025: An RSP Podcast with Bob Harris and Matt Waldman
Tucker Kraft confirmed out for the season with a torn ACL — Luke Musgrave inherits the role at ~80-90% of Kraft's production per Waldman. Waldman flipped the rookie TE hierarchy: Colston Loveland rated above Tyler Warren as a player, with Warren's fantasy value now hostage to whether defenses copy Pittsburgh's blueprint (new concept page, Defensive Blueprints and Copycat Feasibility). Alec Pierce elevated to more complete receiver than Michael Pittman Jr. Injury/role shifts: Rhamondre Stevenson toe (TreVeyon Henderson to RB2/3), Kayshon Boutte hamstring (Demario Douglas window), Samaje Perine ankle (Tahj Brooks window). Waldman pushed back on the Ben Johnson-makes-Caleb-Williams narrative, and named Jahmyr Gibbs the weak link in Detroit's protection (7 pressures on 16 pass-block snaps).

## [2025-11-03] ingest | Harris Fantasy Football Podcast — Week 9 Game Film Breakdowns
Jayden Daniels apparently broke his arm on a scramble — Harris calls the season over and revives RG3 injury comparisons, dragging down the whole Washington offense (Ertz to check-down magnet, Mariota under center). Aaron Jones left with an 'minor' AC joint shoulder injury that both Harris and Rotoworld's Patrick Doherty distrust; Jordan Mason gets no lift because neither thinks the Vikings line can power block for him. Tee Higgins (possible head injury) and Brian Thomas Jr. (leg/ankle, missed OT) both exited hurt. TreVeyon Henderson took over the New England backfield with Rhamondre Stevenson out (52 snaps, 20 touches) but ceded goal-line work. Brock Bowers scored three times and Harris says he floats the Raiders offense. Drake London exploded for three touchdowns. Tory Horton added as a Kupp-minimized Seattle stash. Harris discounts Kyle Monangai's 176 yards against a Bengals defense he calls a joke, while flagging Rome Odunze's shutout as a bitter pill. Doherty on the Chiefs: 'a copy of a copy', with Rashee Rice as a quarterback binky making the offense predictable.

## [2025-11-04] ingest | Harris Fantasy Football Podcast — Week 10 Waivers & More W9 Game Film
Tucker Kraft tore his ACL and is out for the year, making Luke Musgrave (1% rostered) a top waiver add with a blocking caveat. Rico Dowdle confirmed as Carolina's clear lead back — Harris grades his own miss on ranking Chuba Hubbard alongside him. C.J. Stroud concussed, which Harris says makes every Houston skill player including Nico Collins unstartable. Arizona's backfield ruled a patternless committee (Knight 37 snaps and 3-0 inside the five vs Demercado's 15-11 touch edge) with a brutal Seattle matchup — new page for Zonovan Knight. Alec Pierce led Colts targets on intermediate routes rather than bombs and has Harris's attention. Daniel Jones's five-turnover day pinned mostly on a collapsed Colts offensive line. Bo Nix 2-for-11 on 20+ air yard throws. Devin Singletary out-snapped Tyrone Tracy Jr. 31-25 in the post-Skattebo Giants backfield. Waiver lists topped by Tory Horton (Harris) and Parker Washington (Erickson).

## [2025-11-04] ingest | Reception Perception: The Show — Week 9 NFL Takeaways!
JSN declared fully graduated to elite (NFL lead in receiving yards per game). Tory Horton breaks out for 2 TDs starting over an injured Cooper Kupp — Harmon says he is Seattle's second-best perimeter receiver and unlocks moving JSN around; Kupp downgraded to mentor/blocker. Jayden Daniels suffers a severe elbow injury (third injury of 2025); Travis Hunter to IR with a non-contact knee injury and Brian Thomas Jr. possibly a high ankle sprain, pushing slot work to Parker Washington. Kayshon Boutte grade-one hamstring sprain opens a role for rookie Kyle Williams (74% second-half route share). Rome Odunze's zero-catch game called fluky/opponent-driven, not structural.

## [2025-11-06] ingest | Matt Waldman's RSP Cast — Bears, Colts, Jaguars, Falcons, Fantasy Buys, and Ashton Jeanty: Going Deep with Brandon Angelo & Matt Waldman
Waldman/Angelo Going Deep, Week 10 2025. Brian Thomas Jr. downgraded hard — Angelo says Lawrence's third-level limitation neutralizes his superpower, leaving him roughly average, plus a possible high ankle; Parker Washington elevated to a buy with Coen putting Jakobi Meyers on the boundary instead of the slot. Tyler Warren's production reframed as largely schemed 'free parking' yardage (80%+ of one game), which Pittsburgh removed; Daniel Jones's blueprint exposure prompts a playoff-run QB warning. Jahmyr Gibbs named a buy-low (offensive line injuries + Morton dropping option routes, not decline); Kyle Monangai promoted to a real committee role as the David Montgomery-style TD back, with Angelo doubting DeAndre Swift returns in 2026. Drake London called a potential top-five WR after the Penix fade game. New concept pages: Assumption of Rational Coaching, Running Back Longevity and Draft Round Study. New player pages: Greg Dulcich.

## [2025-11-06] ingest | Reception Perception: The Show — NFL Trade Deadline Breakdown!
Trade deadline reshuffle: Jakobi Meyers to JAX starting outside with Parker Washington kept in the slot; Rashid Shaheed to SEA reuniting with Kubiak, capping Tory Horton and further squeezing an unimpactful, injured Cooper Kupp; Adonai Mitchell to NYJ where Harmon wants him at pure X only (87% vs press, bottom-percentile vs zone); Kyler Murray to IR with Jacoby Brissett named starter regardless — Harmon calls Murray a scheme misfit and credits Brissett's under-center rate (46% vs 21%) with activating Marvin Harrison Jr. Jack Bech flagged as the Raiders slot heir with Harmon and Koh disagreeing over veteran deference to Tyler Lockett. Alec Pierce elevated to Harmon's most-improved WR in the league.

## [2025-11-06] ingest | Matt Waldman's RSP Cast — Players We Think We Know & Playing NFL Owner for An Hour: RSP Film & Theory w/Adam Harstad & Matt Waldman
Waldman-Harstad 'players we think we know' episode moved several headline views: Tyler Warren downgraded by Waldman to the schemed-open Tucker Kraft tier (good not great) against Harstad's Bowers-tier read; Trey McBride bumped to his own tier between Kittle/Bowers and the field once Arizona's QB play improves; Ashton Jeanty defended as a buy-low with the LaDainian Tomlinson rookie-year comp; Caleb Williams called an underrated cornerstone; Daniel Jones explicitly not a Darnold-style leap after the Steelers game (3 INTs, 4 tipped passes, 2 forced fumbles); Rome Odunze called a true WR1 and top-15 receiver with the early drops dismissed as noise; Nico Collins framed as a year-to-year injury tease. New concepts: Settled Player Opinion and Flat Dynasty Value, Measurable Skills Bias in Running Back Analytics, Quarterback Ownership of the Offense. Waldman's 23-RB/23-WR longevity study added to Running Back Longevity and Draft Round Study.

## [2025-11-06] ingest | Harris Fantasy Football Podcast — Week 10 Lineup Decisions & Listener Snark
Trade-deadline fallout reshuffles several flex calls: Jakobi Meyers to JAX and Rashid Shaheed to SEA, with Harris ranking Shaheed ahead of Meyers on Klint Kubiak scheme continuity and Meyers a spot behind Parker Washington for Week 10 only. Devin Singletary moves ahead of Tyrone Tracy Jr. on goal-line and blocking snaps in a Dart-centered Giants offense (Behrens disagrees). TreVeyon Henderson is an RB2 with Stevenson out but Harris says his pass protection is bad enough to cost him third downs. Troy Franklin rises into flex range on 28 targets in three games. Emari Demercado/Zonovan Knight remains an unresolved committee. New concept page: Midseason Trade Acquisition and Offensive Acclimation.

## [2025-11-07] ingest | Harris Fantasy Football Podcast — Five Pivotal Players For The Rest Of 2025
Chase Brown raised 38 to 28 in Harris's rest-of-season ranks on Perine's high ankle sprain returning him the passing-down role. Bo Nix downgraded in tone — 'pump the brakes' on elite after a defense-carried 10-7 win with eight three-and-outs. Justin Herbert flagged as a top-ten-QB fall risk with both Chargers tackles gone; Keenan Allen and Ladd McConkey moved into the sell-if-asked bucket. TreVeyon Henderson at 75-80% snaps with Rhamondre Stevenson (toe, possibly long-term) not practicing. Bucky Irving ranked 65 and Ricky Pearsall ~73 as pure lottery tickets. A.J. Brown still WR1 at 23 overall but explicitly a fantasy-playoff dud risk. Joe Flacco named the single most pivotal player as the Atlas under Chase, Chase Brown and Higgins.

## [2025-11-10] ingest | Matt Waldman's RSP Cast — Feel It Or F--It 11.10.2025: An RSP Podcast with Bob Harris and Matt Waldman
Waldman held Colston Loveland as his 2025 TE1 over Tyler Warren even after Warren's 8-99 contested-catch game, arguing look quality and blocking; Ladd McConkey confirmed as WR7 since Week 4 with the prodigy skepticism declared dead; Tetairoa McMillan downgraded to a Michael Pittman Jr. comp — good starter, not a true number one; Isaiah Likely expected priced out of Baltimore in favor of Charlie Kolar (new page); Davis Mills (new page) framed as a journeyman starter; Blake Corum named the Rams handcuff of record over Jarquez Hunter; Luther Burden III's full role called imminent; Bo Nix defended against 'found out' takes.

## [2025-11-10] ingest | Harris Fantasy Football Podcast — Week 10 Game Film Review
Alec Pierce reframed as Indianapolis's primary third-down read rather than a pure deep threat, with Michael Pittman Jr. sliding; goal-line vulture panic around Bijan Robinson and Christian McCaffrey debunked with month-long red zone snap counts (new concept page). TreVeyon Henderson broke out for two long TDs after Terrell Jennings' knee injury; Harris retracted Demario Douglas as the Diggs fill-in in favour of Mack Hollins. Injuries: Dalton Kincaid hamstring, Davante Adams non-contact lower back, Tetairoa McMillan hamstring watch. Mac Jones checkdown act declared over pending Brock Purdy; Aaron Jones confirmed the Vikings lead back with Jordan Mason demoted to handcuff; Alvin Kamara's first 100-yard scrimmage day since Week 2; Aaron Rodgers' worst game of the year.

## [2025-11-11] ingest | Reception Perception: The Show — We're Talkin' About Week 10!
Detroit's offense re-keyed under Dan Campbell as play caller — Jameson Williams unlocked on in-breakers/YAC (7-6-119-1, air yards down to ~10) and Amon-Ra St. Brown to 78% slot. Tyler Shough's stock rises after leading Week 10 in adjusted YPA; Harmon prefers him to Rattler. Devaughn Vele becomes the Saints' snap/route leader post-Shaheed trade while Brandin Cooks is written off as a sacrificial X (0 targets on 22 routes). Justin Jefferson's worst game in 14 defended as a McCarthy catchable-target issue (42%), not effort. Marvin Harrison Jr. 3-33-1 on 12 targets — still zero 100-yard games in 2025. Jerry Jeudy mea culpa from Koh, framed by Harmon as volume-driven.

## [2025-11-11] ingest | Harris Fantasy Football Podcast — Week 11 Waivers & More W10 Game Film
Garrett Wilson re-injured his knee and is out 2-3 more weeks; Nick Chubb's role collapsed (10 snaps to Woody Marks's 54) and Harris says he needn't be rostered; Chris Rodriguez Jr. emerged as the actual Commanders starter but hurt a shoulder, with Croskey-Merritt's snap lead exposed as garbage time; Harris declares Travis Etienne back on film and calls Walker/Charbonnet near-interchangeable; Tyler Allgeier and Tez Johnson the Week 11 top adds, with Alec Pierce named WR add of the week; Harris doubts A.J. Brown is cooked at 28 and dismisses the Jacoby Brissett-over-Kyler Murray narrative.

## [2025-11-13] ingest | Harris Fantasy Football Podcast — Ashton Jeanty Film Futures & Week 11 Lineup Advice
Jeanty's film verdict from Harris: real talent but over-patient and undersized-when-contacted — Ray Rice/D'Angelo Williams as the good outcomes, not a first-round fantasy back. Houston backfield separated: Woody Marks to flex-plus, Nick Chubb down to ~10 snaps. Jameson Williams elevated to near-WR2 on Dan Campbell play-calling (WR18 since Week 6). Jacksonville reframed around Trevor Lawrence's vertical limits — Parker Washington's slot role is the safe target share, Meyers pushed outside, and Waldman/Angelo question whether Brian Thomas Jr. fits long term. Luther Burden III flagged as an active dynasty buy. Michael Wilson gets the Harrison-out volume bump but Harris still ranks Dortch ahead. Dontayvion Wicks's hands graded D.

## [2025-11-13] ingest | Reception Perception: The Show — NFL News & Notes Ahead of Week 11!
Travis Hunter's season ended by LCL surgery (2026 role now uncertain). A.J. Brown publicly unhappy, 83% outside alignment and not separating — Harmon says he is no longer his peak self, while DeVonta Smith ascends to top-ten NFL level. Jaylen Waddle broke out post-Tyreek Hill (2.9 YPRR, third in EPA per target). Troy Franklin overtook Courtland Sutton in Denver targets (81% routes, 43% air-yards share) but with a 48.6% catch rate; Pat Bryant carving a big-slot role. Marvin Harrison Jr. out with appendicitis and Zay Jones on IR, funnelling targets to Trey McBride and Michael Wilson. Jameis Winston named Giants starter — Harmon dismissive, Koh bullish on Darius Slayton; hosts split on whether Minnesota should play out J.J. McCarthy.

## [2025-11-13] ingest | Matt Waldman's RSP Cast — Paper Champions and Moving All-Timers to Different Eras: RSP Film and Theory with Adam Harstad and Matt Waldman
Harstad's paper-value thesis filed as a new concept — flawed public dynasty values still correlate with the ideal, so the prettiest roster on paper really is the best single title bet, with the caveat that it reduces to 'avoid busts.' Chase Brown recorded as a live 2025 paper-value miss (high preseason trade value, market cooled); Rico Dowdle and Jonathan Brooks recorded as the Carolina backfield's opportunity-vs-pedigree lesson. Cordarrelle Patterson framed as the greatest returner ever, records set in the decade the league suppressed kickoffs. Four new concepts added: paper value/championship correlation, era translation and adaptability, formative-era nostalgia bias, and random class clustering warping positional baselines, plus touch volume and in-game adaptation.
