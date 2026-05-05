---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sourav Khandelwal", "Databricks"]
sched_url: https://kccncna2024.sched.com/event/1i7km/automated-multi-cloud-large-scale-k8s-cluster-lifecycle-management-sourav-khandelwal-databricks
youtube_search_url: https://www.youtube.com/results?search_query=Automated+Multi-Cloud+Large+Scale+K8s+Cluster+Lifecycle+Management+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Automated Multi-Cloud Large Scale K8s Cluster Lifecycle Management - Sourav Khandelwal, Databricks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Sourav Khandelwal, Databricks
- Schedule: https://kccncna2024.sched.com/event/1i7km/automated-multi-cloud-large-scale-k8s-cluster-lifecycle-management-sourav-khandelwal-databricks
- Busca YouTube: https://www.youtube.com/results?search_query=Automated+Multi-Cloud+Large+Scale+K8s+Cluster+Lifecycle+Management+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Automated Multi-Cloud Large Scale K8s Cluster Lifecycle Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7km/automated-multi-cloud-large-scale-k8s-cluster-lifecycle-management-sourav-khandelwal-databricks
- YouTube search: https://www.youtube.com/results?search_query=Automated+Multi-Cloud+Large+Scale+K8s+Cluster+Lifecycle+Management+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9E7lenP6pFc
- YouTube title: Automated Multi-Cloud Large Scale K8s Cluster Lifecycle Management - Sourav Khandelwal, Databricks
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/automated-multi-cloud-large-scale-k8s-cluster-lifecycle-management/9E7lenP6pFc.txt
- Transcript chars: 37202
- Keywords: cluster, clusters, create, basically, management, resources, provisioning, network, actually, workloads, created, controller, control, manage, upgrades, upgrade, creating, status

### Resumo baseado na transcript

all right um hi everyone thank you for joining um my name is s kelal I'm a software engineer at data bricks we have worked on various key areas to scale and manage our communities platform today I'm going to talk about how we build an automated way to manage the life cycle of our kuties clusters in a multicloud environment and this was instrumental to uh meet the growing demand of compute that we have seen at data brakes for those who are not very familiar with what data

### Excerpt da transcript

all right um hi everyone thank you for joining um my name is s kelal I'm a software engineer at data bricks we have worked on various key areas to scale and manage our communities platform today I'm going to talk about how we build an automated way to manage the life cycle of our kuties clusters in a multicloud environment and this was instrumental to uh meet the growing demand of compute that we have seen at data brakes for those who are not very familiar with what data break does uh datab aims to simplify data management by providing a comprehensive collaborative and scalable platform for data and AI so as you can see in all these bubbles we have we have different solutions that are catered towards different personas who wants to leverage data and AI capabilities uh be a data engineer data scientist machine learning engineer gen engineer or uh data uh analyst uh we have one platform where they can come in and uh get lever get insights from the data a lot of these products that we I discussed before uh are actually powered by our serverless architecture by serverless I mean that like we manage the compute for our customers so so that our customers don't have to worry or like deal with uh managing uh or setting up their accounts themselves uh and they can get a very serverless experience um let's like dive deep into how the servance architecture looks like so we have our database customer who wants to leverage some of our product the request actually comes to our control plan service here our control plan service our control plan cluster actually hosts a bunch of community services as you can see our frontend facing service is the web application Service uh and then we have a couple of other services like DB SQL for our SQL product Mosaic Mosaic AI for our AI uh product uh the request from the control plane Service uh gets routed to our data plane data plane is uh the place where we we basically schedule all our customer workloads uh who wants to run their data and AI tasks um data plane uh think of data plane as like a large Fleet of pubis clusters where we host all our customer workloads so uh this all these workloads uh talk to the customers account where the customers store their data in either of the three clouds S3 ADLs or gcp and um uh they basically run uh and like all the task uh get the data and run the task on top of that on top of the Clusters all as you can see that like all our cluster our clusters are actually at the core of all databas task
