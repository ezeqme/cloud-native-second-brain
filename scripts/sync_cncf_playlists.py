#!/usr/bin/env python3
"""Synchronize CNCF YouTube playlists with Obsidian session notes.

Initial scope is intentionally conservative: scan CNCF playlists, select playlists
by title/id, reconcile YouTube IDs in existing notes, create missing notes, and
add keyword/topic metadata for Obsidian correlation.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
YTDLP = ROOT / "bin" / "yt-dlp"
RAW = ROOT / "_sources/raw"
MANIFESTS = ROOT / "_sources/manifests"
TRANSCRIPTS = ROOT / "_sources/transcripts/youtube-playlists"
OBS_DAY_DIR = ROOT / "02-Sources/KubeCon/2026-Europe-Amsterdam/Observability-Day/Sessions"
OBS_EVENT = ROOT / "02-Sources/KubeCon/2026-Europe-Amsterdam/Observability-Day/KubeCon Europe 2026 Amsterdam - Observability Day.md"

STOPWORDS = set('''
a an and are as at be by can could do does doing done for from get got had has have he her here him his how i if in into is it its just like may me more most much my not of on or our out over she so some than that the their them then there these they this those through to use using was we what when where which who why will with you your
about after also because before between build building cloud code community data demo different during example first going good great help into kind know let look many need new now one open people problem project really right run see service services should show something start still system talk things think time tool tools two used users want way work would
all already anyone anything applause around back basically come coming cool course day did didnt doesnt dont every everybody everyone few fine gonna here hey hi lot maybe mean okay please probably quite say says session sort take thank thanks thats theyre today together very yeah yes youre
'''.split())

TOPIC_RULES = {
    "OpenTelemetry": ["opentelemetry", "otel", "opamp", "otlp", "semantic convention", "weaver", "baggage"],
    "Collectors": ["collector", "collectors", "gateway", "gateways", "pipeline", "pipelines", "wasm"],
    "Metrics": ["metric", "metrics", "prometheus", "promql", "histogram", "cardinality", "exemplar", "sketch"],
    "Tracing": ["trace", "tracing", "span", "spans", "baggage"],
    "Logging": ["log", "logs", "logging"],
    "Profiling": ["profiling", "profile", "profiles"],
    "SLOs": ["slo", "slos", "sli", "error budget"],
    "Cost Optimization": ["cost", "cardinality", "sampling", "carbon", "pue", "sustainable", "efficiency"],
    "eBPF": ["ebpf", "cilium", "hubble", "tetragon"],
    "Kubernetes": ["kubernetes", "k8s", "pod", "pods", "ingress", "cluster", "clusters"],
    "AI Observability": ["ai", "agent", "agents", "llm", "genai", "autoremediation"],
    "Sustainability": ["carbon", "sustainable", "sustainability", "pue", "energy"],
    "Security": ["security", "pii", "redact", "redaction", "policy", "zero trust"],
}

@dataclass
class Video:
    index: int
    video_id: str
    title: str
    url: str
    duration: int | None = None
    playlist_title: str = ""
    playlist_id: str = ""


def norm(s: str) -> str:
    s = html.unescape(s or "").lower()
    s = re.sub(r"[’'\"“”]", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def slug(s: str, max_len: int = 110) -> str:
    out = re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-")
    return (out[:max_len].strip("-") or "untitled")


def run_jsonl(args: list[str], timeout: int = 300) -> list[dict[str, Any]]:
    p = subprocess.run(args, text=True, capture_output=True, timeout=timeout)
    rows = []
    for line in p.stdout.splitlines():
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
    return rows


def scan_cncf_playlists() -> list[dict[str, Any]]:
    RAW.mkdir(parents=True, exist_ok=True)
    rows = run_jsonl([str(YTDLP), "--flat-playlist", "--dump-json", "https://www.youtube.com/@cncf/playlists"], timeout=600)
    (RAW / "cncf-playlists.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    return rows


def playlist_videos(url_or_id: str, title_hint: str = "") -> list[Video]:
    url = url_or_id if url_or_id.startswith("http") else f"https://www.youtube.com/playlist?list={url_or_id}"
    rows = run_jsonl([str(YTDLP), "--flat-playlist", "--dump-json", url], timeout=600)
    videos = []
    for i, r in enumerate(rows, 1):
        vid = r.get("id")
        title = r.get("title") or ""
        if not vid or not title:
            continue
        videos.append(Video(
            index=i,
            video_id=vid,
            title=html.unescape(title),
            url=f"https://www.youtube.com/watch?v={vid}",
            duration=r.get("duration"),
            playlist_title=title_hint or r.get("playlist_title") or r.get("playlist") or "",
            playlist_id=r.get("playlist_id") or re.sub(r".*list=", "", url),
        ))
    return videos


def extract_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text
    fm_text = text[4:end]
    body = text[end+5:].lstrip("\n")
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body


def replace_frontmatter(text: str, updates: dict[str, Any]) -> str:
    fm, body = extract_frontmatter(text)
    ordered = []
    if text.startswith("---\n"):
        original = text[4:text.find("\n---", 4)].splitlines()
        seen = set()
        for line in original:
            if ":" in line and not line.startswith(" "):
                key = line.split(":", 1)[0].strip()
                if key in updates:
                    ordered.append(format_yaml_line(key, updates[key])); seen.add(key)
                else:
                    ordered.append(line); seen.add(key)
            else:
                ordered.append(line)
        for key, value in updates.items():
            if key not in seen:
                ordered.append(format_yaml_line(key, value))
    else:
        for key, value in updates.items():
            ordered.append(format_yaml_line(key, value))
    return "---\n" + "\n".join(ordered) + "\n---\n\n" + body


def format_yaml_line(key: str, value: Any) -> str:
    if isinstance(value, list):
        return f"{key}: [" + ", ".join(json.dumps(x, ensure_ascii=False) for x in value) + "]"
    if value is None:
        return f"{key}: "
    if isinstance(value, (int, float)):
        return f"{key}: {value}"
    return f"{key}: {json.dumps(str(value), ensure_ascii=False)}"


def note_title(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:80]:
            if line.startswith("# "):
                return line[2:].strip()
    except Exception:
        pass
    return path.stem.replace("-", " ")


def build_note_index() -> tuple[dict[str, Path], list[tuple[Path, str]]]:
    by_id = {}
    titled = []
    for path in (ROOT / "02-Sources").rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"(?:youtube_id:\s*|v=)([A-Za-z0-9_-]{11})", text):
            by_id.setdefault(m.group(1), path)
        titled.append((path, note_title(path)))
    return by_id, titled


def find_best_note(video: Video, by_id: dict[str, Path], titled: list[tuple[Path, str]], prefer_dir: Path) -> tuple[Path | None, float]:
    """Find note for a playlist video.

    Prefer an event-local title match over a global exact-ID match. This matters
    when an old broad KubeCon note was incorrectly enriched with a co-located
    event video ID, while the dedicated Observability Day note exists under the
    event directory.
    """
    best: tuple[float, Path] | None = None
    best_preferred: tuple[float, Path] | None = None
    vnorm = norm(video.title)
    for path, title in titled:
        tnorm = norm(title)
        score = SequenceMatcher(None, vnorm, tnorm).ratio()
        if "observability day" in vnorm and "observability day" in tnorm:
            score += 0.04
        for marker in ("welcome", "opening", "closing", "project updates"):
            if (marker in vnorm) != (marker in tnorm):
                score -= 0.18
        if prefer_dir in path.parents:
            preferred_score = score + 0.08
            if best_preferred is None or preferred_score > best_preferred[0]:
                best_preferred = (preferred_score, path)
        if best is None or score > best[0]:
            best = (score, path)
    if best_preferred and best_preferred[0] >= 0.72:
        return best_preferred[1], round(best_preferred[0], 3)
    if video.video_id in by_id:
        id_path = by_id[video.video_id]
        # Avoid cross-event contamination: a reused/previously wrong ID in a
        # different event directory must not steal this playlist entry. Generic
        # titles like "Project Updates" recur across years.
        if prefer_dir in id_path.parents:
            return id_path, 1.0
        title_score = SequenceMatcher(None, vnorm, norm(note_title(id_path))).ratio()
        return None, round(title_score, 3)
    # Do not title-match into another event directory. If the preferred event
    # directory has no good note, create a local note instead.
    return None, best[0] if best else 0.0


def vtt_to_text(vtt: str) -> str:
    lines=[]; last=None
    for line in vtt.splitlines():
        line=line.strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:")) or "-->" in line or re.fullmatch(r"\d+", line):
            continue
        line=html.unescape(re.sub(r"<[^>]+>", "", line)).strip()
        if line and line != last:
            lines.append(line); last=line
    text=re.sub(r"\s+", " ", " ".join(lines)).strip()
    paras=[]; buf=[]
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        buf.append(sentence)
        if sum(len(x) for x in buf) > 900:
            paras.append(" ".join(buf)); buf=[]
    if buf: paras.append(" ".join(buf))
    return "\n\n".join(paras)


def download_transcript(video: Video, note_slug: str) -> tuple[str, int]:
    outdir = TRANSCRIPTS / slug(video.playlist_title or "cncf-playlist") / note_slug
    outdir.mkdir(parents=True, exist_ok=True)
    txt = outdir / f"{video.video_id}.txt"
    if txt.exists() and txt.stat().st_size > 100:
        rel = str(txt.relative_to(ROOT)); return rel, len(txt.read_text(encoding="utf-8", errors="replace"))
    cmd = [str(YTDLP), "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*", "--sub-format", "vtt", "-o", str(outdir / "%(id)s.%(ext)s"), video.url]
    subprocess.run(cmd, text=True, capture_output=True, timeout=240)
    candidates = sorted(outdir.glob(f"{video.video_id}*.vtt"))
    if not candidates:
        return "", 0
    chosen = next((p for p in candidates if ".en-orig." in p.name), None) or next((p for p in candidates if ".en." in p.name), None) or candidates[0]
    text = vtt_to_text(chosen.read_text(encoding="utf-8", errors="replace"))
    txt.write_text(text, encoding="utf-8")
    rel = str(txt.relative_to(ROOT))
    return rel, len(text)


def infer_keywords(title: str, transcript: str) -> list[str]:
    raw_words = re.findall(r"[a-zA-Z][a-zA-Z0-9+-]{2,}", (title + " " + transcript[:12000]).lower())
    allowed = {needle.split()[0] for needles in TOPIC_RULES.values() for needle in needles}
    def keep(w: str) -> bool:
        if w in STOPWORDS:
            return False
        if w in allowed:
            return True
        return len(w) >= 6
    c = Counter(w for w in raw_words if keep(w))
    # Boost known observability terms.
    for topic, needles in TOPIC_RULES.items():
        for needle in needles:
            token = needle.split()[0]
            if token in c:
                c[token] += 8
    return [w for w, _ in c.most_common(24)]


def infer_topics(title: str, transcript: str, keywords: list[str]) -> list[str]:
    hay = norm(title + " " + " ".join(keywords) + " " + transcript[:4000])
    topics = []
    for topic, needles in TOPIC_RULES.items():
        if any(n in hay for n in needles):
            topics.append(topic)
    return topics or ["Observability"]


def update_note(path: Path, video: Video, match_score: float, transcript_file: str, transcript_chars: int, keywords: list[str], topics: list[str]) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    updates = {
        "youtube_url": video.url,
        "youtube_id": video.video_id,
        "playlist": video.playlist_title,
        "playlist_id": video.playlist_id,
        "playlist_index": video.index,
        "match_score": match_score,
        "keywords": keywords,
        "topics": topics,
        "status": "transcript-downloaded" if transcript_file else "transcript-missing",
    }
    if transcript_file:
        updates["transcript_file"] = transcript_file
    text = replace_frontmatter(text, updates)
    # Metadata lines: keep human-readable area consistent.
    text = re.sub(r"- YouTube: .*", f"- YouTube: {video.url}", text)
    text = re.sub(r"- Topics: .*", "- Topics: " + ", ".join(f"[[{t}]]" for t in topics), text)
    related = "## Related keywords\n\n" + " ".join(f"[[{kw}]]" for kw in keywords[:12]) + "\n"
    if "## Related keywords" in text:
        text = re.sub(r"## Related keywords\n\n.*?(?=\n## |\Z)", related.rstrip()+"\n", text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + related
    # If transcript is clearly wrong or missing, replace transcript section when we have a transcript.
    if transcript_file:
        transcript = (ROOT / transcript_file).read_text(encoding="utf-8", errors="replace")
        new_section = "## Transcript\n\n" + (transcript or "_Transcript not available yet._") + "\n\n"
        if "## Transcript" in text:
            text = re.sub(r"## Transcript\n\n.*?(?=\n## |\Z)", new_section.rstrip()+"\n\n", text, flags=re.S)
        else:
            text += "\n" + new_section
    path.write_text(text, encoding="utf-8")
    return str(path.relative_to(ROOT))


def infer_year(video: Video) -> int:
    m = re.search(r"\b(20\d{2})\b", video.playlist_title or video.title)
    return int(m.group(1)) if m else 2026


def create_note(video: Video, transcript_file: str, transcript_chars: int, keywords: list[str], topics: list[str], outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    base_title = re.sub(r"\s+-\s+.*$", "", video.title).strip() or video.title
    path = outdir / f"{slug(base_title)}.md"
    n = 2
    while path.exists():
        path = outdir / f"{slug(base_title)}-{n}.md"; n += 1
    transcript = (ROOT / transcript_file).read_text(encoding="utf-8", errors="replace") if transcript_file else ""
    speakers = []
    if " - " in video.title:
        speakers = [s.strip() for s in re.split(r",| & |;", video.title.rsplit(" - ", 1)[1]) if s.strip()]
    year = infer_year(video)
    body = f"""---
