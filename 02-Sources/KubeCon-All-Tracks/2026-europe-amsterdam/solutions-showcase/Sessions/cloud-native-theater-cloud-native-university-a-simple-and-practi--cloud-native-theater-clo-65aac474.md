---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Diana Todea", "VictoriaMetrics"]
sched_url: https://kccnceu2026.sched.com/event/2EG0G/cloud-native-theater-cloud-native-university-a-simple-and-practical-guide-to-observability-in-kubernetes-diana-todea-victoriametrics
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+A+Simple+and+Practical+Guide+to+Observability+in+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Cloud Native University: A Simple and Practical Guide to Observability in Kubernetes - Diana Todea, VictoriaMetrics

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Diana Todea, VictoriaMetrics
- Schedule: https://kccnceu2026.sched.com/event/2EG0G/cloud-native-theater-cloud-native-university-a-simple-and-practical-guide-to-observability-in-kubernetes-diana-todea-victoriametrics
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+A+Simple+and+Practical+Guide+to+Observability+in+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Cloud Native University: A Simple and Practical Guide to Observability in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0G/cloud-native-theater-cloud-native-university-a-simple-and-practical-guide-to-observability-in-kubernetes-diana-todea-victoriametrics
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+A+Simple+and+Practical+Guide+to+Observability+in+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nNDNw84Uuqg
- YouTube title: Cloud Native Theater | Cloud Native University: A Simple and Practical Guide to Obser... Diana Todea
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-cloud-native-university-a-simple-and-practical-gu/nNDNw84Uuqg.txt
- Transcript chars: 8690
- Keywords: metrics, logs, around, actually, observability, dashboards, important, instrumentation, application, alerts, specific, obviously, events, control, structure, information, tracing, improve

### Resumo baseado na transcript

I'm also cloud native Romania organizer, co-lead of merge for neurodyiversity. Um Kubernetes obviously it's very well known, it's powerful, but observability can be quite overloading and confusing. Uh so you know if uh they can be modified or deleted at any time um and you know Kubernetes all Kubernetes metrics implicitly fall into this category and we have stable metrics as well that can be guaranteed not to change except that the metric may become marked deprecated for a future Kubernetes version. So there are important metrics like for example coming from control plane like API server request rates API server latency API errors nodes and workloads for CPU usage, memory usage, resource requests versus limits or pod start restarts and scheduling for scheduling latency or pending pods. There are inconsistent naming and labels, high cardality, duplicated metrics or dashboards with no purpose, right? So it's very difficult sometimes for end users to to navigate around this and to like decide which are the metrics that they could start with and uh use them.

### Excerpt da transcript

Uh yeah, thank you so much for being here. I'm going to go quickly uh on introductions. Uh I'm an open telemetry member contributor. I'm also cloud native Romania organizer, co-lead of merge for neurodyiversity. But today I'm going to speak about observability for Kubernetes. Um Kubernetes obviously it's very well known, it's powerful, but observability can be quite overloading and confusing. There are so many tools, there are so many platforms around it, too many metrics, too many dashboards. So how we can make easier for contributors and end users to onboard, right? Um so if we have like metrics, events on one side, logs, traces, um and a whole bunch of things. Uh so we need to focus right on Kubernetes metrics who produces uh the Kubernetes metrics. So we have like API server, we can have app coming from an application, cubelets, C advisor, control manager or scheduler. Um so yeah from this side with the metrics we know how this works right what happens for the Kubernetes metric stability. So at the alpha level we have no stability guarantees.

Uh so you know if uh they can be modified or deleted at any time um and you know Kubernetes all Kubernetes metrics implicitly fall into this category and we have stable metrics as well that can be guaranteed not to change except that the metric may become marked deprecated for a future Kubernetes version. So we may ask ourselves what metrics actually matter right. So there are important metrics like for example coming from control plane like API server request rates API server latency API errors nodes and workloads for CPU usage, memory usage, resource requests versus limits or pod start restarts and scheduling for scheduling latency or pending pods. But here comes the deal, right? Um there's normally around metrics a common problem. There are inconsistent naming and labels, high cardality, duplicated metrics or dashboards with no purpose, right? So it's very difficult sometimes for end users to to navigate around this and to like decide which are the metrics that they could start with and uh use them.

If we go next into the logs, uh we have also um you know a bunch of sources for the logs. We have the application logs, the Kubernetes events, the control plane logs or container runtime logs. So if we follow the same uh kind of narrative there will be also a common log problem. Logs are not standardized. Um for control plane we you know think about the structure JSON. For application logs it could be anything. Uh
