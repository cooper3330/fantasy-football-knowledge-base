#!/usr/bin/env python3
"""
Passively checks the local Apple Podcasts library/cache for new episodes
across all tracked shows and, when Apple's own auto-generated transcript has
finished downloading, stages a plain-text copy in Sources/_inbox/ for wiki
ingestion.

Never touches git. Never calls any Apple API directly -- only reads files
Apple's Podcasts app has already written to disk on this Mac (MTLibrary.sqlite
+ the TTML transcript cache), which only exist because this machine is
subscribed to each show in Podcasts.app.

State is tracked in scripts/state.json, keyed by Apple's globally-unique
episode track ID (safe to share one state file across shows). An episode
whose transcript hasn't appeared in the cache within FLAG_AFTER_DAYS is
written to Sources/_needs-attention.md, but checking continues indefinitely
-- it's a visibility flag, not a terminal failure.

To track another show: subscribe to it in Podcasts.app on this Mac, then add
an entry to SHOWS below.
"""

import glob
import json
import re
import sqlite3
import sys
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = REPO_ROOT / "scripts" / "state.json"
INBOX_DIR = REPO_ROOT / "Sources" / "_inbox"
NEEDS_ATTENTION_PATH = REPO_ROOT / "Sources" / "_needs-attention.md"

PODCASTS_CONTAINER = Path.home() / "Library" / "Group Containers" / "243LU875E5.groups.com.apple.podcasts"
LIBRARY_DB = PODCASTS_CONTAINER / "Documents" / "MTLibrary.sqlite"
TTML_ROOT = PODCASTS_CONTAINER / "Library" / "Cache" / "Assets" / "TTML"

FLAG_AFTER_DAYS = 2

TT_NS = "http://www.w3.org/ns/ttml"
TTM_NS = "http://www.w3.org/ns/ttml#metadata"
PODCASTS_NS = "http://podcasts.apple.com/transcript-ttml-internal"

CORE_DATA_EPOCH = datetime(2001, 1, 1)


def _strip_full_episode_prefix(title):
    return re.sub(r"^\[full episode\]\s*", "", title, flags=re.IGNORECASE).strip()


# Every tracked show. `podcast_title` must exactly match ZMTPODCAST.ZTITLE in
# the local Podcasts library -- the show must already be subscribed there.
# `include_episode` filters ZMTEPISODE rows down to what's actually worth
# ingesting (e.g. dropping short clips); default to including everything for
# shows that don't split full episodes and clips into the same feed.
SHOWS = [
    {
        "slug": "rp",
        "podcast_title": "Reception Perception: The Show",
        "expert_name": "Matt Harmon",
        "show_name": "Reception Perception: The Show",
        "include_episode": lambda title: title.strip().lower().startswith("[full episode]")
        and not title.strip().lower().startswith("rp clips:"),
        "clean_title": _strip_full_episode_prefix,
    },
    {
        "slug": "harris",
        "podcast_title": "Harris Fantasy Football Podcast",
        "expert_name": "Chris Harris",
        "show_name": "Harris Fantasy Football Podcast",
        "include_episode": lambda title: True,
        "clean_title": lambda title: title.strip(),
    },
    {
        "slug": "rsp",
        "podcast_title": "Matt Waldman's RSP Cast",
        "expert_name": "Matt Waldman",
        "show_name": "Matt Waldman's RSP Cast",
        "include_episode": lambda title: True,
        "clean_title": lambda title: title.strip(),
    },
]


def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"episodes": {}, "monitoring_since": date.today().isoformat()}


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def coredata_to_date(seconds):
    if seconds is None:
        return None
    return (CORE_DATA_EPOCH + timedelta(seconds=seconds)).date()


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)


def fetch_episodes_for_show(conn, show):
    """Read the local Podcasts library DB for episode rows of one tracked show."""
    podcast = conn.execute(
        "SELECT Z_PK FROM ZMTPODCAST WHERE ZTITLE = ?", (show["podcast_title"],)
    ).fetchone()
    if podcast is None:
        print(
            f"WARN: '{show['podcast_title']}' not found in local Podcasts library "
            "-- make sure you're subscribed to it in Podcasts.app on this Mac. Skipping.",
            file=sys.stderr,
        )
        return []

    rows = conn.execute(
        """
        SELECT ZTITLE, ZSTORETRACKID, ZPUBDATE, ZGUID
        FROM ZMTEPISODE
        WHERE ZPODCAST = ?
        ORDER BY ZPUBDATE DESC
        """,
        (podcast["Z_PK"],),
    ).fetchall()

    episodes = []
    for row in rows:
        title = row["ZTITLE"] or ""
        if not show["include_episode"](title):
            continue
        episodes.append(
            {
                "track_id": str(row["ZSTORETRACKID"]),
                "title": title,
                "pub_date": coredata_to_date(row["ZPUBDATE"]),
                "guid": row["ZGUID"],
            }
        )
    return episodes


def find_cached_ttml(track_id):
    matches = glob.glob(str(TTML_ROOT / "**" / f"*_{track_id}.ttml*"), recursive=True)
    return Path(matches[0]) if matches else None


def ttml_to_text(ttml_path):
    """Convert an Apple podcast transcript TTML file into readable plain text.

    Apple's transcripts label speakers generically (SPEAKER_1, SPEAKER_2, ...)
    with no name mapping in <head><metadata>, and the label->person mapping
    isn't guaranteed to be stable across episodes -- the ingestion step should
    infer who's speaking from context, not assume a fixed order.
    """
    tree = ET.parse(ttml_path)
    root = tree.getroot()
    lines = []
    for p in root.iter(f"{{{TT_NS}}}p"):
        speaker = p.get(f"{{{TTM_NS}}}agent", "UNKNOWN")
        words = [
            span.text
            for span in p.iter(f"{{{TT_NS}}}span")
            if span.get(f"{{{PODCASTS_NS}}}unit") == "word" and span.text
        ]
        if not words:
            continue
        lines.append(f"{speaker}: {' '.join(words)}")
    return "\n\n".join(lines)


