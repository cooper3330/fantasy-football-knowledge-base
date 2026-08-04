#!/bin/bash
# Daily transcript check + ingestion. Never runs git commands -- the weekly
# backup job (run_weekly_backup.sh) is intentionally independent of this.
set -uo pipefail

REPO_DIR="/Users/kylecooper/dev/fantasy-football-knowledge-base"
cd "$REPO_DIR"

# Detach stdin. Same reasoning as drain_backlog.sh: nohup/launchd block SIGHUP
# but nothing stops SIGTTIN from suspending the job if anything reads the tty.
exec < /dev/null

LOG_DIR="scripts/logs"
mkdir -p "$LOG_DIR"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

CLAUDE_BIN="${CLAUDE_BIN:-/Users/kylecooper/.local/bin/claude}"
PY="/usr/bin/python3"

# How many episodes to ingest per run. Each is a SEPARATE `claude -p` process,
# so this is NOT the batching that CLAUDE.md forbids -- see the loop below.
INGEST_PER_RUN="${INGEST_PER_RUN:-3}"

# Per-episode wall-clock ceiling, seconds. Episodes run ~10-20 min; an hour
# means something is wrong, not slow.
EPISODE_TIMEOUT="${EPISODE_TIMEOUT:-3600}"

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
#
# SKIP_FETCH=1 skips this step. Use it when drain_backlog.sh is already
# running: both call check_new_episodes.py, and while state.json writes are
# locked, nothing stops the two from downloading and transcribing the same
# episode simultaneously and throwing one of the results away.
if [ "${SKIP_FETCH:-0}" = "1" ]; then
  echo "=== $TS: SKIP_FETCH=1, not fetching ===" >> "$LOG_DIR/daily.log"
else
  {
    echo "=== $TS: check_new_episodes.py ==="
    $PY scripts/check_new_episodes.py --oldest --limit 10
  } >> "$LOG_DIR/daily.log" 2>&1
fi

# state.json is the authoritative queue, not the directory listing: a transcript
# on disk under raw/transcripts/ with status already `ingested` would be drift,
# and verify_integrity.py -- not this job -- is what repairs that.
queue_depth() {
  $PY -c "
import json, pathlib
s = json.loads(pathlib.Path('scripts/state.json').read_text())
print(sum(1 for v in s['episodes'].values() if v.get('status') == 'fetched'))
" 2>/dev/null
}

# The guid ingest_manifest.py will pick next. Sort key MUST match its
# load_queue() exactly, or the stall check below compares the wrong episode.
next_guid() {
  $PY -c "
import json, pathlib
s = json.loads(pathlib.Path('scripts/state.json').read_text())
eps = [v for v in s['episodes'].values() if v.get('status') == 'fetched']
eps.sort(key=lambda v: (v.get('pub_date') or '', v.get('title') or ''))
print(eps[0].get('guid', '') if eps else '')
" 2>/dev/null
}

QUEUE="$(queue_depth)"
if [ "${QUEUE:-0}" -eq 0 ]; then
  echo "=== $TS: nothing awaiting ingestion, skipping ===" >> "$LOG_DIR/daily.log"
  exit 0
fi

{
  echo "=== $TS: ingestion ($QUEUE awaiting, taking up to $INGEST_PER_RUN) ==="

  for i in $(seq 1 "$INGEST_PER_RUN"); do
    BEFORE_GUID="$(next_guid)"
    if [ -z "$BEFORE_GUID" ]; then
      echo "--- queue empty after $((i - 1)) episode(s); stopping ---"
      break
    fi

    # Regenerated EVERY iteration, not hoisted out of the loop. Two reasons:
    #   1. It selects the next episode -- a hoisted prompt would re-ingest the
    #      same one N times.
    #   2. It inlines the current page inventory. Episode N-1 may have just
    #      created "Brock Bowers"; agent N has to see that to update it rather
    #      than create a near-duplicate page.
    PROMPT="$($PY scripts/ingest_manifest.py --count 1 2>/dev/null)"

    echo "--- [$i/$INGEST_PER_RUN] $BEFORE_GUID ---"

    # A fresh process per episode. This is what makes the isolation real: no
    # --continue and no --resume, so each agent starts with an empty context
    # and carries nothing from the episode before it.
    #
    # --agent ingest restricts the tool surface to Read/Write/Edit/Bash. An
    # unrestricted agent loads ~44.6k tokens of system prompt and tool schemas
    # (browsers, computer-use, mail, calendar) before doing any work, and
    # re-reads that constant every turn.
    #
    # --model sonnet is the single biggest cost lever in the pipeline; see
    # CLAUDE.md "Model and batch size (cost)".
    # Watchdog. macOS ships no `timeout`, and an unattended run has nobody to
    # notice a hang -- an un-allow-listed Bash call waits on a permission
    # prompt that will never come. Without this the job blocks indefinitely
    # and the next day's run finds it still holding the queue.
    "$CLAUDE_BIN" -p "$PROMPT" \
      --agent ingest \
      --model sonnet \
      --output-format text &
    CPID=$!
    # Polls rather than one long `sleep`, and exits on its own the moment
    # claude finishes. Killing a subshell does NOT kill the `sleep` it is
    # blocked on -- that child is reparented and keeps running, so the naive
    # `(sleep N; kill) &` idiom leaks one stray process per episode.
    (
      for _ in $(seq 1 "$EPISODE_TIMEOUT"); do
        sleep 1
        kill -0 "$CPID" 2>/dev/null || exit 0
      done
      echo "!!! episode exceeded ${EPISODE_TIMEOUT}s -- killing claude !!!"
      kill -TERM "$CPID" 2>/dev/null
    ) &
    WPID=$!
    wait "$CPID"; RC=$?
    wait "$WPID" 2>/dev/null

    # Verify BETWEEN episodes, not just at the end: a corrupt state or a
    # half-moved transcript should stop the run, not be compounded by two more
    # agents writing on top of it.
    if ! $PY scripts/verify_integrity.py; then
      echo "!!! verify_integrity failed after episode $i -- stopping run !!!"
      break
    fi

    # Stall guard. If the agent errored, or finished without setting the status
    # to `ingested`, the queue head is unchanged and the next iteration would
    # hand the identical transcript to a new agent -- burning the full run on
    # one poison episode, repeatedly, unattended. Bail instead.
    if [ "$(next_guid)" = "$BEFORE_GUID" ]; then
      echo "!!! queue head unchanged after episode $i (claude rc=$RC) -- stopping run !!!"
      break
    fi
  done

  echo "=== $TS: post-ingest checks ==="
  $PY scripts/verify_integrity.py
  # Frontmatter is the vault's query layer; an agent that skips it produces
  # pages that look fine in prose and are invisible to every tag/Dataview
  # query. Unattended runs have nobody watching, so check it here.
  $PY scripts/lint_frontmatter.py
} >> "$LOG_DIR/daily.log" 2>&1
