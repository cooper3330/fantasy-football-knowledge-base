#!/usr/bin/env python3
"""Tests for the alias helpers in wiki_update.py and their prompt formatting.

`aliases:` in a page's frontmatter lists the spellings that are the same page
(nicknames, and the ASR mangles this wiki keeps meeting). Nothing used to read it,
which is how one player ended up as Ja'Kobi Lane, Jacoby Lane and (via a misfiled
take) Jaylin Lane. These pin the rules the fix depends on:

  - an alias only resolves a name that has NO page of its own (an existing page
    always wins -- an alias must never redirect a take away from a real page);
  - an ambiguous alias (two pages claim it) resolves to neither;
  - links are rewritten, prose never is;
  - lint can see an alias that is also a page (an unmerged duplicate).

Run directly:  python3 scripts/test_aliases.py
"""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki_update as wu                                           # noqa: E402
import ingest_manifest as im                                       # noqa: E402

fails = 0


def check(label, cond, extra=""):
    global fails
    fails += not cond
    print(f"{'ok  ' if cond else 'FAIL'} {label}")
    if not cond and extra:
        print("     " + str(extra)[:400])


def page(root, d, name, aliases=None, kind="player", body=""):
    fm = f"type: {kind}\n" + (f"aliases: {aliases}\n" if aliases is not None else "") + f"tags: [{kind}]\n"
    p = root / d / f"{name}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"---\n{fm}---\n\n# {name}\n{body}\n")
    return p


def vault():
    root = Path(tempfile.mkdtemp(prefix="aliases-")) / "wiki"
    page(root, "players", "Ja'Kobi Lane", "[Jacoby Lane, Jakobi Lane]")
    page(root, "players", "Jakobi Meyers", "[Jacoby Meyers]")
    page(root, "players", "Plain Player")
    page(root, "concepts", "Sacrificial X Receiver", "[Sacrificial X]", kind="concept")
    return root


# --- parse_aliases ----------------------------------------------------------
check("bracketed list", wu.parse_aliases("[A, B]") == ["A", "B"])
check("bare comma list", wu.parse_aliases("A, B") == ["A", "B"])
check("quoted entries are unquoted", wu.parse_aliases("[\"A B\", 'C']") == ["A B", "C"])
check("an apostrophe inside a name survives", wu.parse_aliases("[Ja'Kobi Lane, X]") == ["Ja'Kobi Lane", "X"])
check("a leading apostrophe is not mistaken for a quote pair", wu.parse_aliases("['Tre, Y]") == ["'Tre", "Y"])
check("empty values give no aliases", wu.parse_aliases("") == [] and wu.parse_aliases("[]") == [])

# --- page_aliases reads frontmatter only -------------------------------------
root = vault()
check("page_aliases reads the key", wu.page_aliases(root / "players" / "Ja'Kobi Lane.md") == ["Jacoby Lane", "Jakobi Lane"])
check("page without aliases gives []", wu.page_aliases(root / "players" / "Plain Player.md") == [])
body_only = page(root, "players", "Body Mention", body="\naliases: [Not Real]\n")
check("an 'aliases:' line in the BODY is not read", wu.page_aliases(body_only) == [])
nofm = root / "players" / "No Frontmatter.md"
nofm.write_text("# No Frontmatter\naliases: [Nope]\n")
check("a page with no frontmatter gives []", wu.page_aliases(nofm) == [])
check("a missing file gives [] instead of raising", wu.page_aliases(root / "players" / "Ghost.md") == [])

# --- load_aliases ------------------------------------------------------------
tbl = wu.load_aliases(root)
check("lookups are case-insensitive", tbl.get("jacoby lane") == [("player", "Ja'Kobi Lane")], tbl)
check("concept aliases carry their kind", tbl.get("sacrificial x") == [("concept", "Sacrificial X Receiver")])
page(root, "players", "Self Alias", "[self alias, Other]")
check("an alias equal to the page's own name is dropped", "self alias" not in wu.load_aliases(root))

