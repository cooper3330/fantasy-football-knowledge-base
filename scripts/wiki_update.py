#!/usr/bin/env python3
"""
Applies deltas to the three shared files an ingest agent only ever appends to:
index.md, log.md, and wiki/sources/SOURCE_CATALOG.md.

WHY THIS EXISTS -- it is the single biggest token lever in the pipeline.

The Edit tool requires reading a file before editing it. So an agent appending
one line to log.md pays for all of log.md. Measured at 25 episodes ingested:

    log.md      ~14,400 tok    read in full to append ~1 entry
    index.md    ~14,100 tok    read in full to touch ~12 lines
    catalog      ~1,300 tok    read in full to append 1 row
    ------------------------------------------------------------
                ~29,800 tok    per episode, ~50% of an episode's unique tokens

Worse, index.md and log.md grow ~570 tok *each* per episode. Extrapolated over
the 278-episode backlog they reach ~170k tokens apiece -- at which point an
ingest agent cannot open them at all and the pipeline simply stops working.

With this script the agent passes only the delta and never opens the files, so
the per-episode cost of all three drops to roughly zero and stays flat no matter
how large they grow.

Secondary benefit: --index-set is insert-or-replace keyed on the page name, so
an index line cannot silently fork into two competing entries. That structurally
removes the "stale index line" failure mode in CLAUDE.md's lint list -- the one
that matters most, because during a live draft the index line is often all that
gets read.

Usage:
  wiki_update.py --index-set "Jahmyr Gibbs" "RB, DET — Waldman's 2024 RB1 over Bijan"
  wiki_update.py --catalog-row 2024-02-26 "Matt Waldman" "Feel It Or F@#k It" "Matt Waldman's RSP Cast - 2024-02-26"
  wiki_update.py --log-append < entry.md        # or heredoc
  wiki_update.py --check-index                  # report over-long index lines
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX = REPO / "index.md"
LOG = REPO / "log.md"
CATALOG = REPO / "wiki" / "sources" / "SOURCE_CATALOG.md"

# The index is the retrieval layer and is often the only thing read during a live
# draft, so a line has to be scannable. It is also read on every future ingest,
# so every word is paid for repeatedly. 25 words is enough for
# "position, team - headline view" and not enough for a paragraph.
MAX_INDEX_WORDS = 25

# Section each page type routes to. Players additionally split by position.
POSITION_SECTION = {
    "QB": "### Quarterbacks",
    "RB": "### Running Backs",
    "WR": "### Wide Receivers",
    "TE": "### Tight Ends",
}


def frontmatter(path):
    fm = {}
    lines = path.read_text(encoding="utf-8").split("\n")
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm


def section_for(page):
    """Which index heading this page's line belongs under."""
    player = REPO / "wiki" / "players" / f"{page}.md"
    if player.exists():
        pos = frontmatter(player).get("position", "")
        if pos not in POSITION_SECTION:
            sys.exit(f"error: {page} has position {pos!r}; expected one of "
                     f"{sorted(POSITION_SECTION)}")
        return POSITION_SECTION[pos]
    if (REPO / "wiki" / "concepts" / f"{page}.md").exists():
        return "## Concepts"
    if (REPO / "wiki" / "synthesis" / f"{page}.md").exists():
        return "## Synthesis"
    sys.exit(f"error: no player, concept or synthesis page named {page!r}. "
             f"Create the page before indexing it.")


def index_set(page, summary):
    summary = summary.strip().lstrip("—-").strip()
    words = len(summary.split())
    if not words:
        sys.exit("error: empty summary. An index entry with no summary is worse "
                 "than none -- it is what gets read during a live draft.")
    if words > MAX_INDEX_WORDS:
        sys.exit(f"error: summary is {words} words, limit is {MAX_INDEX_WORDS}.\n"
                 f"The index is scanned during live drafts and re-read on every "
                 f"future ingest -- lead with position/team and the headline view, "
                 f"and leave the detail on the page itself.")

    heading = section_for(page)
    line = f"- [[{page}]] — {summary}"
    lines = INDEX.read_text(encoding="utf-8").split("\n")

    # Replace in place if this page is already indexed, wherever it currently is.
    # Keyed on the exact wikilink so a rename can never leave two live entries.
    marker = f"- [[{page}]]"
    for i, existing in enumerate(lines):
        if existing.startswith(marker) and existing[len(marker):len(marker) + 3].strip() in ("—", "-", ""):
            lines[i] = line
            INDEX.write_text("\n".join(lines), encoding="utf-8")
            print(f"index: updated {page} under {heading}")
            return

    try:
        start = lines.index(heading)
    except ValueError:
        sys.exit(f"error: heading {heading!r} not found in index.md")

    # Insert after the last existing entry in this section. Sections end with an
    # HTML maintenance comment, so appending blindly would land after it.
    insert = start + 1
    last_entry = None
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("#"):
            break
        if lines[i].startswith("- [["):
            last_entry = i
    insert = (last_entry + 1) if last_entry is not None else insert
    lines.insert(insert, line)
    INDEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"index: added {page} under {heading}")


def catalog_row(date, expert, episode, page):
    text = CATALOG.read_text(encoding="utf-8")
    lines = text.split("\n")
    row = f"| {date} | [[{expert}]] | {episode} | [[{page}]] |"

    if row in lines:
        print("catalog: row already present, nothing to do")
        return

    # Keep the table chronological: insert before the first row with a later
    # date, else after the last row. Never append to end-of-file -- a maintenance
    # comment follows the table.
    rows = [i for i, l in enumerate(lines) if re.match(r"^\| \d{4}-\d{2}-\d{2} \|", l)]
    if not rows:
        sys.exit("error: no dated rows found in SOURCE_CATALOG.md")
    insert = rows[-1] + 1
    for i in rows:
        if lines[i].split("|")[1].strip() > date:
            insert = i
            break
    lines.insert(insert, row)
    CATALOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"catalog: added row for {date}")


def log_append(text):
    text = text.rstrip("\n")
    if not text.strip():
        sys.exit("error: refusing to append an empty log entry")
    if not text.lstrip().startswith("## ["):
        sys.exit("error: log entries must start with '## [YYYY-MM-DD] <operation> | <subject>'")
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write("\n" + text + "\n")
    print(f"log: appended {len(text.split(chr(10)))} line(s)")


def check_index():
    over = []
    for line in INDEX.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^- \[\[([^\]]+)\]\]\s*[—-]?\s*(.*)$", line)
        if m and len(m.group(2).split()) > MAX_INDEX_WORDS:
            over.append((len(m.group(2).split()), m.group(1)))
    if not over:
        print(f"index OK -- every entry within {MAX_INDEX_WORDS} words.")
        return 0
    over.sort(reverse=True)
    print(f"{len(over)} index line(s) over {MAX_INDEX_WORDS} words:\n")
    for words, page in over:
        print(f"  {words:>4} words  {page}")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index-set", nargs=2, metavar=("PAGE", "SUMMARY"))
    ap.add_argument("--catalog-row", nargs=4,
                    metavar=("DATE", "EXPERT", "EPISODE", "SUMMARY_PAGE"))
    ap.add_argument("--log-append", action="store_true",
                    help="append the log entry supplied on stdin")
    ap.add_argument("--check-index", action="store_true")
    args = ap.parse_args()

    if args.index_set:
        index_set(*args.index_set)
    if args.catalog_row:
        catalog_row(*args.catalog_row)
    if args.log_append:
        log_append(sys.stdin.read())
    if args.check_index:
        return check_index()
    if not any((args.index_set, args.catalog_row, args.log_append, args.check_index)):
        ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
