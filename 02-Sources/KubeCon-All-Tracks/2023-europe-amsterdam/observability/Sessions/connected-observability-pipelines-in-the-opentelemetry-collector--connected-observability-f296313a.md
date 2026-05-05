---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability"]
speakers: ["Dan Jaglowski", "observIQ"]
sched_url: https://kccnceu2023.sched.com/event/1HyXb/connected-observability-pipelines-in-the-opentelemetry-collector-dan-jaglowski-observiq
youtube_search_url: https://www.youtube.com/results?search_query=Connected+Observability+Pipelines+in+the+OpenTelemetry+Collector+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Connected Observability Pipelines in the OpenTelemetry Collector - Dan Jaglowski, observIQ

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Dan Jaglowski, observIQ
- Schedule: https://kccnceu2023.sched.com/event/1HyXb/connected-observability-pipelines-in-the-opentelemetry-collector-dan-jaglowski-observiq
- Busca YouTube: https://www.youtube.com/results?search_query=Connected+Observability+Pipelines+in+the+OpenTelemetry+Collector+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Connected Observability Pipelines in the OpenTelemetry Collector.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXb/connected-observability-pipelines-in-the-opentelemetry-collector-dan-jaglowski-observiq
- YouTube search: https://www.youtube.com/results?search_query=Connected+Observability+Pipelines+in+the+OpenTelemetry+Collector+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uPpZ23iu6kI
- YouTube title: Connected Observability Pipelines in the OpenTelemetry Collector - Dan Jaglowski, observIQ
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/connected-observability-pipelines-in-the-opentelemetry-collector/uPpZ23iu6kI.txt
- Transcript chars: 24946
- Keywords: pipeline, collector, metrics, receiver, connector, connectors, exporter, logs, streams, pipelines, processing, stream, component, storage, components, traces, multiple, capabilities

### Resumo baseado na transcript

I'm Daniel glowski I'm a maintainer of the open Telemetry collector and a principal software developer at observe IQ I've been developing observability software for over 10 years and contributing to the open Telemetry collector for the last three most recently I've been working to enhance the collector's ability to manage and process Telemetry and that's what I'll talk about today first I'll talk about the context of these enhancements specifically why the open Telemetry collector is an ideal place to add more sophisticated Telemetry processing capabilities I'll describe the

### Excerpt da transcript

I'm Daniel glowski I'm a maintainer of the open Telemetry collector and a principal software developer at observe IQ I've been developing observability software for over 10 years and contributing to the open Telemetry collector for the last three most recently I've been working to enhance the collector's ability to manage and process Telemetry and that's what I'll talk about today first I'll talk about the context of these enhancements specifically why the open Telemetry collector is an ideal place to add more sophisticated Telemetry processing capabilities I'll describe the collector's pipeline architecture and make a distinction between managing Telemetry and processing it I'll highlight some limitations of the architecture and finally I'll introduce you to a new feature set called connectors which resolve these limitations so traditionally there are three types of telemetry data metrics traces and logs and until recently observability tools were designed as end-to-end Solutions with one data type in mind so to achieve a high degree of observability you would have to deploy several independent tool chains and it also meant that if you wanted to make a change to any one component of that tool chain you might have to replace the entire tool chain so open Telemetry is improving Upon This by supporting multiple data types from the start but it also limits the scope of the problems we're trying to solve we're focused on processing and generating Telemetry we're leaving the other problems to other tools a typical open Telemetry solution looks something like this where if your application is on the left you bring open telemetries instrumentation libraries into your code base where they can capture and emit telemetry often that data will flow through the open Telemetry collector which can process it and forward it to whichever storage and Analysis backends you like and The Collector can also generate its own Telemetry it can read logs from files scrape metrics from apis it's also very highly interoperable so if you've already established data streams using other tools you can usually redirect those through the collector so between the collector the instrumentation libraries and compatibility with other ecosystems The Collector has we have many ways to generate useful Telemetry but it's also of course very important that we have robust processing capabilities a current Trend in the observability industry is to shift left which is with the idea being that we shoul
