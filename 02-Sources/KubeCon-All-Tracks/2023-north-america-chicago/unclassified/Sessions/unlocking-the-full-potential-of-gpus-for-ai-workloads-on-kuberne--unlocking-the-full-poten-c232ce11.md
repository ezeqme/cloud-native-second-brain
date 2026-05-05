---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Kevin Klues", "NVIDIA"]
sched_url: https://kccncna2023.sched.com/event/1R2oG/unlocking-the-full-potential-of-gpus-for-ai-workloads-on-kubernetes-kevin-klues-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+the+Full+Potential+of+GPUs+for+AI+Workloads+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Unlocking the Full Potential of GPUs for AI Workloads on Kubernetes - Kevin Klues, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Kevin Klues, NVIDIA
- Schedule: https://kccncna2023.sched.com/event/1R2oG/unlocking-the-full-potential-of-gpus-for-ai-workloads-on-kubernetes-kevin-klues-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+the+Full+Potential+of+GPUs+for+AI+Workloads+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Unlocking the Full Potential of GPUs for AI Workloads on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oG/unlocking-the-full-potential-of-gpus-for-ai-workloads-on-kubernetes-kevin-klues-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+the+Full+Potential+of+GPUs+for+AI+Workloads+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1QfShSQLsbs
- YouTube title: Unlocking the Full Potential of GPUs for AI Workloads on Kubernetes - Kevin Klues, NVIDIA
- Match score: 0.956
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/unlocking-the-full-potential-of-gpus-for-ai-workloads-on-kubernetes/1QfShSQLsbs.txt
- Transcript chars: 24819
- Keywords: gpu, resource, parameters, driver, access, nvidia, cluster, called, object, running, support, device, sharing, control, allocated, available, container, reference

### Resumo baseado na transcript

hello my name is Kevin Clues and I'm a distinguished engineer at Nvidia I'm here today to talk about a new kubernetes feature called Dynamic resource allocation that will enable us to unlock the full potential of gpus for AI workloads on kubernetes as a community we've already built a solid foundation for GPU support in kubernetes and dynamic resource allocation is the feature we've been waiting for to take us to the next level so what does GPU support in kubernetes look like today well it requires a mix

### Excerpt da transcript

hello my name is Kevin Clues and I'm a distinguished engineer at Nvidia I'm here today to talk about a new kubernetes feature called Dynamic resource allocation that will enable us to unlock the full potential of gpus for AI workloads on kubernetes as a community we've already built a solid foundation for GPU support in kubernetes and dynamic resource allocation is the feature we've been waiting for to take us to the next level so what does GPU support in kubernetes look like today well it requires a mix of host level components as well as kubernetes specific components to be deployed on each node of a cluster that contains gpus where the host components consist of the Nvidia container toolkit and the GPU driver itself and the kubernetes specific components consist of those shown here where the K8 device plugin is the one that ultimately makes the gpus themselves visible to kubernetes with these in place requesting access access to gpus takes the form of an extended resource called nvidia.com GPU and specifying how many gpus you want access to under the hood the scheduler kuet and KH device plug-in will coordinate to find a node where gpus are available schedule the Pod there and inject the requested gpus into the container that requested them if you need access to a specific type of GPU a combination of node labels and node selectors can help direct the schuer to a node containing the specific type of GPU you are looking for in this case an a100 with 40 GB of GPU memory you also have the ability to request a fraction of a GPU through technology called multi-instance gpus or Mig for short in the example shown here we're requesting a MIG device that is 1/8 the size of a full a100 GPU using the canonical naming Convention of mig-1 g.

5gb in the last year or so we also added support for sharing access to gpus through over subscription on a perod basis cluster admins can configure the number of replicas they wish to over subscribe each GPU and users request access to these shared gpus with the special do shared extension shown here under the hood simple time slicing is used to swap one workload off and put another workload on the GPU after some fixed amount of time and this can be layered on top of the fractional GPU support provided by Mig as well we also provide an alternative to time slicing through a technology called multiprocess service or MPS which provides a software solution for running multiple jobs on top of a GPU or Meg device in parallel unlike t
