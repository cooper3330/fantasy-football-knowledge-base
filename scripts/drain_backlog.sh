#!/bin/bash
# One-time backlog drain: transcribes every pending episode across all tracked
# shows, oldest first, using local whisper.cpp.
#
# This is deliberately SEPARATE from the daily job (run_daily_check.sh), which
# is capped at --limit 10 so it can never turn into a multi-hour run.
#
# Safe to interrupt: scripts/check_new_episodes.py checkpoints state.json after
# every single episode, so re-running this picks up exactly where it left off.
# It does NOT ingest into the wiki and does NOT touch git -- it only stages
# transcripts into raw/transcripts/<show>/ for later ingestion.
#
# Logs to scripts/logs/daily.log -- the same stream as the scheduled daily job,
# so all pipeline activity is readable in one place. Drain runs are wrapped in
# BACKLOG DRAIN banners to stay distinguishable from routine daily runs.
#
# Usage:
#   ./scripts/drain_backlog.sh            # drain everything
#   ./scripts/drain_backlog.sh 50         # drain at most 50 episodes this run
#
# Recommended for a long run (survives terminal close):
#   nohup ./scripts/drain_backlog.sh 50 > /dev/null 2>&1 &
#   tail -f scripts/logs/daily.log

set -uo pipefail

REPO_DIR="/Users/kylecooper/dev/fantasy-football-knowledge-base"
cd "$REPO_DIR" || exit 1

LOG_DIR="scripts/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/daily.log"

LIMIT_ARG=""
if [ "$#" -ge 1 ]; then
  LIMIT_ARG="--limit $1"
fi

{
  echo ""
  echo "==================== BACKLOG DRAIN START ===================="
  echo "$(date '+%Y-%m-%d %H:%M:%S')  args: --oldest ${LIMIT_ARG:-(no limit)}"
  echo "============================================================"
} >> "$LOG"

# `nice` keeps the machine responsive for interactive use while this grinds.
nice -n 10 /usr/bin/python3 scripts/check_new_episodes.py --oldest $LIMIT_ARG \
  >> "$LOG" 2>&1
RC=$?

{
  echo "==================== BACKLOG DRAIN END ======================"
  echo "$(date '+%Y-%m-%d %H:%M:%S')  exit=$RC"
  echo "============================================================"
} >> "$LOG"