# --- resolve_name ------------------------------------------------------------
r = lambda kind, name, **k: wu.resolve_name(kind, name, wiki_dir=root, **k)
check("alias resolves to the canonical page", r("player", "Jacoby Lane") == "Ja'Kobi Lane")
check("resolution ignores case", r("player", "jacoby LANE") == "Ja'Kobi Lane")
check("a canonical name is left alone", r("player", "Ja'Kobi Lane") == "Ja'Kobi Lane")
check("an unknown name is left alone", r("player", "Somebody Else") == "Somebody Else")
check("an alias of another KIND does not resolve", r("concept", "Jacoby Lane") == "Jacoby Lane")
check("an unknown kind returns the name instead of exiting", r("team", "Jacoby Lane") == "Jacoby Lane")
# the safety rule: an existing page wins over an alias
page(root, "players", "Jacoby Lane")                 # an unmerged duplicate still on disk
check("an EXISTING page of that name is never redirected", r("player", "Jacoby Lane") == "Jacoby Lane")
(root / "players" / "Jacoby Lane.md").unlink()
check("...and it resolves again once the duplicate is gone", r("player", "Jacoby Lane") == "Ja'Kobi Lane")
# ambiguity: two pages claim one alias
page(root, "players", "Rival Page", "[Jakobi Lane]")
check("an alias claimed by two pages resolves to neither", r("player", "Jakobi Lane") == "Jakobi Lane")

# --- rewrite_links -----------------------------------------------------------
root = vault()
rw = lambda text: wu.rewrite_links(text, wiki_dir=root)
txt, ch = rw("saw [[Jacoby Lane]] today")
check("[[alias]] -> [[canonical]]", txt == "saw [[Ja'Kobi Lane]] today" and ch == [("Jacoby Lane", "Ja'Kobi Lane")], (txt, ch))
txt, _ = rw("saw [[Jacoby Lane|Lane]] today")
check("the |display text is preserved", txt == "saw [[Ja'Kobi Lane|Lane]] today", txt)
txt, ch = rw("known as Jacoby Lane or MVS in prose")
check("alias in PROSE is untouched", txt == "known as Jacoby Lane or MVS in prose" and ch == [])
txt, ch = rw("[[Plain Player]] and [[Nobody]]")
check("non-alias links are untouched", txt == "[[Plain Player]] and [[Nobody]]" and ch == [])
page(root, "players", "Jacoby Meyers")               # unmerged duplicate on disk
txt, ch = rw("[[Jacoby Meyers]]")
check("a link to an EXISTING page of that name is untouched", txt == "[[Jacoby Meyers]]" and ch == [])
txt, ch = rw("two: [[Jacoby Lane]] and [[Jakobi Lane]]")
check("several links in one string all rewrite", txt == "two: [[Ja'Kobi Lane]] and [[Ja'Kobi Lane]]" and len(ch) == 2, (txt, ch))
check("a string with no links short-circuits", rw("no links here") == ("no links here", []))

# --- alias_conflicts ---------------------------------------------------------
root = vault()
check("a clean vault has no conflicts", wu.alias_conflicts(root) == [], wu.alias_conflicts(root))
page(root, "players", "Jacoby Lane")
c = wu.alias_conflicts(root)
check("an alias that is also a page is reported as an unmerged duplicate",
      len(c) == 1 and "Jacoby Lane" in c[0] and "unmerged duplicate" in c[0], c)
page(root, "players", "Rival Page", "[Jakobi Lane]")
c = wu.alias_conflicts(root)
check("an alias claimed by two pages is reported as ambiguous",
      any("claimed by 2 pages" in x for x in c), c)
tpl = root / "_templates" / "player.md"
tpl.parent.mkdir(exist_ok=True)
tpl.write_text("---\ntype: player\ntags: [player]\n---\n")
page(root, "players", "Template Clash", "[player]")
check("template filenames are not treated as pages",
      not any("'player'" in x for x in wu.alias_conflicts(root)))

# --- prompt formatting -------------------------------------------------------
al = {"Ja'Kobi Lane": ["Jacoby Lane", "Jakobi Lane"]}
check("with_aliases appends '(aka ...)' only where aliases exist",
      im.with_aliases(["Ja'Kobi Lane", "Plain Player"], al)
      == ["Ja'Kobi Lane (aka Jacoby Lane, Jakobi Lane)", "Plain Player"])
players, concepts = im.inventory_blocks(
    {"players": ["Ja'Kobi Lane", "Plain Player"], "concepts": ["Sacrificial X Receiver"], "aliases": al})
check("player block renders aliases", players == "Ja'Kobi Lane (aka Jacoby Lane, Jakobi Lane), Plain Player", players)
check("concept block is one entry per line", concepts == "  - Sacrificial X Receiver", concepts)
check("an inventory with no aliases key still renders",
      im.inventory_blocks({"players": ["A"], "concepts": []}) == ("A", "  (none yet)"))
check("the prompt instruction tells the agent how to read 'aka'",
      'after "aka"' in im.ALIAS_NOTE and "never" in im.ALIAS_NOTE)

shutil.rmtree(root.parent, ignore_errors=True)
print(f"\n{'FAILED' if fails else 'all passed'} ({fails} failure(s))")
sys.exit(1 if fails else 0)
