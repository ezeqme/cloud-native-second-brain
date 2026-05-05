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
speakers: ["Morgan McLean", "Splunk", "Jaana Dogan", "Amazon"]
sched_url: https://kccncna2021.sched.com/event/lV3J/correlating-signals-in-opentelemetry-benefits-stories-and-the-road-ahead-morgan-mclean-splunk-jaana-dogan-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Correlating+Signals+in+Opentelemetry%3A+Benefits%2C+Stories%2C+and+the+Road+Ahead+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Correlating Signals in Opentelemetry: Benefits, Stories, and the Road Ahead - Morgan McLean, Splunk & Jaana Dogan, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Los Angeles
- Speakers: Morgan McLean, Splunk, Jaana Dogan, Amazon
- Schedule: https://kccncna2021.sched.com/event/lV3J/correlating-signals-in-opentelemetry-benefits-stories-and-the-road-ahead-morgan-mclean-splunk-jaana-dogan-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Correlating+Signals+in+Opentelemetry%3A+Benefits%2C+Stories%2C+and+the+Road+Ahead+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Correlating Signals in Opentelemetry: Benefits, Stories, and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3J/correlating-signals-in-opentelemetry-benefits-stories-and-the-road-ahead-morgan-mclean-splunk-jaana-dogan-amazon
- YouTube search: https://www.youtube.com/results?search_query=Correlating+Signals+in+Opentelemetry%3A+Benefits%2C+Stories%2C+and+the+Road+Ahead+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lQG6UKpTs6M
- YouTube title: Correlating Signals in Opentelemetry: Benefits, Stories, and the Road... Morgan McLean & Jaana Dogan
- Match score: 0.946
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/correlating-signals-in-opentelemetry-benefits-stories-and-the-road-ahe/lQG6UKpTs6M.txt
- Transcript chars: 29879
- Keywords: correlations, latency, logs, metrics, actually, traces, information, checkout, payment, particular, distributed, already, capture, trace, network, perform, profiles, number

### Resumo baseado na transcript

hi everyone welcome to our talk about correlating signals in open telemetry my name is morgan mclean i'm a director of product management at splunk specifically i work on splunk observability cloud i'm also one of the co-founders of open telemetry hi i'm jana dogen i'm a principal engineer at aws and i'm working on containers and observability so we're going to assume that this is a more advanced talk for people who are fairly familiar with open telemetry for those who aren't i'll give you a quick one-minute rundown

### Excerpt da transcript

hi everyone welcome to our talk about correlating signals in open telemetry my name is morgan mclean i'm a director of product management at splunk specifically i work on splunk observability cloud i'm also one of the co-founders of open telemetry hi i'm jana dogen i'm a principal engineer at aws and i'm working on containers and observability so we're going to assume that this is a more advanced talk for people who are fairly familiar with open telemetry for those who aren't i'll give you a quick one-minute rundown so open telemetry is a set of tools uh protocols and other components that you can use on your services and on your infrastructure to capture machine generated or custom data from them and you can then send that information to a back end for processing there's a number of different backend supported it's a big multi-vendor industry project so there's a number of different places you can send that information but specifically open telemetry includes the following a collector which can be deployed as an agent on a host or as a network service that will capture data from any host operating system if one is present and can also capture data from other sources both sources from open telemetry like the sdks and agents that i'll describe in a second it can also capture information from prometheus endpoints and zip code generators and various other locations next open telemetry also includes sdks and language automatic instrumentation agents these are designed to capture signals like distributed traces and metrics from your application whereas the collector in addition to collecting these also captures those host metrics and host uh host logs that i described earlier open telemetry also includes a protocol that defines these different data types and allows them to be transmitted from different open telemetry components to each other or indeed even to back ends that support the native open telemetry protocol and finally open telemetry has a specification and semantic conventions for various use cases so open telemetry is fairly well opinionated which means that if you want to say capture a trace or metric of http traffic open telemetry is standard conventions for how to do that this means that then when you process that data no matter how it was captured as long as it was through open telemetry the data will be consistent and correlatable with other pieces of information which is a big part of our topic today specifically opensummary captures distribute
