# Fantasy Football Knowledge Base — Index

An LLM-maintained wiki of fantasy football analysis, built from podcast
transcripts of three trusted analysts. Structured after Andrej Karpathy's
[llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern.

**Purpose:** answer real draft and waiver-wire questions — comparing players
across [[Best Ball]], [[Dynasty]], and [[Redraft (Standard)]] formats — grounded
in what specific analysts actually said, with dates and citations.

See [CLAUDE.md](CLAUDE.md) for the schema and workflows. See [log.md](log.md)
for the chronological record of ingests, queries, and lints.

---

## Layers

| Layer | Location | Owner |
|---|---|---|
| **Raw sources** | `raw/transcripts/` (queue)<br>`raw/ingested/` (done) | Contents immutable. Only permitted change is moving between the two trees on ingestion. |
| **Wiki** | `wiki/` | LLM-owned. Created, updated, cross-referenced. |
| **Schema** | `CLAUDE.md` | Conventions + workflows. |

---

## Experts

| Page | Show | Focus |
|---|---|---|
| [[Chris Harris]] | Harris Fantasy Football Podcast | Daily in-season analysis, rankings, Almanac |
| [[Matt Harmon]] | Reception Perception: The Show | WR charting, alignment-based evaluation |
| [[Matt Waldman]] | Matt Waldman's RSP Cast | Film-based rookie/prospect scouting, dynasty |

## Formats

| Page | Priority | Notes |
|---|---|---|
| [[Best Ball]] | 1 (highest) | Ceiling/variance over floor; no in-season management |
| [[Dynasty]] | 2 | Age curves, draft capital, long-term role |
| [[Redraft (Standard)]] | 3 | Current-year role, waivers, start/sit |

## Players

### Quarterbacks
- [[Jake Browning]] — QB, CIN — streamable low-end QB1 on his 2023 run; strong middle-of-field/timing thrower, no off-platform deep ball *(2023 takes, stale)*
- [[Baker Mayfield]] — QB, TB — Waldman expected Tampa to re-sign him for 2024; "like what he's doing within his capabilities," Geno Smith leap possible *(2023 takes, stale)*
- [[C.J. Stroud]] — QB, HOU — talent real, but both hosts credit part of the production to the Shanahan-tree system around him *(2023 takes, stale)*
- [[Lamar Jackson]] — QB, BAL — Waldman's contrarian call: the *most* scheme-dependent of the top QBs; limited outside the numbers, not a knock on talent *(2023 takes, stale)*
- [[Brock Purdy]] — QB, SF — not a system QB per Waldman; in-structure processing travels, and 9.88 Y/A vs Garoppolo in the same offense *(2023 takes, stale)*
- [[Kyler Murray]] — QB, ARI — one narrow knock: bails the pocket on proximity, "runs as if a bomb has blown up" when anyone gets within three yards *(2023 takes, stale)*
- [[Drew Lock]] — QB, SEA — the wiki's case study in coachability; "surface level" game, a missed Peyton Manning lifeline, now a solid long-term backup *(2023 takes, stale)*
- [[Gardner Minshew]] — QB, IND — the model backup: knows exactly who he is, executes schematically, doesn't lose you games *(2023 takes, stale)*

### Running Backs
- [[Christian McCaffrey]] — RB, SF — unqualified 1.01 for 2024; age 28 explicitly dismissed; the "leverage over the field" case *(2023 takes, stale)*
- [[Bijan Robinson]] — RB, ATL — Waldman's 2024 table-pounder *because* the market moved to Gibbs; Bob Harris expects top-5 *(2023 takes, stale)*
- [[Jahmyr Gibbs]] — RB, DET — Waldman's 2023 call, vindicated (RB9); he then flips off him for 2024 on price, not talent *(2023 takes, stale)*
- [[James Cook]] — RB, BUF — "elite" question answered yes; 2023 read as an acclimation year; floated as the next Ekler *(2023 takes, stale)*
- [[Tyler Goodson]] — RB, IND — explosive, natural cutback runner masked by Iowa's scheme; Waldman's long-term Colts preference *(2023 takes, stale)*
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, HOU — had taken the job outright from Dameon Pierce; 26 carries to 1 *(2023 takes, stale)*
- [[Saquon Barkley]] — RB, NYG — valuable, but the last of the space-expensive jump-cut runners; inefficient play-to-play on film *(2023 takes, stale)*
- [[Derrick Henry]] — RB, TEN — "a one of one" and unreplicable, but now with a real knock: once a defense keys him "you're not fixing it mid-game," and linebackers find the small movers harder to tackle *(2023 takes, stale)*
- [[Breece Hall]] — RB, NYJ — "averts one disaster at a time"; processes fast but not two steps ahead, and Waldman still expects big-time yardage with a better line *(2023 takes, stale)*
- [[Nick Chubb]] — RB, CLE — the big back who beats the size rule; best ever at re-accelerating post-contact, "Hall of Fame caliber talent," 2023 knee injury the live question *(2023 takes, stale)*
- [[David Montgomery]] — RB, DET — the low-variance half of the Detroit committee; "very rarely will break a 25-plus-yard run" *(2023 takes, stale)*
- [[Isiah Pacheco]] — RB, KC — the pace-control negative case: one speed, "zero or a hundred" *(2023 takes, stale)*

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — "one of the best three route runners in the NFL"; backup QB costs him a tier, not a start *(2023 takes, stale)*
- [[Ja'Marr Chase]] — WR, CIN — QB-proof ("still going to be Ja'Marr Chase"); AC joint injury was the only live question *(2023 takes, stale)*
- [[Keenan Allen]] — WR, LAC — top-5 WR without speed: beats man *and* zone, plays inside and outside *(2023 takes, stale)*
- [[Amon-Ra St. Brown]] — WR, DET — same profile as Allen, with play-caller continuity as the tiebreaker *(2023 takes, stale)*
- [[Brandon Aiyuk]] — WR, SF — best route runner in San Francisco and a WR1 bet at a bargain price *(2023 takes, stale)*
- [[Tee Higgins]] — WR, CIN — WR21 since Browning took over, but boom/bust without Burrow's moving deep ball *(2023 takes, stale)*
- [[Jordan Addison]] — WR, MIN — rotation promotion missed by box-score watchers; top-15 ceiling, one tier off with Mullens *(2023 takes, stale)*
- [[Jayden Reed]] — WR, GB — Allen/St. Brown route-running mold *with* speed; outcome depends on the offense *(2023 takes, stale)*
- [[Noah Brown]] — WR, HOU — best Texans receiver whenever Nico Collins is out; a conditional weekly start *(2023 takes, stale)*
- [[Tre Tucker]] — WR, LV — "aspiring Jaylen Waddle" in the Tyreek Hill role; high variance, not yet a complete player *(2023 takes, stale)*
- [[Treylon Burks]] — WR, TEN — talent to be mined, still a work in progress; one big game wasn't a role *(2023 takes, stale)*
- [[DeAndre Hopkins]] — WR, TEN — the "old man game" archetype; experts split on how much tail is left *(2023 takes, stale)*
- [[Adam Thielen]] — WR, CAR — reputation as a possession receiver misreads a genuinely elite athletic profile *(2023 takes, stale)*
- [[Deebo Samuel]] — WR, SF — elite vs zone and as a gadget runner, "not remotely as good" vs man; his value may not survive a team change *(2023 takes, stale)*
- [[Malik Nabers]] — WR, LSU prospect — both *Going Deep* hosts take him over Marvin Harrison Jr. "by a healthy margin" on pro-readiness; 1,100/10 rookie projection *(2023 pre-draft takes, stale)*
- [[Marvin Harrison Jr.]] — WR, Ohio State prospect — higher ceiling, longer runway; three correctable technique flags (releases, catch windows, underhand default) and "not as good a player as he is a prospect" *(2023 pre-draft takes, stale)*

### Tight Ends
- [[T.J. Hockenson]] — TE, MIN — great in zone, positions well in man; TE1 ceiling minus a tier with a backup QB *(2023 takes, stale)*
- [[Sam LaPorta]] — TE, DET — Waldman's own miss: needed the perfect fit and found it; the value here is the organizational-floor reasoning, not the ranking *(2023 takes, stale)*

<!-- Claude: maintain grouped by position (QB / RB / WR / TE), each with a
     one-line summary. See CLAUDE.md "Index maintenance". -->

## Concepts

- [[Aging Curves and Career Longevity]] — 30+ production collapsed league-wide since ~2017; cause unknown. Core [[Dynasty]] input. Waldman declines to apply it to elite individuals (McCaffrey at 28).
- [[Start Your Best Players]] — start top-down off your own rankings rather than chasing weekly matchups
- [[Scouting Bias and Player Archetypes]] — archetype labels track appearance/pedigree more than measured traits, and leak into ADP
- [[Weak Quarterback Play and Receiver Value]] — managers over-discount receivers for bad QBs; discount the *throws he can't make*, not the name
- [[Zone vs Man Route Running]] — beating man and beating zone are separate skills; doing both (not speed) is Waldman's top-WR marker
- [[Scheme vs Talent]] — how much production belongs to the system; Houston as the test case, plus the league-wide swing between talent-centric and scheme-centric eras (Dec 2023 read: talent-centric) and why "system quarterback" is a bad label
- [[Running Back Size and Movement Skills]] — change of direction in tight space as the RB separator, and the claimed ~205–215 lb ceiling on the trait (originally Brandon Angelo's argument); Nick Chubb is the standing counter-example
- [[League Trend Cycles and Market Inefficiency]] — NFL trends are cyclical, not progressive; the edge belongs to whoever zags while a trend is crowded
- [[NIL and Player Development]] — whether paid college players thin rookie classes or force the NFL to develop players; Angelo expects a chain reaction and older prospects, Harstad expects mostly nothing
- [[Pace Control and Movement Intellect]] — controlling your own gears and gauging everyone else's; the cross-positional sibling of the RB size argument, and why single-speed runners get corralled
- [[Prospect Pro-Readiness vs Ceiling]] — how much of a rookie's game transfers on day one, graded separately from how good he'll eventually be; Nabers vs Harrison Jr. as the worked example
- [[Player Development and Coachability]] — whether the player will accept coaching and whether the building can give it; why a prospect's floor is usually organizational

<!-- Claude: one line per concept page with a short definition. -->

## Synthesis

Filed answers to recurring draft/waiver questions — comparisons and tiers that
accumulate rather than being re-derived each time.

*No synthesis pages yet.*

<!-- Claude: one line per synthesis page, with the question it answers and the
     date last refreshed. -->

## Sources

Per-episode summary pages live in `wiki/sources/`. The full catalog with
ingestion status is tracked in `scripts/state.json`; see
[SOURCE_CATALOG](wiki/sources/SOURCE_CATALOG.md) for the human-readable list.

---

## Pipeline status

Transcription and ingestion progress is tracked in `scripts/state.json`.

- `pending` — episode known from RSS, not yet transcribed
- `fetched` — transcript in `raw/transcripts/`, awaiting ingestion
- `ingested` — woven into the wiki; transcript moved to `raw/ingested/`

Run `python3 scripts/verify_integrity.py` to reconcile state against disk.

Source-acquisition failures are logged to [raw/_needs-attention.md](raw/_needs-attention.md).
