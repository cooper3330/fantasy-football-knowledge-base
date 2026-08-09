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
- [[Baker Mayfield]] — QB, TB — Doherty and Harris both bust him: 7.2% TD rate vs 4.6% career, sixth-round ADP indefensible (2025 takes)
- [[Justin Fields]] — QB, NYJ — Waldman: same player as ever; startable but volatile, and a tuck-and-run cap on Hall's targets
- [[Derek Carr]] — QB, NO — retired May 2025; Waldman saw it coming after the Shough pick (2025 takes)
- [[Justin Herbert]] — QB, LAC — Harris 2025 flag player #8; 10th-round QB the market wrongly wrote off as too run-heavy (2025 takes)
- [[Russell Wilson]] — QB, NYG — Harris calls Week 1 horrendous and says the Giants cannot use him much longer; Dart shots on TV
- [[C.J. Stroud]] — QB, HOU — Waldman drops him toward QB2 after the OL teardown and Tank Dell's ACL (2025 takes)
- [[Jared Goff]] — QB, DET — Zachariason's headline fade at ~QB8 as the pocket-passer trap; Waldman: good NFL QB, bad fantasy price (2025 takes)
- [[Lamar Jackson]] — QB, BAL — Harmon: most varied passing game of his career on Monken fit, OL fix, Flowers usage; EPA disagrees (2024 takes, stale)
- [[Patrick Mahomes]] — QB, KC — Waldman calls him the bargain of the top-5-to-7 QBs on a stated Chiefs push back downfield
- [[Jalen Hurts]] — QB, PHI — Waldman prefers him to Daniels on price; tush push retained, 52 rushing TDs in four years (2025 takes)
- [[Brock Purdy]] — QB, SF — Waldman's 'discount Joe Burrow'; QB6 two years ago, drafted well outside QB12 (2025 takes)
- [[Kyler Murray]] — QB, ARI — both hosts doubt he can support two top-20 WRs; won't climb pocket, misses open reads (2025 takes)
- [[Drew Lock]] — QB, NYG — takes over from Daniel Jones; film-based arm talent, historically boosts WR/TE production (2024 takes, stale)
- [[Gardner Minshew]] — QB, LV — Waldman buying: reads, anticipation, mid-season rapport with Adams and Bowers (2024 takes, stale)
- [[Anthony Richardson]] — QB, IND — lost job to Daniel Jones; Harris says his 2024 top-50 ADP was dreadful analysis (2025 takes, stale)
- [[Joe Flacco]] — QB, CLE — Waldman: starts all season as scheme fit and 2026 bridge; turnovers the bench risk
- [[Jordan Love]] — QB, GB — Waldman sees reactivity and a 'high-class Jameis Winston' profile; Harris outside the QB1s (2025 takes)
- [[Dak Prescott]] — QB, DAL — Harris outside top 12 on 2024 offensive evidence; flags he could be wrong (2025 takes)
- [[Bryce Young]] — QB, CAR — Harmon/Kinnan: functional not good; best middle-of-field short QB, but can't drive the ball (2025 takes)
- [[Michael Penix Jr.]] — QB, ATL — Waldman all-in: full command vs Tampa blitz/man; expects downfield aggression to follow
- [[Tua Tagovailoa]] — QB, MIA — Waldman says QB22 ADP is too cheap; he'd value him QB15-17 with Prescott and Purdy (2025 takes)
- [[Drake Maye]] — QB, NE — Harris calls Week 1 terrible and says he is not a 1QB-league starter right now (2025 takes)
- [[Bo Nix]] — QB, DEN — Harris' No. 5 bust; not ranked as a fantasy starter, expects at best a repeat of the rookie year (2025 takes)
- [[Caleb Williams]] — QB, CHI — hosts dismiss the Ben Johnson friction reports; Waldman projects ~4,000/31, QB13 with top-6 upside (2025 takes)
- [[Jayden Daniels]] — QB, WAS — falls to the back of Waldman's top ten if McLaurin holds out or is traded; supporting cast is the concern
- [[J.J. McCarthy]] — QB, MIN — Harris' No. 2 Week 1 terror; growing pains expected, drags Jefferson's floor if it goes Zach Wilson-esque (2025 takes, stale)
- [[Spencer Rattler]] — QB, NO — won the starting job over Tyler Shough; Harris saw god-awful rookie tape but allows Kellen Moore upside (2025 takes)
- [[Tanner Mordecai]] — QB, Wisconsin prospect (SMU/Oklahoma transfer) — rocky transfer-year tape, rebounded late vs. LSU; Waldman's grade is future backup of value, not a starter *(2024 pre-draft takes, stale)*
- [[Jack Plummer]] — QB, Louisville prospect — accuracy is the whole story per Waldman: "if he had the accuracy, he would probably be a top-five quarterback in this class" *(2024 pre-draft takes, stale)*
- [[Joe Milton III]] — QB, DAL — Waldman/Kluge both sour: big arm, no touch or processing; superflex emergency only (2025 takes)
- [[Desmond Ridder]] — QB, ARI — traded from Atlanta for Rondale Moore after Falcons signed Kirk Cousins
- [[Kirk Cousins]] — QB, ATL — Waldman buys the velocity return a year post-Achilles; questions his leadership but rates him above Garoppolo
- [[Daniel Jones]] — QB, IND — named Colts starter over Richardson; Harris sees a mistake-prone bridge, minimal lift for pass catchers
- [[Ryan Tannehill]] — QB, TEN — speculative Pittsburgh reunion with former OC Arthur Smith; projected as a Joe-Flacco-style veteran room presence, not a starter bet *(2024 takes, stale)*
- [[Aaron Rodgers]] — QB, PIT — Waldman: back but not MVP-caliber; boots and audibles, strong Arthur Smith fit
- [[Matthew Stafford]] — QB, LAR — Chona: epidurals imply herniated disc; contact and non-contact re-aggravation risk high (2025)
- [[Joe Burrow]] — QB, CIN — Harris's only early QB; discounted for not rushing, elite passing floor on a shootout team
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
- [[Deshaun Watson]] — QB, CLE — Harmon: done as a starter; last in catchable air yards, scheme misfit, Achilles recovery (2024 takes, stale)
- [[Jacoby Brissett]] — QB, NE — good bridge caretaker, but pressured on 44.3% of dropbacks; no boot game (2024 takes, stale)
- [[Will Levis]] — QB, TEN — Waldman 2025: 'fuck it,' processing is the real flaw; mechanics work treats symptoms, No. 1 pick looms
- [[Sam Darnold]] — QB, SEA — Waldman: keeps the job over Milroe; pressure/blitz play is real, not just the Vikings ecosystem (2025 takes)
- [[Sam Howell]] — QB, SEA — backup-level and a bad fit behind a leaky line; 22% sack rate in relief (2024 takes, stale)
- [[Aidan O'Connell]] — QB, LV — Harmon would start him over Minshew; Raiders projected last in pass attempts (2024 takes, stale)
- [[Geno Smith]] — QB, LV — Waldman: QB22 is value; 4,000 yards, 68% completions, Bowers-led passing game (2025 takes)
- [[Zach Wilson]] — QB, NYJ — Waldman: Baker-Mayfield-style redemption in range if he matures; could be out of league in years
- [[Josh Allen]] — QB, BUF — most talented QB in the league but chasing hero throws; 9-for-30 vs HOU (2024 takes, stale)
- [[Trevor Lawrence]] — QB, JAX — Koh bold call: top-five fantasy QB under Coen; Harmon agrees (2025 takes)
- [[Trey Lance]] — QB, LAC — Waldman a deep dynasty stash; sharp preseason, no pressure, first stable org and QB coach to learn under
- [[Malik Willis]] — QB, GB — Angelo says most GMs would now take him over Will Levis; self-awareness cited as the turn (2024 takes, stale)
- [[Jameis Winston]] — QB, NYG — Harmon: 2yr/$8M means bridge/backup, 'zero percent chance' of 17 starts (2025 takes, stale)
- [[Jake Haener]] — QB, NO — Waldman: better than Rattler now; startable-at-times backup who feeds Olave safely (2024)
- [[Hendon Hooker]] — QB, DET — Waldman near-out; backup ceiling, Josh Dobbs career path projected (2024 takes, stale)
- [[Tyson Bagent]] — QB, CHI — Waldman sees a real future and trade value; top QB waiver watch-list name behind Williams (2024 takes, stale)
- [[Cam Ward]] — QB, TEN — rookie; quick release impressed Gretch in preseason, Harris sour on coaching around him (2025 takes)
- [[Darian Mensah]] — QB, Tulane — aggressive downfield passer with elite ball placement; expected power-four transfer (2024 devy takes, stale)
- [[Skylar Thompson]] — QB, PIT — backup; Waldman says Miami governed his aggression, Kansas State tape more downfield (2025 takes)
- [[Carson Beck]] — QB, Georgia — Waldman's QB1 still; buying the dip after 3-INT Texas game, blames lost Bowers/McConkey (2024 takes, stale)
- [[Jalen Milroe]] — QB, SEA — Waldman: no takeover in 2025 barring injury; expect red zone packages and garbage-time flashes only (2025 takes)
- [[Andy Dalton]] — QB, CAR — replaced Bryce Young and revived the offense; Harmon's veteran-in-a-two-high-league archetype (2024 takes, stale)
- [[Marcus Mariota]] — QB, WAS — Waldman: scheme and matchup, not the player; below Minshew as a starter (2024 takes, stale)
- [[Aidan Chiles]] — QB, Michigan State — dual-threat under Jonathan Smith; Waldman's preseason downgrade was situation-based, Marsh fixes it (2024 takes, stale)
- [[Tommy DeVito]] — QB, NYG — named starter over Drew Lock; anticipatory thrower, Rich Gannon-esque, limited vertically (2024 takes, stale)
- [[Shedeur Sanders]] — QB, CLE — Waldman's QB3/4 with borderline-starter grade; young Kirk Cousins comp; expected to start at some point in 2025 (2025 takes)
- [[Will Howard]] — QB, PIT — Kinnan (guest): Mason Rudolph comp not Josh Allen; Jekyll-and-Hyde playoff sample, average velocity, high-floor backup
- [[Kyle McCord]] — QB, Syracuse (2025 pre-draft) — doubles down on bad leverage reads; higher starter ceiling than Brosmer, far lower floor
- [[Jackson Dart]] — QB, NYG — guest Denny Carter's late deep-league stash; expected to take the starting job (2025)
- [[Tyler Shough]] — QB, NO — lost the starting job to Spencer Rattler; Harris calls it damning for a 26-year-old second-rounder (2025 takes)
- [[Kurtis Rourke]] — QB, SF — Waldman likes the Shanahan/Lynch endorsement, but he's a redshirt bridge-QB stash only in very deep leagues
- [[Dillon Gabriel]] — QB, CLE — Waldman: not a starting-caliber candidate now; whiteboard processing mistaken for field processing
- [[Max Brosmer]] — QB, MIN — fundamentally sound stash; Waldman's same-zip-code-as-Purdy comp, a two-QB/dynasty watch behind McCarthy
- [[Quinn Ewers]] — QB, MIA — Kinnan (guest) would not draft him: three injuries in three years, lost drive, checks down in a QB-friendly Sark scheme
- [[Seth Henigan]] — QB, Memphis (2025 pre-draft) — big-play arm range and good pressure escapes; placement under duress and leverage reads lag
- [[Hunter Dekkers]] — QB, FA — off-RSP late add; Waldman grades him ~QB7-10 of 12, one-step-forward/two-back (2025 pre-draft)
- [[Riley Leonard]] — QB, IND — 6th-round rookie; RP charting shows slants/curls strong, digs poor; dark-horse starter if Richardson lingers
- [[LaNorris Sellers]] — QB, South Carolina — Angelo's 2026 QB1; Roethlisberger-level sack avoidance, elite read-option, would want him to sit a year
- [[Cade Klubnik]] — QB, Clemson — Angelo's 2026 QB2; a Jared Goff comp with more athleticism and a very catchable ball at all three levels
- [[John Mateer]] — QB, Oklahoma — Angelo's 2026 QB sleeper, found via Kyle Williams tape at Washington State; better ball carrier than expected
- [[Jimmy Garoppolo]] — QB, LAR — Stafford's backup; anticipatory thrower but self-destructs under pressure, a Derek Carr comp per Waldman

### Running Backs
- [[Christian McCaffrey]] — RB, SF — calf strain surfaced two days before Week 1; Harris' top terror, high risk factor but auto-start if active (2025 takes, stale)
- [[Bijan Robinson]] — RB, ATL — Waldman prefers him at 3rd over Barkley at 2nd on workload security; 22.7 PPG from week 6 on (2025 takes)
- [[Jahmyr Gibbs]] — RB, DET — Waldman sees 'Tony Pollard syndrome': elite spark, but Detroit will not give him a bell-cow workload (2025)
- [[James Cook]] — RB, BUF — Doherty bust pick on 47.7% snaps and touchdown regression; Harris more in, citing low stuffed-run rate (2025 takes)
- [[Tyler Goodson]] — RB, IND — Waldman getting off the train; still likes the versatility but not the Indianapolis situation (2024 takes, stale)
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, HOU — had taken the job outright from Dameon Pierce in December 2023, but Waldman reverses: no longer Houston's presumptive 2024 starter, expects a free-agent RB (Jacobs or Henry) to take over; a rough Divisional Round game (9 carries, 22 yards) reinforces the need for an upgrade, though Harmon notes it followed a genuinely strong late-season stretch *(2024 takes, stale)*
- [[Saquon Barkley]] — RB, PHI — Angelo has him trending down on managed workload; Dillon/Shipley as deliberate redundancy for a playoff push
- [[Derrick Henry]] — RB, BAL — Waldman bets on another top-5 season at 31-32 after the 2-year extension; ~305/850/16 (2025 takes)
- [[Joe Mixon]] — RB, HOU — on NFI list, out 4+ games; Harris cut him to an 8th-round flag player (2025 takes, stale)
- [[Alvin Kamara]] — RB, NO — Harris still above ADP and long-time booster; only fear is the age cliff arriving fast (2025 takes)
- [[Breece Hall]] — RB, NYJ — best player on the field Week 1, 145 scrimmage yards, 36-19 snap edge; Harris says the summer fades look dumb
- [[Nick Chubb]] — RB, HOU — Week 1 lead snaps but no juice on film; Harris says he no longer loves the player (2025 takes)
- [[David Montgomery]] — RB, DET — Waldman calls RB24 price a value; 16 PPG in games played, still in prime (2025 takes)
- [[Isiah Pacheco]] — RB, KC — only 28-23 snap edge on Hunt, who owned third down and short yardage; Harris calls the role not great
- [[Kyren Williams]] — RB, LAR — Harris's safest round-3 pick; new contract kills the disposable-back case, workload injury risk
- [[Kenneth Walker III]] — RB, SEA — out-snapped 29-20 by Charbonnet and lost the goal-line score; Harris says it did not look good
- [[Raheem Mostert]] — RB, LV — Waldman buys a real split behind Jeanty; Harris doesn't believe Carroll. Both like RB69 price (2025 takes)
- [[James Connor]] — RB, ARI — both hosts hanging on for 2024; "toast" skepticism reframed as a second-contract finance story, not a talent decline; Michael Carter cuts into but doesn't replace him *(2024 takes, stale)*
- [[Aaron Jones]] — RB, MIN — Waldman's sneaky weapon back; Mason split frees slot receiving work while Addison is out
- [[Zamir White]] — RB, LV — Koh doubts he fits Chip Kelly's scheme; possible cap/roster casualty (2025 takes, stale)
- [[Tank Bigsby]] — RB, JAX — Harmon: bad pass protection, limited; third in the Jags backfield (2025 takes)
- [[Kendre Miller]] — RB, NO — Waldman: has the talent behind Kamara, but week-to-week unreliability; Akers signed as insurance (2025 takes)
- [[Chase Brown]] — RB, CIN — both hosts skeptical the late-2024 touch spike holds; a balanced 1A, screen-game receiver, Brooks siphons red-zone work
- [[Tony Pollard]] — RB, TEN — round-6 high-floor flex; secure touches but poor goal-line conversion (2025 takes, stale)
- [[Michael Carter]] — RB, ARI — Waldman's dark-horse over Trey Benson as pass-pro/receiving complement to James Conner; 'basically free money' late/waiver
- [[Austin Ekeler]] — RB, WAS — Angelo expects him to lead Washington's backfield work in 2025 ahead of Croskey-Merritt (2025 takes)
- [[Josh Jacobs]] — RB, GB — Harris's most-drafted 2025 player; first-round grade, called ADP ~23 overall 'easy money' (2025 takes)
- [[Najee Harris]] — RB, LAC — Waldman: Week 1 absence was conditioning, not role; expects near-even split with Hampton
- [[Jaylen Warren]] — RB, PIT — more effective back but splitting early-down work with Gainwell after Week 1 (2025 takes)
- [[Jordan Mason]] — RB, MIN — Bloom projects team lead in carries/TDs on Vikings run shift; Harris doubts the premise (2025 takes)
- [[Elijah Mitchell]] — RB, KC — Harris' top-ranked KC backup by default, but he is wavering toward Brashard Smith; no 2024 tape at all (2025 takes)
- [[Tyler Allgeier]] — RB, ATL — Bijan Robinson's complementary piece; "plays really well when in the system they put him in" *(2024 takes, stale)*
- [[Blake Corum]] — RB, LAR — Waldman: better than the market thinks, zone-scheme edge over Hunter; RB63 ADP (2025 takes)
- [[De'Von Achane]] — RB, MIA — Harris split: doubts the player, respects the speed; calf and Dolphins offense are the risks
- [[Braelon Allen]] — RB, NYJ — Montgomery-style role but weaker line/QB; RB3/RB4 value, Waldman buys around RB44-40 (2025)
- [[Jonathan Brooks]] — RB, CAR — stock cratered on injuries per Waldman; not expected back as a factor (2025 takes, stale)
- [[Blake Watson]] — RB, DEN — deepest sleeper in the Denver room; best receiving back there if Harvey stumbles under Payton (2025 takes)
- [[Jabari Small]] — RB, Tennessee prospect — Shrine Game name Waldman likes; undersized (205 lbs) but runs hard with good vision and decision-making *(2024 pre-draft takes, stale)*
- [[Ray Davis]] — RB, BUF — Harris's underpriced 12th-13th round Cook handcuff; power plus surprising one-foot cutting
- [[Dylan Laube]] — RB, LV — late-round stab/waiver target; pass-catching plus better inside running than reputation (2024 takes, stale)
- [[Daijun Edwards]] — RB, Georgia prospect — quick and shifty despite playing through an MCL injury, good pass catcher/blocker; Jalen-Richard floor, dynamic-James-White ceiling; likely the most-rostered of Waldman's three underrated 2024 RBs on name value alone *(2024 pre-draft takes, stale)*
- [[George Holani]] — RB, SEA — beat out Martinez; Walker-style scat back with special-teams value (2025 takes)
- [[Deshaun Fenwick]] — RB, Oregon State prospect — Shrine Game favorite; Leonard-Fournette-adjacent big-back build, gap-scheme thumper, projects as a reserve "B-back" *(2024 pre-draft takes, stale)*
- [[Brian Robinson Jr.]] — RB, SF — named the handcuff of all handcuffs after McCaffrey's calf strain; priority add if free (2025 takes, stale)
- [[Tyjae Spears]] — RB, TEN — on IR with a high ankle sprain, out at least four games (2025 takes)
- [[Mario Anderson]] — RB, LAR — UDFA bowling-ball who fits McVay's type; deep-roster stash only (2025 take)
- [[Cody Schrader]] — RB, Missouri prospect — Angelo's late-round pick to make a roster and stick; 1,800 total yards/14 TDs at Missouri, Senior Bowl standout, graded a smart, reliable long-term role player rather than a star *(2024 pre-draft takes, stale)*
- [[Kendall Milton]] — RB, Georgia prospect — unique size/speed at 6'1"/220-225; hasn't yet shown the Eddie-George-level ceiling his HS recruiting profile promised; combine/pro day season is the swing factor for his stock *(2024 pre-draft takes, stale)*
- [[Kimani Vidal]] — RB, LAC — Waldman reverses to buy: Edwards' IR opens a path, best Dobbins handcuff, plus-pass-protector (2024 takes, stale)
- [[Will Shipley]] — RB, PHI — rotated in first series then left with a rib injury; Harris says Barkley has no rosterable handcuff yet (2025 takes, stale)
- [[Rasheen Ali]] — RB, Marshall prospect — explosive pre-ACL flash back who returned to the same level; graded the best RB at the 2024 Senior Bowl for his limited reps there; ball security is the swing risk *(2024 pre-draft takes, stale)*
- [[Jaylen Wright]] — RB, MIA — out Week 1, Jeff Wilson signed back; Harris downgraded him in the Almanac update (2025)
- [[Dillon Johnson]] — RB, Washington prospect — Waldman's fourth early-round-talent name; played through multiple injuries into the national title game, some of the best contact balance in the class, but a real breakaway-speed/explosiveness ceiling concern *(2024 pre-draft takes, stale)*
- [[Trey Benson]] — RB, ARI — Waldman feels the 1A/1B talk; big-play back worth a double-digit-round bet behind Conner
- [[Bucky Irving]] — RB, TB — Harris reverses his August skepticism after a 43-14 snap and 18-3 touch edge in Week 1
- [[Marshawn Lloyd]] — RB, GB — Waldman expects GB RB2; game-breaker in the crease but decision-making and ball security are the gates (2025 takes)
- [[Khalil Herbert]] — RB, CHI (likely cut) — Waldman: top-5 waiver-wire stash if he lands in a backfield with need
- [[Roschon Johnson]] — RB, CHI — holds goal-line work, but Waldman sees Monangai's pass-pro trust squeezing him out (2025 take)
- [[Javonte Williams]] — RB, DAL — Harris's bounce-back pick; distrusts the efficiency metrics, likes the 10th-round price
- [[Samaje Perine]] — RB, KC — Waldman's preferred Chiefs back with Pacheco out: passing-game and red-zone work, low-end starter ceiling (2024 takes, stale)
- [[Rachaad White]] — RB, TB — back at practice from groin; both hosts ~top-40 Week 1, well above ADP (2025 takes)
- [[DeAndre Swift]] — RB, CHI — Cousin Josh's #5 frag; RB28 for him vs ADP 60, capped upside, Harris's #1 film room zero (2025 takes, stale)
- [[Alexander Mattison]] — RB, LV — Signs as Zamir White's backup; Waldman defends his zero-TD 2023 as a Minnesota QB/red-zone issue, not a talent flaw.
- [[Zach Moss]] — RB, CIN — ceding lead work to Chase Brown; Waldman keeps him as a good secondary back, 8-12 touches (2024 takes, stale)
- [[Aidan Robbins]] — RB, BYU (2024 prospect) — Waldman: strong downhill gap runner, needs to press deeper to fit zone schemes too
- [[Audric Estime]] — RB, DEN — Waldman: 'slightly plus Samaje Perine', good creases, likely committee not every-down (2024 takes, stale)
- [[Isaac Guerendo]] — RB, SF — pushed out of the CMC handcuff role by the Brian Robinson Jr. trade (2025 takes)
- [[Isaiah Davis]] — RB, South Dakota State (2024 prospect) — Waldman: strong man-coverage route runner, needs more decisive vision as a runner
- [[Jalen White]] — RB, Georgia Southern (2024 prospect) — Waldman: solid short-yardage gap runner, decision-making/leverage reads are the issue
- [[Jase McClellan]] — RB, Alabama (2024 prospect) — Waldman: sharp cutter, a competent runner; unclear if that means a competent NFL starter
- [[Montrell Johnson]] — RB, FA — Waldman: underrated speed, outside-zone upside, post-draft waiver name (2025 pre-draft take, stale)
- [[Tyrone Tracy Jr.]] — RB, NYG — Harmon: 'looks like a keeper' despite the fumble; part of the young core worth building around (2024, stale)
- [[Miyan Williams]] — RB, Ohio State (2024 prospect) — Waldman: smart, physical; ceiling of a Peyton-Barber-type committee back
- [[Frank Gore Jr.]] — RB, Southern Miss (2024 prospect) — Waldman: smart cutback runner, must prove he can transcend size like Devin Singletary
- [[Emani Bailey]] — RB, TCU (2024 prospect) — Waldman: inconsistent gap reads, too tight or too wide; needs better control/vision
- [[Dylan McDuffie]] — RB, Kansas (2024 prospect) — Waldman: willing tight-crease runner, Raheem-Mostert-lite burst without the blink-of-an-eye separation
- [[Michael Wiley]] — RB, Arizona (2024 prospect) — Waldman: needs better leverage attacking defenders, same early issue Jahmyr Gibbs had
- [[Gus Edwards]] — RB, LAC — last in league YPC after a top-10 all-time career mark; Harstad calls it noise, not decline (2024 takes, stale)
- [[Travis Etienne Jr.]] — RB, JAX — Harmon's clear pick to lead the Jags backfield after charting every back (2025 takes)
- [[J.K. Dobbins]] — RB, DEN — Waldman has him as Denver's clear No. 1 back ahead of rookie RJ Harvey
- [[Chuba Hubbard]] — RB, CAR — Harris flag player, early-3rd ranks vs 4th-round cost; consistent touches and goal-line role
- [[Miles Sanders]] — RB, CAR — Angelo blames poor Panthers infrastructure/ownership, not talent loss, for his decline
- [[Dylan Johnson]] — RB, TEN UDFA — Waldman's other favorite; projects as low-red-zone role Titans currently lack
- [[Eric Gray]] — RB, NYG — new page; Waldman has Gray 60/40 over Tyrone Tracy Jr. for the complementary role behind Singletary
- [[Dameon Pierce]] — RB, HOU — new page; Waldman: starter role over, misused as a non-receiving back despite receiving ability at Florida
- [[Deuce Vaughn]] — RB, DAL — not viewed as a 2024 fantasy factor; buried behind Elliott/Dowdle regardless of role changes
- [[Justin Strong]] — RB, IND (UDFA) — tryout with Colts; Waldman flags burst/vision but wants a deep-league watch, not a draft pick
- [[Zach Charbonnet]] — RB, SEA — 29 snaps to Walker's 20 plus the goal-line TD; Gold sees him as the trusted red zone back
- [[Cordarrelle Patterson]] — RB, PIT — Waldman: top-15 waiver monitor, but age/build cap him to short-stint upside only
- [[Leonard Fournette]] — RB, FA — Waldman: monitor-only 'next Latavius Murray' type until there's a real, proven role
- [[Ashton Jeanty]] — RB, LV — Waldman: talent real but bad situation; rookie-LT-2001 comp, won't return 2025 ADP
- [[Trevor Etienne]] — RB, 2025 prospect — 'lunch pail' back; adequate everywhere, spot-start/tertiary projection per Angelo (2025 pre-draft takes, stale)
- [[Ollie Gordon II]] — RB, MIA — injuries leave him and Achane as the only healthy backs; Week 1 workload is the story (2025)
- [[Jaleel McLaughlin]] — RB, DEN — Waldman's favorite Denver back at an RB50 price; Payton receiving-back archetype (2024 takes, stale)
- [[Clyde Edwards-Helaire]] — RB, KC — on NFI list to open 2024, out four games; no fantasy path offered (2024 takes, stale)
- [[Deneric Prince]] — RB, KC — camp first-team reps not an endorsement; monitor only, roster risk (2024 takes, stale)
- [[Justice Hill]] — RB, BAL — Waldman's preferred late Derrick Henry handcuff; some standalone TD value (2025 takes)
- [[A.J. Dillon]] — RB, PHI — Waldman: real closeout/short-yardage threat to Shipley behind Barkley, badly underrated (2025 takes)
- [[Christopher Brooks]] — RB, GB — Waldman: no standalone role behind Jacobs, but likely lead back if Jacobs misses time (2024 takes, stale)
- [[Sione Vaki]] — RB, DET — Waldman: cheap luxury-spot stash behind Gibbs after Montgomery MCL injury (2024 takes, stale)
- [[Jordan Lyle]] — RB, Miami — Angelo devy watch: Gibbs-like HS tape, late-1st/early-2nd upside, small frame (~185 lbs)
- [[Kyle Monangai]] — RB, CHI — 5% rostered Week 1 waiver target both hosts ranked; short-yardage upside if Ben Johnson splits carries (2025)
- [[Jacory Croskey-Merritt]] — RB, WAS — fine Week 1 debut and a TD, but Ekeler started and much of the work was garbage time
- [[Carson Steele]] — RB, KC — dropped to third up after a fumble; Waldman cites weak pass-pro and pass-catching (2024 takes, stale)
- [[Rico Dowdle]] — RB, DAL — Waldman: Arian Foster comp, likely 2025 camp starter but faces draft competition (2024 takes, stale)
- [[Ezekiel Elliott]] — RB, DAL — late-round shot; elite short-yardage and pass pro, limited fantasy upside (2024 takes, stale)
- [[Dalvin Cook]] — RB, DAL — fallback committee piece only; Harris sees a Fournette-style dead end (2024 takes, stale)
- [[Sean Tucker]] — RB, TB — repeat Harris super-deep sleeper; 14-136 in his 2024 spot start, starter-level tape, blocked by Irving and White (2025 takes)
- [[Nicholas Singleton]] — RB, Penn State — 220 lbs and fast, good gap runner; outside zone needs work (2026 class, early look)
- [[Dean Connors]] — RB, Rice — Waldman: Ekeler/Swift-lineage receiving back, situational upside, well below class headliners (2024 takes, stale)
- [[Sire Gaines]] — RB, Boise State — 6-0/209 true freshman behind Jeanty; projected 2025 lead back (2024 devy takes, stale)
- [[Tahj Brooks]] — RB, CIN — Harris super-deep sleeper; the Chase Brown contingency after Moss's neck injury (2025 takes, stale)
- [[Keaontay Ingram]] — RB, KC — buried depth piece; Waldman sees Kareem Hunt style but questions dedication and opportunity (2024 takes, stale)
- [[Kalel Mullings]] — RB, Michigan — 2024 riser over Donovan Edwards; ex-LB downhill runner, day-three projection between Jordan Howard and Hassan Haskins (2024 takes, stale)
- [[Donovan Edwards]] — RB, 2025 prospect — Waldman still sees untapped gap-scheme upside after market soured (2025 pre-draft takes, stale)
- [[Nate Frazier]] — RB, Georgia — true freshman, Sharpe's pick as a future national-name back (2024 takes, stale)
- [[Quinshon Judkins]] — RB, CLE — still unsigned; hosts read it as leverage, and call him a 12th-round why-not who likely starts at some point
- [[Kareem Hunt]] — RB, KC — Week 1 third-down and short-yardage back over Pacheco; Harris rates the role above the player
- [[Jonathan Taylor]] — RB, IND — second high ankle sprain, called mild; Sermon/Goodson the stopgaps (2024 takes, stale)
- [[Isaac Brown]] — RB, Louisville — Waldman prefers him to Bucky Irving; creative but disciplined, Clinton Portis flashes (eligibility unclear)
- [[Rhamondre Stevenson]] — RB, NE — Waldman: keeps the Mr. Inside role on pass pro and receiving; Vrabel values it over speed
- [[Jerome Ford]] — RB, CLE — squeezed out by Judkins's return per Waldman/Bob Harris; Sampson keeps the change-up role
- [[Sincere McCormick]] — RB, LV — Angelo and Waldman both see a real starter; gap-scheme fit, contact balance, deep RB class the risk (2024 takes, stale)
- [[Cam Skattebo]] — RB, NYG — Waldman: David Montgomery comp, tortoise to Tracy's hare; hamstring cost camp, more even split expected late (2025 takes)
- [[Ameer Abdullah]] — RB, LV — Waldman's case study in journeyman labeling; versatile with contact balance but not a startable fantasy back (2024 takes)
- [[TreVeyon Henderson]] — RB, NE — Waldman: Mr. Outside only, below ADP; matchup-dependent behind Stevenson's inside role
- [[Omarion Hampton]] — RB, LAC — Waldman: downhill 'hammer' (Mendenhall/Latavius comps); expects closer to even split with Najee
- [[Kaleb Johnson]] — RB, PIT — two offensive snaps in Week 1; hold in 12-team leagues but unstartable per Harris (2025 takes)
- [[Brashard Smith]] — RB, KC — Angelo likes the SMU tape but expects decoy/spacing value for KC, not fantasy production, in year one
- [[LeQuint Allen]] — RB, JAX — both hosts fade the passing-down-role hype in a four-deep backfield (2025 takes)
- [[Jaydon Blue]] — RB, DAL — healthy scratch Week 1; Harris calls the camp hype generic, third on the depth chart (2025 takes, stale)
- [[Woody Marks]] — RB, HOU — 9% rostered; receiving-back upside in a messy Houston backfield, Funston fears a train wreck (2025)
- [[Devin Neal]] — RB, NO — Waldman: gap-scheme toss usage leaves him unproven; Bilal Powell utility outcome, not a Kamara heir (2025 takes)
- [[Jarquez Hunter]] — RB, LAR — camp-hype favorite behind Kyren Williams, but gap-scheme background may cost him early zone reps (2025 takes)
- [[Damien Martinez]] — RB, SEA — practice squad; Waldman keeps him as a deep-league dynasty stash behind Walker
- [[Phil Mafah]] — RB, FA — Waldman: overlooked between-tackles banger, Gus Edwards floor, Day 3 roster-maker (2025 pre-draft take, stale)
- [[Jordan James]] — RB, SF — 49ers depth-chart flyer; broken finger and Guerendo's return stalled the momentum (2025 takes, stale)
- [[RJ Harvey]] — RB, DEN — Waldman sees receiving-driven RB2 value behind Dobbins; Bob Harris prefers the much cheaper Dobbins
- [[Dylan Sampson]] — RB, CLE — Waldman: deep-league flex only; survives Judkins's return better than Ford does
- [[Marcus Yarns]] — RB, FA — Waldman's most intriguing 2025 back; electric space player, needs 200 lbs for a complement role (2025 pre-draft)
- [[Bhayshul Tuten]] — RB, JAX — Waldman: early fumbles matter more here given three-man committee; job less secure (2025 takes)
- [[Lan Larison]] — RB, NE — Koh's deep sleeper: elite hands, possible Woodhead-style hybrid pass-catching role (untracked co-host take)
- [[James Conner]] — RB, ARI — Waldman still has him leading, but only ~2/3 share as Benson's role grows; RB19 ADP roughly fair
- [[Kaytron Allen]] — RB, Penn State — interior tough-yards back, no Singleton speed; coaches always find a use (2026 class, early look)
- [[DeMond Claiborne]] — RB, Wake Forest — Waldman's early 2026 standout; good feet and windback vision, no breakaway speed, weight the question
- [[Noah Whittington]] — RB, Oregon — Hatman's under-the-radar 2026 name; flashed behind better players, injury history (untracked-guest take)
- [[DJ Giddens]] — RB, IND — Ciely's Jonathan Taylor handcuff at RB55; Montgomery comp, Addai as the lofty ceiling (2025 takes, stale)
- [[Keaton Mitchell]] — RB, BAL — Harris super-deep sleeper 3rd straight year; healthy, big-play threat, but pass-pro gap behind Justice Hill (2025 takes)
- [[Chris Rodriguez Jr.]] — RB, WAS — Angelo has him first in line for short yardage/low red zone; Waldman comps a middle-class Spencer Ware (2025 takes)
- [[MarShawn Lloyd]] — RB, GB — on IR after two camp injuries; Harris writes him off as a 2025 contributor (2025 takes)
- [[Kenneth Gainwell]] — RB, PIT — opened Week 1 as the first-quarter starter over Warren; Harris unimpressed by the player (2025 takes)

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — hamstring cost camp reps with McCarthy; Harmon passes on his +900 most-receiving-TDs price for longer odds
- [[Ja'Marr Chase]] — WR, CIN — Harris: elite but the wrong 1.01 in redraft on VBD/scarcity grounds (2025 takes)
- [[Keenan Allen]] — WR, LAC — TD on a deep cross in Week 1; Harris says he looks like a good 12th-round pick (2025 takes)
- [[Amon-Ra St. Brown]] — WR, DET — Harmon's strongest conviction play: over 1,075.5 yards, projects 1,231; man/press marks improve yearly, now 51% outside
- [[Jameson Williams]] — WR, DET — Harmon's No. 6 'best number two'; average separator but elite intermediate out/dig and YAC (2025)
- [[Brandon Aiyuk]] — WR, SF — starts 2025 on PUP recovering from ACL; slower track than Diggs (2025 takes)
- [[Tee Higgins]] — WR, CIN — Harmon's No. 3 'best number two'; maybe the NFL's best contested-catch receiver (2025 takes)
- [[Jordan Addison]] — WR, MIN — three-game suspension made real; Harris happy to draft him outside top 100 as a September stash (2025)
- [[Jayden Reed]] — WR, GB — Jones fracture in foot; Harmon skeptical of 'pain issue', expects IR/surgery within a month
- [[Noah Brown]] — WR, WAS — surprise Houston cut, signed by Washington; competent system depth pushed out by roster crowding (2024 takes, stale)
- [[John Metchie III]] — WR, HOU — Harmon sells the breakout (slot-only role player); Koh buys on vacant slot role (2024 takes, stale)
- [[Xavier Hutchinson]] — WR, HOU — dirty-work flanker ahead of the rookies to open 2025; Allen Lazard comp, low ceiling (2025 takes)
- [[Tre Tucker]] — WR, LV — Harmon expects him squeezed out entirely by Bech and Thornton after 639 routes for 47 catches (2025)
- [[Treylon Burks]] — WR, TEN — Waldman says sell/cut in dynasty: catch-point and zone issues, ~10 targets projected, may not last the year
- [[DeAndre Hopkins]] — WR, BAL — Waldman: still expects him to lead Baltimore in receiving TDs; hit-or-miss in a run-heavy offense
- [[Adam Thielen]] — WR, MIN — traded back to Minnesota as a salary dump; Harris drops him in ranks, slot appeal crushed (2025 takes)
- [[Deebo Samuel]] — WR, WAS — led the Commanders with 10 targets plus a jet-sweep TD, ahead of McLaurin in Week 1
- [[Malik Nabers]] — WR, NYG — 12 targets but Harris warns the Russell Wilson connection makes it a tough way to live (2025 takes)
- [[Marvin Harrison Jr.]] — WR, ARI — Harmon bold call: outproduces Trey McBride; 2024 low catch rate blamed on boundary usage
- [[Rome Odunze]] — WR, CHI — Angelo expects a big year-two step; Ben Johnson praises his timing and route detail (2025 takes)
- [[Keon Coleman]] — WR, BUF — Harris lifting him after alpha flashes and a one-on-one 2pt look in the Week 1 comeback (2025 takes)
- [[Ainias Smith]] — WR, PHI — slow camp start, Johnny Wilson ahead; Waldman says he needs a year or two (2024 takes, stale)
- [[Michael Gallup]] — WR, WAS — un-retired; former true X (95% outside 2020) Harmon sees as a longshot perimeter fit for Daniels (2025 takes)
- [[Brian Thomas Jr.]] — WR, JAX — Koh bold call: top-five in yards and TDs; Harmon sees possible NFL target leader (2025)
- [[Ladd McConkey]] — WR, LAC — round 2/3 turn; keeps the slot with Allen moving around, second-half 1,600-yard pace
- [[Ricky Pearsall]] — WR, SF — Harris cools on the hipster pick after a beat report casts doubt on the No. 1 role
- [[Troy Franklin]] — WR, DEN — rising on Waldman's board; blocking earned snaps at Z/slot; Chris Chambers/Lee Evans comp, WR3 path via Engram injury
- [[CeeDee Lamb]] — WR, DAL — Waldman projects 176 targets/1,500 yards; Pickens frees him from X, doesn't cost him (2025 takes)
- [[Tyreek Hill]] — WR, MIA — Harris takes the third-round upside shot; disputes Jeff Bell's 'nothing can go right' downside-only case (2025)
- [[Mike Evans]] — WR, TB — on Bell's bust list at a third-round price; both see real decline behind the engineered 1,000 yards (2025 takes, stale)
- [[Rashid Shaheed]] — WR, NO — Harmon ahead of consensus: vertical fit in a concentrated Kellen Moore offense (2025 takes)
- [[Jerry Jeudy]] — WR, CLE — flanker, not a true WR1; 2024 route volume unrepeatable, Harmon fades at top-100 ADP (2025 takes)
- [[Courtland Sutton]] — WR, DEN — still Denver's clear No. 1 but Koh calls the room fragile behind him given age/injury (2025 takes)
- [[Chris Godwin]] — WR, TB — Waldman: not obsolete behind Egbuka; expects buy-low windows and blow-up games once acclimated
- [[Rashad Bateman]] — WR, BAL — Harmon bold call: outproduces Zay Flowers; Baltimore's best press-coverage WR (2025)
- [[Stefon Diggs]] — WR, NE — 33 and off a midseason ACL; Harris WR42/Behrens WR35, both fine starting no Patriot (2025 takes)
- [[Cooper Kupp]] — WR, SEA — healthy, moved around the formation, but market skeptical he has much left; barely top 100 (2025)
- [[Quentin Johnston]] — WR, LAC — two TDs plus a drop in Week 1; Harris bumps the Chargers wideouts (2025 takes)
- [[Jaxon Smith-Njigba]] — WR, SEA — Harmon bold call: top-five receiving yards; full-field route runner, not a slot-only (2025)
- [[Zay Flowers]] — WR, BAL — Waldman: big games about once a month; Bob Harris is the standing skeptic on weekly consistency
- [[Puka Nacua]] — WR, LAR — Harmon graduates him to tier-one (6th of 6); elite intermediate/zone/press scores, weak vertical (2025 take)
- [[Tank Dell]] — WR, HOU — injury: multi-injury ACL rehab, Bob Harris says a year away; Kirk added ahead of him (2025 take)
- [[Nico Collins]] — WR, HOU — 3-25 in Week 1 behind a leaky Texans line; Harris still starts him but calls it a bad beginning
- [[Josh Downs]] — WR, IND — Harmon: sub-180-lb over-the-middle role means recurring dings; Koh out for 2025
- [[Marvin Mims Jr.]] — WR, DEN — nominal WR2 but Waldman expects Engram as the real No. 2 target and Franklin possibly passing Mims
- [[Jalen Hyatt]] — WR, NYG — boom/bust deep threat; needs a Wan'Dale Robinson injury to matter (2025 takes)
- [[Rashee Rice]] — WR, KC — six-game suspension served from Week 1 per Harris; returns ~October (2025 takes)
- [[Davante Adams]] — WR, LAR — Cousin Josh's 2025 LVP: WR15-16 price, age 33, new team, number-two role, Stafford back injury (2025 takes)
- [[Gabe Davis]] — WR, BUF — reunion practice-squad signing; Harmon: nothing burger, sacrificial-X depth only (2025)
- [[Khalil Shakir]] — WR, BUF — high ankle sprain, week to week; Harmon's pick as the room's best and most consistent player (80% vs zone)
- [[Drake London]] — WR, ATL — heavy target volume Week 1 but hurt his shoulder late; drop on a short TD (2025 takes)
- [[Michael Wilson]] — WR, ARI — year-three sleeper; strong vs man/press, poor deep success; Koh sees an 850-950 yard upside dart throw
- [[George Pickens]] — WR, DAL — Harris below ADP on offense doubts; guest Gretch takes him round 5 on target consolidation (2025 takes)
- [[Diontae Johnson]] — WR, FA — cut by Cleveland; Harmon thinks his career is over, biggest bag fumble
- [[Tyler Lockett]] — WR, TEN — declining, now a slot move-around piece; neither host sees an every-down role left
- [[Terry McLaurin]] — WR, WAS — out-targeted 10-4 by Deebo after his holdout; Harris invokes the Aiyuk precedent and warns it may last
- [[Wan'Dale Robinson]] — WR, NYG — Harmon expects volume collapse under Wilson; 75th of 76 in EPA/target at -0.23 despite 90+ catches
- [[Ronnie Bell]] — WR, SF — a name to know mostly for injury-contingency reasons behind Aiyuk/Deebo, not his own emergence *(2024 takes, stale)*
- [[Dontayvion Wicks]] — WR, GB — Harmon quietly buying as slot fill-in if Reed misses time; hands still the risk (2025 takes)
- [[Romeo Doubs]] — WR, GB — Harmon's 'Darius Slayton of the Packers': boundary X who keeps starting; heavy early snaps with the room banged up
- [[Christian Watson]] — WR, GB — likely opens season on PUP per Harmon; absence pushes early snaps to Doubs and Golden
- [[Cedric Tillman]] — WR, CLE — Harmon buys the X role, sells the Flacco bump; DFS-friendly Week 1 vs CIN (2025 takes)
- [[Tyler Scott]] — WR, CHI — "overrated on speed" pre-draft per Waldman; used as a one-dimensional RPO/deep-shot option, a Darnell-Mooney-before-he-developed comp *(2024 takes, stale)*
- [[Jonathan Mingo]] — WR, DAL — Harmon questions whether he makes the roster; power-slot-only path blocked by Lamb, athletic traits under-delivered
- [[Demario Douglas]] — WR, NE — 16% rostered; Funston likes the McDaniels slot role, Harris doubts the player himself (2025)
- [[Malik Washington]] — WR, MIA — won WR3 job over Westbrook-Ikhine; 72.1% vs man, day-two grade at a sixth-round price (2025 takes)
- [[Xavier Legette]] — WR, CAR — Harmon buying: Thielen gone, Coker IR, McMillan's X role frees him for Deebo-like job
- [[Malachi Corley]] — WR, FA — cut by Jets; Harmon calls the third-round pick an antiquated gadget mistake
- [[Javon Baker]] — WR, NE — ~40 rookie routes, unchartable; developmental one-side prospect with maturity flags (2025 takes)
- [[Roman Wilson]] — WR, PIT — healthy reset year after lost rookie season; Funston's #3 waiver flier behind Metcalf (2025)
- [[Devontez Walker]] — WR, BAL — total project per Harmon; elite athlete, no consistent college separation (2024 takes, stale)
- [[Brendan Rice]] — WR, LAC — 7th-rounder w/ elite in-breaking numbers, poor vertical/ball-tracking; deep sleeper per Matt Harmon
- [[J. Michael Sturdivant]] — WR, UCLA prospect (Cal transfer) — 6'3"/205, high-end traits that "didn't really emerge at the highest level" of production per Waldman; declared, ungraded *(2024 pre-draft takes, stale)*
- [[Marquise Brown]] — WR, KC — Waldman passes at WR58: predictably unavailable, now an over-the-middle role, 500-700 yards ceiling (2025 takes)
- [[Skyy Moore]] — WR, KC — Harmon calls his outside-receiver usage a "mis-evaluation" of the player; doesn't expect him in Kansas City's plans and would rather see him traded to restart elsewhere *(2024 takes, stale)*
- [[A.J. Brown]] — WR, PHI — won zero routes vs Dallas per Fantasy Points charting; Bob Harris blames missed August reps
- [[DeMarcus Robinson]] — WR, LAR — Rams' only real vertical/outside option post-Nacua; 75% outside, top aDOT on team (2024 takes, stale)
- [[Jahan Dotson]] — WR, PHI — 98th of 99 in YPRR in 2024 but strong camp buzz; Harmon sees a useful red-zone third option, not fantasy relevance
- [[Adonai Mitchell]] — WR, IND — strong late camp but 'don't draft'; Ciely sees the Colts' highest ceiling (2025 takes, stale)
- [[Xavier Worthy]] — WR, KC — injured on the third play of Week 1; Harris doubts his return changes the Chiefs' short-passing identity
- [[Ja'Lynn Polk]] — WR, NE — Harmon calls him a miss; miscast at X, may not make roster (2025 preseason take)
- [[Michael Pittman Jr.]] — WR, IND — Koh bold call: career-high 1,200+ yards with Daniel Jones; back injury is the risk (2025)
- [[D.J. Moore]] — WR, CHI — Angelo recasts him as a Deebo-type run-game extension, not Chicago's primary target earner (2025 takes)
- [[Calvin Ridley]] — WR, TEN — clear No.1 target with Ward upgrade; Gretch fears he's too low, Harris calls him a knucklehead (2025 takes)
- [[Mike Williams]] — WR, LAC — retired after eight seasons; Harmon says he was underrated as a separator, not just a contested-catch guy (2025 take)
- [[Tyler Harrell]] — WR, deep sleeper (Miami) — Waldman: elite play speed, 'as fast as Xavier Worthy' but unproven, injury-plagued (2024 prospect, stale)
- [[Amari Cooper]] — WR, LV — retired 2025-09-04 after a ten-day Raiders return; leaves LV's receiver room unappealing (2025 takes, stale)
- [[Elijah Moore]] — WR, BUF — roster-bubble opening from injuries; Harmon says best separator and man-beater of the Bills group
- [[Christian Kirk]] — WR, HOU — out Week 1 with a pulled hamstring, possibly longer; Harris says don't chase the replacements yet (2025 takes, stale)
- [[Darnell Mooney]] — WR, ATL — back practicing after camp shoulder injury; Week 1 status murky, Harris says sit him if unsure (2025)
- [[Anthony Gould]] — WR, Oregon State (2024 prospect) — Waldman: sub-package contributor early, needs man-coverage refinement to start
- [[Bub Means]] — WR, NO — rookie depth athlete, 4.43/39.5-inch; zone-better, poor start-stop (2024 takes, stale)
- [[Jalen McMillan]] — WR, TB — to IR, possibly out past week nine; Harmon grades him a very good WR3, not a WR2 (2025)
- [[Jermaine Burton]] — WR, CIN — Harmon liked the talent, distrusts the annual good-summer reports; bar is just making the roster (2025 takes)
- [[Johnny Wilson]] — WR, PHI — inside track to WR3; Harmon's charting says true outside X, 71.4% vs man, bad contested hands (2024 takes, stale)
- [[Joshua Cephus]] — WR, UTSA (2024 prospect) — Waldman: slippery zone/YAC weapon, needs man skills to start outside
- [[Kobe Hudson]] — WR, UCF (2024 prospect) — Waldman: deep-threat sub-package piece, could grow into starting outside option
- [[Luke McCaffrey]] — WR, WAS — Harmon defends the quiet rookie year as developmental; full RP profile due August
- [[Ryan Flournoy]] — WR, Southeast Missouri State (2024 prospect) — Waldman: NFL athlete, contributor-vs-reserve hinges on releases/breaks
- [[Xavier Weaver]] — WR, Colorado (2024 prospect) — Waldman: Jordan Addison starter kit, route game a starting-caliber foundation
- [[Michael Thomas]] — WR, FA — suspended one game; Waldman expects a signing by mid-October, a waiver stash not a draft pick (2024 takes, stale)
- [[Curtis Samuel]] — WR, BUF — Harmon: KC game showed real outside role, health finally better, but snap path unclear (2024 takes, stale)
- [[Rondale Moore]] — WR, ATL — Harmon: 'not a real receiver,' pure gadget/motion piece after trade for Desmond Ridder
- [[Garrett Wilson]] — WR, NYJ — Cousin Josh's stealth bust; Harris has drafted him zero times, won't pay round three with the Jets QB room (2025 takes)
- [[Odell Beckham Jr.]] — WR — cut from Harmon's dynasty rankings entirely; he considers the career over (2025 takes)
- [[Xavier Gipson]] — WR, NYJ — Harmon 'really intrigued,' thinks he can play; eyed for bigger slot role in 2024
- [[Greg Dortch]] — WR, ARI -- Harmon/Koh's sleeper pick of a bad Cardinals room; 2024 charting subject
- [[Darius Slayton]] — WR, NYG — re-signed 3yr/$36M; Harmon: low-level starting X, bad deal, predicts a cut within a year
- [[Zay Jones]] — WR, ARI — likely WR3 above Dortch but Waldman sees only 300-400 yards; Kyler cap (2025 takes)
- [[Josh Palmer]] — WR, BUF — repeat Harris super-deep sleeper; Allen upgrade and outside role, but 26 and never cracked the Chargers lineup (2025 takes)
- [[Allen Lazard]] — WR, NYJ — Harmon: without Rodgers he is a non-NFL player; effort and production both cited
- [[D.J. Chark]] — WR, unsigned FA (Apr 2024) — Harmon: can't get open anymore, sold on Cowboys link (stale)
- [[Hunter Renfrow]] — WR, CAR — re-signed as depth after Coker injury; Waldman sees no fantasy starter value
- [[Tyler Boyd]] — WR, CIN — Harmon: overrated, declining, outside experiment doesn't work; open to Steelers fit (2024, stale)
- [[Marquez Valdes-Scantling]] — WR, SEA — signed as the sacrificial X; 23.8 YPR in NO, 'diet Coke Alec Pierce' per Harmon
- [[DeVonta Smith]] — WR, PHI — Harris a round above market, would take round 4; sees 2024 as the usage floor (2025 takes, stale)
- [[Kayshon Boutte]] — WR, NE — Waldman: Woods/Landry clone winning back-shoulder; may be NE's best WR despite playing X
- [[Jalen Coker]] — WR, CAR — short-term IR just after Thielen trade; Harmon still bullish but role risk rose (2025)
- [[Trey Palmer]] — WR, TB — new page; Waldman sees real 2023 development but reads TB's McMillan draft capital as a downgrade signal
- [[Chase Claypool]] — WR, BUF — new page; Waldman rates the signing a camp-body injury hedge, below MVS/Chark on the depth chart
- [[Kadarius Toney]] — WR, FA — cut by KC and unsigned; Harmon says he never had real route-running traits, net negative in 2023 (2024 takes, stale)
- [[Jalen Tolbert]] — WR, DAL — Harmon's 'fine, not special' third receiver; sacrificial-X space-clearer with Marvin Jones jack-of-all-trades comp
- [[Chris Olave]] — WR, NO — both hosts back a top-15 finish on volume from a trailing, downfield-throwing Saints offense (2025 takes)
- [[A.T. Perry]] — WR, NO — boundary X with press/contested-catch chops; Van Jefferson 2021 as best case (2024 takes, stale)
- [[Aeneas Smith]] — WR, PHI — Harmon deep sleeper; projected as Eagles' full-speed motion piece for new OC Kellen Moore's scheme
- [[Calvin Austin III]] — WR, PIT — Waldman: weekly starter as WR2; Rodgers back-shoulder connection and schemed backfield usage
- [[Denzel Mims]] — WR, PIT — buy-low sleeper for the open WR2 job opposite Pickens; Waldman buys the food-poisoning excuse for his lost Jets year
- [[DK Metcalf]] — WR, PIT — Waldman: WR1 usage is 'an adventure'; Rodgers's checks doing the work, shaky in key moments
- [[Brandin Cooks]] — WR, NO — Harmon: WR3 at best on the return to New Orleans; depth signing (2025 takes, stale)
- [[Andrei Iosivas]] — WR, CIN — Waldman dynasty buy: up to ~220 lbs, year-over-year gains; needs a Higgins or Burton opening. (2025 takes)
- [[Charlie Jones]] — WR, CIN — Waldman/Angelo watchlist name for Tyler Boyd's vacated slot role; Purdue product.
- [[Casey Washington]] — WR, ATL — Waldman: reliable third-down target in Week 1, but Mooney's return likely reclaims the role
- [[Parker Washington]] — WR, JAX — Waldman: underrated sleeper, grades above Dyami Brown contested/YAC/zone; deep-league redraft only (2025 takes)
- [[Jaylen Waddle]] — WR, MIA — Cousin Josh's 2025 Chipotle Award: can't quit him; always dinged up, team a mess, still buying the target-volume story
- [[Kendrick Bourne]] — WR, NE -- presumptive Week 1 X off ACL; solid man-coverage charting in 2023 sample but no great season on record
- [[Alec Pierce]] — WR, IND — 22.3 YPR 2024 was Richardson-specific clear-out volume; Harmon doubts it repeats with Jones (2025 takes)
- [[Van Jefferson]] — WR, PIT — Waldman: Jefferson's a cheap stopgap, not a real answer, until Roman Wilson is ready
- [[Jordan Whittington]] — WR, LAR — big slot, possible Kupp-lite long-term; Koh sees no fantasy meat on the bone behind Nacua/Adams
- [[Josh Reynolds]] — WR, DEN — Harmon's bet for Broncos' second-most productive receiver on known-quantity grounds (2024 takes, stale)
- [[Jakobi Meyers]] — WR, LV — trade request Aug 2025; Harmon calls his $11M/yr criminal, blocks Bech
- [[Olamide Zaccheaus]] — WR, CHI — Waldman likes a late stab; converted-RB slot/YAC fit for Ben Johnson while Burden is brought along
- [[Jalen Nailor]] — WR, MIN — camp speedster, near-lock WR3 role; waiver watch list, not draftable (2024 takes, stale)
- [[JuJu Smith-Schuster]] — WR, KC — cut by NE, re-signed with Kansas City; Harmon sees him as a role-cater profile redundant with Rashee Rice (2024 takes, stale)
- [[Tim Patrick]] — WR, DET — Harmon's favorite for WR2 during the Jameson Williams suspension; chain-moving big body (2024 takes, stale)
- [[Tyquan Thornton]] — WR, NE — Harmon: X-receiver role is a camp mirage; design-touches player, not an outside starter (2024 takes, stale)
- [[Dyami Brown]] — WR, JAX — sacrificial X/vertical role that frees BTJ and Hunter inside; 18 screens caught in 2024
- [[Tez Johnson]] — WR, TB — quick, tough slot/returner; Waldman sees bye-week flex upside later, a dynasty monitor more than a 2025 asset
- [[Tyler Johnson]] — WR, LAR — surprise Week 1 YAC flash post-Nacua; Harmon calls possible one-week flash given zero camp buzz (2024 takes, stale)
- [[Jeremiah Smith]] — WR, Ohio State — highest-rated WR recruit ever; leading OSU in receiving as an 18-year-old (2024 devy takes, stale)
- [[Ryan Williams]] — WR, Alabama — 17-year-old reclassified freshman leading Alabama in receiving; top devy stash (2024 takes, stale)
- [[KaVontae Turpin]] — WR, DAL — Waldman: emergency-only playoff stash; fastest NFL speed 22.36 mph, chunk play weekly (2024 takes, stale)
- [[Jauan Jennings]] — WR, SF — hold-in resolved with $3M bump, active Week 1, but Harris warns of an Aiyuk-style slow start
- [[Mack Hollins]] — WR, NE — placeholder X starter; snaps likely, targets not (2025 take)
- [[Travis Hunter]] — WR, JAX — slotted into the Chris Godwin role under Coen; Waldman's safest rookie WR tier (2025 takes)
- [[Devaughn Vele]] — WR, NO — traded from Denver for a fourth and seventh; passable big slot, 52.3% vs man, turns 28 (2025 takes)
- [[Sterling Shepard]] — WR, TB — with Godwin out, Harmon and Koh call him the best receiver left and likeliest target leader; injury risk (2024 takes, stale)
- [[Tutu Atwell]] — WR, LAR — $10M going-rate WR3; Harmon calls him hyper-singular speed, wants an upgrade behind Adams/Nacua
- [[Nick Marsh]] — WR, Michigan State — big boundary freshman, 3rd among FR in yards; Waldman says scoop him in C2C (2024 takes, stale)
- [[Nick Westbrook-Ikhine]] — WR, MIA — Harmon floats him as Miami's sacrificial on-line X in 3WR sets, freeing Waddle role catering
- [[Rakim Jarrett]] — WR, TB — Waldman: 'Stefon Diggs starter kit'; watch-list add on a high-scoring offense (2024 takes, stale)
- [[DJ Moore]] — WR, CHI — Harmon's most disappointing WR of 2024: miscast at X, career-low efficiency (2024 takes, stale)
- [[David Moore]] — WR, CAR — Wk12 team leader in targets/routes/yards, but Harmon sees a depth piece once Coker returns
- [[Savion Williams]] — WR, GB — Waldman's dynasty sleeper; better hands/YAC than Johnston, could take the Deebo-style role (2025)
- [[Tetairoa McMillan]] — WR, CAR — Waldman/Angelo fade the rookie hype; thin release package vs top corners, Harrison Jr. comp (2025 takes)
- [[Nick Nash]] — WR prospect, San Jose State — Waldman intrigued but not in love; timed speed decides his ceiling
- [[Jacob Cowing]] — WR, SF — 67 rookie routes and mostly special teams; getting some Deebo-style jet-sweep work in OTAs
- [[Luther Burden III]] — WR, CHI — third on depth chart behind Zaccheaus; Angelo calls him Chicago's best receiver, stretch-run breakout candidate (2025 takes)
- [[Matthew Golden]] — WR, GB — Waldman/Angelo's preferred rookie WR at cost; movement Z with 150-target upside post-Reed injury (2025 takes)
- [[Jalen Royals]] — WR, KC — Harmon's Rashee Rice insurance; Rice-like split and YAC, raw route runner (2025 takes)
- [[Andrew Armstrong]] — WR, MIA — undrafted Arkansas SEC receiving leader; Harmon day-two grade, decent X profile, 25-year-old rookie
- [[Konata Mumpfield]] — WR, LAR — 7th-round rookie on Harris's super-deep list; quick release, phone-booth quickness, roster spot not assured (2025 takes)
- [[Isaiah Bond]] — WR, CLE — legal cloud cleared, signed by Browns; Waldman dynasty buy over Bech and Tre Harris; best burst in class
- [[LaJohntay Wester]] — WR prospect, Colorado — Angelo's second-tier route runner and returner; 170-lb frame, combine matters
- [[Emeka Egbuka]] — WR, TB — two TDs in Week 1 including a baller deep post; Harris calls the rookie's debut big league
- [[Tre Harris]] — WR, LAC — Keenan Allen signing squeezes him; Harmon wants him at X (Alec Pierce type), team sees a Josh Palmer flanker (2025 takes)
- [[Jayden Higgins]] — WR, HOU — behind Xavier Hutchinson early; Harmon corrects the draft-capital prior, now even odds with Noel (2025 takes)
- [[Xavier Restrepo]] — WR, TEN — UDFA slot/zone-beater with Cam Ward chemistry; Harmon bets he outsnaps a drafted Titans rookie
- [[Justin Watson]] — WR, HOU — Harmon's archetypal sacrificial X: routes on 58.4% of dropbacks, targeted on only 8% of them
- [[Daniel Jackson]] — WR, FA — grittiest pass catcher in Waldman's 2025 class; quick slot, preferred over Restrepo (2025 pre-draft)
- [[Tai Felton]] — WR, MIN — deep dart throw; Harmon likes his underneath/YAC profile as the Rondale Moore replacement, no downfield game
- [[Kyren Lacy]] — WR, FA — Waldman: capable possession type, Noah Brown ceiling; not an outside starter unless razor sharp (2025 pre-draft take)
- [[Elic Ayomanor]] — WR, TEN — Godwin 'shades' on size/physicality only; drops and 21st pct vs zone cap him; developmental, path past Van Jefferson (2025 takes)
- [[Jaylin Noel]] — WR, HOU — Harmon: likely better than Higgins; 84th pct vs man, McConkey/Downs profile (2025 takes)
- [[Jack Bech]] — WR, LV — profile Harmon liked, but no camp impact; he writes off 2025 (2025 takes)
- [[Dont'e Thornton Jr.]] — WR, LV — favorite at X after Cooper retirement, but Harmon selling; MVS-with-hands ceiling (2025 takes)
- [[Isaiah Neyor]] — WR, SF — Waldman: nearly a top-10 board receiver but for ungraded YAC reps; deep dynasty stash, starter upside in 1-2 years (2025 takes)
- [[Arian Smith]] — WR prospect (UGA) — Waldman: 4.4 sleeper with correctable drops (unlike Tai Felton); return-man floor.
- [[Jaylin Lane]] — WR, WAS — best athlete in the room (4.34, 40-inch vert); gadget/screen profile ahead of Luke McCaffrey; uncharted (2025 takes)
- [[Ja'Corey Brooks]] — WR, FA — Waldman: elite release-to-catch-point tape, scared hands; top-7 board player if fixed (2025 pre-draft take, stale)
- [[Isaac TeSlaa]] — WR, DET — WR3 after Tim Patrick trade; slot-to-X convert, 62nd pct vs zone, 66.2% vs man; low target volume expected (2025 takes)
- [[Kelly Akharaiyi]] — WR, FA — Waldman's lone-wolf 2025 sleeper: route running and ball tracking, but likely UDFA (2025 pre-draft, stale)
- [[Bru McCoy]] — WR, FA — 6-3/230 Tennessee sleeper; young JuJu/Hakeem Nicks comp, well-rounded eventual starter (2025 pre-draft)
- [[Julio Jones]] — WR, retired — Harmon's Hall-of-Fame retrospective; 2016 as apex, 86.2% vs zone as Shanahan's X (2025 takes)
- [[Kyle Williams]] — WR, NE — no camp hype, lost the No. 2 job; Harris and guest Denny Carter both sour (2025 takes)
- [[Tory Horton]] — WR, SEA — MVS cut opens perimeter X role; Harmon says move him up draft boards
- [[Jacolby George]] — WR, FA — Waldman: Miami slot/flanker, Travis Benjamin floor to Jordan Addison ceiling (2025 pre-draft take, stale)
- [[Xavier Guillory]] — WR, FA — Waldman: physical blocker/special-teamer, Hines Ward-coached, bye-week waiver gem upside (2025 pre-draft take, stale)
- [[Jordan Moore]] — WR, FA — Waldman: YAC slot with drop problem; 'what people wrongly thought Shakir was' (2025 pre-draft take, stale)
- [[Chimere Dike]] — WR, TEN — gadgety slot move-around type; Koh's favorite of the flawed Titans supporting cast
- [[Pat Bryant]] — WR, DEN — Vele trade opens Payton power-slot work; intermediate/middle-of-field winner, no vertical separation at 4.6 speed (2025 takes)
- [[Robert Woods]] — WR, PIT — 1yr/$2M, age 33; Harmon sees locker-room tone setter for Metcalf/Pickens, no fantasy case
- [[KeAndre Lambert-Smith]] — WR, LAC — Waldman sees a real chance he passes Tre Harris; route runner whose press work is unproven
- [[Elijah Badger]] — WR, KC — UDFA; Harmon says he may be Kansas City's best X candidate, 20 YPR at Florida, press work needed (2025 takes)
- [[KC Concepcion]] — WR, Texas A&M — Waldman's favorite (not best) 2026 receiver; Angelo calls him a gamer who was NC State's whole offense
- [[Jordyn Tyson]] — WR, Arizona State — Angelo's co-top-two receiver in the 2026 class (early look, little detail)
- [[Antonio Williams]] — WR, Clemson — Angelo's co-top-two 2026 receiver; sudden slot-first profile, production capped by a loaded Clemson room
- [[Nyck Harbor]] — WR, South Carolina — on Waldman's 2026 do-not-draft list; elite track athlete who makes everything look hard, hosts want him at TE
- [[Evan Stewart]] — WR, Oregon — on the hosts' 2026 do-not-draft list; couldn't out-produce Tez Johnson as Oregon's third option
- [[Efton Chism III]] — WR, NE — UDFA slot with a strong camp; roster spot not assured, Douglas in the way (2025 takes, stale)
- [[Jordan Watkins]] — WR, SF — 2025 4th-rounder; YAC and run blocking, but spiky college production and poor explosion testing
- [[Jimmy Horn Jr.]] — WR, CAR — Waldman: buzz is warranted, unique big-play slot; must prove coverage reads and man-beating (2025)
- [[Justyn Ross]] — WR, FA — released from KC; timing route runner needing a scheme fit; Waldman likes a Steelers flanker role (2025)
- [[Beaux Collins]] — WR, NYG — camp riser; Waldman sees WR3 this year but journeyman long-term

### Tight Ends
- [[T.J. Hockenson]] — TE, MIN — Nguyen sees target uptick on bootleg crossers/flats with McCarthy at QB (2025 takes)
- [[Travis Kelce]] — TE, KC — Waldman calls him a bargain; ~800-900 yards, 8-10 TDs, possible top-five bounce-back
- [[Sam LaPorta]] — TE, DET — first-read share crashed 19.9% to 8.6% behind Jameson Williams; Harmon expects reversion (2024 takes, stale)
- [[Dalton Kincaid]] — TE, BUF — Waldman: low-end TE1/high-end TE2 ceiling; Brady's throw-to-the-open-man offense caps him (2025 takes)
- [[Luke Musgrave]] — TE, GB — Waldman's pre-draft 7th-ranked TE, now sees as "slightly overrated" relative to teammate Tucker Kraft *(2024 takes, stale)*
- [[Tucker Kraft]] — TE, GB — Angelo projects him as Green Bay's No. 2 receiver post-Reed injury; Waldman flags Musgrave risk (2025 takes)
- [[Brevyn Spann-Ford]] — TE, Minnesota prospect — 6'7"/270; looked lost as a blocker in 2022, visibly figured out technique by late 2023 per Waldman; projects as a practice-squad/depth-TE NFL path *(2024 pre-draft takes, stale)*
- [[Kyle Pitts]] — TE, ATL — Waldman: dump-down role under Penix, not trusted downfield; upside 'possible not probable' (2025 takes)
- [[Pat Freiermuth]] — TE, PIT — Waldman: only Steeler he trusts conceptually with Rodgers; production tracks QB quality (2025 takes)
- [[Brycen Hopkins]] — TE, LAR — pending free agent, promising but flawed (RAC ability, athletic, but poor blocker with drop issues); Dustin Keller comp; deep-league stash or wait-and-see, not a lead-role bet *(2024 takes, stale)*
- [[Brock Bowers]] — TE, LV — limped off Week 1 with a knee issue but expects to play Week 2; big early usage (2025 takes)
- [[George Kittle]] — TE, SF — TD on the opening drive then out with a hamstring; Harris calls it a big story to track (2025 takes)
- [[David Njoku]] — TE, CLE — Flacco's likely security blanket but contract expires; Fannin is the succession plan
- [[Ja'Tavion Sanders]] — TE, CAR — Waldman: underrated at TE31, ~700-yard pace pre-injury plus red-zone TDs = starter (2025 takes)
- [[Ben Sinnott]] — TE, WAS — year-two step possible; blocked by Ertz's veteran competency, unproven (2025 takes)
- [[Jack Westover]] — TE, Washington prospect — Waldman: walk-on who catches everything, projects zone/fullback role
- [[A.J. Barner]] — TE, Michigan (2024 prospect) — Waldman: NFL athlete, not a fantasy option; 2-3 TE-set/matchup role
- [[A.J. Stogner]] — TE, Oklahoma (2024 prospect) — Waldman: move TE, zone-coverage blocker/wall-off type, reserve ceiling
- [[Baylor Cupp]] — TE, Texas Tech (2024 prospect) — Waldman: severe leg-injury history, still moves well, needs route craft
- [[Cade Stover]] — TE, HOU — underrated per both hosts; path to grow as Texans pass-catchers thin out behind Stroud
- [[Dallin Holker]] — TE, Colorado State (2024 prospect) — Waldman: strong hands/tracker, needs 2-3 years on timing routes
- [[Devin Culp]] — TE, Washington (2024 prospect) — Waldman: undersized, high-point ability but clap-catcher lapses
- [[Eric All]] — TE, CIN — Angelo: should be starting over Gesicki; effectively Cincinnati's third receiver and red-zone threat (2024 takes, stale)
- [[Isaac Rex]] — TE, BYU (2024 prospect) — Waldman: good back-shoulder rapport, zone-role upside if he tightens crossers
- [[Jaheim Bell]] — TE/FB, NE — 7th-round pick; both hosts say no fantasy relevance outside special teams
- [[Jared Wiley]] — TE, KC — new-ish contributor; Waldman: mostly special teams early, competing with Noah Gray for Kelce-succession role
- [[McCallan Castles]] — TE, San Jose State (2024 prospect) — Waldman: good ball attack point but small margin for catching-technique error
- [[Tanner McLaughlin]] — TE, Arizona (2024 prospect) — Waldman: athletic but unrefined receiver/blocker, undersized as a blocker
- [[Theo Johnson]] — TE, NYG — Harmon's Giants deep sleeper; elite athletic testing, could lead non-Nabers targets but Bellinger is more refined
- [[Tip Reiman]] — TE, Illinois (2024 prospect) — Waldman: in-line starter athleticism, lacks route craft/guile
- [[Trey Knox]] — TE, South Carolina (2024 prospect) — Waldman: oversized-RB-type YAC role, likely special-teamer/utility target
- [[Zach Hines]] — TE, South Dakota State (2024 prospect) — Waldman: must become a very good in-line blocker to stick in NFL
- [[Dalton Schultz]] — TE, HOU — solid redraft role even as Stroud/Diggs trade drives his price down
- [[Isaiah Likely]] — TE, BAL — post-camp foot surgery, off PUP but unusable Week 1; nudges Andrews slightly safer (2025)
- [[Michael Mayer]] — TE, LV — Nguyen: value is as the in-line blocker Bowers isn't; year-three blocking leap needed
- [[Chigoziem Okonkwo]] — TE, TEN (new page) — Harmon: expects a return to true in-line Y role; talented but never had a defined role, worth monitoring
- [[Zach Ertz]] — TE, WAS — Waldman: re-signed, TE1 upside at a TE26 ADP; short-area only, fits the offense (2025 take)
- [[Evan Engram]] — TE, DEN — Zachariason above consensus; Nix's short-area game plus weak Denver target competition at a low-end TE1 price (2025 takes)
- [[Taysom Hill]] — TE, NO — Waldman's round-12+ league winner: Kubiak system, red-zone monster, TE2/TE3 upside (2024)
- [[Dallas Goedert]] — TE, PHI — Waldman sees a TE2 only; 12-game availability risk, ~600 yards if healthy (2025 takes)
- [[Trey McBride]] — TE, ARI — Waldman comfortable at TE2 as early as round three; QB risk, not talent risk (2025 takes)
- [[Mark Andrews]] — TE, BAL — Harris drafting him at soft ADP but fears he's cooked; tush-push TD upside (2025 takes)
- [[Jake Ferguson]] — TE, DAL — Waldman projects 94 targets/623 yards as a low-end TE1; cheap at TE15 ADP (2025 takes)
- [[Justin Joly]] — TE, NC State — flex/mismatch chess piece, WR-style routes; size limits an every-down role (2024 takes, stale)
- [[Noah Gray]] — TE, KC — Waldman's pick for extra Chiefs targets post-Rice: most versatile option after Kelce, YAC + trust (2024 takes, stale)
- [[Charlie Kolar]] — TE, BAL — both hosts call him a startable three-down TE buried behind Andrews/Likely; dynasty stash (2024 takes, stale)
- [[Brenton Strange]] — TE, JAX — Waldman: sneaky TE1 with Engram gone, but a deep rookie TE class could reload over him (2025)
- [[Darnell Washington]] — TE, PIT — Waldman: two-TE usage under Wilson makes him a matchup/bye-week PPR option (2024 takes, stale)
- [[Cade Otten]] — TE, TB — upside was Evans-absence-dependent; target share evaporated on his return (2025 takes)
- [[Adam Trautman]] — TE, DEN — Waldman: Payton loyalty plus athleticism make him a discounted streaming TE (2024 takes, stale)
- [[Will Dissly]] — TE, LAC — third in Chargers first-read share, leads team in designed targets since bye (2024 takes, stale)
- [[Jonnu Smith]] — TE, PIT — traded to Pittsburgh; Waldman sees a defined YAC/red-zone role, Harris doubts Arthur Smith's usage (2025)
- [[Tyler Warren]] — TE, IND — Harmon skeptical of RPO-funnel role; Koh out on him as a rookie TE (2025 takes)
- [[Harold Fannin Jr.]] — TE, CLE — Waldman: LaPorta clone, better routes than Njoku; low-end TE1, possibly top-12
- [[Colston Loveland]] — TE, CHI — camp buzz pushed ADP up all August to ~TE11/12; the tight end to wait for (2025)
- [[Mason Taylor]] — TE, NYJ — Waldman's pick to lead rookie TEs in receptions; Fields leans on TEs and the price sits outside TE2 range
- [[Elijah Arroyo]] — TE, SEA — both hosts reject the X-receiver talk; Fant-like red-zone/seam role, big slot at best
- [[Mike Gesicki]] — TE, CIN — Waldman: crazy value at TE27 ADP, sneaky TE1 in year two with Burrow despite stiff-footed profile
- [[Thomas Fidone]] — TE, Nebraska — Waldman: elite snapped turns and clean breaks; can handle inline work but it would cap receiving upside (2025 pre-draft)
- [[Gunnar Helm]] — TE, Texas — Waldman: separates short-area and up the seam but lacks breakaway explosion; route pacing too predictable (2025 pre-draft)
- [[Jackson Hawes]] — TE, Georgia Tech — Waldman: best inline blocker in 2025 class, low on RSP board; scouting interest over fantasy (2025 pre-draft take)
- [[Terrance Ferguson]] — TE, LAR — linear athlete, Gesicki-at-best ceiling; Waldman passes in redraft, viable dynasty rookie pick (2025)
- [[Oronde Gadsden II]] — TE, LAC — Waldman: route running and man-to-man wins are the doubt; the one rookie he'd admit whiffing on if buzz is real (2025 takes)
- [[Moliki Matavao]] — TE, UCLA — Waldman: polished zone route runner, but goes down far too easily after the catch for his size (2025 pre-draft)
- [[Mitchell Evans]] — TE, Notre Dame — Waldman: zone separator with size, but clap-catches and struggles changing direction in space (2025 pre-draft)
- [[Luke Lachey]] — TE, Iowa — Waldman: tweener with no clean role fit; his RSP grade likely higher than NFL's valuation (2025 pre-draft take)
- [[Keleki Latu]] — TE, Washington — Waldman: inline striker with strong hands; short-yardage contributor if he adds 15-20 pounds (2025 pre-draft take)
- [[Josh Simon]] — TE, South Carolina — Waldman: speedy H-back and YAC outlet in the flats; breaks and catch technique both leak (2025 pre-draft)
- [[Jalin Conyers]] — TE, Texas Tech — Waldman: bottom of tier three but best path to tier two; four fixable flaws in hands, breaks, blocking (2025 pre-draft)
- [[Jake Briningstool]] — TE, Clemson — Waldman: highest-variance TE in class; could be its best ball winner or a TE2/TE3 (2025 pre-draft take)
- [[Gavin Bartholomew]] — TE, Pittsburgh — Waldman: advanced stair-step and inset route setups; sloppy hands away from frame cap him (2025 pre-draft take)
- [[Caden Prieskorn]] — TE, Ole Miss — Waldman: highlight-reel one-handed catches mask a linear mover with raw routes and blocking (2025 pre-draft)
- [[CJ Dippre]] — TE, Alabama — Waldman: seam winner vs linebackers, not DBs; must protect the ball after high-pointing (2025 pre-draft take)
- [[Bryson Nesbitt]] — TE, North Carolina — Waldman: roster-caliber big-slot type with no elevating trait; WRs do that job better (2025 pre-draft)
- [[Rivaldo Fairweather]] — TE, Auburn — Waldman: athletic zone-stretcher and pass tracker; hands, grip strength and release pacing all need work (2025 pre-draft)
- [[Tyler Neville]] — TE, Virginia — Waldman: special-teamer and stopgap H-back backup; reliable hands and chain-mover, little fantasy value (2025 pre-draft)
- [[Eli Stowers]] — TE, Vanderbilt — Waldman's favorite 2026 tight end; 6-4 converted QB with real route craft and quarterback-runner traits
- [[Cole Kmet]] — TE, CHI — deep-league depth only; check-down/blocking starter, never a one-on-one matchup threat
- [[Noah Fant]] — TE, CIN — Waldman reverses to positive: schemed-up beneficiary of Chase/Higgins attention, not a weekly must-start
- [[Payne Durham]] — TE, TB — red-zone streamer if Otton sits; Waldman praises his hands and short-area work

<!-- Claude: maintain grouped by position (QB / RB / WR / TE), each with a
     one-line summary. See CLAUDE.md "Index maintenance". -->

## Concepts

- [[Aging Curves and Career Longevity]] — Age cliff vs age curve — careers fluctuate around a peak then fall off abruptly; population curve is ecological fallacy (2024 takes)
- [[Start Your Best Players]] — start top-down off your own rankings rather than chasing weekly matchups
- [[Scouting Bias and Player Archetypes]] — Harstad/Waldman: deviant personality traits are usually adaptive, and the archetype police apply the standard unevenly
- [[Weak Quarterback Play and Receiver Value]] — Bad QB play discounts a receiver's ceiling, not his production; the edge is at the draft table where the market overreacts
- [[Zone vs Man Route Running]] — Slot ceiling framework: ~80% vs zone is the baseline; beating man coverage is what unlocks the route tree
- [[Scheme vs Talent]] — Harmon: a coach's concepts travel but roles don't — don't copy-paste Detroit onto Chicago; cater scheme to the players you have
- [[Running Back Size and Movement Skills]] — change of direction in tight space as the RB separator, and the claimed ~205–215 lb ceiling on the trait (originally Brandon Angelo's argument); Nick Chubb is the standing counter-example
- [[League Trend Cycles and Market Inefficiency]] — Harstad: offense isn't down, points per drive third-best since 2016; RB targets collapsed into carries and scrambles
- [[NIL and Player Development]] — whether paid college players thin rookie classes or force the NFL to develop players; Angelo expects a chain reaction and older prospects, Harstad expects mostly nothing
- [[Pace Control and Movement Intellect]] — controlling your own gears and gauging everyone else's; the cross-positional sibling of the RB size argument, and why single-speed runners get corralled
- [[Prospect Pro-Readiness vs Ceiling]] — Harmon's upside vs 'theoretical upside' split: prefer maximised skill you have seen over measurables you must imagine
- [[Player Development and Coachability]] — whether the player will accept coaching and whether the building can give it; why a prospect's floor is usually organizational
- [[Injury-Agnostic Roster Construction]] — draft assuming everyone eventually gets hurt and price/plan for the loss, rather than avoiding injury-flagged players; "injury agnostic, not stupid"
- [[Role Difficulty and Replaceability]] — Judge receivers against the difficulty of the role assigned, not raw stats — Harmon's PhD-program framing
- [[Healthy Enough to Play vs. Healthy Enough to Perform]] — Active status is not performance capability; Waldman/Angelo use Pittman's back injury as the 2024 case study
- [[Post-Rookie-Year Receiver Model]] — Adam Harstad's touchdown-adjusted yards-per-route-run + usage-rate composite for grading rookie WR seasons; historical score buckets from "abandon all hope" to the Beckham/Chase/Jefferson/Brown "big four"; Waldman treats it as one input, not a verdict
- [[Reception Perception Methodology]] — Matt Harmon's WR charting project: success rate vs. press/man/zone coverage, route-type and alignment splits, 3-game early reads expanding to ~8-game final profiles; cross-class "stacked board" with a top-10-worthy "tier one" grade
- [[Quarterback Processing and Confidence]] — Confidence as a trackable QB trait: the gap between identification and action, per Waldman the biggest miss in QB evaluation
- [[NFL Combine and Pro Day Skepticism]] — Concept — Waldman: combine/pro-day workouts mainly useful for unknown small-school prospects, not blue-chip names; film beats lab metrics
- [[Coach Killer Prospects]] — Concept: exec forces unready rookie QB to start, coach takes blame -- Maye, McCarthy, Daniels named 2024 candidates
- [[Running Back Dead Zone]] — Waldman 2024: RBBC 'told to go fuck itself' — close to half the league running bell cows again
- [[Pocket Passer Trap]] — New concept -- JJ Zachariason's 'pocket passer trap': fade immobile QB1s, pair cheap mobile-adjacent QB2s instead
- [[Play Caller Cheat Codes]] — Play-action +26%, snap motion +55%, 2-WR sets +29% PPR per route; McFarland's play-caller scorecard
- [[Catch Technique and Ball Tracking]] — Catch-point technique as the flaw that caps a receiver at tier two rather than elite (2025 takes)
- [[Training Camp Report Skepticism]] — Waldman's rule against single-data-point judgment, esp. RB burst in camp; build a continuum of evidence
- [[Ball Security and Fumble Rate Grading]] — Waldman study: sub-threshold college ball security means only 3% reach elite fantasy production, 10% reach RB1/RB2
- [[Tight End Value in Condensed Formations]] — Waldman's framework: condensed/multi-TE formations create the matchups that make tight ends safe
- [[FAAB Budget Allocation Strategy]] — Concept — cap any single FAAB bid near 50%; all-in early only fits hyper-active traders
- [[Sacrificial X Receiver]] — Harmon walks back his own framing: the industry over-corrected into discounting X receivers; a good X is not sacrificial
- [[Draft for Talent, Trade for Need]] — Dynasty roster theory — Harstad's 'nobody has needs in June'; draft best talent, convert surplus by trade (2024)
- [[Bench Spots as Information Options]] — Roster theory — last bench spots buy information, not upside; waiver wire as your practice squad (2024)
- [[Preseason ADP vs In-Season Production]] — Waldman: June prices track story not projection — Jeanty's rookie-star premium, Pearsall's narrow-sample hype
- [[Kickoff Rule Change and Return Scoring]] — 2024 kickoff rules — Harstad models 50-60% return rate; return scoring becomes fantasy-relevant again (2024)
- [[Win-Win Trade Construction]] — Dynasty trades now require agreement, not disagreement — trade around consensus price and count the freed roster spot as value
- [[Fantasy Playoff Week Value Weighting]] — Harstad's model: one regular-season win is worth ~2% title odds; playoff weeks dominate, and team strength changes the math
- [[Roster Longevity as Talent Signal]] — Late-round hits are signalled by surviving roster competition year after year, not by rookie-year flashes (Harstad)
- [[Rookie Quarterback Evaluation Windows]] — Waldman/Angelo: communicated intermittent benching (Bradshaw, Brees) develops young QBs; silent benchings destroy locker rooms
- [[Receiver Alignment and Quarterback Field-Side Bias]] — Concept — align receivers to the side a mobile QB actually throws to; McLaurin/Daniels 2024 case study
- [[Veteran Quarterback Value in Two-High Era]] — Concept — Harmon: two-high is cyclical, not a boogeyman; veteran QBs in well-designed offenses beat it
- [[Yards After Catch Receiver Archetype]] — Why separation alone fails: modern NFL prizes zone-beating, reliable, after-catch receivers over small pure route-runners
- [[Win-Now Trade Timing]] — Harstad's rule: win-now trades only when chasing a bye, not the last playoff spot; better still, don't make them
- [[Draft Capital as Quarterback Hit Rate Proxy]] — Harstad's name-blind rule: late-second rookie pick goes to any remaining top-10 NFL draft capital QB
- [[Rushing Quarterbacks and Receiver Support]] — Waldman's 20%-of-yards line for running QBs suppressing receivers; Harstad counters that rush attempts is the cleaner measure
- [[Selection Bias and Harstad's Razor]] — Harstad's heuristic: assume any surprising finding is selection bias first; Berkson's paradox and collider examples
- [[Yards Per Carry as Noise]] — Harstad: YPC is near-random; the only repeatable input is straight-line speed, not talent
- [[Irrational Exuberance and Title Odds]] — Managers' self-estimated title odds sum past 100%; Harstad now rejects blanket pessimism for accuracy
- [[Separating the Player from the Person]] — Waldman and Harstad on evaluating on-field contribution apart from off-field conduct, and why 'flaws' are often adaptive
- [[Targets Versus Team Points Rule]] — Harmon's rule: a WR1 out-targeting his team's point total signals a broken offense, not fantasy opportunity
- [[Slot to Outside Conversion Risk]] — Harmon: inside-to-outside receiver conversions almost never take (Skyy Moore, Elijah Moore, McMillan); condensed splits blur alignment data
- [[Writing Craft in the Fantasy Industry]] — Fantasy writing is two crafts — fantasy and writing — with deadlines, volume and outlining tradeoffs (Waldman/Harstad, 2024)
- [[Feedback Scarcity and Analyst Development]] — Analyst work gets ~zero feedback; silence reads as failure but usually means fine — Harstad/Waldman on criticism (2024)
- [[Deliberate Rest and Creative Productivity]] — Waldman/Harstad: time off-screen is the work — Army artillery shift study, Friday football blackouts, burnout 3-4x/year (2024)
- [[Analyst Incentive Alignment and Audience Trust]] — Waldman: ex-player pundits are paid for controversy and confuse football knowledge with scouting; weigh their conclusions accordingly
- [[Fantasy Quarterback Value vs NFL Quarterback Quality]] — Waldman: after QB15 the gap to QB8-12 is small enough to stream matchups; Geno Smith at QB22 as the worked example
- [[Post-Bye Rookie Bump]] — Harmon: rookie post-bye improvement is a coaching-design effect, not automatic; only applies if the rookie wins on film
- [[Quarterback-Receiver Chemistry]] — Harmon and Koh: QB trust built through offseason reps drives targets in ways YPRR and separation metrics can't capture
- [[Recruiting Star Ratings and Early Breakout Age]] — Star ratings are a weak prior; early breakout beats upperclassmen for touches and signals talent — Jeanty, Judkins, Brown
- [[Cross-League Dynasty Portfolio Trading]] — Harstad's many-leagues-one-team framework: treat all dynasty rosters as one portfolio, arbitrage prices across leagues, harvest free picks
- [[Mining Bad Offenses]] — Waldman's waiver rule: skim the surface of bad offenses, dig deep only on high-scoring ones
- [[Historical Comps and Analyst Degrees of Freedom]] — Harstad: comps are 'voodoo that works'; pre-register criteria, and an 80-90% hit-rate comp list means you screwed up
- [[Confidence vs Certainty in Analysis]] — Why QB-turned-analysts aren't definitive on film: a play read rests on ~12 hidden assumptions only the huddle can confirm
- [[Right for the Wrong Reasons]] — Harstad's trust test: an analyst who admits being right for the WRONG reasons, not just wrong for the right ones
- [[Shutdown Corner Travel and Slot Coverage Difficulty]] — Why shutdown corners stopped travelling: compacted formations and the slot's unrestricted route tree (Peterson, 2024)
- [[Multi-Sport Background and Athletic Transfer]] — Concept — generalist, multi-sport backgrounds as an evaluation lens (Mahomes as shortstop, Brady as boxer); specialize only after broad exposure
- [[Deliberate Practice and the Development Sweet Spot]] — Concept — development is most efficient at ~80-90% success / 10-20% failure; frames the sit-vs-start question for young QBs
- [[Politics and Sport]] — Concept — Harstad's history that football has never been apolitical (forward pass, amateurism, NIL, integration, anthem displays)
- [[Quarterback Pressure and Career Trajectory]] — How sustained pressure degrades even good QBs, and why early-career sack punishment does not fix an outcome
- [[Resilience and Coach-GM Fit]] — Why the coach-GM pairing and team resilience are real, unmeasured inputs — Campbell/Holmes in Detroit as the case study
- [[Dented Cans]] — Buy-low framework — collapsed price without collapsed ability; expectation-driven discounts on ex-high-picks (2024 takes)
- [[Waiver Wire Archetypes and Organizational Support]] — Harstad: waivers decide ~5% of starts; hunt highly drafted backup QBs and organization-backed backup RBs (2024 takes)
- [[Serial Correlation in Player Evaluation]] — Harstad: agreement among correlated processes is weak evidence; convergence of uncorrelated ones is strong (applied to Olave)
- [[Wide Receiver Free Agency Contract Tiers]] — How Harmon tiers WR contracts: a 30M+ elite group, a ~23M second tier, and the 11-13M post-rookie bargains he prefers
- [[Running Back Workload Myth]] — Concept — Harstad's age-controlled case that career carries don't predict decline; heavy workload is a coaches' preference reveal (2024 takes)
- [[Quarterback Slide Rules and Rule Weaponization]] — Concept — QB protection rules are good, but faked slides should be penalized; enforce evenly rather than punish by public outrage (2024)
- [[Fantasy Black Hole Quarterbacks]] — Waldman/Hanowitz tiering of QBs who suppress teammate fantasy value — Allen elite, Hurts good, Murray bad, Mariota low grade
- [[Two-Way Player Routine and Snap Acclimation]] — Two-way usage as an outlier claim: Hunter's 100+ snap games, meeting-time constraints, and why the corner-first default may be conceptual not evidential
- [[Multiple Quarterback Investment]] — Harstad's case that teams should split QB bets across two players rather than concentrating on one
- [[Content Creator Audience and Paying Dues]] — Waldman/Bob Harris on audience, niche vs broad reach, dues as ongoing installments, and AI as tool not replacement
- [[Sophomore Slump]] — Waldman: 'sophomore slumps' usually measure the team's decline, not the player's; true version is a rookie who stops working
- [[Rookie Receiver Yards Per Route Run Model]] — Harstad's rookie WR YPRR+TD model and its 2024 tiers, used as a film sanity check (2025)
- [[Volatile Splash Receivers vs Metronome Consistency]] — Metronome-average vs high-variance splash receivers; both get called 'functional', only one is startable as a No. 2
- [[Alpha Receiver vs Committee Pass Catchers]] — Buffalo as the live test: Harmon wants an ace above the committee, Koh says no-No.1 is un-guardable
- [[Tight End as Number One Read]] — Why a TE almost never holds the first read in a concept — the talent gap has to be enormous
- [[Coaching Talent Elevation]] — Waldman: judge a returning coordinator by the role that earned him the promotion, not by his failed head-coaching stint
- [[Rushing Ecosystem and Running Back Weaponization]] — Weapon-back thesis — slot-capable RBs create spacing and neuter blitzes without necessarily gaining targets; Angelo's pyramid, Waldman's fantasy caveat
- [[Shanahan System Fit and Quarterback Empowerment]] — Shanahan-tree offenses raise the floor but may cap an elite QB; Harmon's Goff-to-Stafford template applied to Stroud
- [[Draft Round and Rookie Running Back Touch Share]] — Angelo's 2019-24 charting: rookie touches/game by round — 18/12/10/7; why late-round backs need weak competition
- [[Contact Mitigation and Dictating Contact]] — Waldman/Angelo: elite backs dictate and relax into contact rather than absorb it — the durability trait
- [[Number One Receiver Slot Snap Allocation]] — Harmon's benchmark: even dominant Xs take 20-25% slot snaps; single digits signals wasted alignment
- [[Lid Lifter Receivers and Space Creation]] — Raiders case: outside receivers chosen for vertical function to open interior space for slot types
- [[Paying the Quarterback and Roster Construction]] — Eagles' title with Hurts at $51M refutes the 'can't pay the QB' excuse — Harmon's roster-building lesson
- [[Prospect Model Grade vs Rank]] — Grade beats rank across years; McFarland's supermodel inputs, thresholds and correlations alongside Waldman's film scale
- [[Neurologic Recovery and Movement Inventory]] — Angelo: post-surgery recovery is neurologic, not structural — a repair severs decades of accumulated movement inventory
- [[Offensive Line Investment and Skill Player Value]] — Concept — offensive line spending as a gate on skill-player outcomes; Waldman's Seattle case study (2025)
- [[Tight End Prototype Grind Risk]] — Waldman: the TE prototype is near-mythical; receiver-first TEs last longer, and prototype usage grinds 2025's class to dust
- [[Linear Athletes and Non-Linear Skill Demands]] — Waldman's evaluation trap: straight-line athletes flatter on tape but fail the non-linear releases, breaks and blocking a TE actually needs
- [[X Receiver Scarcity in the Modern NFL]] — Why true X receivers vanished — rising pass volume demands separators, pushing old contested-catch X types inside
- [[Wide Receiver Class Success Baseline]] — Waldman's baseline: ~4.5 receivers per class reach 3+ years of starter production; draft the position every year
- [[Having Skills vs Being Skilled]] — Waldman: rising technical baseline swells the middle tiers — prospects have skills without being skilled; 38 graded 80+ in 2025
- [[Whiteboard Players]] — Waldman archetype: perfect when the play matches the drawing, short-circuits when it doesn't; rarely a long-term starter
- [[Claypool-Galladay Production Privilege]] — Waldman: big athletic WRs inherit mismatches beside established teammates; production fades once defenses key on them
- [[Power Slot Receiver Archetype]] — Harmon uses St. Brown to argue the power slot label is a starting condition, not a ceiling — man and press marks can be built
- [[RSP Quarterback Charting Methodology]] — Waldman's RSP QB charting: throw-point distance bands, Next Gen Stats accuracy thresholds, pinpoint vs general accuracy over box score
- [[Prospect Age and the Raw Label]] — Waldman on why prospect age models are ham-handed, and why 'raw' as inexperienced differs from 'raw' as unskilled
- [[Scouting Sizzle Reels and Front Office Override]] — Concept — Waldman estimates GMs override scouts off highlight reels ~20-30% of the time, owners ~30-35%.
- [[Pre-Draft Misinformation Season]] — Concept — Waldman: ~1% of pre-draft reporting comes true; he avoids it deliberately, mines storylines only.
- [[Elijah Moore Rule]] — Concept — small boundary receivers get open but rarely get the throw; Harmon's rule, named for Elijah Moore
- [[Manufactured Touches vs Natural Separation]] — Manufactured screen volume from a boundary alignment strands a receiver without blockers — Harmon's 2024 D.J. Moore case study
- [[Quarterback Height and Pocket Sight Lines]] — Kinnan's height-purist case: only one sub-6'1" NFL starter; Brees cited as survivorship bias, Murray/Wilson as the cost
- [[Existing Roster Talent and Prospect Opportunity]] — Depth-chart talent as the overlooked input to a scouting grade; Waldman adding it to the RSP grading key
- [[Draft Capital Removal Model Delta]] — Rank gap between draft-capital and no-draft-capital models as an overvaluation flag; ~40 spots is the danger band
- [[Player Family Interference and Draft Risk]] — Why teams discount prospects with disruptive or celebrity parents; Waldman's frame for the Shedeur Sanders slide
- [[Rookie Pick Accumulation and Trading Out]] — Dynasty strategy — Waldman: trade out of the last three rookie rounds; picks don't get hurt, but he admits not doing it himself
- [[Tight End as X Receiver Experiment]] — Why teams announcing a tight end at X receiver keeps failing — Pitts, Kincaid, Arroyo; Harmon's diminishing-returns case
- [[Year Two Value and Vacating Veterans]] — Rookie-draft strategy: buy year-two breakouts at year-one prices when the veteran ahead of them is aging out or leaving
- [[Usage as Evidence of Ability]] — Waldman's counter to 'usage reveals inability': absent route usage can be a scheme, protection or QB artifact, not a skill verdict
- [[Embracing Variance and Directional Correctness]] — Zachariason's core process: aim to be directionally right within a range of outcomes, not precise; edge is liking a player above consensus
- [[Ambiguous Backfields and Market Risk Aversion]] — Waldman: committees get mispriced by narrative — late signings, injury history, phantom moves; name the draft slot, not the projection
- [[Running Back Position Health and Scoring Regression]] — 2024's top-24 RBs were the healthiest in ~15 years, inflating RB2 scoring; Zachariason expects a 2025 ADP overcorrection
- [[Condensed Formations and Blurred Slot-Outside Lines]] — Shanahan/McVay condensed formations blur slot vs outside roles, making alignment labels weak evidence for receiver projection
- [[Off-Script Play Creation and Pocket Climbing]] — Waldman: leaving the pocket wastes blockers and timing; QBs who can't climb cap their pass catchers
- [[Rising Receiver Skill Baseline and Analyst Granularity]] — Waldman: 7-on-7 and private coaching raised receiver technique baseline, compressing the middle and forcing finer tiering
- [[Second-Round Rookie Guarantee Holdouts]] — 2025 leaguewide second-round holdout over full guarantees; hosts blame teams, flag rookie WR rep loss
- [[Value-Based Drafting and Early Tight End Cost]] — Harris's VBD case against first-three-round tight ends: 4 of 24 beat ADP in a decade, never from round one
- [[Late-Round Quarterback and Positional Flattening]] — Flattened QB tier makes QB7-in-round-six indefensible; Kluge drafts two late QBs, Harris waits but rosters only one
- [[Players Not Positions]] — Harris's draft principle: build one blended player list and take names, not positional permutations
- [[Draft Capital Rep Allocation Bias]] — Sunk-cost bias in camp rep allocation — draft capital buys reps and forgiveness; UDFAs get three reps and one mistake
- [[Rookie On-Ramp and Development Runway]] — Rookie deployment as a highway on-ramp — Mahomes behind Alex Smith vs. Richardson thrown into traffic; be patient early
- [[Positional Versatility and Roster Redundancy]] — Rosters balance versatility against redundancy — deliberate Venn-diagram overlap in every room, and it all reduces to coach trust
- [[Speed of Instinct and Overthinking]] — Camp arc for young players — isolated-skill flashes early, then added layers force thinking and cost speed of instinct
- [[Playing Experience and Evaluation Blind Spots]] — Having played a position doesn't guarantee you can evaluate it — Waldman's post office vs FedEx analogy for former-player analysts
- [[High Floor Picks and Draft Risk Balancing]] — Draft strategy — using high-floor mid-round picks to counterbalance earlier upside swings; safety can be illusory
- [[Contract Holdout Slow Starts]] — Harmon: post-holdout receivers start slow — Lamb and Aiyuk target-rate and yardage drops
- [[Automated Draft Grades and Default Rank Conformity]] — Platform draft grades only measure conformity to default ranks; both hosts dismiss them entirely
- [[Category One and Category Two Knowledge]] — Harris's split: Category 1 is what we know, Category 2 is the unknowable we guess at and watch
- [[Legendary Upside and ADP's Repeating Mistakes]] — Why ADP repeats errors: best-case narratives ('legendary upside') on rookies, TE1 and QB1, like betting the over
- [[Stacking Elite Teammates and Portfolio Diversification]] — Two elite teammates is fine in a good offense (both can score on one drive), risky in a bad one
- [[Auction Nomination Strategy]] — Nominate players you don't want, drain homers' budgets early, hold cash until the room tips
- [[Sequencing Bias and the Random Walk]] — Harstad via Waldman: order of good/bad weeks is mostly noise; ADP beats results through ~week four
- [[Optimal Fumble Rate]] — Harstad via Waldman: zero fumbles means insufficient aggression; worry only on a cluster of ball-security signals
- [[Retread Head Coaches and Culture Building]] — Harstad/Waldman: rehiring proven coaches is the league's best hack; culture outlasts scheme novelty
- [[Clearly Defined Roles vs Do-Everything Personnel]] — Payton-style narrow roles vs Belichick do-everything players; Waldman says defined roles are easier to draft
- [[Aging Quarterback Down Years and Rebounds]] — Harstad: QB cliff is partly selection bias — down years often rebound if the player doesn't retire first
- [[Jones Fracture Receiver Recovery Outcomes]] — Jones fracture in receivers: 'pain issue' framing is misleading; mixed recovery precedents, playing through it rarely pays
- [[Draft Capital Zombies and Non-Linear Prospect Outcomes]] — Draft capital is an indicator, not a linear ranking — but it does show what a staff wants to work
- [[Run-Pass Mix as a Lazy Fade Argument]] — Harris: run-pass-mix, depth-chart and coaching fades are usually laziness; the passing game sustains unless its parts stink

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
