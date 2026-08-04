#!/usr/bin/env python3
"""
Checks that every wiki page carries well-formed YAML frontmatter.

Frontmatter is what makes the vault queryable as data rather than as prose --
Obsidian Dataview, tag search, and any future tooling all key off it. It held by
convention alone until now (agents copied the shape from wiki/_templates/), which
works right up until one agent doesn't. This script makes the convention checkable.

Deliberately REPORT-ONLY, with no --fix. Repairing a missing `team:` or `date:`
would mean inventing a value, and CLAUDE.md's "don't fabricate" rule outranks the
convenience. It tells you exactly what is wrong and leaves the writing to a human
or an agent that has the source in front of it.

Parsing is by hand rather than via PyYAML: the schema below is flat scalars and
one-line lists, the repo otherwise depends only on the stdlib, and a hard
dependency here would break the headless launchd path for no real gain.

Usage:
  lint_frontmatter.py           # report; exit 1 if anything is wrong
  lint_frontmatter.py -v        # also list every file checked
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
POSITIONS = {"QB", "RB", "WR", "TE"}

# type -> required keys. `tags` must always be present and must contain the
# page's own type as a tag, so tag search and the `type:` field never disagree.
SCHEMA = {
    "player":    ["type", "team", "position", "tags"],
    "expert":    ["type", "outlet", "tags"],
    "concept":   ["type", "tags"],
    "format":    ["type", "priority", "tags"],
    "source":    ["type", "expert", "show", "episode", "date", "guid", "raw", "tags"],
    "synthesis": ["type", "question", "formats", "last_refreshed", "tags"],
    "index":     ["type", "tags"],
    "log":       ["type", "tags"],
    "catalog":   ["type", "tags"],
}

# Which type each location must declare. Checked against the file's own `type:`
# so a page can never sit in the wrong folder while claiming to be something else.
DIR_TYPE = {
    "wiki/players": "player",
    "wiki/experts": "expert",
    "wiki/concepts": "concept",
    "wiki/formats": "format",
    "wiki/sources": "source",
    "wiki/synthesis": "synthesis",
}
FILE_TYPE = {
    "index.md": "index",
    "log.md": "log",
    "wiki/sources/SOURCE_CATALOG.md": "catalog",
}

# Optional keys that are legal anywhere -- Obsidian reads `aliases` natively, and
# it is the right home for the nickname problem in CLAUDE.md rule 6 ("CMC").
OPTIONAL_ANYWHERE = {"aliases"}


def parse_frontmatter(text):
    """Return (dict, error). dict is None when there is no frontmatter block."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, "no YAML frontmatter (file must open with '---')"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "frontmatter opened with '---' but never closed"

    fm = {}
    for raw_line in lines[1:end]:
        if not raw_line.strip():
            continue
        if ":" not in raw_line:
            return None, f"malformed frontmatter line: {raw_line!r}"
        key, _, value = raw_line.partition(":")
        fm[key.strip()] = value.strip()
    return fm, None


def parse_tags(value):
    """`[player, prospect]` -> {'player', 'prospect'}."""
    inner = value.strip().lstrip("[").rstrip("]")
    return {t.strip() for t in inner.split(",") if t.strip()}


def expected_type(rel):
    """The type a file at this path must declare, or None if unmanaged."""
    if rel in FILE_TYPE:
        return FILE_TYPE[rel]
    parent = str(Path(rel).parent)
    return DIR_TYPE.get(parent)


def check(path, is_template):
    """Return a list of problem strings for one file."""
    rel = str(path.relative_to(REPO))
    problems = []
    fm, err = parse_frontmatter(path.read_text(encoding="utf-8"))
    if err:
        return [err]

    declared = fm.get("type", "")
    if is_template:
        # A template's type is fixed by its own `type:` line; its filename is the
        # shape's name, not a location. Values are intentionally blank.
        want = declared
    else:
        want = expected_type(rel)
        if want is None:
            return []  # not a managed location
        if declared != want:
            problems.append(f"type is {declared!r}, expected {want!r} for this location")

    required = SCHEMA.get(want)
    if required is None:
        return problems + [f"unknown page type {want!r} (not in SCHEMA)"]

    for key in required:
        if key not in fm:
            problems.append(f"missing required key: {key}")

    extra = set(fm) - set(required) - OPTIONAL_ANYWHERE
    if extra:
        problems.append(f"unexpected key(s): {', '.join(sorted(extra))}")

    if "tags" in fm:
        tags = parse_tags(fm["tags"])
        if want and want not in tags:
            problems.append(f"tags {sorted(tags)} missing the base tag {want!r}")

    # Templates ship with empty values on purpose -- that is the whole point of a
    # template -- so value checks apply only to real pages.
    if is_template:
        return problems

    for key in required:
        if key in fm and not fm[key]:
            problems.append(f"empty value for required key: {key}")

    if fm.get("position") and fm["position"] not in POSITIONS:
        problems.append(f"position {fm['position']!r} not one of {sorted(POSITIONS)}")

    for key in ("date", "last_refreshed"):
        if fm.get(key) and not DATE_RE.match(fm[key]):
            problems.append(f"{key} {fm[key]!r} is not YYYY-MM-DD")

    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="list every file checked, not just the failures")
    args = ap.parse_args()

    targets = sorted(REPO.glob("wiki/**/*.md")) + [REPO / "index.md", REPO / "log.md"]
    failures = {}
    checked = 0

    for path in targets:
        if not path.exists():
            continue
        rel = str(path.relative_to(REPO))
        is_template = rel.startswith("wiki/_templates/")
        if not is_template and expected_type(rel) is None:
            continue
        checked += 1
        problems = check(path, is_template)
        if problems:
            failures[rel] = problems
        elif args.verbose:
            print(f"  ok  {rel}")

    print(f"\nChecked {checked} page(s).")
    if not failures:
        print("Frontmatter OK -- every page conforms to its type schema.")
        return 0

    print(f"{len(failures)} page(s) with problems:\n")
    for rel, problems in sorted(failures.items()):
        print(f"  {rel}")
        for p in problems:
            print(f"      - {p}")
    print("\nNo automatic repair: filling these in means knowing the source. "
          "See wiki/_templates/ for each type's shape.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
