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
themes: ["AI ML", "Observability", "GitOps Delivery"]
speakers: ["Juraci Paixão Kröhling", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV0z/opentelemetry-collector-deployment-patterns-juraci-paixao-krohling-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Collector+Deployment+Patterns+CNCF+KubeCon+2021
slides: []
status: parsed
---

# OpenTelemetry Collector Deployment Patterns - Juraci Paixão Kröhling, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[GitOps Delivery]]
- País/cidade: United States / Los Angeles
- Speakers: Juraci Paixão Kröhling, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV0z/opentelemetry-collector-deployment-patterns-juraci-paixao-krohling-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+Collector+Deployment+Patterns+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre OpenTelemetry Collector Deployment Patterns.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0z/opentelemetry-collector-deployment-patterns-juraci-paixao-krohling-red-hat
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+Collector+Deployment+Patterns+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WhRrwSHDBFs
- YouTube title: OpenTelemetry Collector Deployment Patterns - Juraci Paixão Kröhling, Red Hat
- Match score: 0.815
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/opentelemetry-collector-deployment-patterns/WhRrwSHDBFs.txt
- Transcript chars: 21948
- Keywords: collector, application, pattern, patterns, tracing, cluster, talking, deployment, perhaps, multiple, collectors, components, trace, metrics, exporters, destination, prometheus, instances

### Resumo baseado na transcript

hello and welcome to open telemetry collector deployment patterns my name is judas paschenkrolling i'm a software engineer at red hat and i work on the distributed tracing team i am a maintainer on the eager project and a collaborator on open telemetry now for this conversation here today we're talking about patterns before we go into that we're going to invest a couple of minutes talking about open telemetry and the open telemetry collector now those are the patterns that we're going to cover here today the first one

### Excerpt da transcript

hello and welcome to open telemetry collector deployment patterns my name is judas paschenkrolling i'm a software engineer at red hat and i work on the distributed tracing team i am a maintainer on the eager project and a collaborator on open telemetry now for this conversation here today we're talking about patterns before we go into that we're going to invest a couple of minutes talking about open telemetry and the open telemetry collector now those are the patterns that we're going to cover here today the first one is the very basic pattern and if you followed a quick start of open temperature collector you know them already the second pattern is the normalizer pattern and followed by a couple of variants of a pattern for deploying open telemetry collector on kubernetes we talked about load balancing multi-cluster and multi-tenant scenarios as well all right so um all of the the patterns that we talked about here today they are available in this repository here it this repository contains images and configuration file examples and a deeper explanation on those patterns now you can download this slide deck here either from the conferences website or from this box from here and i'm also sharing this live deck right now on twitter all right um so let's get started the open telemetry is a project that was created with a fusion of open tracing and open sensors um it it is actually composed of two big parts the first one is the specification and conventions part so it is uh where the community gets together to determine uh what are the cementing conventions that we should all be following when instrumenting our applications and it also defines um specifications on uh for 23 data types like for uh traces for metrics for logs and so on so forth we have um a group taking care of the the client apis or the instrumentation apis and that's the case we have a group making a definition about otlp and hlp stands for open telemetry line protocol and it is in concrete terms it is a protobuf basically right but it is a specification of on on how we can transmit data uh telemetry data from one service to another right so it specifies both um the the the message and um how the services should look like on the client and on the server side and then the fourth big part of open telemetry is the collector and the collector is where we are focusing on here today in the collector if you go to open the launcher's website the documentation and open the collector documentation you
