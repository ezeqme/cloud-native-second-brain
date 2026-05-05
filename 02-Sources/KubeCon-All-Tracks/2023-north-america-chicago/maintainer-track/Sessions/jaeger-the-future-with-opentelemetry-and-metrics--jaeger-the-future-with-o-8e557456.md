---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Pavol Loffay", "Red Hat"]
sched_url: https://kccncna2023.sched.com/event/1R2q1/jaeger-the-future-with-opentelemetry-and-metrics-pavol-loffay-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Jaeger+the+Future+with+OpenTelemetry+and+Metrics+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Jaeger the Future with OpenTelemetry and Metrics - Pavol Loffay, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Pavol Loffay, Red Hat
- Schedule: https://kccncna2023.sched.com/event/1R2q1/jaeger-the-future-with-opentelemetry-and-metrics-pavol-loffay-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Jaeger+the+Future+with+OpenTelemetry+and+Metrics+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Jaeger the Future with OpenTelemetry and Metrics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2q1/jaeger-the-future-with-opentelemetry-and-metrics-pavol-loffay-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Jaeger+the+Future+with+OpenTelemetry+and+Metrics+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vR6HkNpi8Os
- YouTube title: Jaeger the Future with OpenTelemetry and Metrics - Pavol Loffay, Red Hat
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/jaeger-the-future-with-opentelemetry-and-metrics/vR6HkNpi8Os.txt
- Transcript chars: 26081
- Keywords: jagger, collector, tracing, storage, support, instrumentation, search, instance, exporter, metrics, trace, understand, metric, supported, operation, latency, traces, logs

### Resumo baseado na transcript

so hello everyone and welcome to the uh Jager project I'm excited to be here and continue talking about Jager after the cubec con in Amsterdam and share you you know the project updates uh my name is Powell I am a software engineer at redhead I'm Jagger maintainer as well maintainer of open Telemetry operator and graph Tempo operator uh when I'm not contributing uh I like to spend my time in the mountains doing some free ride skiing and uh Mountain Ling uh if you wouldd like to

### Excerpt da transcript

so hello everyone and welcome to the uh Jager project I'm excited to be here and continue talking about Jager after the cubec con in Amsterdam and share you you know the project updates uh my name is Powell I am a software engineer at redhead I'm Jagger maintainer as well maintainer of open Telemetry operator and graph Tempo operator uh when I'm not contributing uh I like to spend my time in the mountains doing some free ride skiing and uh Mountain Ling uh if you wouldd like to reach out to me you can do that on the cncf slack or on Twitter and we can talk about observability or you one of these font Sports as well so today I will um start with introduction to DBT tracing we'll talk about why we should use tracing in the first place then we will do a live Jagger demo with microservice based application where you will see you know how Jager works and what kind of data you can see in the console uh we'll focus as well on the service performance monitoring tab that we have iner I will explain how it works um and then we have a bunch of topics related to open Telemetry uh we'll talk about how you can use open Telemetry collector with the performance monitoring tab but as well how you can you know mix open Telemetry collector with Jagger collector uh and ultimately talk about Jagger wi2 uh it's a new project that we have in Jagger we want to rebate Jager components on top of open Telemetry collector um and then towards the end I will briefly talk about the open Telemetry Auto instrumentation and how you can use it wither and L but last but not least uh we'll talk about new features and road map for 2024 so why distributed tracing and tldr is because uh we write complicated code and we use complicated at architectures right and we as industry spend a lot of time thinking about how we can decouple our applications how we can split them into separate pieces that can be you know created separately compiled and deployed and shipped which is great it enables us to in innovate uh independently however when things go slow or break uh we should have a proper tool to identify you know what is causing the issue and the issue is is that these separate components or services or even third party apis are um managed and operated by different teams right and if you don't have a tool that can pinpoint the issue uh then we don't know even who to contact right if something goes wrong so tracing besides the root Coast analysis can help us to understand relationships ad dependent e
