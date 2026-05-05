#!/usr/bin/env python3
"""Enrich Obsidian talk/session notes from YouTube metadata and transcripts.

Design goals:
- resumable: writes a JSONL progress file per dataset
- conservative matching: only accepts YouTube search results above threshold
- content-first: adds transcript-based summary, keywords, excerpt, and transcript path
- no external Python dependencies
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import time
import urllib.parse
from collections import Counter
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
YTDLP = ROOT / "bin" / "yt-dlp"
TRANSCRIPTS = ROOT / "_sources/transcripts/youtube-enriched"
MANIFESTS = ROOT / "_sources/manifests"

STOPWORDS = set('''
a an and are as at be by can could do does doing done for from get got had has have he her here him his how i if in into is it its just like may me more most much my not of on or our out over she so some than that the their them then there these they this those through to use using was we what when where which who why will with you your
about after also because before between build building cloud code community data demo different during example first going good great help into kind know kubernetes let look many need new now one open people problem project really right run see service services should show something start still system talk telemetry things think time tool tools two used users want way work would
'''.split())

KEYWORD_ALLOW = {
    'prometheus','opentelemetry','otel','kubernetes','kubecon','promcon','promql','metrics','metric','tracing','trace','logs','logging','profiling','slo','alertmanager','thanos','cortex','mimir','grafana','ebpf','collector','histogram','cardinality','remote','write','storage','security','platform','ai','llm','gpu','mesh','envoy','cilium','istio','gitops','argo','flux','operator','controller','cluster','observability','monitoring','sampling','latency','reliability','scaling','cost','wasm','serverless'
}

@dataclass
class Enrichment:
    dataset: str
    note_file: str
    title: str
    youtube_url: str | None = None
    youtube_id: str | None = None
    youtube_title: str | None = None
    video_match_score: float | None = None
    transcript_file: str | None = None
    transcript_chars: int = 0
    transcript_summary: str = ''
    keywords: list[str] | None = None
    status: str = 'pending'


def norm(s: str) -> str:
    s = html.unescape(s or '').lower()
    s = re.sub(r"[’'\"“”]", '', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def slug(s: str, n=90) -> str:
    s = norm(s).replace(' ', '-')
    return (s[:n].strip('-') or 'untitled')


def run_json(args: list[str], timeout=120) -> dict[str, Any] | None:
    try:
        p = subprocess.run(args, text=True, capture_output=True, timeout=timeout)
    except Exception:
        return None
    if not p.stdout.strip():
        return None
    try:
        return json.loads(p.stdout)
    except Exception:
        return None


def run_jsonl(args: list[str], timeout=150) -> list[dict[str, Any]]:
    try:
        p = subprocess.run(args, text=True, capture_output=True, timeout=timeout)
    except Exception:
        return []
    rows=[]
    for line in p.stdout.splitlines():
        try: rows.append(json.loads(line))
        except Exception: pass
    return rows


def extract_video_id(url: str | None) -> str | None:
    if not url: return None
    m = re.search(r'(?:v=|youtu\.be/|shorts/|live/)([A-Za-z0-9_-]{8,})', url)
    return m.group(1) if m else None


def search_video(title: str, year: Any, conference: str, speakers: list[str], threshold: float) -> tuple[str | None, str | None, float | None]:
    speaker_hint = ' '.join(speakers[:2])
    queries = [
        f'{title} {conference} {year} {speaker_hint}',
        f'{title} {conference} {year}',
        f'{title} CNCF',
    ]
    best=None
    for q in queries:
        rows=run_jsonl([str(YTDLP),'--flat-playlist','--dump-json',f'ytsearch4:{q}'])
        for r in rows:
            yt_title=r.get('title') or ''
            score=SequenceMatcher(None,norm(title),norm(yt_title)).ratio()
            channel=(r.get('channel') or r.get('uploader') or '').lower()
            if 'cncf' in channel or 'cloud native' in channel or 'prometheus' in channel:
                score += .08
            if str(year) and str(year) in yt_title:
                score += .02
            if conference.lower() in yt_title.lower():
                score += .04
            if best is None or score > best[0]:
                best=(score,r)
        if best and best[0] >= threshold + .08:
            break
    if best and best[0] >= threshold:
        r=best[1]
        return f"https://www.youtube.com/watch?v={r.get('id')}", r.get('title'), round(best[0],3)
    return None, None, None


def download_transcript(video_url: str, outdir: Path) -> tuple[Path | None, str]:
    outdir.mkdir(parents=True, exist_ok=True)
    vid=extract_video_id(video_url) or 'video'
    existing=sorted(outdir.glob(f'{vid}*.vtt'))
    if not existing:
        cmd=[str(YTDLP),'--skip-download','--write-subs','--write-auto-subs','--sub-langs','en.*,pt.*,es.*','--sub-format','vtt','-o',str(outdir/'%(id)s.%(ext)s'),video_url]
        subprocess.run(cmd, text=True, capture_output=True, timeout=240)
        existing=sorted(outdir.glob(f'{vid}*.vtt'))
    if not existing:
        return None, ''
    chosen = next((p for p in existing if '.en-orig.' in p.name), None) or next((p for p in existing if '.en.' in p.name), None) or existing[0]
    text=vtt_to_text(chosen.read_text(encoding='utf-8', errors='replace'))
    txt=outdir/f'{vid}.txt'
    txt.write_text(text, encoding='utf-8')
    return txt, text


def vtt_to_text(vtt: str) -> str:
    lines=[]; last=None
    for line in vtt.splitlines():
        line=line.strip()
        if not line or line == 'WEBVTT' or line.startswith(('Kind:','Language:')) or '-->' in line or re.fullmatch(r'\d+', line):
            continue
        line=html.unescape(re.sub(r'<[^>]+>','',line)).strip()
        if line and line != last:
            lines.append(line); last=line
    text=re.sub(r'\s+',' ',' '.join(lines)).strip()
    sentences=re.split(r'(?<=[.!?])\s+', text)
    paras=[]; buf=[]
    for s in sentences:
        buf.append(s)
        if sum(len(x) for x in buf) > 1000:
            paras.append(' '.join(buf)); buf=[]
    if buf: paras.append(' '.join(buf))
    return '\n\n'.join(paras)


def keywords(text: str, title: str) -> list[str]:
    words=re.findall(r'[a-zA-Z][a-zA-Z0-9+.-]{2,}', (title+' '+text).lower())
    words=[w.strip('.,') for w in words]
    c=Counter(w for w in words if w not in STOPWORDS and (w in KEYWORD_ALLOW or len(w)>5))
    return [w for w,_ in c.most_common(18)]


def transcript_summary(text: str, title: str) -> str:
    clean=re.sub(r'\s+',' ',text).strip()
    if not clean:
        return ''
    # YouTube auto-captions often have weak punctuation; make compact extractive chunks instead of trusting sentences.
    pseudo_sentences=re.split(r'(?<=[.!?])\s+', clean)
    chunks=[]
    for s in pseudo_sentences:
        s=s.strip()
        if not s:
            continue
        if len(s) > 320:
            words=s.split()
            for i in range(0, min(len(words), 220), 45):
                c=' '.join(words[i:i+45]).strip()
                if len(c) > 80: chunks.append(c)
        elif len(s) > 70:
            chunks.append(s)
    terms=['problem','challenge','architecture','opentelemetry','prometheus','kubernetes','metrics','tracing','logs','performance','scale','security','cost','reliability','demo','learn','design','query','storage','alert']
    picked=[]
    # opening context
    for c in chunks[:8]:
        picked.append(c)
        if len(picked) >= 2: break
    # thematic/high-signal chunks
    for c in chunks[8:]:
        cl=c.lower()
        if any(t in cl for t in terms) and c not in picked:
            picked.append(c)
        if len(picked) >= 6: break
    summary=' '.join(picked or chunks[:4]).strip()
    if len(summary) > 1400:
        summary=summary[:1397].rsplit(' ',1)[0]+'...'
    return summary


def append_section(note: Path, enr: Enrichment, transcript_text: str):
    original=note.read_text(encoding='utf-8', errors='replace')
    marker='## YouTube enrichment'
    if marker in original:
        original=original.split(marker)[0].rstrip()+"\n\n"
    excerpt=transcript_text[:2500].strip()
    section=f"""## YouTube enrichment

