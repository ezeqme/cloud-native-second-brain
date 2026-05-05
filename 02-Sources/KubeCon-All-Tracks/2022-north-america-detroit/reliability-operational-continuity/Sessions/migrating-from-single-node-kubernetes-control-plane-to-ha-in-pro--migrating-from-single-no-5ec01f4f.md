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
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Cong Yue", "David Oppenheimer", "Databricks"]
sched_url: https://kccncna2022.sched.com/event/182Iq/migrating-from-single-node-kubernetes-control-plane-to-ha-in-production-cong-yue-david-oppenheimer-databricks
youtube_search_url: https://www.youtube.com/results?search_query=Migrating+From+Single-Node+Kubernetes+Control+Plane+To+HA+In+Production+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Migrating From Single-Node Kubernetes Control Plane To HA In Production - Cong Yue & David Oppenheimer, Databricks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Cong Yue, David Oppenheimer, Databricks
- Schedule: https://kccncna2022.sched.com/event/182Iq/migrating-from-single-node-kubernetes-control-plane-to-ha-in-production-cong-yue-david-oppenheimer-databricks
- Busca YouTube: https://www.youtube.com/results?search_query=Migrating+From+Single-Node+Kubernetes+Control+Plane+To+HA+In+Production+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Migrating From Single-Node Kubernetes Control Plane To HA In Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Iq/migrating-from-single-node-kubernetes-control-plane-to-ha-in-production-cong-yue-david-oppenheimer-databricks
- YouTube search: https://www.youtube.com/results?search_query=Migrating+From+Single-Node+Kubernetes+Control+Plane+To+HA+In+Production+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7nLvblrEaDQ
- YouTube title: Migrating From Single-Node Kubernetes Control Plane To HA In Product... Cong Yue & David Oppenheimer
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/migrating-from-single-node-kubernetes-control-plane-to-ha-in-productio/7nLvblrEaDQ.txt
- Transcript chars: 33743
- Keywords: control, server, migration, cluster, single, running, balancer, actually, architecture, controller, basically, process, traffic, workloads, manager, requests, databricks, workload

### Resumo baseado na transcript

welcome to kubecon North America today Kong and David will be going through this migration from single node kubernetes control print to Edge a production uh over to you David and Kong for housekeeping q a will be at the end so please raise your hand and we'll come back to you thank you software engineers at databricks and we're going to be talking about our experience migrating from a single node kubernetes control plane to a highly available control plane in production at databricks so uh briefly the outline

### Excerpt da transcript

welcome to kubecon North America today Kong and David will be going through this migration from single node kubernetes control print to Edge a production uh over to you David and Kong for housekeeping q a will be at the end so please raise your hand and we'll come back to you thank you software engineers at databricks and we're going to be talking about our experience migrating from a single node kubernetes control plane to a highly available control plane in production at databricks so uh briefly the outline of the talk is that first I'll talk about uh how we use kubernetes at databricks I'll talk about the non-ha control plane architecture that we used for many years uh then I'll discuss the ha control plane architecture that we moved to and how it handles different kinds of failures then Kong is going to talk about the migration process we use to move from the non-ha control plane to the ha control plane and then we'll wrap up with a discussion of some of the modifications we made to our day two processes to accommodate the ha control plane so the as a brief overview of what databricks is the databricks product is a SAS data platform that runs on the public clouds we call it the databricks lake house platform and it's a unified platform that serves many Enterprise data use cases such as data warehousing data engineering data science streaming and machine learning the service operates at a very large scale we have many thousands of customers and the aggregate workload that we manage is very large we launch more than 10 million VMS per day across Azure AWS and gcp and our customers use the platform to process many exabytes of data so this slide shows the high-level architecture of the databricks platform it consists of a control plane that runs in databricks owned Cloud accounts and a per customer data plane that runs in the customer's cloud account so you can see in the left hand box some of the services that constitute the databricks control plane these are multi-tenant services that run on kubernetes clusters and then the right hand box shows the data plane for One customer which consists of cloud storage and the compute that does all of the data processing for historical reasons on gcp the data plane runs on kubernetes but on AWS and Azure it runs on VMS that are not managed by kubernetes but that's the data plane this talk is about the control plane all of which runs on kubernetes so the databricks product gives customers the experience of a single u
