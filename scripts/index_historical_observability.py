#!/usr/bin/env python3
"""Index historical KubeCon/CloudNativeCon Observability track sessions.

Scope: official Sched pages with `overview/type/Observability` across known
KubeCon + CloudNativeCon editions. Generates Obsidian notes with event edition,
location, country, topic tags, schedule link, YouTube link when found, summary,
and transcript when subtitles are available.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
YTDLP = ROOT / "bin" / "yt-dlp"
RAW_DIR = ROOT / "_sources/raw/historical-observability"
TRANSCRIPTS_DIR = ROOT / "_sources/transcripts/historical-observability"
MANIFEST_DIR = ROOT / "_sources/manifests"
SOURCES_DIR = ROOT / "02-Sources/KubeCon"
MAP = ROOT / "01-Maps/KubeCon Historical Observability.md"

EVENTS = [
    {"id":"kccnceu2021", "year":2021, "region":"Europe", "city":"Virtual", "country":"Virtual", "domain":"kccnceu2021.sched.com", "date":"2021-05-04/2021-05-07"},
    {"id":"kccncna2021", "year":2021, "region":"North America", "city":"Los Angeles", "country":"United States", "domain":"kccncna2021.sched.com", "date":"2021-10-11/2021-10-15"},
    {"id":"kccnceu2022", "year":2022, "region":"Europe", "city":"Valencia", "country":"Spain", "domain":"kccnceu2022.sched.com", "date":"2022-05-16/2022-05-20"},
    {"id":"kccncna2022", "year":2022, "region":"North America", "city":"Detroit", "country":"United States", "domain":"kccncna2022.sched.com", "date":"2022-10-24/2022-10-28"},
    {"id":"kccnceu2023", "year":2023, "region":"Europe", "city":"Amsterdam", "country":"Netherlands", "domain":"kccnceu2023.sched.com", "date":"2023-04-17/2023-04-21"},
    {"id":"kccncna2023", "year":2023, "region":"North America", "city":"Chicago", "country":"United States", "domain":"kccncna2023.sched.com", "date":"2023-11-06/2023-11-09"},
    {"id":"kccnceu2024", "year":2024, "region":"Europe", "city":"Paris", "country":"France", "domain":"kccnceu2024.sched.com", "date":"2024-03-19/2024-03-22"},
    {"id":"kccncna2024", "year":2024, "region":"North America", "city":"Salt Lake City", "country":"United States", "domain":"kccncna2024.sched.com", "date":"2024-11-12/2024-11-15"},
    {"id":"kccnceu2025", "year":2025, "region":"Europe", "city":"London", "country":"United Kingdom", "domain":"kccnceu2025.sched.com", "date":"2025-04-01/2025-04-04"},
    {"id":"kccncna2025", "year":2025, "region":"North America", "city":"Atlanta", "country":"United States", "domain":"kccncna2025.sched.com", "date":"2025-11-10/2025-11-13"},
    {"id":"kccncchn2025", "year":2025, "region":"China", "city":"Hong Kong", "country":"China", "domain":"kccncchn2025.sched.com", "date":"2025"},
]

TOPIC_RULES = {
    "OpenTelemetry": ["opentelemetry", "otel", "opamp", "otlp", "ottl"],
    "Metrics": ["metric", "promql", "prometheus", "openmetrics", "cardinality", "cortex"],
    "Tracing": ["trace", "tracing", "jaeger", "span", "baggage"],
    "Logging": ["log", "logging", "fluent", "fluentd", "fluent bit"],
    "Profiling": ["profil"],
    "SLOs": ["slo", "sli", "error budget"],
    "Collectors": ["collector", "gateway", "agent", "pipeline", "processor"],
    "Cost Optimization": ["cost", "sampling", "budget", "efficient"],
    "eBPF": ["ebpf", "bpf"],
    "Kubernetes Observability": ["kubernetes", "k8s", "cluster", "pod", "container", "ingress"],
    "AI Observability": ["ai", "llm", "genai", "agentic"],
    "Sustainability": ["carbon", "sustainab", "green"],
}

@dataclass
class HistSession:
    event_id: str
    edition: str
    year: int
    region: str
    city: str
    country: str
    event_date: str
    title: str
    session_title: str
    speakers: list[str]
    room: str
    sched_url: str
    schedule_url: str
    description: str = ""
    summary: str = ""
    topics: list[str] | None = None
    slides: list[str] | None = None
    youtube_id: str | None = None
    youtube_title: str | None = None
    youtube_url: str | None = None
    video_match_score: float | None = None
    transcript_file: str | None = None
    note_file: str | None = None
    status: str = "parsed"


def request(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def strip_tags(s: str) -> str:
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<.*?>", "", s, flags=re.S)
    return html.unescape(re.sub(r"[ \t]+", " ", s)).strip()


def slugify(value: str, max_len: int = 110) -> str:
    value = html.unescape(value).lower()
    value = re.sub(r"[’']", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def norm(value: str) -> str:
    value = strip_tags(value).lower()
    value = re.sub(r"[’'\"“”]", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def split_speakers(title: str) -> tuple[str, list[str]]:
    if " - " not in title:
        return title, []
    base, raw = title.rsplit(" - ", 1)
    parts = [p.strip() for p in re.split(r",| & |;", raw) if p.strip()]
    # Drop company-only fragments when obvious, keep imperfect data rather than losing names.
    return base.strip(), parts


def infer_topics(title: str, description: str) -> list[str]:
    text = norm(title + " " + description)
    topics = []
    for topic, needles in TOPIC_RULES.items():
        if any(n in text for n in needles):
            topics.append(topic)
    return topics or ["Observability"]


def summarize(description: str, title: str) -> str:
    text = re.sub(r"\s+", " ", description).strip()
    if not text:
        return f"Sessão da trilha de Observability sobre {title}."
    sentences = re.split(r"(?<=[.!?])\s+", text)
    summary = " ".join(sentences[:3]).strip()
    if len(summary) > 700:
        summary = summary[:697].rsplit(" ", 1)[0] + "..."
    return summary


def parse_overview(event: dict[str, Any]) -> list[HistSession]:
    url = f"https://{event['domain']}/overview/type/Observability?iframe=no"
    html_text = request(url)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (RAW_DIR / f"{event['id']}-overview.html").write_text(html_text, encoding="utf-8")
    pat = re.compile(r"<a href='([^']+)' class='name' id='[^']+'><span class=\"session-title\">(.*?)</span> <span class=\"vs\">(.*?)</span>", re.S)
    sessions = []
    for href, raw_title, raw_room in pat.findall(html_text):
        title = strip_tags(raw_title)
        if any(x in title.lower() for x in ["break", "lunch", "reception", "cancelled"]):
            continue
        room = strip_tags(raw_room)
        sched_url = f"https://{event['domain']}/{href}"
        session_title, speakers = split_speakers(title)
        edition = f"KubeCon + CloudNativeCon {event['region']} {event['year']} - {event['city']}, {event['country']}"
        sessions.append(HistSession(
            event_id=event['id'], edition=edition, year=event['year'], region=event['region'], city=event['city'], country=event['country'], event_date=event['date'],
            title=title, session_title=session_title, speakers=speakers, room=room, sched_url=sched_url, schedule_url=url,
        ))
    return sessions


def enrich_from_event_page(s: HistSession) -> None:
    try:
        page = request(s.sched_url + ("&iframe=no" if "?" in s.sched_url else "?iframe=no"), timeout=30)
    except Exception:
        s.status = "event-page-fetch-failed"
        return
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (RAW_DIR / f"{s.event_id}-{slugify(s.session_title, 60)}.html").write_text(page, encoding="utf-8")
    m = re.search(r'<div class="tip-description">(.*?)</div>\s*</div>', page, re.S)
    if m:
        desc = strip_tags(m.group(1))
        desc = re.sub(r"^Speakers\s+", "", desc).strip()
        s.description = desc
    slides = re.findall(r'<a class="file-uploaded[^"]*" href="([^"]+)"', page)
    s.slides = [html.unescape(x) for x in slides]
    s.summary = summarize(s.description, s.session_title)
    s.topics = infer_topics(s.title, s.description)


def run_jsonl(args: list[str], timeout: int = 120) -> list[dict[str, Any]]:
    try:
        p = subprocess.run(args, text=True, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return []
    rows = []
    for line in p.stdout.splitlines():
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
    return rows


def search_video(s: HistSession) -> None:
    if not YTDLP.exists():
        return
    speaker_hint = " ".join(s.speakers[:2])
    queries = [
        f"{s.session_title} {speaker_hint} CNCF KubeCon {s.year}",
        f"{s.session_title} CNCF",
    ]
    best: tuple[float, dict[str, Any]] | None = None
    for q in queries:
        rows = run_jsonl([str(YTDLP), "--flat-playlist", "--dump-json", f"ytsearch4:{q}"], timeout=150)
        for row in rows:
            title = row.get("title") or ""
            channel = (row.get("channel") or row.get("uploader") or "").lower()
            score = SequenceMatcher(None, norm(s.session_title), norm(title)).ratio()
            if "cncf" in channel or "cloud native" in channel:
                score += 0.08
            if str(s.year) in title:
                score += 0.02
            if best is None or score > best[0]:
                best = (score, row)
        if best and best[0] >= 0.73:
            break
    if best and best[0] >= 0.55:
        row = best[1]
        s.youtube_id = row.get("id")
        s.youtube_title = row.get("title")
        s.youtube_url = f"https://www.youtube.com/watch?v={s.youtube_id}"
        s.video_match_score = round(best[0], 3)
        s.status = "video-found"


def vtt_to_text(vtt: str) -> str:
    lines, last = [], None
    for line in vtt.splitlines():
        line = line.strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:")) or "-->" in line or re.fullmatch(r"\d+", line):
            continue
        line = html.unescape(re.sub(r"<[^>]+>", "", line)).strip()
        if line and line != last:
            lines.append(line)
            last = line
    text = re.sub(r"\s+", " ", " ".join(lines)).strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paras, buf = [], []
    for sent in sentences:
        buf.append(sent)
        if sum(len(x) for x in buf) > 900:
            paras.append(" ".join(buf)); buf=[]
    if buf: paras.append(" ".join(buf))
    return "\n\n".join(paras)


def download_transcript(s: HistSession) -> None:
    if not s.youtube_url or not YTDLP.exists():
        return
    outdir = TRANSCRIPTS_DIR / s.event_id / slugify(s.session_title, 80)
    outdir.mkdir(parents=True, exist_ok=True)
    cmd = [str(YTDLP), "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*", "--sub-format", "vtt", "-o", str(outdir / "%(id)s.%(ext)s"), s.youtube_url]
    subprocess.run(cmd, text=True, capture_output=True, timeout=180)
    files = sorted(outdir.glob(f"{s.youtube_id}*.vtt"))
    if not files:
        return
    chosen = next((p for p in files if ".en-orig." in p.name), files[0])
    txt = outdir / f"{s.youtube_id}.txt"
    txt.write_text(vtt_to_text(chosen.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
    s.transcript_file = str(txt.relative_to(ROOT))
    s.status = "transcript-downloaded"


def yaml_list(items: list[str] | None) -> str:
    return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in (items or [])) + "]"


def write_note(s: HistSession) -> None:
    event_dir = SOURCES_DIR / f"{s.year}-{slugify(s.region)}-{slugify(s.city)}" / "Observability"
    sessions_dir = event_dir / "Sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    note = sessions_dir / f"{slugify(s.session_title)}.md"
    transcript = ""
    if s.transcript_file and (ROOT / s.transcript_file).exists():
        transcript = (ROOT / s.transcript_file).read_text(encoding="utf-8", errors="replace")
    body = f"""---
