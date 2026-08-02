# fantasy-football-knowledge-base

An LLM-maintained Obsidian wiki of fantasy football advice, built from podcast
and media transcripts of select experts — in the spirit of Andrej Karpathy's
"LLM wiki" approach: small, atomic, densely cross-linked notes that Claude
writes and links as source material comes in.

Start at [Home.md](Home.md). See [CLAUDE.md](CLAUDE.md) for the wiki's
maintenance rules and how new transcripts get ingested.

## Structure
- `Experts/` — analyst/host notes: philosophy, track record, sources
- `Players/` — one note per player, aggregating dated, attributed takes
- `Concepts/` — strategy/scheme notes (e.g. Zero RB)
- `Formats/` — formats played, in priority order: Best Ball, Dynasty, Redraft (Standard)
- `Sources/` — one note per ingested transcript/appearance
- `Sources/_inbox/` — transcripts staged by the automated pipeline, awaiting ingestion
- `_templates/` — starting shape for each note type
- `Experts.md` / `Players.md` / `Concepts.md` / `Formats.md` / `Sources.md` — top-level indexes
- `scripts/` — the automated ingestion pipeline (see below)

## Automated ingestion pipeline

The wiki has a standing pipeline that watches for new episodes across all
tracked experts' shows and ingests their transcripts automatically. It runs
entirely on a local Mac — nothing about it depends on cloud infrastructure.
This section documents *why* it's built this way, in enough detail to tear it
down and rebuild it (on this machine or another) or to extend it to another
show.

Currently tracked, each configured as an entry in the `SHOWS` list at the top
of `scripts/check_new_episodes.py`:

| Show | Expert | Episode filtering |
|---|---|---|
| Reception Perception: The Show | Matt Harmon | Only `[FULL EPISODE]` titles — this feed also publishes short `RP Clips: ...` segments, which are excluded |
| Harris Fantasy Football Podcast | Chris Harris | Every episode — this feed doesn't split full episodes and clips |
| Matt Waldman's RSP Cast | Matt Waldman | Every episode — same, no clip-splitting |

Not every show needs a filter — the RP-specific `[FULL EPISODE]` convention
was a property of *that* feed, not a general rule. Confirm each new show's
actual title conventions in `ZMTEPISODE` before assuming one filtering
approach fits all (see "Recreating this for another show" below).

### The core problem: getting a transcript at all

The show's RSS feed (`https://rss.amperwave.net/v2/feed/audacynetwork/reception-perception-the-show`)
has no `<podcast:transcript>` tag — just an MP3 enclosure per episode. Several
options were investigated and rejected before landing on the current approach:

1. **Written transcripts elsewhere online** — none found for free. Audacy's
   show page, Yahoo Sports, and Matt Harmon's own `receptionperception.com`
   only have episode titles/summaries, not transcripts. Rephonic has them but
   gates access behind a paid plan; Metacast's page is blocked (403).
