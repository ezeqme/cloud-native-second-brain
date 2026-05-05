---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Motohiro Otsuka", "LY Corporation", "Tomoyuki Nakamura", "LY Corporation"]
sched_url: https://kccnceu2026.sched.com/event/2CW1H/generalizing-kubernetes-controller-sharding-patterns-that-work-beyond-simple-operators-motohiro-otsuka-ly-corporation-tomoyuki-nakamura-ly-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Generalizing+Kubernetes+Controller+Sharding%3A+Patterns+That+Work+Beyond+Simple+Operators+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Generalizing Kubernetes Controller Sharding: Patterns That Work Beyond Simple Operators - Motohiro Otsuka, LY Corporation & Tomoyuki Nakamura, LY Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Motohiro Otsuka, LY Corporation, Tomoyuki Nakamura, LY Corporation
- Schedule: https://kccnceu2026.sched.com/event/2CW1H/generalizing-kubernetes-controller-sharding-patterns-that-work-beyond-simple-operators-motohiro-otsuka-ly-corporation-tomoyuki-nakamura-ly-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Generalizing+Kubernetes+Controller+Sharding%3A+Patterns+That+Work+Beyond+Simple+Operators+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Generalizing Kubernetes Controller Sharding: Patterns That Work Beyond Simple Operators.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1H/generalizing-kubernetes-controller-sharding-patterns-that-work-beyond-simple-operators-motohiro-otsuka-ly-corporation-tomoyuki-nakamura-ly-corporation
- YouTube search: https://www.youtube.com/results?search_query=Generalizing+Kubernetes+Controller+Sharding%3A+Patterns+That+Work+Beyond+Simple+Operators+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7qsOwyE_uOo
- YouTube title: Generalizing Kubernetes Controller Sharding: Patterns That Wo... Motohiro Otsuka & Tomoyuki Nakamura
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/generalizing-kubernetes-controller-sharding-patterns-that-work-beyond/7qsOwyE_uOo.txt
- Transcript chars: 17488
- Keywords: manager, namespace, parent, operator, control, cluster, sharding, architecture, spaces, resources, design, identity, resource, clusters, reference, single, object, assigned

### Resumo baseado na transcript

My name is Tommoakamra from Corporation and here is my co-speaker Moto Hiroka. Our core message is this sharding is not a feature to it is an architectural decision about where you place your replication boundary. At this scale we started observing pain not out of memory not classes instead through initial syn through initial synchronization during restart longer reconcile latency delayed user visible proication. This design is extremely efficient for vertical scaling, one process, one shared cache, minimal deplication, but it is not elastic horizontally. So when reconcile facial increases you cannot just add replicas and expect throughput scale controllers are vertically efficient but not horizontally asterric that as a structural constraint uh I don't know actually uh how many people are They are struggling with Kubernetes reconcile delays caused by large number of resources but we currently are so we choose Kubernetes contra sharing KCS KCS is an opensource project developed by team EAD you can find it at GitHub its goal to make Kubernetes controllers horizonally scalable KCS works by computing shard selection

### Excerpt da transcript

Good morning and thank you for being here. My name is Tommoakamra from Corporation and here is my co-speaker Moto Hiroka. Today we want to talk about generalizing command control sharding. This is not a story about clever trick. This is not a story about the performance hack. Our core message is this sharding is not a feature to it is an architectural decision about where you place your replication boundary. At that boundary determines whether determines whether your system scales or quietly cores. We walk through five parts. First why scaring broke horse. Second, what shing can and can't not solve. Third, why our first architecture failed. Fourth, how we pivot it. And finally, the reasonal decision framework we ended to up with. This is not just our story. It is a reason model you can apply to your own controllers. Our team develops and operates a command based internal pass platform at Li Corporation. This diagram shows an overview of the pass environment we provide internally. It consists of a single control control plane Kubernetes cluster and many data plane Kubernetes clusters.

Internal users define up resource in the control is in the control plane cluster and through it they manage resource such post learning in the data brain clusters. My team operates at roughly 66,000 ports 5,000 nodes 3,000 name spaces and 500,000 managed object. At this scale we started observing pain not out of memory not classes instead through initial syn through initial synchronization during restart longer reconcile latency delayed user visible proication. The system was not broken but it was approaching a structure limit and we knew vertical scaling alone would not protect us forever. Let's quickly review how most Kubernetes control are structured. Most controllers follow the same model, shadow inform cache, single active reader and standby replicas. This design is extremely efficient for vertical scaling, one process, one shared cache, minimal deplication, but it is not elastic horizontally. Reader election ensures only one replica reconciles. So when reconcile facial increases you cannot just add replicas and expect throughput scale controllers are vertically efficient but not horizontally asterric that as a structural constraint uh I don't know actually uh how many people are They are struggling with Kubernetes reconcile delays caused by large number of resources but we currently are so we choose Kubernetes contra sharing KCS KCS is an opensource project developed by
