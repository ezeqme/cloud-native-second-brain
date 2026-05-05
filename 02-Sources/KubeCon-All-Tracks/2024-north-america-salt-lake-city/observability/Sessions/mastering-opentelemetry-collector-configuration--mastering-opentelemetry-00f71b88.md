---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Steve Flanders", "Cisco"]
sched_url: https://kccncna2024.sched.com/event/1i7ot/mastering-opentelemetry-collector-configuration-steve-flanders-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Mastering+OpenTelemetry+Collector+Configuration+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Mastering OpenTelemetry Collector Configuration - Steve Flanders, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Steve Flanders, Cisco
- Schedule: https://kccncna2024.sched.com/event/1i7ot/mastering-opentelemetry-collector-configuration-steve-flanders-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Mastering+OpenTelemetry+Collector+Configuration+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Mastering OpenTelemetry Collector Configuration.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ot/mastering-opentelemetry-collector-configuration-steve-flanders-cisco
- YouTube search: https://www.youtube.com/results?search_query=Mastering+OpenTelemetry+Collector+Configuration+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vzJpDNfA5xU
- YouTube title: Mastering OpenTelemetry Collector Configuration - Steve Flanders, Cisco
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/mastering-opentelemetry-collector-configuration/vzJpDNfA5xU.txt
- Transcript chars: 43702
- Keywords: collector, actually, config, basically, configuration, processors, metrics, receiver, called, vendor, exporter, exporters, symmetry, memory, otel, receivers, specific, components

### Resumo baseado na transcript

for those who don't know me my name is Steve Flanders I am a senior director of engineering at Splunk which was recently acquired by Cisco so I'm not sure which one I'm supposed to say uh but I still call myself a splunker uh I've been involved with the open census which is kind of the precursor project to to open symmetry uh there was open sensus and open tracing uh and now open symetry since the the very beginning uh been involved in the observability space for over a uh question about uh large scale use cases of open Telemetry oftentimes it's advised in monitoring systems to push aggregations to the edge as much as possible yep um are there either any stateful or stateless aggregation capabilities currently in the collector and are

### Excerpt da transcript

for those who don't know me my name is Steve Flanders I am a senior director of engineering at Splunk which was recently acquired by Cisco so I'm not sure which one I'm supposed to say uh but I still call myself a splunker uh I've been involved with the open census which is kind of the precursor project to to open symmetry uh there was open sensus and open tracing uh and now open symetry since the the very beginning uh been involved in the observability space for over a decade now I was at VMware working on a logging product I joined as part of a founding team uh at company called omnition that Splunk acquired it's now the Splunk APM product uh and at Splunk I've been responsible for the Splunk infrastructure monitoring product which was the signal effects acquisition uh so I've been working with traces metrics and logs uh for a very long time and then very recently in fact last week I released a book called mastering open Symmetry and observability uh hopefully you will uh take a look at it so let's start quick with a a poll I mean I think we're at cubec con so I think there's going to be a lot of hands here but how many people have heard of open simetry okay great how many people are using open slimmetry how many people are using open slimmetry in production oh wow I love it we've come a long way uh so many people in fact earlier I was having some conversations with some folks that were talking about the collector uh which I thought was great right so I'm going to start with a little bit of basics who has not used the open open elry before anyone here we go yeah there's a few hands that that's expected so I'm going to start with a quick introduction of the project but I'm going to spend most of my time today talking about one specific component and that is called The Collector uh so let's start at a very high level what is open Telemetry basically it is an open standard uh that makes it possible to generate collect and process Telemetry data uh you might have heard of the three pillars of observability traces metrics and logs open symmetry provides a standard for that but it supports even more than those three pillars right you have things like client instrumentation or profiling synthetic data and the like uh so the project is really focus focused on all Telemetry data that you would care about in your environment whether that's within an application maybe an end user device like a browser or a mobile device uh any language that you care about all of th