2. **YouTube auto-captions** (free, no API key, via the same mechanism the
   unofficial `youtube-transcript-api` uses) — technically real, but Google is
   actively blocking this specific scrape from datacenter/cloud IPs (see
   `jdepoix/youtube-transcript-api` issues #511 and #593), and it wasn't
   confirmed that full episodes — as opposed to clips — are consistently
   uploaded to Matt Harmon's channel (`@MattHarmonRP`). Rejected for
   reliability.
3. **Paid ASR** (transcribing the RSS audio directly via OpenAI/AssemblyAI/
   Deepgram) — fully reliable, works from anywhere including a cloud runner,
   ~$0.30–0.50/episode. **Explicitly declined** in favor of the free
   Apple-transcript route below (see "Should new episodes be pushed straight
   to the wiki..." decision point in project history — cost/complexity vs.
   the free option was a deliberate tradeoff, not an oversight).
4. **Apple's private live transcript API**
   (`amp-api.podcasts.apple.com/.../transcripts`, reachable by compiling a
   small tool that `dlopen`s Apple's private `PodcastsFoundation.framework`
   and signs requests via its internal `AMSMescal` class under a live,
   signed-in Apple ID session — see
   [dado3212/apple-podcast-transcript-downloader](https://github.com/dado3212/apple-podcast-transcript-downloader)).
   This works and doesn't require disabling SIP, but it's an undocumented,
   unsupported, version-fragile private API (confirmed working on macOS
   15.5, confirmed broken on 14.4.1), and using it means compiling and
   running third-party code that performs Apple-ID-authenticated requests
   through a reverse-engineered internal framework. **Rejected** — judged too
   risky/fragile for standing automation, in favor of:
5. **Passively reading Apple's own local transcript cache** — the approach
   actually used. See below.

### How the chosen method works

Since 2024, the Apple Podcasts app auto-generates transcripts for most
episodes and displays them in-app. Critically, once you're **subscribed to a
show in Podcasts.app on a given Mac**, two things happen automatically, with
no need to ever open an episode's Transcript tab:

1. **Metadata sync** populates a transcript identifier for each episode almost
   immediately, in the app's local library database.
2. **A background job** then asynchronously downloads the actual transcript
   file into a local cache — this can take anywhere from minutes to a couple
   of days per episode, and Apple doesn't expose control over the order/pace.

This means the whole pipeline is just **reading two things Apple's own app
already wrote to disk** — no network calls, no authentication, no reverse
engineering:

- **`~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts/Documents/MTLibrary.sqlite`**
  — a SQLite DB. Relevant tables/columns:
  - `ZMTPODCAST` — one row per subscribed show; matched by `ZTITLE = 'Reception Perception: The Show'`.
  - `ZMTEPISODE` — one row per episode (`ZPODCAST` foreign key). Key columns:
    `ZTITLE`, `ZSTORETRACKID` (Apple's numeric episode/track ID — the same ID
    that appears as `?i=<id>` in an episode's `podcasts.apple.com` URL),
    `ZPUBDATE` (Core Data reference date — seconds since 2001-01-01 00:00:00
    UTC, *not* Unix epoch), `ZGUID`, and `ZTRANSCRIPTIDENTIFIER` /
    `ZFREETRANSCRIPTIDENTIFIER` (non-null once the metadata sync above has run
    for that episode).
- **`~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts/Library/Cache/Assets/TTML/`**
  — the actual transcript files, once downloaded, nested under generated
  subfolders. The on-disk filename embeds the track ID
  (`transcript_<trackId>.ttml...`), but the path doesn't exactly match the
  `ZTRANSCRIPTIDENTIFIER` string — the pipeline globs for
  `*_<trackId>.ttml*` under this root rather than trusting an exact path.

**TTML structure**: each file is `<tt>` (namespaces `tt`, `ttm`, and a
show-specific `podcasts` namespace) → `<body><div>` → one `<p begin=".."
end=".." ttm:agent="SPEAKER_N">` per speaker turn → nested `<span
unit="sentence"><span unit="word">token</span>...</span>` leaves. **Speaker
labels are generic** (`SPEAKER_1`, `SPEAKER_2`, ...) with no name mapping
anywhere in the file, and the label→person mapping isn't guaranteed stable
across episodes — the ingestion step has to infer who's actually talking from
context each time.

**Full episode vs. clip filtering**: this show publishes both to the same
feed. Full episodes are titled `"[FULL EPISODE] ..."`; short clips are titled
`"RP Clips: ..."`. The pipeline queries `ZTITLE LIKE '[FULL EPISODE]%'`
(SQLite `LIKE` is case-insensitive for ASCII) and additionally skips anything
literally starting with `"RP Clips:"` as a second guard.

### Adding another show, or recreating this on another machine

Prerequisite: a Mac with Podcasts.app signed into an Apple ID that is
**subscribed to the target show**. Without a subscription, `ZMTPODCAST`/
`ZMTEPISODE` rows for it won't exist locally at all.

1. Subscribe to the show in Podcasts.app on that Mac. Wait for sync (metadata
   populates in minutes; TTML caching can take up to a couple of days per
   episode — there's no way to force it).
2. Check its actual episode title conventions before assuming a filter is
   needed:
   ```bash
   sqlite3 ~/"Library/Group Containers/243LU875E5.groups.com.apple.podcasts/Documents/MTLibrary.sqlite" \
     "SELECT ZTITLE FROM ZMTEPISODE WHERE ZPODCAST = (SELECT Z_PK FROM ZMTPODCAST WHERE ZTITLE = 'Exact Show Title') ORDER BY ZPUBDATE DESC LIMIT 20;"
   ```
   Most shows (like Harris Fantasy Football Podcast and Matt Waldman's RSP
   Cast) publish only full episodes to their feed, so `include_episode`
   should just be `lambda title: True`. Only add a title-based filter if the
   show actually mixes full episodes and clips/bonus content in one feed,
   the way Reception Perception does.
3. Add an entry to the `SHOWS` list at the top of
   `scripts/check_new_episodes.py` — `slug` (short, unique, used as a
   filename prefix), `podcast_title` (must exactly match `ZMTPODCAST.ZTITLE`),
   `expert_name`, `show_name`, `include_episode`, and `clean_title` (strip any
   title prefix that shouldn't appear in the wiki, or `lambda title: title.strip()`
   if there's nothing to strip).
4. If recreating on a different machine/user account, re-point the absolute
   paths in the two `.plist` files under `scripts/launchd/` and in
   `scripts/run_daily_check.sh` / `scripts/run_weekly_backup.sh`.

### Scheduling: local `launchd`, not Claude Code's cloud scheduling

Two Claude-native scheduling mechanisms were considered and rejected:

- **Claude Code cloud "routines"** (the `/schedule` skill, `RemoteTrigger`
  API) — these explicitly run in Anthropic's cloud sandbox and have **no
  access to local files**, per their own documentation. Since this entire
  pipeline depends on reading `~/Library/Group Containers/...`, a cloud
  routine can't run any part of it.
- **`CronCreate`** — session-scoped only; the job is deleted when the Claude
  session ends, and auto-expires after 7 days regardless. Not durable enough
  for standing infrastructure.

Instead, this uses **macOS `launchd`** (the modern replacement for `cron`) —
runs locally, persists across reboots and Claude sessions, no expiry. Two
independent `LaunchAgent`s, canonical copies tracked in
`scripts/launchd/*.plist`, installed into `~/Library/LaunchAgents/`:

| Job | Label | Schedule | What it runs |
|---|---|---|---|
| Daily check + ingest | `com.kylecooper.fantasy-wiki-daily-check` | Every day, 12:00 PM local | `scripts/run_daily_check.sh` |
| Weekly git backup | `com.kylecooper.fantasy-wiki-weekly-backup` | Sundays, 5:00 PM local | `scripts/run_weekly_backup.sh` |

**`run_daily_check.sh`** runs `scripts/check_new_episodes.py` (pure Python
3, stdlib only — no pip dependencies) to update `scripts/state.json` and
stage any newly-available transcripts into `Sources/_inbox/`. If anything
landed there, it then invokes `claude -p "..."` — Claude Code's headless
mode, running locally in the repo so it picks up `CLAUDE.md` automatically —
to do the actual wiki-writing ingestion. **No git commands run here.**

**`run_weekly_backup.sh`** is deliberately trivial and fully decoupled from
ingestion: `git add -A && git commit && git push`, nothing else. This
separation (ingestion never touches git; git backup never touches ingestion
logic) was an explicit design decision, not an accident.

To reinstall on a fresh machine:
```bash
cp scripts/launchd/*.plist ~/Library/LaunchAgents/
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.kylecooper.fantasy-wiki-daily-check.plist
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.kylecooper.fantasy-wiki-weekly-backup.plist
```
To uninstall: `launchctl bootout "gui/$(id -u)/<label>"`, then delete the
`.plist` from `~/Library/LaunchAgents/`.

### Pipeline state & recovery

`scripts/state.json` tracks every episode by Apple track ID:
`pending` (seen, no transcript cached yet) → `fetched` (transcript staged in
`Sources/_inbox/`) → `ingested` (fully woven into the wiki; set by Claude, not
the script, once it's done processing a staged file). A `monitoring_since`
date anchors flagging: only episodes **published on or after** that date are
eligible to be flagged as overdue — pre-existing backlog episodes (hundreds of
them, going back years) retry passively forever without ever flagging, since
Apple may never backfill transcripts that far back and that's not an
actionable signal.

An episode published since `monitoring_since` whose transcript still hasn't
appeared after **2 days** gets logged to `Sources/_needs-attention.md` by the
script (not by Claude) — this is a visibility flag, not a dead end; checking
continues automatically every day regardless.
