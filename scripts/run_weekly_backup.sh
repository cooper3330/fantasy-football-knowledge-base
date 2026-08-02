#!/bin/bash
# Weekly git backup. Intentionally independent of the daily ingestion job --
# just snapshots whatever's accumulated in the working tree.
set -uo pipefail

REPO_DIR="/Users/kylecooper/dev/fantasy-football-knowledge-base"
cd "$REPO_DIR"

LOG_DIR="scripts/logs"
mkdir -p "$LOG_DIR"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

{
  echo "=== $TS: weekly git backup ==="
  /usr/bin/git add -A
  if /usr/bin/git diff --cached --quiet; then
    echo "Nothing to commit."
  else
    /usr/bin/git commit -m "Weekly backup: $TS"
    /usr/bin/git push origin main
  fi
} >> "$LOG_DIR/weekly.log" 2>&1
