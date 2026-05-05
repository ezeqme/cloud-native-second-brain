---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Vijay Samuel", "Sandeep Raveesh", "eBay"]
sched_url: https://kccncna2025.sched.com/event/27FYq/retrofitting-otel-collectors-prometheus-how-to-overcome-scaledesign-limitations-vijay-samuel-sandeep-raveesh-ebay
youtube_search_url: https://www.youtube.com/results?search_query=Retrofitting+OTEL+Collectors+%26+Prometheus+-+How+To+Overcome+Scale%2FDesign+Limitations+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Retrofitting OTEL Collectors & Prometheus - How To Overcome Scale/Design Limitations - Vijay Samuel & Sandeep Raveesh, eBay

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Vijay Samuel, Sandeep Raveesh, eBay
- Schedule: https://kccncna2025.sched.com/event/27FYq/retrofitting-otel-collectors-prometheus-how-to-overcome-scaledesign-limitations-vijay-samuel-sandeep-raveesh-ebay
- Busca YouTube: https://www.youtube.com/results?search_query=Retrofitting+OTEL+Collectors+%26+Prometheus+-+How+To+Overcome+Scale%2FDesign+Limitations+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Retrofitting OTEL Collectors & Prometheus - How To Overcome Scale/Design Limitations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FYq/retrofitting-otel-collectors-prometheus-how-to-overcome-scaledesign-limitations-vijay-samuel-sandeep-raveesh-ebay
- YouTube search: https://www.youtube.com/results?search_query=Retrofitting+OTEL+Collectors+%26+Prometheus+-+How+To+Overcome+Scale%2FDesign+Limitations+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O5GdShQJCgE
- YouTube title: Retrofitting OTEL Collectors & Prometheus - How To Overcome Scale... Vijay Samuel & Sandeep Raveesh
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/retrofitting-otel-collectors-prometheus-how-to-overcome-scale-design-l/O5GdShQJCgE.txt
- Transcript chars: 28092
- Keywords: exemplars, prometheus, basically, series, single, trace, connector, cluster, metric, exemplar, latency, clusters, shards, collectors, memory, within, sampling, region

### Resumo baseado na transcript

Um my name is Vijay Samuel and I'm a principal architect at uh eBay's reliability engineering group. >> Uh I'm Sep and uh I'm one of the lead engineer of the observability platform at eBay. it needs the entire trace to complete for it to be able to uh generate a complete call graph and when you're running at scale say 10 million spans per second um and spans coming in from hundreds of cubernetes clusters like how things are set up uh inside of eBay um waiting for the trace to finish at that scale in memory is a tall ask you need a lot of memory because there is a lot of uh uh latency patterns that are there. Um but you have open telemetry collectors that write to um a gateway u and from the gateway we uh we aggregate and then write into um a metric store which is in this case a cluster of Prometheus pods. need to hold things in memory as and when things are coming in you can construct the call graph and then you can just write the call graph uh into prometheus which open telemetry collector uh supports Yeah.

### Excerpt da transcript

Hello everyone. How's everyone doing? >> Good. Uh hope everyone is having a good cubecon so far. Um my name is Vijay Samuel and I'm a principal architect at uh eBay's reliability engineering group. >> Uh I'm Sep and uh I'm one of the lead engineer of the observability platform at eBay. Um and here we are here today to talk about uh retrofitting open telemetry collectors and Prometheus and u how uh and talk about how we have gone about uh adjusting to the scale at which we operate at eBay uh and how we overcome some of the u scale/design limitations that that we saw in uh both of these uh projects. So we'll talk about three use cases. The first one being uh service graph connector. The next one being Prometheus exemplars and then uh Prometheus itself and how we went about doing clustering. Let's talk about service graph connector first. Um so refresher service graph connector is uh uh one of the connectors available in the uh open telemetry collector contrib. Um and it's typically used to construct uh uh as the name suggests uh a service graph which uh provides all the uh adjacent nodes uh between the various uh microservices, databases, um message cues that are involved in a distributed trace.

Um where would this uh be useful if you're looking to know what the exact call chain is and you're trying to do some automation in terms of okay I have an incident that's going on on a particular service I'm going to walk either upwards or downwards to to see where the increase in calls is coming from or where the most amount of latency is being spent where there are any changes that were executed in any of these services in the call chain for for a lot of causal analysis, a service graph is very useful. Uh and as we go into more automation with uh things like AI, uh a service graph is uh paramount for being able to successfully uh do causal analysis. So what the service graph essentially does is uh it processes all the spans, constructs the call graph, but with a with an important caveat. it needs the entire trace to complete for it to be able to uh generate a complete call graph and when you're running at scale say 10 million spans per second um and spans coming in from hundreds of cubernetes clusters like how things are set up uh inside of eBay um waiting for the trace to finish at that scale in memory is a tall ask you need a lot of memory because there is a lot of uh uh latency patterns that are there.

Some finish at 5 seconds, some finish 50, some finish 5 mi
