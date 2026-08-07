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
- [[Baker Mayfield]] — QB, TB — pocket-climbing and audible freedom now real; Waldman sees top-12, Harstad top-10 to 15 (2024 takes, stale)
- [[Justin Fields]] — QB, PIT — Waldman: should keep the job; rushing floor makes him a Konami-code fantasy QB (2024 takes, stale)
- [[Derek Carr]] — QB, NO — Harstad back in after Week 1 deep shot; ceiling QB12–16, floor is a rug-pull (2024 takes, stale)
- [[Justin Herbert]] — QB, LAC — Waldman rejects the low-volume fear; sees high-end QB2/low-end QB1 at QB17 ADP (2024 takes, stale)
- [[Russell Wilson]] — QB, PIT — Waldman says not cooked (~3,500 yds); McFarland says deep-safety trends killed his money plays
- [[C.J. Stroud]] — QB, HOU — Waldman's rankings riser with 3 startable WRs after Diggs trade
- [[Jared Goff]] — QB, DET — Harmon's direct ceiling comp for Tua: "somewhere" top-11-14, stronger arm than Tua; the "what happens once Ben Johnson leaves" question is resolved — Johnson turned down every HC opening, including Washington, and is staying in Detroit; Harmon's sharper follow-up: "there is a level where Jared Goff cannot take you much further," with a clear remaining team need at X receiver *(2024 takes, stale)*
- [[Lamar Jackson]] — QB, BAL — Waldman's contrarian call: the *most* scheme-dependent of the top QBs, not a knock on talent; unqualified 2024 QB1 for both hosts regardless; after the AFC Championship loss, Waldman expects him to supplant Mahomes as 2024 redraft QB2 (maybe QB1), with real year-two growth expected once Monken's offense and a gutted receiver room get an offseason to heal — but Harmon's harder-nosed recap of the same game logs 3 turnover-worthy throws and a near-total run-game abandonment (563rd-of-568 design-run rate), opening an unresolved "are playoff losses mounting" question even while still calling him a top-three QB outright *(2024 takes, stale)*
- [[Patrick Mahomes]] — QB, KC — Waldman's 2024 redraft value call: pushed down boards by Jackson (and maybe Hurts) but won't fall past QB4-5, a real value gap between cost and rank; post-Super-Bowl-LVIII framework — "a wiser Brett Favre," sees through scheme and adapts with far fewer era-defining mistakes *(2024 takes, stale)*
- [[Jalen Hurts]] — QB, PHI — Klassen's disappointment pick: Kellen Moore's full-field progressions plus post-Kelce protection duties (2024 takes, stale)
- [[Brock Purdy]] — QB, SF — not a system QB per Waldman; both hosts lean Purdy over Stroud for 2024; Waldman's career-arc forecast comps him to early Brady/Warner/Wilson/Roethlisberger; Waldman: "exposed as nothing other than what he is" after the Divisional Round win, early ECR outside the top-12 called "a mistake"; Harmon disagrees on that same game — an explicit "bad game," good but "top 20," not elite-tier; Waldman's counter after the NFC Championship win — "subtle skills," carried further by a stacked supporting cast, real front-office skittishness risk if SF doesn't win the Super Bowl *(2024 takes, stale)*
- [[Kyler Murray]] — QB, ARI — Waldman: rushing-driven QB1 ceiling but a 'black hole' who won't lift his pass catchers (2024 takes, stale)
- [[Drew Lock]] — QB, NYG — new page; Waldman expects Lock to open 2024 as starter over ACL-recovering Daniel Jones
- [[Gardner Minshew]] — QB, LV — named Raiders starter over O'Connell; Waldman calls it the right developmental call (2024 takes, stale)
- [[Anthony Richardson]] — QB, IND — accuracy Rorschach test: elite one-of-one throws alongside egregious misses; health is the gate (2024 takes, stale)
- [[Joe Flacco]] — QB, CLE — 2023 turnaround credited to O-line coach Tom Cable and Stefanski's scheme more than to Flacco himself; ran the Cleveland offense better than Watson has, but expected to hit the veteran-backup market after the Wild Card exit *(2024 takes, stale)*
- [[Jordan Love]] — QB, GB — Waldman says QB10 underprices him; 21.1 PPG over final eight games (2024 takes, stale)
- [[Dak Prescott]] — QB, DAL — "a good quarterback... when you give him the talent, he can give you elite production"; a boom/bust "prevailing wind" player, helped by the McCarthy scheme fit; Harmon reads the Wild Card blowout loss as having hit his ceiling relative to Jordan Love *(2024 takes, stale)*
- [[Bryce Young]] — QB, CAR — both hosts buy the bounce-back; ~3,600 yards, preferred over Levis (2024 takes, stale)
- [[Michael Penix Jr.]] — QB, ATL — Waldman sold: trust-throw fit; Atlanta resting him read as a hedge on Cousins (2024 takes, stale)
- [[Tua Tagovailoa]] — QB, MIA — a genuine anticipation/timing thrower who can be schemed into big windows, but a weak post-snap reader who struggles once those windows disappear; Harmon calls a Wild Card loss at KC "straight up bad," ceiling below Jared Goff's *(2024 takes, stale)*
- [[Drake Maye]] — QB, NE — Klassen blames UNC personnel for weak intermediate charting; expects Polk fit to fix it; starting by midseason (2024 takes, stale)
- [[Bo Nix]] — QB, DEN — named starter; Klassen: Minshew/Dalton range, risk-averse, college-hash accuracy inflation (2024 takes, stale)
- [[Caleb Williams]] — QB, CHI — ugly debut: 3/13 beyond 2.5s, 0 completions past 15 air yards; pocket habits the concern (2024 takes, stale)
- [[Jayden Daniels]] — QB, WAS — rushing-driven fantasy value with Kyler-esque profile; may suppress his own receivers (2024 takes, stale)
- [[J.J. McCarthy]] — QB, MIN — Waldman favors him ~60/40 over Sam Darnold for Week 1 job; Minnesota called his ideal fit
- [[Spencer Rattler]] — QB, NO — Waldman: Rattler winning the backup job still leaves Carr as the year-long starter
- [[Tanner Mordecai]] — QB, Wisconsin prospect (SMU/Oklahoma transfer) — rocky transfer-year tape, rebounded late vs. LSU; Waldman's grade is future backup of value, not a starter *(2024 pre-draft takes, stale)*
- [[Jack Plummer]] — QB, Louisville prospect — accuracy is the whole story per Waldman: "if he had the accuracy, he would probably be a top-five quarterback in this class" *(2024 pre-draft takes, stale)*
- [[Joe Milton III]] — QB, Tennessee prospect — the class's clearest boom/bust arm-talent case; top-five-pick ceiling, out-of-the-league floor; Malik Willis comp, explicit "Jordan Love treatment" recommended by Waldman *(2024 pre-draft takes, stale)*
- [[Desmond Ridder]] — QB, ARI — traded from Atlanta for Rondale Moore after Falcons signed Kirk Cousins
- [[Kirk Cousins]] — QB, ATL — Waldman: leg injury killing velocity and play-action; job insecure by end of September (2024 takes, stale)
- [[Daniel Jones]] — QB, NYG — Waldman sees QB12-15 ceiling, superflex-only, and expects Lock to see the field (2024 takes, stale)
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
- [[Deshaun Watson]] — QB, CLE — Waldman expects him benched for Winston by midseason; commitment questioned (2024 takes, stale)
- [[Jacoby Brissett]] — QB, WAS (FA) — Harmon's top pick as Minnesota's veteran bridge QB post-Cousins
- [[Will Levis]] — QB, TEN — Harmon likes the Levis-Ridley in-breaking-route fit under Brian Callahan (2024 takes, stale)
- [[Sam Darnold]] — QB, MIN — elite Week 1 (19/24, 2 TD, 12 straight completions); Harmon wants October before believing (2024 takes, stale)
- [[Sam Howell]] — QB, SEA — Trades to Seattle to push Geno Smith; Waldman expects Smith to keep the job into midseason at least.
- [[Aidan O'Connell]] — QB, LV — Harmon would start him over Minshew; Raiders projected last in pass attempts (2024 takes, stale)
- [[Geno Smith]] — QB, SEA — Klassen's surprise pick: 30+ TDs on the table if the OL is even league-average; Grubb the risk (2024 takes, stale)
- [[Zach Wilson]] — QB, NYJ — Waldman: Baker-Mayfield-style redemption in range if he matures; could be out of league in years
- [[Josh Allen]] — QB, BUF — Waldman avoiding him in Best Ball at current ADP despite Diggs trade fallout
- [[Trevor Lawrence]] — QB, JAX — 'dented can' value buy for Waldman; Harstad says fine-not-star, saved by baseline rushing (2024 takes, stale)
- [[Trey Lance]] — QB, DAL — Waldman still grades top-2-3 in his class, good Cowboys fit; not a bust, per 2024-04-15
- [[Malik Willis]] — QB, TEN — rumored cut/bubble candidate; Waldman's ceiling comp is Tyler Huntley, may be asked to switch positions
- [[Jameis Winston]] — QB, CLE — Waldman and Harris both expect him starting by midseason over Watson (2024 takes, stale)
- [[Jake Haener]] — QB, NO — Waldman: Haener winning Saints' backup job is the redraft-relevant outcome, not Rattler
- [[Hendon Hooker]] — QB, DET — Waldman near-out; backup ceiling, Josh Dobbs career path projected (2024 takes, stale)
- [[Tyson Bagent]] — QB, CHI — Waldman sees a real future and trade value; top QB waiver watch-list name behind Williams (2024 takes, stale)
- [[Cam Ward]] — QB, Miami (FL) — 2024 Heisman-level riser; downfield accuracy jumped, still passes up easy throws (2024 devy takes, stale)
- [[Darian Mensah]] — QB, Tulane — aggressive downfield passer with elite ball placement; expected power-four transfer (2024 devy takes, stale)

### Running Backs
- [[Christian McCaffrey]] — RB, SF — unqualified 2024 1.01 for Waldman again, edging [[CeeDee Lamb]] and [[Tyreek Hill]]; age 28 explicitly dismissed; the "leverage over the field" case; Harmon: even a strong Detroit run defense "isn't stopping that train" in the NFC Championship *(2024 takes, stale)*
- [[Bijan Robinson]] — RB, ATL — Knight (Falcons reporter): 2023 usage was a play-calling failure, offense 'really close' with him healthy (2024 takes, stale)
- [[Jahmyr Gibbs]] — RB, DET — Waldman's 2023 call, vindicated (RB9); he then flips off him for 2024 on price, not talent *(2023 takes, stale)*
- [[James Cook]] — RB, BUF — "elite" question answered yes; fully unleashed in year two, "a real shot" at top-12 value in 2024, floated as the next Ekeler *(2024 takes, stale)*
- [[Tyler Goodson]] — RB, IND — explosive, natural cutback runner masked by Iowa's scheme; Waldman's long-term Colts preference *(2023 takes, stale)*
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, HOU — had taken the job outright from Dameon Pierce in December 2023, but Waldman reverses: no longer Houston's presumptive 2024 starter, expects a free-agent RB (Jacobs or Henry) to take over; a rough Divisional Round game (9 carries, 22 yards) reinforces the need for an upgrade, though Harmon notes it followed a genuinely strong late-season stretch *(2024 takes, stale)*
- [[Saquon Barkley]] — RB, PHI — Waldman: top-five league back behind Eagles line; Swift had ~720 of 1,000 yards before contact (2024)
- [[Derrick Henry]] — RB, BAL — Signs with Baltimore, Waldman's happiest move of free agency; 2023 speed data shows no decline, heavy Best Ball shares.
- [[Joe Mixon]] — RB, HOU — Waldman: possible top-five finish after 159-yard opener; age-28 decline overstated (2024 takes, stale)
- [[Alvin Kamara]] — RB, NO — cap-squeeze uncertainty in New Orleans, but a weeks-4-17 top-4 fantasy back when playing; a Shanahan-tree scheme (new OC Klint Kubiak) could extend his effective range *(2024 takes, stale)*
- [[Breece Hall]] — RB, NYJ — Waldman's RB2 overall behind McCaffrey, just ahead of Bijan; upside pick, OL is the risk (2024 takes, stale)
- [[Nick Chubb]] — RB, CLE — Waldman off him entirely; second reconstruction of same knee, not worth a 10th-round pick (2024 takes, stale)
- [[David Montgomery]] — RB, DET — still projected fringe top-20 on TD equity/role despite Gibbs workload increase; not rendered obsolete
- [[Isiah Pacheco]] — RB, KC — RB2 with low-end RB1 weeks; Perine caps the ceiling in Reid's committee (2024 takes, stale)
- [[Kyren Williams]] — RB, LAR -- JJ lower on him vs. market in 2024; Blake Corum's draft capital and weak combine are risk flags
- [[Kenneth Walker III]] — RB, SEA — Waldman draft him higher than market: Pete Carroll's pattern is to "covet" one back until injury forces a change, and Walker is currently that back; Carroll is now out, new HC Mike McDonald in, reopening the usage-pattern question *(2024 takes, stale)*
- [[Raheem Mostert]] — RB, MIA — the cheap half of Miami's committee; both hosts value him as a 2024 RB2, expect more work to shift to Achane *(2024 takes, stale)*
- [[James Connor]] — RB, ARI — both hosts hanging on for 2024; "toast" skepticism reframed as a second-contract finance story, not a talent decline; Michael Carter cuts into but doesn't replace him *(2024 takes, stale)*
- [[Aaron Jones]] — RB, Free Agent — released by GB after Jacobs signing; still good healthy, but 30 and injury-prone
- [[Zamir White]] — RB, LV — Waldman benching him after a bad week-one usage split with Mattison, but not dropping (2024 takes, stale)
- [[Tank Bigsby]] — RB, JAX — clean Week 1, but same player as at Auburn; RB2 ceiling absent huge volume (2024 takes, stale)
- [[Kendre Miller]] — RB, NO — Waldman's preferred dynasty stash over Bigsby, on opportunity alone *(2024 takes, stale)*
- [[Chase Brown]] — RB, CIN — Waldman: better upside than Moss on speed and pass-game role, cheaper price (2024 takes, stale)
- [[Tony Pollard]] — RB, TEN — Signs with Tennessee on a hedge-y deal; Waldman calls him 'the shiny object,' drops Tyjae Spears's redraft value further.
- [[Michael Carter]] — RB, ARI — Waldman's dark-horse over Trey Benson as pass-pro/receiving complement to James Conner; 'basically free money' late/waiver
- [[Austin Ekeler]] — RB, WAS — Split: Harris says underrated, Waldman says Robinson is the lead back, not Ekeler
- [[Josh Jacobs]] — RB, GB — undervalued in 2024 drafts; clear early-season workhorse with Dillon on IR (2024 takes, stale)
- [[Najee Harris]] — RB, PIT — option decline is a leverage/money move per Waldman's Steelers.com source; long-term future still likely
- [[Jaylen Warren]] — RB, PIT — intriguing complementary piece under new OC Arthur Smith, but explicitly tempered — "if you were waiting for a full-on revival, I don't think we're going to get that" *(2024 takes, stale)*
- [[Jordan Mason]] — RB, SF — the 49ers lead back for now, but Shanahan's hook makes him a one-game handcuff (2024 takes, stale)
- [[Elijah Mitchell]] — RB, SF — got more 2023 volume than Mason down the stretch, but still Waldman's #2 McCaffrey handcuff on price *(2024 takes, stale)*
- [[Tyler Allgeier]] — RB, ATL — Bijan Robinson's complementary piece; "plays really well when in the system they put him in" *(2024 takes, stale)*
- [[Blake Corum]] — RB, LAR — 'wildly overdrafted' per Waldman/Harris; real contingent value if Williams hurt, but McVay historically avoids rookies
- [[De'Von Achane]] — RB, MIA — Waldman moved him above Mostert; expects a near-even split, big-play role (2024 takes, stale)
- [[Braelon Allen]] — RB, NYJ — Waldman rates his long-term outlook behind Breece Hall below Guerendo's behind McCaffrey.
- [[Jonathan Brooks]] — RB, CAR — ACL recovery caps early season; McFarland graded him over Gibbs as a prospect (2024 takes, stale)
- [[Blake Watson]] — RB, DEN — Angelo's biggest 2025 riser dark horse, ranked ahead of Estime on ADP-value grounds
- [[Jabari Small]] — RB, Tennessee prospect — Shrine Game name Waldman likes; undersized (205 lbs) but runs hard with good vision and decision-making *(2024 pre-draft takes, stale)*
- [[Ray Davis]] — RB, BUF — Angelo sold: contact balance, becomes Buffalo's clear No. 2 and goal-line back (2024 takes, stale)
- [[Dylan Laube]] — RB, LV — late-round stab/waiver target; pass-catching plus better inside running than reputation (2024 takes, stale)
- [[Daijun Edwards]] — RB, Georgia prospect — quick and shifty despite playing through an MCL injury, good pass catcher/blocker; Jalen-Richard floor, dynamic-James-White ceiling; likely the most-rostered of Waldman's three underrated 2024 RBs on name value alone *(2024 pre-draft takes, stale)*
- [[George Holani]] — RB, SEA — dynasty stash only; strong camp but may lose the RB3 job to McIntosh (2024 takes, stale)
- [[Deshaun Fenwick]] — RB, Oregon State prospect — Shrine Game favorite; Leonard-Fournette-adjacent big-back build, gap-scheme thumper, projects as a reserve "B-back" *(2024 pre-draft takes, stale)*
- [[Brian Robinson Jr.]] — RB, WAS — Waldman top-15-20 back, not a flex; gap scheme fit plus real passing-down role (2024 takes, stale)
- [[Tyjae Spears]] — RB, TEN -- JJ's highest-rostered RB target this year; favored over Tony Pollard in Titans' even timeshare
- [[Mario Anderson]] — RB, Memphis prospect (future class) — flagged by Waldman as the next name in Memphis's RB pipeline (Pollard, Henderson, Gainwell); shifty, good vision, Ray Davis size/balance comp *(2024 pre-draft takes, stale)*
- [[Cody Schrader]] — RB, Missouri prospect — Angelo's late-round pick to make a roster and stick; 1,800 total yards/14 TDs at Missouri, Senior Bowl standout, graded a smart, reliable long-term role player rather than a star *(2024 pre-draft takes, stale)*
- [[Kendall Milton]] — RB, Georgia prospect — unique size/speed at 6'1"/220-225; hasn't yet shown the Eddie-George-level ceiling his HS recruiting profile promised; combine/pro day season is the swing factor for his stock *(2024 pre-draft takes, stale)*
- [[Kimani Vidal]] — RB, LAC — Waldman buying as a cheap dynasty stash; Austin Ekeler size comp, thin/injury-prone depth chart ahead
- [[Will Shipley]] — RB, Clemson prospect — underrated receiving-back profile with real speed (6.4s HS 55m); combine 40 time is the key swing event for his stock; projects as a Dion-Lewis/James-White-style complementary role *(2024 pre-draft takes, stale)*
- [[Rasheen Ali]] — RB, Marshall prospect — explosive pre-ACL flash back who returned to the same level; graded the best RB at the 2024 Senior Bowl for his limited reps there; ball security is the swing risk *(2024 pre-draft takes, stale)*
- [[Jaylen Wright]] — RB, MIA — Angelo projects him as Dolphins' touch leader by end of 2025 as Mostert/Connor age out
- [[Dillon Johnson]] — RB, Washington prospect — Waldman's fourth early-round-talent name; played through multiple injuries into the national title game, some of the best contact balance in the class, but a real breakaway-speed/explosiveness ceiling concern *(2024 pre-draft takes, stale)*
- [[Trey Benson]] — RB, ARI — dynasty comp to peak David Johnson; expected to take over lead role by year two behind James Connor
- [[Bucky Irving]] — RB, TB — Angelo: hype ahead of role; hot-hand split with White, Tucker lurking (2024 takes, stale)
- [[Marshawn Lloyd]] — RB, GB — Waldman firmly skeptical: below-committee ball security, bounces plays; a 'wait a year' back (2024 takes, stale)
- [[Khalil Herbert]] — RB, CHI (likely cut) — Waldman: top-5 waiver-wire stash if he lands in a backfield with need
- [[Roschon Johnson]] — RB, CHI — Waldman: RB35 ADP near his peak-production ceiling; Herbert preferred as the better value
- [[Javonte Williams]] — RB, DEN — Waldman up to low-end starter with upside after weight loss; ceiling gated by Nix (2024 takes, stale)
- [[Samaje Perine]] — RB, KC — Waldman: plus Darrel Williams for Reid; power/pass-pro role caps Pacheco's ceiling (2024 takes, stale)
- [[Rachaad White]] — RB, TB — zone additions fit his wide-crease running better than duo; usage finally matched to strengths (2024 takes, stale)
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
- [[Tyrone Tracy Jr.]] — RB, NYG — Waldman calls him an overhyped sleeper; expects early mistakes behind Singletary (2024 takes, stale)
- [[Miyan Williams]] — RB, Ohio State (2024 prospect) — Waldman: smart, physical; ceiling of a Peyton-Barber-type committee back
- [[Frank Gore Jr.]] — RB, Southern Miss (2024 prospect) — Waldman: smart cutback runner, must prove he can transcend size like Devin Singletary
- [[Emani Bailey]] — RB, TCU (2024 prospect) — Waldman: inconsistent gap reads, too tight or too wide; needs better control/vision
- [[Dylan McDuffie]] — RB, Kansas (2024 prospect) — Waldman: willing tight-crease runner, Raheem-Mostert-lite burst without the blink-of-an-eye separation
- [[Michael Wiley]] — RB, Arizona (2024 prospect) — Waldman: needs better leverage attacking defenders, same early issue Jahmyr Gibbs had
- [[Gus Edwards]] — RB, LAC — Waldman: slipping to the short-yardage side of a hot-hand split behind Dobbins (2024 takes, stale)
- [[Travis Etienne Jr.]] — RB, JAX — Best Ball RB6, near ceiling but preferred over unproven Tank Bigsby
- [[J.K. Dobbins]] — RB, LAC — explosive second half a year off Achilles; Harbaugh/Roman run-first tempo boosts his role (2024 takes, stale)
- [[Chuba Hubbard]] — RB, CAR — Waldman feeling Hubbard as CAR's de facto starter at RB39 ADP, clearly ahead of Miles Sanders (2024 speculation, stale).
- [[Miles Sanders]] — RB, CAR — Angelo blames poor Panthers infrastructure/ownership, not talent loss, for his decline
- [[Dylan Johnson]] — RB, TEN UDFA — Waldman's other favorite; projects as low-red-zone role Titans currently lack
- [[Eric Gray]] — RB, NYG — new page; Waldman has Gray 60/40 over Tyrone Tracy Jr. for the complementary role behind Singletary
- [[Dameon Pierce]] — RB, HOU — new page; Waldman: starter role over, misused as a non-receiving back despite receiving ability at Florida
- [[Deuce Vaughn]] — RB, DAL — not viewed as a 2024 fantasy factor; buried behind Elliott/Dowdle regardless of role changes
- [[Justin Strong]] — RB, IND (UDFA) — tryout with Colts; Waldman flags burst/vision but wants a deep-league watch, not a draft pick
- [[Zach Charbonnet]] — RB, SEA — Waldman cools: beat reporters say nobody plays if Walker is healthy; correlation data flags him (2024 takes, stale)
- [[Cordarrelle Patterson]] — RB, PIT — Waldman: top-15 waiver monitor, but age/build cap him to short-stint upside only
- [[Leonard Fournette]] — RB, FA — Waldman: monitor-only 'next Latavius Murray' type until there's a real, proven role
- [[Ashton Jeanty]] — RB, Boise State (prospect) — Waldman: explosive lead back with a shot to be the class' top RB (2024 take)
- [[Trevor Etienne]] — RB, Georgia (prospect) — Waldman: good space/inside runner, but pass-pro flaw and a DUI suspension risk
- [[Ollie Gordon II]] — RB, Oklahoma State (prospect) — Waldman unimpressed: not top-3 in class, needs years to read NFL run game
- [[Jaleel McLaughlin]] — RB, DEN — Waldman's favorite Denver back at an RB50 price; Payton receiving-back archetype (2024 takes, stale)
- [[Clyde Edwards-Helaire]] — RB, KC — on NFI list to open 2024, out four games; no fantasy path offered (2024 takes, stale)
- [[Deneric Prince]] — RB, KC — camp first-team reps not an endorsement; monitor only, roster risk (2024 takes, stale)
- [[Justice Hill]] — RB, BAL — Waldman: the reserve behind Henry but not the handcuff to own; Baltimore will sign a volume vet (2024 takes, stale)
- [[A.J. Dillon]] — RB, GB — Waldman holds firm: underrated power back with vision, hands; may hold off Lloyd (2024 takes, stale)
- [[Christopher Brooks]] — RB, GB — talent-without-opportunity stash; Waldman says wait for a Packers backfield trigger before adding (2024 takes, stale)
- [[Sione Vaki]] — RB, DET — converted safety, natural receiving back; 2024 watch list, floated as Montgomery's eventual successor (2024 takes, stale)
- [[Jordan Lyle]] — RB, Miami — Angelo devy watch: Gibbs-like HS tape, late-1st/early-2nd upside, small frame (~185 lbs)
- [[Kyle Monangai]] — RB, Rutgers — Waldman: Devonta Freeman comp; 410 touches, zero fumbles; career over fantasy ceiling (2024 takes, stale)
- [[Jacory Croskey-Merritt]] — RB, Arizona — Waldman devy watch: Aaron Jones-like quickness and creativity, ~205-210 lbs
- [[Carson Steele]] — RB, KC — UDFA with vision and hands; Waldman says roster-worthy only, isolated looks (2024 takes, stale)
- [[Rico Dowdle]] — RB, DAL — cheap shot the Cowboys want to work; talent to surprise but expendable (2024 takes, stale)
- [[Ezekiel Elliott]] — RB, DAL — late-round shot; elite short-yardage and pass pro, limited fantasy upside (2024 takes, stale)
- [[Dalvin Cook]] — RB, DAL — fallback committee piece only; Harris sees a Fournette-style dead end (2024 takes, stale)
- [[Sean Tucker]] — RB, TB — Waldman: best cutback zone runner and big-play threat in Tampa's backfield (2024 takes, stale)
- [[Nicholas Singleton]] — RB, Penn State — Waldman: 6-0/224 volume back, elite play-design discipline and high-knee traffic running (2024 takes, stale)
- [[Dean Connors]] — RB, Rice — Waldman: Ekeler/Swift-lineage receiving back, situational upside, well below class headliners (2024 takes, stale)
- [[Sire Gaines]] — RB, Boise State — 6-0/209 true freshman behind Jeanty; projected 2025 lead back (2024 devy takes, stale)
- [[Tahj Brooks]] — RB, Texas Tech — Waldman film favorite; elite ball security and contact balance, likely day-three (2024 takes, stale)

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — Harmon: best WR in league, live 200-target case on a thin depth chart; 40%+ first-read share (2024 takes, stale)
- [[Ja'Marr Chase]] — WR, CIN — holdout, zero practices; Harmon expects Week 1 absence, slot-expansion plan on hold (2024 takes, stale)
- [[Keenan Allen]] — WR, CHI — Koh: leads Bears early as uncovered slot; Harmon sees him as the low read, fades late (2024 takes, stale)
- [[Amon-Ra St. Brown]] — WR, DET — six-target Week 1 an outlier; Harmon unworried, but Jameson Williams' role may shrink the ceiling (2024 takes, stale)
- [[Jameson Williams]] — WR, DET — first career 100-yd game; 42.9% first-read share, motion-schemed away from press; needs to stack weeks (2024 takes, stale)
- [[Brandon Aiyuk]] — WR, SF — Waldman down on him vs 2023; contract unresolved, trade would cap him ~800-900 yards (2024 takes, stale)
- [[Tee Higgins]] — WR, CIN — franchise-tagged, Harmon doubts a 2025 return; Cincinnati's WR1 while Chase holds out (2024 takes, stale)
- [[Jordan Addison]] — WR, MIN — Harmon: strong WR2 ceiling, top-30 not top-20; off-field driving incidents a real availability risk (2024 takes, stale)
- [[Jayden Reed]] — WR, GB — RP 72.2% vs man, 81.7% vs zone; Harmon: top-20 talent capped only by Packers rotation (2024 takes, stale)
- [[Noah Brown]] — WR, WAS — surprise Houston cut, signed by Washington; competent system depth pushed out by roster crowding (2024 takes, stale)
- [[John Metchie III]] — WR, HOU — flashed filling in for an injured Noah Brown in the Wild Card win, but downgraded after the Divisional Round — Harmon: "has proven nothing to this point in his career," replacement-level depth, not a real answer opposite Nico Collins *(2024 takes, stale)*
- [[Xavier Hutchinson]] — WR, HOU — faint praise, an Allen-Lazard-type depth/blocking piece rather than a real target threat *(2024 takes, stale)*
- [[Tre Tucker]] — WR, LV — effectively WR4 behind Bowers; redraft value nil, matchup/injury dart (2024 takes, stale)
- [[Treylon Burks]] — WR, TEN — Harmon: big-slot-only, can't play X; an afterthought to the new staff (2024 takes, stale)
- [[DeAndre Hopkins]] — WR, TEN — knee injury, out 4-6 weeks at age 32; Harmon sees an aging-curve warning sign (2024 takes, stale)
- [[Adam Thielen]] — WR, CAR — 2023 volume was 'only game in town'; slides to a comfortable No. 2 behind Diontae (2024 takes, stale)
- [[Deebo Samuel]] — WR, SF — elite zone beater, career-long man-coverage weakness; Harmon would move on after 2024 (2024 takes, stale)
- [[Malik Nabers]] — WR, NYG — Angelo's WR1 on film; carries a thin Giants offense, biggest first rookie splash (2024)
- [[Marvin Harrison Jr.]] — WR, ARI — Waldman: overpriced redraft, WR35-40 not WR15; bad fit with Kyler Murray (2024 takes, stale)
- [[Rome Odunze]] — WR, CHI — Harmon hot take: Chicago's fantasy WR1, could lead team in TDs; Moore still leads yards (2024 takes, stale)
- [[Keon Coleman]] — WR, BUF — Waldman: led BUF targets week one, Allen trusts the jump ball; flex-worthy, role not settled (2024)
- [[Ainias Smith]] — WR, PHI — slow camp start, Johnny Wilson ahead; Waldman says he needs a year or two (2024 takes, stale)
- [[Michael Gallup]] — WR, LV — retired July 2024; Harmon's case study that post-ACL confidence never returned
- [[Brian Thomas Jr.]] — WR, JAX — nuanced man/zone route work in Week 1; Waldman sees him as the team's primary receiver soon (2024 takes, stale)
- [[Ladd McConkey]] — WR, LAC — team-leading 7 targets and a highlight TD; Harmon wants his routes to grow at Palmer's expense (2024 takes, stale)
- [[Ricky Pearsall]] — WR, SF — shot in chest; Harmon expects a redshirt rookie year, 2025 slot/flanker upside (2024 takes, stale)
- [[Troy Franklin]] — WR, DEN — elite deep charting but 176 lbs; Harmon projects low-volume stretch receiver, not year-one piece (2024 takes, stale)
- [[CeeDee Lamb]] — WR, DAL — Harmon projects 180-200 targets in 2024 given Dallas's total lack of a second target earner.
- [[Tyreek Hill]] — WR, MIA — 3rd in Waldman's 2024 top tier, but Bob Harris's personal #2 as "an old-school wide receiver one" *(2024 takes, stale)*
- [[Mike Evans]] — WR, TB — Harmon's best WR in the NFC South; route tree redesigned for Mayfield, don't let Cohen change it (2024 takes, stale)
- [[Rashid Shaheed]] — WR, NO — complete route runner behind a viral in-breaking-only chart; zone score is the swing factor (2024 takes, stale)
- [[Jerry Jeudy]] — WR, CLE — Waldman reverses: no longer believes, durability plus 'settled for good'; hedged as intuition (2024 takes, stale)
- [[Courtland Sutton]] — WR, DEN — good X, not a No. 1; slant-dependent, age-29 concerns, ranked behind McConkey (2024 takes, stale)
- [[Chris Godwin]] — WR, TB — Waldman: healthy in the slot in a Rams-style scheme; can approach peak-Kupp reception volume (2024)
- [[Rashad Bateman]] — WR, BAL — Harmon likes him as a starter if healthy; Ravens slow to recognize his separation (2024 takes, stale)
- [[Stefon Diggs]] — WR, HOU — deep-route RP decline; Harmon projects backside third-down ISO role, hosts split on slot fit (2024 takes, stale)
- [[Cooper Kupp]] — WR, LAR — 21-target Week 1 but Harmon sees 2022-Rams volume-without-efficiency; slot-only at 31 (2024 takes, stale)
- [[Quentin Johnston]] — WR, LAC — Roman finally using him underneath/across the field, Bateman-type role; hands confidence still an open question (2024 takes, stale)
- [[Jaxon Smith-Njigba]] — WR, SEA — Harmon hot take: leads Seattle in catches and yards; Koh lower than consensus (2024 takes, stale)
- [[Zay Flowers]] — WR, BAL — Harmon hot take: clears 1,200 yards; elite 85% vs zone, weak press (2024 takes, stale)
- [[Puka Nacua]] — WR, LAR — short-term IR, new PCL injury to same knee, out 4+ games; Rams lose their press-man outside receiver (2024 takes, stale)
- [[Tank Dell]] — WR, HOU — 80%+ success on all out-breaking routes; graded No. 1 in separation, likely off-ball motion role (2024 takes, stale)
- [[Nico Collins]] — WR, HOU — Harmon's highest-conviction WR; predicts NFL TD reception lead, clearest role in Houston (2024 takes, stale)
- [[Josh Downs]] — WR, IND — talented slot capped by Richardson and heavy 12 personnel; cheap price (2024 takes, stale)
- [[Marvin Mims Jr.]] — WR, DEN — buried behind Tim Patrick despite Payton draft capital; Meachem/Henderson role hasn't materialized (2024 takes, stale)
- [[Jalen Hyatt]] — WR, NYG — running ahead of Slayton; Harmon: vertical stretcher, 'sacrificial adjacent,' not a target earner (2024 takes, stale)
- [[Rashee Rice]] — WR, KC — suspension may not land in 2024; WR4 price could return value, aided by two-high shells (2024 takes, stale)
- [[Davante Adams]] — WR, LV — still top-three NFL receiver on 2023 charting; vertical routes slipping at 85th percentile vs man (2024 takes, stale)
- [[Gabe Davis]] — WR, JAX (signed FA) - 3yr/$39M; Harmon: was 7th percentile vs man in 2023, pairs into a bottom-5 WR room
- [[Khalil Shakir]] — WR, BUF — Harmon's Week 1 bet as Buffalo's most productive receiver; entrenched in the slot (2024 takes, stale)
- [[Drake London]] — WR, ATL — in-breaking routes align with Cousins' 150.6 rating on digs/crossers; carries a bottom-10 room (2024 takes, stale)
- [[Michael Wilson]] — WR, ARI — underrated rookie year; played X in final 3 games (81.8% outside), frees Harrison to move around (2024, stale)
- [[George Pickens]] — WR, PIT — WR2 baseline tied to Russell Wilson's volume; Waldman's most-drafted early WR (2024 takes, stale)
- [[Diontae Johnson]] — WR, CAR — McFarland's most-drafted WR as Canales' focal point; Waldman flags hands/tracking (2024 takes, stale)
- [[Tyler Lockett]] — WR, SEA — declined but not washed; Harmon sees a high-quality WR3 with slot reps available (2024 takes, stale)
- [[Terry McLaurin]] — WR, WAS — 46 snaps left, 3 right, zero pre-snap motion under Kingsbury; Harmon sees iso-receiver misuse (2024 takes, stale)
- [[Wan'Dale Robinson]] — WR, NYG — real after-the-catch and contested-catch value; outlook entirely a Giants-QB question *(2024 takes, stale)*
- [[Ronnie Bell]] — WR, SF — a name to know mostly for injury-contingency reasons behind Aiyuk/Deebo, not his own emergence *(2024 takes, stale)*
- [[Dontayvion Wicks]] — WR, GB — Harmon: best true ISO route runner in the Packers room, wins outside vs press (2024 takes, stale)
- [[Romeo Doubs]] — WR, GB — part of Green Bay's "big three," but "a little less multi-dimensional" than what Wicks offers; Harmon's clear #4 of the group — solid vertical player and best 2023 postseason of the four, but not a path to more *(2024 takes, stale)*
- [[Christian Watson]] — WR, GB — Harmon: less-is-more big-play specialist, boom/bust and not a full-time player (2024 takes, stale)
- [[Cedric Tillman]] — WR, CLE — Waldman curious: potential Cooper successor, floor of a better Josh Palmer (2024 takes, stale)
- [[Tyler Scott]] — WR, CHI — "overrated on speed" pre-draft per Waldman; used as a one-dimensional RPO/deep-shot option, a Darnell-Mooney-before-he-developed comp *(2024 takes, stale)*
- [[Jonathan Mingo]] — WR, CAR — Waldman's bounce-back pick after Steve Smith work; WR3 ceiling, strong camp (2024 takes, stale)
- [[Demario Douglas]] — WR, NE — inverted man(69%)/zone(76% but bottom-quartile) profile; muddled 2024 role behind Polk, Baker, Bourne [Dynasty]
- [[Malik Washington]] — WR, MIA — 6th-round slot fit; McDaniel personally lobbied to draft him, Harmon very high
- [[Xavier Legette]] — WR, CAR — manufactured-touch rookie role only; Waldman says wait until 2025 (2024 takes, stale)
- [[Malachi Corley]] — WR, NYJ -- slot-only gadget profile (66% man/85% zone); blocks Xavier Gipson's slot role
- [[Javon Baker]] — WR, NE — Koh's 1,000-yard hot take; Harmon likes the X profile but calls the number a stretch (2024 takes, stale)
- [[Roman Wilson]] — WR, PIT — Waldman bearish for 2024: can't beat press, long-term bet only (2024 takes, stale)
- [[Devontez Walker]] — WR, BAL — total project per Harmon; elite athlete, no consistent college separation (2024 takes, stale)
- [[Brendan Rice]] — WR, LAC — 7th-rounder w/ elite in-breaking numbers, poor vertical/ball-tracking; deep sleeper per Matt Harmon
- [[J. Michael Sturdivant]] — WR, UCLA prospect (Cal transfer) — 6'3"/205, high-end traits that "didn't really emerge at the highest level" of production per Waldman; declared, ungraded *(2024 pre-draft takes, stale)*
- [[Marquise Brown]] — WR, KC — Koh's pick to lead Chiefs in targets/yards; Harmon sees him defaulting into the X role (2024 takes, stale)
- [[Skyy Moore]] — WR, KC — Harmon calls his outside-receiver usage a "mis-evaluation" of the player; doesn't expect him in Kansas City's plans and would rather see him traded to restart elsewhere *(2024 takes, stale)*
- [[A.J. Brown]] — WR, PHI — Harmon predicts new OC Kellen Moore could shift Brown into the slot as primary read; Koh disagrees
- [[DeMarcus Robinson]] — WR, LAR — Rams' only real vertical/outside option post-Nacua; 75% outside, top aDOT on team (2024 takes, stale)
- [[Jahan Dotson]] — WR, PHI — traded from Washington; Harmon sees a solid non-star, likely better in the slot, useful Eagles depth (2024 takes, stale)
- [[Adonai Mitchell]] — WR, IND — separated consistently but 0.11 YPRR on Richardson misses; encouraging debut hidden by box score (2024 takes, stale)
- [[Xavier Worthy]] — WR, KC — Angelo: hot start/cold finish rookie in a crowded room; 2025 is the bet (2024 takes, stale)
- [[Ja'Lynn Polk]] — WR, NE — 85%+ RP success on dig/curl/comeback; the intermediate-window target Klassen says Maye needs (2024 takes, stale)
- [[Michael Pittman Jr.]] — WR, IND — team-friendly deal; Harmon calls him a true, underrated WR1, eyes top-10 breakout in 2024
- [[D.J. Moore]] — WR, CHI — Harmon promotes him to tier two ('superstar No. 1'); favourite to lead Bears in yards (2024 takes, stale)
- [[Calvin Ridley]] — WR, TEN — Harmon says under-discussed; Callahan's pass-heavy scheme sets up a big year (2024 takes, stale)
- [[Mike Williams]] — WR, NYJ -- health is the swing factor for whole room; ACL/age risk, no real depth if he's out
- [[Tyler Harrell]] — WR, deep sleeper (Miami) — Waldman: elite play speed, 'as fast as Xavier Worthy' but unproven, injury-plagued (2024 prospect, stale)
- [[Amari Cooper]] — WR, CLE — Harmon's true No. 1 X, best ball of his career; age-30 holdout risk (2024 takes, stale)
- [[Elijah Moore]] — WR, CLE — separates fine but capped as a No. 2; miscast as a gadget player (2024 takes, stale)
- [[Christian Kirk]] — WR, JAX - Harmon: best receiver on Jaguars roster, slot-mostly; now in a bottom-5 receiver room
- [[Darnell Mooney]] — WR, ATL — Harmon projects vertical-slot/flanker role (60-40 split), a WR3-caliber 'a 3'
- [[Anthony Gould]] — WR, Oregon State (2024 prospect) — Waldman: sub-package contributor early, needs man-coverage refinement to start
- [[Bub Means]] — WR, NO — rookie depth athlete, 4.43/39.5-inch; zone-better, poor start-stop (2024 takes, stale)
- [[Jalen McMillan]] — WR, TB — Angelo: immediate 3WR starter at Z, 'Darius Slayton plus', better NFL WR2 in 3-5 years
- [[Jermaine Burton]] — WR, CIN — Harmon holds dynasty value on talent but flags trust/professionalism reports; possible Week 1 scratch (2024 takes, stale)
- [[Johnny Wilson]] — WR, PHI — inside track to WR3; Harmon's charting says true outside X, 71.4% vs man, bad contested hands (2024 takes, stale)
- [[Joshua Cephus]] — WR, UTSA (2024 prospect) — Waldman: slippery zone/YAC weapon, needs man skills to start outside
- [[Kobe Hudson]] — WR, UCF (2024 prospect) — Waldman: deep-threat sub-package piece, could grow into starting outside option
- [[Luke McCaffrey]] — WR, WAS — reportedly outside the top four; both hosts call the third-round pick too early for a two-year receiver convert (2024, stale)
- [[Ryan Flournoy]] — WR, Southeast Missouri State (2024 prospect) — Waldman: NFL athlete, contributor-vs-reserve hinges on releases/breaks
- [[Xavier Weaver]] — WR, Colorado (2024 prospect) — Waldman: Jordan Addison starter kit, route game a starting-caliber foundation
- [[Michael Thomas]] — WR, FA — suspended one game; Waldman expects a signing by mid-October, a waiver stash not a draft pick (2024 takes, stale)
- [[Curtis Samuel]] — WR, BUF -- best man-coverage beater in room per Harmon; ideally deployed all over formation, not pinned at X
- [[Rondale Moore]] — WR, ATL — Harmon: 'not a real receiver,' pure gadget/motion piece after trade for Desmond Ridder
- [[Garrett Wilson]] — WR, NYJ — Waldman WR11, down from fourth overall on Rodgers-timing reports; Rodgers compares his drive to Adams (2024 takes, stale)
- [[Odell Beckham Jr.]] — WR, unsigned FA (Mar 2024) — Miami offered contract; usage confusingly declined in Baltimore; Harmon skeptical of full-time player again
- [[Xavier Gipson]] — WR, NYJ — Harmon 'really intrigued,' thinks he can play; eyed for bigger slot role in 2024
- [[Greg Dortch]] — WR, ARI -- Harmon/Koh's sleeper pick of a bad Cardinals room; 2024 charting subject
- [[Darius Slayton]] — WR, NYG — on the roster bubble behind Jalen Hyatt, but Harmon calls him a survivor (2024 takes, stale)
- [[Zay Jones]] — WR, ARI — signing seen as smart depth/flex insurance behind Marvin Harrison Jr. given thin WR room
- [[Josh Palmer]] — WR, LAC — leads Chargers outside receivers in targets, but behind McConkey overall (2024 takes, stale)
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
- [[Kadarius Toney]] — WR, FA — cut by KC and unsigned; Harmon says he never had real route-running traits, net negative in 2023 (2024 takes, stale)
- [[Jalen Tolbert]] — WR, DAL — third-year-leap candidate; 70.5% vs man / 81.2% vs zone RP profile, but sample is tiny (2024 takes, stale)
- [[Chris Olave]] — WR, NO — Waldman bumping him up on Kubiak's scheme; sees top-15 possible, not top-10 (2024 takes, stale)
- [[A.T. Perry]] — WR, NO — boundary X with press/contested-catch chops; Van Jefferson 2021 as best case (2024 takes, stale)
- [[Aeneas Smith]] — WR, PHI — Harmon deep sleeper; projected as Eagles' full-speed motion piece for new OC Kellen Moore's scheme
- [[Calvin Austin III]] — WR, PIT — Waldman's last-round best ball dart; Baldwin/Lockett comp if motion unlocks him (2024 takes, stale)
- [[Denzel Mims]] — WR, PIT — buy-low sleeper for the open WR2 job opposite Pickens; Waldman buys the food-poisoning excuse for his lost Jets year
- [[DK Metcalf]] — WR, SEA — Harmon: has peaked as a top-10-to-15 receiver, not tier one; Koh expects deep-shot volume (2024 takes, stale)
- [[Brandin Cooks]] — WR, DAL — Waldman's WR4 at a WR59 price; Prescott chemistry reported in OTAs (2024 takes, stale)
- [[Andrei Iosivas]] — WR, CIN — Harmon's pick to inherit Boyd's ~100 slot targets in Cincinnati's 11-personnel offense (2024 takes, stale)
- [[Charlie Jones]] — WR, CIN — Waldman/Angelo watchlist name for Tyler Boyd's vacated slot role; Purdue product.
- [[Casey Washington]] — WR, ATL — Angelo camp watchlist name behind Drake London/Darnell Mooney; Illinois product.
- [[Parker Washington]] — WR, JAX — late-round dart throw and waiver-monitor name; watch late-camp adjustment with Lawrence (2024 takes, stale)
- [[Jaylen Waddle]] — WR, MIA — best RP profile yet; press-coverage leap to 72% success, but Harmon still ranks him below Diggs/Ayuk tier [Dynasty]
- [[Kendrick Bourne]] — WR, NE -- presumptive Week 1 X off ACL; solid man-coverage charting in 2023 sample but no great season on record
- [[Alec Pierce]] — WR, IND — sacrificial X, but Richardson's deep-ball willingness makes Harmon skeptical he's a fantasy zero (2024 takes, stale)
- [[Van Jefferson]] — WR, PIT — Waldman: Jefferson's a cheap stopgap, not a real answer, until Roman Wilson is ready
- [[Jordan Whittington]] — WR, LAR — one snap in Week 1 but named as the tough-player candidate for the WR3 role post-Nacua (2024 takes, stale)
- [[Josh Reynolds]] — WR, DEN — Harmon's bet for Broncos' second-most productive receiver on known-quantity grounds (2024 takes, stale)
- [[Jakobi Meyers]] — WR, LV — Harmon calls him badly underrated, better than any Chiefs WR; capped by Raiders volume (2024 takes, stale)
- [[Olamide Zaccheaus]] — WR, WAS — Waldman's pick for the WR3 job over Dyami Brown and McCaffrey; versatile vertical winner (2024 takes, stale)
- [[Jalen Nailor]] — WR, MIN — camp speedster, near-lock WR3 role; waiver watch list, not draftable (2024 takes, stale)
- [[JuJu Smith-Schuster]] — WR, KC — cut by NE, re-signed with Kansas City; Harmon sees him as a role-cater profile redundant with Rashee Rice (2024 takes, stale)
- [[Tim Patrick]] — WR, DET — Angelo: fills the missing outside X if healthy; unlocks Jameson Williams (2024 takes, stale)
- [[Tyquan Thornton]] — WR, NE — Harmon: X-receiver role is a camp mirage; design-touches player, not an outside starter (2024 takes, stale)
- [[Dyami Brown]] — WR, WAS — late-round dart throw; healthy but unproven, Waldman prefers Chark (2024 takes, stale)
- [[Tez Johnson]] — WR, Oregon — Angelo: elite low-red-zone separator, slight-framed slot, projected day-two pick (2024 takes, stale)
- [[Tyler Johnson]] — WR, LAR — surprise Week 1 YAC flash post-Nacua; Harmon calls possible one-week flash given zero camp buzz (2024 takes, stale)
- [[Jeremiah Smith]] — WR, Ohio State — highest-rated WR recruit ever; leading OSU in receiving as an 18-year-old (2024 devy takes, stale)
- [[Ryan Williams]] — WR, Alabama — 17-year-old reclassified freshman leading Alabama in receiving; top devy stash (2024 takes, stale)

### Tight Ends
- [[T.J. Hockenson]] — TE, MIN — great in zone, positions well in man; TE1 ceiling minus a tier with a backup QB *(2023 takes, stale)*
- [[Travis Kelce]] — TE, KC — his first-round-pick days are over per Waldman; a nagging early-2023 injury may have lingered all year — but guest Daniel Harms pushes back hard, attributing the down year to two specific in-season injuries rather than decline and projecting at least two more strong seasons; unresolved disagreement; still finished TE1 in 2023 despite the down year, "he'll be fine" per Waldman after the AFC Championship; post-Super-Bowl reframe — no longer "the dominant force," but because KC lacks a second weapon, not because of age *(2024 takes, stale)*
- [[Sam LaPorta]] — TE, DET — Waldman's own miss: needed the perfect fit and found it; outproduced Kincaid as a rookie, still a top-5 dynasty TE in his tier; "one of the best young tight ends, if not the best young tight end in the game" *(2024 takes, stale)*
- [[Dalton Kincaid]] — TE, BUF — Waldman: shut out in week one despite 'primary receiver' talk; hold, don't sell low (2024 takes, stale)
- [[Luke Musgrave]] — TE, GB — Waldman's pre-draft 7th-ranked TE, now sees as "slightly overrated" relative to teammate Tucker Kraft *(2024 takes, stale)*
- [[Tucker Kraft]] — TE, GB — the value pick of Green Bay's two rookie tight ends per Waldman — more rugged, more room to grow, and cheaper on his board *(2024 takes, stale)*
- [[Brevyn Spann-Ford]] — TE, Minnesota prospect — 6'7"/270; looked lost as a blocker in 2022, visibly figured out technique by late 2023 per Waldman; projects as a practice-squad/depth-TE NFL path *(2024 pre-draft takes, stale)*
- [[Kyle Pitts]] — TE, ATL — Waldman: McVay-style system plus a real QB should restore his rookie-year form (2024)
- [[Pat Freiermuth]] — TE, PIT — real usage-risk flag off the Arthur Smith hire, not a talent knock — "two of three" Steelers TEs will be fine and it's "probably going to be the more athletic two," an explicit Kyle-Pitts-underuse comparison *(2024 takes, stale)*
- [[Brycen Hopkins]] — TE, LAR — pending free agent, promising but flawed (RAC ability, athletic, but poor blocker with drop issues); Dustin Keller comp; deep-league stash or wait-and-see, not a lead-role bet *(2024 takes, stale)*
- [[Brock Bowers]] — TE, LV — Angelo/Waldman: Vernon Davis-Hernandez hybrid, 90%+ snaps, leapfrogs Meyers in pecking order
- [[George Kittle]] — TE, SF — quiet Super Bowl LVIII box score plus a brief locker-room injury scare; career-best yards-per-target season in 2023; flagged as one leg of a coming SF pass-catcher roster crunch (Aiyuk/Deebo/Kittle can't all stay past 2024) per Harmon *(2024 takes, stale)*
- [[David Njoku]] — TE, CLE — Waldman: still TE8 value post-Jeudy trade, retains Browns #2 role behind Amari Cooper on Watson tie (2024, stale)
- [[Ja'Tavion Sanders]] — TE, CAR — meaningful games but not a weekly starter as a rookie; promising dynasty hold (2024 takes, stale)
- [[Ben Sinnott]] — TE, WAS — rookie GM comp spans George Kittle to Kyle Juszczyk; Harmon expects more 12-personnel usage.
- [[Jack Westover]] — TE, Washington prospect — Waldman: walk-on who catches everything, projects zone/fullback role
- [[A.J. Barner]] — TE, Michigan (2024 prospect) — Waldman: NFL athlete, not a fantasy option; 2-3 TE-set/matchup role
- [[A.J. Stogner]] — TE, Oklahoma (2024 prospect) — Waldman: move TE, zone-coverage blocker/wall-off type, reserve ceiling
- [[Baylor Cupp]] — TE, Texas Tech (2024 prospect) — Waldman: severe leg-injury history, still moves well, needs route craft
- [[Cade Stover]] — TE, HOU — underrated per both hosts; path to grow as Texans pass-catchers thin out behind Stroud
- [[Dallin Holker]] — TE, Colorado State (2024 prospect) — Waldman: strong hands/tracker, needs 2-3 years on timing routes
- [[Devin Culp]] — TE, Washington (2024 prospect) — Waldman: undersized, high-point ability but clap-catcher lapses
- [[Eric All]] — TE, CIN — dynasty stash, 2024 blocked by Cincinnati's TE room (2024 takes, stale)
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
- [[Isaiah Likely]] — TE, BAL — Waldman: must-add; BAL at 53% two-TE sets vs ~10% last year, huge upside if Andrews misses time (2024)
- [[Michael Mayer]] — TE, LV — Waldman: Raiders' blocker-first TE coaching philosophy makes Mayer the likely TE2, Bowers boom/bust
- [[Chigoziem Okonkwo]] — TE, TEN (new page) — Harmon: expects a return to true in-line Y role; talented but never had a defined role, worth monitoring
- [[Zach Ertz]] — TE, WAS — Harmon skeptical; views Ertz as a fading placeholder while rookie Ben Sinnott is groomed for immediate role
- [[Evan Engram]] — TE, JAX — 115+ targets in 2023; Waldman/Angelo call him a locked-in top-2 piece of the Jaguars' passing game.
- [[Taysom Hill]] — TE, NO — Waldman's round-12+ league winner: Kubiak system, red-zone monster, TE2/TE3 upside (2024)
- [[Dallas Goedert]] — TE, PHI — buy at ~TE10 price; Kellen Moore's tight ends historically produce, practice points to heavier usage (2024 takes, stale)
- [[Trey McBride]] — TE, ARI — Klassen/Koh: star every-down weapon, a stated condition for a Kyler Murray leap (2024 takes, stale)
- [[Mark Andrews]] — TE, BAL — Waldman rejects the 'washed' narrative; a zone-beater KC has clamped 5 straight games (2024 takes, stale)

<!-- Claude: maintain grouped by position (QB / RB / WR / TE), each with a
     one-line summary. See CLAUDE.md "Index maintenance". -->

## Concepts

- [[Aging Curves and Career Longevity]] — Waldman: 'washed' verdicts from one game are near-worthless; decline is harder to see than peak ability
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
- [[Running Back Dead Zone]] — New concept -- JJ Zachariason's running back 'dead zone': rookie RBs are the exploitable value there, per his ADP research
- [[Pocket Passer Trap]] — New concept -- JJ Zachariason's 'pocket passer trap': fade immobile QB1s, pair cheap mobile-adjacent QB2s instead
- [[Play Caller Cheat Codes]] — Play-action +26%, snap motion +55%, 2-WR sets +29% PPR per route; McFarland's play-caller scorecard
- [[Catch Technique and Ball Tracking]] — RSP hands study: elite WRs attack the ball 94% of the time, WR3s 58% with triple the serial flaws
- [[Training Camp Report Skepticism]] — Preseason clips mostly confirm college tape; coach-speak marks a coach's blind spots, not a scouting report
- [[Ball Security and Fumble Rate Grading]] — Waldman study: sub-threshold college ball security means only 3% reach elite fantasy production, 10% reach RB1/RB2
- [[Tight End Value in Condensed Formations]] — Waldman's framework: condensed/multi-TE formations create the matchups that make tight ends safe
- [[FAAB Budget Allocation Strategy]] — Concept — cap any single FAAB bid near 50%; all-in early only fits hyper-active traders
- [[Sacrificial X Receiver]] — The clear-out/blocking outside receiver who earns snaps without targets — Harmon's frame for Pierce, Hollins, Doubs
- [[Draft for Talent, Trade for Need]] — Dynasty roster theory — Harstad's 'nobody has needs in June'; draft best talent, convert surplus by trade (2024)
- [[Bench Spots as Information Options]] — Roster theory — last bench spots buy information, not upside; waiver wire as your practice squad (2024)
- [[Preseason ADP vs In-Season Production]] — Week-one usage is a starting point, not a verdict — pair utilization with film and game context
- [[Kickoff Rule Change and Return Scoring]] — 2024 kickoff rules — Harstad models 50-60% return rate; return scoring becomes fantasy-relevant again (2024)
- [[Win-Win Trade Construction]] — Dynasty trades now require agreement, not disagreement — trade around consensus price and count the freed roster spot as value

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
