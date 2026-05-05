#!/usr/bin/env python3
"""Index PromCon editions from promcon.io into Obsidian."""
from __future__ import annotations
import html,json,re,subprocess,urllib.request,urllib.parse,time
from dataclasses import asdict,dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_sources/raw/promcon'; MANIFESTS=ROOT/'_sources/manifests'; BASE=ROOT/'02-Sources/PromCon'; MAP=ROOT/'01-Maps/PromCon.md'; YTDLP=ROOT/'bin/yt-dlp'
EDITIONS=[
 {'id':'2016-berlin','year':2016,'name':'PromCon 2016','city':'Berlin','country':'Germany','url':'https://promcon.io/2016-berlin/'},
 {'id':'2017-munich','year':2017,'name':'PromCon 2017','city':'Munich','country':'Germany','url':'https://promcon.io/2017-munich/'},
 {'id':'2018-munich','year':2018,'name':'PromCon 2018','city':'Munich','country':'Germany','url':'https://promcon.io/2018-munich/'},
 {'id':'2019-munich','year':2019,'name':'PromCon EU 2019','city':'Munich','country':'Germany','url':'https://promcon.io/2019-munich/'},
 {'id':'2020-online','year':2020,'name':'PromCon Online 2020','city':'Online','country':'Online','url':'https://promcon.io/2020-online/'},
 {'id':'2021-online','year':2021,'name':'PromCon Online 2021','city':'Online','country':'Online','url':'https://promcon.io/2021-online/'},
 {'id':'2021-losangeles','year':2021,'name':'PromCon NA 2021','city':'Los Angeles','country':'United States','url':'https://promcon.io/2021-losangeles/'},
 {'id':'2022-munich','year':2022,'name':'PromCon EU 2022','city':'Munich','country':'Germany','url':'https://promcon.io/2022-munich/'},
 {'id':'2023-berlin','year':2023,'name':'PromCon EU 2023','city':'Berlin','country':'Germany','url':'https://promcon.io/2023-berlin/'},
 {'id':'2024-berlin','year':2024,'name':'PromCon EU 2024','city':'Berlin','country':'Germany','url':'https://promcon.io/2024-berlin/'},
 {'id':'2025-munich','year':2025,'name':'PromCon EU 2025','city':'Munich','country':'Germany','url':'https://promcon.io/2025-munich/'},
]
TOPICS={
 'Prometheus Core':['prometheus 3','prometheus','promql','tsdb','scrape','rules','alertmanager'],
 'Metrics':['metric','histogram','counter','gauge','native histogram'],
 'Remote Write Storage':['remote write','remote read','thanos','cortex','mimir','storage','long-term'],
 'Alerting':['alert','alertmanager','on-call'],
 'OpenTelemetry':['opentelemetry','otel'],
 'Kubernetes':['kubernetes','k8s','operator','cluster'],
 'Scalability Reliability':['scale','scaling','reliability','performance','limits','ha','capacity'],
 'Visualization Dashboards':['grafana','dashboard','visualization','perses'],
 'Cost Optimization':['cost','efficient','cardinality'],
 'Community':['community','maintainer','governance'],
}
@dataclass
class Talk:
    edition_id:str; edition:str; year:int; city:str; country:str; title:str; speakers:list[str]; url:str; abstract:str=''; summary:str=''; topics:list[str]|None=None; youtube_url:str|None=None; youtube_title:str|None=None; video_match_score:float|None=None; note_file:str|None=None; status:str='parsed'

def req(url):
 r=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}); return urllib.request.urlopen(r,timeout=30).read().decode('utf-8','replace')
def strip(s):
 s=re.sub(r'<br\s*/?>','\n',s,flags=re.I); s=re.sub(r'<.*?>','',s,flags=re.S); return html.unescape(re.sub(r'[ \t]+',' ',s)).strip()
def slug(s,n=90):
 s=html.unescape(s).lower(); s=re.sub(r"[’']",'',s); s=re.sub(r'[^a-z0-9]+','-',s); s=re.sub(r'-+','-',s).strip('-'); return (s[:n].strip('-') or 'untitled')
