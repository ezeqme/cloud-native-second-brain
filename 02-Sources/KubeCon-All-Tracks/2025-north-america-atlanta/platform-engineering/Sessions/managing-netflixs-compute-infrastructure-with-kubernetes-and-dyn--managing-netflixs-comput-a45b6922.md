---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Charles Zheng", "Nick Parker", "Netflix"]
sched_url: https://kccncna2025.sched.com/event/27FZx/managing-netflixs-compute-infrastructure-with-kubernetes-and-dynamic-capacity-management-charles-zheng-nick-parker-netflix
youtube_search_url: https://www.youtube.com/results?search_query=Managing+Netflix%E2%80%99s+Compute+Infrastructure+With+Kubernetes+and+Dynamic+Capacity+Management+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Managing Netflix’s Compute Infrastructure With Kubernetes and Dynamic Capacity Management - Charles Zheng & Nick Parker, Netflix

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Charles Zheng, Nick Parker, Netflix
- Schedule: https://kccncna2025.sched.com/event/27FZx/managing-netflixs-compute-infrastructure-with-kubernetes-and-dynamic-capacity-management-charles-zheng-nick-parker-netflix
- Busca YouTube: https://www.youtube.com/results?search_query=Managing+Netflix%E2%80%99s+Compute+Infrastructure+With+Kubernetes+and+Dynamic+Capacity+Management+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Managing Netflix’s Compute Infrastructure With Kubernetes and Dynamic Capacity Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZx/managing-netflixs-compute-infrastructure-with-kubernetes-and-dynamic-capacity-management-charles-zheng-nick-parker-netflix
- YouTube search: https://www.youtube.com/results?search_query=Managing+Netflix%E2%80%99s+Compute+Infrastructure+With+Kubernetes+and+Dynamic+Capacity+Management+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vaTOiXR2KSM
- YouTube title: Managing Netflix’s Compute Infrastructure With Kubernetes and Dynamic... Charles Zheng & Nick Parker
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/managing-netflixs-compute-infrastructure-with-kubernetes-and-dynamic-c/vaTOiXR2KSM.txt
- Transcript chars: 31848
- Keywords: cluster, capacity, trough, federation, scaling, netflix, workload, management, process, across, reason, disruption, around, custom, architecture, workloads, running, resource

### Resumo baseado na transcript

Um today we will be sharing how we use Kubernetes to manage the Netflix computer infrastructure and how we perform dynamic capacity management on top of it. So first I will give you an overview of our system and walk through each layer of our stack so you can get a clear picture of how everything fits together. I think one of the most important lessons we have learned during the past eight years is the most developer don't really care about Kubernetes specific concepts. This fundamental requirement has been there since day one of Titus API and even through we even though we switch from misos to kubernetes this API layer has remained largely unchanged. As you will see throughout this talk having a unified API layer like Titus can greatly simplify the overall system architect architecture and make managing large fleets much much more easier. So um now let's dive into the system architecture starting with our fleet topology.

### Excerpt da transcript

So thanks everyone for joining us today. I'm Charles. This is Nick. We are both members of comput platform and Netflix. Um today we will be sharing how we use Kubernetes to manage the Netflix computer infrastructure and how we perform dynamic capacity management on top of it. Today's talk will be dividing two parts. So first I will give you an overview of our system and walk through each layer of our stack so you can get a clear picture of how everything fits together. Then Nick will dive into the mechanisms we develop to on top of this platform to manage the cloud capacity. So before I dive into the system I wanted to introduce a term you have we will have you will hear a lot throughout this talk since I assume most of you are familiar with the basic Kubernetes concept. I would like to focus on something specific for Netflix which is Titus. So Titus is our original API that everyone at Netflix use to launch container workflow. Unlike some organization developers at Netflix don't use the Kubernetes API directly.

All workflow launch go through Titus. So Titus API has been around for over eight years. It originally sat in front of Misos before we migrated to Kubernetes. At the heart of Titus is a concept of Titus job. You can think of Titus job as a specialized type of Kubernetes workflow similar to deployment or job but with custom business logic tailored for Netflix. I think one of the most important lessons we have learned during the past eight years is the most developer don't really care about Kubernetes specific concepts. What matters to them is whether layer job or container can be launched and around their service. This fundamental requirement has been there since day one of Titus API and even through we even though we switch from misos to kubernetes this API layer has remained largely unchanged. As you will see throughout this talk having a unified API layer like Titus can greatly simplify the overall system architect architecture and make managing large fleets much much more easier. So um now let's dive into the system architecture starting with our fleet topology.

So Anle our cloud infrastructure is built on top of the cloud provider and spans multiple regions. In each region we operate a fleet of Kubernetes cluster. However we don't provide a single unifi entry point across regions. So when users want to launch containers, they need to specify the region where their workload should run. Within each region though there is a unifi entry point for