type: session
event: {json.dumps(s.edition, ensure_ascii=False)}
event_id: {s.event_id}
year: {s.year}
region: {json.dumps(s.region, ensure_ascii=False)}
city: {json.dumps(s.city, ensure_ascii=False)}
country: {json.dumps(s.country, ensure_ascii=False)}
event_date: {json.dumps(s.event_date, ensure_ascii=False)}
track: Observability
sched_url: {s.sched_url}
youtube_url: {s.youtube_url or ''}
youtube_id: {s.youtube_id or ''}
video_match_score: {s.video_match_score or ''}
speakers: {yaml_list(s.speakers)}
topics: {yaml_list(s.topics)}
slides: {yaml_list(s.slides)}
status: {s.status}
---

# {s.title}

## Identificação

- Edição: {s.edition}
- País/cidade: {s.country} / {s.city}
- Ano: {s.year}
- Trilha/tema: Observability
- Tópicos: {', '.join('[[' + t + ']]' for t in (s.topics or []))}
- Speakers: {', '.join(s.speakers) if s.speakers else 'N/A'}
- Schedule: {s.sched_url}
- YouTube: {s.youtube_url or 'Não encontrado automaticamente'}

## Resumo

{s.summary or '_Resumo indisponível._'}

## Descrição oficial

