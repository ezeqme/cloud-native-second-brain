---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: ["Björn Rabenstein"]
source_url: https://promcon.io/2025-munich/talks/eight-definitions-of-observability-vs-monitoring--and-why-none-of-them-work/
youtube_url: https://www.youtube.com/watch?v=m_xePp_jvtk
youtube_search_url: https://www.youtube.com/results?search_query=Eight+definitions+of+%E2%80%9Cobservability%E2%80%9D+vs.+%E2%80%9Cmonitoring%E2%80%9D+%E2%80%93+and+why+none+of+them+work+PromCon+2025
video_match_score: 1.049
status: video-found
---

# Eight definitions of “observability” vs. “monitoring” – and why none of them work

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: Björn Rabenstein
- Página oficial: https://promcon.io/2025-munich/talks/eight-definitions-of-observability-vs-monitoring--and-why-none-of-them-work/
- YouTube: https://www.youtube.com/watch?v=m_xePp_jvtk

## Resumo

When Prometheus became popular, the term “observability” was rarely used. A few years later, “observability” went on an impressive buzzword trajectory. For some, Prometheus became a core observability tool, while others wouldn't consider it an observability tool at all.

## Abstract oficial

When Prometheus became popular, the term “observability” was rarely used. A few years later, “observability” went on an impressive buzzword trajectory. For some, Prometheus became a core observability tool, while others wouldn't consider it an observability tool at all. Obviously, there is some confusion around what “observability” actually means and how it differs from “mere monitoring”. Let's explore common (and some not so common) definitions of “o11y” vs. “m8g”. We’ll evaluate if they make sense and how popular and useful they are. And maybe in the end, we'll finally know if Prometheus is actually an observability tool.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/eight-definitions-of-observability-vs-monitoring--and-why-none-of-them-work/
- YouTube: https://www.youtube.com/watch?v=m_xePp_jvtk
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m_xePp_jvtk
- YouTube title: PromCon 2025 - Eight definitions of “observability” vs. “monitoring” – and why none of them work
- Match score: 1.049
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/eight-definitions-of-observability-vs-monitoring-and-why-none-of-them/m_xePp_jvtk.txt
- Transcript chars: 32862
- Keywords: observability, monitoring, prometheus, theory, control, popular, whatever, actually, definition, useful, distributed, course, metrics, tracing, already, correct, difference, essentially

### Resumo baseado na transcript

This is why I have to start with that like I've been doing distributed systems for longer than some of you live. We we joke sometimes even before it was created but that's that's maybe an insider. They mention white box metrics here which is essentially you instrument for metrics. They also mentioned structured logs which was hot new concept I guess and you so we're getting concepts from our profession. I was wondering if there's a new movie called observability or but I don't know like yeah um so but you can kind of see we we took off like whatever 2020 or something right so definitely after Prometheus so I wanted to compare this to monitoring but monitoring is actually a term that is used a lot outside of our profession just randomly by people so if I put monitoring it's it's still way high up there so I thought why not use Prometheus as a representative for monitoring

### Excerpt da transcript

Okay. So, hello. Um, I'm John. I was mentioned on a bunch of slides already. So, you might have guessed that I did a thing or two for Prometheus. I've um been this plays a role in this talk. This is why I have to start with that like I've been doing distributed systems for longer than some of you live. I've been doing Prometheus. We we joke sometimes even before it was created but that's that's maybe an insider. So 2013 was first contribution to Prometheus relatively recently I guess in relative terms. I started to work for Grafana and they even pay me. So I work for can contribute to Prometheus. So this is why there are a lot of Grafana logos on the slides and I wear the Grafana shirt. I'm Yeah, thank you. Tom might be still here. My boss's bosses boss, whatever. Um Um So I want to talk actually not so much about Prometheus, more about observability and what is the difference between observability and monitoring. So we'll see how this works. Um I already started with that. We have go back to history. It's a bit of bragging rights here.

So it's the year of 2006, right? Um so I run distributed systems at scale. Of course I work for the company that gives us this room. Um I use locks, metrics and profiles. I also use distributed tracing not quite in 2006. There was the Dapper paper in 2010. Uh but of course Google doesn't just publish a paper and then implement stuff. Some people do it that way, but they do stuff and and try it out in real world production system and then they publish a paper. So even before the paper was published, I had the privilege of using distributed tracing. Nobody says observability in the year of 2006. Fast forward, it's the year 2012. SoundCloud runs a makeshift container orchestration platform called Bizooker. Matt and Julius in the room. uh they create Prometheus nowadays observability. Let's uh go fast forwards the year 2016. This was a very happy year because Google suddenly or finally publishes the SR book. I could finally explain to people what was my job the last 10 years because nobody knew what an SR is.

It says observability once. So this is the only occurrence of observability in the whole S3 book. Uh and I mean it's it could be that the author just wanted they they just used this term because it's a normal English word. Maybe they had control theory in mind which we'll come to later. They mention white box metrics here which is essentially you instrument for metrics. That was a thing that people didn't do generally in
