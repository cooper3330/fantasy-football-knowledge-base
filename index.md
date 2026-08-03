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
- [[C.J. Stroud]] — QB, HOU — talent real, both hosts credit part of the production to the Shanahan-tree system; 2024 mid-round tiebreaker vs. Purdy hinges on Tank Dell's health *(2024 takes, stale)*
- [[Lamar Jackson]] — QB, BAL — Waldman's contrarian call: the *most* scheme-dependent of the top QBs, not a knock on talent; unqualified 2024 QB1 for both hosts regardless *(2024 takes, stale)*
- [[Brock Purdy]] — QB, SF — not a system QB per Waldman; both hosts lean Purdy over Stroud for 2024; Waldman's career-arc forecast comps him to early Brady/Warner/Wilson/Roethlisberger *(2024 takes, stale)*
- [[Kyler Murray]] — QB, ARI — one narrow knock: bails the pocket on proximity, "runs as if a bomb has blown up" when anyone gets within three yards *(2023 takes, stale)*
- [[Drew Lock]] — QB, SEA — the wiki's case study in coachability; "surface level" game, a missed Peyton Manning lifeline, now a solid long-term backup *(2023 takes, stale)*
- [[Gardner Minshew]] — QB, IND — the model backup: knows exactly who he is, executes schematically, doesn't lose you games *(2023 takes, stale)*
- [[Anthony Richardson]] — QB, IND — unqualified top-12 QB call for 2024 from both hosts, "100%," on film upside alone *(2024 takes, stale)*
- [[Joe Flacco]] — QB, CLE — 2023 turnaround credited to O-line coach Tom Cable and Stefanski's scheme more than to Flacco himself; praised on film for spreading the field and as a locker-room steadying force *(2024 takes, stale)*
- [[Jordan Love]] — QB, GB — Harstad's case study in overreacting to young QBs on small samples; Waldman credits Green Bay's patient development runway *(2024 takes, stale)*
- [[Dak Prescott]] — QB, DAL — "a good quarterback... when you give him the talent, he can give you elite production"; a boom/bust "prevailing wind" player, helped by the McCarthy scheme fit *(2024 takes, stale)*

