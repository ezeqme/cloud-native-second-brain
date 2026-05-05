#!/usr/bin/env python3
"""Bulk-index all official KubeCon + CloudNativeCon schedule tracks into Obsidian.

This creates structured source notes grouped by edition and track/theme. It is
metadata-first by design: schedule link, description, speakers, inferred topics,
summary, and a YouTube search URL. Actual YouTube resolution/transcript download
can be added later per track without turning the vault into an unreliable dump.
"""
from __future__ import annotations

import html, json, re, sys, time, urllib.request, urllib.parse
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "_sources/raw/kubecon-all-tracks"
MANIFESTS = ROOT / "_sources/manifests"
BASE = ROOT / "02-Sources/KubeCon-All-Tracks"
MAP = ROOT / "01-Maps/KubeCon All Tracks.md"

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
    {"id":"kccnceu2026", "year":2026, "region":"Europe", "city":"Amsterdam", "country":"Netherlands", "domain":"kccnceu2026.sched.com", "date":"2026-03-23/2026-03-26"},
]

THEME_RULES = {
  "AI ML": ["ai", "ml", "llm", "genai", "machine learning", "gpu", "inference", "agent"],
  "Observability": ["observability", "opentelemetry", "otel", "prometheus", "metrics", "tracing", "logs", "logging", "slo", "profil"],
  "Security": ["security", "secure", "policy", "supply chain", "sbom", "vulnerability", "zero trust", "identity"],
  "Platform Engineering": ["platform", "developer experience", "devex", "backstage", "golden path"],
  "Networking": ["network", "cilium", "envoy", "service mesh", "gateway", "ingress", "istio"],
  "Storage Data": ["storage", "database", "data", "postgres", "mysql", "kafka", "spark", "etcd"],
  "GitOps Delivery": ["gitops", "argo", "flux", "delivery", "deployment", "progressive"],
  "Runtime Containers": ["container", "runtime", "wasm", "webassembly", "cri-o", "containerd", "sandbox"],
  "Kubernetes Core": ["kubernetes", "scheduler", "controller", "operator", "cluster", "kubectl", "api server"],
  "SRE Reliability": ["reliability", "incident", "resilien", "sre", "scal", "performance", "capacity"],
  "Sustainability": ["sustainab", "carbon", "green", "energy"],
  "Community Governance": ["community", "governance", "maintainer", "contributor", "open source"],
}

@dataclass
class Session:
    event_id: str; edition: str; year: int; region: str; city: str; country: str; event_date: str
    title: str; session_title: str; speakers: list[str]; room: str; sched_url: str; schedule_url: str
    track: str = "Unclassified"; themes: list[str] | None = None; description: str = ""; summary: str = ""; slides: list[str] | None = None
    youtube_search_url: str = ""; note_file: str | None = None; status: str = "parsed"

def req(url: str, timeout=30) -> str:
    r = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(r, timeout=timeout) as resp: return resp.read().decode("utf-8", "replace")

def strip(s: str) -> str:
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I); s = re.sub(r"<.*?>", "", s, flags=re.S)
    return html.unescape(re.sub(r"[ \t]+", " ", s)).strip()

def slug(s: str, n=90) -> str:
    s = html.unescape(s).lower(); s = re.sub(r"[’']", "", s); s = re.sub(r"[^a-z0-9]+", "-", s); s = re.sub(r"-+", "-", s).strip("-")
    return (s[:n].strip("-") or "untitled")

def split_speakers(title: str):
    if " - " not in title: return title, []
    base, raw = title.rsplit(" - ", 1)
    return base.strip(), [p.strip() for p in re.split(r",| & |;", raw) if p.strip()]

def summarize(desc: str, title: str) -> str:
    text = re.sub(r"\s+", " ", desc).strip()
    if not text: return f"Sessão da KubeCon sobre {title}."
    ss = re.split(r"(?<=[.!?])\s+", text); out = " ".join(ss[:3]).strip()
    return out[:900].rsplit(" ",1)[0] + "..." if len(out) > 900 else out

def infer_themes(title: str, desc: str, track: str) -> list[str]:
    blob = (title + " " + desc + " " + track).lower()
    themes = [name for name, needles in THEME_RULES.items() if any(x in blob for x in needles)]
    return themes or [track if track != "Unclassified" else "Cloud Native"]

