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
themes: ["AI ML", "Community Governance"]
speakers: ["Filip Křepinský", "Red Hat", "Lucy Sweet", "Uber", "Ryan Hallisey", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2EF6B/improving-pod-disruption-and-node-lifecycle-filip-krepinsky-red-hat-lucy-sweet-uber-ryan-hallisey-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Improving+Pod+Disruption+and+Node+Lifecycle+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Improving Pod Disruption and Node Lifecycle - Filip Křepinský, Red Hat; Lucy Sweet, Uber; Ryan Hallisey, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Filip Křepinský, Red Hat, Lucy Sweet, Uber, Ryan Hallisey, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2EF6B/improving-pod-disruption-and-node-lifecycle-filip-krepinsky-red-hat-lucy-sweet-uber-ryan-hallisey-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+Pod+Disruption+and+Node+Lifecycle+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Improving Pod Disruption and Node Lifecycle.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6B/improving-pod-disruption-and-node-lifecycle-filip-krepinsky-red-hat-lucy-sweet-uber-ryan-hallisey-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Improving+Pod+Disruption+and+Node+Lifecycle+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dpRlhe9EgiY
- YouTube title: Improving Pod Disruption and Node Lifecycle - Filip Křepinský, Lucy Sweet & Ryan Hallisey
- Match score: 0.763
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/improving-pod-disruption-and-node-lifecycle/dpRlhe9EgiY.txt
- Transcript chars: 27706
- Keywords: eviction, basically, application, request, graceful, responder, actually, maintenance, termination, shutdown, create, working, kubelet, ecosystem, status, lifecycle, management, imperative

### Resumo baseado na transcript

So, our working group focuses on trying to improve the entire node lifecycle experience with Kubernetes. So, that's anything from node drains and maintenance through through admitting what nodes kept taking nodes out of clusters. So, the ways how initially we decided to do graceful eviction or termination in Kubernetes was by introducing eviction API which is basically imperative path that you call and give an intent to evict a pod. So, for example, your application even if it's high available, it might prefer scaling out first before it scales down. And this is not something that is like natively supported in Kubernetes. And if you don't fulfill this contract, we will go to the next responder and we have a default responder in our in Kubernetes that is added to every pod and that's the original imperative eviction.

### Excerpt da transcript

Um, okay, everyone. Welcome to improving pod disruption and node lifecycle. So, my name is Lucy. I'm a staff software engineer at Uber. I'm joined on stage today by Philip from Red Hat and Ryan from Nvidia. We are the leads of the Kubernetes node lifecycle working group. So, our working group focuses on trying to improve the entire node lifecycle experience with Kubernetes. So, that's anything from node drains and maintenance through through admitting what nodes kept taking nodes out of clusters. All of these things that right now today are pretty reactive and things we're trying to improve these process flows. So, we're trying to do that in a few ways. I talked a bit about in the morning talk if you were there. Who was at the morning talk? Put your hand up if you were at the morning talk. Hey, nice to see you all. Um, so we're trying to do that in a few ways such as video eviction request API and to close the node maintenance which Philip and Ryan will speak about later. Um, so we work quite closely with a few of the other SIGs around Kubernetes, particularly node.

We're very closely tied in with them and also app scheduling auto scaling. Node is such a tight integration point that we end up having stakeholder SIGs in nearly every part of the K8s project. So, today we're going to talk about three particular projects that we wanted to call out in a more technical level. We're going to talk about eviction request which is if you were at the morning talk, you know is a way to to signal the intent to evict a workload before you actually evict it which allows you to much more complex logic before evicting the workload. We call that specialized lifecycle management. You may have seen it under the old kept name declarative node maintenance which I think gives a pretty good idea of what's going on there. And we're going to talk about graceful node shutdown and all of the kubelet amnesia bugs around the project. So, to start, I think Philip you're going to talk about the eviction request project. Yeah. So, when we talk about eviction like we have to look at the pod or pod disruption or termination in general.

So, as you know like there are many vectors on of like terminating a pod and it's very hard to like deal with deal with the termination in concise manner especially like if you don't have a high availability application or you require special handling of your application. So, there are ways today how you can do that. You can just use your SIGTERM handler in