def stage_transcript(show, episode, ttml_path):
    pub_date = episode["pub_date"].isoformat() if episode["pub_date"] else "unknown-date"
    title = show["clean_title"](episode["title"])
    slug = slugify(title)[:80]
    out_path = INBOX_DIR / f"{pub_date}-{show['slug']}-{slug}.md"

    transcript_text = ttml_to_text(ttml_path)

    front_matter = (
        "---\n"
        "type: source\n"
        f"expert: {show['expert_name']}\n"
        f"show: {show['show_name']}\n"
        f"date: {pub_date}\n"
        f"apple_track_id: {episode['track_id']}\n"
        f"guid: {episode['guid']}\n"
        "tags: [source, inbox]\n"
        "---\n\n"
        f"# {title}\n\n"
        "## Transcript\n"
        "<!-- Auto-generated by Apple Podcasts (speaker labels are generic --\n"
        "     infer who's speaking from context, not label order). -->\n\n"
    )

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(front_matter + transcript_text + "\n")
    return out_path


def write_needs_attention(flagged):
    if not flagged:
        if NEEDS_ATTENTION_PATH.exists():
            NEEDS_ATTENTION_PATH.write_text(
                "# Needs Attention\n\nNothing flagged right now.\n"
            )
        return

    lines = [
        "# Needs Attention\n",
        "Episodes published more than "
        f"{FLAG_AFTER_DAYS} day(s) ago whose Apple-generated transcript "
        "still hasn't appeared in the local cache. Checking continues "
        "automatically each day -- this list is just visibility, not a "
        "dead end.\n",
    ]
    for ep in flagged:
        lines.append(
            f"- **[{ep['show']}] {ep['title']}** (published {ep['pub_date']}, "
            f"track id `{ep['track_id']}`) -- first seen "
            f"{ep['first_seen']}, still pending as of {date.today().isoformat()}"
        )
    NEEDS_ATTENTION_PATH.write_text("\n".join(lines) + "\n")


def main():
    if not LIBRARY_DB.exists():
        print(f"ERROR: Podcasts library DB not found at {LIBRARY_DB}", file=sys.stderr)
        print("Is Podcasts.app installed and has it synced at least once?", file=sys.stderr)
        sys.exit(1)

    state = load_state()
    episodes_state = state.setdefault("episodes", {})
    monitoring_since = date.fromisoformat(
        state.setdefault("monitoring_since", date.today().isoformat())
    )
    today = date.today()

    conn = sqlite3.connect(f"file:{LIBRARY_DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    total_checked = 0
    fetched_count = 0
    pending_count = 0

    try:
        for show in SHOWS:
            episodes = fetch_episodes_for_show(conn, show)
            total_checked += len(episodes)

            for ep in episodes:
                track_id = ep["track_id"]
                entry = episodes_state.get(track_id)

                if entry is None:
                    entry = {
                        "title": show["clean_title"](ep["title"]),
                        "show": show["show_name"],
                        "expert": show["expert_name"],
                        "pub_date": ep["pub_date"].isoformat() if ep["pub_date"] else None,
                        "guid": ep["guid"],
                        "status": "pending",
                        "first_seen": today.isoformat(),
                        "last_checked": today.isoformat(),
                    }
                    episodes_state[track_id] = entry

                if entry["status"] in ("fetched", "ingested"):
                    continue

                entry["last_checked"] = today.isoformat()

                ttml_path = find_cached_ttml(track_id)
                if ttml_path is not None:
                    try:
                        out_path = stage_transcript(show, ep, ttml_path)
                    except ET.ParseError as e:
                        print(f"WARN: failed to parse TTML for track {track_id}: {e}", file=sys.stderr)
                        continue
                    entry["status"] = "fetched"
                    entry["staged_path"] = str(out_path.relative_to(REPO_ROOT))
                    fetched_count += 1
                    print(f"Fetched transcript [{show['show_name']}]: {entry['title']} -> {out_path}")
                    continue

                # Only episodes published since we started monitoring are eligible to be
                # flagged -- pre-existing backlog episodes retry passively forever
                # without spamming needs-attention (Apple may never backfill transcripts
                # for old episodes, and that's not an actionable "pipeline is broken" signal).
                pub_date = date.fromisoformat(entry["pub_date"]) if entry["pub_date"] else None
                eligible_for_flagging = pub_date is not None and pub_date >= monitoring_since
                age_days = (today - pub_date).days if pub_date else 0

                if eligible_for_flagging and age_days >= FLAG_AFTER_DAYS:
                    entry["status"] = "flagged"
                else:
                    pending_count += 1
    finally:
        conn.close()

    # re-collect anything still flagged (from this run or prior ones) across all shows
    all_flagged = [
        {
            "title": v["title"],
            "show": v.get("show", "unknown show"),
            "pub_date": v["pub_date"],
            "track_id": k,
            "first_seen": v["first_seen"],
        }
        for k, v in episodes_state.items()
        if v["status"] == "flagged"
    ]
    write_needs_attention(all_flagged)

    save_state(state)

    print(
        f"\nChecked {total_checked} episode(s) across {len(SHOWS)} show(s): "
        f"{fetched_count} newly fetched, {pending_count} pending, "
        f"{len(all_flagged)} flagged (>= {FLAG_AFTER_DAYS} days without a transcript)."
    )


if __name__ == "__main__":
    main()