- YouTube: {enr.youtube_url or 'Não encontrado'}
- YouTube title: {enr.youtube_title or 'N/A'}
- Match score: {enr.video_match_score if enr.video_match_score is not None else 'N/A'}
- Transcript file: {enr.transcript_file or 'N/A'}
- Transcript chars: {enr.transcript_chars}
- Keywords: {', '.join(enr.keywords or [])}

### Resumo baseado na transcript

{enr.transcript_summary or '_Transcript indisponível; enriquecimento baseado apenas em metadados._'}

### Excerpt da transcript

{excerpt if excerpt else '_Sem transcript disponível._'}
"""
    note.write_text(original+section, encoding='utf-8')


def load_dataset(dataset: str) -> list[dict[str, Any]]:
    if dataset == 'promcon':
        return json.loads((MANIFESTS/'promcon.json').read_text())
    if dataset == 'kubecon':
        return json.loads((MANIFESTS/'kubecon-all-tracks.json').read_text())
    if dataset == 'kubecon-observability':
        return json.loads((MANIFESTS/'kubecon-historical-observability.json').read_text())
    raise SystemExit(f'unknown dataset: {dataset}')


def progress_path(dataset: str) -> Path:
    return MANIFESTS/f'youtube-enrichment-{dataset}.jsonl'


def load_done(path: Path) -> set[str]:
    done=set()
    if path.exists():
        for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
            try:
                r=json.loads(line)
                if r.get('status') in {'transcript-downloaded','video-found','video-not-found','transcript-missing'}:
                    done.add(r.get('note_file') or r.get('title'))
            except Exception:
                pass
    return done


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--dataset', choices=['promcon','kubecon','kubecon-observability'], required=True)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--threshold', type=float, default=0.62)
    ap.add_argument('--no-search', action='store_true', help='Only use existing youtube_url from manifest')
    ap.add_argument('--no-transcript', action='store_true')
    ap.add_argument('--track')
    ap.add_argument('--theme')
    ap.add_argument('--year', type=int)
    args=ap.parse_args()

    rows=load_dataset(args.dataset)
    if args.track:
        rows=[r for r in rows if norm(r.get('track','')) == norm(args.track)]
    if args.theme:
        rows=[r for r in rows if any(norm(t)==norm(args.theme) for t in (r.get('themes') or r.get('topics') or []))]
    if args.year:
        rows=[r for r in rows if int(r.get('year') or 0)==args.year]
    prog=progress_path(args.dataset)
    done=load_done(prog)
    pending=[r for r in rows if (r.get('note_file') or r.get('title')) not in done]
    if args.limit:
        pending=pending[:args.limit]
    print(f'dataset={args.dataset} selected={len(rows)} pending={len(pending)}', flush=True)
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    with prog.open('a', encoding='utf-8') as pf:
        for i,r in enumerate(pending,1):
            title=r.get('session_title') or r.get('title') or ''
            note_rel=r.get('note_file')
            note=ROOT/note_rel if note_rel else None
            if not note or not note.exists():
                continue
            year=r.get('year') or ''
            conference='PromCon' if args.dataset=='promcon' else 'KubeCon'
            speakers=r.get('speakers') or []
            youtube_url=r.get('youtube_url') or None
            youtube_title=r.get('youtube_title') or None
            score=r.get('video_match_score') or None
            if not youtube_url and not args.no_search:
                youtube_url,youtube_title,score=search_video(title, year, conference, speakers, args.threshold)
            enr=Enrichment(args.dataset, note_rel, title, youtube_url, extract_video_id(youtube_url), youtube_title, score)
            transcript=''
            if youtube_url and not args.no_transcript:
                outdir=TRANSCRIPTS/args.dataset/slug(str(year))/slug(title,70)
                txt, transcript=download_transcript(youtube_url, outdir)
                if txt:
                    enr.transcript_file=str(txt.relative_to(ROOT)); enr.transcript_chars=len(transcript); enr.status='transcript-downloaded'
                else:
                    enr.status='transcript-missing'
            elif youtube_url:
                enr.status='video-found'
            else:
                enr.status='video-not-found'
            enr.keywords=keywords(transcript, title) if transcript else keywords(r.get('description') or r.get('abstract') or '', title)
            enr.transcript_summary=transcript_summary(transcript, title)
            append_section(note,enr,transcript)
            pf.write(json.dumps(asdict(enr), ensure_ascii=False)+'\n'); pf.flush()
            print(f'[{i}/{len(pending)}] {enr.status}: {title[:90]}', flush=True)
            time.sleep(0.05)

if __name__ == '__main__':
    main()
