---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Runtime Containers", "Community Governance"]
speakers: ["Sohan Kunkerkar", "Ayato Tokubi", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF6N/cri-o-faster-pulls-better-metrics-and-a-future-beyond-images-sohan-kunkerkar-ayato-tokubi-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=CRI-O%3A+Faster+Pulls%2C+Better+Metrics%2C+and+a+Future+Beyond+Images+CNCF+KubeCon+2026
slides: []
status: parsed
---

# CRI-O: Faster Pulls, Better Metrics, and a Future Beyond Images - Sohan Kunkerkar & Ayato Tokubi, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sohan Kunkerkar, Ayato Tokubi, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF6N/cri-o-faster-pulls-better-metrics-and-a-future-beyond-images-sohan-kunkerkar-ayato-tokubi-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=CRI-O%3A+Faster+Pulls%2C+Better+Metrics%2C+and+a+Future+Beyond+Images+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre CRI-O: Faster Pulls, Better Metrics, and a Future Beyond Images.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6N/cri-o-faster-pulls-better-metrics-and-a-future-beyond-images-sohan-kunkerkar-ayato-tokubi-red-hat
- YouTube search: https://www.youtube.com/results?search_query=CRI-O%3A+Faster+Pulls%2C+Better+Metrics%2C+and+a+Future+Beyond+Images+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=en2oz2BWHW8
- YouTube title: CRI-O: Faster Pulls, Better Metrics, and a Future Beyond Images - Sohan Kunkerkar & Ayato Tokubi
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cri-o-faster-pulls-better-metrics-and-a-future-beyond-images/en2oz2BWHW8.txt
- Transcript chars: 25133
- Keywords: memory, runtime, kernel, cublet, actually, container, feature, protection, request, spiegel, worker, containers, guaranteed, layers, across, artifacts, registry, images

### Resumo baseado na transcript

Uh I know it's the last day of CubeCon and I hope you had enjoyed some interesting sessions and we are going to make this session also engaging and we have a lot of things to cover in this presentation. I'm one of the Kaio maintainers and actually involved in sign activities. It implements Kubernetes container runtime interface and supports OCI compliant images, registries and containers. So in cryo we believe uh simplicity balanced approach where we try to make sure we get some of the features which are battle tested both in upstream kubernetes as well as the cryo side and uh cryo release version goes lock step with kubernetes one. So you will always see kubernetes releases uh and the changes in the latest cryo release and last but not the least but very important cryo is a CNCF graduated project. So it's majority defense with the wider adoption across both open shift and kubernetes.

### Excerpt da transcript

Good afternoon everyone. Thank you all for joining us today. Uh I know it's the last day of CubeCon and I hope you had enjoyed some interesting sessions and we are going to make this session also engaging and we have a lot of things to cover in this presentation. So let's get started. Let me let me introduce myself. I'm San Kerkar. I work at Red Hat as a senior software engineer. I'm one of the Kaio maintainers and actually involved in sign activities. I'm also uh contributing to Q which is uh queuing system for batch workloads and I'm the reviewer of the project. With me we have Ayatu Tokobi. He's also the co-maintainer for cryo and actually involved with sig node. So here is the agenda for today's talk. We're going to quickly cover the introduction to cryo for those who are new. Then we'll talk about the cryo updates including the sign node that we are working in the upstream side. Then towards the end we'll see how uh peer-to-peer image distribution fits into cryo system followed by a short demo and towards the end we'll open for question answers.

All right can I get a quick show of hands how many of you know about cryo? Cool. So I'll probably quickly cover what is cryo. Uh it's as you see the acronym CRI it's container runtime interface. O came from the open uh container initiative. So it it is specifically designed for Kubernetes. It implements Kubernetes container runtime interface and supports OCI compliant images, registries and containers. So in a nutshell you can say cryo spins up the pod, creates the containers and dumps a log where it should be. So in cryo we believe uh simplicity balanced approach where we try to make sure we get some of the features which are battle tested both in upstream kubernetes as well as the cryo side and uh cryo release version goes lock step with kubernetes one. So you will always see kubernetes releases uh and the changes in the latest cryo release and last but not the least but very important cryo is a CNCF graduated project. So it's majority defense with the wider adoption across both open shift and kubernetes.

So with this I'll hand it over to who will cover some of the cry updates. Hello everyone. Uh as you probably already know um cryo talks to cublet to know like what containers and what ports are running on that node. And I'm going to talk about some uh Kubernetes upstream related uh features in cryo and also some like cryo uh specific uh features in my part. So first one is CL list streaming. So in some ca
