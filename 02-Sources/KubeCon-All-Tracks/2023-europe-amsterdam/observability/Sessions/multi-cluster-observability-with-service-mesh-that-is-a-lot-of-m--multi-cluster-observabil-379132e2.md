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
themes: ["Observability", "Networking", "Kubernetes Core"]
speakers: ["Ryota Sawada", "UPSIDER", "Inc."]
sched_url: https://kccnceu2023.sched.com/event/1Hyd7/multi-cluster-observability-with-service-mesh-that-is-a-lot-of-moving-parts-ryota-sawada-upsider-inc
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Cluster+Observability+with+Service+Mesh+-+That+Is+a+Lot+of+Moving+Parts%21%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Multi-Cluster Observability with Service Mesh - That Is a Lot of Moving Parts!? - Ryota Sawada, UPSIDER, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ryota Sawada, UPSIDER, Inc.
- Schedule: https://kccnceu2023.sched.com/event/1Hyd7/multi-cluster-observability-with-service-mesh-that-is-a-lot-of-moving-parts-ryota-sawada-upsider-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Cluster+Observability+with+Service+Mesh+-+That+Is+a+Lot+of+Moving+Parts%21%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Multi-Cluster Observability with Service Mesh - That Is a Lot of Moving Parts!?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyd7/multi-cluster-observability-with-service-mesh-that-is-a-lot-of-moving-parts-ryota-sawada-upsider-inc
- YouTube search: https://www.youtube.com/results?search_query=Multi-Cluster+Observability+with+Service+Mesh+-+That+Is+a+Lot+of+Moving+Parts%21%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6KTzE3LppDg
- YouTube title: Multi-Cluster Observability with Service Mesh - That Is a Lot of Moving Parts!? - Ryota Sawada
- Match score: 1.0
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/multi-cluster-observability-with-service-mesh-that-is-a-lot-of-moving/6KTzE3LppDg.txt
- Transcript chars: 29686
- Keywords: cluster, istio, prometheus, observability, mesh, metrics, clusters, multi-cluster, control, another, repository, definitely, moving, multi-class, solution, sidecar, simple, created

### Resumo baseado na transcript

so thank you very much for coming I'm Rio de savada this talk is multi-cluster observability with service mesh and that is a lot of moving parts so before going to the details I want to go through some agenda which yeah shows up so we'll start with the introduction about myself about upsider and about this talk and what this talk is about and what this talk is not about and before going to so much details we would also look at observability with service mesh what it looks is your data plane can connect to each other so that's the white lines here that is your sidecars are connected to each other so they can finally talk to each other and also have the metrics and let's see how deploying metrics looks uh deploying Prometheus looks like the following promises would have istio sidecar injected in this case and how does it look like with the Prometheus retrieving metrics from each istio sidecar or Amboy Amboy Sidecar so the orange lines are added and you can see that and that was just deploying Prometheus operator now I need to deploy Prometheus itself and I'm starting with Prometheus for collecting istio metrics and I say that because I'll be deploying two different types of metric Prometheus so first of all is Prometheus istio metrics collection and it will be directly connecting to istio and I get that Prometheus set up with promise this operator so I'm using crds for that...

### Excerpt da transcript

so thank you very much for coming I'm Rio de savada this talk is multi-cluster observability with service mesh and that is a lot of moving parts so before going to the details I want to go through some agenda which yeah shows up so we'll start with the introduction about myself about upsider and about this talk and what this talk is about and what this talk is not about and before going to so much details we would also look at observability with service mesh what it looks like with standard setup which is just single cluster and then we would go into a multi-classes setup and we would go into multi-classical challenges before going to Quick reviews of each project that I will be using and quick and then Solutions and demo and after the demo I'll have a bit of recap alternatives to consider and other considerations that I couldn't touch in this in this talk so firstly introduction of myself so I'm ryota I'm platform engineer at upsider I'm passionate about learning and sharing all the things technology it's a first time speaking in person in person event and it's a first time in person keep con for me it's nerve-wracking as hell but hopefully things go okay um I have a son and two cats and you can find me uh to roit swd which is my full name without vowel and you can find me in usual places and about upside up briefly uh it's a fintech startup we are providing B2B Payment Solutions we are adopted by 15 000 plus companies the headquarter is based in Japan Tokyo Japan and the business is mainly in Japan but the remote team is all around the world I myself am based in London we have a few folks with us today here and we have been Cloud native end user from early 2019 and we use multi-cloud and multi-classes system for the production setup so that's why I wanted to give this talk and we are hiring so if you wanted to know more about us about us please come to me so about this talk so a little bit of prerequisites so I want you to at least have a basic idea about observability what it is about okay it's about metrics traces logs and then service mesh what service mesh can provide it provides traffic management security but this talk is about observability so the talk is going to be mainly about observability metrics aspect and also service mesh in terms of observability and this talk is about so I'm just going to talk about that service Financial behaviors and multi-cluster scenarios observability challenges our learning at upsider and it is a lot of moving part
