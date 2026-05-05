---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Peter Schuurman", "Google", "Matt Schallert", "Chronosphere"]
sched_url: https://kccncna2022.sched.com/event/182It/multi-cluster-stateful-set-migration-a-solution-to-upgrade-pain-peter-schuurman-google-matt-schallert-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Cluster+Stateful+Set+Migration%3A+A+Solution+To+Upgrade+Pain+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Multi-Cluster Stateful Set Migration: A Solution To Upgrade Pain - Peter Schuurman, Google & Matt Schallert, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Peter Schuurman, Google, Matt Schallert, Chronosphere
- Schedule: https://kccncna2022.sched.com/event/182It/multi-cluster-stateful-set-migration-a-solution-to-upgrade-pain-peter-schuurman-google-matt-schallert-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Cluster+Stateful+Set+Migration%3A+A+Solution+To+Upgrade+Pain+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Multi-Cluster Stateful Set Migration: A Solution To Upgrade Pain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182It/multi-cluster-stateful-set-migration-a-solution-to-upgrade-pain-peter-schuurman-google-matt-schallert-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=Multi-Cluster+Stateful+Set+Migration%3A+A+Solution+To+Upgrade+Pain+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hkyUqgwTZL8
- YouTube title: Multi-Cluster Stateful Set Migration: A Solution To Upgrade Pain - Peter Schuurman & Matt Schallert
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/multi-cluster-stateful-set-migration-a-solution-to-upgrade-pain/hkyUqgwTZL8.txt
- Transcript chars: 28192
- Keywords: cluster, clusters, application, across, replicas, storage, migration, staple, multi-cluster, stateful, workloads, replica, moving, orchestration, migrate, source, clients, operator

### Resumo baseado na transcript

all right uh hey everyone welcome to uh our talk today we're gonna be talking about uh multi-cluster stateful set migrations uh and how they can solve some of your upgrade payments um my name is Matt I'm a software engineer at chronosphere where I work on the infrastructure team dealing with all things storage reliability scalability and for chronosphere I was an SRE at Uber on the observability platform there and I'm Peter I work at Google on Staple workloads on gke so deal with storage drivers that GK

### Excerpt da transcript

all right uh hey everyone welcome to uh our talk today we're gonna be talking about uh multi-cluster stateful set migrations uh and how they can solve some of your upgrade payments um my name is Matt I'm a software engineer at chronosphere where I work on the infrastructure team dealing with all things storage reliability scalability and for chronosphere I was an SRE at Uber on the observability platform there and I'm Peter I work at Google on Staple workloads on gke so deal with storage drivers that GK uses we're connecting to storage infrastructure uh so a little general idea of what we're going to be talking about today I'm going to give you a bit of context on uh how we use kubernetes at chronosphere uh some of the use cases and challenges we have with uh cross cluster stateful workloads uh Peter is going to tell you about some of the work going on in open source kubernetes to make these use cases possible and we're going to show you a demo of how it all ties together so first to give you a little bit of context about what chronosphere does and how we use kubernetes chronosphere is a software as a service observability platform particularly built for high scale use cases in cloud-native environments and given how Mission critical observability is we have a really high SLA and we take reliability incredibly seriously to meet that SLA so although we have three nines uh in our SLA we aim for four nines and have achieved four nines in production uh part of the way that we achieve these reliability and fault tolerance needs is by running on top of kubernetes so our kubernetes footprint spans multiple regions with thousands of kubernetes nodes in total and over 40 000 pods in total each of these clusters were on a mix of stateless and stateful workloads but the largest stateful workload is our metrics data store which I'm going to tell you more about so the architecture of our metrics data store really heavily influences how we operate it how we deploy about it or sorry how we operate it how we think about it deploy it and kind of architect our clusters for it so our metrics data store is based on M3 which is an open source metrics engine and Metric datastore clusters are deployed as three separate stateful sets each in a separate Zone and each having the full copy of the data so data is sharded and started across multiple nodes in a stateful set and then each staple set owns an entire copy of the data all reads and writes are done through client-side Quorum
