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
- [[Jake Browning]] — QB, CIN — starting again with Burrow out; INT-prone, Harris says the whole Bengals operation downticks (2025 takes)
- [[Baker Mayfield]] — QB, TB — Harris would take him over Maye, Dak and Love for one game; still doubts the fantasy ceiling
- [[Justin Fields]] — QB, NYJ — Waldman sees a Kordell Stewart career arc; expects backup or out, not another starting shot (2025 takes)
- [[Derek Carr]] — QB, NO — retired May 2025; Waldman saw it coming after the Shough pick (2025 takes)
- [[Justin Herbert]] — QB, LAC — QB3/QB4 but both tackles gone; Harris fears a fall outside the top ten and won't trade for him (2025 takes, stale)
- [[Russell Wilson]] — QB, NYG — Harmon calls the 450-yard Cowboys game a mirage; limited menu capping Nabers (2025 takes)
- [[C.J. Stroud]] — QB, HOU — concussed Week 9; without him Harris will not start any Houston skill player (2025 takes)
- [[Jared Goff]] — QB, DET — Zachariason's headline fade at ~QB8 as the pocket-passer trap; Waldman: good NFL QB, bad fantasy price (2025 takes)
- [[Lamar Jackson]] — QB, BAL — hamstring exit vs KC, may sit before the Week 7 bye; Eisenberg still starts him if active
- [[Patrick Mahomes]] — QB, KC — QB2 through five weeks on rushing and air-yards volume; both hosts hold, guest projects top-three finish
- [[Jalen Hurts]] — QB, PHI — Harris: not aggressive enough as a thrower; defenses sit in zone and crash his rollout side (2025 takes)
- [[Brock Purdy]] — QB, SF — Harris says not a QB1 right now; accuracy off and line collapsing (2025 takes)
- [[Kyler Murray]] — QB, ARI — on IR with foot injury (4+ games); Harmon says scheme misfit, same player as his rookie self
- [[Drew Lock]] — QB, NYG — takes over from Daniel Jones; film-based arm talent, historically boosts WR/TE production (2024 takes, stale)
- [[Gardner Minshew]] — QB, LV — Waldman buying: reads, anticipation, mid-season rapport with Adams and Bowers (2024 takes, stale)
- [[Anthony Richardson]] — QB, IND — lost job to Daniel Jones; Harris says his 2024 top-50 ADP was dreadful analysis (2025 takes, stale)
- [[Joe Flacco]] — QB, CIN — Harris's most pivotal player: not a start, but the Atlas propping up Chase, Brown and Higgins (2025 takes, stale)
- [[Jordan Love]] — QB, GB — hesitant, in-his-own-head after LaFleur's patience message; 0-0 half vs PHI (2025 takes)
- [[Dak Prescott]] — QB, DAL — Harris outside top 12 on 2024 offensive evidence; flags he could be wrong (2025 takes)
- [[Bryce Young]] — QB, CAR — Waldman defends him: resilient, processing showing up; roster and scheme are the problem (2025 takes)
- [[Michael Penix Jr.]] — QB, ATL — see-it-throw-it per Koh; efficiency tracks London's target share, struggles vs man coverage
- [[Tua Tagovailoa]] — QB, MIA — Harris's worst QB performance of W1 (2 INTs, a fumble); Miami blown out, he retracts his own take (2025)
- [[Drake Maye]] — QB, NE — Waldman: leap already made; judicious with ball, elite under pressure, placement still short of Burrow (2025 takes)
- [[Bo Nix]] — QB, DEN — QB8 but Harris pumps the brakes: eight three-and-outs, defense-carried team, deep-ball recklessness (2025 takes, stale)
- [[Caleb Williams]] — QB, CHI — Waldman: underrated cornerstone; air raid to Ben Johnson transition explains the acclimation mistakes
- [[Jayden Daniels]] — QB, WAS — third injury of 2025, a severe elbow injury sustained down 31 on SNF (2025 takes)
- [[J.J. McCarthy]] — QB, MIN — Harmon says play him out to learn if he can play; Jefferson under 55 yards/game with him (2025 takes)
- [[Spencer Rattler]] — QB, NO — Waldman: real journeyman-backup promise, climbs pocket, beats blitzes; not the reason NO lost (2025 takes)
- [[Tanner Mordecai]] — QB, Wisconsin prospect (SMU/Oklahoma transfer) — rocky transfer-year tape, rebounded late vs. LSU; Waldman's grade is future backup of value, not a starter *(2024 pre-draft takes, stale)*
- [[Jack Plummer]] — QB, Louisville prospect — accuracy is the whole story per Waldman: "if he had the accuracy, he would probably be a top-five quarterback in this class" *(2024 pre-draft takes, stale)*
- [[Joe Milton III]] — QB, DAL — Waldman/Kluge both sour: big arm, no touch or processing; superflex emergency only (2025 takes)
- [[Desmond Ridder]] — QB, ARI — traded from Atlanta for Rondale Moore after Falcons signed Kirk Cousins
- [[Kirk Cousins]] — QB, ATL — Waldman buys the velocity return a year post-Achilles; questions his leadership but rates him above Garoppolo
- [[Daniel Jones]] — QB, IND — Waldman: not a Darnold-style leap, a good thrower propped up by play action; folds under pressure
- [[Ryan Tannehill]] — QB, TEN — speculative Pittsburgh reunion with former OC Arthur Smith; projected as a Joe-Flacco-style veteran room presence, not a starter bet *(2024 takes, stale)*
- [[Aaron Rodgers]] — QB, PIT — Harris: a retirement-inducing game; Eisenberg says only good matchups now (2025 wk10)
- [[Matthew Stafford]] — QB, LAR — Waldman: the reason LAR is competitive; 'Mahomes 1.0' pocket reset, whole passing game leans on him (2025)
- [[Joe Burrow]] — QB, CIN — Wk2 toe injury, surgery with three-month recovery; Browning takes over (2025 takes)
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
- [[Jacoby Brissett]] — QB, ARI — Harris says the Cowboys game was the outlier; expect this version, not a real upgrade
- [[Will Levis]] — QB, TEN — Waldman 2025: 'fuck it,' processing is the real flaw; mechanics work treats symptoms, No. 1 pick looms
- [[Sam Darnold]] — QB, SEA — 21/24, 330, 4 TD on SNF; Koh publicly drops his skepticism, Harmon credits Kubiak/JSN fit
- [[Sam Howell]] — QB, SEA — backup-level and a bad fit behind a leaky line; 22% sack rate in relief (2024 takes, stale)
- [[Aidan O'Connell]] — QB, LV — Harmon would start him over Minshew; Raiders projected last in pass attempts (2024 takes, stale)
- [[Geno Smith]] — QB, LV — three interceptions vs CHI; Harris says the picks triggered conservative Carroll play calling
- [[Zach Wilson]] — QB, NYJ — Waldman: Baker-Mayfield-style redemption in range if he matures; could be out of league in years
- [[Josh Allen]] — QB, BUF — most talented QB in the league but chasing hero throws; 9-for-30 vs HOU (2024 takes, stale)
- [[Trevor Lawrence]] — QB, JAX — Waldman/Angelo: not the vertical thrower Coen bet on; offense being retooled underneath (2025 takes)
- [[Trey Lance]] — QB, LAC — Waldman a deep dynasty stash; sharp preseason, no pressure, first stable org and QB coach to learn under
- [[Malik Willis]] — QB, GB — Angelo says most GMs would now take him over Will Levis; self-awareness cited as the turn (2024 takes, stale)
- [[Jameis Winston]] — QB, NYG — named starter over Dart; Harmon calls him a fantasy 'pump and dump' with no worthwhile targets (2025 takes)
- [[Jake Haener]] — QB, NO — Waldman: better than Rattler now; startable-at-times backup who feeds Olave safely (2024)
- [[Hendon Hooker]] — QB, DET — Waldman near-out; backup ceiling, Josh Dobbs career path projected (2024 takes, stale)
- [[Tyson Bagent]] — QB, CHI — Waldman sees a real future and trade value; top QB waiver watch-list name behind Williams (2024 takes, stale)
- [[Cam Ward]] — QB, TEN — Harstad prefers proven vets over Ward in a rebuild; hasn't cleared the can-he-play filter (2025 take)
- [[Darian Mensah]] — QB, Tulane — aggressive downfield passer with elite ball placement; expected power-four transfer (2024 devy takes, stale)
- [[Skylar Thompson]] — QB, PIT — backup; Waldman says Miami governed his aggression, Kansas State tape more downfield (2025 takes)
- [[Carson Beck]] — QB, Georgia — Waldman's QB1 still; buying the dip after 3-INT Texas game, blames lost Bowers/McConkey (2024 takes, stale)
- [[Jalen Milroe]] — QB, SEA — Waldman: no takeover in 2025 barring injury; expect red zone packages and garbage-time flashes only (2025 takes)
- [[Andy Dalton]] — QB, CAR — replaced Bryce Young and revived the offense; Harmon's veteran-in-a-two-high-league archetype (2024 takes, stale)
- [[Marcus Mariota]] — QB, WAS — Harris's Week 11 streamer vs MIA on rushing floor; Funston prefers Geno Smith
- [[Aidan Chiles]] — QB, Michigan State — dual-threat under Jonathan Smith; Waldman's preseason downgrade was situation-based, Marsh fixes it (2024 takes, stale)
- [[Tommy DeVito]] — QB, NYG — named starter over Drew Lock; anticipatory thrower, Rich Gannon-esque, limited vertically (2024 takes, stale)
- [[Shedeur Sanders]] — QB, CLE — Waldman's QB3/4 with borderline-starter grade; young Kirk Cousins comp; expected to start at some point in 2025 (2025 takes)
- [[Will Howard]] — QB, PIT — Kinnan (guest): Mason Rudolph comp not Josh Allen; Jekyll-and-Hyde playoff sample, average velocity, high-floor backup
- [[Kyle McCord]] — QB, Syracuse (2025 pre-draft) — doubles down on bad leverage reads; higher starter ceiling than Brosmer, far lower floor
- [[Jackson Dart]] — QB, NYG — exceeded rookie expectations but taking dangerous punishment; Daboll fired, next scheme fit uncertain (2025 takes)
- [[Tyler Shough]] — QB, NO — impressive first extended look; arm, on-time processing, pocket climbing; Harmon prefers him to Rattler (2025 takes)
- [[Kurtis Rourke]] — QB, SF — Waldman likes the Shanahan/Lynch endorsement, but he's a redshirt bridge-QB stash only in very deep leagues
- [[Dillon Gabriel]] — QB, CLE — Harris: looks very small, worse than Wentz that day; would prep Shedeur Sanders to start (2025)
- [[Max Brosmer]] — QB, MIN — fundamentally sound stash; Waldman's same-zip-code-as-Purdy comp, a two-QB/dynasty watch behind McCarthy
- [[Quinn Ewers]] — QB, MIA — Kinnan (guest) would not draft him: three injuries in three years, lost drive, checks down in a QB-friendly Sark scheme
- [[Seth Henigan]] — QB, Memphis (2025 pre-draft) — big-play arm range and good pressure escapes; placement under duress and leverage reads lag
- [[Hunter Dekkers]] — QB, FA — off-RSP late add; Waldman grades him ~QB7-10 of 12, one-step-forward/two-back (2025 pre-draft)
- [[Riley Leonard]] — QB, IND — 6th-round rookie; RP charting shows slants/curls strong, digs poor; dark-horse starter if Richardson lingers
- [[LaNorris Sellers]] — QB, South Carolina — Angelo's 2026 QB1; Roethlisberger-level sack avoidance, elite read-option, would want him to sit a year
- [[Cade Klubnik]] — QB, Clemson — Angelo's 2026 QB2; a Jared Goff comp with more athleticism and a very catchable ball at all three levels
- [[John Mateer]] — QB, Oklahoma — Angelo's 2026 QB sleeper, found via Kyle Williams tape at Washington State; better ball carrier than expected
- [[Jimmy Garoppolo]] — QB, LAR — Stafford's backup; anticipatory thrower but self-destructs under pressure, a Derek Carr comp per Waldman
- [[Mac Jones]] — QB, SF — playing well on a cheap two-year deal; hosts see him as a bridge-starter fit for several teams (2025 takes)
- [[Davis Mills]] — QB, HOU — Waldman: bright spots, no special trait; profiles as a journeyman starter, possible 49ers backup fit

### Running Backs
- [[Christian McCaffrey]] — RB, SF — Waldman keeps redraft edge over Bijan despite fumble/drops; dynasty edge goes to Bijan
- [[Bijan Robinson]] — RB, ATL — goal-line vulture panic debunked by snap counts; still 23-13 red zone edge (2025 wk10)
- [[Jahmyr Gibbs]] — RB, DET — Angelo buy-low: tape unchanged, hurt by injured O-line and Morton dropping the option-route usage (2025)
- [[James Cook]] — RB, BUF — Doherty bust pick on 47.7% snaps and touchdown regression; Harris more in, citing low stuffed-run rate (2025 takes)
- [[Tyler Goodson]] — RB, IND — Waldman getting off the train; still likes the versatility but not the Indianapolis situation (2024 takes, stale)
- [[Trey Sermon]] — RB, IND — competent one-week fill-in, nothing beyond it; Howard/Williams comp *(2023 takes, stale)*
- [[Devin Singletary]] — RB, NYG — Harris's Week 10 flex pick over Tracy; goal-line and blocking snaps post-Skattebo (2025 in-season take)
- [[Saquon Barkley]] — RB, PHI — Harris: Eagles offense not the same, three-and-outs and abandoned run; may not be lucrative to hold Eagles in 2H
- [[Derrick Henry]] — RB, BAL — Waldman flex-only w/o Lamar; Harris RB19 (2025 in-season take, stale)
- [[Joe Mixon]] — RB, HOU — reportedly 'not close' to returning; may miss the season (2025 takes)
- [[Alvin Kamara]] — RB, NO — biggest workload in a month, 100+ scrimmage yards; Harris wants one repeat first (2025 wk10)
- [[Breece Hall]] — RB, NYJ — six 10+ yard carries; Harris: the only thing that works on a bad Jets offense (2025 takes)
- [[Nick Chubb]] — RB, HOU — role collapsed to ~10 snaps; clearly behind Woody Marks as of Week 11 (2025 takes)
- [[David Montgomery]] — RB, DET — Waldman calls RB24 price a value; 16 PPG in games played, still in prime (2025 takes)
- [[Isiah Pacheco]] — RB, KC — only 28-23 snap edge on Hunt, who owned third down and short yardage; Harris calls the role not great
- [[Kyren Williams]] — RB, LAR — still the lead back, but Waldman sees a slow drift toward committee as Corum earns work (2025 takes)
- [[Kenneth Walker III]] — RB, SEA — Harris says he and Charbonnet are used near-interchangeably; big ranking gaps are wrong
- [[Raheem Mostert]] — RB, LV — Waldman buys a real split behind Jeanty; Harris doesn't believe Carroll. Both like RB69 price (2025 takes)
- [[James Connor]] — RB, ARI — both hosts hanging on for 2024; "toast" skepticism reframed as a second-contract finance story, not a talent decline; Michael Carter cuts into but doesn't replace him *(2024 takes, stale)*
- [[Aaron Jones]] — RB, MIN — clear lead and passing-downs back at 44 snaps; back-end RB2 (2025 wk10)
- [[Zamir White]] — RB, LV — Koh doubts he fits Chip Kelly's scheme; possible cap/roster casualty (2025 takes, stale)
- [[Tank Bigsby]] — RB, PHI — traded from JAX to Philadelphia; now Saquon Barkley's closest handcuff, trade bait in deep leagues (2025)
- [[Kendre Miller]] — RB, NO — top-five Week 6 waiver add on rising usage, but Harris says he has not displaced Kamara (2025 takes)
- [[Chase Brown]] — RB, CIN — Harstad's 2025 paper-value miss; market cooled after a high preseason trade value (2025 take)
- [[Tony Pollard]] — RB, TEN — held the starting role; Harris calls the Spears takeover exaggerated, Doherty less sure (2025 takes)
- [[Michael Carter]] — RB, ARI — confirmed lead back with Conner out for the year and Benson scoped; the shallow-league add over Gainwell (2025 takes)
- [[Austin Ekeler]] — RB, WAS — torn Achilles Week 2 2025, season over; backfield opens for Croskey-Merritt (2025 takes)
- [[Josh Jacobs]] — RB, GB — two TDs in 40-40 tie but late shin/knee look and no OT snaps; bye Week 5 (2025 takes)
- [[Najee Harris]] — RB, LAC — ruptured Achilles Week 3 2025, out for the season; backfield ceded to Omarion Hampton (2025 takes, stale)
- [[Jaylen Warren]] — RB, PIT — surprise Week 4 inactive after warming up; Harris expects him back after the Week 5 bye (2025 takes)
- [[Jordan Mason]] — RB, MIN — demoted to pure handcuff behind Jones (2025 wk10 take)
- [[Elijah Mitchell]] — RB, KC — Harris' top-ranked KC backup by default, but he is wavering toward Brashard Smith; no 2024 tape at all (2025 takes)
- [[Tyler Allgeier]] — RB, ATL — top Week 11 add; flex-viable behind Bijan, ~1/3 of carries in a run-heavy plan
- [[Blake Corum]] — RB, LAR — Waldman's handcuff of record over Jarquez Hunter if Kyren Williams misses time; pass pro needs work
- [[De'Von Achane]] — RB, MIA — receiving role exploded; on pace for ~970 receiving yards as Miami plays to Tua's quick game (2025)
- [[Braelon Allen]] — RB, NYJ — Montgomery-style role but weaker line/QB; RB3/RB4 value, Waldman buys around RB44-40 (2025)
- [[Jonathan Brooks]] — RB, CAR — Waldman's former class RB1; now cited as the paper-value trap that Dowdle's role exposed
- [[Blake Watson]] — RB, DEN — deepest sleeper in the Denver room; best receiving back there if Harvey stumbles under Payton (2025 takes)
- [[Jabari Small]] — RB, Tennessee prospect — Shrine Game name Waldman likes; undersized (205 lbs) but runs hard with good vision and decision-making *(2024 pre-draft takes, stale)*
- [[Ray Davis]] — RB, BUF — Harris's underpriced 12th-13th round Cook handcuff; power plus surprising one-foot cutting
- [[Dylan Laube]] — RB, LV — late-round stab/waiver target; pass-catching plus better inside running than reputation (2024 takes, stale)
- [[Daijun Edwards]] — RB, Georgia prospect — quick and shifty despite playing through an MCL injury, good pass catcher/blocker; Jalen-Richard floor, dynamic-James-White ceiling; likely the most-rostered of Waldman's three underrated 2024 RBs on name value alone *(2024 pre-draft takes, stale)*
- [[George Holani]] — RB, SEA — beat out Martinez; Walker-style scat back with special-teams value (2025 takes)
- [[Deshaun Fenwick]] — RB, Oregon State prospect — Shrine Game favorite; Leonard-Fournette-adjacent big-back build, gap-scheme thumper, projects as a reserve "B-back" *(2024 pre-draft takes, stale)*
- [[Brian Robinson Jr.]] — RB, SF — named the handcuff of all handcuffs after McCaffrey's calf strain; priority add if free (2025 takes, stale)
- [[Tyjae Spears]] — RB, TEN — Harris's number five Week 4 add as a pure RB stash behind Pollard (2025 in-season, stale)
- [[Mario Anderson]] — RB, LAR — UDFA bowling-ball who fits McVay's type; deep-roster stash only (2025 take)
- [[Cody Schrader]] — RB, Missouri prospect — Angelo's late-round pick to make a roster and stick; 1,800 total yards/14 TDs at Missouri, Senior Bowl standout, graded a smart, reliable long-term role player rather than a star *(2024 pre-draft takes, stale)*
- [[Kendall Milton]] — RB, Georgia prospect — unique size/speed at 6'1"/220-225; hasn't yet shown the Eddie-George-level ceiling his HS recruiting profile promised; combine/pro day season is the swing factor for his stock *(2024 pre-draft takes, stale)*
- [[Kimani Vidal]] — RB, LAC — mid-tier RB2 holding the job until Hampton returns; line-dependent (2025 wk10)
- [[Will Shipley]] — RB, PHI — rotated in first series then left with a rib injury; Harris says Barkley has no rosterable handcuff yet (2025 takes, stale)
- [[Rasheen Ali]] — RB, Marshall prospect — explosive pre-ACL flash back who returned to the same level; graded the best RB at the 2024 Senior Bowl for his limited reps there; ball security is the swing risk *(2024 pre-draft takes, stale)*
- [[Jaylen Wright]] — RB, MIA — healthy but zero offensive snaps; Harris calls his summer hype absolutely wrong (2025 in-season, stale)
- [[Dillon Johnson]] — RB, Washington prospect — Waldman's fourth early-round-talent name; played through multiple injuries into the national title game, some of the best contact balance in the class, but a real breakaway-speed/explosiveness ceiling concern *(2024 pre-draft takes, stale)*
- [[Trey Benson]] — RB, ARI — on IR after meniscus scope, 4-6 weeks; Harris says gone for most of the fantasy regular season (2025 takes)
- [[Bucky Irving]] — RB, TB — foot/shoulder injury with no information from Tampa; Harris RB rank 65, league-winner-or-nothing (2025 takes, stale)
- [[Marshawn Lloyd]] — RB, GB — Waldman expects GB RB2; game-breaker in the crease but decision-making and ball security are the gates (2025 takes)
- [[Khalil Herbert]] — RB, CHI (likely cut) — Waldman: top-5 waiver-wire stash if he lands in a backfield with need
- [[Roschon Johnson]] — RB, CHI — holds goal-line work, but Waldman sees Monangai's pass-pro trust squeezing him out (2025 take)
- [[Javonte Williams]] — RB, DAL — Waldman: low-end RB1, scheme-and-health dependent bruiser; ranked above where he sees him
- [[Samaje Perine]] — RB, CIN — ankle injury on a kick return; opens a Tahj Brooks window behind Chase Brown
- [[Rachaad White]] — RB, TB — Waldman: underrated, better than priors suggest, real NFL starter case; fantasy value ends when Irving returns (2025)
- [[DeAndre Swift]] — RB, CHI — into a near-even committee with Monangai; Angelo doubts he is a Bear in 2026 (2025 takes)
- [[Alexander Mattison]] — RB, LV — Signs as Zamir White's backup; Waldman defends his zero-TD 2023 as a Minnesota QB/red-zone issue, not a talent flaw.
- [[Zach Moss]] — RB, CIN — ceding lead work to Chase Brown; Waldman keeps him as a good secondary back, 8-12 touches (2024 takes, stale)
- [[Aidan Robbins]] — RB, BYU (2024 prospect) — Waldman: strong downhill gap runner, needs to press deeper to fit zone schemes too
- [[Audric Estime]] — RB, DEN — Waldman: 'slightly plus Samaje Perine', good creases, likely committee not every-down (2024 takes, stale)
- [[Isaac Guerendo]] — RB, SF — pushed out of the CMC handcuff role by the Brian Robinson Jr. trade (2025 takes)
- [[Isaiah Davis]] — RB, South Dakota State (2024 prospect) — Waldman: strong man-coverage route runner, needs more decisive vision as a runner
- [[Jalen White]] — RB, Georgia Southern (2024 prospect) — Waldman: solid short-yardage gap runner, decision-making/leverage reads are the issue
- [[Jase McClellan]] — RB, Alabama (2024 prospect) — Waldman: sharp cutter, a competent runner; unclear if that means a competent NFL starter
- [[Montrell Johnson]] — RB, FA — Waldman: underrated speed, outside-zone upside, post-draft waiver name (2025 pre-draft take, stale)
- [[Tyrone Tracy Jr.]] — RB, NYG — 46-24 snap edge but goal line goes to Singletary; flex only with Wilson at QB (2025 wk10)
- [[Miyan Williams]] — RB, Ohio State (2024 prospect) — Waldman: smart, physical; ceiling of a Peyton-Barber-type committee back
- [[Frank Gore Jr.]] — RB, Southern Miss (2024 prospect) — Waldman: smart cutback runner, must prove he can transcend size like Devin Singletary
- [[Emani Bailey]] — RB, TCU (2024 prospect) — Waldman: inconsistent gap reads, too tight or too wide; needs better control/vision
- [[Dylan McDuffie]] — RB, Kansas (2024 prospect) — Waldman: willing tight-crease runner, Raheem-Mostert-lite burst without the blink-of-an-eye separation
- [[Michael Wiley]] — RB, Arizona (2024 prospect) — Waldman: needs better leverage attacking defenders, same early issue Jahmyr Gibbs had
- [[Gus Edwards]] — RB, LAC — last in league YPC after a top-10 all-time career mark; Harstad calls it noise, not decline (2024 takes, stale)
- [[Travis Etienne Jr.]] — RB, JAX — Harris says he's back on film, running downhill; holding off Tuten/Allen, start him
- [[J.K. Dobbins]] — RB, DEN — Harris holds firm (would take him over Pickens); guest shopping him on injury history, Harvey now seen as 60/40
- [[Chuba Hubbard]] — RB, CAR — demoted behind Dowdle; Week 9 snaps were injury-driven, not role-driven (2025 takes)
- [[Miles Sanders]] — RB, CAR — Angelo blames poor Panthers infrastructure/ownership, not talent loss, for his decline
- [[Dylan Johnson]] — RB, TEN UDFA — Waldman's other favorite; projects as low-red-zone role Titans currently lack
- [[Eric Gray]] — RB, NYG — new page; Waldman has Gray 60/40 over Tyrone Tracy Jr. for the complementary role behind Singletary
- [[Dameon Pierce]] — RB, HOU — new page; Waldman: starter role over, misused as a non-receiving back despite receiving ability at Florida
- [[Deuce Vaughn]] — RB, DAL — not viewed as a 2024 fantasy factor; buried behind Elliott/Dowdle regardless of role changes
- [[Justin Strong]] — RB, IND (UDFA) — tryout with Colts; Waldman flags burst/vision but wants a deep-league watch, not a draft pick
- [[Zach Charbonnet]] — RB, SEA — foot injury, no practice in week 3; Walker back as lead if he sits
- [[Cordarrelle Patterson]] — RB/KR, PIT — Harstad: greatest returner ever, records set in the era most hostile to returns
- [[Leonard Fournette]] — RB, FA — Waldman: monitor-only 'next Latavius Murray' type until there's a real, proven role
- [[Ashton Jeanty]] — RB, LV — Harris film study: good not transcendent; over-patient, compact; Ray Rice/D'Angelo Williams comps; unearned first-round ADP (2025 takes)
- [[Trevor Etienne]] — RB, 2025 prospect — 'lunch pail' back; adequate everywhere, spot-start/tertiary projection per Angelo (2025 pre-draft takes, stale)
- [[Ollie Gordon II]] — RB, MIA — power/goal-line role behind Achane; top-two Week 4 waiver add for Harris, fifth for Fish (2025, stale)
- [[Jaleel McLaughlin]] — RB, DEN — Waldman's favorite Denver back at an RB50 price; Payton receiving-back archetype (2024 takes, stale)
- [[Clyde Edwards-Helaire]] — RB, KC — on NFI list to open 2024, out four games; no fantasy path offered (2024 takes, stale)
- [[Deneric Prince]] — RB, KC — camp first-team reps not an endorsement; monitor only, roster risk (2024 takes, stale)
- [[Justice Hill]] — RB, BAL — Waldman's preferred late Derrick Henry handcuff; some standalone TD value (2025 takes)
- [[A.J. Dillon]] — RB, PHI — Waldman: real closeout/short-yardage threat to Shipley behind Barkley, badly underrated (2025 takes)
- [[Christopher Brooks]] — RB, GB — Waldman: no standalone role behind Jacobs, but likely lead back if Jacobs misses time (2024 takes, stale)
- [[Sione Vaki]] — RB, DET — Waldman: cheap luxury-spot stash behind Gibbs after Montgomery MCL injury (2024 takes, stale)
- [[Jordan Lyle]] — RB, Miami — Angelo devy watch: Gibbs-like HS tape, late-1st/early-2nd upside, small frame (~185 lbs)
- [[Kyle Monangai]] — RB, CHI — earned committee role; Angelo sees the David Montgomery TD role, Waldman says RB3/4 price with RB1 upside (2025)
- [[Jacory Croskey-Merritt]] — RB, WAS — snap-count lead was garbage time; Harris says avoid as a flex (2025 takes)
- [[Carson Steele]] — RB, KC — dropped to third up after a fumble; Waldman cites weak pass-pro and pass-catching (2024 takes, stale)
- [[Rico Dowdle]] — RB, CAR — late-blooming volume back; four years and a Hubbard injury to get a role, now the anti-paper-value case study
- [[Ezekiel Elliott]] — RB, DAL — late-round shot; elite short-yardage and pass pro, limited fantasy upside (2024 takes, stale)
- [[Dalvin Cook]] — RB, DAL — fallback committee piece only; Harris sees a Fournette-style dead end (2024 takes, stale)
- [[Sean Tucker]] — RB, TB — Waldman: NFL starter talent, cutback runner with open-field burst; sees a committee lead role coming
- [[Nicholas Singleton]] — RB, Penn State — 220 lbs and fast, good gap runner; outside zone needs work (2026 class, early look)
- [[Dean Connors]] — RB, Rice — Waldman: Ekeler/Swift-lineage receiving back, situational upside, well below class headliners (2024 takes, stale)
- [[Sire Gaines]] — RB, Boise State — 6-0/209 true freshman behind Jeanty; projected 2025 lead back (2024 devy takes, stale)
- [[Tahj Brooks]] — RB, CIN — Harris super-deep sleeper; the Chase Brown contingency after Moss's neck injury (2025 takes, stale)
- [[Keaontay Ingram]] — RB, KC — buried depth piece; Waldman sees Kareem Hunt style but questions dedication and opportunity (2024 takes, stale)
- [[Kalel Mullings]] — RB, Michigan — 2024 riser over Donovan Edwards; ex-LB downhill runner, day-three projection between Jordan Howard and Hassan Haskins (2024 takes, stale)
- [[Donovan Edwards]] — RB, 2025 prospect — Waldman still sees untapped gap-scheme upside after market soured (2025 pre-draft takes, stale)
- [[Nate Frazier]] — RB, Georgia — true freshman, Sharpe's pick as a future national-name back (2024 takes, stale)
- [[Quinshon Judkins]] — RB, CLE — Waldman: RB1 talent on a non-RB1 team; not an RB1 this season, someday if Browns improve (2025 takes)
- [[Kareem Hunt]] — RB, KC — Week 1 third-down and short-yardage back over Pacheco; Harris rates the role above the player
- [[Jonathan Taylor]] — RB, IND — Harris: must-start weekly, the engine of Indy's offense alongside Tyler Warren (2025 in-season takes)
- [[Isaac Brown]] — RB, Louisville — Waldman prefers him to Bucky Irving; creative but disciplined, Clinton Portis flashes (eligibility unclear)
- [[Rhamondre Stevenson]] — RB, NE — toe injury, no practice, possibly long-term; backfield trending to TreVeyon Henderson (2025 takes, stale)
- [[Jerome Ford]] — RB, CLE — squeezed out by Judkins's return per Waldman/Bob Harris; Sampson keeps the change-up role
- [[Sincere McCormick]] — RB, LV — Angelo and Waldman both see a real starter; gap-scheme fit, contact balance, deep RB class the risk (2024 takes, stale)
- [[Cam Skattebo]] — RB, NYG — Waldman: fun, smart runner, TD-driven RB1 spike weeks, but pass pro worries and not a league winner (2025)
- [[Ameer Abdullah]] — RB, LV — Waldman's case study in journeyman labeling; versatile with contact balance but not a startable fantasy back (2024 takes)
- [[TreVeyon Henderson]] — RB, NE — gap-scheme guided missile; boom-bust 'slot machine' role, startable with Stevenson out (2025 takes)
- [[Omarion Hampton]] — RB, LAC — on IR with an ankle injury, out at least four weeks; his absence drove the Week 6 waiver run (2025 takes)
- [[Kaleb Johnson]] — RB, PIT — out of the doghouse but Waldman caps 2025 expectations; next year is the window [Dynasty]
- [[Brashard Smith]] — RB, KC — leaked 'more involved' role with Pacheco struggling and Hunt cooked; Harris a speculative add (2025)
- [[LeQuint Allen]] — RB, JAX — 1% rostered; Harris's No. 5 waiver add as possible third-down back behind Etienne (2025 takes)
- [[Jaydon Blue]] — RB, DAL — healthy scratch Week 1; Harris calls the camp hype generic, third on the depth chart (2025 takes, stale)
- [[Woody Marks]] — RB, HOU — lead back over Chubb; RB24 since Week 6, 18-22 touch upside, flex-plus (2025 takes)
- [[Devin Neal]] — RB, NO — Waldman: gap-scheme toss usage leaves him unproven; Bilal Powell utility outcome, not a Kamara heir (2025 takes)
- [[Jarquez Hunter]] — RB, LAR — camp-hype favorite behind Kyren Williams, but gap-scheme background may cost him early zone reps (2025 takes)
- [[Damien Martinez]] — RB, SEA — practice squad; Waldman keeps him as a deep-league dynasty stash behind Walker
- [[Phil Mafah]] — RB, FA — Waldman: overlooked between-tackles banger, Gus Edwards floor, Day 3 roster-maker (2025 pre-draft take, stale)
- [[Jordan James]] — RB, SF — 49ers depth-chart flyer; broken finger and Guerendo's return stalled the momentum (2025 takes, stale)
- [[RJ Harvey]] — RB, DEN — Harris sees no elusiveness; lost early-down work to J.K. Dobbins in Week 3 2025 (2025 takes, stale)
- [[Dylan Sampson]] — RB, CLE — 20 touches in W1 debut, quick but small; Ciely prefers him to Judkins, Harris prefers Judkins (2025)
- [[Marcus Yarns]] — RB, FA — Waldman's most intriguing 2025 back; electric space player, needs 200 lbs for a complement role (2025 pre-draft)
- [[Bhayshul Tuten]] — RB, JAX — better inside runner than Etienne but Waldman sees too few touches to take over in 2025
- [[Lan Larison]] — RB, NE — Koh's deep sleeper: elite hands, possible Woodhead-style hybrid pass-catching role (untracked co-host take)
- [[James Conner]] — RB, ARI — broken ankle Week 3 2025, believed out for the year; Trey Benson inherits (2025 takes, stale)
- [[Kaytron Allen]] — RB, Penn State — interior tough-yards back, no Singleton speed; coaches always find a use (2026 class, early look)
- [[DeMond Claiborne]] — RB, Wake Forest — Waldman's early 2026 standout; good feet and windback vision, no breakaway speed, weight the question
- [[Noah Whittington]] — RB, Oregon — Hatman's under-the-radar 2026 name; flashed behind better players, injury history (untracked-guest take)
- [[DJ Giddens]] — RB, IND — Ciely's Jonathan Taylor handcuff at RB55; Montgomery comp, Addai as the lofty ceiling (2025 takes, stale)
- [[Keaton Mitchell]] — RB, BAL — Harris super-deep sleeper 3rd straight year; healthy, big-play threat, but pass-pro gap behind Justice Hill (2025 takes)
- [[Chris Rodriguez Jr.]] — RB, WAS — was the actual starter vs DET (17 first-half snaps) but hurt a shoulder; wait on news
- [[MarShawn Lloyd]] — RB, GB — on IR after two camp injuries; Harris writes him off as a 2025 contributor (2025 takes)
- [[Kenneth Gainwell]] — RB, PIT — Waldman: smart, singles-hitter, ~600-800 yards; Angelo sees possible 50/50 split with Warren post-bye (2025)
- [[Isaiah Pacheco]] — RB, KC — Waldman: no better than post-injury late 2024; camp hype unmatched on tape; OL is the real problem
- [[Jeremy McNichols]] — RB, WAS — third-down back (7 of 10 third-down snaps); both hosts say don't chase the long touchdown (2025, stale)
- [[Emari Demercado]] — RB, ARI — touch lead over Knight in a committee; Harris has no conviction either way, bad matchup vs Seattle (2025 take)
- [[Antonio Gibson]] — RB, NE — knee injury on a kick return vs BUF; Harris expects a long absence (2025 takes)
- [[Hassan Haskins]] — RB, LAC — No. 2 Week 6 waiver add behind Vidal after Hampton's IR; trust and physicality, no passing-down role (2025)
- [[Zonovan Knight]] — RB, ARI — Harris's slight Week 10 nod over Demercado on goal-line and two-minute work, low conviction (2025 take)

### Wide Receivers
- [[Justin Jefferson]] — WR, MIN — elite talent capped by McCarthy: 42% catchable target rate Week 10, headed for a disappointing season (2025 takes)
- [[Ja'Marr Chase]] — WR, CIN — Waldman sees Burrow's absence as raising, not lowering, his ceiling
- [[Keenan Allen]] — WR, LAC — thriving vs zone on one-on-ones off McConkey's coverage draw; Harmon didn't see it coming
- [[Amon-Ra St. Brown]] — WR, DET — Harmon's strongest conviction play: over 1,075.5 yards, projects 1,231; man/press marks improve yearly, now 51% outside
- [[Jameson Williams]] — WR, DET — WR18 since Week 6 on Campbell play-calling; near-WR2, start weekly but still feast-or-famine (2025 takes)
- [[Brandon Aiyuk]] — WR, SF — starts 2025 on PUP recovering from ACL; slower track than Diggs (2025 takes)
- [[Tee Higgins]] — WR, CIN — big day cut short by a possible head injury; status unresolved at recording (2025 takes)
- [[Jordan Addison]] — WR, MIN — benched a quarter in London for missing a walkthrough; GW TD bailed managers out (2025 takes)
- [[Jayden Reed]] — WR, GB — elite per-route efficiency but chronically underplayed; his absence has flattened the Packers passing game (2025 takes)
- [[Noah Brown]] — WR, WAS — surprise Houston cut, signed by Washington; competent system depth pushed out by roster crowding (2024 takes, stale)
- [[John Metchie III]] — WR, HOU — Harmon sells the breakout (slot-only role player); Koh buys on vacant slot role (2024 takes, stale)
- [[Xavier Hutchinson]] — WR, HOU — dirty-work flanker ahead of the rookies to open 2025; Allen Lazard comp, low ceiling (2025 takes)
- [[Tre Tucker]] — WR, LV — every-down X on speed; 100% route participation, 85% out wide, but a supporting piece to Bowers
- [[Treylon Burks]] — WR, TEN — Waldman says sell/cut in dynasty: catch-point and zone issues, ~10 targets projected, may not last the year
- [[DeAndre Hopkins]] — WR, BAL — Waldman contrarian garbage-time start; Harris says low routes, don't (2025)
- [[Adam Thielen]] — WR, MIN — Harmon: effectively a paid retirement at 35, a 'ghost'; the Carolina trade aged well for Carolina (2025 takes)
- [[Deebo Samuel]] — WR, WAS — resurgent as a 64%-slot zone beater under Kingsbury; PPR WR7 through Week 5 (2025 takes)
- [[Malik Nabers]] — WR, NYG — torn ACL Week 4 2025, out for season; Harmon's irreplaceable full-field WR1 (2025 takes)
- [[Marvin Harrison Jr.]] — WR, ARI — out weeks with appendicitis; Harmon flags mental side plus poor Murray fit as ongoing drags (2025 takes)
- [[Rome Odunze]] — WR, CHI — bounce-back after a zero; Eisenberg says buy the panic sell (2025 wk10 take)
- [[Keon Coleman]] — WR, BUF — Waldman: no Bills 1,000-yard receiver; Brady's open-man design caps him despite the talent (2025 takes)
- [[Ainias Smith]] — WR, PHI — slow camp start, Johnny Wilson ahead; Waldman says he needs a year or two (2024 takes, stale)
- [[Michael Gallup]] — WR, WAS — un-retired; former true X (95% outside 2020) Harmon sees as a longshot perimeter fit for Daniels (2025 takes)
- [[Brian Thomas Jr.]] — WR, JAX — route-tree limits over the middle plus availability issues; bounce-back is an open question (2025 takes)
- [[Ladd McConkey]] — WR, LAC — WR7 since Week 4; Waldman calls the prodigy skepticism dead, though target share still an open book
- [[Ricky Pearsall]] — WR, SF — knee still keeping him from practice; Harris ranks him ~73 as a lottery ticket, McCormick a believer (2025 takes, stale)
- [[Troy Franklin]] — WR, DEN — now the target leader at 81% routes, but Harmon calls him a complementary piece with weak efficiency (2025 takes)
- [[CeeDee Lamb]] — WR, DAL — high ankle sprain, multi-week absence; the move-around zone beater Dallas cannot replace (2025 takes)
- [[Tyreek Hill]] — WR, MIA — dislocated knee Week 4, out for the season (2025 in-season takes)
- [[Mike Evans]] — WR, TB — hamstring pull late in Week 3, exited and did not return; timeline unknown (2025 in-season, stale)
- [[Rashid Shaheed]] — WR, SEA — Harmon says the quiet debut was game script; expects a bigger role, likely not full-time (2025 takes)
- [[Jerry Jeudy]] — WR, CLE — first TD of 2025 on 12 targets; Harris wants a repeat vs BAL before buying
- [[Courtland Sutton]] — WR, DEN — lost the target lead to Franklin; good-not-great X, 71% man beater, weak vs zone, slowing (2025 takes)
- [[Chris Godwin]] — WR, TB — fibula injury again, out Week 6; Harris fears a long-term recurrence of last season's break
- [[Rashad Bateman]] — WR, BAL — Harmon bold call: outproduces Zay Flowers; Baltimore's best press-coverage WR (2025)
- [[Stefon Diggs]] — WR, NE — post-ACL role finally unlocked; 146-yd revenge game on sub-50% snaps, still capped (2025 takes)
- [[Cooper Kupp]] — WR, SEA — hamstring/heel, possible multi-week; not impactful (one 60-yard game), Shaheed trade may signal fading standing
- [[Quentin Johnston]] — WR, LAC — Harmon reverses: 'QJ is legit,' developed into a real starter, squeezing McConkey (2025 takes)
- [[Jaxon Smith-Njigba]] — WR, SEA — Harmon's fully graduated elite receiver; leads NFL in receiving yards per game (2025 takes)
- [[Zay Flowers]] — WR, BAL — buy-the-dip after Detroit dud; Josh believes the tier, Harris more shaken
- [[Puka Nacua]] — WR, LAR — Waldman: top-3-5 fantasy WR in McVay's scheme, but a zone-beater, not a Chase-class route runner (2025)
- [[Tank Dell]] — WR, HOU — injury: multi-injury ACL rehab, Bob Harris says a year away; Kirk added ahead of him (2025 take)
- [[Nico Collins]] — WR, HOU — Waldman: top-8-12 when healthy but a year-to-year injury tease, not a durable cornerstone
- [[Josh Downs]] — WR, IND — Harmon loves the player but 12 personnel with Tyler Warren caps his snaps and receptions (2025 take)
- [[Marvin Mims Jr.]] — WR, DEN — Harris and Daigle would drop him for Troy Franklin; Payton clearly does not see him as the guy (2025 takes)
- [[Jalen Hyatt]] — WR, NYG — boom/bust deep threat; needs a Wan'Dale Robinson injury to matter (2025 takes)
- [[Rashee Rice]] — WR, KC — big-slot YAC bully, but Harmon flags real ramp-up risk after a year away (2025 in-season take)
- [[Davante Adams]] — WR, LAR — non-contact lower-back exit in Week 10; Harris flags real concern (2025 wk10)
- [[Gabe Davis]] — WR, BUF — reunion practice-squad signing; Harmon: nothing burger, sacrificial-X depth only (2025)
- [[Khalil Shakir]] — WR, BUF — Waldman: close to but short of 1,000 yards; Brady's spread design, not a talent issue (2025 takes)
- [[Drake London]] — WR, ATL — Angelo: potential top-five WR, 10+ targets a game; Penix fade game may have unlocked him (2025)
- [[Michael Wilson]] — WR, ARI — deep sleeper with Harrison and Jones out; Pittman-axis middle-of-field big receiver (2025 takes)
- [[George Pickens]] — WR, DAL — Harris ~WR50 and an active sell (Lamb returning, character risk); guest holds, sees WR12 upside
- [[Diontae Johnson]] — WR, FA — cut by Cleveland; Harmon thinks his career is over, biggest bag fumble
- [[Tyler Lockett]] — WR, LV — Koh expects veteran-deference snaps post-Meyers; Harmon says not needle-moving for years, 28% route rate
- [[Terry McLaurin]] — WR, WAS — week to week with a high quad injury, no surgery yet; specialist visit raises concern
- [[Wan'Dale Robinson]] — WR, NYG — Harris WR34, Bell WR32; volume-by-default with Nabers out but Giants may not throw 20 times
- [[Ronnie Bell]] — WR, SF — a name to know mostly for injury-contingency reasons behind Aiyuk/Deebo, not his own emergence *(2024 takes, stale)*
- [[Dontayvion Wicks]] — WR, GB — separates but hands graded D in Harris's Almanac; drops make him unplayable (2025 takes)
- [[Romeo Doubs]] — WR, GB — Waldman: now GB's best WR, catch-point issues fixed; possible emergence as a top-tier WR (2025 takes)
- [[Christian Watson]] — WR, GB — Harris's repeat No. 2 waiver add; big-play emergency starter, preferred to Horton for Week 10 (2025 takes)
- [[Cedric Tillman]] — WR, CLE — hamstring injury Week 4, reportedly out multiple weeks (2025 takes)
- [[Tyler Scott]] — WR, CHI — "overrated on speed" pre-draft per Waldman; used as a one-dimensional RPO/deep-shot option, a Darnell-Mooney-before-he-developed comp *(2024 takes, stale)*
- [[Jonathan Mingo]] — WR, DAL — Harmon questions whether he makes the roster; power-slot-only path blocked by Lamb, athletic traits under-delivered
- [[Demario Douglas]] — WR, NE — Harris retracts him as the Diggs-injury fill-in; out-snapped by Kyle Williams (2025 wk10)
- [[Malik Washington]] — WR, MIA — Waldman: talent underused, McDaniel conservative with young players; role capped behind Waddle/Waller (2025)
- [[Xavier Legette]] — WR, CAR — Waldman calls him a bust: good athlete, slow processor, too many loose threads in his game (2025 takes)
- [[Malachi Corley]] — WR, FA — cut by Jets; Harmon calls the third-round pick an antiquated gadget mistake
- [[Javon Baker]] — WR, NE — ~40 rookie routes, unchartable; developmental one-side prospect with maturity flags (2025 takes)
- [[Roman Wilson]] — WR, PIT — healthy reset year after lost rookie season; Funston's #3 waiver flier behind Metcalf (2025)
- [[Devontez Walker]] — WR, BAL — total project per Harmon; elite athlete, no consistent college separation (2024 takes, stale)
- [[Brendan Rice]] — WR, LAC — 7th-rounder w/ elite in-breaking numbers, poor vertical/ball-tracking; deep sleeper per Matt Harmon
- [[J. Michael Sturdivant]] — WR, UCLA prospect (Cal transfer) — 6'3"/205, high-end traits that "didn't really emerge at the highest level" of production per Waldman; declared, ungraded *(2024 pre-draft takes, stale)*
- [[Marquise Brown]] — WR, KC — 61% route share but Harmon sees little pop left; intermediate-only zone beater (2025 in-season take)
- [[Skyy Moore]] — WR, KC — Harmon calls his outside-receiver usage a "mis-evaluation" of the player; doesn't expect him in Kansas City's plans and would rather see him traded to restart elsewhere *(2024 takes, stale)*
- [[A.J. Brown]] — WR, PHI — publicly unhappy, 83% outside alignment, not separating; Harmon says he is no longer the peak player (2025 takes)
- [[DeMarcus Robinson]] — WR, LAR — Rams' only real vertical/outside option post-Nacua; 75% outside, top aDOT on team (2024 takes, stale)
- [[Jahan Dotson]] — WR, PHI — led Eagles in yards Week 1 on 15 routes; Harmon sees a real third-option role behind Brown/Smith (2025)
- [[Adonai Mitchell]] — WR, NYJ — traded from IND; Harmon wants pure X only (87% vs press, awful vs zone), very wide range of outcomes
- [[Xavier Worthy]] — WR, KC — Harris walks back his top-10 Week 4 rank after ankle limits and decoy usage; no must-start Chief but Mahomes/Kelce (2025 takes)
- [[Ja'Lynn Polk]] — WR, NE — Harmon calls him a miss; miscast at X, may not make roster (2025 preseason take)
- [[Michael Pittman Jr.]] — WR, IND — losing primary-read work to Pierce; two-catch game (2025 wk10 take)
- [[D.J. Moore]] — WR, CHI — bypassed by Odunze's second-year leap; Harmon floats him as a veteran trade candidate (2025)
- [[Calvin Ridley]] — WR, TEN — droppable in many leagues; drops, chemistry and possible effort issues with Ward
- [[Mike Williams]] — WR, LAC — retired after eight seasons; Harmon says he was underrated as a separator, not just a contested-catch guy (2025 take)
- [[Tyler Harrell]] — WR, deep sleeper (Miami) — Waldman: elite play speed, 'as fast as Xavier Worthy' but unproven, injury-plagued (2024 prospect, stale)
- [[Amari Cooper]] — WR, LV — retired 2025-09-04 after a ten-day Raiders return; leaves LV's receiver room unappealing (2025 takes, stale)
- [[Elijah Moore]] — WR, BUF — roster-bubble opening from injuries; Harmon says best separator and man-beater of the Bills group
- [[Christian Kirk]] — WR, HOU — out Week 1 with a pulled hamstring, possibly longer; Harris says don't chase the replacements yet (2025 takes, stale)
- [[Darnell Mooney]] — WR, ATL — hamstring plus staff friction; Harmon writes him off as a role player behind London (2025)
- [[Anthony Gould]] — WR, Oregon State (2024 prospect) — Waldman: sub-package contributor early, needs man-coverage refinement to start
- [[Bub Means]] — WR, NO — rookie depth athlete, 4.43/39.5-inch; zone-better, poor start-stop (2024 takes, stale)
- [[Jalen McMillan]] — WR, TB — to IR, possibly out past week nine; Harmon grades him a very good WR3, not a WR2 (2025)
- [[Jermaine Burton]] — WR, CIN — Harmon liked the talent, distrusts the annual good-summer reports; bar is just making the roster (2025 takes)
- [[Johnny Wilson]] — WR, PHI — inside track to WR3; Harmon's charting says true outside X, 71.4% vs man, bad contested hands (2024 takes, stale)
- [[Joshua Cephus]] — WR, UTSA (2024 prospect) — Waldman: slippery zone/YAC weapon, needs man skills to start outside
- [[Kobe Hudson]] — WR, UCF (2024 prospect) — Waldman: deep-threat sub-package piece, could grow into starting outside option
- [[Luke McCaffrey]] — WR, WAS — startable only while McLaurin and Brown are out; keeps a small role after
- [[Ryan Flournoy]] — WR, Southeast Missouri State (2024 prospect) — Waldman: NFL athlete, contributor-vs-reserve hinges on releases/breaks
- [[Xavier Weaver]] — WR, Colorado (2024 prospect) — Waldman: Jordan Addison starter kit, route game a starting-caliber foundation
- [[Michael Thomas]] — WR, FA — suspended one game; Waldman expects a signing by mid-October, a waiver stash not a draft pick (2024 takes, stale)
- [[Curtis Samuel]] — WR, BUF — Harmon: KC game showed real outside role, health finally better, but snap path unclear (2024 takes, stale)
- [[Rondale Moore]] — WR, ATL — Harmon: 'not a real receiver,' pure gadget/motion piece after trade for Desmond Ridder
- [[Garrett Wilson]] — WR, NYJ — re-injured knee vs CLE, ruled out and expected to miss 2-3 more weeks
- [[Odell Beckham Jr.]] — WR — cut from Harmon's dynasty rankings entirely; he considers the career over (2025 takes)
- [[Xavier Gipson]] — WR, NYJ — Harmon 'really intrigued,' thinks he can play; eyed for bigger slot role in 2024
- [[Greg Dortch]] — WR, ARI -- Harmon/Koh's sleeper pick of a bad Cardinals room; 2024 charting subject
- [[Darius Slayton]] — WR, NYG — Koh sees a Winston-driven target bump; Harmon expects empty volume and low catch rate (2025 takes)
- [[Zay Jones]] — WR, ARI — likely WR3 above Dortch but Waldman sees only 300-400 yards; Kyler cap (2025 takes)
- [[Josh Palmer]] — WR, BUF — repeat Harris super-deep sleeper; Allen upgrade and outside role, but 26 and never cracked the Chargers lineup (2025 takes)
- [[Allen Lazard]] — WR, NYJ — Harmon: without Rodgers he is a non-NFL player; effort and production both cited
- [[D.J. Chark]] — WR, unsigned FA (Apr 2024) — Harmon: can't get open anymore, sold on Cowboys link (stale)
- [[Hunter Renfrow]] — WR, CAR — Harris: two-TD day as Carolina's WR3; tough to chase but a fine swap for Legette (2025 in-season)
- [[Tyler Boyd]] — WR, CIN — Harmon: overrated, declining, outside experiment doesn't work; open to Steelers fit (2024, stale)
- [[Marquez Valdes-Scantling]] — WR, SEA — signed as the sacrificial X; 23.8 YPR in NO, 'diet Coke Alec Pierce' per Harmon
- [[DeVonta Smith]] — WR, PHI — ascended past A.J. Brown; 2.2+ YPRR and Harmon's read is top-ten NFL receiver level (2025 takes)
- [[Kayshon Boutte]] — WR, NE — grade one hamstring sprain, may return in a week; volatile vertical-X role per Harmon
- [[Jalen Coker]] — WR, CAR — Angelo's lower-tier buy as he returns to health and defenses key on Dowdle (2025 takes)
- [[Trey Palmer]] — WR, TB — new page; Waldman sees real 2023 development but reads TB's McMillan draft capital as a downgrade signal
- [[Chase Claypool]] — WR, BUF — new page; Waldman rates the signing a camp-body injury hedge, below MVS/Chark on the depth chart
- [[Kadarius Toney]] — WR, FA — cut by KC and unsigned; Harmon says he never had real route-running traits, net negative in 2023 (2024 takes, stale)
- [[Jalen Tolbert]] — WR, DAL — Harmon's 'fine, not special' third receiver; sacrificial-X space-clearer with Marvin Jones jack-of-all-trades comp
- [[Chris Olave]] — WR, NO — second in NFL targets; big downfield game with Shough, answered contested-catch critics (2025 takes)
- [[A.T. Perry]] — WR, NO — boundary X with press/contested-catch chops; Van Jefferson 2021 as best case (2024 takes, stale)
- [[Aeneas Smith]] — WR, PHI — Harmon deep sleeper; projected as Eagles' full-speed motion piece for new OC Kellen Moore's scheme
- [[Calvin Austin III]] — WR, PIT — Waldman: weekly starter as WR2; Rodgers back-shoulder connection and schemed backfield usage
- [[Denzel Mims]] — WR, PIT — buy-low sleeper for the open WR2 job opposite Pickens; Waldman buys the food-poisoning excuse for his lost Jets year
- [[DK Metcalf]] — WR, PIT — only usable Steelers pass catcher, and only in games where the script forces them to throw (2025 takes)
- [[Brandin Cooks]] — WR, NO — sacrificial X: zero targets on 22 routes despite 49% snaps; not startable in this offense (2025 takes)
- [[Andrei Iosivas]] — WR, CIN — Waldman dynasty buy: up to ~220 lbs, year-over-year gains; needs a Higgins or Burton opening. (2025 takes)
- [[Charlie Jones]] — WR, CIN — Waldman/Angelo watchlist name for Tyler Boyd's vacated slot role; Purdue product.
- [[Casey Washington]] — WR, ATL — Waldman: reliable third-down target in Week 1, but Mooney's return likely reclaims the role
- [[Parker Washington]] — WR, JAX — likeable but miscast as a vertical outside option; profiles as a third/rotational receiver (2025 takes)
- [[Jaylen Waddle]] — WR, MIA — post-Hill breakout: 2.9 YPRR, top-five efficiency; Harmon says he was always this good, circumstance changed
- [[Kendrick Bourne]] — WR, SF — Waldman: the answer in the SF passing game while Mac Jones plays; role shrinks when Jennings/Pearsall return (2025)
- [[Alec Pierce]] — WR, IND — Harris's WR add of the week for Week 11, ahead of Tez Johnson
- [[Van Jefferson]] — WR, PIT — Waldman: Jefferson's a cheap stopgap, not a real answer, until Roman Wilson is ready
- [[Jordan Whittington]] — WR, LAR — big slot, possible Kupp-lite long-term; Koh sees no fantasy meat on the bone behind Nacua/Adams
- [[Josh Reynolds]] — WR, DEN — Harmon's bet for Broncos' second-most productive receiver on known-quantity grounds (2024 takes, stale)
- [[Jakobi Meyers]] — WR, JAX — traded from LV; Harris rates him plug-and-play and better than Washington but ranks him behind for Week 10
- [[Olamide Zaccheaus]] — WR, CHI — Waldman likes a late stab; converted-RB slot/YAC fit for Ben Johnson while Burden is brought along
- [[Jalen Nailor]] — WR, MIN — camp speedster, near-lock WR3 role; waiver watch list, not draftable (2024 takes, stale)
- [[JuJu Smith-Schuster]] — WR, KC — team-high 82.9% route share but Harmon sees a replacement-level veteran holding the slot (2025 take)
- [[Tim Patrick]] — WR, DET — Harmon's favorite for WR2 during the Jameson Williams suspension; chain-moving big body (2024 takes, stale)
- [[Tyquan Thornton]] — WR, KC — Harris' No. 3 Week 6 waiver add despite thinking he 'stinks'; window closes when Rashee Rice returns Week 7
- [[Dyami Brown]] — WR, JAX — sacrificial X/vertical role that frees BTJ and Hunter inside; 18 screens caught in 2024
- [[Tez Johnson]] — WR, TB — 4 TDs in 5 games with Evans/Godwin out; Harris calls the production partly lucky
- [[Tyler Johnson]] — WR, LAR — surprise Week 1 YAC flash post-Nacua; Harmon calls possible one-week flash given zero camp buzz (2024 takes, stale)
- [[Jeremiah Smith]] — WR, Ohio State — highest-rated WR recruit ever; leading OSU in receiving as an 18-year-old (2024 devy takes, stale)
- [[Ryan Williams]] — WR, Alabama — 17-year-old reclassified freshman leading Alabama in receiving; top devy stash (2024 takes, stale)
- [[KaVontae Turpin]] — WR, DAL — primary slot with Lamb out (~85% inside); Harmon comps him to a target-earning Tutu Atwell
- [[Jauan Jennings]] — WR, SF — talent of a mid-WR2 but ranked ~WR35 on health, snap-share and Mac Jones ceiling concerns (2025)
- [[Mack Hollins]] — WR, NE — placeholder X starter; snaps likely, targets not (2025 take)
- [[Travis Hunter]] — WR/CB, JAX — season ended by LCL surgery; 2026 role and deployment now an open question (2025 takes)
- [[Devaughn Vele]] — WR, NO — post-Shaheed-trade snap leader in the Saints WR room (86.6%), routes leader; production still Olave's (2025 takes)
- [[Sterling Shepard]] — WR, TB — one-week streamer only if both Evans and Godwin are out (2025 in-season, stale)
- [[Tutu Atwell]] — WR, LAR — $10M going-rate WR3; Harmon calls him hyper-singular speed, wants an upgrade behind Adams/Nacua
- [[Nick Marsh]] — WR, Michigan State — big boundary freshman, 3rd among FR in yards; Waldman says scoop him in C2C (2024 takes, stale)
- [[Nick Westbrook-Ikhine]] — WR, MIA — Harmon floats him as Miami's sacrificial on-line X in 3WR sets, freeing Waddle role catering
- [[Rakim Jarrett]] — WR, TB — Waldman: 'Stefon Diggs starter kit'; watch-list add on a high-scoring offense (2024 takes, stale)
- [[DJ Moore]] — WR, CHI — Waldman: drifting toward a mini-Deebo manufactured-touch role as Burden takes downfield work (2025 takes)
- [[David Moore]] — WR, CAR — Wk12 team leader in targets/routes/yards, but Harmon sees a depth piece once Coker returns
- [[Savion Williams]] — WR, GB — Waldman's dynasty sleeper; better hands/YAC than Johnston, could take the Deebo-style role (2025)
- [[Tetairoa McMillan]] — WR, CAR — 5-60 and still the Panthers' guy; broadcast-sourced hamstring watch (2025 wk10)
- [[Nick Nash]] — WR prospect, San Jose State — Waldman intrigued but not in love; timed speed decides his ceiling
- [[Jacob Cowing]] — WR, SF — 67 rookie routes and mostly special teams; getting some Deebo-style jet-sweep work in OTAs
- [[Luther Burden III]] — WR, CHI — Waldman dynasty buy: YAC machine with Kupp-drill conviction; path to snaps if D.J. Moore's shoulder lingers (2025 takes)
- [[Matthew Golden]] — WR, GB — disappointing rookie tape in isolation; hosts blame scattered alignment usage, not the talent (2025 takes)
- [[Jalen Royals]] — WR, KC — four routes in Week 4; Rice-shaded slot profile but buried in the rotation (2025 in-season take)
- [[Andrew Armstrong]] — WR, MIA — undrafted Arkansas SEC receiving leader; Harmon day-two grade, decent X profile, 25-year-old rookie
- [[Konata Mumpfield]] — WR, LAR — 7th-round rookie on Harris's super-deep list; quick release, phone-booth quickness, roster spot not assured (2025 takes)
- [[Isaiah Bond]] — WR, CLE — 57% snaps and team-high 7 targets with Tillman on IR; speed in-breaker, character flags (2025 takes)
- [[LaJohntay Wester]] — WR prospect, Colorado — Angelo's second-tier route runner and returner; 170-lb frame, combine matters
- [[Emeka Egbuka]] — WR, TB — Godwin's fibula re-injury solidifies his role; Harris now agrees with Behrens to hold rather than sell high
- [[Tre Harris]] — WR, LAC — Keenan Allen signing squeezes him; Harmon wants him at X (Alec Pierce type), team sees a Josh Palmer flanker (2025 takes)
- [[Jayden Higgins]] — WR, HOU — rookie: only 11 routes Week 1, behind Hutchinson and Watson; staff not trusting rookies yet (2025)
- [[Xavier Restrepo]] — WR, TEN — UDFA slot/zone-beater with Cam Ward chemistry; Harmon bets he outsnaps a drafted Titans rookie
- [[Justin Watson]] — WR, HOU — Harmon's archetypal sacrificial X: routes on 58.4% of dropbacks, targeted on only 8% of them
- [[Daniel Jackson]] — WR, FA — grittiest pass catcher in Waldman's 2025 class; quick slot, preferred over Restrepo (2025 pre-draft)
- [[Tai Felton]] — WR, MIN — deep dart throw; Harmon likes his underneath/YAC profile as the Rondale Moore replacement, no downfield game
- [[Kyren Lacy]] — WR, FA — Waldman: capable possession type, Noah Brown ceiling; not an outside starter unless razor sharp (2025 pre-draft take)
- [[Elic Ayomanor]] — WR, TEN — 2-18; Harris' bye-week-emergency question answered with a 'resounding no' (2025 takes)
- [[Jaylin Noel]] — WR, HOU — rookie: 11 routes Week 1, buried behind Hutchinson and Watson in Houston's pecking order (2025)
- [[Jack Bech]] — WR, LV — Harmon says he should inherit Meyers' big-slot role; zero offensive snaps last week clouds it
- [[Dont'e Thornton Jr.]] — WR, LV — raw rookie miscast as full-time X; Harmon says he isn't getting open, wants Bech instead
- [[Isaiah Neyor]] — WR, SF — Waldman: nearly a top-10 board receiver but for ungraded YAC reps; deep dynasty stash, starter upside in 1-2 years (2025 takes)
- [[Arian Smith]] — WR prospect (UGA) — Waldman: 4.4 sleeper with correctable drops (unlike Tai Felton); return-man floor.
- [[Jaylin Lane]] — WR, WAS — deep dynasty stash flag from Harris; rookie flashes, no defined role (2025 takes)
- [[Ja'Corey Brooks]] — WR, FA — Waldman: elite release-to-catch-point tape, scared hands; top-7 board player if fixed (2025 pre-draft take, stale)
- [[Isaac TeSlaa]] — WR, DET — snap share up to 34% with Raymond out; Harmon sees Detroit's big-bodied X developing (2025 takes)
- [[Kelly Akharaiyi]] — WR, FA — Waldman's lone-wolf 2025 sleeper: route running and ball tracking, but likely UDFA (2025 pre-draft, stale)
- [[Bru McCoy]] — WR, FA — 6-3/230 Tennessee sleeper; young JuJu/Hakeem Nicks comp, well-rounded eventual starter (2025 pre-draft)
- [[Julio Jones]] — WR, retired — Harmon's Hall-of-Fame retrospective; 2016 as apex, 86.2% vs zone as Shanahan's X (2025 takes)
- [[Kyle Williams]] — WR, NE — elite speed (21.7 mph, 9th fastest); Waldman says catch technique is the only thing between him and the WR2 role
- [[Tory Horton]] — WR, SEA — Shaheed trade caps him; Harmon sees best on-ball role but expects Shaheed to out-snap him
- [[Jacolby George]] — WR, FA — Waldman: Miami slot/flanker, Travis Benjamin floor to Jordan Addison ceiling (2025 pre-draft take, stale)
- [[Xavier Guillory]] — WR, FA — Waldman: physical blocker/special-teamer, Hines Ward-coached, bye-week waiver gem upside (2025 pre-draft take, stale)
- [[Jordan Moore]] — WR, FA — Waldman: YAC slot with drop problem; 'what people wrongly thought Shakir was' (2025 pre-draft take, stale)
- [[Chimere Dike]] — WR, TEN — gadgety slot move-around type; Koh's favorite of the flawed Titans supporting cast
- [[Pat Bryant]] — WR, DEN — carving out a big-slot role at 79% inside, though still only a ~20% snap share (2025 takes)
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
- [[T.J. Hockenson]] — TE, MIN — top-12 by default only; check-down volume, Harris fine with dropping him for a hot streamer (2025)
- [[Travis Kelce]] — TE, KC — drafted as a top-12 TE but Gretch calls him pretty washed on tape; startable alternatives exist (2025 takes)
- [[Sam LaPorta]] — TE, DET — first-read share crashed 19.9% to 8.6% behind Jameson Williams; Harmon expects reversion (2024 takes, stale)
- [[Dalton Kincaid]] — TE, BUF — hamstring injury exited Week 10; Harris shelves him near-term (2025 wk10)
- [[Luke Musgrave]] — TE, GB — top waiver add on Kraft's season-ending ACL; blocking gap means rotation, not a clean role inheritance
- [[Tucker Kraft]] — TE, GB — torn ACL Week 9, out for the year; Harris valued him as a blocking-first three-down TE, not an elite athlete
- [[Brevyn Spann-Ford]] — TE, Minnesota prospect — 6'7"/270; looked lost as a blocker in 2022, visibly figured out technique by late 2023 per Waldman; projects as a practice-squad/depth-TE NFL path *(2024 pre-draft takes, stale)*
- [[Kyle Pitts]] — TE, ATL — Waldman sees Atlanta finally targeting him downfield; contract clock may end the fit anyway (2025 takes)
- [[Pat Freiermuth]] — TE, PIT — Waldman expects a target uptick; Rodgers' goal-line lean
- [[Brycen Hopkins]] — TE, LAR — pending free agent, promising but flawed (RAC ability, athletic, but poor blocker with drop issues); Dustin Keller comp; deep-league stash or wait-and-see, not a lead-role bet *(2024 takes, stale)*
- [[Brock Bowers]] — TE, LV — Harstad's cornerstone: WR who plays TE, Kittle tier, five years of flat-value elite production
- [[George Kittle]] — TE, SF — IR a month with hamstring; Harris buys only very cheap (2025 in-season takes, stale)
- [[David Njoku]] — TE, CLE — out-produced 7-63 to 3-37 by rookie Fannin in W1; Harris calls it a blow to his fantasy case (2025)
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
- [[Theo Johnson]] — TE, NYG — Harmon's most interesting Giants pass catcher under Winston (2025 takes)
- [[Tip Reiman]] — TE, Illinois (2024 prospect) — Waldman: in-line starter athleticism, lacks route craft/guile
- [[Trey Knox]] — TE, South Carolina (2024 prospect) — Waldman: oversized-RB-type YAC role, likely special-teamer/utility target
- [[Zach Hines]] — TE, South Dakota State (2024 prospect) — Waldman: must become a very good in-line blocker to stick in NFL
- [[Dalton Schultz]] — TE, HOU — solid redraft role even as Stroud/Diggs trade drives his price down
- [[Isaiah Likely]] — TE, BAL — Waldman expects him priced out of Baltimore; Ravens prefer Kolar's blocking and zone-beating profile
- [[Michael Mayer]] — TE, LV — Nguyen: value is as the in-line blocker Bowers isn't; year-three blocking leap needed
- [[Chigoziem Okonkwo]] — TE, TEN (new page) — Harmon: expects a return to true in-line Y role; talented but never had a defined role, worth monitoring
- [[Zach Ertz]] — TE, WAS — Waldman: re-signed, TE1 upside at a TE26 ADP; short-area only, fits the offense (2025 take)
- [[Evan Engram]] — TE, DEN — Zachariason above consensus; Nix's short-area game plus weak Denver target competition at a low-end TE1 price (2025 takes)
- [[Taysom Hill]] — TE, NO — snap and touch spike; deep-league add only, not yet a start (2025 wk10)
- [[Dallas Goedert]] — TE, PHI — health worry; Kluge pulled him from Week 2 ranks, Kraft passing him (2025 takes, stale)
- [[Trey McBride]] — TE, ARI — massive target funnel with Brissett and receivers hurt; 38% target rate on blitz routes (2025 takes)
- [[Mark Andrews]] — TE, BAL — Waldman buy with Lamar back; expects Likely priced out in free agency (2025 takes)
- [[Jake Ferguson]] — TE, DAL — target volume spikes with Lamb out; Harmon unsure of the player, sure of the workload
- [[Justin Joly]] — TE, NC State — flex/mismatch chess piece, WR-style routes; size limits an every-down role (2024 takes, stale)
- [[Noah Gray]] — TE, KC — Waldman's pick for extra Chiefs targets post-Rice: most versatile option after Kelce, YAC + trust (2024 takes, stale)
- [[Charlie Kolar]] — TE, BAL — Waldman expects Baltimore to keep him over Likely: blocker who wins vs zone, does the little things
- [[Brenton Strange]] — TE, JAX — Waldman: sneaky TE1 with Engram gone, but a deep rookie TE class could reload over him (2025)
- [[Darnell Washington]] — TE, PIT — Waldman endorses the expanded role; wants Washington-Freiermuth as the Steelers pairing
- [[Cade Otten]] — TE, TB — Evans injury streamer; Gretch has him TE2 range, Harris outside top 25 (2025 in-season takes)
- [[Adam Trautman]] — TE, DEN — Waldman: Payton loyalty plus athleticism make him a discounted streaming TE (2024 takes, stale)
- [[Will Dissly]] — TE, LAC — third in Chargers first-read share, leads team in designed targets since bye (2024 takes, stale)
- [[Jonnu Smith]] — TE, PIT — Waldman wants his snaps reallocated to Freiermuth and Washington
- [[Tyler Warren]] — TE, IND — 8-99 breakout with real contested catches; Waldman still ranks Loveland above him, credits usage and availability
- [[Harold Fannin Jr.]] — TE, CLE — Angelo: Browns' best offensive playmaker through four weeks (2025 takes)
- [[Colston Loveland]] — TE, CHI — Waldman holds him as 2025 TE1 over Tyler Warren on look quality and blocking; slow rise after injuries
- [[Mason Taylor]] — TE, NYJ — Waldman low-end TE1 on Fields' tight-end lean; widely available (2025 take)
- [[Elijah Arroyo]] — TE, SEA — emerging boom/bust matchup play; splits with Barner, who keeps the low red zone
- [[Mike Gesicki]] — TE, CIN — Waldman: crazy value at TE27 ADP, sneaky TE1 in year two with Burrow despite stiff-footed profile
- [[Thomas Fidone]] — TE, Nebraska — Waldman: elite snapped turns and clean breaks; can handle inline work but it would cap receiving upside (2025 pre-draft)
- [[Gunnar Helm]] — TE, Texas — Waldman: separates short-area and up the seam but lacks breakaway explosion; route pacing too predictable (2025 pre-draft)
- [[Jackson Hawes]] — TE, Georgia Tech — Waldman: best inline blocker in 2025 class, low on RSP board; scouting interest over fantasy (2025 pre-draft take)
- [[Terrance Ferguson]] — TE, LAR — linear athlete, Gesicki-at-best ceiling; Waldman passes in redraft, viable dynasty rookie pick (2025)
- [[Oronde Gadsden II]] — TE, LAC — breaking out in a Syracuse-style straight-line role; Waldman revisiting his own evaluation
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
- [[Juwan Johnson]] — TE, NO — top-4 waiver add; 100% of dropbacks on field, sneaky TE1 with Taysom Hill out most of the season (2025)
- [[Darren Waller]] — TE, MIA — TD in each of two weeks and Dolphins' No. 2 target behind Waddle post-Hill, but on a snap pitch count (2025 takes)
- [[Hunter Henry]] — TE, NE — sell-high 'found money' TE9; Harris doubts any buyer exists (2025 takes)
- [[Greg Dulcich]] — TE, MIA — Angelo rest-of-season buy purely on negative game script in Miami (2025 takes)

<!-- Claude: maintain grouped by position (QB / RB / WR / TE), each with a
     one-line summary. See CLAUDE.md "Index maintenance". -->

## Concepts

- [[Aging Curves and Career Longevity]] — Age cliff vs age curve — careers fluctuate around a peak then fall off abruptly; population curve is ecological fallacy (2024 takes)
- [[Start Your Best Players]] — start top-down off your own rankings rather than chasing weekly matchups
- [[Scouting Bias and Player Archetypes]] — Harstad/Waldman: deviant personality traits are usually adaptive, and the archetype police apply the standard unevenly
- [[Weak Quarterback Play and Receiver Value]] — Bad QB play isn't a blanket label — what matters is which throws he'll make; Nabers under Jones vs Russ
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
- [[Preseason ADP vs In-Season Production]] — How many bad games outweigh a draft-day case — Harris and Ben Gretch on Thomas, Harrison, Jeanty, Kelce
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
- [[Targets Versus Team Points Rule]] — Harris: almost no receiver gets 10 targets a game now — undercuts both panic and WR1 overall picks
- [[Slot to Outside Conversion Risk]] — Harmon: inside-to-outside receiver conversions almost never take (Skyy Moore, Elijah Moore, McMillan); condensed splits blur alignment data
- [[Writing Craft in the Fantasy Industry]] — Fantasy writing is two crafts — fantasy and writing — with deadlines, volume and outlining tradeoffs (Waldman/Harstad, 2024)
- [[Feedback Scarcity and Analyst Development]] — Analyst work gets ~zero feedback; silence reads as failure but usually means fine — Harstad/Waldman on criticism (2024)
- [[Deliberate Rest and Creative Productivity]] — Waldman/Harstad: time off-screen is the work — Army artillery shift study, Friday football blackouts, burnout 3-4x/year (2024)
- [[Analyst Incentive Alignment and Audience Trust]] — Waldman: insiders praise players to recruit them as sources; discount access-driven hype (Schultz/Clark example)
- [[Fantasy Quarterback Value vs NFL Quarterback Quality]] — Waldman: after QB15 the gap to QB8-12 is small enough to stream matchups; Geno Smith at QB22 as the worked example
- [[Post-Bye Rookie Bump]] — Harmon: rookie post-bye improvement is a coaching-design effect, not automatic; only applies if the rookie wins on film
- [[Quarterback-Receiver Chemistry]] — Harmon and Koh: QB trust built through offseason reps drives targets in ways YPRR and separation metrics can't capture
- [[Recruiting Star Ratings and Early Breakout Age]] — Star ratings are a weak prior; early breakout beats upperclassmen for touches and signals talent — Jeanty, Judkins, Brown
- [[Cross-League Dynasty Portfolio Trading]] — Harstad's many-leagues-one-team framework: treat all dynasty rosters as one portfolio, arbitrage prices across leagues, harvest free picks
- [[Mining Bad Offenses]] — Waldman's waiver rule: skim the surface of bad offenses, dig deep only on high-scoring ones
- [[Historical Comps and Analyst Degrees of Freedom]] — Harstad via Waldman: 98% of backs comped to Trent Richardson in year one go on to great careers — comps prove little
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
- [[Alpha Receiver vs Committee Pass Catchers]] — Only 36 ten-target receiver games in 96 team games; five players did it twice — volume is spread thin
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
- [[Draft Capital Rep Allocation Bias]] — Draft capital does not guarantee rookie-year usage — Harris on Matthew Golden and depth chart analysis
- [[Rookie On-Ramp and Development Runway]] — Rookie deployment as a highway on-ramp — Mahomes behind Alex Smith vs. Richardson thrown into traffic; be patient early
- [[Positional Versatility and Roster Redundancy]] — Rosters balance versatility against redundancy — deliberate Venn-diagram overlap in every room, and it all reduces to coach trust
- [[Speed of Instinct and Overthinking]] — Camp arc for young players — isolated-skill flashes early, then added layers force thinking and cost speed of instinct
- [[Playing Experience and Evaluation Blind Spots]] — Waldman: playing one position doesn't confer knowledge of another; judge a critique by whether it names skills
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
- [[Pre-Snap Complexity and Operational Lag]] — Motion-heavy play callers (Coen, Ben Johnson) need time — false starts and illegal shifts as an early-season lag signal
- [[Third-Year Receiver Leap and the Six-Game Breakout Window]] — Third-year receiver leaps vs the modern six-game bust window — Harmon on Flowers and JSN as live examples
- [[Receiver Buy-In and Addition by Subtraction]] — Receiver buy-in as a team-context variable — Harmon/Koh on Diontae Johnson, D.J. Moore and Tyreek Hill; trade before the cheese curdles
- [[Explanatory Models That Predict Nothing]] — Harstad's test: an explanation that fits every outcome predicts nothing; make the call first, then grade it against chance
- [[Toughness Narratives and Salience Bias]] — Soft/hands narratives are set by nationally visible moments, not rates; Waldman and Harstad on reputation, salience and player temperament
- [[Yards Before Contact vs Rushing Efficiency Delta]] — Read RB efficiency against the line's yards before contact; missed tackles forced buys contracts but hides on-schedule failure
- [[Anonymous Sourcing and Disgruntled Former Staff]] — Discount anonymous character reporting sourced from staff already fired; the same method writes the opposite article
- [[Loaded Boxes and Unblocked Defender Rate]] — Koh's run-context charting: ~19% unblocked and ~23% loaded-box baselines; extremes suggest tipped plays
- [[Running Back Trade Market Scarcity Premium]] — In-season trade market prices RBs far above WRs; Harris says pay up or don't trade for one
- [[Buy-Low Windows and Panic Sells]] — Trade windows close on one good game; find the manager most likely to panic-sell, and buy cheap
- [[Personality Narratives and Retrofitted Explanations]] — Announcers retrofit personality explanations onto results; Harris argues for judging only observable play
- [[Hot Dog Quarterbacks]] — Guest Jeff Bell's term for a QB whose points you don't want to watch being made — production without process comfort
- [[Twelve Personnel Rise and Slot Receiver Playing Time]] — Harmon: 12 personnel up to 22.4% since 2024, structurally capping slot receiver snaps and top-30 WR receptions
- [[Wide Receiver Injury Rate Trend]] — Harmon's untested theory: alpha WRs absorbing middle-of-field manufactured volume may be raising WR injury rates
- [[Dig Routes and Deep Overs vs Cover Two]] — Digs and deep overs as the cover-two answer; middle-of-field winners plus a confident veteran QB are the league's top producers
- [[Fantasy Points Allowed and Opponent Context]] — Concept — points-allowed ranks are 'paper champions'; check who a defense actually faced
- [[Wide Receiver Positional Flatness]] — Concept — Harris: WR5 through WR50 is flat, so weekly rank gaps rarely decide lineups
- [[Goodhart's Law and Metrics as Targets]] — Harstad's Goodhart's Law framing — a good measure stops being good once it becomes a target; drops, size thresholds, SPARQ
- [[Dynasty Rebuild Timing and Value Decay]] — Harstad: rebuild only when old and non-contending; value decays ~20%/yr, so 'don't lose value'; cap rebuilds at 1-2 years
- [[Positional Stockpiling and Roster Imbalance]] — Concentrating picks at one position lowers variance and upside; Harstad says effect is small and needs a liquid trade market
- [[Sunday Morning Insider Reports and Fantasy Noise]] — Waldman on Sunday-morning splash reports overriding your own read — Vidal case study; 'fuck the news, feel your hunches'
- [[Defensive Blueprints and Copycat Feasibility]] — When a shutdown game plan is a copyable blueprint vs a personnel artifact — Waldman on the Steelers-Colts tape
- [[Assumption of Rational Coaching]] — Sigmund Bloom's phrase, adopted by Waldman — don't assume a staff will repeat the obviously good thing it just did
- [[Running Back Longevity and Draft Round Study]] — Waldman study: 23 RBs and 23 WRs cleared 5-of-7 starter seasons; 16 of 23 RBs went rounds 1-2
- [[Settled Player Opinion and Flat Dynasty Value]] — Known players carry flat dynasty value so production is free; profit sits where your read beats consensus
- [[Measurable Skills Bias in Running Back Analytics]] — Analytics overrate what is measurable: tackle-breaking and charted drops mislead without tackle quality context
- [[Quarterback Ownership of the Offense]] — Harstad: some QBs author an offense and some administer one; Nix owns Denver's, Goff runs Johnson's
- [[Midseason Trade Acquisition and Offensive Acclimation]] — Why deadline-acquired receivers stall; scheme continuity and chunk-play scoring as the two mitigators (Harris, 2025)
- [[Goal Line Vulture Panic and Snap Share Evidence]] — Test goal-line vulture panic against red zone snap counts before acting; one conversion is not a trend
- [[Paper Value and Championship Correlation]] — Harstad: perfect values would make paper champions real champions; flawed values still correlate, so don't mock the strategy
- [[Era Translation and Player Adaptability]] — Waldman and Harstad: era-bound critiques of all-timers ignore that great players adapt; only physical paradigm shifts truly disqualify
- [[Formative Era Nostalgia and Golden Age Bias]] — Harstad: your first football era locks in as your golden age and silently sets your archetype preferences for life
- [[Positional Class Clustering and Warped Expectations]] — Harstad: class talent is random; the early-2000s RB pile-up was a fluke that warped fantasy's positional baselines for decades
- [[Touch Volume and In-Game Adaptation]] — Waldman: volume lets a back learn in-game tendencies; Harstad agrees usage flatters backs but says the 2000s group was truly great

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
