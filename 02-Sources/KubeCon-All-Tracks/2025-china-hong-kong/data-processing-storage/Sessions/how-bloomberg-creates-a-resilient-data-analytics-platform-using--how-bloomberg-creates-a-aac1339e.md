---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Data Processing + Storage"
themes: ["Platform Engineering", "Storage Data", "SRE Reliability"]
speakers: ["Michas Szacillo", "Ilan Filonenko", "Bloomberg"]
sched_url: https://kccncchn2025.sched.com/event/1x5je/how-bloomberg-creates-a-resilient-data-analytics-platform-using-karmada-michas-szacillo-ilan-filonenko-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=How+Bloomberg+Creates+a+Resilient+Data+Analytics+Platform+Using+Karmada+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How Bloomberg Creates a Resilient Data Analytics Platform Using Karmada - Michas Szacillo & Ilan Filonenko, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Platform Engineering]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: China / Hong Kong
- Speakers: Michas Szacillo, Ilan Filonenko, Bloomberg
- Schedule: https://kccncchn2025.sched.com/event/1x5je/how-bloomberg-creates-a-resilient-data-analytics-platform-using-karmada-michas-szacillo-ilan-filonenko-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=How+Bloomberg+Creates+a+Resilient+Data+Analytics+Platform+Using+Karmada+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How Bloomberg Creates a Resilient Data Analytics Platform Using Karmada.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5je/how-bloomberg-creates-a-resilient-data-analytics-platform-using-karmada-michas-szacillo-ilan-filonenko-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=How+Bloomberg+Creates+a+Resilient+Data+Analytics+Platform+Using+Karmada+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oQMJj5Mf7QA
- YouTube title: How Bloomberg Creates a Resilient Data Analytics Platform Using... Michas Szacillo & Ilan Filonenko
- Match score: 0.868
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-bloomberg-creates-a-resilient-data-analytics-platform-using-karmad/oQMJj5Mf7QA.txt
- Transcript chars: 39944
- Keywords: resource, cluster, endpoint, application, platform, apache, deployment, carmata, clusters, status, connect, failover, scheduling, resources, health, across, management, unified

### Resumo baseado na transcript

I would like to welcome you all to our talk on how Bloomberg creates a resilient data analytics platform on Carmada. My name is Alain and I'll be speaking with my colleague Mihash who works with me at Bloomberg on cloudnative data analytics infrastructure. Trino, another distributed compute engine for interactive and batch exploration that uses NCSQL APIs for its querying. Kubernetes provides an extremely powerful compute, networking, and scheduling abstraction on top of heterogeneous hardware types, and we rely on it heavily to both operate our platforms and teams with the right separation of concerns and ownership. By leveraging Kubernetes and an observability layer like Prometheus and Graphfana, the platforms can solely focus on operators that govern platform specific CRDs like a Spark CRD, a Flink application CRD or Trino CRD and rely on lower infrastructure substrates to provide the necessary platform But given the current feature set that Kubernetes provides, these data analytic platforms are limited in what they can provide for their users.

### Excerpt da transcript

So hello everyone. I would like to welcome you all to our talk on how Bloomberg creates a resilient data analytics platform on Carmada. My name is Alain and I'll be speaking with my colleague Mihash who works with me at Bloomberg on cloudnative data analytics infrastructure. To kick things off, I would like to walk through the agenda for today's talk. We will begin by giving a short introduction to Bloomberg's data landscape and how how our uh and how our organization has built a data analytics platform spread across multiple Kubernetes clusters and the challenges that we have encountered in operating in such a platform and then we will talk in depth about how Cromada has functioned as a solution for Apache Flink and poses as a promising fit for solving the challenges in Trino and Apache Spark and lastly we will close out by highlighting the ongoing improvements within the community. So when looking at Bloomberg's data landscape, the key thing to highlight is the importance of Bloomberg's commitment towards providing extremely reliable, robust, and accurate data products.

These products operate at a huge scale with massive growth and spread across various data cataloging solutions and are ingested and explored with various analytical compute engines. to highlight some of the managed offerings that Bloomberg provides within its data analytics ecosystem. These include Apache Flink, which is a distributed processing engine for data streams that uses data stream APIs for its real-time processing. Trino, another distributed compute engine for interactive and batch exploration that uses NCSQL APIs for its querying. And Apache Spark, a third distributed compute engine for batch ingestion and interactive exploration that uses dataf frame APIs for its analytics. Putting these analytical engines together, what you see on the screen is an example of a data analytics pipeline that a data engineering team may manage for their business use case. As we provide these data analytics pipelines for our teams, building a scalable, selfservice, reliable, and multi-tenant platform is critical.

Kubernetes provides an extremely powerful compute, networking, and scheduling abstraction on top of heterogeneous hardware types, and we rely on it heavily to both operate our platforms and teams with the right separation of concerns and ownership. By leveraging Kubernetes and an observability layer like Prometheus and Graphfana, the platforms can solely focus on operators that govern p
