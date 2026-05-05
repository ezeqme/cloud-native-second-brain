---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Frances Chong", "Coinbase"]
sched_url: https://kccncna2025.sched.com/event/27FZ5/rearchitecting-compute-at-coinbase-migrating-to-karpenter-for-fast-reliable-scaling-frances-chong-coinbase
youtube_search_url: https://www.youtube.com/results?search_query=Rearchitecting+Compute+at+Coinbase%3A+Migrating+To+Karpenter+for+Fast%2C+Reliable+Scaling+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Rearchitecting Compute at Coinbase: Migrating To Karpenter for Fast, Reliable Scaling - Frances Chong, Coinbase

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Frances Chong, Coinbase
- Schedule: https://kccncna2025.sched.com/event/27FZ5/rearchitecting-compute-at-coinbase-migrating-to-karpenter-for-fast-reliable-scaling-frances-chong-coinbase
- Busca YouTube: https://www.youtube.com/results?search_query=Rearchitecting+Compute+at+Coinbase%3A+Migrating+To+Karpenter+for+Fast%2C+Reliable+Scaling+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Rearchitecting Compute at Coinbase: Migrating To Karpenter for Fast, Reliable Scaling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZ5/rearchitecting-compute-at-coinbase-migrating-to-karpenter-for-fast-reliable-scaling-frances-chong-coinbase
- YouTube search: https://www.youtube.com/results?search_query=Rearchitecting+Compute+at+Coinbase%3A+Migrating+To+Karpenter+for+Fast%2C+Reliable+Scaling+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=06MmxgGbg6U
- YouTube title: Rearchitecting Compute at Coinbase: Migrating To Karpenter for Fast, Reliable Scali... Frances Chong
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/rearchitecting-compute-at-coinbase-migrating-to-karpenter-for-fast-rel/06MmxgGbg6U.txt
- Transcript chars: 29780
- Keywords: carpenter, actually, workloads, cluster, clusters, groups, autoscaler, instance, manage, having, around, across, itself, running, controller, disruption, managed, whatnot

### Resumo baseado na transcript

Um, today we're going to talk about migrating to Carpenter fast reliable scaling. Today we'll be talking about the background pre-scaling pre-Carper scaling problems like Carpenter the migration on architecture um, and lessons and future and Q&A. Um, and cluster autoscaler was actually in charge of changing the autoscaling group uh when a certain threshold was hit. once a certain threshold is hit it's going to um make a decision and figure out which um autoscaling group to scale. All right, so let's dive into some of the pain points we had and why we started hitting these limitations and what was like kind of the root problem for us. a node in that ASG and it's going to attempt to drain it in the 15 minute interval or 15-inute window and if it fails for some reason then that node group fails and so it's very non- Kubernetes native in that sense and it

### Excerpt da transcript

Hi everybody. Um, today we're going to talk about migrating to Carpenter fast reliable scaling. So this is the table of contents. Today we'll be talking about the background pre-scaling pre-Carper scaling problems like Carpenter the migration on architecture um, and lessons and future and Q&A. Just a quick intro. So, I'm Francis and I am a staff software engineer at Coinbase. Um, I work on the compute team which manages all Kubernetes clusters at Coinbase. Let's dive into the intro and background of Coinbase. So, we run approximately 160 EKS clusters. Um, and we were running previously on EKS manage node groups and also cluster autoscaler. Uh we did have Carpenter at that time but new and we were on the B1 alpha and B1 beta uh resources and this was only primarily for isolate uh workloads that needed additional isolation. Uh but at some point when we completed our migration about a year and a half ago over to Kubernetes we started to hit limitations on cluster autoscaler and also EKS managed node groups themselves.

just some context of how our clusters looked like back then. Um, each cluster would have its own managed node groups and this would comprise of different ones for infra, different ones for main service loads and whatnot. Um, and under the hood, if folks don't know, under EKS manage no group, an autoscaler group is attached. Um, and cluster autoscaler was actually in charge of changing the autoscaling group uh when a certain threshold was hit. Um, and so for this, you know that for every node group that you want to support, you have to create a separate node group for every instance type, which is pretty annoying. You're going to have to manage this. Say for instance, we have 160 clusters. That's just a ton of stuff to manage. And on average, when uh we saw no provisioning come up, it took about four minutes. This is assuming there's no capacity at all on the clusters themselves. So this is kind of the diagram. You can kind of see um here is the EKS cluster and we have some this is just kind of a very generic one where we have a main node group um with the autoscaling um group in each of these EKS node groups and once a certain threshold is hit it's going to um make a decision and figure out which um autoscaling group to scale.

All right, so let's dive into some of the pain points we had and why we started hitting these limitations and what was like kind of the root problem for us. So slow responsiveness, we saw kind of issues with scaling up a
