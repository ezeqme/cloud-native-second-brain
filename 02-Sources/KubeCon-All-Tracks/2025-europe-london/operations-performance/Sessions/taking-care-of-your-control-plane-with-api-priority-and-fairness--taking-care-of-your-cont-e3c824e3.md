---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Matteo Ruina", "Ayaz Badouraly", "Datadog"]
sched_url: https://kccnceu2025.sched.com/event/1tx80/taking-care-of-your-control-plane-with-api-priority-and-fairness-and-resource-quotas-matteo-ruina-ayaz-badouraly-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Taking+Care+of+Your+Control+Plane+With+API+Priority+and+Fairness+and+Resource+Quotas+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Taking Care of Your Control Plane With API Priority and Fairness and Resource Quotas - Matteo Ruina & Ayaz Badouraly, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Matteo Ruina, Ayaz Badouraly, Datadog
- Schedule: https://kccnceu2025.sched.com/event/1tx80/taking-care-of-your-control-plane-with-api-priority-and-fairness-and-resource-quotas-matteo-ruina-ayaz-badouraly-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Taking+Care+of+Your+Control+Plane+With+API+Priority+and+Fairness+and+Resource+Quotas+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Taking Care of Your Control Plane With API Priority and Fairness and Resource Quotas.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx80/taking-care-of-your-control-plane-with-api-priority-and-fairness-and-resource-quotas-matteo-ruina-ayaz-badouraly-datadog
- YouTube search: https://www.youtube.com/results?search_query=Taking+Care+of+Your+Control+Plane+With+API+Priority+and+Fairness+and+Resource+Quotas+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=c73SzCKx-OY
- YouTube title: Taking Care of Your Control Plane With API Priority and Fairness an... Matteo Ruina & Ayaz Badouraly
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/taking-care-of-your-control-plane-with-api-priority-and-fairness-and-r/c73SzCKx-OY.txt
- Transcript chars: 29025
- Keywords: resource, priority, requests, cluster, resources, number, control, controller, object, server, incident, utilization, config, fairness, clusters, traffic, schema, running

### Resumo baseado na transcript

Hi, welcome to our talk to learn how to take down the Kubernetes control plane and more importantly how to take good care of it using two techniques the API priority and fairness and the resource kota. I started in the SR team and now I'm applying all the reality best practices to our internal Kubernetes platform. So why should you be uh interested in the performance and reliability of the control plane when this is used uh and operated by a third party? Spoiler alert, those are the API priority and fairness and the resource kota. We also present the challenges that we faced when we were using them with the default configuration and the lessons that we learned as we use them more extensively. So our Kubernetes clusters they are multi-tenant which means that they run various types of workloads from various team and with that we have the controllers that ensure the proper functionalities of the Kubernetes clusters.

### Excerpt da transcript

Hi, welcome to our talk to learn how to take down the Kubernetes control plane and more importantly how to take good care of it using two techniques the API priority and fairness and the resource kota. My name is Ayas Badali. I'm a software engineer at data dog. I started in the SR team and now I'm applying all the reality best practices to our internal Kubernetes platform. Hello everyone, it's great to be here. My name is Materowina. I'm a software engineer at data dog and I worked on the control plane and I'm working in the cluster life cycle automation. Data dog is a SAS monitoring company providing full observability on your applications. We over 2,000 engineers building the data platform which consists of workloads that are completely running on Kubernetes. To give you an idea of the scales, we are running hundred of thousands of pods over tens of thousands of nodes which are spread over dozens of Kubernetes clusters. Uh one detail over here is that we manage our own clusters which means that we deploy and operate the control plane that that is underlying the Kubernetes clusters.

If you don't and if you rely on manage Kubernetes clusters by third parties, don't worry. The best practices that we're going to introduce today are user side and you will still be able to use them uh to ensure the proper availability of the control plane of yours even though it is managed by a third party. So why should you be uh interested in the performance and reliability of the control plane when this is used uh and operated by a third party? It should just work right and be right. But we'll show you a few of the failures that we encountered where a single user could affect the stability of the whole platform for everyone in the cluster. And for each of those failure mods, we'll present the tools a cluster name can use to keep and ensure the stability of the platform. Spoiler alert, those are the API priority and fairness and the resource kota. We also present the challenges that we faced when we were using them with the default configuration and the lessons that we learned as we use them more extensively.

So our Kubernetes clusters they are multi-tenant which means that they run various types of workloads from various team and with that we have the controllers that ensure the proper functionalities of the Kubernetes clusters. Um all of them they coexist in an environment that is resource constrainted. The control pane itself is limited in resources and we successfully
