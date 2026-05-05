---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Zvonko Kaiser", "NVIDIA"]
sched_url: https://kccncna2025.sched.com/event/27FWQ/hybrid-confidential-cloud-democratize-secure-ai-with-gpus-and-confidential-containers-zvonko-kaiser-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Hybrid-Confidential-Cloud%3A+Democratize+Secure+AI+With+GPUs+and+Confidential+Containers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Hybrid-Confidential-Cloud: Democratize Secure AI With GPUs and Confidential Containers - Zvonko Kaiser, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Atlanta
- Speakers: Zvonko Kaiser, NVIDIA
- Schedule: https://kccncna2025.sched.com/event/27FWQ/hybrid-confidential-cloud-democratize-secure-ai-with-gpus-and-confidential-containers-zvonko-kaiser-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Hybrid-Confidential-Cloud%3A+Democratize+Secure+AI+With+GPUs+and+Confidential+Containers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Hybrid-Confidential-Cloud: Democratize Secure AI With GPUs and Confidential Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWQ/hybrid-confidential-cloud-democratize-secure-ai-with-gpus-and-confidential-containers-zvonko-kaiser-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Hybrid-Confidential-Cloud%3A+Democratize+Secure+AI+With+GPUs+and+Confidential+Containers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=afL3PqVEzVo
- YouTube title: Hybrid-Confidential-Cloud: Democratize Secure AI With GPUs and Confidential Contain... Zvonko Kaiser
- Match score: 1.008
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/hybrid-confidential-cloud-democratize-secure-ai-with-gpus-and-confiden/afL3PqVEzVo.txt
- Transcript chars: 26238
- Keywords: confidential, running, containers, overlay, station, workload, control, container, identity, compute, cluster, virtualization, storage, infrastructure, specific, protect, networking, gpu

### Resumo baseado na transcript

Hi everyone uh welcome to my session Harvard cloud GPUs democratized secure AI with confidential containers my name is Kaiser I'm with the cloud native team uh at Nvidia and uh I'm also responsible for all things related to kata and confidential containers this talk is part of a multi-series of talks that I gave in in the past so let's do some some recap Okay. Um and as we all know today why we are here Kubernetes is the platform of choice for any aim ML pipeline. Um, if you look at it, Kubernetes essentially a huge shared state between all pods. They're sharing storage and they're sharing all the uh all the control plane. Um once a attacker is on the node it's completely game over for for any Kubernetes cluster because then you label yourself as a master take over master nodes uh lateral movement to maybe other clusters or availability zones.

### Excerpt da transcript

Hi everyone uh welcome to my session Harvard cloud GPUs democratized secure AI with confidential containers my name is Kaiser I'm with the cloud native team uh at Nvidia and uh I'm also responsible for all things related to kata and confidential containers this talk is part of a multi-series of talks that I gave in in the past so let's do some some recap Okay. Um, one of the talks when I started to talk about confidential containers is to make the point that uh containers are not for isolation, right? Isolation. Uh, containers are more of a packaging mechanism to package a user space. It's not a means of isolation. So we need some sandboxing uh for containers to make um them more trusty worthiness right um there are the different threat models um if you're infrastructure owner and you want to protect your infrastructure from the workload you use kata to isolate uh your workload but when we are talking about confidential compute the threat model is 180° right where the workload does not trust the infrastructure So that's why we're running then containers in a confidential VM where a confidential VM is encrypting the memory encrypting the state registers and all the other stuff so that the infrastructure cannot have access to it right.

So we talked about how to protect the workload um and isolating containers but then we thought okay what about the thing that realizes our or creates our confidential container right where we extended the trust model also to the note where we're saying okay we need to protect also the note which realizes the confidential container because hypervisor is running on the node QM is running on the node all the helper libraries are running on the node that are realizing confidential container where I talked where I talked about you know we need to have a full stack at a station and at the station is u the method of of making sure that your state that you're expecting is really on the note right comparing values that you measure during runtime with some reference values that you have offsite uh which is called remote at the station right um the point was we need to protect the complete node from silicon up to the container with sbomb's uh signed images signed as bombs and all the other stuff that would entail the complete stack.

So we went from container, we went to the complete note. Um and as we all know today why we are here Kubernetes is the platform of choice for any aim ML pipeline. So we need to think about how we are also p
