#!/usr/bin/env python3
"""
Fetches new podcast episodes for every tracked show and stages a plain-text
transcript into raw/transcripts/<show>/ for wiki ingestion.

Transcript acquisition, in preference order:
  1. A <podcast:transcript> tag on the RSS item (publisher-provided, exact,
     free, instant). Handles SRT/VTT/plain text.
  2. Local speech-to-text via whisper.cpp on the episode's public MP3
     enclosure -- free, offline, no API key, ~24x realtime on Apple Silicon.

Never touches git. Never calls a paid API. Audio comes from the same public
RSS enclosures any podcast client downloads.

State lives in scripts/state.json, keyed by RSS <guid>. Episodes move
pending -> fetched (transcript written to raw/) -> ingested (woven into the wiki by
Claude, per CLAUDE.md).

Usage:
  check_new_episodes.py                      # normal run: newest first, all shows
  check_new_episodes.py --limit 3            # process at most 3 episodes
  check_new_episodes.py --oldest             # process oldest-first (backlog drain)
  check_new_episodes.py --show rp             # restrict to one show slug
  check_new_episodes.py --dry-run            # list what would be done, do nothing
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = REPO_ROOT / "scripts" / "state.json"
RAW_DIR = REPO_ROOT / "raw" / "transcripts"
NEEDS_ATTENTION_PATH = REPO_ROOT / "raw" / "_needs-attention.md"

WHISPER_BIN = "/opt/homebrew/bin/whisper-cli"
WHISPER_MODEL = Path.home() / ".local/share/whisper-models/ggml-large-v3-turbo.bin"
FFMPEG_BIN = "/opt/homebrew/bin/ffmpeg"

PODCAST_NS = "https://podcastindex.org/namespace/1.0"
ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"

USER_AGENT = "fantasy-football-knowledge-base/1.0 (personal podcast archiver)"
FLAG_AFTER_DAYS = 2

# Whether to prefer a <podcast:transcript> feed tag over local transcription.
#
# Default False. The only feed transcripts available across these three shows
# are 8 RSP Cast episodes from a July 2024 Blubrry auto-transcription trial,
# and their ASR is measurably worse than local whisper large-v3-turbo -- the
# Blubrry text renders "Matt Waldman" (the host's own name) as "about Wall"
# and "Matt W". Since this wiki is keyed on correctly-spelled proper nouns,
# consistent higher-quality output is worth ~2 minutes of compute per episode.
#
# Flip to True if a show ever starts publishing genuine human-written
# transcripts, which would beat any ASR.
PREFER_FEED_TRANSCRIPTS = False

# Minimum free disk space (GB) before we'll download audio.
MIN_FREE_GB = 5


def _strip_full_episode_prefix(title):
    return re.sub(r"^\[full episode\]\s*", "", title, flags=re.IGNORECASE).strip()


# Every tracked show. `include_episode` filters the feed down to what's worth
# ingesting -- only Reception Perception mixes full episodes and short clips
# into one feed, so only it needs a real filter.
SHOWS = [
    {
        "slug": "rp",
        "raw_subdir": "reception-perception",
        "feed_url": "https://feeds.megaphone.fm/reception-perception-the-show",
        "expert_name": "Matt Harmon",
        "show_name": "Reception Perception: The Show",
        "include_episode": lambda t: t.strip().lower().startswith("[full episode]"),
        "clean_title": _strip_full_episode_prefix,
    },
    {
        "slug": "harris",
        "raw_subdir": "harris-football",
        "feed_url": "https://harrisfootball.libsyn.com/rss",
        "expert_name": "Chris Harris",
        "show_name": "Harris Fantasy Football Podcast",
        "include_episode": lambda t: True,
        "clean_title": lambda t: t.strip(),
    },
    {
        "slug": "rsp",
        "raw_subdir": "rsp-cast",
        "feed_url": "https://mattwaldmanrsp.com/feed/podcast/",
        "expert_name": "Matt Waldman",
        "show_name": "Matt Waldman's RSP Cast",
        "include_episode": lambda t: True,
        "clean_title": lambda t: t.strip(),
    },
]


# ---------------------------------------------------------------- state ----

def load_state():
    if not STATE_PATH.exists():
        return {"episodes": {}, "monitoring_since": date.today().isoformat()}
    state = json.loads(STATE_PATH.read_text())
    return migrate_state(state)


def migrate_state(state):
    """Re-key legacy state (keyed by Apple track id) to RSS guid.

    The pipeline used to read Apple Podcasts' local library; it now reads RSS
    directly. Episodes already ingested must keep that status so they aren't
    re-staged and duplicated into the wiki.
    """
    eps = state.get("episodes", {})
    if not eps or state.get("key") == "guid":
        state["key"] = "guid"
        return state

    migrated = {}
    for old_key, v in eps.items():
        guid = v.get("guid")
        migrated[guid or old_key] = v
    state["episodes"] = migrated
    state["key"] = "guid"
    print(f"Migrated state to guid keys ({len(migrated)} episodes).", file=sys.stderr)
    return state


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


# ------------------------------------------------------------- helpers ----

def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)


def http_get(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def download_to(url, dest, timeout=900):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)
    return dest


def free_gb(path):
    st = shutil.disk_usage(path)
    return st.free / (1024 ** 3)


# --------------------------------------------------------------- feeds ----

def parse_feed(show):
    raw = http_get(show["feed_url"], timeout=180)
    root = ET.fromstring(raw)
    episodes = []
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        if not title or not show["include_episode"](title):
            continue

        guid = (item.findtext("guid") or "").strip()
        if not guid:
            continue

        enc = item.find("enclosure")
        audio_url = enc.get("url") if enc is not None else None

        tr = item.find(f"{{{PODCAST_NS}}}transcript")
        transcript_url = tr.get("url") if tr is not None else None
        transcript_type = (tr.get("type") or "") if tr is not None else ""

        pub_raw = item.findtext("pubDate")
        try:
            pub = parsedate_to_datetime(pub_raw).date() if pub_raw else None
        except Exception:
            pub = None

        episodes.append({
            "guid": guid,
            "title": title,
            "pub_date": pub,
            "audio_url": audio_url,
            "transcript_url": transcript_url,
            "transcript_type": transcript_type,
        })
    return episodes


# --------------------------------------------------------- transcripts ----

def timedtext_to_plain(raw_bytes):
    """Strip SRT/VTT cue numbering and timestamps down to prose."""
    text = raw_bytes.decode("utf-8", errors="replace")
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s == "WEBVTT":
            continue
        if "-->" in s:
            continue
        if re.fullmatch(r"\d+", s):
            continue
        if s.startswith(("NOTE ", "Kind:", "Language:")):
            continue
        out.append(s)

    # Collapse consecutive duplicate lines (common in rolling-caption formats)
    deduped = []
    for line in out:
        if not deduped or deduped[-1] != line:
            deduped.append(line)
    return " ".join(deduped)


def transcript_from_tag(ep):
    raw = http_get(ep["transcript_url"], timeout=180)
    ttype = (ep["transcript_type"] or "").lower()
    if "srt" in ttype or "vtt" in ttype or ep["transcript_url"].lower().endswith((".srt", ".vtt")):
        return timedtext_to_plain(raw)
    return raw.decode("utf-8", errors="replace").strip()


def transcript_from_whisper(ep, verbose=True):
    """Download the episode audio and transcribe it locally with whisper.cpp."""
    if not WHISPER_MODEL.exists():
        raise RuntimeError(f"Whisper model missing at {WHISPER_MODEL}")
    if free_gb(REPO_ROOT) < MIN_FREE_GB:
        raise RuntimeError(f"Low disk space (<{MIN_FREE_GB}GB free); refusing to download audio")

    with tempfile.TemporaryDirectory(prefix="ffkb-") as tmp:
        tmp = Path(tmp)
        audio = tmp / "episode.audio"
        wav = tmp / "episode.wav"
        out_base = tmp / "out"

        if verbose:
            print("      downloading audio...", flush=True)
        download_to(ep["audio_url"], audio)

        if verbose:
            print("      converting to 16kHz mono...", flush=True)
        subprocess.run(
            [FFMPEG_BIN, "-y", "-i", str(audio), "-ar", "16000", "-ac", "1",
             "-c:a", "pcm_s16le", str(wav)],
            check=True, capture_output=True,
        )

        if verbose:
            print("      transcribing (whisper large-v3-turbo)...", flush=True)
        proc = subprocess.run(
            [WHISPER_BIN,
             "-m", str(WHISPER_MODEL),
             "-f", str(wav),
             # Disable carrying decoded text forward as context. On long-form
             # audio that context can drift the model into uncased/unpunctuated
             # output for the rest of the file.
             "--max-context", "0",
             "--output-txt",
             "--output-file", str(out_base),
             "--no-prints"],
            capture_output=True, text=True,
        )

        txt = out_base.with_suffix(".txt")
        if not txt.exists():
            err = (proc.stderr or proc.stdout or "").strip().splitlines()
            tail = " | ".join(err[-3:]) if err else "no stderr"
            raise RuntimeError(f"whisper produced no output (rc={proc.returncode}): {tail}")
        body = txt.read_text(errors="replace").strip()

    # Reflow into readable paragraphs on sentence boundaries.
    body = re.sub(r"\s+", " ", body).strip()
    sentences = re.split(r"(?<=[.!?])\s+", body)
    paras, cur = [], []
    for s in sentences:
        cur.append(s)
        if len(cur) >= 5:
            paras.append(" ".join(cur))
            cur = []
    if cur:
        paras.append(" ".join(cur))
    return "\n\n".join(paras)


# ---------------------------------------------------------------- stage ----

def stage_transcript(show, ep, text, source_kind):
    pub = ep["pub_date"].isoformat() if ep["pub_date"] else "unknown-date"
    title = show["clean_title"](ep["title"])
    out_dir = RAW_DIR / show["raw_subdir"]
    out_path = out_dir / f"{pub}-{show['slug']}-{slugify(title)[:70]}.md"

    if source_kind == "feed-transcript":
        note = ("<!-- Publisher-provided transcript from the RSS <podcast:transcript>\n"
                "     tag. No speaker labels. -->")
    else:
        note = ("<!-- Auto-transcribed locally with whisper.cpp (large-v3-turbo) from\n"
                "     the episode's public RSS audio enclosure. No speaker labels --\n"
                "     infer who is speaking from context. Expect occasional errors on\n"
                "     player names and jargon. -->")

    front = (
        "---\n"
        "type: source\n"
        f"expert: {show['expert_name']}\n"
        f"show: {show['show_name']}\n"
        f"date: {pub}\n"
        f"guid: {ep['guid']}\n"
        f"transcript_source: {source_kind}\n"
        "tags: [source, inbox]\n"
        "---\n\n"
        f"# {title}\n\n"
        "## Transcript\n"
        f"{note}\n\n"
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(front + text + "\n")
    return out_path


def write_needs_attention(entries):
    if not entries:
        NEEDS_ATTENTION_PATH.write_text("# Needs Attention\n\nNothing flagged right now.\n")
        return
    lines = [
        "# Needs Attention\n",
        "Episodes the pipeline could not transcribe. Each is retried on every "
        "run -- this list is visibility, not a dead end.\n",
    ]
    for e in entries:
        lines.append(
            f"- **[{e.get('show','?')}] {e.get('title','?')}** "
            f"(published {e.get('pub_date','?')}) — {e.get('error','unknown error')}"
        )
    NEEDS_ATTENTION_PATH.write_text("\n".join(lines) + "\n")


# ----------------------------------------------------------------- main ----

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="max episodes to process")
    ap.add_argument("--oldest", action="store_true", help="process oldest-first (backlog drain)")
    ap.add_argument("--show", default=None, help="restrict to one show slug (rp/harris/rsp)")
    ap.add_argument("--dry-run", action="store_true", help="report only, change nothing")
    args = ap.parse_args()

    state = load_state()
    episodes_state = state.setdefault("episodes", {})
    today = date.today()

    shows = [s for s in SHOWS if not args.show or s["slug"] == args.show]
    if not shows:
        print(f"No show matching slug '{args.show}'", file=sys.stderr)
        sys.exit(1)

    # Build the work list across all selected shows.
    work = []
    for show in shows:
        try:
            eps = parse_feed(show)
        except Exception as e:
            print(f"ERROR: could not fetch {show['show_name']} feed: {e}", file=sys.stderr)
            continue
        print(f"{show['show_name']}: {len(eps)} episode(s) in feed")
        for ep in eps:
            entry = episodes_state.get(ep["guid"])
            if entry and entry.get("status") in ("fetched", "ingested"):
                continue
            if not ep["audio_url"] and not ep["transcript_url"]:
                continue
            work.append((show, ep))

    work.sort(key=lambda t: (t[1]["pub_date"] or date.min), reverse=not args.oldest)
    total_pending = len(work)
    if args.limit:
        work = work[: args.limit]

    print(f"\n{total_pending} episode(s) pending; processing {len(work)} "
          f"({'oldest' if args.oldest else 'newest'} first)\n")

    if args.dry_run:
        for show, ep in work:
            use_feed = (PREFER_FEED_TRANSCRIPTS and ep["transcript_url"]) or (
                not ep["audio_url"] and ep["transcript_url"])
            src = "feed-transcript" if use_feed else "whisper"
            print(f"  [{src:16}] {ep['pub_date']} | {show['slug']} | {ep['title'][:60]}")
        return

    fetched = 0
    failures = []
    for i, (show, ep) in enumerate(work, 1):
        label = f"[{i}/{len(work)}] {show['slug']} | {ep['pub_date']} | {ep['title'][:55]}"
        print(label, flush=True)
        started = datetime.now()
        try:
            use_feed = PREFER_FEED_TRANSCRIPTS and ep["transcript_url"]
            if not use_feed and not ep["audio_url"]:
                use_feed = bool(ep["transcript_url"])   # no audio: feed tag is the only option

            if use_feed:
                text, kind = transcript_from_tag(ep), "feed-transcript"
                print("      used publisher transcript from feed", flush=True)
            else:
                text, kind = transcript_from_whisper(ep), "whisper"

            if not text or len(text) < 500:
                raise RuntimeError(f"transcript suspiciously short ({len(text)} chars)")

            out_path = stage_transcript(show, ep, text, kind)
            episodes_state[ep["guid"]] = {
                "title": show["clean_title"](ep["title"]),
                "show": show["show_name"],
                "expert": show["expert_name"],
                "pub_date": ep["pub_date"].isoformat() if ep["pub_date"] else None,
                "guid": ep["guid"],
                "status": "fetched",
                "transcript_source": kind,
                "staged_path": str(out_path.relative_to(REPO_ROOT)),
                "first_seen": today.isoformat(),
                "last_checked": today.isoformat(),
            }
            fetched += 1
            elapsed = (datetime.now() - started).total_seconds()
            print(f"      OK  {len(text.split()):,} words in {elapsed:.0f}s -> {out_path.name}\n",
                  flush=True)
            save_state(state)   # checkpoint after every episode so long runs are resumable
        except Exception as e:
            print(f"      FAILED: {e}\n", file=sys.stderr, flush=True)
            failures.append({
                "show": show["show_name"],
                "title": ep["title"],
                "pub_date": ep["pub_date"].isoformat() if ep["pub_date"] else "?",
                "error": str(e)[:200],
            })

    write_needs_attention(failures)
    save_state(state)

    remaining = total_pending - fetched
    print(f"Done. {fetched} staged, {len(failures)} failed, ~{remaining} still pending.")


if __name__ == "__main__":
    main()