def parse_overview(ev: dict[str, Any]) -> list[Session]:
    url = f"https://{ev['domain']}/overview?iframe=no"
    RAW.mkdir(parents=True, exist_ok=True)
    overview_cache = RAW/f"{ev['id']}-overview.html"
    try:
        text = req(url, 45)
        overview_cache.write_text(text, encoding="utf-8")
    except Exception:
        if not overview_cache.exists():
            raise
        text = overview_cache.read_text(encoding="utf-8", errors="replace")
    pat = re.compile(r"<a href='([^']+)' class='name' id='[^']+'><span class=\"session-title\">(.*?)</span> <span class=\"vs\">(.*?)</span>", re.S)
    out=[]; seen={}
    def add_rows(page_text: str, track: str):
        for href, raw_title, raw_room in pat.findall(page_text):
            title=strip(raw_title); low=title.lower()
            if not title or any(x in low for x in ["break", "lunch", "registration", "reception", "booth crawl"]): continue
            key=href
            if key in seen: continue
            st, speakers = split_speakers(title)
            edition=f"KubeCon + CloudNativeCon {ev['region']} {ev['year']} - {ev['city']}, {ev['country']}"
            sched=f"https://{ev['domain']}/{href}"
            search="https://www.youtube.com/results?"+urllib.parse.urlencode({"search_query": f"{st} CNCF KubeCon {ev['year']}"})
            s=Session(ev['id'], edition, ev['year'], ev['region'], ev['city'], ev['country'], ev['date'], title, st, speakers, strip(raw_room), sched, url, track=track, youtube_search_url=search)
            seen[key]=s; out.append(s)
    # Prefer top-level official track pages so notes are separated by track without fetching every event detail.
    type_paths=[]
    for m in re.findall(r"type/([^\"'?#]+)", text):
        decoded=urllib.parse.unquote_plus(m)
        if '/' in decoded: continue
        if decoded.lower() in ['breaks','experiences']: continue
        if decoded not in type_paths: type_paths.append(decoded)
    for track in type_paths:
        enc=urllib.parse.quote_plus(track)
        turl=f"https://{ev['domain']}/overview/type/{enc}?iframe=no"
        cache = RAW/f"{ev['id']}-type-{slug(track,50)}.html"
        try:
            ttext=req(turl, 30)
            cache.write_text(ttext, encoding='utf-8')
            add_rows(ttext, track)
        except Exception:
            if cache.exists():
                add_rows(cache.read_text(encoding='utf-8', errors='replace'), track)
    # Fallback: anything not represented in top-level type pages.
    add_rows(text, 'Unclassified')
    return out

def enrich(s: Session):
    try: page=req(s.sched_url + ("&iframe=no" if "?" in s.sched_url else "?iframe=no"), 30)
    except Exception as e: s.status=f"fetch-failed:{type(e).__name__}"; return
    (RAW/f"{s.event_id}-{slug(s.session_title,55)}.html").write_text(page, encoding="utf-8")
    m=re.search(r'<div class="tip-description">(.*?)</div>\s*</div>', page, re.S)
    if m: s.description=strip(m.group(1)); s.description=re.sub(r"^Speakers\s+", "", s.description).strip()
    types=re.findall(r'href="type/([^"]+)">(?:<span.*?</span>\s*)?([^<]+)</a>', page, re.S)
    if types:
        s.track=strip(types[0][1]) or urllib.parse.unquote(types[0][0])
    slides=re.findall(r'<a class="file-uploaded[^"]*" href="([^"]+)"', page)
    s.slides=[html.unescape(x) for x in slides]
    s.summary=summarize(s.description, s.session_title)
    s.themes=infer_themes(s.title, s.description, s.track)

def ylist(items): return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in (items or [])) + "]"

