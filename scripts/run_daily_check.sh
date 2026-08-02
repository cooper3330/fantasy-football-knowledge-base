#!/bin/bash
# Daily transcript check + ingestion. Never runs git commands -- the weekly
# backup job (run_weekly_backup.sh) is intentionally independent of this.
set -uo pipefail

REPO_DIR="/Users/kylecooper/dev/fantasy-football-knowledge-base"
cd "$REPO_DIR"

LOG_DIR="scripts/logs"
mkdir -p "$LOG_DIR"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

{
  echo "=== $TS: check_new_episodes.py ==="
  /usr/bin/python3 scripts/check_new_episodes.py
} >> "$LOG_DIR/daily.log" 2>&1

if [ -n "$(ls -A Sources/_inbox 2>/dev/null)" ]; then
  {
    echo "=== $TS: claude -p ingestion ==="
    /Users/kylecooper/.local/bin/claude -p \
      "Check Sources/_inbox for staged transcripts and ingest each one into the wiki per CLAUDE.md. Do not run any git commands." \
      --output-format text
  } >> "$LOG_DIR/daily.log" 2>&1
else
  echo "=== $TS: nothing staged, skipping ingestion ===" >> "$LOG_DIR/daily.log"
fi
