#!/usr/bin/env python3
"""Index Observability Day Europe 2026 into an Obsidian vault.

No third-party Python dependencies required. Uses the local yt-dlp binary for
YouTube search/metadata/subtitle download.
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from difflib import SequenceMatcher
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
YTDLP = ROOT / "bin" / "yt-dlp"
SCHEDULE_URL = "https://colocatedeventseu2026.sched.com/overview/area/Observability+Day?iframe=no"
EVENT_NOTE = ROOT / "02-Sources/KubeCon/2026-Europe-Amsterdam/Observability-Day/KubeCon Europe 2026 Amsterdam - Observability Day.md"
SESSIONS_DIR = ROOT / "02-Sources/KubeCon/2026-Europe-Amsterdam/Observability-Day/Sessions"
RAW_DIR = ROOT / "_sources/raw"
TRANSCRIPTS_DIR = ROOT / "_sources/transcripts"
MANIFEST_DIR = ROOT / "_sources/manifests"

SKIP_TITLE_PATTERNS = ["break", "cancelled"]

TOPIC_RULES = {
    "OpenTelemetry": ["opentelemetry", "otel", "opamp"],
    "Metrics": ["metric", "promql", "prometheus", "cardinality", "sketch"],
    "Tracing": ["trace", "tracing", "baggage"],
    "Logging": ["log", "logging"],
    "Profiling": ["profil"],
    "SLOs": ["slo"],
    "Collectors": ["collector", "gateway", "gateways", "wasm"],
    "Cost Optimization": ["cost", "sampling", "carbon", "sustainable", "pue"],
    "eBPF": ["ebpf"],
    "Kubernetes Observability": ["kubernetes", "ingress", "pods", "microservices"],
    "AI Observability": ["ai", "agent", "autoremediation", "genai"],
    "Sustainability": ["carbon", "sustainable", "cern", "pue"],
}

@dataclass
class Session:
    title: str
    href: str
    sched_url: str
    room: str
    slug: str
    kind: str
    speakers: list[str]
    topics: list[str]
    youtube_id: str | None = None
    youtube_title: str | None = None
    youtube_url: str | None = None
    match_score: float | None = None
    transcript_file: str | None = None
    note_file: str | None = None
    status: str = "pending"


def slugify(value: str, max_len: int = 96) -> str:
    value = value.lower().strip()
    value = re.sub(r"[’']", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def normalize(value: str) -> str:
    value = html.unescape(value).lower()
    value = re.sub(r"[’'\"“”]", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_title(raw: str) -> str:
    raw = html.unescape(re.sub(r"<.*?>", "", raw)).strip()
    # The schedule renders hidden icon text oddly for one title; recover intent from href/search later if needed.
    raw = raw.replace("The  Trick", "The Meta Trick")
    return raw


def split_speakers(title: str) -> tuple[str, list[str]]:
    # Use the last " - " as speaker delimiter.
    if " - " not in title:
        return title, []
    base, speakers_raw = title.rsplit(" - ", 1)
    speakers = [s.strip() for s in re.split(r",| & |;", speakers_raw) if s.strip()]
    return base.strip(), speakers


def infer_kind(title: str) -> str:
    t = title.lower()
    if "lightning talk" in t:
        return "lightning-talk"
    if "keynote" in t:
        return "keynote"
    if "panel" in t:
        return "panel"
    if "project updates" in t:
        return "project-update"
    if "remarks" in t:
        return "remarks"
    return "session"


def infer_topics(title: str) -> list[str]:
    n = normalize(title)
    topics = []
    for topic, needles in TOPIC_RULES.items():
        if any(needle in n for needle in needles):
            topics.append(topic)
    return topics or ["Observability"]


def fetch_schedule() -> str:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    target = RAW_DIR / "observability-day-schedule.html"
    req = urllib.request.Request(SCHEDULE_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        body = response.read().decode("utf-8", errors="replace")
    target.write_text(body, encoding="utf-8")
    return body


def parse_schedule(schedule_html: str) -> list[Session]:
    pat = re.compile(
        r"<a href='([^']+)' class='name' id='([^']+)'><span class=\"session-title\">(.*?)</span> <span class=\"vs\">(.*?)</span>",
        re.S,
    )
    sessions: list[Session] = []
    for href, _id, raw_title, raw_room in pat.findall(schedule_html):
        title = clean_title(raw_title)
        if any(p in title.lower() for p in SKIP_TITLE_PATTERNS):
            continue
        room = html.unescape(re.sub(r"<.*?>", "", raw_room)).strip()
        sched_url = "https://colocatedeventseu2026.sched.com/" + href
        base_title, speakers = split_speakers(title)
        slug = slugify(base_title)
        sessions.append(Session(
            title=title,
            href=href,
            sched_url=sched_url,
            room=room,
            slug=slug,
            kind=infer_kind(title),
            speakers=speakers,
            topics=infer_topics(title),
        ))
    return sessions


def run_jsonl(args: list[str], timeout: int = 90) -> list[dict[str, Any]]:
    proc = subprocess.run(args, text=True, capture_output=True, timeout=timeout)
    rows = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return rows


def search_youtube(session: Session) -> None:
    base, speakers = split_speakers(session.title)
    base = re.sub(r"^Observability Day \|\s*", "", base)
    base = re.sub(r"^⚡Lightning Talk:\s*", "", base)
    speaker_hint = " ".join(speakers[:2])
    queries = [
        f"{base} {speaker_hint}".strip(),
        f"{base} CNCF",
        session.title,
    ]
    best: tuple[float, dict[str, Any]] | None = None
    for query in queries:
        rows = run_jsonl([str(YTDLP), "--flat-playlist", "--dump-json", f"ytsearch5:{query}"], timeout=120)
        for row in rows:
            title = row.get("title") or ""
            channel = (row.get("channel") or row.get("uploader") or "").lower()
            score = SequenceMatcher(None, normalize(base), normalize(title)).ratio()
            if "cncf" in channel or "cloud native" in channel:
                score += 0.08
            if best is None or score > best[0]:
                best = (score, row)
        if best and best[0] >= 0.70:
            break
    if best and best[0] >= 0.52:
        row = best[1]
        session.youtube_id = row.get("id")
        session.youtube_title = row.get("title")
        session.youtube_url = f"https://www.youtube.com/watch?v={session.youtube_id}"
        session.match_score = round(best[0], 3)
        session.status = "video-found"
    else:
        session.status = "video-not-found"


def vtt_to_text(vtt: str) -> str:
    out = []
    last = None
    for line in vtt.splitlines():
        line = line.strip()
        if not line or line == "WEBVTT" or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line or re.fullmatch(r"\d+", line):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = html.unescape(line).strip()
        if not line or line == last:
            continue
        out.append(line)
        last = line
    # Join into readable paragraphs.
    text = " ".join(out)
    text = re.sub(r"\s+", " ", text).strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paras = []
    buf = []
    for sentence in sentences:
        buf.append(sentence)
        if sum(len(x) for x in buf) > 700:
            paras.append(" ".join(buf))
            buf = []
    if buf:
        paras.append(" ".join(buf))
    return "\n\n".join(paras)


def download_transcript(session: Session) -> None:
    if not session.youtube_id:
        return
    outdir = TRANSCRIPTS_DIR / session.slug
    outdir.mkdir(parents=True, exist_ok=True)
    output = str(outdir / "%(id)s.%(ext)s")
    cmd = [
        str(YTDLP), "--skip-download", "--write-subs", "--write-auto-subs",
        "--sub-langs", "en.*", "--sub-format", "vtt", "-o", output, session.youtube_url,
    ]
    subprocess.run(cmd, text=True, capture_output=True, timeout=180)
    candidates = sorted(outdir.glob(f"{session.youtube_id}*.vtt"))
    if not candidates:
        session.status = "transcript-missing"
        return
    # Prefer original English if present.
    chosen = next((p for p in candidates if ".en-orig." in p.name), candidates[0])
    txt = outdir / f"{session.youtube_id}.txt"
    txt.write_text(vtt_to_text(chosen.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
    session.transcript_file = str(txt.relative_to(ROOT))
    session.status = "transcript-downloaded"


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in items) + "]"


def write_session_note(session: Session) -> None:
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    path = SESSIONS_DIR / f"{session.slug}.md"
    transcript = ""
    if session.transcript_file:
        transcript = (ROOT / session.transcript_file).read_text(encoding="utf-8", errors="replace")
    body = f"""---
