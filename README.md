# fantasy-football-knowledge-base

An LLM-maintained Obsidian wiki of fantasy football advice, built from podcast
and media transcripts of select experts — in the spirit of Andrej Karpathy's
"LLM wiki" approach: small, atomic, densely cross-linked notes that Claude
writes and links as source material comes in.

Start at [Home.md](Home.md). See [CLAUDE.md](CLAUDE.md) for the wiki's
maintenance rules and how new transcripts get ingested.

## Structure
- `Experts/` — analyst/host notes: philosophy, track record, sources
- `Players/` — one note per player, aggregating dated, attributed takes
- `Concepts/` — strategy/scheme notes (e.g. Zero RB)
- `Sources/` — one note per ingested transcript/appearance
- `_templates/` — starting shape for each note type
- `Experts.md` / `Players.md` / `Concepts.md` / `Sources.md` — top-level indexes
