---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Hongcai Ren", "Huawei", "Tessa Pham", "Wei-Cheng Lai", "Bloomberg"]
sched_url: https://kccncna2025.sched.com/event/27Nmh/karmada-in-action-scaling-ai-workloads-across-multi-cluster-at-scale-hongcai-ren-huawei-tessa-pham-wei-cheng-lai-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Karmada+in+Action%3A+Scaling+AI+Workloads+Across+Multi-Cluster+at+Scale+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Karmada in Action: Scaling AI Workloads Across Multi-Cluster at Scale - Hongcai Ren, Huawei; Tessa Pham & Wei-Cheng Lai, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Hongcai Ren, Huawei, Tessa Pham, Wei-Cheng Lai, Bloomberg
- Schedule: https://kccncna2025.sched.com/event/27Nmh/karmada-in-action-scaling-ai-workloads-across-multi-cluster-at-scale-hongcai-ren-huawei-tessa-pham-wei-cheng-lai-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Karmada+in+Action%3A+Scaling+AI+Workloads+Across+Multi-Cluster+at+Scale+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Karmada in Action: Scaling AI Workloads Across Multi-Cluster at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nmh/karmada-in-action-scaling-ai-workloads-across-multi-cluster-at-scale-hongcai-ren-huawei-tessa-pham-wei-cheng-lai-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Karmada+in+Action%3A+Scaling+AI+Workloads+Across+Multi-Cluster+at+Scale+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=M1-yTjC2hTI
- YouTube title: Karmada in Action: Scaling AI Workloads Across Multi-Clus... Hongcai Ren, Tessa Pham & Wei-Cheng Lai
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/karmada-in-action-scaling-ai-workloads-across-multi-cluster-at-scale/M1-yTjC2hTI.txt
- Transcript chars: 29971
- Keywords: cluster, clusters, resource, policy, control, across, federated, region, replicas, scheduling, workloads, hardware, member, features, single, inference, finally, custom

### Resumo baseado na transcript

Specifically, how you can use Kromata to overcome the massive challenge of scaling AI workloads across multiple Kubernetes clusters. Hong Kai Ren who is our Chromata maintainer and expert couldn't join us today but we're excited to walk you through all the Chromata 101's and 2011's today. While the idea of multicluster AI workloads is very tempting and appealing, we do run into massive challenges. How to decide where to deploy a workload based on several factors capacity cost latency. You will also lack a unified resource view if you just rely on individual Kubernetes schedulers because they're cluster local. Now on top of these general um multicluster challenges they are magnified when you deal with AI inference.

### Excerpt da transcript

Good afternoon everyone. Welcome to our talk. We're here today um to talk about Kmata in action. Specifically, how you can use Kromata to overcome the massive challenge of scaling AI workloads across multiple Kubernetes clusters. My name is Tessa Fam. I am a senior software engineer at Bloomberg. And joining me today is my teammate Way Changai. Oh, >> hi. I'm Way Changai. I'm the software engineer at Bloomberg working on AI platform. Hong Kai Ren who is our Chromata maintainer and expert couldn't join us today but we're excited to walk you through all the Chromata 101's and 2011's today. So the question of why we want to run AI workloads on multiple clusters is no longer new. Um first AI models now are huge and they are critical parts of applications. They are um production services. So it requires multiple region high availability for a continuity during any disaster. Secondly, when you run multicluster strategy um you can serve the you can solve the challenge of low latency because right now real-time AI inference demands very very low latency.

um you need to use geo distribution in order to have your model server as close as possible to the end users or to the data sources. Third, we want scalability and cost because we need to handle spiky demands by being able to burst capacity and utilize cheaper resources across different clouds um to save costs. Next, we'll get to centralizing management of diverse and expensive hardware like A100s and T4s. Um, with a multicluster management, you can pull them into one logical resource view. And finally, by diversifying your hardware and cloud providers, you can use multiple clouds and even onrem simultaneously to give you the infrastructure independence and avoid vendor and platform lock in. Multicluster strategy now is used quite widely for two key AI use cases. One is distributed training. So if you have a really large model um that you want to train parallelly across clusters or if you're running your infant services and you want to serve that model um globally in different regions. While the idea of multicluster AI workloads is very tempting and appealing, we do run into massive challenges.

The first one is obviously the operational complexity. It is hard to manage independent independent clusters including upgrades, patching, monitoring um and is quite labor intensive to do so manually. You will have to worry about synchronizing all the configs. So you need first consistent configs like arbbacks network pol
