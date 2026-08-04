#!/usr/bin/env python3
"""
Reports what an ingest subagent actually cost, from its own transcript.

WHY: the token total shown in tool output is misleading -- it excludes cached
input, which is ~92% of the tokens an agent consumes. A run reported as "149k
tokens" really moved ~9.1M. Any tuning done against the reported number is
tuning against noise.

The real cost model is:

    cost ~= turns x context size at each turn

An agent re-reads its whole conversation every turn. Caching makes those reads
10x cheaper, not free, so the only two levers are FEWER TURNS and SMALLER
CONTEXT. There is no third lever -- the cache hit rate is already ~93% and has
no knob.

Weighting matters when comparing runs. Cache writes cost 1.25x base input and
cache reads 0.10x, a 12.5x spread, so a component that is 7% of token volume can
be 42% of cost. This script reports both.

Usage:
  agent_cost.py                    # every agent in the current session, newest first
  agent_cost.py --session <id>     # a specific session directory
  agent_cost.py --agent <agentId>  # one agent
  agent_cost.py --limit 5
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"
# Relative to base input = 1.0.
WEIGHTS = {
    "input_tokens": 1.0,
    "cache_creation_input_tokens": 1.25,
    "cache_read_input_tokens": 0.10,
    "output_tokens": 5.0,
}
LABEL = {
    "cache_read_input_tokens": "cache read",
    "cache_creation_input_tokens": "cache write",
    "output_tokens": "output",
    "input_tokens": "fresh input",
}


def project_dir():
    """The projects subdir for this repo, named after its path with / as -."""
    repo = Path(__file__).resolve().parent.parent
    return PROJECTS / str(repo).replace("/", "-")


def sessions(root):
    return sorted((p for p in root.glob("*/subagents") if p.is_dir()),
                  key=lambda p: p.stat().st_mtime, reverse=True)


def analyze(path):
    tot, tools, turns, ctx = Counter(), Counter(), 0, []
    for line in path.read_text(errors="ignore").splitlines():
        try:
            o = json.loads(line)
        except Exception:
            continue
        msg = o.get("message") or {}
        usage = msg.get("usage") or o.get("usage")
        if isinstance(usage, dict) and any(usage.get(k) for k in WEIGHTS):
            turns += 1
            for k in WEIGHTS:
                tot[k] += usage.get(k) or 0
            ctx.append((usage.get("cache_read_input_tokens") or 0)
                       + (usage.get("cache_creation_input_tokens") or 0))
        content = msg.get("content")
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    tools[c.get("name")] += 1
    return tot, tools, turns, ctx


def report(path, tot, tools, turns, ctx):
    volume = sum(tot.values())
    cost = sum(tot[k] * WEIGHTS[k] for k in WEIGHTS)
    if not volume:
        return
    print(f"\n{path.stem}")
    print(f"  turns {turns:<5} tool calls {sum(tools.values()):<5} "
          f"{dict(tools.most_common(6))}")
    if ctx:
        peak = max(ctx)
        print(f"  context: first {ctx[0]:,} -> peak {peak:,} "
              f"(median {sorted(ctx)[len(ctx) // 2]:,})")
        writes = tot["cache_creation_input_tokens"]
        if peak:
            # 1.0x means the cache was built once and never rebuilt. Materially
            # above that means it expired or was invalidated mid-run, and every
            # rebuild is charged at the 1.25x write rate.
            print(f"  cache rebuilt {writes / peak:.1f}x over the run "
                  f"(1.0x = built once)")
    print(f"    {'component':<14}{'tokens':>12}{'%vol':>8}{'cost':>12}{'%cost':>8}")
    for k in ("cache_read_input_tokens", "cache_creation_input_tokens",
              "output_tokens", "input_tokens"):
        print(f"    {LABEL[k]:<14}{tot[k]:>12,}{100 * tot[k] / volume:>7.1f}%"
              f"{tot[k] * WEIGHTS[k]:>12,.0f}{100 * tot[k] * WEIGHTS[k] / cost:>7.1f}%")
    print(f"    {'TOTAL':<14}{volume:>12,}{'':>8}{cost:>12,.0f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session")
    ap.add_argument("--agent")
    ap.add_argument("--limit", type=int, default=8)
    args = ap.parse_args()

    root = project_dir()
    if not root.exists():
        sys.exit(f"no transcripts at {root}")

    dirs = [root / args.session / "subagents"] if args.session else sessions(root)
    if not dirs:
        sys.exit("no subagent transcripts found")

    files = []
    for d in dirs:
        if d.is_dir():
            files += sorted(d.glob("agent-*.jsonl"),
                            key=lambda p: p.stat().st_mtime, reverse=True)
    if args.agent:
        files = [f for f in files if args.agent in f.stem]
    if not files:
        sys.exit("no matching agent transcripts")

    shown = 0
    for f in files:
        tot, tools, turns, ctx = analyze(f)
        if not sum(tot.values()):
            continue
        report(f, tot, tools, turns, ctx)
        shown += 1
        if shown >= args.limit:
            break
    print("\ncost units are relative to base input (cache write 1.25x, "
          "cache read 0.10x, output 5x).")


if __name__ == "__main__":
    main()
