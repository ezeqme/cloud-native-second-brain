---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Michas Szacillo", "Wang Li", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1txFA/flink-on-karmada-building-resilient-data-pipelines-on-multi-cluster-k8s-michas-szacillo-wang-li-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Flink+on+Karmada%3A+Building+Resilient+Data+Pipelines+on+Multi-Cluster+K8s+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Flink on Karmada: Building Resilient Data Pipelines on Multi-Cluster K8s - Michas Szacillo & Wang Li, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Michas Szacillo, Wang Li, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1txFA/flink-on-karmada-building-resilient-data-pipelines-on-multi-cluster-k8s-michas-szacillo-wang-li-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Flink+on+Karmada%3A+Building+Resilient+Data+Pipelines+on+Multi-Cluster+K8s+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Flink on Karmada: Building Resilient Data Pipelines on Multi-Cluster K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFA/flink-on-karmada-building-resilient-data-pipelines-on-multi-cluster-k8s-michas-szacillo-wang-li-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Flink+on+Karmada%3A+Building+Resilient+Data+Pipelines+on+Multi-Cluster+K8s+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mqXZ2T-jWuU
- YouTube title: Flink on Karmada: Building Resilient Data Pipelines on Multi-Cluster K8s - Michas Szacillo & Wang Li
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/flink-on-karmada-building-resilient-data-pipelines-on-multi-cluster-k8/mqXZ2T-jWuU.txt
- Transcript chars: 22180
- Keywords: cluster, application, failover, apache, clusters, healthy, carmata, applications, platform, deployment, resource, actually, carmada, processing, running, health, scheduled, unhealthy

### Resumo baseado na transcript

I'm sure it's been a long day so hopefully uh it doesn't feel too long. Um so here's our talk Flink on Carmata building resilient data pipelines on multicluster Kubernetes. With that background in mind, we'll review some of the challenges we faced with managing Flink applications in a multicluster environment while ensuring resil resiliency and how we were able to use Carmata to support automated and stateful cluster failover. So, at Bloomberg, we operates a large scale streaming platform that empowers critical financial data processing. We currently have around 1,000 unique Apache Flink jobs running on top of multiple Kubernetes cluster spread across multiple tiers. Given this scale, ensure reliability and efficiency is our top priority.

### Excerpt da transcript

Hi everyone. Uh welcome to our talk. Uh thank you so much for coming. I'm sure it's been a long day so hopefully uh it doesn't feel too long. Um so here's our talk Flink on Carmata building resilient data pipelines on multicluster Kubernetes. Um we'll guide you through the journey that we went through to support stateful application failover on Apache Flink and the collaboration that took place between the Carmada community as well as the Bloomberg streaming platform team to add this support. Hopefully by the end you'll have followed along been introduced to the Carmada project and learned some of the basics about how you can improve your data pipeline resiliency as well. So starting with introductions, my name is Mihas Chachilo. Um I'm a senior software engineer and tech lead at Bloomberg. Uh my name is Leewan and I'm also a software engineer from Bloomberg as well. Together we work on the streaming platform team which provides Apache Flink to many different users within Bloomberg. Oh sorry. Uh for the agenda today um we'll start with a condensed overview of Apache Flink for those who might not be familiar.

Um so we can provide just more context for you as it's the main point of our talk. Specifically, we'll touch a little bit about the importance of application state and the recovery mechanisms that we already um that are already provided by Apache Flink. With that background in mind, we'll review some of the challenges we faced with managing Flink applications in a multicluster environment while ensuring resil resiliency and how we were able to use Carmata to support automated and stateful cluster failover. Finally, we'll touch on the overall benefits of Carmada, the outcomes, limitations, and further improvements. We're working together with the Carmada community um to improve. So, at Bloomberg, we operates a large scale streaming platform that empowers critical financial data processing. We currently have around 1,000 unique Apache Flink jobs running on top of multiple Kubernetes cluster spread across multiple tiers. This Flink jobs handles a variety of use cases including data ETL, real-time analytics, and event processing.

To give you an idea of its impact, this system is crucial to Bloomberg's core financial products, which provides real-time marketing insights to traders, analysts, and financial professionals across the world. it. This image here showcas the Bloomberg's terminal which is where the process data is visualized. Helping our user to
