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
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Tasdik Rahman", "Javi Mosquera", "New Relic"]
sched_url: https://kccnceu2025.sched.com/event/1txDE/resilient-multi-cloud-strategies-harnessing-kubernetes-cluster-api-and-cell-based-architecture-tasdik-rahman-javi-mosquera-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=Resilient+Multi-Cloud+Strategies%3A+Harnessing+Kubernetes%2C+Cluster+API%2C+and+Cell-Based+Architecture+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Resilient Multi-Cloud Strategies: Harnessing Kubernetes, Cluster API, and Cell-Based Architecture - Tasdik Rahman & Javi Mosquera, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Tasdik Rahman, Javi Mosquera, New Relic
- Schedule: https://kccnceu2025.sched.com/event/1txDE/resilient-multi-cloud-strategies-harnessing-kubernetes-cluster-api-and-cell-based-architecture-tasdik-rahman-javi-mosquera-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=Resilient+Multi-Cloud+Strategies%3A+Harnessing+Kubernetes%2C+Cluster+API%2C+and+Cell-Based+Architecture+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Resilient Multi-Cloud Strategies: Harnessing Kubernetes, Cluster API, and Cell-Based Architecture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txDE/resilient-multi-cloud-strategies-harnessing-kubernetes-cluster-api-and-cell-based-architecture-tasdik-rahman-javi-mosquera-new-relic
- YouTube search: https://www.youtube.com/results?search_query=Resilient+Multi-Cloud+Strategies%3A+Harnessing+Kubernetes%2C+Cluster+API%2C+and+Cell-Based+Architecture+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4DjydLH21nM
- YouTube title: Resilient Multi-Cloud Strategies: Harnessing Kubernetes, Cluster API, and... T. Rahman & J. Mosquera
- Match score: 0.873
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/resilient-multi-cloud-strategies-harnessing-kubernetes-cluster-api-and/4DjydLH21nM.txt
- Transcript chars: 30546
- Keywords: cluster, control, specific, process, architecture, scheduling, inside, create, application, providers, running, management, objects, provider, carpenter, clusters, traffic, infrastructure

### Resumo baseado na transcript

Hello everyone and thanks for joining us uh to our session at at the end of this intense week. Uh we're going to showcase how a new relic we uh manage a multi cloud Kubernetes infrastructure levering cluster API on top of a cell architecture um in order to scale out uh workloads but also uh while limiting the blast radius uh for incidents. Now uh at a high level our architecture ingests and processes telemetry data from our customers that they send us instrumenting their applications and their infrastructure leveraging our agents. So for ingest data flows through HTTP endpoints exposed via CDNs and gets ingested and process it through a specific data pipelines depending on each data type uh preparing it for storage in our distributed New Relic database but also going into a hot path for triggering alert notifications. for the query path customers query this store data library in our UIs and APIs also exposed through a CDN. we are heavy CFKA users and we were running also a unique uh Kafka clusters uh in order to to accomplish that um because of this kind um monolithic infrastructure it was very hard to scale um update so any operation regarding adding nodes or

### Excerpt da transcript

Hello everyone and thanks for joining us uh to our session at at the end of this intense week. Uh we're going to showcase how a new relic we uh manage a multi cloud Kubernetes infrastructure levering cluster API on top of a cell architecture um in order to scale out uh workloads but also uh while limiting the blast radius uh for incidents. Uh my name is Javier Mosca Sanchez. I'm working as a so principal software engineer. Um I'm a Kubernetes and multicloud architect at New Relic and I'm joined at the stage uh by my colleague Tazik. Hey I'm Tazik and I work as a senior software engineer at New Relic in the same team as Javi. Cool. So we'll start outlining some context, some numbers uh about our scale, the the problem that we want to solve. Um also why we move to a cellular architecture um librarian also cluster API in order to implement uh this uh Kubernetes infrastructure in multiple cloud providers. Um, additionally, we are going to showcase how we added some layers uh on top of this to easy, uh, consumption for uh, instances and the the different offerings and nuances that the multi the cloud providers offer us.

Now what we do on New Relic uh we provide um intelligent observability platform that empowers developers to enhance uh digital experiences. Uh we have more than 85,000 active customers. Uh we process more than 400 400 million queries per day. Uh we ingest around seven pabytes per day. That makes uh at the end of the year around 3 xabytes. And with that we process 12 billion of events per minute. Now how does this um translate into uh Kubernetes? Uh so we operate all of these uh on top of uh 280 Kubernetes clusters. Um we operate we run more than uh 5,000 uh pots uh on on over the uh 21,000 nodes. Um and we run all of these in multiple cloud providers uh and multiple regions. Uh and our average cluster has uh between 300 and 500 uh nodes and we run on top of them on each of the of our clusters um around 5,000 and 7,000 bots. Now uh at a high level our architecture ingests and processes telemetry data from our customers that they send us instrumenting their applications and their infrastructure leveraging our agents.

Uh this could be done through language agents infrastructure agents cloud integrations etc. So for ingest data flows through HTTP endpoints exposed via CDNs and gets ingested and process it through a specific data pipelines depending on each data type uh preparing it for storage in our distributed New Relic database but also going i
