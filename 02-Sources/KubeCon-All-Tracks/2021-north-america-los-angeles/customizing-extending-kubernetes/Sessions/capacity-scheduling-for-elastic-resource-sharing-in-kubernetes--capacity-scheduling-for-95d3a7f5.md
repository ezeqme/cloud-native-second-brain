---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Qingcan Wang", "Alibaba", "Yuan Chen", "Apple"]
sched_url: https://kccncna2021.sched.com/event/lV0A/capacity-scheduling-for-elastic-resource-sharing-in-kubernetes-qingcan-wang-alibaba-yuan-chen-apple
youtube_search_url: https://www.youtube.com/results?search_query=Capacity+Scheduling+for+Elastic+Resource+Sharing+in+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Capacity Scheduling for Elastic Resource Sharing in Kubernetes - Qingcan Wang, Alibaba & Yuan Chen, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Qingcan Wang, Alibaba, Yuan Chen, Apple
- Schedule: https://kccncna2021.sched.com/event/lV0A/capacity-scheduling-for-elastic-resource-sharing-in-kubernetes-qingcan-wang-alibaba-yuan-chen-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Capacity+Scheduling+for+Elastic+Resource+Sharing+in+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Capacity Scheduling for Elastic Resource Sharing in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0A/capacity-scheduling-for-elastic-resource-sharing-in-kubernetes-qingcan-wang-alibaba-yuan-chen-apple
- YouTube search: https://www.youtube.com/results?search_query=Capacity+Scheduling+for+Elastic+Resource+Sharing+in+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=B-8dGwU3gto
- YouTube title: Capacity Scheduling for Elastic Resource Sharing in Kubernetes - Qingcan Wang & Yuan Chen
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/capacity-scheduling-for-elastic-resource-sharing-in-kubernetes/B-8dGwU3gto.txt
- Transcript chars: 24048
- Keywords: quarter, gpu, resources, resource, scheduling, schedule, elastic, namespace, workloads, minimum, maximum, scheduler, cluster, management, workload, capacity, preemption, basically

### Resumo baseado na transcript

all right well good morning almost afternoon everybody welcome my name is randy i'm a cloud native ambassador with the cncf and this is the capacity scheduling for elastic resource sharing and kubernetes session and i would like you all online and here in person to welcome juan chen from apple thank you already [Applause] good morning good afternoon good evening we are so excited to be here it's the first on-site event almost in two years it's my sixth and cubecon was my sixth talk and now on-site and

### Excerpt da transcript

all right well good morning almost afternoon everybody welcome my name is randy i'm a cloud native ambassador with the cncf and this is the capacity scheduling for elastic resource sharing and kubernetes session and i would like you all online and here in person to welcome juan chen from apple thank you already [Applause] good morning good afternoon good evening we are so excited to be here it's the first on-site event almost in two years it's my sixth and cubecon was my sixth talk and now on-site and hope can get and make new friends get connected with the community for those people who are virtual and look forward to seeing you next time so today i'm co-presenting our work on capacity scheduling in kubernetes with ching chan unfortunately chinchon is not able to attend in person they will present a demo in a pre-recorded video later so a little bit about ourselves king tut is a software engineer from oni baba cloud he has been a very and active contributor in kubernetes especially the sikh scheduling group he made a lot of the code contribution design contribution to the kubernetes schedule i'm yan chen from apple cloud services i'm a kubernetes contributor too and my work is mainly focused on the kubernetes scheduling performance scalability okay i'd like to start with some background context and motivations about the work as all of all of us know kubernetes has becoming a de facto cluster and cloud resource management platform so more and more workloads and different type of workloads are running in kubernetes in addition to the traditional service workloads and now there are more batch workloads from the machine learning deep learning to big data workloads or running kubernetes a key issue we have realized after talking to our customers there are some look at today's kubernetes how does kubernetes manage resources between different users or name space so the quarter is a basic concept but quarter mainly used just for the admission control or capacity planning not involve the scheduling and in a more dynamic way the secondary the quarter so far we can define just a single value for example for each namespace that's the request the total request a namespace can ask for the third one is during the wrong time the resource coordination is purely based on priority and the default preemption we based on priority to do this and eviction to achieve this kind of the fairness or the resource education so as a result we can see and internet some of these more fle
