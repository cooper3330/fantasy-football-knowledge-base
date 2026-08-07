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

# Pinned, not the `sonnet` alias: the alias tracks whatever the latest Sonnet is,
# so a model release would silently change ingest cost and output shape mid-
# backlog. Bump this deliberately.
INGEST_MODEL="${INGEST_MODEL:-claude-sonnet-5}"

# Extraction against a schema this explicit is not a reasoning-heavy task -- the
# prompt already names the steps. Effort buys thinking tokens, which are output
# tokens at 5x base input, and they compound: every turn re-reads them.
INGEST_EFFORT="${INGEST_EFFORT:-medium}"

# legacy: one agent reads the transcript AND writes the wiki across ~66 turns.
# extract: the agent emits a JSON plan (phase A) and apply_ingest.py writes it
# for zero tokens (phase B). See docs/ingest-v2-plan.md.
#
# Validated 2026-08-05 over 4 applied episodes plus a 2-episode A/B against
# legacy on identical transcripts: 5 turns and ~346k cost units per episode
# against a 2.88M legacy baseline (88% lower), at 1.09x legacy content volume.
# `legacy` is kept as a one-env-var fallback, not because it is expected to be
# needed.
INGEST_MODE="${INGEST_MODE:-extract}"
PLAN_DIR="${PLAN_DIR:-scripts/logs/plans}"
mkdir -p "$PLAN_DIR"

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

# The next fetched guid in ingest order (oldest-first), EXCLUDING any guids
# passed as arguments. The sort key MUST match ingest_manifest.load_queue().
#
# The exclusion is what makes skip-and-continue possible: when an episode fails,
# the loop adds its guid here so selection moves past it to the next good one,
# instead of handing the same poison episode to every remaining iteration. This
# is only safe because the applier inserts bullets by date -- ingesting a later
# episode before an earlier one no longer breaks chronology (rule 4).
next_guid() {  # $@ = guids to skip
  SKIP="$*" $PY -c "
import json, os, pathlib
skip = set(os.environ.get('SKIP', '').split())
s = json.loads(pathlib.Path('scripts/state.json').read_text())
eps = [v for v in s['episodes'].values()
       if v.get('status') == 'fetched' and v.get('guid') not in skip]
eps.sort(key=lambda v: (v.get('pub_date') or '', v.get('title') or ''))
print(eps[0].get('guid', '') if eps else '')
" 2>/dev/null
}

# Detect a partial write: state.json still calls this episode `fetched`, but the
# wiki already carries content from it. A failed agent is rarely a no-op -- it
# typically dies AFTER writing bullets to 10-40 pages and BEFORE setting the
# status, so re-ingesting appends every one of those bullets a second time.
#
# Checked BEFORE each episode, not only after a failure. Stopping the failed run
# was never the fix: the damage is done by the NEXT run, and unattended there is
# nobody reading the last one's log.
#
# Do NOT gate this on "no source page exists" -- that was the original bug. An
# agent that got far enough to write its source page and then died still leaves a
# partial write, and the source page made it look finished. If state says
# `fetched`, NOTHING in wiki/ should reference the episode.
# See scripts/partial_write_check.py -- the detection rules and the two ways
# they have previously been wrong are documented there. Exit 2 = partial write.
partial_write() {
  $PY scripts/partial_write_check.py --guid "$1"
  [ $? -eq 2 ]
}

# Run one agent under the watchdog and return its exit code. macOS ships no
# `timeout`, and an unattended run has nobody to notice a hang -- an
# un-allow-listed Bash call waits on a permission prompt that never comes.
#
# The watchdog polls rather than using one long `sleep`: killing a subshell does
# NOT kill the `sleep` it is blocked on -- that child is reparented and keeps
# running, so the naive `(sleep N; kill) &` idiom leaks one stray process per
# episode.
run_agent() {  # $1 = prompt, $2 = agent name
  "$CLAUDE_BIN" -p "$1" \
    --agent "$2" \
    --model "$INGEST_MODEL" \
    --effort "$INGEST_EFFORT" \
    --output-format text &
  local cpid=$!
  (
    for _ in $(seq 1 "$EPISODE_TIMEOUT"); do
      sleep 1
      kill -0 "$cpid" 2>/dev/null || exit 0
    done
    echo "!!! episode exceeded ${EPISODE_TIMEOUT}s -- killing claude !!!"
    kill -TERM "$cpid" 2>/dev/null
  ) &
  local wpid=$!
  wait "$cpid"; local rc=$?
  wait "$wpid" 2>/dev/null
  return $rc
}

QUEUE="$(queue_depth)"
if [ "${QUEUE:-0}" -eq 0 ]; then
  echo "=== $TS: nothing awaiting ingestion, skipping ===" >> "$LOG_DIR/daily.log"
  exit 0
fi

