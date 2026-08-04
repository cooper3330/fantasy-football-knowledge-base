---
type: index
tags: [index]
---

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
| [[Matt Harmon]] | Reception Perception: The Show | WR charting (success rate vs. man/zone/press), general NFL analysis with James Koh |
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
- [[Baker Mayfield]] — QB, TB — both hosts now bullish on a Tampa re-sign; "Pro Bowl level Jeff Garcia" season, mature version of his rookie-year traits; Harmon more skeptical — "streaky," career ceiling "lower than the 20th-best QB," but agrees he should stay in Tampa Bay rather than face a 7th head coach; new OC Liam Coen (a Mayfield-approved former Rams assistant) resolves the Dave-Canales-departure question, but Waldman's "totally feeling it" 2024 outlook is explicitly conditioned on Mike Evans and Chris Godwin both staying too *(2024 takes, stale)*
- [[Justin Fields]] — QB, CHI — Waldman's best-outcome pick is Atlanta or Pittsburgh once Chicago moves on for Caleb Williams; more sophisticated coverage-reading decision-maker than Desmond Ridder was in Atlanta's 2023 offense *(2024 takes, stale)*
- [[Derek Carr]] — QB, NO — 2023's rough start traced to left tackle Trevor Penning's play, not Carr himself; strong finish once protection was fixed (3+ TD games in 5 of 6 late-season outings); cheap streaming/QB2 value if the Saints add a receiver *(2024 takes, stale)*
- [[Justin Herbert]] — QB, LAC — Waldman's history-based case that new OC Greg Roman/HC Jim Harbaugh won't cap him despite their run-heavy reputation; projects a more efficient "dink and dunk" ~3,300-3,500 yards, 30+ TD ceiling that specifically benefits Keenan Allen *(2024 takes, stale)*
- [[Russell Wilson]] — QB, DEN — hedged outlook; likely a 2024 Week 1 starter but doubtful long-term; Waldman partially disputes a harsher outside read (Dwain McFarland) that Cover-2-high defenses ended his career, pointing instead to a weak Denver receiving corps; Pittsburgh or a Deshaun-Watson-replacing Cleveland floated as fits *(2024 takes, stale)*
- [[C.J. Stroud]] — QB, HOU — talent real, both hosts credit part of the production to the Shanahan-tree system; Harmon/Koh call him an easy top-5 NFL QB after a Wild Card clinic on Cleveland; looked like a rookie with no counterpunch once Baltimore took Nico Collins away in the Divisional Round, the first real bad game logged; 2024 mid-round tiebreaker vs. Purdy hinges on Tank Dell's health *(2024 takes, stale)*
- [[Jared Goff]] — QB, DET — Harmon's direct ceiling comp for Tua: "somewhere" top-11-14, stronger arm than Tua; the "what happens once Ben Johnson leaves" question is resolved — Johnson turned down every HC opening, including Washington, and is staying in Detroit; Harmon's sharper follow-up: "there is a level where Jared Goff cannot take you much further," with a clear remaining team need at X receiver *(2024 takes, stale)*
- [[Lamar Jackson]] — QB, BAL — Waldman's contrarian call: the *most* scheme-dependent of the top QBs, not a knock on talent; unqualified 2024 QB1 for both hosts regardless; after the AFC Championship loss, Waldman expects him to supplant Mahomes as 2024 redraft QB2 (maybe QB1), with real year-two growth expected once Monken's offense and a gutted receiver room get an offseason to heal — but Harmon's harder-nosed recap of the same game logs 3 turnover-worthy throws and a near-total run-game abandonment (563rd-of-568 design-run rate), opening an unresolved "are playoff losses mounting" question even while still calling him a top-three QB outright *(2024 takes, stale)*
- [[Patrick Mahomes]] — QB, KC — Waldman's 2024 redraft value call: pushed down boards by Jackson (and maybe Hurts) but won't fall past QB4-5, a real value gap between cost and rank; post-Super-Bowl-LVIII framework — "a wiser Brett Favre," sees through scheme and adapts with far fewer era-defining mistakes *(2024 takes, stale)*
- [[Jalen Hurts]] — QB, PHI — only introduced as the Lamar Jackson value comparison; Philadelphia's Kellen Moore OC hire now has a first grade from Harmon — "definitely an upgrade" over Brian Johnson but "something left to be desired," with a specific worry about how shotgun-exclusive Hurts's usage has become *(2024 takes, stale)*
- [[Brock Purdy]] — QB, SF — not a system QB per Waldman; both hosts lean Purdy over Stroud for 2024; Waldman's career-arc forecast comps him to early Brady/Warner/Wilson/Roethlisberger; Waldman: "exposed as nothing other than what he is" after the Divisional Round win, early ECR outside the top-12 called "a mistake"; Harmon disagrees on that same game — an explicit "bad game," good but "top 20," not elite-tier; Waldman's counter after the NFC Championship win — "subtle skills," carried further by a stacked supporting cast, real front-office skittishness risk if SF doesn't win the Super Bowl *(2024 takes, stale)*
- [[Kyler Murray]] — QB, ARI — one narrow knock: bails the pocket on proximity, "runs as if a bomb has blown up" when anyone gets within three yards *(2023 takes, stale)*
- [[Drew Lock]] — QB, SEA — the wiki's case study in coachability; "surface level" game, a missed Peyton Manning lifeline, now a solid long-term backup *(2023 takes, stale)*
- [[Gardner Minshew]] — QB, IND — the model backup: knows exactly who he is, executes schematically, doesn't lose you games *(2023 takes, stale)*
- [[Anthony Richardson]] — QB, IND — unqualified top-12 QB call for 2024 from both hosts, "100%," on film upside alone *(2024 takes, stale)*
- [[Joe Flacco]] — QB, CLE — 2023 turnaround credited to O-line coach Tom Cable and Stefanski's scheme more than to Flacco himself; ran the Cleveland offense better than Watson has, but expected to hit the veteran-backup market after the Wild Card exit *(2024 takes, stale)*
- [[Jordan Love]] — QB, GB — Harstad's case study in overreacting to young QBs on small samples; after the Wild Card demolition of Dallas, Harmon says he wouldn't take 10 other QBs over him given age/contract; Waldman defends the Divisional Round pick as growing pains, calls him a 2024 value target *(2024 takes, stale)*
- [[Dak Prescott]] — QB, DAL — "a good quarterback... when you give him the talent, he can give you elite production"; a boom/bust "prevailing wind" player, helped by the McCarthy scheme fit; Harmon reads the Wild Card blowout loss as having hit his ceiling relative to Jordan Love *(2024 takes, stale)*
- [[Bryce Young]] — QB, CAR — Harmon declines to call the bad rookie year settled — no functional line, weapons, or play-calling in Carolina; real physical limits (below-average arm, undersized, limited elusiveness) mean accuracy/processing is his only real path; new HC Dave Canales graded as the right guy to get a fair year-two evaluation *(2024 takes, stale)*
- [[Michael Penix Jr.]] — QB, Washington prospect — talent real, but outlook dominated by injury history; downgraded to "journeyman starter" tier on accuracy concerns, wanted him higher; Waldman's updated call is medical-contingent — "if he checks out medically, he's probably a top-20, top-25 pick," still among his top-5 QBs in the class; reverses back upward three weeks later — now Waldman's top outlier-QB pick in the class, pushing back on outside "not good under pressure" critiques *(2024 pre-draft takes, stale)*
- [[Tua Tagovailoa]] — QB, MIA — a genuine anticipation/timing thrower who can be schemed into big windows, but a weak post-snap reader who struggles once those windows disappear; Harmon calls a Wild Card loss at KC "straight up bad," ceiling below Jared Goff's *(2024 takes, stale)*
- [[Drake Maye]] — QB, North Carolina prospect — Harms's strong buy on lower-body pocket mechanics/pressure sense ("spidey sense"); Waldman disagrees, more skeptical — "my Desmond Ritter of this class," box-score accuracy not matching the film; Waldman's re-watch reinforces it — new Jake Locker comp, plus a structural North Carolina-QB-archetype risk (Trubisky, Howell, Maye) that's flagged independent of individual talent *(2024 pre-draft takes, stale)*
- [[Bo Nix]] — QB, Oregon prospect — Harms's skeptical outlier take (Oregon's one-read system); Waldman disagrees, possibly top 3-4 in the class; Angelo now splits with Waldman too after watching him live at the Senior Bowl — "Mitch Trubisky syndrome," borderline contributor/emergency-starter grade — leaving a live 3-way disagreement *(2024 pre-draft takes, stale)*
- [[Caleb Williams]] — QB, USC prospect — still the top 2024 QB prospect, but "the most boom-bust top prospect... in a few years"; won't check the ball down, Aaron Rodgers ceiling vs. Jay Cutler/Drew Lock floor; Waldman independently corroborates; a Cliff-Kingsbury-to-Washington trade-up scenario worries Waldman it's "the worst end of Caleb Williams to start his career" — more Kyler-Murray-esque instability than structured football; explicit verdict on the mock-draft top-3 — "hell no" all three (with Maye/Daniels) hit their draft capital, "most likely only one" does, and Williams is that one *(2024 pre-draft takes, stale)*
- [[Jayden Daniels]] — QB, LSU prospect — Waldman's floor is a second-contract starter with real upside; a lesser Lamar Jackson comp *(2024 pre-draft takes, stale)*
- [[J.J. McCarthy]] — QB, Michigan prospect — coordinated athlete, whip arm, flashes elite leverage reads; outcome hinges on decisiveness (Mayfield/Alex Smith floor vs. Mahomes ceiling); both hosts admit they had Will Levis ungraded pre-draft and now use his rookie year as McCarthy's floor/median comp — Angelo grades McCarthy "a tier higher" than Levis, on the "Mason-Dixon line" between contributor and reserve *(2024 pre-draft takes, stale)*
- [[Spencer Rattler]] — QB, South Carolina prospect — better tape at South Carolina than Oklahoma per Waldman, moves better in the pocket than expected; strong vs. one of man/zone, poor vs. the other — "half a game" right now; Angelo's Senior Bowl take adds a real maturity/coachability angle — self-aware about a cocky younger self — on a mixed on-field week *(2024 pre-draft takes, stale)*
- [[Tanner Mordecai]] — QB, Wisconsin prospect (SMU/Oklahoma transfer) — rocky transfer-year tape, rebounded late vs. LSU; Waldman's grade is future backup of value, not a starter *(2024 pre-draft takes, stale)*
- [[Jack Plummer]] — QB, Louisville prospect — accuracy is the whole story per Waldman: "if he had the accuracy, he would probably be a top-five quarterback in this class" *(2024 pre-draft takes, stale)*
- [[Joe Milton III]] — QB, Tennessee prospect — the class's clearest boom/bust arm-talent case; top-five-pick ceiling, out-of-the-league floor; Malik Willis comp, explicit "Jordan Love treatment" recommended by Waldman *(2024 pre-draft takes, stale)*
- [[Desmond Ridder]] — QB, ATL — the mechanism Waldman blames for Atlanta's 2023 passing-game struggles: couldn't read the field dynamically between zones, forcing Arthur Smith into a simplified, static route scheme; real doubt he keeps the 2024 starting job *(2024 takes, stale)*
- [[Kirk Cousins]] — QB, MIN — both hosts feel it on staying in Minnesota, "another year or two" before any QB draft pick takes over; standing double-digit-round redraft value coming off a torn Achilles *(2024 takes, stale)*
- [[Daniel Jones]] — QB, NYG — flat "not the answer" per Waldman; expects a two-step Giants succession (a developmental pick first, a real QB1 pick once they're ready to move on) rather than an immediate bench *(2024 takes, stale)*
- [[Ryan Tannehill]] — QB, TEN — speculative Pittsburgh reunion with former OC Arthur Smith; projected as a Joe-Flacco-style veteran room presence, not a starter bet *(2024 takes, stale)*
- [[Aaron Rodgers]] — QB, NYJ — both hosts feel it on a return to form post-Achilles; intangible/effort-based case ("too obsessed with the game") rather than tape-based *(2024 takes, stale)*
- [[Matthew Stafford]] — QB, LAR — Waldman comps his ball placement to 'Mahomes 1.0'; less mobile, more mistake-prone
- [[Joe Burrow]] — QB, CIN — Waldman 'Goldilocks' on QB7 best ball ADP; top-3 QB talent when healthy

### Running Backs
- [[Christian McCaffrey]] — RB, SF — unqualified 2024 1.01 for Waldman again, edging [[CeeDee Lamb]] and [[Tyreek Hill]]; age 28 explicitly dismissed; the "leverage over the field" case; Harmon: even a strong Detroit run defense "isn't stopping that train" in the NFC Championship *(2024 takes, stale)*
- [[Bijan Robinson]] — RB, ATL — Waldman's 2024 table-pounder *because* the market moved to Gibbs; Bob Harris expects top-5; reaffirmed post-Arthur-Smith as a bell-cow workload bet; new OC Zach Robinson (ex-Rams) projected by Harmon as a good man/gap-run scheme fit *(2024 takes, stale)*
- [[Jahmyr Gibbs]] — RB, DET — Waldman's 2023 call, vindicated (RB9); he then flips off him for 2024 on price, not talent *(2023 takes, stale)*
- [[James Cook]] — RB, BUF — "elite" question answered yes; fully unleashed in year two, "a real shot" at top-12 value in 2024, floated as the next Ekeler *(2024 takes, stale)*
- [[Tyler Goodson]] — RB, IND — explosive, natural cutback runner masked by Iowa's scheme; Waldman's long-term Colts preference *(2023 takes, stale)*
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, HOU — had taken the job outright from Dameon Pierce in December 2023, but Waldman reverses: no longer Houston's presumptive 2024 starter, expects a free-agent RB (Jacobs or Henry) to take over; a rough Divisional Round game (9 carries, 22 yards) reinforces the need for an upgrade, though Harmon notes it followed a genuinely strong late-season stretch *(2024 takes, stale)*
- [[Saquon Barkley]] — RB, NYG — valuable, but the last of the space-expensive jump-cut runners; inefficient play-to-play on film *(2023 takes, stale)*
- [[Derrick Henry]] — RB, TEN — "a one of one" and unreplicable, with a real knock (defenses key him and it sticks); wouldn't draft as RB1 for 2024, wants him as a cheap "dead zone" back and is rooting for a Ravens landing spot; explicit [Best Ball] value call — a 7th/8th-round price on a 2023 RB12 is a market miss per both hosts; price keeps sliding — fifth-round redraft value Waldman calls a likely "huge steal," worth a third-round pick on talent alone; Chargers/Dallas/Philadelphia now added to the Ravens landing-spot list *(2024 takes, stale)*
- [[Joe Mixon]] — RB, CIN — expected to be moved on from by Cincinnati; Waldman's ideal fit is Dallas, offering the explosion/power/receiving package fans hoped Tony Pollard would provide *(2024 takes, stale)*
- [[Alvin Kamara]] — RB, NO — cap-squeeze uncertainty in New Orleans, but a weeks-4-17 top-4 fantasy back when playing; a Shanahan-tree scheme (new OC Klint Kubiak) could extend his effective range *(2024 takes, stale)*
- [[Breece Hall]] — RB, NYJ — "averts one disaster at a time"; processes fast but not two steps ahead, and Waldman still expects big-time yardage with a better line *(2023 takes, stale)*
- [[Nick Chubb]] — RB, CLE — the big back who beats the size rule; best ever at re-accelerating post-contact, "Hall of Fame caliber talent," 2023 knee injury the live question *(2023 takes, stale)*
- [[David Montgomery]] — RB, DET — the low-variance half of the Detroit committee; "very rarely will break a 25-plus-yard run"; part of Waldman's "dynamic running back duo" praise for Detroit's backfield post-NFC-Championship *(2024 takes, stale)*
- [[Isiah Pacheco]] — RB, KC — the pace-control negative case: one speed, "zero or a hundred"; running well anyway through the postseason, open bell-cow question, but a Joe Thuney injury is a live threat to his AFC Championship workload; one of the pieces giving KC enough to "play with anyone" per Waldman post-AFC-Championship; two Super Bowl LVIII fumbles read as a 2024 buying opportunity, not a red flag — KC never benched him, "should be a top-10 running back," ADP currently round 2-3 turn *(2024 takes, stale)*
- [[Kyren Williams]] — RB, LAR — sub-top-10 talent, top-10 production off the Rams' line and scheme; Waldman's 2024 RB1, contingent on the coaching staff/line and no free-agent power-back addition *(2024 takes, stale)*
- [[Kenneth Walker III]] — RB, SEA — Waldman draft him higher than market: Pete Carroll's pattern is to "covet" one back until injury forces a change, and Walker is currently that back; Carroll is now out, new HC Mike McDonald in, reopening the usage-pattern question *(2024 takes, stale)*
- [[Raheem Mostert]] — RB, MIA — the cheap half of Miami's committee; both hosts value him as a 2024 RB2, expect more work to shift to Achane *(2024 takes, stale)*
- [[James Connor]] — RB, ARI — both hosts hanging on for 2024; "toast" skepticism reframed as a second-contract finance story, not a talent decline; Michael Carter cuts into but doesn't replace him *(2024 takes, stale)*
- [[Aaron Jones]] — RB, GB — "injury agnostic, not stupid": still playable, price-sensitive given his injury history; Harmon calls him "criminally underrated" off a 5-straight-100-yard-game close to the season, but flags him as unreliable to stay healthy and wants Green Bay to draft a real RB2 rather than lean on A.J. Dillon again *(2024 takes, stale)*
- [[Zamir White]] — RB, LV — the industry's hottest 2024 sleeper name per Waldman, who flags his own overhype risk; tied to Antonio Pierce keeping his job; a clear RB2 behind a Jacobs-elsewhere RB1 ceiling *(2024 takes, stale)*
- [[Tank Bigsby]] — RB, JAX — overrated by "about a round and a half" pre-draft per Waldman; costly drops, indecisive runner; opportunity would still get him 1,000 yards *(2024 takes, stale)*
- [[Kendre Miller]] — RB, NO — Waldman's preferred dynasty stash over Bigsby, on opportunity alone *(2024 takes, stale)*
- [[Chase Brown]] — RB, CIN — "I love Chase Brown"; Waldman's other preferred dynasty stash over Bigsby *(2024 takes, stale)*
- [[Tony Pollard]] — RB, DAL — a real reversal one week later: both Waldman and guest Daniel Harms flip to skeptical, citing a lack of elite vision in condensed spaces and lost explosiveness; best-case outcome is now a complementary role, not a bell cow *(2024 takes, stale)*
- [[Michael Carter]] — RB, ARI — "a pretty damn good back" who should cut into James Connor's 2024 workload, receiving skills underused so far *(2024 takes, stale)*
- [[Austin Ekeler]] — RB, LAC — possible 2024 rebound, but Waldman wouldn't personally invest; may be closer to the end than the industry realizes *(2024 takes, stale)*
- [[Josh Jacobs]] — RB, LV — "easily" the best free-agent candidate to become the next James Connor; the better back in a direct comparison with Zamir White *(2024 takes, stale)*
- [[Najee Harris]] — RB, PIT — both hosts "intrigued" by his backfield outlook under new OC Arthur Smith's volume-funneling scheme; no explicit split from [[Jaylen Warren]] projected yet *(2024 takes, stale)*
- [[Jaylen Warren]] — RB, PIT — intriguing complementary piece under new OC Arthur Smith, but explicitly tempered — "if you were waiting for a full-on revival, I don't think we're going to get that" *(2024 takes, stale)*
- [[Jordan Mason]] — RB, SF — Waldman's preferred McCaffrey-injury contingency over Elijah Mitchell, on versatility and price *(2024 takes, stale)*
- [[Elijah Mitchell]] — RB, SF — got more 2023 volume than Mason down the stretch, but still Waldman's #2 McCaffrey handcuff on price *(2024 takes, stale)*
- [[Tyler Allgeier]] — RB, ATL — Bijan Robinson's complementary piece; "plays really well when in the system they put him in" *(2024 takes, stale)*
- [[Blake Corum]] — RB, Michigan prospect — Angelo's case for "the safest prospect in this class," built on feel for closing space rather than measurables; Kyren Williams/Devin Singletary comp *(2024 pre-draft takes, stale)*
- [[De'Von Achane]] — RB, MIA — spectacular rookie efficiency, but a real 2024 overrated risk: great to the edge, only good between the tackles, exploitable once defenses take the edge away; fine value in rounds 4-5, dangerous priced top-3 *(2024 takes, stale)*
- [[Braelon Allen]] — RB, Wisconsin prospect — Harms's most overrated back in the class, echoed by Angelo on competitiveness grounds; Waldman frames him as a "Wisconsin curse" case (cf. Jonathan Taylor, Melvin Gordon) who needs a Derrick-Henry-understudy runway rather than a rookie workhorse role — Baltimore is the dream fit *(2024 pre-draft takes, stale)*
- [[Jonathan Brooks]] — RB, Texas prospect — good size, an excellent pass protector; real three-down-back candidate per Waldman *(2024 pre-draft takes, stale)*
- [[Blake Watson]] — RB, Memphis prospect — "very underrated" per Waldman, a Giovanni Bernard/Austin Ekeler type; catches, runs inside, blocks well; could go earlier than expected if he tests well *(2024 pre-draft takes, stale)*
- [[Jabari Small]] — RB, Tennessee prospect — Shrine Game name Waldman likes; undersized (205 lbs) but runs hard with good vision and decision-making *(2024 pre-draft takes, stale)*
- [[Ray Davis]] — RB, Kentucky prospect — 5'8"/217, Frank-Gore-esque build that plays more fluidly than the size suggests; all-three-phases competent, projected 4th-5th round per Angelo *(2024 pre-draft takes, stale)*
- [[Dylan Laube]] — RB, New Hampshire prospect — small-school pass-catching riser; Angelo now grades him a top-5 back in the class outright against a public RB15-20 perception, built on genuine outside/boundary receiving skill; Waldman ranks him almost even with [[Blake Corum]] — floor a receiving Kenneth Gainwell, ceiling between Gainwell and [[James Cook]] *(2024 pre-draft takes, stale)*
- [[Daijun Edwards]] — RB, Georgia prospect — quick and shifty despite playing through an MCL injury, good pass catcher/blocker; Jalen-Richard floor, dynamic-James-White ceiling; likely the most-rostered of Waldman's three underrated 2024 RBs on name value alone *(2024 pre-draft takes, stale)*
- [[George Holani]] — RB, Boise State prospect — the highest-variance of Waldman's three underrated 2024 RBs; real injury history but explosive flash (7 missed tackles forced on one screen vs. UCLA), needs added weight to profile as a committee back *(2024 pre-draft takes, stale)*
- [[Deshaun Fenwick]] — RB, Oregon State prospect — Shrine Game favorite; Leonard-Fournette-adjacent big-back build, gap-scheme thumper, projects as a reserve "B-back" *(2024 pre-draft takes, stale)*
- [[Brian Robinson Jr.]] — RB, WAS — Cliff Kingsbury's move to Washington OC "doesn't hurt as much as people think" per Waldman (James Connor/Arizona comp); red-zone-touch-dependent, projects low-end RB1/high-end RB2 *(2024 takes, stale)*
- [[Tyjae Spears]] — RB, TEN — stock rising regardless of Derrick Henry's free-agency outcome, on receiving work alone; new O-line coach Bill Callahan and a likely Henry departure both add further tailwind; Jerome Ford value comp, "more talented" per Waldman *(2024 takes, stale)*
- [[Mario Anderson]] — RB, Memphis prospect (future class) — flagged by Waldman as the next name in Memphis's RB pipeline (Pollard, Henderson, Gainwell); shifty, good vision, Ray Davis size/balance comp *(2024 pre-draft takes, stale)*
- [[Cody Schrader]] — RB, Missouri prospect — Angelo's late-round pick to make a roster and stick; 1,800 total yards/14 TDs at Missouri, Senior Bowl standout, graded a smart, reliable long-term role player rather than a star *(2024 pre-draft takes, stale)*
- [[Kendall Milton]] — RB, Georgia prospect — unique size/speed at 6'1"/220-225; hasn't yet shown the Eddie-George-level ceiling his HS recruiting profile promised; combine/pro day season is the swing factor for his stock *(2024 pre-draft takes, stale)*
- [[Kimani Vidal]] — RB, Troy prospect — 5'7"/215 power back with a low center of gravity and real movement skill; standout Senior Bowl pass protector; projects as a Day 3 committee piece if he survives camp *(2024 pre-draft takes, stale)*
- [[Will Shipley]] — RB, Clemson prospect — underrated receiving-back profile with real speed (6.4s HS 55m); combine 40 time is the key swing event for his stock; projects as a Dion-Lewis/James-White-style complementary role *(2024 pre-draft takes, stale)*
- [[Rasheen Ali]] — RB, Marshall prospect — explosive pre-ACL flash back who returned to the same level; graded the best RB at the 2024 Senior Bowl for his limited reps there; ball security is the swing risk *(2024 pre-draft takes, stale)*
- [[Jaylen Wright]] — RB, Tennessee prospect — a rawer Travis Etienne comp per Angelo (elite high-school-caliber accelerator, brilliant but inconsistent through contact); Waldman rates him lower, in [[Blake Watson]]'s tier, on ball security and contact-balance concerns *(2024 pre-draft takes, stale)*
- [[Dillon Johnson]] — RB, Washington prospect — Waldman's fourth early-round-talent name; played through multiple injuries into the national title game, some of the best contact balance in the class, but a real breakaway-speed/explosiveness ceiling concern *(2024 pre-draft takes, stale)*
- [[Trey Benson]] — RB, Florida State prospect — physical, "nasty" finisher paired with genuine [[Isiah Pacheco]]-caliber acceleration but without Pacheco's unconventional movement signature *(2024 pre-draft takes, stale)*
- [[Bucky Irving]] — RB, Oregon prospect — a [[Devin Singletary]]-style boom/bust comp; real disagreement between hosts on how close he already is to the "on schedule" discipline that would unlock a "Singletary-plus" outcome *(2024 pre-draft takes, stale)*
- [[Marshawn Lloyd]] — RB, USC prospect — the episode's clearest bust-risk name; ball security, outside-bounce tendencies, and third-down role questions behind a perception both hosts think is inflated by a handful of highlight plays; Waldman's 50th-percentile outcome is "out of the league in a couple years" *(2024 pre-draft takes, stale)*
- [[Khalil Herbert]] — RB, CHI — Waldman prefers him over Roschon Johnson as the value side of a Bears RB timeshare
- [[Roschon Johnson]] — RB, CHI — Waldman: RB35 ADP near his peak-production ceiling; Herbert preferred as the better value
- [[Javonte Williams]] — RB, DEN — Waldman: 2023 dud likely lingering knee-injury effect, not decline; value play
- [[Samaje Perine]] — RB, DEN — Waldman: elite YAC receiving back, will complicate a Javonte Williams breakout

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — Waldman: 1-2 with Ja'Marr Chase, negligible gap; would take Chase today only for Cincinnati's QB certainty edge
- [[Ja'Marr Chase]] — WR, CIN — Waldman: locked in almost any scenario if Burrow stays; slight dynasty edge over Justin Jefferson on QB certainty
- [[Keenan Allen]] — WR, LAC — top-5 WR without speed: beats man *and* zone, plays inside and outside *(2023 takes, stale)*
- [[Amon-Ra St. Brown]] — WR, DET — same profile as Allen, with play-caller continuity as the tiebreaker; Harmon's #2 overall receiver remaining in the playoffs but #1 by team value ("in a runaway") — now beating press-man as well as zone; entering his contract year, "up for a big payday pretty soon" *(2024 takes, stale)*
- [[Jameson Williams]] — WR, DET — real but hedged optimism after a big NFC Championship game; Waldman's explicit overdraft warning — "the Gabe Davis factor" — don't price him off one game; Harmon's harder technical critique — "shaky hands," not a "go up and get it" guy, a "splash play dude" whose highlights lean on Ben-Johnson-designed structure (Johnson is now confirmed staying in Detroit) *(2024 takes, stale)*
- [[Brandon Aiyuk]] — WR, SF — best route runner in San Francisco and a WR1 bet at a bargain price; Harmon's #1 overall of the playoffs' remaining receivers, expects a 100-yard NFC Championship against Detroit's league-worst secondary; "woefully underpaid" on his fifth-year option per Harmon, who floats a hypothetical trade inquiry and flags him as one leg of a coming SF pass-catcher roster crunch (Aiyuk/Deebo/Kittle can't all stay past 2024) *(2024 takes, stale)*
- [[Tee Higgins]] — WR, CIN — WR21 since Browning took over, but boom/bust without Burrow's moving deep ball; expected to be franchise-tagged by Cincinnati, but drawing outside interest anyway per Waldman, including a floated (unlikely) Detroit trade scenario *(2024 takes, stale)*
- [[Jordan Addison]] — WR, MIN — rotation promotion missed by box-score watchers; Waldman's #2 2023 rookie WR, "a better version of Devonta Smith"; ceiling is a Minnesota-QB question *(2024 takes, stale)*
- [[Jayden Reed]] — WR, GB — Allen/St. Brown route-running mold *with* speed; Waldman wouldn't trade him for any other 2023 rookie WR, Diggs upside/Coles floor; Harmon's pick as the Green Bay receiver with the best odds to become a true number one, capable of an Amon-Ra St. Brown-style role *(2024 takes, stale)*
- [[Noah Brown]] — WR, HOU — best Texans receiver whenever Nico Collins is out; a conditional weekly start; placed on IR during the 2023 playoff run *(2024 takes, stale)*
- [[John Metchie III]] — WR, HOU — flashed filling in for an injured Noah Brown in the Wild Card win, but downgraded after the Divisional Round — Harmon: "has proven nothing to this point in his career," replacement-level depth, not a real answer opposite Nico Collins *(2024 takes, stale)*
- [[Xavier Hutchinson]] — WR, HOU — faint praise, an Allen-Lazard-type depth/blocking piece rather than a real target threat *(2024 takes, stale)*
- [[Tre Tucker]] — WR, LV — "aspiring Jaylen Waddle" in the Tyreek Hill role; high variance, not yet a complete player *(2023 takes, stale)*
- [[Treylon Burks]] — WR, TEN — talent to be mined, still a work in progress; one big game wasn't a role; by January "his injury ship has kind of sailed" per Brandon Angelo *(2024 takes, stale)*
- [[DeAndre Hopkins]] — WR, TEN — the "old man game" archetype; experts split on how much tail is left *(2023 takes, stale)*
- [[Adam Thielen]] — WR, CAR — reputation as a possession receiver misreads a genuinely elite athletic profile *(2023 takes, stale)*
- [[Deebo Samuel]] — WR, SF — elite vs zone and as a gadget runner, "not remotely as good" vs man; his value may not survive a team change; Harmon's #3 overall receiver remaining in the playoffs, "a true game wrecker" hard to rank against traditional route runners; Super Bowl LVIII was a live confirmation on tape — pressed all game, held to 3-for-33 on 11 targets — and he's flagged as one leg of a coming SF pass-catcher roster crunch (Aiyuk/Deebo/Kittle can't all stay past 2024) *(2024 takes, stale)*
- [[Malik Nabers]] — WR, LSU prospect — both *Going Deep* hosts take him over Marvin Harrison Jr. "by a healthy margin" on pro-readiness; 1,100/10 rookie projection; Harmon's early RP charting has him 3rd of the top-3-prospect trio in separation/contested-catch/hands but still elite, with a "60 to zero" deceleration signature (92% curl-route success rate) *(2024 pre-draft takes, stale)*
- [[Marvin Harrison Jr.]] — WR, OSU prospect — skips combine AND pro day too, no agent; Waldman/Harmon read it as confidence, still top-5 projected
- [[Rome Odunze]] — WR, Washington prospect — Harmon's early RP charting: no separation concerns despite a contested-catch reputation, versatile across all three alignments; same Daniel Jeremiah grade as Harrison Jr. *(2024 pre-draft takes, stale)*
- [[Keon Coleman]] — WR, Florida State prospect — genuinely athletic but not elite-tier; catch-point skills "borderline otherworldly"; outcome hinges on landing in a timing-based passing scheme or risks a Courtland-Sutton-style outside-only pigeonhole; Harmon's early charting is more skeptical still — real separation issues, ~33rd percentile, a direct Treylon Burks bust comp *(2024 pre-draft takes, stale)*
- [[Ainias Smith]] — WR/RB, Texas A&M prospect — both hosts' sleeper, "miscast as a gadget"; clean catch-point technique the real gadget archetypes lack; risk is a permanent gimmick-role typecast *(2024 pre-draft takes, stale)*
- [[Michael Gallup]] — WR, DAL — Harms is out on a 2024 rebound; doesn't create separation as an X, may not even be in Dallas, projects a Chris-Conley-style "good player, not fantasy relevant" career *(2024 takes, stale)*
- [[Brian Thomas Jr.]] — WR, LSU prospect — not top-5 in this specific class but would be fringe top-5 in most others; elite downfield/catch-point skills, route-running polish and YAC the open questions; Harmon's early charting confirms a good press-beater with a heavily concentrated 3-route tree, floats a speculative Detroit fit *(2024 pre-draft takes, stale)*
- [[Ladd McConkey]] — WR, Georgia prospect — the strongest of Harmon's early-charted 2024 WR trio, despite his own stated skepticism going in; excellent at selling vertical routes and snapping back on comebacks, an early Cooper Kupp mold comp with a real size caveat; Daniel Jeremiah has him 44th overall *(2024 pre-draft takes, stale)*
- [[Ricky Pearsall]] — WR, Florida prospect — Harms's favorite sleeper, an explicit Puka Nacua comp; outcome hinges almost entirely on scheme/QB fit rather than his own ceiling; Waldman independently corroborates — "the guy that's getting overlooked," what Alec Pierce was supposed to be with a better route game; Angelo's Senior Bowl take agrees — late Day 2/early Day 3, immediate-impact slot role, a Cole Beasley NFL comp *(2024 pre-draft takes, stale)*
- [[Troy Franklin]] — WR, Oregon prospect — real speed and a growing route feel, but "disappears with physicality"; range spans a Jordan-Addison-style hit to a marginal role player *(2024 pre-draft takes, stale)*
- [[CeeDee Lamb]] — WR, DAL — Bob Harris's pick for 2024 #1 overall over McCaffrey; Waldman ranks him 2nd *(2024 takes, stale)*
- [[Tyreek Hill]] — WR, MIA — 3rd in Waldman's 2024 top tier, but Bob Harris's personal #2 as "an old-school wide receiver one" *(2024 takes, stale)*
- [[Mike Evans]] — WR, TB — 11 straight 1,000-yard seasons; 2024 outlook is pure situation — cheap and startable if he stays in Tampa with Baker Mayfield, cautious if he leaves; "an absolute smash spot" for the Divisional Round per Harmon; Harmon says Tampa "cannot allow him to test the open market" (3yr/$50M+ projected), with Detroit's cap space and culture fit floated as the top alternative landing spot; Waldman independently floats Kansas City as another suitor; now a scheme question too — OC Dave Canales, credited by Harmon for "unleashing" him in 2023, is leaving for the Carolina HC job; a reported contract-deadline has now passed with no new deal — closer than ever to actually reaching the open market *(2024 takes, stale)*
- [[Rashid Shaheed]] — WR, NO — "WR4 with WR3 upside," a good Best Ball play; Waldman skeptical New Orleans sees him as more than a speed-role piece unless a coach says otherwise in camp *(2024 takes, stale)*
- [[Jerry Jeudy]] — WR, DEN — "skilled" but not a strong true #1; "more the next Reggie Wayne" than the next A.J. Brown per Waldman, who also flags a vague, unexplained concern ("something going on there") *(2024 takes, stale)*
- [[Courtland Sutton]] — WR, DEN — "always thought was overrated" per Waldman; not a great route runner, "throw him five balls for him to catch three" *(2024 takes, stale)*
- [[Chris Godwin]] — WR, TB — Waldman's strongest Bucs-receiver praise in the wiki: a Pro-Bowl-level, all-alignment "complete skill-set guy," Gronkowski-versatility comp; health/age the only live question; Harmon's retrospective — Tampa's 2023 move of him to a primarily outside role was "a gigantic mistake" not fixed until Week 14-15 — is now more relevant with OC Dave Canales (who fixed it) leaving for Carolina's HC job *(2024 takes, stale)*
- [[Rashad Bateman]] — WR, BAL — "a super value play" if cheap per Waldman; limited by Andrews/Likely both being non-blocking tight ends; career-long availability question ("always hurt" per Waldman) though he made it through the full 2023 season healthy per Harmon, who still stops short of calling him a proven "key contributor" without the Ravens adding more around him *(2024 takes, stale)*
- [[Stefon Diggs]] — WR, BUF — Bob Harris's instant no; Waldman sees 2024 value if he falls to the 2nd/3rd-round turn, with a Gabe Davis-shaped caution; Harmon flags real role dilution; Waldman senses unspecified off-field smoke after the Divisional Round loss; Harmon's specific theory — an unreported oblique/back injury behind a steep 2nd-half production collapse — with $32M in dead cap ruling out a cut, restructure or trade the likely paths *(2024 takes, stale)*
- [[Cooper Kupp]] — WR, LAR — not hung up, but Puka Nacua's emergence caps his ceiling; "days of being that true alpha... are over, draft accordingly"; Harmon puts it at a "50/50 shot" that repeated ankle injuries have permanently sapped his explosiveness rather than a one-year dip, and RP charting now has Nacua separating better vs. man *(2024 takes, stale)*
- [[Quentin Johnston]] — WR, LAC — the 2023 rookie class's clearest bust risk so far; a route-runner without a catch-point, better projected as a slot piece than the outside role he was drafted for; now cited by Harmon as one of the all-time worst RP rookie seasons and the standard scheme-fit cautionary tale *(2024 takes, stale)*
- [[Jaxon Smith-Njigba]] — WR, SEA — Waldman's #1 2023 rookie WR despite thin volume; built as the season went on; new HC Mike McDonald reportedly wants to move him into "a more premier role," with [[Tyler Lockett]]'s roster spot now in doubt *(2024 takes, stale)*
- [[Zay Flowers]] — WR, BAL — in Waldman's top rookie WR tier but more boom/bust, entirely on how much Lamar Jackson's offense trusts him; the earlier "don't trade London for Flowers" debate is now resolved in London's favor after the full season; Harmon's #4 remaining playoff receiver with real "superstar tier" upside language, but a tough outside-alignment matchup vs. Kansas City's AFC Championship secondary *(2024 takes, stale)*
- [[Puka Nacua]] — WR, LAR — Waldman's #3 2023 rookie WR, #1 by pure production; Harstad's post-rookie model scores his rookie year the single best in its 2006-2023 sample, expanding the "big four" to a "big five"; long-term outlook tied to Stafford's remaining runway *(2024 takes, stale)*
- [[Tank Dell]] — WR, HOU — just outside Waldman's top-5 rookie WRs; Harstad's counter-read is he's inflated by Nico Collins drawing tougher coverage *(2024 takes, stale)*
- [[Nico Collins]] — WR, HOU — Harstad's "doing the harder thing" pick — harder to replace in Houston's offense than Tank Dell; Harmon calls him a top-10 NFL receiver after the Wild Card win, expects a 2nd/3rd-round 2024 ADP jump from a 2023 waiver price; boxed up by Baltimore's coverage in the Divisional Round (68 yards, 47 after the catch) but the season-long top-10 grade holds *(2024 takes, stale)*
- [[Josh Downs]] — WR, IND — "certainly going to be worthwhile" once Anthony Richardson is back and healthy *(2024 takes, stale)*
- [[Marvin Mims Jr.]] — WR, DEN — underused rookie year per Waldman; profile fits a Sean Payton deep-threat role once friction resolves *(2024 takes, stale)*
- [[Jalen Hyatt]] — WR, NYG — Waldman "a little more convinced" despite a bad Giants QB situation *(2024 takes, stale)*
- [[Rashee Rice]] — WR, KC — Waldman's self-admitted biggest 2023 rookie-WR pre-draft miss (had him 44th, late-4th-round value); Harstad's post-rookie model now scores him in the same tier as Reed/Flowers with real Tyreek Hill-level upside, though the manufactured/scheme-inflated-role downside case (Matt Harmon agrees) is equally live; Harmon's #5 (last) of the playoffs' remaining receivers — "very good" but capped at a Cooper-Kupp-archetype ceiling; Waldman's "notable exception" to GM Brett Veach's weak WR-drafting history, hoping KC adds a proven FA weapon around him; post-Super-Bowl real ADP downgrade — explicit "Gabe Davis effect," undrafted deep into Waldman's own mock — "not reliably valuable for top-five-round" picks *(2024 takes, stale)*
- [[Davante Adams]] — WR, LV — feeling it on staying in Vegas now that Luke Getsy (his old Packers OC) is the new OC; falling ADP (late 2nd round) framed as an explicit buy, "regardless of quarterback" *(2024 takes, stale)*
- [[Gabe Davis]] — WR, BUF — "a good football player," but the boom/bust role (not the talent) is the problem; "playing somewhere else next year for sure" per Waldman, Atlanta floated as a fit; Harmon independently corroborates "not a true number two receiver," zero yards in 5 of last 9 games *(2024 takes, stale)*
- [[Khalil Shakir]] — WR, BUF — now rated above both Gabe Davis and Stefon Diggs "in this moment"; expected 2024 starter, only question is role overlap with Kincaid; Harmon corroborates — reliable, "a good football player," part of Buffalo's future *(2024 takes, stale)*
- [[Drake London]] — WR, ATL — top-15 value in play for 2024 once Atlanta hires a real coach/QB; cheaper price, but not that cheap given industry consensus; "no question" he had the better rookie year than Zay Flowers once the full season is in; one of only 5 receivers ever to earn Harmon's tier-one Reception Perception "stacked board" grade; new OC Zach Robinson (ex-Rams) projected by Harmon to feature him on Nacua/Kupp-style in-breaking routes *(2024 takes, stale)*
- [[Michael Wilson]] — WR, ARI — a genuinely good route runner in the "aspiring Michael Thomas" mold; top-24 value if he can finally stay healthy *(2024 takes, stale)*
- [[George Pickens]] — WR, PIT — the headline beneficiary of Pittsburgh hiring Arthur Smith as OC; charted evidence (Drake London's dig/slant usage under Smith vs. Pickens's own under Matt Canada) projects real middle-of-field volume for the first time in his career *(2024 takes, stale)*
- [[Diontae Johnson]] — WR, PIT — cited as further charted evidence of Matt Canada's middle-of-field neglect (9.4% dig routes in 2022); grouped with Pickens as a likely beneficiary of the Arthur Smith scheme change *(2024 takes, stale)*
- [[Tyler Lockett]] — WR, SEA — still part of "one of the best three-person WR trios in the NFL," but his roster spot is a real 2024 question under new HC Mike McDonald given his cap hit; floated as a fit to reunite with OC Shane Waldron in Chicago *(2024 takes, stale)*
- [[Terry McLaurin]] — WR, WAS — Waldman: solid WR2 (not a true WR1), flags genuinely poor hand-catch technique despite the production
- [[Wan'Dale Robinson]] — WR, NYG — real after-the-catch and contested-catch value; outlook entirely a Giants-QB question *(2024 takes, stale)*
- [[Ronnie Bell]] — WR, SF — a name to know mostly for injury-contingency reasons behind Aiyuk/Deebo, not his own emergence *(2024 takes, stale)*
- [[Dontayvion Wicks]] — WR, GB — "turned some heads"; catch-point toughness threatens to bump Doubs or an injury-prone Watson out of the fantasy-relevant mix; Harstad's post-rookie model calls him the single biggest buy in the whole 2023 WR class, and Waldman upgrades him from hold to active trade target; Harmon's #2 pick (behind Reed) for Green Bay's eventual number one *(2024 takes, stale)*
- [[Romeo Doubs]] — WR, GB — part of Green Bay's "big three," but "a little less multi-dimensional" than what Wicks offers; Harmon's clear #4 of the group — solid vertical player and best 2023 postseason of the four, but not a path to more *(2024 takes, stale)*
- [[Christian Watson]] — WR, GB — speed is unquestioned; durability is the entire 2024 question mark; Harmon's real new knock — can't make the true-number-one-receiver case for him "without mentioning height," unlike Reed or Wicks *(2024 takes, stale)*
- [[Cedric Tillman]] — WR, CLE — bottom-tier post-rookie model score; the "Amari Cooper-esque hopeful" behind Cooper himself, free add but not worth paying up for *(2024 takes, stale)*
- [[Tyler Scott]] — WR, CHI — "overrated on speed" pre-draft per Waldman; used as a one-dimensional RPO/deep-shot option, a Darnell-Mooney-before-he-developed comp *(2024 takes, stale)*
- [[Jonathan Mingo]] — WR, CAR — one of only two 2023 rookie WRs to open as a Week 1 starter, but tanked by historically bad Carolina QB play; Waldman revising down hard on coaching-change risk, not talent *(2024 takes, stale)*
- [[Demario Douglas]] — WR, NE — league-average post-rookie model score held down by zero touchdowns; both hosts think he outplayed a barren Patriots offense; buy in the 4th/5th round, not the 3rd *(2024 takes, stale)*
- [[Malik Washington]] — WR, Virginia prospect — one of Waldman's favorite under-the-radar 2024 receivers; thick slot build with big-play juice, could start within his first contract *(2024 pre-draft takes, stale)*
- [[Xavier Legette]] — WR, South Carolina prospect — DK Metcalf comp per industry, Waldman's own range is Alshon Jeffery-to-Metcalf; big, physical, fast enough; tempered after live Senior Bowl reps looked "sloppier," less dominant than his frame suggested per Angelo *(2024 pre-draft takes, stale)*
- [[Malachi Corley]] — WR, Western Kentucky prospect — "already" a sleeper per Waldman; DJ-Moore-lite comp, elite after the catch, real early fantasy relevance if the role grows; Angelo corroborates with more technical detail — real route-running nuance, better catch-point work than the early consensus credited *(2024 pre-draft takes, stale)*
- [[Javon Baker]] — WR, UCF prospect — Alabama transfer with excellent catch-point skills and a strong release; a 2/1b-type number-one-adjacent ceiling, some bust risk but not a lot *(2024 pre-draft takes, stale)*
- [[Roman Wilson]] — WR, Michigan prospect — flashed despite a run-heavy offense; one of the best 3 WRs at the Senior Bowl per Angelo, creeping into the top 100 *(2024 pre-draft takes, stale)*
- [[Devontez Walker]] — WR, North Carolina prospect — a real stock disagreement: outside buzz has him as high as late Round 1, Angelo's own grade is late Day 3 and he's sticking with it *(2024 pre-draft takes, stale)*
- [[Brendan Rice]] — WR, USC prospect — solidified as a late Day 2/Day 3 pick per Angelo through Senior Bowl week *(2024 pre-draft takes, stale)*
- [[J. Michael Sturdivant]] — WR, UCLA prospect (Cal transfer) — 6'3"/205, high-end traits that "didn't really emerge at the highest level" of production per Waldman; declared, ungraded *(2024 pre-draft takes, stale)*
- [[Marquise Brown]] — WR, ARI — floated as a hypothetical Kansas City free-agent fit; Harmon rejects it on archetype grounds — "another zone-beating type," not a man-coverage or contested-catch threat *(2024 takes, stale)*
- [[Skyy Moore]] — WR, KC — Harmon calls his outside-receiver usage a "mis-evaluation" of the player; doesn't expect him in Kansas City's plans and would rather see him traded to restart elsewhere *(2024 takes, stale)*
- [[A.J. Brown]] — WR, PHI — Waldman: worth a 1st-rounder in best ball; unbothered by WIP-call drama, worries about Eagles' org instead
- [[DeMarcus Robinson]] — WR, LAR — Waldman: WR99 ADP 'free square'; late-2023 DFS run buildable but temper expectations
- [[Jahan Dotson]] — WR, WAS — Waldman: skilled WR3/matchup WR2, but unsure new Kingsbury-called offense unlocks him

### Tight Ends
- [[T.J. Hockenson]] — TE, MIN — great in zone, positions well in man; TE1 ceiling minus a tier with a backup QB *(2023 takes, stale)*
- [[Travis Kelce]] — TE, KC — his first-round-pick days are over per Waldman; a nagging early-2023 injury may have lingered all year — but guest Daniel Harms pushes back hard, attributing the down year to two specific in-season injuries rather than decline and projecting at least two more strong seasons; unresolved disagreement; still finished TE1 in 2023 despite the down year, "he'll be fine" per Waldman after the AFC Championship; post-Super-Bowl reframe — no longer "the dominant force," but because KC lacks a second weapon, not because of age *(2024 takes, stale)*
- [[Sam LaPorta]] — TE, DET — Waldman's own miss: needed the perfect fit and found it; outproduced Kincaid as a rookie, still a top-5 dynasty TE in his tier; "one of the best young tight ends, if not the best young tight end in the game" *(2024 takes, stale)*
- [[Dalton Kincaid]] — TE, BUF — Waldman's stated long-term preference over LaPorta despite being outproduced as a rookie; a top-5 2024 TE call in an offense he says can support three fantasy starters *(2024 takes, stale)*
- [[Luke Musgrave]] — TE, GB — Waldman's pre-draft 7th-ranked TE, now sees as "slightly overrated" relative to teammate Tucker Kraft *(2024 takes, stale)*
- [[Tucker Kraft]] — TE, GB — the value pick of Green Bay's two rookie tight ends per Waldman — more rugged, more room to grow, and cheaper on his board *(2024 takes, stale)*
- [[Brevyn Spann-Ford]] — TE, Minnesota prospect — 6'7"/270; looked lost as a blocker in 2022, visibly figured out technique by late 2023 per Waldman; projects as a practice-squad/depth-TE NFL path *(2024 pre-draft takes, stale)*
- [[Kyle Pitts]] — TE, ATL — both hosts "totally feel it" on a 2024 rebound now that Zach Robinson is OC; Waldman's down-2023 diagnosis is QB-driven (Desmond Ridder's field-reading limits), not a talent decline *(2024 takes, stale)*
- [[Pat Freiermuth]] — TE, PIT — real usage-risk flag off the Arthur Smith hire, not a talent knock — "two of three" Steelers TEs will be fine and it's "probably going to be the more athletic two," an explicit Kyle-Pitts-underuse comparison *(2024 takes, stale)*
- [[Brycen Hopkins]] — TE, LAR — pending free agent, promising but flawed (RAC ability, athletic, but poor blocker with drop issues); Dustin Keller comp; deep-league stash or wait-and-see, not a lead-role bet *(2024 takes, stale)*
- [[Brock Bowers]] — TE, Georgia prospect — Waldman leaning "feel it" on him becoming the next big rookie-TE fantasy producer; a LaPorta-mold "move tight end" with one real catch-point flaw and blocking to develop; Dalton-Kincaid-outcome comp, not LaPorta/Pitts-level rookie production *(2024 pre-draft takes, stale)*
- [[George Kittle]] — TE, SF — quiet Super Bowl LVIII box score plus a brief locker-room injury scare; career-best yards-per-target season in 2023; flagged as one leg of a coming SF pass-catcher roster crunch (Aiyuk/Deebo/Kittle can't all stay past 2024) per Harmon *(2024 takes, stale)*

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
- [[Post-Rookie-Year Receiver Model]] — Adam Harstad's touchdown-adjusted yards-per-route-run + usage-rate composite for grading rookie WR seasons; historical score buckets from "abandon all hope" to the Beckham/Chase/Jefferson/Brown "big four"; Waldman treats it as one input, not a verdict
- [[Reception Perception Methodology]] — Matt Harmon's WR charting project: success rate vs. press/man/zone coverage, route-type and alignment splits, 3-game early reads expanding to ~8-game final profiles; cross-class "stacked board" with a top-10-worthy "tier one" grade
- [[Quarterback Processing and Confidence]] — Waldman's framework for why teams miss on QB evaluations: processing speed under pressure is a confidence/intuition skill, not an academic one; Alex Smith as the cautionary "over-processed" example
- [[NFL Combine and Pro Day Skepticism]] — Concept — Waldman: combine/pro-day workouts mainly useful for unknown small-school prospects, not blue-chip names; film beats lab metrics

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