type: session
event: "{video.playlist_title}"
year: {year}
kind: session
youtube_url: {video.url}
youtube_id: {video.video_id}
playlist: "{video.playlist_title}"
playlist_id: {video.playlist_id}
playlist_index: {video.index}
speakers: {json.dumps(speakers, ensure_ascii=False)}
topics: {json.dumps(topics, ensure_ascii=False)}
keywords: {json.dumps(keywords, ensure_ascii=False)}
transcript_file: {transcript_file}
transcript_chars: {transcript_chars}
status: {"transcript-downloaded" if transcript_file else "transcript-missing"}
---

# {video.title}

## Metadata

- YouTube: {video.url}
- Playlist: {video.playlist_title}
- Speakers: {', '.join(speakers) if speakers else 'N/A'}
- Topics: {', '.join('[[' + t + ']]' for t in topics)}

## Transcript

{transcript if transcript else '_Transcript not available yet._'}

## Related keywords

{' '.join(f'[[{kw}]]' for kw in keywords[:12])}

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
"""
    path.write_text(body, encoding="utf-8")
    return path


def write_event_note(videos: list[Video], note_paths: dict[str, str]) -> None:
    if not OBS_EVENT.exists():
        return
    lines = ["# KubeCon Europe 2026 Amsterdam - Observability Day", "", "- Type: event", "- Event date: 2026-03-23", "- Location: Amsterdam, The Netherlands", "- Parent event: KubeCon + CloudNativeCon Europe 2026", "- Source playlist: https://www.youtube.com/playlist?list=PLeAHoVP1opzM1cBlt5cQ_EEkw_eotxRyx", "- Video channel: https://www.youtube.com/@cncf", "", "## Sessions", ""]
    for v in videos:
        rel = note_paths.get(v.video_id, "")
        stem = Path(rel).stem if rel else slug(v.title)
        lines.append(f"- ✅ [[{stem}|{v.title}]] — `{v.video_id}`")
    OBS_EVENT.write_text("\n".join(lines)+"\n", encoding="utf-8")


def sync_playlist(playlist_url: str, playlist_title: str, outdir: Path = OBS_DAY_DIR, create_missing: bool = True, update_event_note: bool = True) -> list[dict[str, Any]]:
    videos = playlist_videos(playlist_url, playlist_title)
    by_id, titled = build_note_index()
    results=[]; note_paths={}
    for v in videos:
        path, score = find_best_note(v, by_id, titled, outdir)
        action = "updated"
        if not path and create_missing:
            note_slug = slug(re.sub(r"\s+-\s+.*$", "", v.title))
            transcript_file, transcript_chars = download_transcript(v, note_slug)
            transcript = (ROOT / transcript_file).read_text(encoding="utf-8", errors="replace") if transcript_file else ""
            kws = infer_keywords(v.title, transcript)
            topics = infer_topics(v.title, transcript, kws)
            path = create_note(v, transcript_file, transcript_chars, kws, topics, outdir)
            action = "created"
        elif path:
            note_slug = path.stem
            transcript_file, transcript_chars = download_transcript(v, note_slug)
            transcript = (ROOT / transcript_file).read_text(encoding="utf-8", errors="replace") if transcript_file else ""
            kws = infer_keywords(v.title, transcript)
            topics = infer_topics(v.title, transcript, kws)
            rel = update_note(path, v, score, transcript_file, transcript_chars, kws, topics)
            action = "updated" if score < 1 else "verified"
        else:
            rel = ""
            kws=[]; topics=[]; transcript_file=""; transcript_chars=0
            action = "missing"
        rel = str(path.relative_to(ROOT)) if path else ""
        note_paths[v.video_id] = rel
        results.append({"action": action, "video": asdict(v), "note_file": rel, "match_score": score, "keywords": kws, "topics": topics, "transcript_file": transcript_file, "transcript_chars": transcript_chars})
        by_id[v.video_id] = path if path else by_id.get(v.video_id)  # keep index warm
    if update_event_note and outdir == OBS_DAY_DIR:
        write_event_note(videos, note_paths)
    return results


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-playlists", action="store_true", help="scan @cncf/playlists into _sources/raw/cncf-playlists.jsonl")
    ap.add_argument("--playlist-url", default="https://www.youtube.com/playlist?list=PLeAHoVP1opzM1cBlt5cQ_EEkw_eotxRyx")
    ap.add_argument("--playlist-title", default="Observability Day Europe 2026")
    ap.add_argument("--outdir", default=str(OBS_DAY_DIR), help="directory where missing notes should be created and local title matches preferred")
    ap.add_argument("--no-event-note", action="store_true", help="do not rewrite the Observability Day event note")
    args = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True); MANIFESTS.mkdir(parents=True, exist_ok=True)
    if args.scan_playlists:
        rows = scan_cncf_playlists()
        print(f"Scanned {len(rows)} CNCF playlists")
    outdir = Path(args.outdir)
    if not outdir.is_absolute():
        outdir = ROOT / outdir
    results = sync_playlist(args.playlist_url, args.playlist_title, outdir=outdir, update_event_note=not args.no_event_note)
    out = MANIFESTS / f"cncf-playlist-sync-{slug(args.playlist_title, 80)}.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = defaultdict(int)
    for r in results: counts[r["action"]] += 1
    print("Synced", len(results), "videos", dict(counts), "manifest", out.relative_to(ROOT))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