def write_note(s: Session):
    evdir=BASE/f"{s.year}-{slug(s.region)}-{slug(s.city)}"/slug(s.track,70)/"Sessions"; evdir.mkdir(parents=True, exist_ok=True)
    import hashlib
    event_code = slug(s.sched_url.rstrip('/').split('/')[-1], 24)
    event_hash = hashlib.sha1(s.sched_url.encode('utf-8')).hexdigest()[:8]
    p=evdir/f"{slug(s.session_title,64)}--{event_code}-{event_hash}.md"
    body=f"""---
type: kubecon-session
event: {json.dumps(s.edition, ensure_ascii=False)}
event_id: {s.event_id}
year: {s.year}
region: {json.dumps(s.region, ensure_ascii=False)}
city: {json.dumps(s.city, ensure_ascii=False)}
country: {json.dumps(s.country, ensure_ascii=False)}
event_date: {json.dumps(s.event_date, ensure_ascii=False)}
track: {json.dumps(s.track, ensure_ascii=False)}
themes: {ylist(s.themes)}
speakers: {ylist(s.speakers)}
sched_url: {s.sched_url}
youtube_search_url: {s.youtube_search_url}
slides: {ylist(s.slides)}
status: {s.status}
---

# {s.title}

## Identificação

- Edição: {s.edition}
- Trilha oficial: [[{s.track}]]
- Temas: {', '.join('[['+x+']]' for x in (s.themes or []))}
- País/cidade: {s.country} / {s.city}
- Speakers: {', '.join(s.speakers) if s.speakers else 'N/A'}
- Schedule: {s.sched_url}
- Busca YouTube: {s.youtube_search_url}

## Resumo

{s.summary}

## Descrição oficial

{s.description or '_Descrição oficial não encontrada._'}

## Links

- Schedule oficial: {s.sched_url}
- YouTube search: {s.youtube_search_url}
"""
    for x in s.slides or []: body += f"- Slides: {x}\n"
    p.write_text(body, encoding="utf-8"); s.note_file=str(p.relative_to(ROOT))

def write_indexes(rows: list[Session]):
    from collections import defaultdict
    by_event=defaultdict(list); by_track=defaultdict(list); by_theme=defaultdict(list)
    for s in rows:
        by_event[s.event_id].append(s); by_track[s.track].append(s)
        for t in s.themes or []: by_theme[t].append(s)
    content="# KubeCon All Tracks\n\nÍndice metadata-first de todas as trilhas oficiais das edições KubeCon + CloudNativeCon mapeadas.\n\n"
    content+=f"- Sessões indexadas: {len(rows)}\n- Edições: {len(by_event)}\n- Trilhas oficiais: {len(by_track)}\n- Temas inferidos: {len(by_theme)}\n\n## Por edição\n\n"
    for eid, ss in sorted(by_event.items(), key=lambda kv:(kv[1][0].year, kv[1][0].region, kv[1][0].city)):
        f=ss[0]; content+=f"- {f.edition}: {len(ss)} sessões\n"
    content += "\n## Por trilha oficial\n\n"
    for tr, ss in sorted(by_track.items(), key=lambda kv:(-len(kv[1]), kv[0])):
        content+=f"- [[{tr}]] — {len(ss)} sessões\n"
    content += "\n## Por tema inferido\n\n"
    for th, ss in sorted(by_theme.items(), key=lambda kv:(-len(kv[1]), kv[0])):
        content+=f"- [[{th}]] — {len(ss)} sessões\n"
    MAP.write_text(content, encoding="utf-8")
    # Theme map files
    tdir=ROOT/"01-Maps/KubeCon-Themes"; tdir.mkdir(parents=True, exist_ok=True)
    for th, ss in by_theme.items():
        txt=f"# {th}\n\nSessões KubeCon classificadas neste tema.\n\n"
        for s in sorted(ss, key=lambda x:(x.year,x.region,x.session_title)):
            txt+=f"- [[{Path(s.note_file).stem}|{s.session_title}]] — {s.edition} / {s.track}\n"
        (tdir/f"{slug(th)}.md").write_text(txt, encoding="utf-8")

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--limit', type=int, default=0); ap.add_argument('--event', action='append'); ap.add_argument('--fast', action='store_true', help='Do not fetch each event page; infer track/themes from overview CSS/title only.')
    args=ap.parse_args(); events=[e for e in EVENTS if not args.event or e['id'] in args.event]
    rows=[]
    for ev in events:
        print(f"Fetching {ev['id']}...", flush=True)
        try: ss=parse_overview(ev)
        except Exception as e: print('failed', ev['id'], e, file=sys.stderr); continue
        print(f"  {len(ss)} sessions", flush=True); rows.extend(ss)
    if args.limit: rows=rows[:args.limit]
    for i,s in enumerate(rows,1):
        if i%25==1 or i==len(rows): print(f"Enrich {i}/{len(rows)}", flush=True)
        if args.fast:
            s.summary=summarize('', s.session_title)
            s.themes=infer_themes(s.title, '', s.track)
        else:
            enrich(s)
        write_note(s); time.sleep(0.005 if args.fast else 0.03)
    write_indexes(rows); MANIFESTS.mkdir(parents=True, exist_ok=True)
    out=MANIFESTS/'kubecon-all-tracks.json'; out.write_text(json.dumps([asdict(x) for x in rows], ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done', len(rows), 'manifest', out, flush=True)
if __name__=='__main__': main()
