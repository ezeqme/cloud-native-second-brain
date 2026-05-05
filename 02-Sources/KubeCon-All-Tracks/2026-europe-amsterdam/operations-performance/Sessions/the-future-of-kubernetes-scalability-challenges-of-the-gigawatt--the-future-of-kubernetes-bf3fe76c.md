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
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Maciek Różacki", "Google Cloud", "Artur Rodrigues", "Anthropic"]
sched_url: https://kccnceu2026.sched.com/event/2CVzF/the-future-of-kubernetes-scalability-challenges-of-the-gigawatt-computing-power-of-the-ai-era-maciek-rozacki-google-cloud-artur-rodrigues-anthropic
youtube_search_url: https://www.youtube.com/results?search_query=The+Future+of+Kubernetes+Scalability%3A+Challenges+of+the+GigaWatt+Computing+Power+of+the+AI+Era+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Future of Kubernetes Scalability: Challenges of the GigaWatt Computing Power of the AI Era - Maciek Różacki, Google Cloud & Artur Rodrigues, Anthropic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maciek Różacki, Google Cloud, Artur Rodrigues, Anthropic
- Schedule: https://kccnceu2026.sched.com/event/2CVzF/the-future-of-kubernetes-scalability-challenges-of-the-gigawatt-computing-power-of-the-ai-era-maciek-rozacki-google-cloud-artur-rodrigues-anthropic
- Busca YouTube: https://www.youtube.com/results?search_query=The+Future+of+Kubernetes+Scalability%3A+Challenges+of+the+GigaWatt+Computing+Power+of+the+AI+Era+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Future of Kubernetes Scalability: Challenges of the GigaWatt Computing Power of the AI Era.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzF/the-future-of-kubernetes-scalability-challenges-of-the-gigawatt-computing-power-of-the-ai-era-maciek-rozacki-google-cloud-artur-rodrigues-anthropic
- YouTube search: https://www.youtube.com/results?search_query=The+Future+of+Kubernetes+Scalability%3A+Challenges+of+the+GigaWatt+Computing+Power+of+the+AI+Era+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y7FDWmLbLa4
- YouTube title: The Future of Kubernetes Scalability: Challenges of the GigaWatt... Maciek Różacki & Artur Rodrigues
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-future-of-kubernetes-scalability-challenges-of-the-gigawatt-comput/Y7FDWmLbLa4.txt
- Transcript chars: 31249
- Keywords: actually, clusters, cluster, scheduling, workloads, control, operate, platforms, companies, controllers, future, especially, capacity, training, microservices, pattern, solutions, upstream

### Resumo baseado na transcript

Uh together we will give you uh a glimpse into what we think is the future evolution of Kubernetes and what challenges we think it has to face uh so that it remains relevant in the gigawatt AI computing era. So what we're trying to give you folks here are the key points that we observing in the feud and the implications that steam the implications that steam out uh based on our own experience building some of the largest uh clusters um uh that we know of. >> And if we look at the most important representative workloads which actually are stretching uh the scale limits and the profile of Kubernetes project and the Kubernetes clusters. Um we um up until now the primary ones that were the driving function of of how Kubernetes has been growing and for a big part of its history were the primary active uh extending uh force for kubernetes scalability were microservices especially operated by large digital native companies that were founded with especially with the internet and cloud native era and the plat these platforms um operate a variety of services that uh um scale horizontally that are relatively fragmented into multiple microservices as the name suggests um and Now when we think about the um most problematic and actively stretching workloads when it comes to AI training platforms we're looking at well at the AI platforms we're looking at the AI training workloads which uh...

### Excerpt da transcript

Welcome everyone to the future of Kubernetes scalability talk. Uh together we will give you uh a glimpse into what we think is the future evolution of Kubernetes and what challenges we think it has to face uh so that it remains relevant in the gigawatt AI computing era. >> Uh we obviously do not know the future. So what we're trying to give you folks here are the key points that we observing in the feud and the implications that steam the implications that steam out uh based on our own experience building some of the largest uh clusters um uh that we know of. >> And my name is Arthur Rodriguez. I'm a member of technical staff at Entropic. I've been uh working on Kubernetes clusters there for the past two years. >> And my name is Mati Kjatski. I'm a product manager at Google and I've been working with the problems of uh operating at a very large scale with Kubernetes for the last eight years. And again a minor disclaimer of course we're going to share a lot of things that come with from our professional experience but the views and especially the opinions about the future and what the community should do are our own and not our companies.

And with that all right so let's first let's talk about um uh basics of the terminology and semantics. So usually when we say that Kubernetes has many is is a large scale cluster we mean how many nodes it have maybe nowadays we would say how many accelerators it actually has in one cluster but we in practice when you look at the realities of how it is to operate very large scale platforms. um just the compute power is really and the number of nodes is not the right uh parameter or not the right question to ask and workload patterns actually start to m more >> and the better question to ask we find uh especially lately it's uh what's the mutation rate that the cluster can sustain uh in our own synthetic uh uh load tests uh we find that uh it's in the order of five to 16 uh pod mutations per second obviously that varies a lot depending on what's the storage layer uh behind kind of that that that that that test. Um and that's the ceiling on CD uh regardless of the node count. So at some point you start growing your clusters and the nodes that you're adding on top of it, they're basically sitting idle because we cannot sustain the the those uh those pod mutation rates and that primarily comes from CD having a single kind of right ordering uh characteristic so that the pod write path uh as it's as it's shipped does not shard.