### Running Backs
- [[Christian McCaffrey]] — RB, SF — unqualified 2024 1.01 for Waldman again, edging [[CeeDee Lamb]] and [[Tyreek Hill]]; age 28 explicitly dismissed; the "leverage over the field" case *(2024 takes, stale)*
- [[Bijan Robinson]] — RB, ATL — Waldman's 2024 table-pounder *because* the market moved to Gibbs; Bob Harris expects top-5; reaffirmed post-Arthur-Smith as a bell-cow workload bet *(2024 takes, stale)*
- [[Jahmyr Gibbs]] — RB, DET — Waldman's 2023 call, vindicated (RB9); he then flips off him for 2024 on price, not talent *(2023 takes, stale)*
- [[James Cook]] — RB, BUF — "elite" question answered yes; fully unleashed in year two, "a real shot" at top-12 value in 2024, floated as the next Ekeler *(2024 takes, stale)*
- [[Tyler Goodson]] — RB, IND — explosive, natural cutback runner masked by Iowa's scheme; Waldman's long-term Colts preference *(2023 takes, stale)*
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, HOU — had taken the job outright from Dameon Pierce; 26 carries to 1 *(2023 takes, stale)*
- [[Saquon Barkley]] — RB, NYG — valuable, but the last of the space-expensive jump-cut runners; inefficient play-to-play on film *(2023 takes, stale)*
- [[Derrick Henry]] — RB, TEN — "a one of one" and unreplicable, with a real knock (defenses key him and it sticks); wouldn't draft as RB1 for 2024, wants him as a cheap "dead zone" back and is rooting for a Ravens landing spot *(2024 takes, stale)*
- [[Breece Hall]] — RB, NYJ — "averts one disaster at a time"; processes fast but not two steps ahead, and Waldman still expects big-time yardage with a better line *(2023 takes, stale)*
- [[Nick Chubb]] — RB, CLE — the big back who beats the size rule; best ever at re-accelerating post-contact, "Hall of Fame caliber talent," 2023 knee injury the live question *(2023 takes, stale)*
- [[David Montgomery]] — RB, DET — the low-variance half of the Detroit committee; "very rarely will break a 25-plus-yard run" *(2023 takes, stale)*
- [[Isiah Pacheco]] — RB, KC — the pace-control negative case: one speed, "zero or a hundred" *(2023 takes, stale)*
- [[Kyren Williams]] — RB, LAR — sub-top-10 talent, top-10 production off the Rams' line and scheme; Waldman's 2024 RB1, contingent on the coaching staff/line and no free-agent power-back addition *(2024 takes, stale)*
- [[Kenneth Walker III]] — RB, SEA — Waldman draft him higher than market: Pete Carroll's pattern is to "covet" one back until injury forces a change, and Walker is currently that back *(2024 takes, stale)*
- [[Raheem Mostert]] — RB, MIA — the cheap half of Miami's committee; both hosts value him as a 2024 RB2, expect more work to shift to Achane *(2024 takes, stale)*
- [[James Connor]] — RB, ARI — both hosts hanging on for 2024; "toast" skepticism reframed as a second-contract finance story, not a talent decline; Michael Carter cuts into but doesn't replace him *(2024 takes, stale)*
- [[Aaron Jones]] — RB, GB — "injury agnostic, not stupid": still playable, price-sensitive given his injury history *(2024 takes, stale)*
- [[Zamir White]] — RB, LV — the industry's hottest 2024 sleeper name per Waldman, who flags his own overhype risk; tied to Antonio Pierce keeping his job; a clear RB2 behind a Jacobs-elsewhere RB1 ceiling *(2024 takes, stale)*
- [[Tank Bigsby]] — RB, JAX — overrated by "about a round and a half" pre-draft per Waldman; costly drops, indecisive runner; opportunity would still get him 1,000 yards *(2024 takes, stale)*
- [[Kendre Miller]] — RB, NO — Waldman's preferred dynasty stash over Bigsby, on opportunity alone *(2024 takes, stale)*
- [[Chase Brown]] — RB, CIN — "I love Chase Brown"; Waldman's other preferred dynasty stash over Bigsby *(2024 takes, stale)*
- [[Tony Pollard]] — RB, DAL — real rebound odds for 2024 if his 2023 injuries (not talent) explain the down year; McCarthy's usage was the wrong fit regardless *(2024 takes, stale)*
- [[Michael Carter]] — RB, ARI — "a pretty damn good back" who should cut into James Connor's 2024 workload, receiving skills underused so far *(2024 takes, stale)*
- [[Austin Ekeler]] — RB, LAC — possible 2024 rebound, but Waldman wouldn't personally invest; may be closer to the end than the industry realizes *(2024 takes, stale)*
- [[Josh Jacobs]] — RB, LV — "easily" the best free-agent candidate to become the next James Connor; the better back in a direct comparison with Zamir White *(2024 takes, stale)*
- [[Jordan Mason]] — RB, SF — Waldman's preferred McCaffrey-injury contingency over Elijah Mitchell, on versatility and price *(2024 takes, stale)*
- [[Elijah Mitchell]] — RB, SF — got more 2023 volume than Mason down the stretch, but still Waldman's #2 McCaffrey handcuff on price *(2024 takes, stale)*
- [[Tyler Allgeier]] — RB, ATL — Bijan Robinson's complementary piece; "plays really well when in the system they put him in" *(2024 takes, stale)*

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — "one of the best three route runners in the NFL"; backup QB costs him a tier, not a start *(2023 takes, stale)*
- [[Ja'Marr Chase]] — WR, CIN — QB-proof ("still going to be Ja'Marr Chase"); AC joint injury was the only live question *(2023 takes, stale)*
- [[Keenan Allen]] — WR, LAC — top-5 WR without speed: beats man *and* zone, plays inside and outside *(2023 takes, stale)*
- [[Amon-Ra St. Brown]] — WR, DET — same profile as Allen, with play-caller continuity as the tiebreaker *(2023 takes, stale)*
- [[Brandon Aiyuk]] — WR, SF — best route runner in San Francisco and a WR1 bet at a bargain price *(2023 takes, stale)*
- [[Tee Higgins]] — WR, CIN — WR21 since Browning took over, but boom/bust without Burrow's moving deep ball *(2023 takes, stale)*
- [[Jordan Addison]] — WR, MIN — rotation promotion missed by box-score watchers; Waldman's #2 2023 rookie WR, "a better version of Devonta Smith"; ceiling is a Minnesota-QB question *(2024 takes, stale)*
- [[Jayden Reed]] — WR, GB — Allen/St. Brown route-running mold *with* speed; Waldman wouldn't trade him for any other 2023 rookie WR, Diggs upside/Coles floor *(2024 takes, stale)*
- [[Noah Brown]] — WR, HOU — best Texans receiver whenever Nico Collins is out; a conditional weekly start *(2023 takes, stale)*
- [[Tre Tucker]] — WR, LV — "aspiring Jaylen Waddle" in the Tyreek Hill role; high variance, not yet a complete player *(2023 takes, stale)*
- [[Treylon Burks]] — WR, TEN — talent to be mined, still a work in progress; one big game wasn't a role *(2023 takes, stale)*
- [[DeAndre Hopkins]] — WR, TEN — the "old man game" archetype; experts split on how much tail is left *(2023 takes, stale)*
- [[Adam Thielen]] — WR, CAR — reputation as a possession receiver misreads a genuinely elite athletic profile *(2023 takes, stale)*
- [[Deebo Samuel]] — WR, SF — elite vs zone and as a gadget runner, "not remotely as good" vs man; his value may not survive a team change *(2023 takes, stale)*
- [[Malik Nabers]] — WR, LSU prospect — both *Going Deep* hosts take him over Marvin Harrison Jr. "by a healthy margin" on pro-readiness; 1,100/10 rookie projection *(2023 pre-draft takes, stale)*
- [[Marvin Harrison Jr.]] — WR, Ohio State prospect — higher ceiling, longer runway; three correctable technique flags (releases, catch windows, underhand default) and "not as good a player as he is a prospect" *(2023 pre-draft takes, stale)*
- [[CeeDee Lamb]] — WR, DAL — Bob Harris's pick for 2024 #1 overall over McCaffrey; Waldman ranks him 2nd *(2024 takes, stale)*
- [[Tyreek Hill]] — WR, MIA — 3rd in Waldman's 2024 top tier, but Bob Harris's personal #2 as "an old-school wide receiver one" *(2024 takes, stale)*
- [[Mike Evans]] — WR, TB — 11 straight 1,000-yard seasons; 2024 outlook is pure situation — cheap and startable if he stays in Tampa with Baker Mayfield, cautious if he leaves *(2024 takes, stale)*
- [[Stefon Diggs]] — WR, BUF — Bob Harris's instant no; Waldman sees 2024 value if he falls to the 2nd/3rd-round turn, with a Gabe Davis-shaped caution *(2024 takes, stale)*
- [[Cooper Kupp]] — WR, LAR — not hung up, but Puka Nacua's emergence caps his ceiling; "days of being that true alpha... are over, draft accordingly" *(2024 takes, stale)*
- [[Quentin Johnston]] — WR, LAC — the 2023 rookie class's clearest bust risk so far; a route-runner without a catch-point, better projected as a slot piece than the outside role he was drafted for *(2024 takes, stale)*
- [[Jaxon Smith-Njigba]] — WR, SEA — Waldman's #1 2023 rookie WR despite thin volume; built as the season went on *(2024 takes, stale)*
- [[Zay Flowers]] — WR, BAL — in Waldman's top rookie WR tier but more boom/bust, entirely on how much Lamar Jackson's offense trusts him *(2024 takes, stale)*
- [[Puka Nacua]] — WR, LAR — Waldman's #3 2023 rookie WR, #1 by pure production; long-term outlook tied to Stafford's remaining runway *(2024 takes, stale)*
- [[Tank Dell]] — WR, HOU — just outside Waldman's top-5 rookie WRs; Harstad's counter-read is he's inflated by Nico Collins drawing tougher coverage *(2024 takes, stale)*
- [[Nico Collins]] — WR, HOU — Harstad's "doing the harder thing" pick — harder to replace in Houston's offense than Tank Dell *(2024 takes, stale)*
- [[Josh Downs]] — WR, IND — "certainly going to be worthwhile" once Anthony Richardson is back and healthy *(2024 takes, stale)*
- [[Marvin Mims Jr.]] — WR, DEN — underused rookie year per Waldman; profile fits a Sean Payton deep-threat role once friction resolves *(2024 takes, stale)*
- [[Jalen Hyatt]] — WR, NYG — Waldman "a little more convinced" despite a bad Giants QB situation *(2024 takes, stale)*
- [[Rashee Rice]] — WR, KC — Waldman withholds judgment; role reads more Skyy Moore-style underneath than his pre-draft outside profile, Mahomes-inflation caution *(2024 takes, stale)*
- [[Gabe Davis]] — WR, BUF — "a good football player," but the boom/bust role (not the talent) is the problem; expected to leave Buffalo in free agency *(2024 takes, stale)*
- [[Khalil Shakir]] — WR, BUF — "65% feeling it" as a 2024 starter inheriting Gabe Davis's role; only question is role overlap with Kincaid *(2024 takes, stale)*
- [[Drake London]] — WR, ATL — top-15 value in play for 2024 once Atlanta hires a real coach/QB; cheaper price, but not that cheap given industry consensus *(2024 takes, stale)*
- [[Michael Wilson]] — WR, ARI — a genuinely good route runner in the "aspiring Michael Thomas" mold; top-24 value if he can finally stay healthy *(2024 takes, stale)*
- [[Wan'Dale Robinson]] — WR, NYG — real after-the-catch and contested-catch value; outlook entirely a Giants-QB question *(2024 takes, stale)*
- [[Ronnie Bell]] — WR, SF — a name to know mostly for injury-contingency reasons behind Aiyuk/Deebo, not his own emergence *(2024 takes, stale)*
- [[Dontayvion Wicks]] — WR, GB — "turned some heads"; catch-point toughness threatens to bump Doubs or an injury-prone Watson out of the fantasy-relevant mix *(2024 takes, stale)*
- [[Romeo Doubs]] — WR, GB — part of Green Bay's "big three," but "a little less multi-dimensional" than what Wicks offers *(2024 takes, stale)*
- [[Christian Watson]] — WR, GB — speed is unquestioned; durability is the entire 2024 question mark *(2024 takes, stale)*

### Tight Ends
- [[T.J. Hockenson]] — TE, MIN — great in zone, positions well in man; TE1 ceiling minus a tier with a backup QB *(2023 takes, stale)*
- [[Travis Kelce]] — TE, KC — his first-round-pick days are over per Waldman; a nagging early-2023 injury may have lingered all year *(2024 takes, stale)*
- [[Sam LaPorta]] — TE, DET — Waldman's own miss: needed the perfect fit and found it; outproduced Kincaid as a rookie, still a top-5 dynasty TE in his tier *(2024 takes, stale)*
- [[Dalton Kincaid]] — TE, BUF — Waldman's stated long-term preference over LaPorta despite being outproduced as a rookie; a top-5 2024 TE call in an offense he says can support three fantasy starters *(2024 takes, stale)*
- [[Luke Musgrave]] — TE, GB — Waldman's pre-draft 7th-ranked TE, now sees as "slightly overrated" relative to teammate Tucker Kraft *(2024 takes, stale)*
- [[Tucker Kraft]] — TE, GB — the value pick of Green Bay's two rookie tight ends per Waldman — more rugged, more room to grow, and cheaper on his board *(2024 takes, stale)*

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
- [[Injury-Agnostic Roster Construction]] — draft assuming everyone eventually gets hurt and price/plan for the loss, rather than avoiding injury-flagged players; "injury agnostic, not stupid"
- [[Role Difficulty and Replaceability]] — prefer the receiver doing the harder assignment over the one whose easier usage produces similar numbers; the replaceability test
- [[Healthy Enough to Play vs. Healthy Enough to Perform]] — a disappointing "healthy" season is often explained by clearing the bar to suit up, not the bar to perform at draft-day level

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
