---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Observability"
themes: ["Observability"]
speakers: ["Steve Flanders", "Splunk"]
sched_url: https://kccnceu2021.sched.com/event/iE5f/log-support-in-opentelemetry-steve-flanders-splunk
youtube_search_url: https://www.youtube.com/results?search_query=Log+Support+in+OpenTelemetry+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Log Support in OpenTelemetry - Steve Flanders, Splunk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Virtual / Virtual
- Speakers: Steve Flanders, Splunk
- Schedule: https://kccnceu2021.sched.com/event/iE5f/log-support-in-opentelemetry-steve-flanders-splunk
- Busca YouTube: https://www.youtube.com/results?search_query=Log+Support+in+OpenTelemetry+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Log Support in OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5f/log-support-in-opentelemetry-steve-flanders-splunk
- YouTube search: https://www.youtube.com/results?search_query=Log+Support+in+OpenTelemetry+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ypq-nXh38Zk
- YouTube title: Log Support in OpenTelemetry - Steve Flanders, Splunk
- Match score: 0.798
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/log-support-in-opentelemetry/ypq-nXh38Zk.txt
- Transcript chars: 25299
- Keywords: collector, instrumentation, logs, logging, actually, fluent, support, libraries, trace, symmetry, attributes, traces, context, fields, signals, metrics, pretty, stable

### Resumo baseado na transcript

hello and welcome to this session log support and open telemetry what is open telemetry openslimetry is all about making robust portable telemetry data a feature of cloud-native software that means the goal is to provide a set of apis libraries agents and collector technology that's bundled automatically and available so that you can easily generate emit and collect the telemetry data that you need in order to observe your systems open telemetry is a very active project in fact it's the second most active project in cncf behind only

### Excerpt da transcript

hello and welcome to this session log support and open telemetry what is open telemetry openslimetry is all about making robust portable telemetry data a feature of cloud-native software that means the goal is to provide a set of apis libraries agents and collector technology that's bundled automatically and available so that you can easily generate emit and collect the telemetry data that you need in order to observe your systems open telemetry is a very active project in fact it's the second most active project in cncf behind only kubernetes and this is according to cncf dev sets the project is seeing a lot of momentum with many people contributing and adopting the technology from cloud providers and end users to vendors and other open source projects you can learn all about it and the links provided below telemetry is really focused today around three primary signals traces metrics and logs and each are in a different phase of maturity traces recently reached the stable milestone with three major languages providing support two more right on the way and the rest planned later this year metrics is currently in beta but the goal is to offer a stable data model here in the next couple of months and then instrumentation libraries will start adopting the data model and logs is currently in alpha the goal is that traces and metrics will be stable across all major languages later this year and logs will at least reach the beta milestone hi my name is steve flanders i'm a director of engineering at splunk and actively involved in the open telemetry project including the collector and website i'm also a member of the cncf sig observability i've been working in the open telemetry space since its inception and previously on the open census project i've also been in the observability space now for over a decade prior to splunk i was at an omniscient that was acquired by splunk about a year and a half ago working in the distributed tracing space and prior to that i was working in the logging space at vmware if you're interested in learning more about me take a look at the social media links i want to start by kind of walking through the major components of open telemetry and then overlaying how logs plays into it open telemetry is about cloud native telemetry if you've heard of observability you've probably heard of the three pillars of observability which are represented as verticals here traces metrics and logs these signals or data sources are full of rich inform
