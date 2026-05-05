---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "SRE Reliability", "Community Governance"]
speakers: ["Friedrich Gonzalez", "Charlie Le", "Apple"]
sched_url: https://kccnceu2026.sched.com/event/2EF6K/discover-cortex-high-scalability-metrics-in-2026-friedrich-gonzalez-charlie-le-apple
youtube_search_url: https://www.youtube.com/results?search_query=Discover+Cortex%3A+High+Scalability+Metrics+in+2026+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Discover Cortex: High Scalability Metrics in 2026 - Friedrich Gonzalez & Charlie Le, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Friedrich Gonzalez, Charlie Le, Apple
- Schedule: https://kccnceu2026.sched.com/event/2EF6K/discover-cortex-high-scalability-metrics-in-2026-friedrich-gonzalez-charlie-le-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Discover+Cortex%3A+High+Scalability+Metrics+in+2026+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Discover Cortex: High Scalability Metrics in 2026.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6K/discover-cortex-high-scalability-metrics-in-2026-friedrich-gonzalez-charlie-le-apple
- YouTube search: https://www.youtube.com/results?search_query=Discover+Cortex%3A+High+Scalability+Metrics+in+2026+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PCeS4YLKTwg
- YouTube title: Discover Cortex: High Scalability Metrics in 2026 - Friedrich Gonzalez & Charlie Le, Apple
- Match score: 0.827
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/discover-cortex-high-scalability-metrics-in-2026/PCeS4YLKTwg.txt
- Transcript chars: 22708
- Keywords: cortex, metrics, feature, features, actually, queries, support, prometheus, release, tenant, blocks, coming, basically, storage, querying, better, wanted, tenants

### Resumo baseado na transcript

Maybe everyone is a little tired now, but hopefully we can keep you awake during this talk. He's also a software engineer at Apple and we're both maintainers for Cortex. Uh what it does is allow you to send metrics from Prometheus or open telemetry collectors uh to a backend that can then store it for you and allow you to query it for a long duration of time. Um, essentially you can run it as a service for your whole company, allow other teams to send you metrics and then separate them out by tenants. Um this is a completely open source project right Zapachi 2 and uh part of the CNCF so you don't have to worry about um you know the licenses changing or anything like that um and uh if you're using Prometheus it should be completely compatible with that so you shouldn't have any issues using cortex as if you're using open telemetry as well you can send metrics via OTLP or the remote write uh protocol.

### Excerpt da transcript

All right. Should we start? Thank you uh everyone for joining today. Um I know it's the last day. Maybe everyone is a little tired now, but hopefully we can keep you awake during this talk. Um so hello everyone. My name is Charlie. Um I am a software engineer at Apple. I'm joined by Frederick Gonzalez. He's also a software engineer at Apple and we're both maintainers for Cortex. And uh today we're going to be talking to you about uh Cortex, some new things like um that have come out in the 1.20 release. I'm going to be going through some of those new features that have come out and then Frederick will go over some of the new things that are coming out in the 1.21 release candidate. Um so um it's pretty exciting. And then uh we'll round out the talk with uh the road to graduation for the project as well as um sort of what's in the road map for things to come. And uh if at the end hopefully there will be some time for Q&A. So keep in mind some questions that you have and uh we'll try to answer them at the end.

So before we go into those uh features, I just wanted to quickly introduce some of the people that um maybe haven't used Cortex. Can I get like a show of hands? People have used Cortex before. Okay, people that are new to Cortex. Okay, wow, a lot of people. Great. Thank you. You're in the right place. Um so let me just quickly uh introduce you to what Cortex is. Um, I've been at the booth for the last uh three days, so I've been getting this question a lot. So hopefully I've uh figured it out by now. But uh so what is Cortex? Uh what it does is allow you to send metrics from Prometheus or open telemetry collectors uh to a backend that can then store it for you and allow you to query it for a long duration of time. Um, essentially you can run it as a service for your whole company, allow other teams to send you metrics and then separate them out by tenants. Um, so that way each team can only query and send their own metrics. There's a bunch of other knobs that you can add to each tenant so that uh no single tenant can cause an issue for another.

So this solves the noisy neighbor problem as well. Um this is a completely open source project right Zapachi 2 and uh part of the CNCF so you don't have to worry about um you know the licenses changing or anything like that um and uh if you're using Prometheus it should be completely compatible with that so you shouldn't have any issues using cortex as if you're using open telemetry as well you can send metric
