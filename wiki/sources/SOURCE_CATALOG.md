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

<!-- Claude: append a row per ingested episode as you process it:
     | date | expert | episode | summary page |
     Keep this table in chronological order, oldest first. -->
