---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Paolo Patierno", "Gantigmaa Selenge", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1tcxz/simplifying-apache-kafka-on-kubernetes-with-strimzi-paolo-patierno-gantigmaa-selenge-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Simplifying+Apache+Kafka+on+Kubernetes+With+Strimzi+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Simplifying Apache Kafka on Kubernetes With Strimzi - Paolo Patierno & Gantigmaa Selenge, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Paolo Patierno, Gantigmaa Selenge, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1tcxz/simplifying-apache-kafka-on-kubernetes-with-strimzi-paolo-patierno-gantigmaa-selenge-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Simplifying+Apache+Kafka+on+Kubernetes+With+Strimzi+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Simplifying Apache Kafka on Kubernetes With Strimzi.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxz/simplifying-apache-kafka-on-kubernetes-with-strimzi-paolo-patierno-gantigmaa-selenge-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Simplifying+Apache+Kafka+on+Kubernetes+With+Strimzi+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sLFmnCyZ89M
- YouTube title: Simplifying Apache Kafka on Kubernetes With Strimzi - Paolo Patierno & Gantigmaa Selenge, Red Hat
- Match score: 0.793
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/simplifying-apache-kafka-on-kubernetes-with-strimzi/sLFmnCyZ89M.txt
- Transcript chars: 27288
- Keywords: cluster, stream, storage, brokers, rebalancing, mirror, running, course, controller, control, zookeeper, custom, scaling, metadata, broker, support, within, streamy

### Resumo baseado na transcript

I am a software engineer working on Redat on the messaging and data streaming team. So mostly working on Apachi Kafka and even on stream that this is what we are going to talk about which is a CNCF incubating project. How however even that presents uh its own challenges because Kubernetes doesn't have that Kafka specific necessary Kafka specific knowledge um to keep that high maintain um highly uh sorry availability and performance. So streams manages Apache Cafka and Kubernetes as I said uh it's based on Kubernetes operator pattern and it provides various operators for running and managing cafka components and it and massively reduces uh operational overhead. So streams really allows you to run kubernet uh cafka in a kubernetes native way. It uses the CRDs to extend uh Kubernetes API to define uh Kafka resources and integrates that Kafka knowledge into the operator and that is uh really important when it comes to like doing upgrades and rolling updates and also manages Kafka resources through the

### Excerpt da transcript

Thank you very much for being here. Uh I am Paulo Paderno. I am a software engineer working on Redat on the messaging and data streaming team. So mostly working on Apachi Kafka and even on stream that this is what we are going to talk about which is a CNCF incubating project. Um and it's about running Kafka Kubernetes. I'm one of the core maintainers and with me there is Tina. Hi everyone. Uh my name is Kantasa but I usually go by Tina. So I'm a software engineer at Red Hat as well and I also contribute to StreamZ and Kafka as well. All right. Um so agenda for this session we will start with introducing um Kafka and StreamZy. So don't worry if you don't know too much about them and we'll also talk about some of the new features that came to streams uh such as craft tier storage and auto rebalancing. And we will also talk about some of the exciting upcoming features. So what is Apache Kafka? It's a leading distributed event streaming platform. Um it scales horizontally and has a it's highly available in fault tolerant and it has wide variety of use cases.

It can capture data in real time um from various sources uh data sources like database event driven applications or other cloud services and store that durably to be uh consumed by other systems to uh manipulate or um react to them in real time. So it was originally created by LinkedIn and open sourced under Apache uh software foundation. It's licensed under Apache license 20. So what is StreamZ? Um so it's also um open source project. It's CNC included project as Paulo already mentioned. It's also licensed under Apache license 20. Um so Kafka sounds great in terms of what it can offer but it is operationally very complex. Um that's why uh running CFKA on Kubernetes become very popular. it was probably the most popular way to run Kafka. How however even that presents uh its own challenges because Kubernetes doesn't have that Kafka specific necessary Kafka specific knowledge um to keep that high maintain um highly uh sorry availability and performance. So streams manages Apache Cafka and Kubernetes as I said uh it's based on Kubernetes operator pattern and it provides various operators for running and managing cafka components and it and massively reduces uh operational overhead.

So streams really allows you to run kubernet uh cafka in a kubernetes native way. It uses the CRDs to extend uh Kubernetes API to define uh Kafka resources and integrates that Kafka knowledge into the operator and that is uh real
