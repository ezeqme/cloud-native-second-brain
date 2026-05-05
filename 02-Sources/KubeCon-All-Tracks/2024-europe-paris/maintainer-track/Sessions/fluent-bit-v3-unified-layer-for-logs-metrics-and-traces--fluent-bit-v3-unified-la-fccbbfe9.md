---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Eduardo Silva", "Calyptia"]
sched_url: https://kccnceu2024.sched.com/event/1aDbX/fluent-bit-v3-unified-layer-for-logs-metrics-and-traces-eduardo-silva-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit+v3%3A+Unified+Layer+for+Logs%2C+Metrics+and+Traces+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fluent Bit v3: Unified Layer for Logs, Metrics and Traces - Eduardo Silva, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Eduardo Silva, Calyptia
- Schedule: https://kccnceu2024.sched.com/event/1aDbX/fluent-bit-v3-unified-layer-for-logs-metrics-and-traces-eduardo-silva-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit+v3%3A+Unified+Layer+for+Logs%2C+Metrics+and+Traces+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fluent Bit v3: Unified Layer for Logs, Metrics and Traces.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aDbX/fluent-bit-v3-unified-layer-for-logs-metrics-and-traces-eduardo-silva-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit+v3%3A+Unified+Layer+for+Logs%2C+Metrics+and+Traces+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4SqDRokC7ac
- YouTube title: Fluent Bit v3: Unified Layer for Logs, Metrics and Traces - Eduardo Silva, Calyptia
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fluent-bit-v3-unified-layer-for-logs-metrics-and-traces/4SqDRokC7ac.txt
- Transcript chars: 40013
- Keywords: fluent, processor, thread, called, filters, running, message, logs, output, metrics, version, information, single, everything, traces, support, exporter, matrix

### Resumo baseado na transcript

unified layer for logs metrics and traces like six seven years ago we started teaching how to do a unified login layer right that's how well maybe 10 years ago how we started in this journey and one of the challenges is like when you're dealing with Telemetry data called today right it's really hard to concentrate them handle the volume even more when data come from different sources and a destinations first of all I would like to know who are your first timers using fluent bed or fluent

### Excerpt da transcript

unified layer for logs metrics and traces like six seven years ago we started teaching how to do a unified login layer right that's how well maybe 10 years ago how we started in this journey and one of the challenges is like when you're dealing with Telemetry data called today right it's really hard to concentrate them handle the volume even more when data come from different sources and a destinations first of all I would like to know who are your first timers using fluent bed or fluent D maybe you can raise your hand so I can get an idea oh just a few ones so I'm going to get more back reports or or similar things so I assume that most of you have some knowledge about what fluent bit does but first of all it's good to clarify where we came from you know cncf has projects is a neutral plan place for all the projects around Cloud native space started for kubernetes prome jger and so on fluentd our parent project was graduated around 2019 if I'm not wrong and fluent bit is part of that Journey both projects are graduated and While others are still you know in this phase of incubation we expecting to also get open Telemetry um graduated at the end of the year so it's really interesting to see how the projects evolve from one stage to the other and what is really important is adoption it's adoption not just because somebody's using it it's because they are using it they're reporting issues and there people contributing back to the project which at the end of the day is more important you don't want to deploy something that nobody's going to maintain it over time you want to deploy something like this and forget about it right and when you get security issues somebody will issue a fix but at the end of the day um what is important is that this is a very new vendor neutral Place despite there company like us from chronosphere calpia or Amazon using this projects developing code you will make sure that whatever you have here will be there for many many years so let's get started with ls metos and traces H in a nutshell flow and bit as an agent as you might know can handle all of the Telemetry types of data and to be honest it was not designed for that it was designed for logs but the way and this was lack the way that we designed how to handle logs was in a very agnostic way we don't care how the data looks like we're going to caliz it and provide some processing and be able to ship it out to any type of backend storage and that's how fluent bid was evolving for
