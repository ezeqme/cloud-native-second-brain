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
themes: ["Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Sung Yun", "Aki Sukegawa", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1txF1/trino-and-data-governance-on-kubernetes-sung-yun-aki-sukegawa-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Trino+and+Data+Governance+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Trino and Data Governance on Kubernetes - Sung Yun & Aki Sukegawa, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Sung Yun, Aki Sukegawa, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1txF1/trino-and-data-governance-on-kubernetes-sung-yun-aki-sukegawa-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Trino+and+Data+Governance+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Trino and Data Governance on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txF1/trino-and-data-governance-on-kubernetes-sung-yun-aki-sukegawa-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Trino+and+Data+Governance+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vCfehltPKxk
- YouTube title: Trino and Data Governance on Kubernetes - Sung Yun & Aki Sukegawa, Bloomberg
- Match score: 0.789
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/trino-and-data-governance-on-kubernetes/vCfehltPKxk.txt
- Transcript chars: 26388
- Keywords: access, catalog, owners, policy, cataloges, resources, cluster, control, within, specific, queries, platform, clusters, across, catalogs, policies, centralized, define

### Resumo baseado na transcript

This is S and Aki from Bloomberg and we're here to talk about Trino and data governance on Kubernetes. A story of how we were able to deploy Trino on as a pro service product on Kubernetes to meet the evolving requirements of data analytics and data governance within our company. For instance, a market data engineering team may build their data catalogs by utilizing a variety of ingestion tools like Apache Spark, Apachi Flink or even Pi iceberg. Truno is a scalable and highly distributed processing engine that optimizes query performance through parallel processing as well as predicate pushdowns that is very typical of a distributed processing engine and has it has a few new tricks up its sleeve as well. Uh it also optimizes query performance by distributed caching which allows the cluster to be able to uh avoid redundant S3 reads when it's repeatedly accessing the same object. So these qualities all have made Trino a data analytics tool of choice for a variety of workloads because let's face it the switching costs of having to learn the different quirks of multiple different data analytics tools is very much real and that's where we come in.

### Excerpt da transcript

Hello everyone. This is S and Aki from Bloomberg and we're here to talk about Trino and data governance on Kubernetes. A story of how we were able to deploy Trino on as a pro service product on Kubernetes to meet the evolving requirements of data analytics and data governance within our company. So here's a high level overview of the data environment at Bloomberg. Our teams deal with a massive scale of data often ranging in pabyte scale of financial data spanning across the global markets and we acquire data from a variety of different sources like market data news from over a 125,000 different curated news sources as well as thirdparty alternative data to name a few. Our teams often also ingest real-time streaming data and analytics for market insights. And recently there's been a growth of self-maintained data cataloges across teams utilizing on-prem S3 compatible object storage solutions to facilitate their analytical workloads. And last but not least, there's a need to secure data discovery for AI workloads so that only authorized users and AI applications can get access to the data for specified use cases.

So given these characteristics of our data environment, there was an opportunity to centralize our data analytics infrastructure with the goal of enabling our data owners to share data catalogs securely across many other teams. What you see on the screen here is an example of the data analyst pipeline that a data engineering team may manage at Bloomberg. For instance, a market data engineering team may build their data catalogs by utilizing a variety of ingestion tools like Apache Spark, Apachi Flink or even Pi iceberg. And in turn they would use a largecale distributed processing engine to extract and transform the data into a generative form or simply manage a data exploration tool to enable their data quality teams or their client support teams to interactively analyze data. So what is Trino and how does it help centralize the data analytics environment we have within our firm? Truno is a scalable and highly distributed processing engine that optimizes query performance through parallel processing as well as predicate pushdowns that is very typical of a distributed processing engine and has it has a few new tricks up its sleeve as well.

Uh it also optimizes query performance by distributed caching which allows the cluster to be able to uh avoid redundant S3 reads when it's repeatedly accessing the same object. Trino is also an NISSQL compliant
