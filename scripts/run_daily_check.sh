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

if [ -n "$(ls -A Sources/_inbox 2>/dev/null)" ]; then
  {
    echo "=== $TS: claude -p ingestion ==="
    /Users/kylecooper/.local/bin/claude -p \
      "Check Sources/_inbox for staged transcripts and ingest them into the wiki per CLAUDE.md. IMPORTANT: process them strictly in chronological order, oldest episode first (the filenames are date-prefixed, so sorting by filename gives the right order). Expert opinions evolve, so newer takes must be appended after older ones. Do not run any git commands." \
      --output-format text
  } >> "$LOG_DIR/daily.log" 2>&1
else
  echo "=== $TS: nothing staged, skipping ingestion ===" >> "$LOG_DIR/daily.log"
fi