type: session
event: KubeCon Europe 2026 Amsterdam - Observability Day
year: 2026
kind: {session.kind}
room: {json.dumps(session.room, ensure_ascii=False)}
sched_url: {session.sched_url}
youtube_url: {session.youtube_url or ''}
youtube_id: {session.youtube_id or ''}
match_score: {session.match_score or ''}
speakers: {yaml_list(session.speakers)}
topics: {yaml_list(session.topics)}
status: {session.status}
---

# {session.title}

## Metadata

- Schedule: {session.sched_url}
- YouTube: {session.youtube_url or 'Not found'}
- Room: {session.room}
- Speakers: {', '.join(session.speakers) if session.speakers else 'N/A'}
- Topics: {', '.join('[[' + t + ']]' for t in session.topics)}

## Transcript

{transcript if transcript else '_Transcript not available yet._'}

## Notes

- Raw note. Promote durable insights to topic notes under `03-Topics/`.
"""
    path.write_text(body, encoding="utf-8")
    session.note_file = str(path.relative_to(ROOT))


def write_event_note(sessions: list[Session]) -> None:
    header = """# KubeCon Europe 2026 Amsterdam - Observability Day

- Type: event
- Event date: 2026-03-23
- Location: Amsterdam, The Netherlands
- Parent event: KubeCon + CloudNativeCon Europe 2026
- Source schedule: https://colocatedeventseu2026.sched.com/overview/area/Observability+Day
- Video channel: https://www.youtube.com/@cncf

## Sessions

"""
    lines = []
    for s in sessions:
        note = Path(s.note_file).stem if s.note_file else s.slug
        marker = "✅" if s.status == "transcript-downloaded" else "⚠️"
        lines.append(f"- {marker} [[{note}|{s.title}]] — `{s.status}`")
    EVENT_NOTE.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if not YTDLP.exists():
        print(f"Missing yt-dlp at {YTDLP}. Download it first.", file=sys.stderr)
        return 2
    for d in [RAW_DIR, TRANSCRIPTS_DIR, MANIFEST_DIR, SESSIONS_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    schedule = fetch_schedule()
    sessions = parse_schedule(schedule)
    print(f"Parsed {len(sessions)} schedule sessions")
    for i, session in enumerate(sessions, 1):
        print(f"[{i}/{len(sessions)}] {session.title}")
        search_youtube(session)
        if session.youtube_id:
            print(f"  video: {session.youtube_id} score={session.match_score} {session.youtube_title}")
            download_transcript(session)
            print(f"  status: {session.status}")
        else:
            print("  video not found")
        write_session_note(session)
    write_event_note(sessions)
    manifest = MANIFEST_DIR / "observability-day-eu-2026.json"
    manifest.write_text(json.dumps([asdict(s) for s in sessions], ensure_ascii=False, indent=2), encoding="utf-8")
    ok = sum(1 for s in sessions if s.status == "transcript-downloaded")
    print(f"Done: {ok}/{len(sessions)} transcripts downloaded")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
