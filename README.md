# fantasy-football-knowledge-base

An LLM-maintained Obsidian wiki of fantasy football analysis, built from the
podcast transcripts of three trusted analysts and structured after Andrej
Karpathy's [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern.

**Purpose:** answer real draft and waiver-wire questions — comparing players
across Best Ball, Dynasty, and Redraft formats — grounded in what specific
analysts actually said, with dates and citations.

Start at [index.md](index.md). See [CLAUDE.md](CLAUDE.md) for the schema and
workflows, and [log.md](log.md) for the operation history.

## Structure

Follows Andrej Karpathy's [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
three-layer pattern:

```
index.md              catalog of every wiki page (retrieval entry point)
log.md                append-only record of ingests / queries / lints
CLAUDE.md             the schema: conventions + workflows

raw/                  LAYER 1 - immutable sources, never edited
  transcripts/
    reception-perception/
    harris-football/
    rsp-cast/
  _needs-attention.md source-acquisition failures

wiki/                 LAYER 2 - LLM-owned
  players/            one page per NFL player
  experts/            one page per tracked analyst
  concepts/           strategy / scheme pages
  formats/            Best Ball, Dynasty, Redraft (Standard)
  sources/            per-episode summaries + SOURCE_CATALOG.md
  synthesis/          filed answers to recurring draft/waiver questions
  _templates/         starting shapes for each page type

scripts/              transcription pipeline + state.json
```

Key property: raw transcripts are written once into `raw/` and **never move**.
Ingestion status lives in `scripts/state.json`, not in a file's location — so no
transcript can be lost to a failed or partial move.

## Automated ingestion pipeline

The wiki has a standing pipeline that watches for new episodes across all
tracked experts' shows and ingests their transcripts automatically. It runs
entirely on a local Mac — nothing about it depends on cloud infrastructure.
This section documents *why* it's built this way, in enough detail to tear it
down and rebuild it (on this machine or another) or to extend it to another
show.

Currently tracked, each configured as an entry in the `SHOWS` list at the top
of `scripts/check_new_episodes.py`:

| Show | Expert | Feed | Episode filtering |
|---|---|---|---|
| Reception Perception: The Show | Matt Harmon | `feeds.megaphone.fm/reception-perception-the-show` | Only `[FULL EPISODE]` titles — this feed also publishes short `RP Clips: ...` segments, which are excluded |
| Harris Fantasy Football Podcast | Chris Harris | `harrisfootball.libsyn.com/rss` | Every episode — no clip-splitting |
| Matt Waldman's RSP Cast | Matt Waldman | `mattwaldmanrsp.com/feed/podcast/` | Every episode — same, no clip-splitting |

Not every show needs a filter — the RP-specific `[FULL EPISODE]` convention
was a property of *that* feed, not a general rule. Confirm each new show's
actual title conventions in its feed before assuming one filtering approach
fits all (see "Adding another show" below).

### How it works

