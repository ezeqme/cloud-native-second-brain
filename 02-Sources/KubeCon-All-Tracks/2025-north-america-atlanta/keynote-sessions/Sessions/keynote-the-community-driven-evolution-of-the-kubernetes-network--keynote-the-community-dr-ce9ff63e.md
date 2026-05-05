---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["Networking", "Kubernetes Core", "Community Governance"]
speakers: ["Lionel Jouin", "Software Engineer", "Red Hat", "Antonio Ojea", "Staff Software Engineer", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FYh/keynote-the-community-driven-evolution-of-the-kubernetes-network-driver-lionel-jouin-software-engineer-red-hat-antonio-ojea-staff-software-engineer-google
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+The+Community-Driven+Evolution+of+the+Kubernetes+Network+Driver+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: The Community-Driven Evolution of the Kubernetes Network Driver - Lionel Jouin, Software Engineer, Red Hat & Antonio Ojea, Staff Software Engineer, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Lionel Jouin, Software Engineer, Red Hat, Antonio Ojea, Staff Software Engineer, Google
- Schedule: https://kccncna2025.sched.com/event/27FYh/keynote-the-community-driven-evolution-of-the-kubernetes-network-driver-lionel-jouin-software-engineer-red-hat-antonio-ojea-staff-software-engineer-google
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+The+Community-Driven+Evolution+of+the+Kubernetes+Network+Driver+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: The Community-Driven Evolution of the Kubernetes Network Driver.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FYh/keynote-the-community-driven-evolution-of-the-kubernetes-network-driver-lionel-jouin-software-engineer-red-hat-antonio-ojea-staff-software-engineer-google
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+The+Community-Driven+Evolution+of+the+Kubernetes+Network+Driver+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1iFYEWx2zC8
- YouTube title: Keynote: The Community-Driven Evolution of the Kubernetes Network Dri... Lionel Jouin & Antonio Ojea
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-the-community-driven-evolution-of-the-kubernetes-network-drive/1iFYEWx2zC8.txt
- Transcript chars: 9425
- Keywords: network, resource, driver, resources, interface, working, networking, performance, applause, evolution, hardware, evolving, standard, ecosystem, workloads, training, interfaces, common

### Resumo baseado na transcript

>> We have been working at Kubernetes networking for a long time, maybe a long time. I've been working in Kubernetes for a long time as I said and I can say that Kubernetes is no longer only a project. And this needs is reshaping how we think about Kubernetes today and is evolving Kubernetes networking. So what works on one Kubernetes distribution would not necessarily work on another. And we were starting to lose the core promise of Kubernetes which is to have a consistent and portable API. Later in 2017 in Kubernetes the plug-in happier has a stable feature in Kubernetes.

### Excerpt da transcript

Hello QCOM. My name is Antonio Ha. I work at Google. And I'm Lionel from Red Hat. >> We have been working at Kubernetes networking for a long time, maybe a long time. Um, well, we are here because we want to share a story. The story of how this community was evolving Kubernetes networking. I've been working in Kubernetes for a long time as I said and I can say that Kubernetes is no longer only a project. Kubernetes is a standard. Kubernetes is the foundation of the cloud native ecosystem. And the other important thing is that Kubernetes is also evolving. Kubernetes is adapting for this new workloads, new workload that are coming from AI tco high performance computing. These workloads are different. They require new hardware, accelerators, TPUs, GPUs, synchronization with the network data center and the existing the standard Kubernetes networking model were not prepared for this. So if we dive into this new workloads, we can start to see some patterns. We see that these large BLM training that training models that need to execute uh complex operations and synchronize uh GPUs with high ultra low level latency.

If you have just milliseconds of latency, it causes a big penalty on the performance of the training job. In the other side in the telco space you need rock solid applications. You need multiple interference interfaces for redundancy. You need uh numa nick and CPU alignment for line rate packet processing. And as you can see there is a common pattern. All of them have a a common problem. They need tight access for hardware. And this needs is reshaping how we think about Kubernetes today and is evolving Kubernetes networking. So how do we solve this? Well, this evolution was not a single project. This was the result of an effort, a collaboration between multiple companies and communities and also the convergence of many ideas and experiment over several years. This is where the communitydriven part is so critical. When facing the limits, the community always find creative solutions. We saw this everywhere has every community was creating their own solution based on custom annotation and CRDs. This solution are brilliant.

They are solving immediate and real problem for the users. But they are also nonportable. They create fragmentation. So what works on one Kubernetes distribution would not necessarily work on another. And we were starting to lose the core promise of Kubernetes which is to have a consistent and portable API. The innovation coming first
