---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Dejan Pejchev", "Priyanka Ravi", "G-Research"]
sched_url: https://kccncna2025.sched.com/event/27FaX/multi-cluster-wars-the-scheduler-awakens-dejan-pejchev-priyanka-ravi-g-research
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Cluster+Wars%3A+The+Scheduler+Awakens+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Multi-Cluster Wars: The Scheduler Awakens - Dejan Pejchev & Priyanka Ravi, G-Research

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Dejan Pejchev, Priyanka Ravi, G-Research
- Schedule: https://kccncna2025.sched.com/event/27FaX/multi-cluster-wars-the-scheduler-awakens-dejan-pejchev-priyanka-ravi-g-research
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Cluster+Wars%3A+The+Scheduler+Awakens+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Multi-Cluster Wars: The Scheduler Awakens.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FaX/multi-cluster-wars-the-scheduler-awakens-dejan-pejchev-priyanka-ravi-g-research
- YouTube search: https://www.youtube.com/results?search_query=Multi-Cluster+Wars%3A+The+Scheduler+Awakens+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=R0gDne5CuKs
- YouTube title: Multi-Cluster Wars: The Scheduler Awakens - Dejan Pejchev & Priyanka Ravi, G-Research
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/multi-cluster-wars-the-scheduler-awakens/R0gDne5CuKs.txt
- Transcript chars: 24461
- Keywords: cluster, scheduling, clusters, multicluster, worker, armada, management, control, admission, multiq, workloads, carmada, workload, volcano, single, resources, compute, controller

### Resumo baseado na transcript

So, we're really happy there is such an interest in multicluster bed schedulers. I'm a open source software engineer with the Jurarch open source uh software team. It's actually the perfect metaphor for how scheduling goes wrong when the system isn't designed for scale. In our analogy, that's like opening more security lanes in the same congested hallway. Imagine if the overhead security staff were scanning every badge twice because too many people were requesting their attention. When a single cluster hits control plane pain such as CD churn, um API P99 spikeuler backlog, we scale out, not up.

### Excerpt da transcript

Okay. Hello. So, we're really happy there is such an interest in multicluster bed schedulers. So, my name is Dan Pachev. I'm a open source software engineer with the Jurarch open source uh software team. So, we'd like to welcome you to our talk multicluster wars theuler awakens. So with my colleague, we'll walk you through bet scheduling and do a deep dive of how various bet schedulers approach the concept of multicluster. So Pinky, >> hi. >> Um my name is Priyanka Ravi. I also go by Pinky and I am a tech advocate at G Research. Before we dive into schedulers, I want to set the stage with the why. Why batch scheduling is important, where single clusters start to fall apart, and why must multicluster scheduling becomes necessary. And once we've got that foundation, I'll hand things over to Dan to walk us through the schedulers themselves and different approaches the ecosystem offers. Batch scheduling is all about coordinating workloads that start, run, and complete. Things like training jobs, simulations, pipelines, analytics, or research web hooks.

Research workloads. We all either had to deal with or know people who were stuck in that massive line yesterday to get into this conference center. It's actually the perfect metaphor for how scheduling goes wrong when the system isn't designed for scale. Every batch scheduler, regardless of how sophisticated it is, uses the same core primitives. So the first is queuing and prioritization. First in, first out is cute, but not for production or conference lines. We need a coordinator at the door. Critical jobs up front, experiments later. Yesterday's security line didn't do that. speakers, staff, and attendees were all in the same queue. In a cluster, that's like letting latency sensitive workloads wait behind test jobs. The goal is to ship the important stuff first without letting hardware slide. So, um, second is bin packing. Think Tetris with CPUs, GPUs, and memory in that security line. It's like leaving the other entrances empty, which they were because no one's directing traffic. Good packing fills every lane and every node efficiently.

Um, when we waste little pockets of compute, we're basically leaving money scattered across the cluster. Gang scheduling. Some workloads are a band, not soloist. Everything must start together or it sounds awful. We launch the whole gang or nothing. So MPI and training jobs don't half start and block everything else. Fair share prevents hogs. It's the equivalent of not lett