The pipeline reads each show's **public RSS feed** and transcribes every
episode with [whisper.cpp](https://github.com/ggerganov/whisper.cpp)
(`large-v3-turbo`) run locally on the episode's public MP3 enclosure — the same
file any podcast client downloads. Free, offline, no API key, no account.

A second path exists for `<podcast:transcript>` feed tags (SRT/VTT/plain text),
but it is **off by default** (`PREFER_FEED_TRANSCRIPTS = False`). The only such
transcripts across these three shows are 8 RSP Cast episodes from a July 2024
Blubrry auto-transcription trial, and measurement showed their ASR is
noticeably *worse* than local Whisper — the Blubrry text renders "Matt Waldman"
(the host's own name) as "about Wall" and "Matt W", where Whisper gets it right.
Since this wiki is keyed on correctly-spelled proper nouns, uniform
higher-quality output is worth ~2 min of compute per episode. Flip the constant
to `True` if a show ever publishes genuine human-written transcripts, which
would beat any ASR. The feed path is also used automatically for any episode
that has a transcript tag but no audio enclosure.

Measured on this Mac (M4 Pro, 12 cores, 24 GB): a **76-minute episode
transcribes in ~3 minutes**, roughly 24× realtime, using the Metal GPU backend.
Audio is downloaded to a temp dir and deleted immediately after — nothing
persists but the text.

Setup (one-time):

```bash
brew install whisper-cpp ffmpeg
mkdir -p ~/.local/share/whisper-models
curl -L -o ~/.local/share/whisper-models/ggml-large-v3-turbo.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
```

**Known quality characteristics** (both are recorded in `CLAUDE.md` so the
ingestion step compensates):

- **No speaker diarization.** Neither source labels speakers; the ingestion
  step infers speakers from context.
- **Capitalization/punctuation drifts** on long episodes — Whisper oscillates
  between properly-cased and lowercase passages. This is inherent long-form
  behavior, *not* fixable via `--max-context 0` or `--carry-initial-prompt`
  (both tested; the latter produced byte-identical output). **Content accuracy
  is unaffected** — lowercase passages are as accurate as the rest.
- **Proper-noun errors** are the one thing that genuinely matters here, since
  the wiki is keyed on player names. Observed: "Malik neighbors" (Nabers),
  "Romo Dunze" (Rome Odunze), "Jameer Gibbs" (Jahmyr Gibbs), "Debo Samuel"
  (Deebo Samuel), "Dijon Stribling" (De'Zhaun Stribling). `CLAUDE.md` requires
  normalizing these before creating any `wiki/players/` page.

**Full episode vs. clip filtering**: Reception Perception publishes both to one
feed — full episodes titled `[FULL EPISODE] ...`, clips titled `RP Clips: ...`.
Its `include_episode` filter keeps only the former. The other two shows publish
only full episodes and take everything.

### Rejected alternatives (researched, for the record)

| Option | Why rejected |
|---|---|
| **Apple Podcasts local TTML cache** | Was the original approach. Apple caches transcripts on disk once subscribed, but the background caching stalls indefinitely — it delivered ~21 files then stopped, never reaching these shows' back catalogs. No way to trigger it: the web player has no transcript UI, Podcasts.app ships no AppleScript dictionary (`OSAScriptingDefinition` absent), and being a Mac Catalyst app it exposes nothing to System Events (an `entire contents` walk returns only the 3 window-chrome buttons). |
| **Apple's private transcript API** | `amp-api.podcasts.apple.com/.../transcripts` via `dlopen` of the private `PodcastsFoundation.framework` + `AMSMescal` signing under a live Apple ID. Works, but undocumented, version-fragile (confirmed broken on macOS 14.4.1), and requires running reverse-engineered third-party code against your Apple account. |
| **Spotify** | Official Web API has **no** transcript field. The internal `spclient.wg.spotify.com/transcript-read-along/v2/...` endpoint returns 401 without a session cookie + rotating TOTP — undocumented and breaks on Spotify's schedule. |
| **YouTube auto-captions** (`yt-dlp`) | Verified working (needs `--extractor-args "youtube:player_client=android"`; the default client is currently broken). But: **Chris Harris isn't on YouTube at all**, and **Reception Perception uploads only 12–23 min segments** of its 54–60 min episodes — ingesting those would capture a third of each episode while appearing complete. Only Waldman posts genuine full episodes, and there the captions are lower quality than Whisper. Rejected as not worth a fragile dependency for one of three shows. |
| **Paid ASR APIs** (OpenAI / AssemblyAI / Deepgram) | ~$0.30–0.50/episode, ~$200+ for the backlog. Strictly worse than free local Whisper on identical audio. |
| **Taddy API** | The only real off-the-shelf option (on-demand ASR for any public show) — but $75/mo. Free tier is creator-uploaded transcripts only. |
| **Rephonic** | Has Reception Perception transcripts; **$299/mo** API. |
| **Podscribe** | $250/mo + $1,500/mo transcript add-on. It's an ad-attribution product. |
| **Listen Notes** | <1% of episodes have transcripts, PRO-gated. Their own docs recommend fetching audio and running your own STT. |
| **Podcast Index API** | Free, but a pure pass-through of feed `<podcast:transcript>` tags — adds nothing over parsing the RSS directly. |
| **Podchaser / Deepcast / Steno / Snipd / Metacast** | No public transcript API; consumer apps, contact-sales, or bot-blocked. |
| **Shows' own sites & paid tiers** | None publish transcripts. Chris Harris's Yacht Club ($50/yr) is premium podcasts/blog/Discord — no transcripts. |

### Adding another show, or recreating this on another machine

Prerequisite: a Mac with Podcasts.app signed into an Apple ID that is
**subscribed to the target show**. Without a subscription, `ZMTPODCAST`/
`ZMTEPISODE` rows for it won't exist locally at all.

No podcast-app subscription is needed — everything comes from public RSS.

1. Find the show's RSS feed URL. If you only have an Apple Podcasts link, the
   public iTunes lookup API returns it:
   ```bash
   curl -s "https://itunes.apple.com/lookup?id=<APPLE_ID>&entity=podcast" | python3 -m json.tool | grep feedUrl
   ```
2. Check its episode title conventions before assuming a filter is needed:
   ```bash
   curl -s "<FEED_URL>" | grep -o '<title>[^<]*</title>' | head -20
   ```
   Most shows publish only full episodes, so `include_episode` should just be
   `lambda t: True`. Only add a title filter if the show mixes full episodes
   and clips in one feed, the way Reception Perception does.
3. Add an entry to the `SHOWS` list at the top of
   `scripts/check_new_episodes.py` — `slug` (short, unique, used as a filename
   prefix), `feed_url`, `expert_name`, `show_name`, `include_episode`, and
   `clean_title` (strip any title prefix that shouldn't appear in the wiki, or
   `lambda t: t.strip()` if there's nothing to strip).
4. Dry-run it before committing to a long transcription job:
   ```bash
   python3 scripts/check_new_episodes.py --show <slug> --dry-run
   ```
5. If recreating on a different machine/user account, install the prerequisites
   (see setup above) and re-point the absolute paths in the two `.plist` files
   under `scripts/launchd/` and in `scripts/run_daily_check.sh` /
   `scripts/run_weekly_backup.sh` / `scripts/drain_backlog.sh`.

### Scheduling: local `launchd`, not Claude Code's cloud scheduling

Two Claude-native scheduling mechanisms were considered and rejected:

- **Claude Code cloud "routines"** (the `/schedule` skill, `RemoteTrigger`
  API) — these explicitly run in Anthropic's cloud sandbox and have **no
  access to local files**, per their own documentation. This pipeline depends
  on local `whisper.cpp` + the local model file, so a cloud routine can't run
  the transcription step.
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

**`run_daily_check.sh`** runs `scripts/check_new_episodes.py --oldest --limit 10`
(pure Python 3, stdlib only — no pip dependencies) to update `scripts/state.json`
and write new transcripts into `raw/transcripts/<show>/`. If anything landed there, it
then invokes `claude -p "..."` — Claude Code's headless mode, running locally in
the repo so it picks up `CLAUDE.md` automatically — to do the actual wiki-writing
ingestion, explicitly instructed to process staged files in chronological order.
**No git commands run here.**

Two deliberate choices in that invocation:

- **`--oldest`** — expert opinion on a player evolves (injuries, camp reports,
  depth-chart moves), and each `wiki/players/` page accumulates dated takes in file
  order. Processing oldest → newest means a more current take always lands
  *after* an older one, so a stale 2024 opinion can never appear to supersede a
  fresher 2026 one. The same ordering is enforced at the ingestion step and
  codified as rule 4 in `CLAUDE.md`.
- **`--limit 10`** — without a cap, a daily run with a large backlog pending
  would become a multi-hour transcription job.

⚠️ **These two interact.** Oldest-first assumes the back catalog is already
drained. With a large backlog still pending, the daily job works forward from
the oldest episode and a newly published one waits behind it (at 10/day, a
538-episode backlog delays new episodes by ~54 days). Run `drain_backlog.sh` to
completion first; afterwards only 0–3 episodes are ever pending and oldest-first
is exactly right.

**`scripts/drain_backlog.sh`** is the separate, one-time counterpart for the
back catalog — same underlying script, but `--oldest` and optionally uncapped,
run under `nice`. It logs to the **same `scripts/logs/daily.log`** as the
scheduled job so all pipeline activity reads as one stream, wrapped in
`BACKLOG DRAIN START/END` banners to stay distinguishable. Safe to interrupt:
state is checkpointed after every episode, so re-running resumes exactly where
it stopped.

```bash
nohup ./scripts/drain_backlog.sh 50 > /dev/null 2>&1 &   # drain 50 episodes
nohup ./scripts/drain_backlog.sh > /dev/null 2>&1 &      # or drain everything
tail -f scripts/logs/daily.log                           # watch progress
```

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

`scripts/state.json` tracks every episode, **keyed by RSS `<guid>`**:
`pending` (seen in the feed, no transcript yet) → `fetched` (transcript staged
in `raw/transcripts/`, with `transcript_source` recording which path produced
it) → `ingested` (fully woven into the wiki; set by Claude, not the script,
once it's done processing a staged file).

State was previously keyed by Apple track ID, from the era when the pipeline
read Apple's local library. `migrate_state()` in the script re-keys legacy
state to GUIDs on first run, preserving `ingested` status so already-processed
episodes are never re-staged or duplicated into the wiki. The migration is
idempotent (guarded by a `"key": "guid"` marker).

State is saved after **every single episode**, so a long backlog run can be
interrupted at any point — by Ctrl-C, a reboot, or a crash — and resumed with
no lost work and no duplicate transcription.

Episodes the pipeline fails to transcribe are logged to
`raw/_needs-attention.md` by the script (not by Claude) and retried on
every subsequent run — that file is visibility into what's stuck, not a dead
end.
