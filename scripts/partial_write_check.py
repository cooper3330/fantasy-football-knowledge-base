#!/usr/bin/env python3
"""
Detect a partial write: state.json still calls an episode `fetched`, but the
wiki already carries content from it.

WHY THIS EXISTS: a failed ingest agent is rarely a no-op. It typically dies
after writing bullets to 10-40 pages and before setting the status, so the next
run hands the same transcript to a fresh agent and every one of those bullets is
appended a second time. Stopping the failed run does not help -- the damage is
done by the NEXT run, which is why this is checked BEFORE each episode.

Two earlier versions of this check were wrong, in opposite directions:

  1. "bullets dated to the episode AND no source page for it" -- missed a real
     partial write, because the agent got far enough to write its source page
     before dying, which made an unfinished ingest look complete.
  2. "any page citing the episode's date" -- halted a run on a false positive,
     because two shows published on 2024-04-11 and the pages citing that date
     belonged to the other one, already ingested.

So a date alone proves nothing. What matters is whether a citation *resolves* to
a source page belonging to some OTHER episode. Anything dated to this episode
that cannot be accounted for that way is unexplained, and unexplained means
partial.

Exit 0 = clean (also when the episode is not `fetched`, or is unknown).
Exit 2 = partial write; details on stdout.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "wiki" / "sources"
CONTENT = ["players", "concepts", "formats", "experts"]
WIKILINK = re.compile(r"\[\[([^\]|]+)")


def frontmatter_value(text, key):
    for line in text.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
        if line.strip() == "---" and not line.startswith(key):
            continue
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guid", required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    state = json.loads((REPO / "scripts" / "state.json").read_text())
    ep = state["episodes"].get(args.guid) or {}
    # Content in the wiki for an already-ingested episode is the expected
    # outcome, not damage. Only `fetched` can be partial.
    if ep.get("status") != "fetched":
        return 0
    pdate = ep.get("pub_date") or ""
    if not pdate:
        return 0

    findings = []

    # Source pages, mapped to the episode they belong to. A source page carrying
    # OUR guid is proof on its own -- that is failure mode (1) above.
    accounted = set()
    for p in sorted(SOURCES.glob("*.md")):
        if p.name == "SOURCE_CATALOG.md":
            continue
        text = p.read_text(errors="ignore")
        sguid = frontmatter_value(text, "guid")
        if sguid == args.guid:
            findings.append(f"source page belongs to this episode: {p.relative_to(REPO)}")
        elif frontmatter_value(text, "date") == pdate and sguid:
            # Same date, different episode -- this is what legitimately explains
            # bullets dated pdate.
            accounted.add(p.stem)

    # Pages dated to this episode that cannot be explained by another episode's
    # source page are unexplained.
    #
    # Resolution is PAGE-level, not line-level. Line-level was tried and cries
    # wolf: a section heading can carry the date with no citation, and a bullet's
    # source wikilink often sits in a section header rather than on the bullet
    # itself. Both look like dangling citations line-by-line and are fine in
    # context. If a page links the same-date source page of a different episode
    # anywhere, its mentions of that date are accounted for.
    for sub in CONTENT:
        for p in sorted((REPO / "wiki" / sub).rglob("*.md")):
            text = p.read_text(errors="ignore")
            if pdate not in text:
                continue
            if set(WIKILINK.findall(text)) & accounted:
                continue
            lines = [i for i, l in enumerate(text.splitlines(), 1) if pdate in l]
            findings.append(
                f"{p.relative_to(REPO)} cites {pdate} on line(s) "
                f"{','.join(map(str, lines[:5]))} with no source page for another episode"
            )

    if not findings:
        return 0

    if not args.quiet:
        print(f"!!! PARTIAL WRITE for {args.guid} ({pdate}) -- {len(findings)} finding(s):")
        for f in findings[:15]:
            print(f"!!!   {f}")
        if len(findings) > 15:
            print(f"!!!   ... and {len(findings) - 15} more")
        print("!!! state.json still says 'fetched', so re-ingesting WILL duplicate")
        print("!!! these. Roll back the episode's writes before retrying.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
