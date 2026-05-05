---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Marcin Wielgus", "Google", "Kevin Hannon", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1hoys/wg-batch-updates-whats-new-and-what-is-next-marcin-wielgus-google-kevin-hannon-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=WG+Batch+Updates%3A+What%E2%80%99s+New+and+What+Is+Next+CNCF+KubeCon+2024
slides: []
status: parsed
---

# WG Batch Updates: What’s New and What Is Next - Marcin Wielgus, Google & Kevin Hannon, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Marcin Wielgus, Google, Kevin Hannon, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1hoys/wg-batch-updates-whats-new-and-what-is-next-marcin-wielgus-google-kevin-hannon-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=WG+Batch+Updates%3A+What%E2%80%99s+New+and+What+Is+Next+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre WG Batch Updates: What’s New and What Is Next.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoys/wg-batch-updates-whats-new-and-what-is-next-marcin-wielgus-google-kevin-hannon-red-hat
- YouTube search: https://www.youtube.com/results?search_query=WG+Batch+Updates%3A+What%E2%80%99s+New+and+What+Is+Next+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aWxuaEFSarU
- YouTube title: WG-Batch Updates: What’s New and What Is Next? - Marcin Wielgus, Google
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/wg-batch-updates-whats-new-and-what-is-next/aWxuaEFSarU.txt
- Transcript chars: 24232
- Keywords: workloads, yellow, capacity, workload, cluster, little, sharing, probably, running, coming, scheduling, resources, working, deployment, around, researchers, ecosystem, server

### Resumo baseado na transcript

So batch working group is a forum to discuss enhancements to better support batch workloads in Kubernetes and by batch workload I mean everything that is related to uh high performance computing, AI, machine learning, data analytics, continuous integrations and the goal of this group We come from six scheduling, six apps, six nodes, six autoscaling and we definitely can operate with the six but we are not limited to the six. It can be classic pure vanilla kubernetes jobs or something from cubeflow portfolio in Q and in the remaining of this presentation we will refer to all of these things as workloads. It is very critical for machine learning erh stuff because these things require all parts and all pieces of computations to be present in order to make progress. Maybe with this accelerators, maybe on spot, maybe on demons, maybe on your reservation, maybe in a specific rack or maybe in specific nodes. It has built-in integration for various APIs for classical things from training and batch word like kubernetes jobs, job set, cubeflow portfolio, cubray as well as for inference/serving deployment, stateful set, leader worker set and other things that could be used universally like aer plane pods and pod groups.

### Excerpt da transcript

Hello everyone, welcome to bot working group updates. My name is Martin Velgus. I'm one of the organizers of this working group. Uh so you all gathered here. So you probably have some intuition what working group is all about. My laptop almost died. Okay. So batch working group is a forum to discuss enhancements to better support batch workloads in Kubernetes and by batch workload I mean everything that is related to uh high performance computing, AI, machine learning, data analytics, continuous integrations and the goal of this group is to reduce fragmentation in Kubernetes ecosystem. People in patchworking room come from different SIS. We come from six scheduling, six apps, six nodes, six autoscaling and we definitely can operate with the six but we are not limited to the six. Uh we also have some people who are uh just coming to this group from outside. The scope of the g group is to uh talk and discuss and do additions to batch related APIs. Think about job queuing and scheduling primitives. Uh do tools that maximize cluster utilization and make the best use of the hardware to improve the workload performance.

And we also work on supporting specialized hardware for batch, AI, ML and all that sort of stuff. uh how to take part uh probably the most important uh part of batchworking group is our slack channel. We have uh bi-weekly meetings. Uh they are both eur in European time friendly slot and in west coast Pacific time uh slot. The details you can find in the link below along with calendar invites, zooms, links and all of this stuff needed for you to join these meetings. What is uh bus working group doing? Probably our biggest endeavor and biggest project is Q. You may have heard of Q but for those who have not so far let me give you a little bit of introduction of what what is it. So uh Q acts a little bit like a bouncer in a club. He decides who who should wait, who can get in so that the uh club is not too crowded. And by club I mean Kubernetes cluster. It acts a little bit like a receptionist desks who admit people with pro reservation quickly and let other weights. It also acts like a little bit of a waiter in the restaurant which gives you to gives you the table and takes you to the desired seating.

[Music] And when we're talking about people, we are actually talking about various computational units that come to the cluster. And uh this can be in form of a ray job. It can be a plain pots. It can be classic pure vanilla kubernetes jobs or somet