def norm(s): return re.sub(r'[^a-z0-9]+',' ',strip(s).lower()).strip()
def summary(a,t):
 x=re.sub(r'\s+',' ',a).strip()
 if not x: return f'Talk da PromCon sobre {t}.'
 ss=re.split(r'(?<=[.!?])\s+',x); out=' '.join(ss[:3]); return out[:800].rsplit(' ',1)[0]+'...' if len(out)>800 else out
def topics(title,abstract):
 blob=(title+' '+abstract).lower(); out=[k for k,v in TOPICS.items() if any(n in blob for n in v)]; return out or ['Prometheus']
def parse_schedule(ed):
 url=ed['url'].rstrip('/')+'/schedule/'; text=req(url); RAW.mkdir(parents=True,exist_ok=True); (RAW/f"{ed['id']}-schedule.html").write_text(text,encoding='utf-8')
 hrefs=[]
 for h in re.findall(r'href="([^"]*talks/[^"]+)"', text):
  h=h.rstrip('/')+'/'
  if h not in hrefs: hrefs.append(h)
 talks=[]
 for h in hrefs:
  full=urllib.parse.urljoin(url,h)
  if any(x in full for x in ['/welcome/','/closing','/break']): pass
  try: page=req(full)
  except Exception: continue
  (RAW/f"{ed['id']}-{slug(full.split('/talks/')[-1],60)}.html").write_text(page,encoding='utf-8')
  m=re.search(r'<h3>Talk abstract</h3>(.*?)(?:<h3 id="speakers">|<h3>Speakers</h3>|<a class="btn)',page,re.S|re.I)
  block=m.group(1) if m else ''
  hm=re.search(r'<h2[^>]*>(.*?)</h2>',block,re.S); title=strip(hm.group(1)) if hm else slug(full.split('/talks/')[-1]).replace('-',' ').title()
  abs_block=re.sub(r'<h2[^>]*>.*?</h2>','',block,flags=re.S)
  abstract=strip(abs_block)
  sp=[]
  sm=re.search(r'<h3 id="speakers">.*?</h3>(.*?)(?:<a class="btn|</div>)',page,re.S|re.I)
  if sm:
   sp=[strip(x) for x in re.findall(r'<a [^>]*>(.*?)</a>',sm.group(1),re.S) if strip(x)]
  t=Talk(ed['id'],ed['name'],ed['year'],ed['city'],ed['country'],title,sp,full,abstract,summary(abstract,title)); t.topics=topics(title,abstract); talks.append(t)
 return talks
def run_jsonl(args):
 try: p=subprocess.run(args,text=True,capture_output=True,timeout=120)
 except Exception: return []
 out=[]
 for l in p.stdout.splitlines():
  try: out.append(json.loads(l))
  except Exception: pass
 return out
def find_video(t:Talk):
 if not YTDLP.exists(): return
 q=f'{t.title} PromCon {t.year} Prometheus'
 best=None
 for r in run_jsonl([str(YTDLP),'--flat-playlist','--dump-json',f'ytsearch4:{q}']):
  title=r.get('title') or ''; score=SequenceMatcher(None,norm(t.title),norm(title)).ratio()
  chan=(r.get('channel') or r.get('uploader') or '').lower()
  if 'prometheus' in chan: score+=.08
  if 'promcon' in title.lower(): score+=.05
  if best is None or score>best[0]: best=(score,r)
 if best and best[0]>=.55:
  r=best[1]; t.youtube_url=f"https://www.youtube.com/watch?v={r.get('id')}"; t.youtube_title=r.get('title'); t.video_match_score=round(best[0],3); t.status='video-found'
