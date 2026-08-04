---
type: catalog
tags: [catalog]
---

# Source Catalog

Every raw source and its ingestion status. The authoritative machine-readable
record is `scripts/state.json`; this page is the human-readable view.

Raw transcripts live in `raw/transcripts/<show>/` and are **never modified**.
Once ingested, each episode also gets a summary page in `wiki/sources/`.

| Status | Meaning |
|---|---|
| `pending` | Known from the RSS feed, not yet transcribed |
| `fetched` | Transcript sitting in `raw/transcripts/`, awaiting ingestion |
| `ingested` | Read and woven into the wiki; summary page exists here |

## Shows

| Show | Expert | Feed | Raw path |
|---|---|---|---|
| Reception Perception: The Show | [[Matt Harmon]] | `feeds.megaphone.fm/reception-perception-the-show` | `raw/transcripts/reception-perception/` |
| Harris Fantasy Football Podcast | [[Chris Harris]] | `harrisfootball.libsyn.com/rss` | `raw/transcripts/harris-football/` |
| Matt Waldman's RSP Cast | [[Matt Waldman]] | `mattwaldmanrsp.com/feed/podcast/` | `raw/transcripts/rsp-cast/` |

## Ingested episodes

| Date | Expert | Episode | Summary page |
|---|---|---|---|
| 2023-12-14 | [[Matt Waldman]] | What Is Happening to NFL Careers? (w/ Adam Harstad) | [[Matt Waldman's RSP Cast - 2023-12-14]] |
| 2023-12-18 | [[Matt Waldman]] | Feel It or F@#k It 12.18.23 — Week 15 (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2023-12-18]] |
| 2023-12-21 | [[Matt Waldman]] | Going Deep — Pacing/Control of Elite Movers + Harrison Jr. vs Nabers Pro-Readiness (w/ Brandon Angelo) | [[Matt Waldman's RSP Cast - 2023-12-21 (Pacing and Control)]] |
| 2023-12-21 | [[Matt Waldman]] | The Cyclical Nature of Talent vs. Scheme + NIL's Impact (w/ Adam Harstad) | [[Matt Waldman's RSP Cast - 2023-12-21]] |
| 2024-01-01 | [[Matt Waldman]] | Feel It Or F@#k It: 1.1.24 (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-01-01]] |
| 2024-01-04 | [[Matt Waldman]] | Favorite 2023 NFL Storylines and 2023 Rookie Review (w/ Adam Harstad) | [[Matt Waldman's RSP Cast - 2024-01-04]] |
| 2024-01-08 | [[Matt Waldman]] | Feel It Or F@#k It: 1.8.24 (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-01-08]] |
| 2024-01-11 | [[Matt Waldman]] | Adam's 2023 Post-Rookie-Year Prospect Model — RSP Film and Theory (w/ Adam Harstad) | [[Matt Waldman's RSP Cast - 2024-01-11 (Post-Rookie Model)]] |
| 2024-01-11 | [[Matt Waldman]] | The Safest RB in the Draft, the Sleeper Miscast as a Gadget, the Keon Coleman Rollercoaster, and Penix and Punishment — Going Deep (w/ Brandon Angelo) | [[Matt Waldman's RSP Cast - 2024-01-11 (Going Deep - Draft Prospects)]] |
| 2024-01-15 | [[Matt Waldman]] | Feel It Or F@#k It, with guest Daniel Harms | [[Matt Waldman's RSP Cast - 2024-01-15]] |
| 2024-01-16 | [[Matt Harmon]] | Wild Card Weekend Recap (w/ James Koh) | [[Reception Perception The Show - 2024-01-16]] |
| 2024-01-18 | [[Matt Harmon]] | College Standouts & NFL Divisional Round Preview (w/ James Koh) | [[Reception Perception The Show - 2024-01-18]] |
| 2024-01-22 | [[Matt Waldman]] | Feel It Or F@#k It: 1.22.24 (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-01-22]] |
| 2024-01-23 | [[Matt Harmon]] | Some Fun Games in the Divisional Round (w/ James Koh) | [[Reception Perception The Show - 2024-01-23]] |
| 2024-01-25 | [[Matt Harmon]] | Head Coaching News & Conference Championship Breakdowns (w/ James Koh) | [[Reception Perception The Show - 2024-01-25]] |
| 2024-01-29 | [[Matt Waldman]] | Feel It Or F@#k It: 1.29.24 (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-01-29]] |
| 2024-01-30 | [[Matt Harmon]] | Conference Championship Review & More Coaching Hires (w/ James Koh) | [[Reception Perception The Show - 2024-01-30]] |
| 2024-02-01 | [[Matt Waldman]] | 2024 Sr. Bowl Fallout and Fave Developmental Picks — Going Deep (w/ Brandon Angelo) | [[Matt Waldman's RSP Cast - 2024-02-01]] |
| 2024-02-01 | [[Matt Harmon]] | Arthur Smith to Pittsburgh, Seahawks Personnel & Senior Bowl Takes (w/ James Koh) | [[Reception Perception The Show - 2024-02-01]] |
| 2024-02-02 | [[Matt Waldman]] | The NFL Hall of Fame (And Our Picks for the '24 Class) — RSP Film and Theory (w/ Adam Harstad) | [[Matt Waldman's RSP Cast - 2024-02-02]] |
| 2024-02-05 | [[Matt Waldman]] | Feel It Or F@#k It: 2.5.24 (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-02-05]] |
| 2024-02-12 | [[Matt Waldman]] | Feel It Or F@#k It Post-Super Bowl Edition (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-02-12]] |
| 2024-02-13 | [[Matt Harmon]] | Chiefs Take Down 49ers for Super Bowl LVIII (w/ James Koh) | [[Reception Perception The Show - 2024-02-13]] |
| 2024-02-19 | [[Matt Waldman]] | Feel It Or F@#k It: Never Too Early to Draft Edition (w/ Bob Harris) | [[Matt Waldman's RSP Cast - 2024-02-19]] |
| 2024-02-22 | [[Matt Waldman]] | Going Deep with Brandon Angelo and Matt Waldman: The 2024 RB Class Edition (w/ Brandon Angelo) | [[Matt Waldman's RSP Cast - 2024-02-22]] |
| 2024-02-26 | [[Matt Waldman]] | Feel It Or F@#k It: Fantasy Drafts in February, the NFL Combine, and QB Metrics | [[Matt Waldman's RSP Cast - 2024-02-26]] |
| 2024-02-27 | [[Matt Harmon]] | Tee Higgins & Mike Evans, Marvin Harrison Jr. & Bieniemy Picks College Ball | [[Reception Perception The Show - 2024-02-27]] |

<!-- Claude: append a row per ingested episode as you process it:
     | date | expert | episode | summary page |
     Keep this table in chronological order, oldest first. -->
