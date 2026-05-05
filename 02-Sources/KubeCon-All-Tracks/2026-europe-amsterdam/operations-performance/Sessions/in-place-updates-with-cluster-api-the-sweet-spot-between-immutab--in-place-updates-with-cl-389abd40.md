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
speakers: ["Fabrizio Pandini", "Stefan Büringer", "Broadcom"]
sched_url: https://kccnceu2026.sched.com/event/2CW1r/in-place-updates-with-cluster-api-the-sweet-spot-between-immutable-and-mutable-infrastructure-fabrizio-pandini-stefan-buringer-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=In-place+Updates+with+Cluster+API%3A+The+Sweet+Spot+Between+Immutable+and+Mutable+Infrastructure+CNCF+KubeCon+2026
slides: []
status: parsed
---

# In-place Updates with Cluster API: The Sweet Spot Between Immutable and Mutable Infrastructure - Fabrizio Pandini & Stefan Büringer, Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Fabrizio Pandini, Stefan Büringer, Broadcom
- Schedule: https://kccnceu2026.sched.com/event/2CW1r/in-place-updates-with-cluster-api-the-sweet-spot-between-immutable-and-mutable-infrastructure-fabrizio-pandini-stefan-buringer-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=In-place+Updates+with+Cluster+API%3A+The+Sweet+Spot+Between+Immutable+and+Mutable+Infrastructure+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre In-place Updates with Cluster API: The Sweet Spot Between Immutable and Mutable Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1r/in-place-updates-with-cluster-api-the-sweet-spot-between-immutable-and-mutable-infrastructure-fabrizio-pandini-stefan-buringer-broadcom
- YouTube search: https://www.youtube.com/results?search_query=In-place+Updates+with+Cluster+API%3A+The+Sweet+Spot+Between+Immutable+and+Mutable+Infrastructure+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CMf6rOPo9Z0
- YouTube title: In-place Updates with Cluster API: The Sweet Spot Between Immu... Fabrizio Pandini & Stefan Büringer
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/in-place-updates-with-cluster-api-the-sweet-spot-between-immutable-and/CMf6rOPo9Z0.txt
- Transcript chars: 24173
- Keywords: machine, cluster, update, create, machines, control, basically, disruption, replicas, additional, change, delete, replica, extension, updates, infrastructure, worker, upgrade

### Resumo baseado na transcript

Thank you for being here at the talk about cluster API and in place update. So okay next >> so I'm Fabritz Pandini I'm principal engineer at Broadcom and also cluster API maintainer. Now what's happen when you edit your pod is that Kubernetes you edit your YAML but Kubernetes is not going to change in place your pod. it and because it is the one of the key of the success of Kubernetes and cluster API it is because system based on on immutability have some nice properties and I let me mention mention two of them. Um there can be also friction at application level um because not every application is designed to handle drains or like single node um outages basically the node goes away in a nice way because maybe you only have one replica. So let's now move on and start talking about how we implemented uh in place and and a good way to understand this is to start talking about a few design principle that that were implemented in the proposal.

### Excerpt da transcript

Welcome everyone. Thank you for being here at the talk about cluster API and in place update. It is overwhelming to see so many people for a project like Luxer Abi. We are not talking about AI in this talk. So okay next >> so I'm Fabritz Pandini I'm principal engineer at Broadcom and also cluster API maintainer. >> I'm Stefan Ginger also principal engineer at Broadcom cluster API and also controller runtime maintainer. Okay, so in place updating cluster API for people that knows the project you should probably be aware that this has been a journey. This is probably the most complex change that we merged in last few years. It took really a while for the community to figure it out how to make it right. So in order to understand why this was so difficult from a technical standpoint, let's start setting a little bit of context. So immutability, let's talk about immutability in Kubernetes. When you create a pod, what happens is that a container, a piece of infrastructure gets created on your machine. Apply pod create.

Okay. Now what's happen when you edit your pod is that Kubernetes you edit your YAML but Kubernetes is not going to change in place your pod. Kubernetes is going to deletate the old pod and create a new one. So in in Kubernetes there is no in place updates. There is always create and delete. And cluster API is a project that treats machine like a mutable pod. Okay. So when you create a cluster, you create a new machine. When you scale up, you create. When you scale down, you delay. When you roll out changes, you first create and then delay. Okay. Why mutability is important? it and because it is the one of the key of the success of Kubernetes and cluster API it is because system based on on immutability have some nice properties and I let me mention mention two of them. So system based on mutability are simple. They are based only on two primitives. They are not complex to implement. And the fact that that they are simple, it makes those system more robust, less errorprone, less racy when things happen.

The second properties that I would like to highlight is that system based on immutability are also more predictable are more reliable because whenever you create a new machine or a new pod you create starting from a trusted image. You create a pod you start from the uh docker image. You create a machine you start from your machine image. So what does it means? It means that there is no configuration drift. All your pod, all your machine looks the
