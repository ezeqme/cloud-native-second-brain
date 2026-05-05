---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Amit Kumar", "Kevin Xu", "Uber"]
sched_url: https://kccncna2023.sched.com/event/1R2qq/efficient-resource-utilization-for-batch-compute-on-kubernetes-amit-kumar-kevin-xu-uber
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Resource+Utilization+for+Batch+Compute+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Efficient Resource Utilization for Batch Compute on Kubernetes - Amit Kumar & Kevin Xu, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Amit Kumar, Kevin Xu, Uber
- Schedule: https://kccncna2023.sched.com/event/1R2qq/efficient-resource-utilization-for-batch-compute-on-kubernetes-amit-kumar-kevin-xu-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Resource+Utilization+for+Batch+Compute+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Efficient Resource Utilization for Batch Compute on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qq/efficient-resource-utilization-for-batch-compute-on-kubernetes-amit-kumar-kevin-xu-uber
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Resource+Utilization+for+Batch+Compute+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mmLD5GcUcec
- YouTube title: Efficient Resource Utilization for Batch Compute on Kubernetes - Amit Kumar & Kevin Xu, Uber
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/efficient-resource-utilization-for-batch-compute-on-kubernetes/mmLD5GcUcec.txt
- Transcript chars: 26651
- Keywords: resource, cluster, resources, clusters, workload, gpu, compute, available, capacity, regional, utilization, manager, create, within, special, workloads, multiple, sharing

### Resumo baseado na transcript

hello everyone welcome to the session my name is Amit and I have Kevin here with me both of us work for compute platform team at Uber compute platform team is part of platform engine group so in today's session we are going to talk about efficient resource utilization for batch compute on cetes we will talk about multiple challenges that we face while achieving efficient resource utilization and how we resolve all of them so coming to the agenda first we will talk about batch compute at Uber and

### Excerpt da transcript

hello everyone welcome to the session my name is Amit and I have Kevin here with me both of us work for compute platform team at Uber compute platform team is part of platform engine group so in today's session we are going to talk about efficient resource utilization for batch compute on cetes we will talk about multiple challenges that we face while achieving efficient resource utilization and how we resolve all of them so coming to the agenda first we will talk about batch compute at Uber and overview then we'll talk about importance of resource sharing and what types of challenges we face in in efficient resource utilization then we'll jump to Solutions some key of them are resource digal resource management and Federation and a specialized Hardware efficiency after that we'll talk about some of the future work that we are going to do in next year and then we'll happily answer some of your questions coming to the quick overview of compute team we have two forms of compute in compute team stateless compute and batch compute adya and Aura already talked about the stateless compute in the previous session in this session we are going to focus on batch compute the underlying architecture remains literally same for both stateless compute and batch compute earlier we were running on Pon powered by meos and now we are in the phase of migration to Coes all the lower level architecture like cran host treasure service and the physical hardware and the network infrastructure remain same as for the stateless compute in the batch compute we largely focus on machine learning jobs which is powered by our sister team Michelangelo we'll also talk about spark jobs and data science workbench so let's move on coming to the use cases at Uber we have both end user use cases and platform use cases which are solved through batch workloads some of the key end user use cases are writer pricing intelligence ETA estimation destination suggestion Etc like when you see Uber app and you see the ETS those are powered by B workloads from the platform team we solve some of the use cases like AI model training data science notebooks also through vatch workloads to solve all these use cases we largely depend on three types of processing Frameworks namely spark Ray cluster and Ray jobs and coord be on job sparkk jobs are solved through the spark application crd and the spark operator that is open source by Google Cloud platform Ray jobs are solved through the ray cluster crd and the ray o
