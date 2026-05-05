---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Arpit Singh", "Abhijit Paithankar", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7qv/enabling-fault-tolerance-for-gpu-accelerated-ai-workloads-in-kubernetes-arpit-singh-abhijit-paithankar-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Enabling+Fault+Tolerance+for+GPU+Accelerated+AI+Workloads+in+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Enabling Fault Tolerance for GPU Accelerated AI Workloads in Kubernetes - Arpit Singh & Abhijit Paithankar, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Arpit Singh, Abhijit Paithankar, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7qv/enabling-fault-tolerance-for-gpu-accelerated-ai-workloads-in-kubernetes-arpit-singh-abhijit-paithankar-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Enabling+Fault+Tolerance+for+GPU+Accelerated+AI+Workloads+in+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Enabling Fault Tolerance for GPU Accelerated AI Workloads in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qv/enabling-fault-tolerance-for-gpu-accelerated-ai-workloads-in-kubernetes-arpit-singh-abhijit-paithankar-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Enabling+Fault+Tolerance+for+GPU+Accelerated+AI+Workloads+in+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yPkljSjo3qg
- YouTube title: Enabling Fault Tolerance for GPU Accelerated AI Workloads in Kubernetes - A. Singh & A. Paithankar
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/enabling-fault-tolerance-for-gpu-accelerated-ai-workloads-in-kubernete/yPkljSjo3qg.txt
- Transcript chars: 33638
- Keywords: gpu, application, running, cluster, network, monitoring, failures, recovery, training, determine, components, operator, performance, workload, restart, storage, errors, device

### Resumo baseado na transcript

I'm Abit I'm a tech lead manager at Nvidia hey uh this is arit I'm a senior s engineer at Nvidia so by a show of hands how many of you manage GPU plers oh wow and that's a lot and how many gpus or how many nodes in your cluster 10 20 30 5050 100 okay 500 1,000 5,000 10,000 more than 10,000 oh nice nice you in right talk we go all right yeah all right so um in this talk we'll go over uh the motivation for

### Excerpt da transcript

I'm Abit I'm a tech lead manager at Nvidia hey uh this is arit I'm a senior s engineer at Nvidia so by a show of hands how many of you manage GPU plers oh wow and that's a lot and how many gpus or how many nodes in your cluster 10 20 30 5050 100 okay 500 1,000 5,000 10,000 more than 10,000 oh nice nice you in right talk we go all right yeah all right so um in this talk we'll go over uh the motivation for resiliency understanding some of the characteristics of AI workloads we'll see where failures come from uh we'll look into AI infrastructure components and bring up and validation then we'll talk about uh fall tolerance and it building blocks and then the four pillars of fall horns are monitoring propagation recovery and uh remediation and then we'll see where's their scope for enhancement as a community so why do we need fonns in AI workloads inherently AI Hardware is complex here you see the schematic of uh uh djx h100 200 uh system in addition to the typical components in a CPU server like you know the CPU socks dam and vme drives and fans there are a few additional components um these two are the 400 gig ethernet cards that are used to connect to your uh high performance parallel file system like cluster and you have the eight infinity band cards which are connected to the backend Network they connect to the gpus um you know could be h100 200 and then those all the gpus inside a server are connected to each other via the NV switch over a 900 GB GPU to GPU interconnect yeah it's 900 gbes and um the second dimension so on one side we have complex hardware and the second dimension is very large scale um you can imagine a single training job being run at this scale uses up all the nodes in your data center all the gpus all the infinite band connections and everything um here's a topology for a 1,000 GPU uh rail optimized fabric by rail optimized it means you want to minimize the number of collisions that can happen and so it creates a two- layer topology uh at 32k scale again you can you know Drive some of that through a two layer topology but depending on your how your back end is connected could be two or three layers and the scale keeps growing there are already 100K plus GPU clusters in production and 200 and 300K GPU clusters are being built uh when you combine the effect of complex Hardware with scale the combined effect is synergistic so it's compounding rather than additive uh at a scale of course we want to run you know training of billions and tr
