---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/configuring-your-opentelemetry-collector-for-prometheus/
youtube_url: https://www.youtube.com/watch?v=GAi_3Bgwa64
youtube_search_url: https://www.youtube.com/results?search_query=Configuring+your+OpenTelemetry+collector+for+Prometheus+PromCon+2023
video_match_score: 1.024
status: video-found
---

# Configuring your OpenTelemetry collector for Prometheus

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/configuring-your-opentelemetry-collector-for-prometheus/
- YouTube: https://www.youtube.com/watch?v=GAi_3Bgwa64

## Resumo

Speaker(s): Matej Gera Although OpenTelemetry has been rising in popularity as a solution for collecting observability signals, Prometheus and its exposition format is not going anywhere. Whether the reason you are switching to OpenTelemetry is due to its expanded functionality, organizational reasons, or you’re just curious, this talk will give you a basis for understanding how to configure the Prometheus receiver and exporter in the OpenTelemetry collector and what to look out for. The presenter will also explain how to bring your existing Prometheus Operator setup and leverage it for metrics collection with the OpenTelemetry Operator.

## Abstract oficial

Speaker(s): Matej Gera

Although OpenTelemetry has been rising in popularity as a solution for collecting observability signals, Prometheus and its exposition format is not going anywhere. Whether the reason you are switching to OpenTelemetry is due to its expanded functionality, organizational reasons, or you’re just curious, this talk will give you a basis for understanding how to configure the Prometheus receiver and exporter in the OpenTelemetry collector and what to look out for. The presenter will also explain how to bring your existing Prometheus Operator setup and leverage it for metrics collection with the OpenTelemetry Operator.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/configuring-your-opentelemetry-collector-for-prometheus/
- YouTube: https://www.youtube.com/watch?v=GAi_3Bgwa64
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GAi_3Bgwa64
- YouTube title: PromCon 2023 - Configuring Your OpenTelemetry Collector for Prometheus
- Match score: 1.024
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/configuring-your-opentelemetry-collector-for-prometheus/GAi_3Bgwa64.txt
- Transcript chars: 26494
- Keywords: collector, prometheus, receiver, exporter, metric, format, receivers, protocols, promus, configuration, resource, promes, operator, protocol, define, attributes, pipeline, metrics

### Resumo baseado na transcript

[Music] thank you so once again my name is ma I work as a software engineer uh at the company called cic we are an observability vendor I'm mostly work on the collection side of things so I deal with um agents and actually also open Telemetry collector which partly inspired this talk but in my previous work and my own source contributions I also worked within the promes ecosystem I worked on on Thanos um but currently it's mostly open tet so I thought it might be an interesting uh the configuration is very similar to what you would see in your Prometheus agent or or other solution you might use for remote writing so it just simply sends right remote WR compatible back ends uh you have some options to uh to find

### Excerpt da transcript

[Music] thank you so once again my name is ma I work as a software engineer uh at the company called cic we are an observability vendor I'm mostly work on the collection side of things so I deal with um agents and actually also open Telemetry collector which partly inspired this talk but in my previous work and my own source contributions I also worked within the promes ecosystem I worked on on Thanos um but currently it's mostly open tet so I thought it might be an interesting um interesting combination to talk about this today so what we'll talk about um we'll take a look at the current status of both uh ecosystem where they are how they compare uh then we'll Dive Right into talking about what is the famous open telemetric collector and its pipeline we'll talk about how we can um receive and Export promes metrics with this collector we'll also look partly at um how we can then further automate this if you're running on kubernetes there is a op Optometry operator that you can use and we'll look at how this relates to Prometheus metrics as well and we'll end up with some some summary and some some wrap up so current status we have we have two projects uh what do we see when we look at them side by side op t we hear it left and right uh this new emerging standard and ecosystem is starting itself to be Cloud native window neutral it's under the AES of cncf same as Prometheus um but when it come to its definition for me it's always kind of elusive because it's it's it's it cuts through so many aspects of observability I cannot sum it up better as as a collection of of different things uh that are named there but you can we can start from the collector where some people see open Telemetry as a kind of synonym with the open Telemetry collector which is the implementation of how open Telemetry imagines The Collection uh and processing and exporting of telemetry data uh but it's much more than this this binary this piece of code it's also a very robust specification that tells us how things should and should not be implemented it comes with its own protocol for transferring data uh the open elry protocol or OTP for short there is a whole set of sdks instrumentation libraries um and so on for for all the languages that um you can desire and very importantly the data model is also different from Prometheus World um because Prometheus uh we could say the Prometheus data model is simpler and serves its purposes but because open Telemetry tries to be kind of a more al