{
  echo "=== $TS: ingestion ($QUEUE awaiting, target $INGEST_PER_RUN) ==="

  # INGEST_PER_RUN counts SUCCESSES, not attempts. An episode that fails after
  # its one retry is added to SKIPPED and the run moves on to the next, rather
  # than stalling every remaining episode on one poison transcript. SKIPPED
  # episodes stay `fetched` and are retried on a later run; because the applier
  # inserts bullets by date, ingesting them out of order does not break rule 4.
  DONE=0
  SKIPPED=""
  while [ "$DONE" -lt "$INGEST_PER_RUN" ]; do
    GUID="$(next_guid $SKIPPED)"
    if [ -z "$GUID" ]; then
      echo "--- no more ingestable episodes (${DONE} done, skipped:$(echo $SKIPPED | wc -w | tr -d ' ')) ---"
      break
    fi

    # A partial write from a prior crashed run must be cleaned before we touch
    # this episode; re-ingesting on top of it would duplicate bullets. This is
    # the one condition that stops the whole run -- it needs a human.
    if partial_write "$GUID"; then
      echo "!!! refusing to continue -- clean up the partial write first !!!"
      break
    fi

    N=$((DONE + 1))
    echo "--- [$N/$INGEST_PER_RUN] $GUID ($INGEST_MODE) ---"

    # A fresh `claude -p` per episode is what makes the isolation real: no
    # --continue, no --resume, so each agent starts empty and carries nothing
    # from the episode before it. The prompt is regenerated per episode so it
    # inlines the CURRENT page inventory -- episode N-1 may have just created
    # "Brock Bowers", and agent N must see that to update rather than duplicate.
    # --agent restricts the tool surface (extract = Read/Write only); --model and
    # --effort are the two biggest cost levers (CLAUDE.md "Model and batch size").
    if [ "$INGEST_MODE" = "extract" ]; then
      # Phase A emits a plan; apply_ingest.py (phase B) writes the wiki after
      # validating the whole plan, so a bad plan costs only the extraction.
      # Exit codes: 0 applied; 2 validation rejection; 3 missing/unparseable plan.
      # Both failure modes are often a stochastic slip (a dropped citation, an
      # unescaped quote), so retry ONCE on either before giving up on the episode.
      ARC=1
      for attempt in 1 2; do
        PLAN="$PLAN_DIR/plan-$$-$N-$attempt.json"
        rm -f "$PLAN"
        PROMPT="$($PY scripts/ingest_manifest.py --guid "$GUID" --mode extract \
                      --plan-out "$PLAN" 2>/dev/null)"
        [ "$attempt" -eq 2 ] && echo "--- re-extracting: previous plan was rejected/unusable ---"
        run_agent "$PROMPT" extract; RC=$?
        $PY scripts/apply_ingest.py "$PLAN"; ARC=$?
        [ "$ARC" -eq 0 ] && break
      done
    else
      PROMPT="$($PY scripts/ingest_manifest.py --guid "$GUID" 2>/dev/null)"
      run_agent "$PROMPT" ingest; RC=$?
      ARC=0   # legacy agent writes directly; success is judged by the queue move below
    fi

    # verify_integrity between episodes: corrupt state or a half-moved transcript
    # must stop the run, not be compounded by writing more on top of it.
    if ! $PY scripts/verify_integrity.py; then
      echo "!!! verify_integrity failed after $GUID -- stopping run !!!"
      break
    fi

    # Did this episode actually leave the queue? If the guid is still fetched, the
    # ingest did not take (a rejection that survived the retry, or a legacy agent
    # that died).
    if [ "$(next_guid $SKIPPED)" = "$GUID" ]; then
      # A clean rejection writes nothing (apply_ingest validates first), so it is
      # safe to skip and continue. A PARTIAL write -- content on disk from an
      # episode still marked `fetched` -- is not: re-ingesting it later duplicates
      # bullets, so it needs a human. That is the one thing that stops the run.
      if partial_write "$GUID"; then
        echo "!!! $GUID left a PARTIAL WRITE -- stopping the run for cleanup !!!"
        break
      fi
      echo "!!! $GUID did not ingest (rc=$RC, apply=$ARC), nothing written -- skipping it !!!"
      SKIPPED="$SKIPPED $GUID"
      continue
    fi
    DONE=$((DONE + 1))
  done
  echo "--- run complete: $DONE ingested$([ -n "$SKIPPED" ] && echo ", skipped:$SKIPPED") ---"

  echo "=== $TS: post-ingest checks ==="
  $PY scripts/verify_integrity.py
  # Frontmatter is the vault's query layer; an agent that skips it produces
  # pages that look fine in prose and are invisible to every tag/Dataview
  # query. Unattended runs have nobody watching, so check it here.
  $PY scripts/lint_frontmatter.py
} >> "$LOG_DIR/daily.log" 2>&1
