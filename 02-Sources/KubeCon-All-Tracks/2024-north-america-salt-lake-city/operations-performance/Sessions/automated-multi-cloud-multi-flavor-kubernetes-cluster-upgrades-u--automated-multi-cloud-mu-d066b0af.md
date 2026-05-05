---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Ziyuan Chen", "Databricks"]
sched_url: https://kccncna2024.sched.com/event/1i7kt/automated-multi-cloud-multi-flavor-kubernetes-cluster-upgrades-using-operators-ziyuan-chen-databricks
youtube_search_url: https://www.youtube.com/results?search_query=Automated+Multi-Cloud%2C+Multi-Flavor+Kubernetes+Cluster+Upgrades+Using+Operators+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Automated Multi-Cloud, Multi-Flavor Kubernetes Cluster Upgrades Using Operators - Ziyuan Chen, Databricks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Ziyuan Chen, Databricks
- Schedule: https://kccncna2024.sched.com/event/1i7kt/automated-multi-cloud-multi-flavor-kubernetes-cluster-upgrades-using-operators-ziyuan-chen-databricks
- Busca YouTube: https://www.youtube.com/results?search_query=Automated+Multi-Cloud%2C+Multi-Flavor+Kubernetes+Cluster+Upgrades+Using+Operators+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Automated Multi-Cloud, Multi-Flavor Kubernetes Cluster Upgrades Using Operators.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kt/automated-multi-cloud-multi-flavor-kubernetes-cluster-upgrades-using-operators-ziyuan-chen-databricks
- YouTube search: https://www.youtube.com/results?search_query=Automated+Multi-Cloud%2C+Multi-Flavor+Kubernetes+Cluster+Upgrades+Using+Operators+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LldZE-nNNj0
- YouTube title: Automated Multi-Cloud, Multi-Flavor Kubernetes Cluster Upgrades Using Operators - Ziyuan Chen
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/automated-multi-cloud-multi-flavor-kubernetes-cluster-upgrades-using-o/LldZE-nNNj0.txt
- Transcript chars: 38586
- Keywords: upgrade, upgrades, operators, actually, operator, workloads, cluster, clusters, process, configuration, running, version, called, basically, specific, clouds, always, custom

### Resumo baseado na transcript

my name is Zan uh I am a software engineer at data bricks and today I'm going to talk about automated multic Cloud multif flavor kubernetes cluster upgrades using operators so just a quick introduction of uh what data brakes is uh we are an endtoend data and AI platform we help customers understand their data so we run all of these workloads um on our platform for our customers so these include like machine learning streaming generative AI data data warehouse ETL uh and many other things all data their own logic to migrate their workloads for example I would like my uh inference pause to not be evicted using the eviction Pi but redeployed by making a request to the uh orchestrator service for machine learning based on application Level signals and uh

### Excerpt da transcript

my name is Zan uh I am a software engineer at data bricks and today I'm going to talk about automated multic Cloud multif flavor kubernetes cluster upgrades using operators so just a quick introduction of uh what data brakes is uh we are an endtoend data and AI platform we help customers understand their data so we run all of these workloads um on our platform for our customers so these include like machine learning streaming generative AI data data warehouse ETL uh and many other things all data brakes products run on kubernetes so we have uh a really large footprint of kubernetes uh it's really a multi-billion Dollar business that's totally run on kubernetes very early on we realized that we needed to upgrade all kubernetes nodes uh frequently and in this case monthly so we had uh required frequent OS security patches um for kubernetes notes so those are for compliance reasons and uh we had a kubernetes version upgrades so we need to uh get ined features from the community we want to get uh bug fixes and uh also security patches on kubernetes and uh we needed a way to roll out infrastructure changes uh so the changes include for example the node OS image uh we make a lot of changes to it over time uh the instance type upgrades um updates um we want to update no configurations we want to update the launch templates of the virtual machines that uh back the notes so uh yeah for all of these we needed to run upgrades very frequently and uh usually upgrades are considered to be just some operational work so like some engineer will just go and do it but we soon realized that for us uh it was very challenging we run on three clouds uh we have AWS edger and Google Cloud we have multiple regions per Cloud around the world like double digit of regions per cloud and uh we have four different kubernetes flavors AKA drrs we have uh eks on AWS AKs on aure uh gke on Google cloud and we also have our self-managed kubernetes clusters that actually run on all three clouds and uh at data breakes kubernetes runs workflows for both internal uh users and external customers so it's really just everything so we have uh microservices we have like serverless customer workflows like all the serverless functions uh serverless SQL UDF um all these data Brak uh products they uh automat automated run on kubernetes we have uh machine learning workloads and that's both uh internal and external um it uh it includes uh training and inference we also run internal tools and systems uh all t
