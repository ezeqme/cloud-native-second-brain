---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Application + Development"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Chirag Narang", "Yugabyte"]
sched_url: https://kccnceu2021.sched.com/event/iE3s/building-the-multi-cluster-data-layer-chirag-narang-yugabyte
youtube_search_url: https://www.youtube.com/results?search_query=Building+the+Multi-Cluster+Data+Layer+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Building the Multi-Cluster Data Layer - Chirag Narang, Yugabyte

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Application + Development]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Chirag Narang, Yugabyte
- Schedule: https://kccnceu2021.sched.com/event/iE3s/building-the-multi-cluster-data-layer-chirag-narang-yugabyte
- Busca YouTube: https://www.youtube.com/results?search_query=Building+the+Multi-Cluster+Data+Layer+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Building the Multi-Cluster Data Layer.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3s/building-the-multi-cluster-data-layer-chirag-narang-yugabyte
- YouTube search: https://www.youtube.com/results?search_query=Building+the+Multi-Cluster+Data+Layer+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rfRiqLtwMwE
- YouTube title: Building the Multi-Cluster Data Layer - Chirag Narang, Yugabyte
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/building-the-multi-cluster-data-layer/rfRiqLtwMwE.txt
- Transcript chars: 23994
- Keywords: cluster, database, across, master, server, access, clusters, single, region, application, actually, setting, multiple, discovery, multi-cluster, distributed, switch, servers

### Resumo baseado na transcript

hi kubecon and welcome to building the multi-cluster data layer talk my name is chirag narang i'm a product lead at egobyte in today's session i'm going to show you how to build a multi-cluster data layer the easy way we'll go over some key requirements for deploying a database across multiple kubernetes clusters running in different regions and how to use a service mesh like sto to solve for networking challenges then we'll have the product demo and at the end i'm going to give you an interesting use

### Excerpt da transcript

hi kubecon and welcome to building the multi-cluster data layer talk my name is chirag narang i'm a product lead at egobyte in today's session i'm going to show you how to build a multi-cluster data layer the easy way we'll go over some key requirements for deploying a database across multiple kubernetes clusters running in different regions and how to use a service mesh like sto to solve for networking challenges then we'll have the product demo and at the end i'm going to give you an interesting use case for improving your application performance that you can use on your own so with that let's start with the ego by db project you could buy db is a fully open source distributed database which is built for the cloud native world it can be deployed across private and public clouds including kubernetes it reuses the query layer of postgres sql so it offers advanced features like triggers stored procedures partial indexes it allows easy migration from other databases like postgres mysql cassandra the database offers high resiliency and high availability the multi-node architecture allows you to survive different failures on the node level zone level region or entire data center it allows you to do zero downtime upgrades and security patching unlike traditional databases you can scale yiga by db horizontally to serve high throughput like billions of operations a day and store hundreds of terabytes of data you can reliably scale out and scale in on demand with larger data set without really impacting the application performance this ensures that you can handle peak traffic during black friday and cyber monday so once the holiday season is over you can always scale back eh you don't need maintenance maintenance window for these operations anymore all these operations can happen while your database is online you can distribute data across excuse me across zones regions or clouds with acid consistency so you can move data closer to your customers and comply with regulations like gdpr so very quickly let's look at the database design the guiding principle for gigabyte is a layered approach we built a plugable query engine which preserves the top half query layer of postgres and cassandra but at the storage layer is changed to use docdb which is common across both apis it is built using a custom integration of rough replication distributed asset transaction and the roxdb storage engine which all are based on the google spanner design so now next let's see what a few
