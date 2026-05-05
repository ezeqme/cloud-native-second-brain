---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Maulin Patel", "Pradeep Venkatachalam", "Google"]
sched_url: https://kccnceu2022.sched.com/event/ytlt/improving-gpu-utilization-using-kubernetes-maulin-patel-pradeep-venkatachalam-google
youtube_search_url: https://www.youtube.com/results?search_query=Improving+GPU+Utilization+using+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Improving GPU Utilization using Kubernetes - Maulin Patel & Pradeep Venkatachalam, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Maulin Patel, Pradeep Venkatachalam, Google
- Schedule: https://kccnceu2022.sched.com/event/ytlt/improving-gpu-utilization-using-kubernetes-maulin-patel-pradeep-venkatachalam-google
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+GPU+Utilization+using+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Improving GPU Utilization using Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlt/improving-gpu-utilization-using-kubernetes-maulin-patel-pradeep-venkatachalam-google
- YouTube search: https://www.youtube.com/results?search_query=Improving+GPU+Utilization+using+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=X876kr-LkPA
- YouTube title: Improving GPU Utilization using Kubernetes - Maulin Patel & Pradeep Venkatachalam, Google
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/improving-gpu-utilization-using-kubernetes/X876kr-LkPA.txt
- Transcript chars: 29549
- Keywords: gpu, sharing, memory, containers, single, workload, workloads, container, actually, utilization, configuration, basically, instances, physical, provisioning, solution, specify, context

### Resumo baseado na transcript

My name is Maulin and I'm a good group product manager in Google Cloud working on Kubernetes engine. So, in this talk we're going to show you how to improve GPU utilization using Kubernetes. So, they can actually focus on their core business mission, be it be training, serving, or high performance computing. So, let me quickly walk you through an architecture of Google Kubernetes engine. Google Kubernetes engine is a fully managed container orchestration platform provided by Google. Under utilization problem is especially acute for certain type of workloads such as inference, gaming, visualization, and notebooks.

### Excerpt da transcript

Good afternoon, everyone. My name is Maulin and I'm a good group product manager in Google Cloud working on Kubernetes engine. We all know that GPUs are very expensive resource. And utilization of a GPU is a core concern for all the GPU users. Poor utilization of the GPUs cost them dearly. So, in this talk we're going to show you how to improve GPU utilization using Kubernetes. So, in my humble opinion, I believe Kubernetes is an ideal platform for AI/ML and high performance computing workload. And there are three core reasons why I think Kubernetes is best suited for AI/ML and high performance computing workloads. Number one is portability. Kubernetes provide open, standard base, and cloud native APIs. This allows the practitioner to seamlessly port workloads between their laptops, private data center, and the public cloud. Second, Kubernetes can seamlessly scale from a single node to thousands of nodes. It supports auto scaling, auto provisioning, GPUs, TPUs, and many other advanced features that allows them to do a very large scale training and inference.

Third is productivity. Kubernetes makes the practitioner more productive by freeing them up from having to manage the underlying resources and compatibility issue. So, they can actually focus on their core business mission, be it be training, serving, or high performance computing. So, let me quickly walk you through an architecture of Google Kubernetes engine. Google Kubernetes engine is a fully managed container orchestration platform provided by Google. It has two main components. Control plane and data plane. Control plane comprises of many things including master nodes, API server, scheduler, etcd, and many other services. So, control plane provisions the data plane, which comprises of worker nodes. Worker node is the place where workloads run. And worker nodes can run the workloads using GPUs and TPUs. Worker nodes are grouped together as a node pool. All the nodes that belong to a single node pool share the configuration. Node pool is also the basic unit of auto scaling. All the nodes in the node pool either have a CPU or GPU to run the workload.

So, as I mentioned before, GPU utilization is a core concern for GPU users. And poor utilization cost them very, very dearly. What we have observed in our GKE fleet is that GPU utilization for typical workload is quite low. And the GPU utilization is actually getting worse day by day as GPUs are getting more and more powerful. A single workload may no
