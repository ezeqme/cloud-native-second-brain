---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Sponsored Sessions"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Peter Irwin", "ScaleOps", "Carl Baumcratz", "Coupa"]
sched_url: https://kccnceu2026.sched.com/event/2ICgs/sponsored-session-performance-at-enterprise-cloud-scale-coupas-kubernetes-optimization-journey-peter-irwin-scaleops-carl-baumcratz-coupa
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Performance+at+Enterprise+Cloud+Scale%3A+Coupa%E2%80%99s+Kubernetes+Optimization+Journey+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sponsored Session: Performance at Enterprise Cloud Scale: Coupa’s Kubernetes Optimization Journey - Peter Irwin, ScaleOps & Carl Baumcratz, Coupa

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Sponsored Sessions]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Peter Irwin, ScaleOps, Carl Baumcratz, Coupa
- Schedule: https://kccnceu2026.sched.com/event/2ICgs/sponsored-session-performance-at-enterprise-cloud-scale-coupas-kubernetes-optimization-journey-peter-irwin-scaleops-carl-baumcratz-coupa
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Performance+at+Enterprise+Cloud+Scale%3A+Coupa%E2%80%99s+Kubernetes+Optimization+Journey+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sponsored Session: Performance at Enterprise Cloud Scale: Coupa’s Kubernetes Optimization Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2ICgs/sponsored-session-performance-at-enterprise-cloud-scale-coupas-kubernetes-optimization-journey-peter-irwin-scaleops-carl-baumcratz-coupa
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Performance+at+Enterprise+Cloud+Scale%3A+Coupa%E2%80%99s+Kubernetes+Optimization+Journey+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yV8_keBkCJo
- YouTube title: Sponsored Session: Performance at Enterprise Cloud Scale: Coupa’s Ku... Peter Irwin & Carl Baumcratz
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sponsored-session-performance-at-enterprise-cloud-scale-coupas-kuberne/yV8_keBkCJo.txt
- Transcript chars: 12281
- Keywords: cost, scaleups, workloads, platform, clusters, journey, environment, carpenter, awesome, helped, performance, coming, savings, product, moving, little, challenges, number

### Resumo baseado na transcript

Uh we know we're standing between you guys and beer, so we're going to keep it moving and appreciate everybody showing up. Uh today we're going to talk a little bit about how Kubernetes can perform at enterprise cloud scale with my friend Carl here from Koopa. cost measures and the efficiency measures in favor of developing and building new features where their time is is better spent. Um over the last several years we're trying to um really drive down the cost of that EEC2 uh uh platform shifting all that left um right now we were cost um managing just by reports and now we want to shift it left into the pipeline. So um why traditional autoscaling fails um it falls short um the minute you set a static threshold in your values files it's already drifted it's a snapshot in time there's risk of downtime performance issues for your customer um cluster level uh signals they're Um we tested out a couple different um couple different solutions uh off the shelf, scaleups being one of them.

### Excerpt da transcript

Well, thank you guys for joining us here. Uh we know we're standing between you guys and beer, so we're going to keep it moving and appreciate everybody showing up. Uh today we're going to talk a little bit about how Kubernetes can perform at enterprise cloud scale with my friend Carl here from Koopa. Uh as an agenda, uh we want to talk a little bit about the challenges at managing Kubernetes at scale, some of the problems it presents as you uh try to stay efficient as as more and more teams come onto an enterprise platform. We're going to talk a little bit about Koopa's environment and some of their journey through optimization uh from workloads to nodes and carpenter and uh and the path forward and the outcomes that they got uh throughout this journey. So just to introduce ourselves, I'm Peter. I lead the global sales team here at Scale Ops and Carl >> uh director of cloud software engineering at Koopa. >> Awesome. So when you run Kubernetes at scale, there's a there's a number of factors that come into play and and become challenging to manage, especially supporting many uh development teams.

Uh as things are as dynamic as they can be and uh performance will change over time, behaviors will change, keeping up with that becomes really challenging. Uh and and it can be inconsistent. That leads to a lot of inefficient packing of nodes and pods uh and sizing and and results in a lot of time spent by teams manually tuning resources trying to stay ahead of the curve but always uh dep prioritizing some of the the cost measures and the efficiency measures in favor of developing and building new features where their time is is better spent. Um Koopa experienced this firsthand and Carl, why don't you share a little bit about your environment? >> All right. Uh so our environment has been expanding over the last three years. We're a very transformative fastm moving company. Um we were kind of born in cloud uh AIdriven spend management platform for at least a half a decade now. Um so AI is kind of it runs through our blood. Uh AI continues to expand for us. growing number of workloads coming into our our clusters and a growing number of of customers coming into older workloads as well as the newer workloads that are coming.

Um to manage our our growing environment um we use a GitOps approach delivering our clusters uh as well as its configurations. We're currently at our at our uh control plane. We're at 140 clusters. Um that sets us up for a very large data plane
