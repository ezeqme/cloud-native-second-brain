---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Alolita Sharma", "Amazon"]
sched_url: https://kccncna2021.sched.com/event/lV5O/building-prometheus-metrics-support-in-opentelemetry-alolita-sharma-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Building+Prometheus+Metrics+Support+in+OpenTelemetry+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Building Prometheus Metrics Support in OpenTelemetry - Alolita Sharma, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Los Angeles
- Speakers: Alolita Sharma, Amazon
- Schedule: https://kccncna2021.sched.com/event/lV5O/building-prometheus-metrics-support-in-opentelemetry-alolita-sharma-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Prometheus+Metrics+Support+in+OpenTelemetry+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Building Prometheus Metrics Support in OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5O/building-prometheus-metrics-support-in-opentelemetry-alolita-sharma-amazon
- YouTube search: https://www.youtube.com/results?search_query=Building+Prometheus+Metrics+Support+in+OpenTelemetry+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7WV5GMFXaV4
- YouTube title: Building Prometheus Metrics Support in OpenTelemetry - Alolita Sharma, Amazon
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/building-prometheus-metrics-support-in-opentelemetry/7WV5GMFXaV4.txt
- Transcript chars: 16887
- Keywords: prometheus, support, metrics, observability, collector, source, working, projects, protocol, progress, interoperability, components, making, process, receiver, design, having, applications

### Resumo baseado na transcript

hi everyone i'm alolita sharma from aws and i am also an open telemetry governance committee member uh i will be presenting today on building prometheus support in open telemetry which has been a great effort in collaboration and give you an update on what's uh what's in progress a little bit about myself i'm a principal technologist at aws and i lead open source strategy and engineering i'm also a co-chair of the cncf technical advisory group for observability and i have a great um you know appreciation for

### Excerpt da transcript

hi everyone i'm alolita sharma from aws and i am also an open telemetry governance committee member uh i will be presenting today on building prometheus support in open telemetry which has been a great effort in collaboration and give you an update on what's uh what's in progress a little bit about myself i'm a principal technologist at aws and i lead open source strategy and engineering i'm also a co-chair of the cncf technical advisory group for observability and i have a great um you know appreciation for open standards and interoperability i see prometheus support in open telemetry as a great opportunity to multiply the usefulness and reach of observability data and i see the effort that we are making on the open telemetry project to fully support prometheus as an uh effort that really will you know bring a great value to both projects as well as to the users who use these so many of you know already about open about observability and as you know observability brings and deep understanding of the behavior of a system the best modern solutions today in observability live in open source and open telemetry as well as prometheus are great examples of such amazing and powerful open source projects tracing metrics and logging as you know are the core data signals in observability and they give the opportunity for the user to be able to use metrics you know for aggregation tracing for each request which is transaction based as well as logging and events that are collected for telemetry so observability in kubernetes is an area that we is near and dear to all of our hearts because we have been working in that space and it's something that you know really is important for kubernetes developers to understand uh and use telemetry data to understand in in turn what the behavior of their code is during runtime and having more observability data whether that's metrics or traces or logs really helps in the effectiveness of kubernetes monitoring so a little bit about the architecture of open telemetry just to set the context for the components that are being enhanced and the overall objective of the project is that open telemetry not only provides an open standard for collection of telemetry and data format in the form of the open telemetry protocol but also provides open source components such as the collector agent and api and sdk libraries in 11 languages which provide the ability to use and and customize your applications to build in in different languages and pro