{s.description or '_Descrição oficial não encontrada na página do evento._'}

## Transcript

{transcript if transcript else '_Transcript não disponível ou ainda não baixada._'}

## Links

- Schedule oficial: {s.sched_url}
"""
    if s.youtube_url:
        body += f"- Vídeo no YouTube: {s.youtube_url}\n"
    for slide in s.slides or []:
        body += f"- Slides: {slide}\n"
    note.write_text(body, encoding="utf-8")
    s.note_file = str(note.relative_to(ROOT))


def write_event_indexes(sessions: list[HistSession]) -> None:
    by_event: dict[str, list[HistSession]] = {}
    for s in sessions:
        by_event.setdefault(s.event_id, []).append(s)
    for event_id, rows in by_event.items():
        first = rows[0]
        event_dir = SOURCES_DIR / f"{first.year}-{slugify(first.region)}-{slugify(first.city)}" / "Observability"
        event_dir.mkdir(parents=True, exist_ok=True)
        content = f"# {first.edition} - Observability\n\n- Ano: {first.year}\n- Região: {first.region}\n- País/cidade: {first.country} / {first.city}\n- Schedule: {first.schedule_url}\n- Sessões indexadas: {len(rows)}\n\n## Sessões\n\n"
        for s in rows:
            stem = Path(s.note_file).stem if s.note_file else slugify(s.session_title)
            marker = "✅" if s.status == "transcript-downloaded" else ("🎥" if s.youtube_url else "⚠️")
            content += f"- {marker} [[{stem}|{s.session_title}]] — {', '.join(s.topics or [])}\n"
        (event_dir / f"{first.edition} - Observability.md".replace('/','-')).write_text(content, encoding="utf-8")
    content = "# KubeCon Historical Observability\n\nVarredura histórica da trilha `Observability` em agendas oficiais Sched da KubeCon + CloudNativeCon.\n\n## Edições\n\n"
    for event_id, rows in sorted(by_event.items(), key=lambda kv:(kv[1][0].year, kv[1][0].region)):
        f = rows[0]
        content += f"- [[{f.edition} - Observability]] — {len(rows)} sessões — {f.country}/{f.city}\n"
    content += "\n## Status\n\n"
    content += f"- Total de sessões: {len(sessions)}\n"
    content += f"- Com vídeo encontrado: {sum(1 for s in sessions if s.youtube_url)}\n"
    content += f"- Com transcript baixada: {sum(1 for s in sessions if s.status == 'transcript-downloaded')}\n"
    MAP.write_text(content, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-video", action="store_true")
    ap.add_argument("--no-transcripts", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    all_sessions: list[HistSession] = []
    for event in EVENTS:
        print(f"Fetching {event['id']}...")
        try:
            sessions = parse_overview(event)
        except Exception as e:
            print(f"  failed: {e}", file=sys.stderr)
            continue
        print(f"  {len(sessions)} sessions")
        all_sessions.extend(sessions)
    if args.limit:
        all_sessions = all_sessions[:args.limit]
    for i, s in enumerate(all_sessions, 1):
        print(f"[{i}/{len(all_sessions)}] {s.event_id} :: {s.session_title}")
        enrich_from_event_page(s)
        if not args.no_video:
            search_video(s)
            if s.youtube_url and not args.no_transcripts:
                download_transcript(s)
        write_note(s)
        time.sleep(0.1)
    write_event_indexes(all_sessions)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    manifest = MANIFEST_DIR / "kubecon-historical-observability.json"
    manifest.write_text(json.dumps([asdict(s) for s in all_sessions], ensure_ascii=False, indent=2), encoding="utf-8")
    print("Done")
    print("sessions", len(all_sessions))
    print("videos", sum(1 for s in all_sessions if s.youtube_url))
    print("transcripts", sum(1 for s in all_sessions if s.status == "transcript-downloaded"))
    print("manifest", manifest)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
