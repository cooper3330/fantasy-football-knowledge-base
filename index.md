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
- [[Justin Fields]] — QB, PIT — traded from CHI for a conditional 6th; Harmon/Koh split on whether return was too low
- [[Derek Carr]] — QB, NO — 2023's rough start traced to left tackle Trevor Penning's play, not Carr himself; strong finish once protection was fixed (3+ TD games in 5 of 6 late-season outings); cheap streaming/QB2 value if the Saints add a receiver *(2024 takes, stale)*
- [[Justin Herbert]] — QB, LAC — Waldman's history-based case that new OC Greg Roman/HC Jim Harbaugh won't cap him despite their run-heavy reputation; projects a more efficient "dink and dunk" ~3,300-3,500 yards, 30+ TD ceiling that specifically benefits Keenan Allen *(2024 takes, stale)*
- [[Russell Wilson]] — QB, PIT (signed FA) - Harmon skeptical of real impact; missed Jeudy deep in DEN, doubts top-20 QB ceiling
- [[C.J. Stroud]] — QB, HOU — Waldman's rankings riser with 3 startable WRs after Diggs trade
- [[Jared Goff]] — QB, DET — Harmon's direct ceiling comp for Tua: "somewhere" top-11-14, stronger arm than Tua; the "what happens once Ben Johnson leaves" question is resolved — Johnson turned down every HC opening, including Washington, and is staying in Detroit; Harmon's sharper follow-up: "there is a level where Jared Goff cannot take you much further," with a clear remaining team need at X receiver *(2024 takes, stale)*
- [[Lamar Jackson]] — QB, BAL — Waldman's contrarian call: the *most* scheme-dependent of the top QBs, not a knock on talent; unqualified 2024 QB1 for both hosts regardless; after the AFC Championship loss, Waldman expects him to supplant Mahomes as 2024 redraft QB2 (maybe QB1), with real year-two growth expected once Monken's offense and a gutted receiver room get an offseason to heal — but Harmon's harder-nosed recap of the same game logs 3 turnover-worthy throws and a near-total run-game abandonment (563rd-of-568 design-run rate), opening an unresolved "are playoff losses mounting" question even while still calling him a top-three QB outright *(2024 takes, stale)*
- [[Patrick Mahomes]] — QB, KC — Waldman's 2024 redraft value call: pushed down boards by Jackson (and maybe Hurts) but won't fall past QB4-5, a real value gap between cost and rank; post-Super-Bowl-LVIII framework — "a wiser Brett Favre," sees through scheme and adapts with far fewer era-defining mistakes *(2024 takes, stale)*
- [[Jalen Hurts]] — QB, PHI — only introduced as the Lamar Jackson value comparison; Philadelphia's Kellen Moore OC hire now has a first grade from Harmon — "definitely an upgrade" over Brian Johnson but "something left to be desired," with a specific worry about how shotgun-exclusive Hurts's usage has become *(2024 takes, stale)*
- [[Brock Purdy]] — QB, SF — not a system QB per Waldman; both hosts lean Purdy over Stroud for 2024; Waldman's career-arc forecast comps him to early Brady/Warner/Wilson/Roethlisberger; Waldman: "exposed as nothing other than what he is" after the Divisional Round win, early ECR outside the top-12 called "a mistake"; Harmon disagrees on that same game — an explicit "bad game," good but "top 20," not elite-tier; Waldman's counter after the NFC Championship win — "subtle skills," carried further by a stacked supporting cast, real front-office skittishness risk if SF doesn't win the Super Bowl *(2024 takes, stale)*
- [[Kyler Murray]] — QB, ARI — one narrow knock: bails the pocket on proximity, "runs as if a bomb has blown up" when anyone gets within three yards *(2023 takes, stale)*
- [[Drew Lock]] — QB, NYG — new page; Waldman expects Lock to open 2024 as starter over ACL-recovering Daniel Jones
- [[Gardner Minshew]] — QB, IND — the model backup: knows exactly who he is, executes schematically, doesn't lose you games *(2023 takes, stale)*
- [[Anthony Richardson]] — QB, IND — trainer Will Hewlett's favorite prospect since Mahomes; Waldman argues pocket processing was underrated, not 'raw' (2024, pre-draft take)
- [[Joe Flacco]] — QB, CLE — 2023 turnaround credited to O-line coach Tom Cable and Stefanski's scheme more than to Flacco himself; ran the Cleveland offense better than Watson has, but expected to hit the veteran-backup market after the Wild Card exit *(2024 takes, stale)*
- [[Jordan Love]] — QB, GB — Waldman's Best Ball QB9 bargain, top-5 QB ceiling if young WRs mature
- [[Dak Prescott]] — QB, DAL — "a good quarterback... when you give him the talent, he can give you elite production"; a boom/bust "prevailing wind" player, helped by the McCarthy scheme fit; Harmon reads the Wild Card blowout loss as having hit his ceiling relative to Jordan Love *(2024 takes, stale)*
- [[Bryce Young]] — QB, CAR — Waldman feeling real 2024 upside: better O-line, Diontae Johnson, Dave Canales; Superflex job-security value
- [[Michael Penix Jr.]] — QB, ATL — trade-up target for Angelo/Waldman on Kirk Cousins' limited runway; projected starter within two years
- [[Tua Tagovailoa]] — QB, MIA — a genuine anticipation/timing thrower who can be schemed into big windows, but a weak post-snap reader who struggles once those windows disappear; Harmon calls a Wild Card loss at KC "straight up bad," ceiling below Jared Goff's *(2024 takes, stale)*
- [[Drake Maye]] — QB, NE — Waldman skeptical of Year 1 start; expects Jacoby Brissett to open camp as starter
- [[Bo Nix]] — QB, DEN — highest floor, lowest ceiling of the rookie QB class per Waldman; Sean Payton scheme fit seen as top-2 producer
- [[Caleb Williams]] — QB, CHI — Waldman's top-1% rookie QB tier; 3,500-4,000 yd projection, Peyton Manning early-career comp
- [[Jayden Daniels]] — QB, WAS — hosts project rocky rookie year despite strong camp buzz; weak supporting cast cited as the limiter
- [[J.J. McCarthy]] — QB, MIN — Waldman favors him ~60/40 over Sam Darnold for Week 1 job; Minnesota called his ideal fit
- [[Spencer Rattler]] — QB, South Carolina prospect — better tape at South Carolina than Oklahoma per Waldman, moves better in the pocket than expected; strong vs. one of man/zone, poor vs. the other — "half a game" right now; Angelo's Senior Bowl take adds a real maturity/coachability angle — self-aware about a cocky younger self — on a mixed on-field week *(2024 pre-draft takes, stale)*
- [[Tanner Mordecai]] — QB, Wisconsin prospect (SMU/Oklahoma transfer) — rocky transfer-year tape, rebounded late vs. LSU; Waldman's grade is future backup of value, not a starter *(2024 pre-draft takes, stale)*
- [[Jack Plummer]] — QB, Louisville prospect — accuracy is the whole story per Waldman: "if he had the accuracy, he would probably be a top-five quarterback in this class" *(2024 pre-draft takes, stale)*
- [[Joe Milton III]] — QB, Tennessee prospect — the class's clearest boom/bust arm-talent case; top-five-pick ceiling, out-of-the-league floor; Malik Willis comp, explicit "Jordan Love treatment" recommended by Waldman *(2024 pre-draft takes, stale)*
- [[Desmond Ridder]] — QB, ARI — traded from Atlanta for Rondale Moore after Falcons signed Kirk Cousins
- [[Kirk Cousins]] — QB, ATL — Achilles recovery in question for accuracy/mechanics, not just availability; Penix takeover risk by Wk 7-8
- [[Daniel Jones]] — QB, NYG — flat "not the answer" per Waldman; expects a two-step Giants succession (a developmental pick first, a real QB1 pick once they're ready to move on) rather than an immediate bench *(2024 takes, stale)*
- [[Ryan Tannehill]] — QB, TEN — speculative Pittsburgh reunion with former OC Arthur Smith; projected as a Joe-Flacco-style veteran room presence, not a starter bet *(2024 takes, stale)*
- [[Aaron Rodgers]] — QB, NYJ — both hosts feel it on a return to form post-Achilles; intangible/effort-based case ("too obsessed with the game") rather than tape-based *(2024 takes, stale)*
- [[Matthew Stafford]] — QB, LAR — Waldman comps his ball placement to 'Mahomes 1.0'; less mobile, more mistake-prone
- [[Joe Burrow]] — QB, CIN — Waldman 'Goldilocks' on QB7 best ball ADP; top-3 QB talent when healthy
- [[Kenny Pickett]] — QB, PHI — Traded to Philadelphia as Jalen Hurts's backup; pressure-processing concerns limited his Pittsburgh ceiling per Waldman.
- [[Austin Reed]] — QB, West Florida — Waldman: aggressive Stafford/Warner-flavored arm, likely journeyman prospect
- [[Brennan Armstrong]] — QB, NC State — Waldman: lefty, developmental-league grade, needs to unlock arm talent
- [[Carter Bradley]] — QB, South Alabama — Waldman: mechanics need work, overreacts to pressure, dev-league grade
- [[Devin Leary]] — QB, Kentucky — Waldman: roster-spot arm, limited by trail coverage and pressure ID
- [[Emory Jones]] — QB, 2024 prospect — Waldman: athletic/accurate but behind on technical foundation
- [[Gunner Watson]] — QB, 2024 prospect — Waldman: accurate arm, lacks conceptual acumen to read leverage
- [[Jordan Travis]] — QB, Florida State — Waldman: aggressive tight-window thrower, Jeff Blake/Keenum/Garcia comp
- [[Keaton Slovis]] — QB, USC — Waldman: developmental arm, poor peripheral vision/pressure recognition
- [[Michael Pratt]] — QB, 2024 prospect — Waldman: high-floor fundamentals, too slow to throw underneath/away
- [[Sam Hartman]] — QB, 2024 prospect — Waldman: technically sound but capped arm limits him to distributor role
- [[Deshaun Watson]] — QB, CLE — Waldman 'open to' bounce-back after improved late-2023 spurts, ahead of Jeudy trade addition (2024, stale)
- [[Jacoby Brissett]] — QB, WAS (FA) — Harmon's top pick as Minnesota's veteran bridge QB post-Cousins
- [[Will Levis]] — QB, TEN - Harmon: Titans spending on weapons (Ridley) to properly evaluate him; unsure McCarthy is real upgrade
- [[Sam Darnold]] — QB, MIN — Signs with Minnesota; Waldman rejects any Baker Mayfield redemption framing, calls him 'a placeholder for somebody else at best.'
- [[Sam Howell]] — QB, SEA — Trades to Seattle to push Geno Smith; Waldman expects Smith to keep the job into midseason at least.
- [[Aidan O'Connell]] — QB, LV — Pierce publicly backing him over Gardner Minshew; ceiling tied to cutting reckless downfield decisions
- [[Geno Smith]] — QB, SEA — Waldman backs off frontline-starter grade; Sam Howell/Ryan Grubb create real competition (2024-04-15)
- [[Zach Wilson]] — QB, NYJ — Waldman: Baker-Mayfield-style redemption in range if he matures; could be out of league in years
- [[Josh Allen]] — QB, BUF — Waldman avoiding him in Best Ball at current ADP despite Diggs trade fallout
- [[Trevor Lawrence]] — QB, JAX — Waldman's bargain QB1, 2023 dip blamed on O-line/Bigsby turnovers, not talent
- [[Trey Lance]] — QB, DAL — Waldman still grades top-2-3 in his class, good Cowboys fit; not a bust, per 2024-04-15
- [[Malik Willis]] — QB, TEN — rumored cut/bubble candidate; Waldman's ceiling comp is Tyler Huntley, may be asked to switch positions
- [[Jameis Winston]] — QB, CLE — Waldman's pick as 2024's 'Joe Flacco': cheap Stefanski-scheme fit as Deshaun Watson injury insurance.

### Running Backs
- [[Christian McCaffrey]] — RB, SF — unqualified 2024 1.01 for Waldman again, edging [[CeeDee Lamb]] and [[Tyreek Hill]]; age 28 explicitly dismissed; the "leverage over the field" case; Harmon: even a strong Detroit run defense "isn't stopping that train" in the NFC Championship *(2024 takes, stale)*
- [[Bijan Robinson]] — RB, ATL — Knight (Falcons reporter): 2023 usage was a play-calling failure, offense 'really close' with him healthy (2024 takes, stale)
- [[Jahmyr Gibbs]] — RB, DET — Waldman's 2023 call, vindicated (RB9); he then flips off him for 2024 on price, not talent *(2023 takes, stale)*
- [[James Cook]] — RB, BUF — "elite" question answered yes; fully unleashed in year two, "a real shot" at top-12 value in 2024, floated as the next Ekeler *(2024 takes, stale)*
- [[Tyler Goodson]] — RB, IND — explosive, natural cutback runner masked by Iowa's scheme; Waldman's long-term Colts preference *(2023 takes, stale)*
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, HOU — had taken the job outright from Dameon Pierce in December 2023, but Waldman reverses: no longer Houston's presumptive 2024 starter, expects a free-agent RB (Jacobs or Henry) to take over; a rough Divisional Round game (9 carries, 22 yards) reinforces the need for an upgrade, though Harmon notes it followed a genuinely strong late-season stretch *(2024 takes, stale)*
- [[Saquon Barkley]] — RB, PHI — Signs with Philadelphia (not Waldman's predicted Houston); expects lead role, 'vengeance tour' upside on a loaded offensive line.
- [[Derrick Henry]] — RB, BAL — Signs with Baltimore, Waldman's happiest move of free agency; 2023 speed data shows no decline, heavy Best Ball shares.
- [[Joe Mixon]] — RB, HOU — Traded from Cincinnati; Waldman likes the fit with C.J. Stroud, downplays breakaway-rate criticism as overblown.
- [[Alvin Kamara]] — RB, NO — cap-squeeze uncertainty in New Orleans, but a weeks-4-17 top-4 fantasy back when playing; a Shanahan-tree scheme (new OC Klint Kubiak) could extend his effective range *(2024 takes, stale)*
- [[Breece Hall]] — RB, NYJ — "averts one disaster at a time"; processes fast but not two steps ahead, and Waldman still expects big-time yardage with a better line *(2023 takes, stale)*
- [[Nick Chubb]] — RB, CLE — Waldman keeps him RB40 post-ACL/MCL trusting the recovery; Bob Harris (untracked) says fade him entering age 28.
- [[David Montgomery]] — RB, DET — still projected fringe top-20 on TD equity/role despite Gibbs workload increase; not rendered obsolete
- [[Isiah Pacheco]] — RB, KC — the pace-control negative case: one speed, "zero or a hundred"; running well anyway through the postseason, open bell-cow question, but a Joe Thuney injury is a live threat to his AFC Championship workload; one of the pieces giving KC enough to "play with anyone" per Waldman post-AFC-Championship; two Super Bowl LVIII fumbles read as a 2024 buying opportunity, not a red flag — KC never benched him, "should be a top-10 running back," ADP currently round 2-3 turn *(2024 takes, stale)*
- [[Kyren Williams]] — RB, LAR — Waldman/Harris call him overrated at RB8 price; role likely shifts toward receiving as Corum eats early-down work
- [[Kenneth Walker III]] — RB, SEA — Waldman draft him higher than market: Pete Carroll's pattern is to "covet" one back until injury forces a change, and Walker is currently that back; Carroll is now out, new HC Mike McDonald in, reopening the usage-pattern question *(2024 takes, stale)*
- [[Raheem Mostert]] — RB, MIA — the cheap half of Miami's committee; both hosts value him as a 2024 RB2, expect more work to shift to Achane *(2024 takes, stale)*
- [[James Connor]] — RB, ARI — both hosts hanging on for 2024; "toast" skepticism reframed as a second-contract finance story, not a talent decline; Michael Carter cuts into but doesn't replace him *(2024 takes, stale)*
- [[Aaron Jones]] — RB, Free Agent — released by GB after Jacobs signing; still good healthy, but 30 and injury-prone
- [[Zamir White]] — RB, LV — Waldman calls him underpriced on anticipated volume, but must prove out as receiver/blocker or cede passing downs to Laube
- [[Tank Bigsby]] — RB, JAX — overrated by "about a round and a half" pre-draft per Waldman; costly drops, indecisive runner; opportunity would still get him 1,000 yards *(2024 takes, stale)*
- [[Kendre Miller]] — RB, NO — Waldman's preferred dynasty stash over Bigsby, on opportunity alone *(2024 takes, stale)*
- [[Chase Brown]] — RB, CIN — "I love Chase Brown"; Waldman's other preferred dynasty stash over Bigsby *(2024 takes, stale)*
- [[Tony Pollard]] — RB, TEN — Signs with Tennessee on a hedge-y deal; Waldman calls him 'the shiny object,' drops Tyjae Spears's redraft value further.
- [[Michael Carter]] — RB, ARI — Waldman's dark-horse over Trey Benson as pass-pro/receiving complement to James Conner; 'basically free money' late/waiver
- [[Austin Ekeler]] — RB, WASH — Signs cheap 2-yr deal; Waldman reads it as a complementary/McKissick-type role, bad news for Brian Robinson Jr.'s workload split.
- [[Josh Jacobs]] — RB, GB — Waldman moving him top-10, strong pass-catcher fit in LaFleur's offense
- [[Najee Harris]] — RB, PIT — option decline is a leverage/money move per Waldman's Steelers.com source; long-term future still likely
- [[Jaylen Warren]] — RB, PIT — intriguing complementary piece under new OC Arthur Smith, but explicitly tempered — "if you were waiting for a full-on revival, I don't think we're going to get that" *(2024 takes, stale)*
- [[Jordan Mason]] — RB, SF — Waldman's preferred McCaffrey-injury contingency over Elijah Mitchell, on versatility and price *(2024 takes, stale)*
- [[Elijah Mitchell]] — RB, SF — got more 2023 volume than Mason down the stretch, but still Waldman's #2 McCaffrey handcuff on price *(2024 takes, stale)*
- [[Tyler Allgeier]] — RB, ATL — Bijan Robinson's complementary piece; "plays really well when in the system they put him in" *(2024 takes, stale)*
- [[Blake Corum]] — RB, LAR — 'wildly overdrafted' per Waldman/Harris; real contingent value if Williams hurt, but McVay historically avoids rookies
- [[De'Von Achane]] — RB, MIA — spectacular rookie efficiency, but a real 2024 overrated risk: great to the edge, only good between the tackles, exploitable once defenses take the edge away; fine value in rounds 4-5, dangerous priced top-3 *(2024 takes, stale)*
- [[Braelon Allen]] — RB, NYJ — Waldman rates his long-term outlook behind Breece Hall below Guerendo's behind McCaffrey.
- [[Jonathan Brooks]] — RB, CAR — won't be ready for camp after ACL tear; Waldman expects a PUP stint and a stronger finish (Breece Hall comp).
- [[Blake Watson]] — RB, DEN — Angelo's biggest 2025 riser dark horse, ranked ahead of Estime on ADP-value grounds
- [[Jabari Small]] — RB, Tennessee prospect — Shrine Game name Waldman likes; undersized (205 lbs) but runs hard with good vision and decision-making *(2024 pre-draft takes, stale)*
- [[Ray Davis]] — RB, Kentucky prospect — 5'8"/217, Frank-Gore-esque build that plays more fluidly than the size suggests; all-three-phases competent, projected 4th-5th round per Angelo *(2024 pre-draft takes, stale)*
- [[Dylan Laube]] — RB, LV — Waldman sees real receiving-down opportunity behind Zamir White (~5 catches/season projected)
- [[Daijun Edwards]] — RB, Georgia prospect — quick and shifty despite playing through an MCL injury, good pass catcher/blocker; Jalen-Richard floor, dynamic-James-White ceiling; likely the most-rostered of Waldman's three underrated 2024 RBs on name value alone *(2024 pre-draft takes, stale)*
- [[George Holani]] — RB, Boise State prospect — the highest-variance of Waldman's three underrated 2024 RBs; real injury history but explosive flash (7 missed tackles forced on one screen vs. UCLA), needs added weight to profile as a committee back *(2024 pre-draft takes, stale)*
- [[Deshaun Fenwick]] — RB, Oregon State prospect — Shrine Game favorite; Leonard-Fournette-adjacent big-back build, gap-scheme thumper, projects as a reserve "B-back" *(2024 pre-draft takes, stale)*
- [[Brian Robinson Jr.]] — RB, WAS — Cliff Kingsbury's move to Washington OC "doesn't hurt as much as people think" per Waldman (James Connor/Arizona comp); red-zone-touch-dependent, projects low-end RB1/high-end RB2 *(2024 takes, stale)*
- [[Tyjae Spears]] — RB, TEN — stock rising regardless of Derrick Henry's free-agency outcome, on receiving work alone; new O-line coach Bill Callahan and a likely Henry departure both add further tailwind; Jerome Ford value comp, "more talented" per Waldman *(2024 takes, stale)*
- [[Mario Anderson]] — RB, Memphis prospect (future class) — flagged by Waldman as the next name in Memphis's RB pipeline (Pollard, Henderson, Gainwell); shifty, good vision, Ray Davis size/balance comp *(2024 pre-draft takes, stale)*
- [[Cody Schrader]] — RB, Missouri prospect — Angelo's late-round pick to make a roster and stick; 1,800 total yards/14 TDs at Missouri, Senior Bowl standout, graded a smart, reliable long-term role player rather than a star *(2024 pre-draft takes, stale)*
- [[Kendall Milton]] — RB, Georgia prospect — unique size/speed at 6'1"/220-225; hasn't yet shown the Eddie-George-level ceiling his HS recruiting profile promised; combine/pro day season is the swing factor for his stock *(2024 pre-draft takes, stale)*
- [[Kimani Vidal]] — RB, LAC — Waldman buying as a cheap dynasty stash; Austin Ekeler size comp, thin/injury-prone depth chart ahead
- [[Will Shipley]] — RB, Clemson prospect — underrated receiving-back profile with real speed (6.4s HS 55m); combine 40 time is the key swing event for his stock; projects as a Dion-Lewis/James-White-style complementary role *(2024 pre-draft takes, stale)*
- [[Rasheen Ali]] — RB, Marshall prospect — explosive pre-ACL flash back who returned to the same level; graded the best RB at the 2024 Senior Bowl for his limited reps there; ball security is the swing risk *(2024 pre-draft takes, stale)*
- [[Jaylen Wright]] — RB, MIA — Angelo projects him as Dolphins' touch leader by end of 2025 as Mostert/Connor age out
- [[Dillon Johnson]] — RB, Washington prospect — Waldman's fourth early-round-talent name; played through multiple injuries into the national title game, some of the best contact balance in the class, but a real breakaway-speed/explosiveness ceiling concern *(2024 pre-draft takes, stale)*
- [[Trey Benson]] — RB, ARI — dynasty comp to peak David Johnson; expected to take over lead role by year two behind James Connor
- [[Bucky Irving]] — RB, Oregon prospect — a [[Devin Singletary]]-style boom/bust comp; real disagreement between hosts on how close he already is to the "on schedule" discipline that would unlock a "Singletary-plus" outcome *(2024 pre-draft takes, stale)*
- [[Marshawn Lloyd]] — RB, GB — Angelo's biggest 2025 RB riser pick; role hinges on Josh Jacobs' 2025 contract out
- [[Khalil Herbert]] — RB, CHI — Waldman prefers him over Roschon Johnson as the value side of a Bears RB timeshare
- [[Roschon Johnson]] — RB, CHI — Waldman: RB35 ADP near his peak-production ceiling; Herbert preferred as the better value
- [[Javonte Williams]] — RB, DEN — Waldman: 2023 dud likely lingering knee-injury effect, not decline; value play
- [[Samaje Perine]] — RB, DEN — Waldman: elite YAC receiving back, will complicate a Javonte Williams breakout
- [[Rachaad White]] — RB, TB — RB14 ADP; Waldman buying the dip, dismisses Bucky Irving as a real workload threat
- [[DeAndre Swift]] — RB, CHI — Signs 3yr/$8M with Chicago; Waldman expects part-time, mid-range production, not a bell-cow workload, behind Caleb Williams.
- [[Alexander Mattison]] — RB, LV — Signs as Zamir White's backup; Waldman defends his zero-TD 2023 as a Minnesota QB/red-zone issue, not a talent flaw.
- [[Zach Moss]] — RB, CIN — Signs post-Joe Mixon; pairs with Chase Brown as a solid 1-2 punch per Waldman, contingent on Joe Burrow's health.
- [[Aidan Robbins]] — RB, BYU (2024 prospect) — Waldman: strong downhill gap runner, needs to press deeper to fit zone schemes too
- [[Audric Estime]] — RB, DEN — could inherit two-down banger role from Javonte Williams (FA next year), per Angelo
- [[Isaac Guerendo]] — RB, SF — Waldman: 'Elijah Mitchell 2.0' with more speed; prefers his long-term spot over Braelon Allen's.
- [[Isaiah Davis]] — RB, South Dakota State (2024 prospect) — Waldman: strong man-coverage route runner, needs more decisive vision as a runner
- [[Jalen White]] — RB, Georgia Southern (2024 prospect) — Waldman: solid short-yardage gap runner, decision-making/leverage reads are the issue
- [[Jase McClellan]] — RB, Alabama (2024 prospect) — Waldman: sharp cutter, a competent runner; unclear if that means a competent NFL starter
- [[Montrell Johnson]] — RB, Florida (2024 prospect) — Waldman: good leverage reader/gap runner, misses third-level lanes bouncing to open backers
- [[Tyrone Tracy Jr.]] — RB, NYG — Angelo's biggest 2025 RB riser pick; open backfield role beyond Nabers, still free in rookie ADP
- [[Miyan Williams]] — RB, Ohio State (2024 prospect) — Waldman: smart, physical; ceiling of a Peyton-Barber-type committee back
- [[Frank Gore Jr.]] — RB, Southern Miss (2024 prospect) — Waldman: smart cutback runner, must prove he can transcend size like Devin Singletary
- [[Emani Bailey]] — RB, TCU (2024 prospect) — Waldman: inconsistent gap reads, too tight or too wide; needs better control/vision
- [[Dylan McDuffie]] — RB, Kansas (2024 prospect) — Waldman: willing tight-crease runner, Raheem-Mostert-lite burst without the blink-of-an-eye separation
- [[Michael Wiley]] — RB, Arizona (2024 prospect) — Waldman: needs better leverage attacking defenders, same early issue Jahmyr Gibbs had
- [[Gus Edwards]] — RB, LAC — Waldman: underrated best-ball value on Greg Roman history, 13 TDs, could figure prominently
- [[Travis Etienne Jr.]] — RB, JAX — Best Ball RB6, near ceiling but preferred over unproven Tank Bigsby
- [[J.K. Dobbins]] — RB, LAC — Waldman buying Dobbins at ~RB20 ADP in the Greg Roman offense; best-ball flyer (2024 speculation, stale).
- [[Chuba Hubbard]] — RB, CAR — Waldman feeling Hubbard as CAR's de facto starter at RB39 ADP, clearly ahead of Miles Sanders (2024 speculation, stale).
- [[Miles Sanders]] — RB, CAR — Angelo blames poor Panthers infrastructure/ownership, not talent loss, for his decline
- [[Dylan Johnson]] — RB, TEN UDFA — Waldman's other favorite; projects as low-red-zone role Titans currently lack
- [[Eric Gray]] — RB, NYG — new page; Waldman has Gray 60/40 over Tyrone Tracy Jr. for the complementary role behind Singletary
- [[Dameon Pierce]] — RB, HOU — new page; Waldman: starter role over, misused as a non-receiving back despite receiving ability at Florida
- [[Deuce Vaughn]] — RB, DAL — not viewed as a 2024 fantasy factor; buried behind Elliott/Dowdle regardless of role changes
- [[Justin Strong]] — RB, IND (UDFA) — tryout with Colts; Waldman flags burst/vision but wants a deep-league watch, not a draft pick
- [[Zach Charbonnet]] — RB, SEA — new page; Waldman sees him capping Kenneth Walker's ceiling as Seahawks trend pass-heavy under new OC Ryan Grubb

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — Waldman: 1-2 with Ja'Marr Chase, negligible gap; would take Chase today only for Cincinnati's QB certainty edge
- [[Ja'Marr Chase]] — WR, CIN — Waldman: locked in almost any scenario if Burrow stays; slight dynasty edge over Justin Jefferson on QB certainty
- [[Keenan Allen]] — WR, CHI — traded from LAC; Harmon: role-narrowed not declining, elite on layup routes, great high-low fit w/ D.J. Moore
- [[Amon-Ra St. Brown]] — WR, DET — same profile as Allen, with play-caller continuity as the tiebreaker; Harmon's #2 overall receiver remaining in the playoffs but #1 by team value ("in a runaway") — now beating press-man as well as zone; entering his contract year, "up for a big payday pretty soon" *(2024 takes, stale)*
- [[Jameson Williams]] — WR, DET — RP split shows bust-level early '23 tape but strong week-15-on zone/dig numbers; comp range Corey Coleman to Gabe Davis
- [[Brandon Aiyuk]] — WR, SF — Steelers trade rumor (Daniel Jeremiah) read as contract leverage per Harmon; expects Aiyuk stays in SF
- [[Tee Higgins]] — WR, CIN — Waldman/Angelo expect Cincinnati to move on from Higgins (walk or midseason trade), durability the key risk.
- [[Jordan Addison]] — WR, MIN — RP profile flags man/press weakness (51.5%); Harmon projects capable No. 2, not a WR1
- [[Jayden Reed]] — WR, GB — elite RP profile (77% vs press); Harmon says role, not talent, is the risk
- [[Noah Brown]] — WR, HOU — best Texans receiver whenever Nico Collins is out; a conditional weekly start; placed on IR during the 2023 playoff run *(2024 takes, stale)*
- [[John Metchie III]] — WR, HOU — flashed filling in for an injured Noah Brown in the Wild Card win, but downgraded after the Divisional Round — Harmon: "has proven nothing to this point in his career," replacement-level depth, not a real answer opposite Nico Collins *(2024 takes, stale)*
- [[Xavier Hutchinson]] — WR, HOU — faint praise, an Allen-Lazard-type depth/blocking piece rather than a real target threat *(2024 takes, stale)*
- [[Tre Tucker]] — WR, LV — "aspiring Jaylen Waddle" in the Tyreek Hill role; high variance, not yet a complete player *(2023 takes, stale)*
- [[Treylon Burks]] — WR, TEN — Waldman: 50/50 to stick vs. get cut, make-or-break year; Bob Harris more bearish, predicts a cut
- [[DeAndre Hopkins]] — WR, TEN — the "old man game" archetype; experts split on how much tail is left *(2023 takes, stale)*
- [[Adam Thielen]] — WR, CAR — reputation as a possession receiver misreads a genuinely elite athletic profile *(2023 takes, stale)*
- [[Deebo Samuel]] — WR, SF — Angelo calls him increasingly scheme-dependent/'obsolete' with McCaffrey in the backfield; floats him as the trade candidate
- [[Malik Nabers]] — WR, NYG -- Koh/Harmon comp him to Waddle's rookie year: heavy underneath volume, TD/efficiency the risk (2024 proj)
- [[Marvin Harrison Jr.]] — WR, ARI — Waldman praised his combine-skip decision as the class's best pre-draft answer, worth +5 board spots
- [[Rome Odunze]] — WR, CHI — Waldman sees outside X role, not a slot-heavy Njigba clone despite shared Shane Waldron scheme
- [[Keon Coleman]] — WR, BUF -- horrible man-press profile (20th pct) for X; Harmon projects him to slot long-term
- [[Ainias Smith]] — WR, PHI — Waldman likes his path to a Danny Woodhead-style role as Eagles' emerging third receiver
- [[Michael Gallup]] — WR, DAL — Harms is out on a 2024 rebound; doesn't create separation as an X, may not even be in Dallas, projects a Chris-Conley-style "good player, not fantasy relevant" career *(2024 takes, stale)*
- [[Brian Thomas Jr.]] — WR, JAX — Angelo's top overrated-by-fit pick; heavy target competition pushes him to a tougher outside role
- [[Ladd McConkey]] — WR, LAC -- Koh's most aggressive non-top-tier rookie WR line (76/912/7.7); Harmon takes over on 775.5 yds (2024 proj)
- [[Ricky Pearsall]] — WR, SF — Angelo expects strong camp but a limited, undefined rookie-year role behind Aiyuk/Deebo
- [[Troy Franklin]] — WR, DEN — fell to R4; strong man/zone marks but poor press/hands, size a real concern
- [[CeeDee Lamb]] — WR, DAL — Bob Harris's pick for 2024 #1 overall over McCaffrey; Waldman ranks him 2nd *(2024 takes, stale)*
- [[Tyreek Hill]] — WR, MIA — 3rd in Waldman's 2024 top tier, but Bob Harris's personal #2 as "an old-school wide receiver one" *(2024 takes, stale)*
- [[Mike Evans]] — WR, TB — re-signed 2yr/$52M; 2023 was career-best charted season, 2022 dip was scheme not decline (Harmon 3/5)
- [[Rashid Shaheed]] — WR, NO — "WR4 with WR3 upside," a good Best Ball play; Waldman skeptical New Orleans sees him as more than a speed-role piece unless a coach says otherwise in camp *(2024 takes, stale)*
- [[Jerry Jeudy]] — WR, CLE — Harmon's official RP profile: plateaued/worsened vs zone (8th %ile), better fit at flanker than slot
- [[Courtland Sutton]] — WR, DEN — "always thought was overrated" per Waldman; not a great route runner, "throw him five balls for him to catch three" *(2024 takes, stale)*
- [[Chris Godwin]] — WR, TB — Waldman's strongest Bucs-receiver praise in the wiki: a Pro-Bowl-level, all-alignment "complete skill-set guy," Gronkowski-versatility comp; health/age the only live question; Harmon's retrospective — Tampa's 2023 move of him to a primarily outside role was "a gigantic mistake" not fixed until Week 14-15 — is now more relevant with OC Dave Canales (who fixed it) leaving for Carolina's HC job *(2024 takes, stale)*
- [[Rashad Bateman]] — WR, BAL — Harmon back on the bandwagon after contract extension; projects ~600 yards, Keenan Allen mold.
- [[Stefon Diggs]] — WR, HOU — Waldman's biggest Houston WR trio gamble on age cliff, still buying at R2-3 ADP
- [[Cooper Kupp]] — WR, LAR — not hung up, but Puka Nacua's emergence caps his ceiling; "days of being that true alpha... are over, draft accordingly"; Harmon puts it at a "50/50 shot" that repeated ankle injuries have permanently sapped his explosiveness rather than a one-year dip, and RP charting now has Nacua separating better vs. man *(2024 takes, stale)*
- [[Quentin Johnston]] — WR, LAC — historically bad rookie RP profile (44.1% vs. man, top-5 worst ever); Harmon: reclamation project, unclear 2024 role
- [[Jaxon Smith-Njigba]] — WR, SEA — Harmon projects ~900 yds median (400 low-end) as JSN passes Lockett; vertical Grubb scheme fits his intermediate routes
- [[Zay Flowers]] — WR, BAL — in Waldman's top rookie WR tier but more boom/bust, entirely on how much Lamar Jackson's offense trusts him; the earlier "don't trade London for Flowers" debate is now resolved in London's favor after the full season; Harmon's #4 remaining playoff receiver with real "superstar tier" upside language, but a tough outside-alignment matchup vs. Kansas City's AFC Championship secondary *(2024 takes, stale)*
- [[Puka Nacua]] — WR, LAR — Waldman's #3 2023 rookie WR, #1 by pure production; Harstad's post-rookie model scores his rookie year the single best in its 2006-2023 sample, expanding the "big four" to a "big five"; long-term outlook tied to Stafford's remaining runway *(2024 takes, stale)*
- [[Tank Dell]] — WR, HOU — elite outbreaking-route separator/dig-route ace as rookie; weaker vs. zone. (2024 takes, stale)
- [[Nico Collins]] — WR, HOU -- historic year-3 RP jump (77.6% vs. man, 82.5% vs. press); Harmon says market underrates him
- [[Josh Downs]] — WR, IND — elite RP profile: 93rd-pctile vs. man, NFL-best off-script production; Shepherd-level ceiling, not a breakout
- [[Marvin Mims Jr.]] — WR, DEN -- rookie film 'a disaster...nonfunctional,' RP data poor (2024-03-28, stale watch)
- [[Jalen Hyatt]] — WR, NYG — Waldman "a little more convinced" despite a bad Giants QB situation *(2024 takes, stale)*
- [[Rashee Rice]] — WR, KC — Harmon comps rookie role (slot/screen-heavy) to Juju Smith-Schuster/Jarvis Landry; St. Brown is the upside outcome
- [[Davante Adams]] — WR, LV — feeling it on staying in Vegas now that Luke Getsy (his old Packers OC) is the new OC; falling ADP (late 2nd round) framed as an explicit buy, "regardless of quarterback" *(2024 takes, stale)*
- [[Gabe Davis]] — WR, JAX (signed FA) - 3yr/$39M; Harmon: was 7th percentile vs man in 2023, pairs into a bottom-5 WR room
- [[Khalil Shakir]] — WR, BUF — Waldman: could be Bills' #2/3 WR, bargain, earns Josh Allen's trust on tough throws
- [[Drake London]] — WR, ATL — Harmon projects 1,300 yds on new McVay-tree scheme, more inside alignment vs. Arthur Smith's static usage
- [[Michael Wilson]] — WR, ARI — a genuinely good route runner in the "aspiring Michael Thomas" mold; top-24 value if he can finally stay healthy *(2024 takes, stale)*
- [[George Pickens]] — WR, PIT — deep/outside route tree may clash with Arthur Smith's in-breaking scheme; still better than under Canada
- [[Diontae Johnson]] — WR, CAR — Harmon: career-best efficiency metrics in 2023 masked by poor role; scheme fit under Canales/Idzik projects bounce-back
- [[Tyler Lockett]] — WR, SEA — still part of "one of the best three-person WR trios in the NFL," but his roster spot is a real 2024 question under new HC Mike McDonald given his cap hit; floated as a fit to reunite with OC Shane Waldron in Chicago *(2024 takes, stale)*
- [[Terry McLaurin]] — WR, WAS — Harmon: potential career season via heavy RPO/first-read usage with Jayden Daniels under new OC Kliff Kingsbury
- [[Wan'Dale Robinson]] — WR, NYG — real after-the-catch and contested-catch value; outlook entirely a Giants-QB question *(2024 takes, stale)*
- [[Ronnie Bell]] — WR, SF — a name to know mostly for injury-contingency reasons behind Aiyuk/Deebo, not his own emergence *(2024 takes, stale)*
- [[Dontayvion Wicks]] — WR, GB — LaFleur comps his route running to Davante Adams; Harmon's sleeper breakout pick. (2024 takes, stale)
- [[Romeo Doubs]] — WR, GB — part of Green Bay's "big three," but "a little less multi-dimensional" than what Wicks offers; Harmon's clear #4 of the group — solid vertical player and best 2023 postseason of the four, but not a path to more *(2024 takes, stale)*
- [[Christian Watson]] — WR, GB — speed is unquestioned; durability is the entire 2024 question mark; Harmon's real new knock — can't make the true-number-one-receiver case for him "without mentioning height," unlike Reed or Wicks *(2024 takes, stale)*
- [[Cedric Tillman]] — WR, CLE — bottom-tier post-rookie model score; the "Amari Cooper-esque hopeful" behind Cooper himself, free add but not worth paying up for *(2024 takes, stale)*
- [[Tyler Scott]] — WR, CHI — "overrated on speed" pre-draft per Waldman; used as a one-dimensional RPO/deep-shot option, a Darnell-Mooney-before-he-developed comp *(2024 takes, stale)*
- [[Jonathan Mingo]] — WR, CAR — one of only two 2023 rookie WRs to open as a Week 1 starter, but tanked by historically bad Carolina QB play; Waldman revising down hard on coaching-change risk, not talent *(2024 takes, stale)*
- [[Demario Douglas]] — WR, NE — inverted man(69%)/zone(76% but bottom-quartile) profile; muddled 2024 role behind Polk, Baker, Bourne [Dynasty]
- [[Malik Washington]] — WR, MIA — 6th-round slot fit; McDaniel personally lobbied to draft him, Harmon very high
- [[Xavier Legette]] — WR, CAR — Harmon: motion/gadget role like Deebo Samuel-lite, not outside X, likely third receiver early
- [[Malachi Corley]] — WR, NYJ -- slot-only gadget profile (66% man/85% zone); blocks Xavier Gipson's slot role
- [[Javon Baker]] — WR, NE -- co-host Coe's top sleeper; strong contested-catch/deep marks but developmental X profile
- [[Roman Wilson]] — WR, PIT — Harmon projects speed-slot/flanker role on vertical & play-action routes; take the under vs. Diontae Johnson volume
- [[Devontez Walker]] — WR, BAL -- Ravens 4th-rounder; Harmon's worst RP man-coverage score charted in 4+ years, buried depth chart
- [[Brendan Rice]] — WR, LAC — 7th-rounder w/ elite in-breaking numbers, poor vertical/ball-tracking; deep sleeper per Matt Harmon
- [[J. Michael Sturdivant]] — WR, UCLA prospect (Cal transfer) — 6'3"/205, high-end traits that "didn't really emerge at the highest level" of production per Waldman; declared, ungraded *(2024 pre-draft takes, stale)*
- [[Marquise Brown]] — WR, KC — Waldman: now de facto WR1 with Rice suspended; durability (11-13 game career-high) is the main risk.
- [[Skyy Moore]] — WR, KC — Harmon calls his outside-receiver usage a "mis-evaluation" of the player; doesn't expect him in Kansas City's plans and would rather see him traded to restart elsewhere *(2024 takes, stale)*
- [[A.J. Brown]] — WR, PHI — Harmon predicts new OC Kellen Moore could shift Brown into the slot as primary read; Koh disagrees
- [[DeMarcus Robinson]] — WR, LAR — Waldman: WR99 ADP 'free square'; late-2023 DFS run buildable but temper expectations
- [[Jahan Dotson]] — WR, WAS — Waldman: skilled WR3/matchup WR2, but unsure new Kingsbury-called offense unlocks him
- [[Adonai Mitchell]] — WR, IND — Harmon: great value/fit at 52nd overall, fills needed vertical/boundary X role
- [[Xavier Worthy]] — WR, KC — first KC WR off the board in best ball; Waldman 'feeling it' on gut despite acknowledging aggressive price
- [[Ja'Lynn Polk]] — WR, NE -- Harmon high on rookie; strong zone/contested-catch marks, projects a Puka Nacua-lite usage role
- [[Michael Pittman Jr.]] — WR, IND — team-friendly deal; Harmon calls him a true, underrated WR1, eyes top-10 breakout in 2024
- [[D.J. Moore]] — WR, CHI — Harmon: versatile vertical/man-beating X, ideal high-low duo w/ new teammate Keenan Allen for rookie QB
- [[Calvin Ridley]] — WR, TEN (signed FA) - 4yr/$92M; Harmon: overpay but still elite separator, good fit off Titans static-X usage
- [[Mike Williams]] — WR, NYJ -- health is the swing factor for whole room; ACL/age risk, no real depth if he's out
- [[Tyler Harrell]] — WR, deep sleeper (Miami) — Waldman: elite play speed, 'as fast as Xavier Worthy' but unproven, injury-plagued (2024 prospect, stale)
- [[Amari Cooper]] — WR, CLE — Waldman: secure top target post-Jeudy trade, 'ain't going anywhere,' upgrade over Sutton for Watson (2024, stale)
- [[Elijah Moore]] — WR, CLE - Harmon: good player, best in slot/off-ball; beats press/zone better than Jeudy, projects WR3
- [[Christian Kirk]] — WR, JAX - Harmon: best receiver on Jaguars roster, slot-mostly; now in a bottom-5 receiver room
- [[Darnell Mooney]] — WR, ATL — Harmon projects vertical-slot/flanker role (60-40 split), a WR3-caliber 'a 3'
- [[Anthony Gould]] — WR, Oregon State (2024 prospect) — Waldman: sub-package contributor early, needs man-coverage refinement to start
- [[Bub Means]] — WR, Pittsburgh (2024 prospect) — Waldman: open-field skills, ceiling of a starting split end one day
- [[Jalen McMillan]] — WR, TB — Waldman expects immediate WR3 role, grades him ahead of Ja'Lynn Polk with Chris Godwin-type ceiling
- [[Jermaine Burton]] — WR, CIN — both hosts' top reach and biggest 2025 riser pick; projected heir to Tee Higgins
- [[Johnny Wilson]] — WR, PHI -- Harmon's most uncertain evaluation in the class; huge X frame, bad hands, risk of premature TE conversion
- [[Joshua Cephus]] — WR, UTSA (2024 prospect) — Waldman: slippery zone/YAC weapon, needs man skills to start outside
- [[Kobe Hudson]] — WR, UCF (2024 prospect) — Waldman: deep-threat sub-package piece, could grow into starting outside option
- [[Luke McCaffrey]] — WR, Rice (2024 prospect) — Waldman: Christian McCaffrey's brother, patient open-field runner, needs route polish
- [[Ryan Flournoy]] — WR, Southeast Missouri State (2024 prospect) — Waldman: NFL athlete, contributor-vs-reserve hinges on releases/breaks
- [[Xavier Weaver]] — WR, Colorado (2024 prospect) — Waldman: Jordan Addison starter kit, route game a starting-caliber foundation
- [[Michael Thomas]] — WR, FA — Speculative Miami fit floated by Waldman as a 'great fit' if healthy; still worth a cheap late-round flier.
- [[Curtis Samuel]] — WR, BUF -- best man-coverage beater in room per Harmon; ideally deployed all over formation, not pinned at X
- [[Rondale Moore]] — WR, ATL — Harmon: 'not a real receiver,' pure gadget/motion piece after trade for Desmond Ridder
- [[Garrett Wilson]] — WR, NYJ -- Harmon's 2024 breakout-ceiling pick; 96th-pct man rate, 1,337 median/1,700 high-side yardage projection
- [[Odell Beckham Jr.]] — WR, unsigned FA (Mar 2024) — Miami offered contract; usage confusingly declined in Baltimore; Harmon skeptical of full-time player again
- [[Xavier Gipson]] — WR, NYJ — Harmon 'really intrigued,' thinks he can play; eyed for bigger slot role in 2024
- [[Greg Dortch]] — WR, ARI -- Harmon/Koh's sleeper pick of a bad Cardinals room; 2024 charting subject
- [[Darius Slayton]] — WR, NYG -- 'a pro,' the floor player anchoring the Giants' weak but knowable room
- [[Zay Jones]] — WR, ARI — signing seen as smart depth/flex insurance behind Marvin Harrison Jr. given thin WR room
- [[Josh Palmer]] — WR, LAC -- 'non-embarrassing' 3 forced into a 1 role; part of NFL's worst WR room
- [[Allen Lazard]] — WR, NYJ -- Harmon/Koh: 'I think he's done'; unmovable contract, buried on depth chart
- [[D.J. Chark]] — WR, unsigned FA (Apr 2024) — Harmon: can't get open anymore, sold on Cowboys link (stale)
- [[Hunter Renfrow]] — WR, unsigned FA (Apr 2024) — Harmon cautious buy to Chiefs, worried room gets too slotty (stale)
- [[Tyler Boyd]] — WR, CIN — Harmon: overrated, declining, outside experiment doesn't work; open to Steelers fit (2024, stale)
- [[Marquez Valdes-Scantling]] — WR, unsigned FA (Apr 2024) — Harmon/Koh sell on Chargers pairing w/ Quentin Johnston (stale)
- [[DeVonta Smith]] — WR, PHI — Harmon now grades him tier-3/bottom-tier-2 after 2023 dip; expects Kellen Moore to use him at boundary/X
- [[Kayshon Boutte]] — WR, NE — Waldman's speculative stash add behind a thin NE WR room; talent vs. work-ethic question mark (2024 speculation, stale).
- [[Jalen Coker]] — WR, CAR UDFA — Angelo's top UDFA pick; path to WR3 relevance behind thin Panthers room
- [[Trey Palmer]] — WR, TB — new page; Waldman sees real 2023 development but reads TB's McMillan draft capital as a downgrade signal
- [[Chase Claypool]] — WR, BUF — new page; Waldman rates the signing a camp-body injury hedge, below MVS/Chark on the depth chart
- [[Kadarius Toney]] — WR, NYG — new page; Waldman: career as impactful starter ~80-90% over, compares to Michael Westbrook
- [[Jalen Tolbert]] — WR, DAL — Harmon: promising Day 3 flashes late 2023 but flags 'Skyy Moore bucket' small-sample risk.
- [[Chris Olave]] — WR, NO -- elite RP separator but scheme-mismatched under Carr; Harmon: very good WR1, not yet superstar tier
- [[A.T. Perry]] — WR, NO — poised for expanded X-receiver role in Kubiak's Shanahan-tree scheme; Harmon bullish over rookie Bub Means
- [[Aeneas Smith]] — WR, PHI — Harmon deep sleeper; projected as Eagles' full-speed motion piece for new OC Kellen Moore's scheme
- [[Calvin Austin III]] — WR, PIT — Waldman reverses prior Expo skepticism, now bullish on Austin as a Doug Baldwin-type fit for Russell Wilson
- [[Denzel Mims]] — WR, PIT — buy-low sleeper for the open WR2 job opposite Pickens; Waldman buys the food-poisoning excuse for his lost Jets year
- [[DK Metcalf]] — WR, SEA — Waldman calls him underpriced at ~WR22 Underdog ADP; fastest NFL player per Next Gen Stats last season.
- [[Brandin Cooks]] — WR, DAL — Waldman/Angelo project 100+ targets as Dallas' clear No. 2 behind CeeDee Lamb, pass-first offense.
- [[Andrei Iosivas]] — WR, CIN — Princeton product; Waldman/Angelo see him as a candidate for a big slot role if Tee Higgins is traded.
- [[Charlie Jones]] — WR, CIN — Waldman/Angelo watchlist name for Tyler Boyd's vacated slot role; Purdue product.
- [[Casey Washington]] — WR, ATL — Angelo camp watchlist name behind Drake London/Darnell Mooney; Illinois product.
- [[Parker Washington]] — WR, JAX — Waldman's top pick of the young Jaguars WRs; Robert Woods-type role, rapport with Trevor Lawrence.
- [[Jaylen Waddle]] — WR, MIA — best RP profile yet; press-coverage leap to 72% success, but Harmon still ranks him below Diggs/Ayuk tier [Dynasty]
- [[Kendrick Bourne]] — WR, NE -- presumptive Week 1 X off ACL; solid man-coverage charting in 2023 sample but no great season on record

### Tight Ends
- [[T.J. Hockenson]] — TE, MIN — great in zone, positions well in man; TE1 ceiling minus a tier with a backup QB *(2023 takes, stale)*
- [[Travis Kelce]] — TE, KC — his first-round-pick days are over per Waldman; a nagging early-2023 injury may have lingered all year — but guest Daniel Harms pushes back hard, attributing the down year to two specific in-season injuries rather than decline and projecting at least two more strong seasons; unresolved disagreement; still finished TE1 in 2023 despite the down year, "he'll be fine" per Waldman after the AFC Championship; post-Super-Bowl reframe — no longer "the dominant force," but because KC lacks a second weapon, not because of age *(2024 takes, stale)*
- [[Sam LaPorta]] — TE, DET — Waldman's own miss: needed the perfect fit and found it; outproduced Kincaid as a rookie, still a top-5 dynasty TE in his tier; "one of the best young tight ends, if not the best young tight end in the game" *(2024 takes, stale)*
- [[Dalton Kincaid]] — TE, BUF — Waldman: Bills' true WR1/2 in passing game, underused as rookie, big 2024 upside
- [[Luke Musgrave]] — TE, GB — Waldman's pre-draft 7th-ranked TE, now sees as "slightly overrated" relative to teammate Tucker Kraft *(2024 takes, stale)*
- [[Tucker Kraft]] — TE, GB — the value pick of Green Bay's two rookie tight ends per Waldman — more rugged, more room to grow, and cheaper on his board *(2024 takes, stale)*
- [[Brevyn Spann-Ford]] — TE, Minnesota prospect — 6'7"/270; looked lost as a blocker in 2022, visibly figured out technique by late 2023 per Waldman; projects as a practice-squad/depth-TE NFL path *(2024 pre-draft takes, stale)*
- [[Kyle Pitts]] — TE, ATL — Knight: was never truly healthy in 2023, could rebound if paired with a real QB (2024 takes, stale)
- [[Pat Freiermuth]] — TE, PIT — real usage-risk flag off the Arthur Smith hire, not a talent knock — "two of three" Steelers TEs will be fine and it's "probably going to be the more athletic two," an explicit Kyle-Pitts-underuse comparison *(2024 takes, stale)*
- [[Brycen Hopkins]] — TE, LAR — pending free agent, promising but flawed (RAC ability, athletic, but poor blocker with drop issues); Dustin Keller comp; deep-league stash or wait-and-see, not a lead-role bet *(2024 takes, stale)*
- [[Brock Bowers]] — TE, Georgia prospect — Waldman leaning "feel it" on him becoming the next big rookie-TE fantasy producer; a LaPorta-mold "move tight end" with one real catch-point flaw and blocking to develop; Dalton-Kincaid-outcome comp, not LaPorta/Pitts-level rookie production *(2024 pre-draft takes, stale)*
- [[George Kittle]] — TE, SF — quiet Super Bowl LVIII box score plus a brief locker-room injury scare; career-best yards-per-target season in 2023; flagged as one leg of a coming SF pass-catcher roster crunch (Aiyuk/Deebo/Kittle can't all stay past 2024) per Harmon *(2024 takes, stale)*
- [[David Njoku]] — TE, CLE — Waldman: still TE8 value post-Jeudy trade, retains Browns #2 role behind Amari Cooper on Watson tie (2024, stale)
- [[Ja'Tavion Sanders]] — TE, CAR — Waldman: favorable landing spot (no incumbent receiving TE); projects 500-600 yard range.
- [[Ben Sinnott]] — TE, WAS — rookie comped to a Kittle/Juszczyk hybrid; expected to play early even with Zach Ertz on roster
- [[Jack Westover]] — TE, Washington prospect — Waldman: walk-on who catches everything, projects zone/fullback role
- [[A.J. Barner]] — TE, Michigan (2024 prospect) — Waldman: NFL athlete, not a fantasy option; 2-3 TE-set/matchup role
- [[A.J. Stogner]] — TE, Oklahoma (2024 prospect) — Waldman: move TE, zone-coverage blocker/wall-off type, reserve ceiling
- [[Baylor Cupp]] — TE, Texas Tech (2024 prospect) — Waldman: severe leg-injury history, still moves well, needs route craft
- [[Cade Stover]] — TE, HOU — underrated per both hosts; path to grow as Texans pass-catchers thin out behind Stroud
- [[Dallin Holker]] — TE, Colorado State (2024 prospect) — Waldman: strong hands/tracker, needs 2-3 years on timing routes
- [[Devin Culp]] — TE, Washington (2024 prospect) — Waldman: undersized, high-point ability but clap-catcher lapses
- [[Eric All]] — TE, Michigan (2024 prospect) — Waldman: strong all-around game, ACL/back-surgery medicals are the real risk
- [[Isaac Rex]] — TE, BYU (2024 prospect) — Waldman: good back-shoulder rapport, zone-role upside if he tightens crossers
- [[Jaheim Bell]] — TE/FB, NE — 7th-round pick; both hosts say no fantasy relevance outside special teams
- [[Jared Wiley]] — TE, KC — new-ish contributor; Waldman: mostly special teams early, competing with Noah Gray for Kelce-succession role
- [[McCallan Castles]] — TE, San Jose State (2024 prospect) — Waldman: good ball attack point but small margin for catching-technique error
- [[Tanner McLaughlin]] — TE, Arizona (2024 prospect) — Waldman: athletic but unrefined receiver/blocker, undersized as a blocker
- [[Theo Johnson]] — TE, Penn State (2024 prospect) — Waldman: elite zone-coverage speed but looks slow vs. tight man; refinement needed
- [[Tip Reiman]] — TE, Illinois (2024 prospect) — Waldman: in-line starter athleticism, lacks route craft/guile
- [[Trey Knox]] — TE, South Carolina (2024 prospect) — Waldman: oversized-RB-type YAC role, likely special-teamer/utility target
- [[Zach Hines]] — TE, South Dakota State (2024 prospect) — Waldman: must become a very good in-line blocker to stick in NFL
- [[Dalton Schultz]] — TE, HOU — solid redraft role even as Stroud/Diggs trade drives his price down
- [[Isaiah Likely]] — TE, BAL — Harmon: too talented to keep buried behind Mark Andrews; efficient on low volume (16.1 YPR).
- [[Michael Mayer]] — TE, LV — dynasty value cratered after Raiders drafted Brock Bowers; projected as 2-3 target/game short-yardage piece
- [[Chigoziem Okonkwo]] — TE, TEN (new page) — Harmon: expects a return to true in-line Y role; talented but never had a defined role, worth monitoring
- [[Zach Ertz]] — TE, WAS — Harmon skeptical; views Ertz as a fading placeholder while rookie Ben Sinnott is groomed for immediate role
- [[Evan Engram]] — TE, JAX — 115+ targets in 2023; Waldman/Angelo call him a locked-in top-2 piece of the Jaguars' passing game.
- [[Taysom Hill]] — TE/QB, NO — Waldman likes him over many TE2s for expanded red-zone/backfield role under new OC Clint Kubiak

<!-- Claude: maintain grouped by position (QB / RB / WR / TE), each with a
     one-line summary. See CLAUDE.md "Index maintenance". -->

## Concepts

- [[Aging Curves and Career Longevity]] — 30+ production collapsed league-wide since ~2017; cause unknown. Core [[Dynasty]] input. Waldman declines to apply it to elite individuals (McCaffrey at 28).
- [[Start Your Best Players]] — start top-down off your own rankings rather than chasing weekly matchups
- [[Scouting Bias and Player Archetypes]] — archetype labels track appearance/pedigree more than measured traits, and leak into ADP
- [[Weak Quarterback Play and Receiver Value]] — managers over-discount receivers for bad QBs; discount the *throws he can't make*, not the name
- [[Zone vs Man Route Running]] — beating man and beating zone are separate skills; doing both (not speed) is Waldman's top-WR marker
- [[Scheme vs Talent]] — Concept — Angelo weighs draft capital by position (RB most, QB least) and treats infrastructure as a top evaluation layer
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
- [[Coach Killer Prospects]] — Concept: exec forces unready rookie QB to start, coach takes blame -- Maye, McCarthy, Daniels named 2024 candidates

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
