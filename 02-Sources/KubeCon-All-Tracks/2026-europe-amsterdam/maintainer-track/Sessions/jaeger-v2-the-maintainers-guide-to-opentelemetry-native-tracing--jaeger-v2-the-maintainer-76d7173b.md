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
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Pavol Loffay", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF43/jaeger-v2-the-maintainers-guide-to-opentelemetry-native-tracing-pavol-loffay-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Jaeger+V2%3A+The+Maintainers%27+Guide+To+OpenTelemetry-Native+Tracing+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Jaeger V2: The Maintainers' Guide To OpenTelemetry-Native Tracing - Pavol Loffay, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Pavol Loffay, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF43/jaeger-v2-the-maintainers-guide-to-opentelemetry-native-tracing-pavol-loffay-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Jaeger+V2%3A+The+Maintainers%27+Guide+To+OpenTelemetry-Native+Tracing+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Jaeger V2: The Maintainers' Guide To OpenTelemetry-Native Tracing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF43/jaeger-v2-the-maintainers-guide-to-opentelemetry-native-tracing-pavol-loffay-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Jaeger+V2%3A+The+Maintainers%27+Guide+To+OpenTelemetry-Native+Tracing+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gH_JzIXFshI
- YouTube title: Jaeger V2: The Maintainers' Guide To OpenTelemetry-Native Tracing - Pavol Loffay, Red Hat
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/jaeger-v2-the-maintainers-guide-to-opentelemetry-native-tracing/gH_JzIXFshI.txt
- Transcript chars: 23534
- Keywords: jagger, trace, tracing, storage, actually, retention, jerger, prometheus, traces, collector, search, configure, logging, database, minutes, metrics, systems, support

### Resumo baseado na transcript

Um there will be as well a live demo and we'll spend some time talking about Jagger V2 which is the current uh currently supported version version of Jagger. Nowadays I do mostly open telemetry open telemetry operator and collector. it's very difficult to reason where the error happened and distributed tracing is one of the observability signals that can help us to answer these questions. Um it's as well great because with tracing we see um um kind of we get the full lifespan of the request and we are able to kind of pinpoint the error and as we'll talk to the right people that maintain that service uh and tell them to to fix it because tracing system observes all the transactions. Uh but in my opinion, why people use tracing is actually the root cause analysis. Uh and then last but not least, I mentioned the tracing system uh can be used to set up monitor monitoring uh and so you can use you can as well set up your your SLAs's and I think this is very important in microser

### Excerpt da transcript

Hello everyone and welcome to Jagger project session. Uh my name is Pavle and now we're going to talk about observability. I'm curious who is using Jagger. Awesome. And who doesn't know anything about tracing? Okay. So yeah, in this 30 minutes we'll talk about Jagger. We'll do a lot of introductory stuff. Um there will be as well a live demo and we'll spend some time talking about Jagger V2 which is the current uh currently supported version version of Jagger. Uh and yeah that's pretty much it. Uh my name is Powell. I'm a Jerger maintainer. Um I used to contribute a lot to the project in the past. Nowadays I do mostly open telemetry open telemetry operator and collector. Um and eager is a CNCF project uh graduated um it has been released I think 10 years ago. Uh that's when I started VGER. So it's been long time with the project. Uh and so today we'll do an introduction to distributed tracing. I will talk about what use cases does it solve. Um and then we'll do a intro to Jerger. I will talk about the tracing data model and do a live demo that we actually publish for anyone to use.

It's on the on the website. Uh and then briefly talk about Jerger with Prometheus, how you can use tracing system to as well set up your monitoring and alerting. And then um finally something about Jagger V2. I will be talking as well about Jagger MCP which is one of the latest additions to the project. and at the end uh the new features since the last CubeCon and the road map for 2026 and beyond. So why distributed tracing? Uh and the answer is very simple. It's because our code is too complicated. We write very complex architectures systems uh and it's very difficult to understand these systems. it's very difficult to reason where the error happened and distributed tracing is one of the observability signals that can help us to answer these questions. Um it's as well great because with tracing we see um um kind of we get the full lifespan of the request and we are able to kind of pinpoint the error and as we'll talk to the right people that maintain that service uh and tell them to to fix it because tracing system observes all the transactions.

is able to kind of construct service um diagram which is very useful because we can plan for updates in our complex systems. We understands which APIs are used, who uses this API and as well who uses our APIs. It's it's very important. Uh but in my opinion, why people use tracing is actually the root cause analysis. Since we see every
