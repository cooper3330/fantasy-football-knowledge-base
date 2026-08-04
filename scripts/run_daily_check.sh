#!/bin/bash
# Daily transcript check + ingestion. Never runs git commands -- the weekly
# backup job (run_weekly_backup.sh) is intentionally independent of this.
set -uo pipefail

REPO_DIR="/Users/kylecooper/dev/fantasy-football-knowledge-base"
cd "$REPO_DIR"

LOG_DIR="scripts/logs"
mkdir -p "$LOG_DIR"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

# --oldest is deliberate: expert opinions evolve, and the wiki accumulates
# dated takes per player. Processing oldest -> newest means later (more
# current) takes are always appended after earlier ones, so a stale 2024
# opinion can never land on top of a fresher 2026 one.
#
# --limit caps the run so the daily job can never turn into a multi-hour
# backlog drain.
#
# NOTE: this ordering assumes the back catalog has already been drained by
# drain_backlog.sh. With a large backlog still pending, oldest-first means
# newly published episodes wait behind it.
{
  echo "=== $TS: check_new_episodes.py ==="
  /usr/bin/python3 scripts/check_new_episodes.py --oldest --limit 10
} >> "$LOG_DIR/daily.log" 2>&1

# state.json is the authoritative queue, not the directory listing: a transcript
# on disk under raw/transcripts/ with status already `ingested` would be drift,
# and verify_integrity.py -- not this job -- is what repairs that.
QUEUE="$(/usr/bin/python3 -c "
import json, pathlib
s = json.loads(pathlib.Path('scripts/state.json').read_text())
print(sum(1 for v in s['episodes'].values() if v.get('status') == 'fetched'))
" 2>/dev/null)"

if [ "${QUEUE:-0}" -gt 0 ]; then
  # ingest_manifest.py builds the whole prompt -- schema pointer, ordering rule,
  # co-host roster, existing-page inventory, the 8 ingest steps, and the hard
  # no-git constraint -- so there is nothing to restate inline here. Its
  # diagnostics go to stderr, so this captures only the prompt.
  #
  # --model sonnet is the single biggest cost lever in the pipeline (CLAUDE.md,
  # "Model and batch size"); --count 3 keeps an unattended run bounded and gives
  # the last transcript in the batch a clean context.
  PROMPT="$(/usr/bin/python3 scripts/ingest_manifest.py --count 3 2>/dev/null)"
  {
    echo "=== $TS: claude -p ingestion ($QUEUE awaiting, taking 3) ==="
    /Users/kylecooper/.local/bin/claude -p "$PROMPT" \
      --model sonnet \
      --output-format text
    echo "=== $TS: post-ingest integrity ==="
    /usr/bin/python3 scripts/verify_integrity.py
    # Frontmatter is the vault's query layer; an agent that skips it produces
    # pages that look fine in prose and are invisible to every tag/Dataview
    # query. Unattended runs have nobody watching, so check it here.
    /usr/bin/python3 scripts/lint_frontmatter.py
  } >> "$LOG_DIR/daily.log" 2>&1
else
  echo "=== $TS: nothing awaiting ingestion, skipping ===" >> "$LOG_DIR/daily.log"
fi