def ylist(xs): return '['+', '.join(json.dumps(x,ensure_ascii=False) for x in (xs or []))+']'
def write_note(t:Talk):
 d=BASE/f"{t.year}-{slug(t.edition_id)}"/'Sessions'; d.mkdir(parents=True,exist_ok=True); p=d/f"{slug(t.title)}.md"
 search='https://www.youtube.com/results?'+urllib.parse.urlencode({'search_query':f'{t.title} PromCon {t.year}'})
 body=f"""---
type: promcon-talk
conference: PromCon
edition: {json.dumps(t.edition, ensure_ascii=False)}
edition_id: {t.edition_id}
year: {t.year}
city: {json.dumps(t.city, ensure_ascii=False)}
country: {json.dumps(t.country, ensure_ascii=False)}
topics: {ylist(t.topics)}
speakers: {ylist(t.speakers)}
source_url: {t.url}
youtube_url: {t.youtube_url or ''}
youtube_search_url: {search}
video_match_score: {t.video_match_score or ''}
status: {t.status}
---

# {t.title}

## Identificação

- Edição: {t.edition}
- País/cidade: {t.country} / {t.city}
- Temas: {', '.join('[['+x+']]' for x in (t.topics or []))}
- Speakers: {', '.join(t.speakers) if t.speakers else 'N/A'}
- Página oficial: {t.url}
- YouTube: {t.youtube_url or search}

## Resumo

{t.summary}

## Abstract oficial

{t.abstract or '_Abstract não encontrado._'}

## Links

- Página oficial: {t.url}
- YouTube: {t.youtube_url or search}
"""
 p.write_text(body,encoding='utf-8'); t.note_file=str(p.relative_to(ROOT))
def write_indexes(rows):
 from collections import defaultdict
 by_ed=defaultdict(list); by_topic=defaultdict(list)
 for t in rows:
  by_ed[t.edition_id].append(t)
  for x in t.topics or []: by_topic[x].append(t)
 s='# PromCon\n\nÍndice das trilhas/talks PromCon mapeadas a partir de promcon.io.\n\n'
 s+=f'- Talks indexadas: {len(rows)}\n- Edições: {len(by_ed)}\n- Temas: {len(by_topic)}\n- Com vídeo encontrado automaticamente: {sum(1 for x in rows if x.youtube_url)}\n\n## Por edição\n\n'
 for eid,ts in sorted(by_ed.items(), key=lambda kv:(kv[1][0].year,kv[0])): s+=f"- {ts[0].edition}: {len(ts)} talks\n"
 s+='\n## Por tema\n\n'
 for topic,ts in sorted(by_topic.items(), key=lambda kv:(-len(kv[1]),kv[0])): s+=f'- [[{topic}]] — {len(ts)} talks\n'
 MAP.write_text(s,encoding='utf-8')
 tdir=ROOT/'01-Maps/PromCon-Themes'; tdir.mkdir(parents=True,exist_ok=True)
 for topic,ts in by_topic.items():
  txt=f'# {topic}\n\nTalks PromCon classificadas neste tema.\n\n'
  for t in sorted(ts,key=lambda x:(x.year,x.title)): txt+=f"- [[{Path(t.note_file).stem}|{t.title}]] — {t.edition}\n"
  (tdir/f'{slug(topic)}.md').write_text(txt,encoding='utf-8')
def main():
 import argparse
 ap=argparse.ArgumentParser(); ap.add_argument('--no-video',action='store_true'); ap.add_argument('--limit',type=int,default=0)
 args=ap.parse_args(); rows=[]
 for ed in EDITIONS:
  print('Fetching',ed['id'],flush=True)
  try: ts=parse_schedule(ed)
  except Exception as e: print('failed',ed['id'],e); continue
  print(' ',len(ts),'talks',flush=True); rows.extend(ts)
 if args.limit: rows=rows[:args.limit]
 for i,t in enumerate(rows,1):
  if i%20==1 or i==len(rows): print('Enrich',i,'/',len(rows),flush=True)
  if not args.no_video: find_video(t)
  write_note(t); time.sleep(.05)
 write_indexes(rows); MANIFESTS.mkdir(parents=True,exist_ok=True); out=MANIFESTS/'promcon.json'; out.write_text(json.dumps([asdict(x) for x in rows],ensure_ascii=False,indent=2),encoding='utf-8')
 print('Done',len(rows),'videos',sum(1 for x in rows if x.youtube_url),'manifest',out,flush=True)
if __name__=='__main__': main()
