---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["AI ML", "Networking", "Storage Data", "Kubernetes Core"]
speakers: ["Yuichiro Ueno", "Toru Komatsu", "Preferred Networks", "Inc."]
sched_url: https://kccncna2024.sched.com/event/1i7nw/distributed-cache-empowers-aiml-workloads-on-kubernetes-cluster-yuichiro-ueno-toru-komatsu-preferred-networks-inc
youtube_search_url: https://www.youtube.com/results?search_query=Distributed+Cache+Empowers+AI%2FML+Workloads+on+Kubernetes+Cluster+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Distributed Cache Empowers AI/ML Workloads on Kubernetes Cluster - Yuichiro Ueno & Toru Komatsu, Preferred Networks, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Networking]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Yuichiro Ueno, Toru Komatsu, Preferred Networks, Inc.
- Schedule: https://kccncna2024.sched.com/event/1i7nw/distributed-cache-empowers-aiml-workloads-on-kubernetes-cluster-yuichiro-ueno-toru-komatsu-preferred-networks-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Distributed+Cache+Empowers+AI%2FML+Workloads+on+Kubernetes+Cluster+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Distributed Cache Empowers AI/ML Workloads on Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nw/distributed-cache-empowers-aiml-workloads-on-kubernetes-cluster-yuichiro-ueno-toru-komatsu-preferred-networks-inc
- YouTube search: https://www.youtube.com/results?search_query=Distributed+Cache+Empowers+AI%2FML+Workloads+on+Kubernetes+Cluster+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bjiFFSRyXmo
- YouTube title: Distributed Cache Empowers AI/ML Workloads on Kubernetes Cluster - Yuichiro Ueno & Toru Komatsu
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/distributed-cache-empowers-ai-ml-workloads-on-kubernetes-cluster/bjiFFSRyXmo.txt
- Transcript chars: 21241
- Keywords: traffic, object, access, bucket, network, second, compute, therefore, consistent, solutions, storage, performance, drives, backend, consider, number, however, capacity

### Resumo baseado na transcript

I think it's time so let's get started thank you for all being here today's session is on distributed cash and PR a cloud on kubernetes crust we' buil a distributed Cash System on kubernetes and use it for a cloud in our own premise we've uploaded our slide so if you need please check it he's a u from Japan he works for preer networks which is a AI ml company in Japan I'll explain our company's cust in detail later I'm T which is colleagues also I'm a

### Excerpt da transcript

I think it's time so let's get started thank you for all being here today's session is on distributed cash and PR a cloud on kubernetes crust we' buil a distributed Cash System on kubernetes and use it for a cloud in our own premise we've uploaded our slide so if you need please check it he's a u from Japan he works for preer networks which is a AI ml company in Japan I'll explain our company's cust in detail later I'm T which is colleagues also I'm a founder of Yi sh shf SBX project and the Mainer of some OS related to cncf this is today's agenda so we first introduce background Ai and the M workload on kubernetes cruster second we talked about the main topic simple cast services that is developed for AI workloads to solve the problem that we talk about the background start we describe the Lear world use cases next in deoy consideration we describe techniques to achieve higher performance in the end we conclude the attack okay next which explains our background yeah thank you uh first we start the talk from artificial intelligence and machine learning workloads so let's consider the training or machine learning model that recognize a numerical digit we have a data set of pictures with numbers and the training job of deep newer networks here it is a correspond to a two commity spots so KU spots will access the data set and get the data samples and F the Deep new networks with the data samples so it will optimize the model then by continuing the iterations the Deep new network will become to be able to recognize the numbers here I'd like to look at the strategies to store the data set so we are Ai and ml company with onpl cluster so we need on premise solutions for that first one is a NFS so we can mount NFS storet to KU spots by using a host bu volume NFS is fast if the NFS server has a fast red drives fast CPUs uh yeah so if the number of client is limited the performance is acceptable however the large number of client access the NFS you can easily notice the performance slowdowns second one is object stretch we have on premise S3 compatible object stretch with open source software apure zones we are using hard drives as a back end so by adding a new hard drives we can scale the performance and its capacity actually the performance of hardk drives are not sufficient to perform a random deed of data set so it cannot be a solutions for the data set Rolling S is the no loal stres so our compute node with AI accelerators has additional nbme drives so it is d
