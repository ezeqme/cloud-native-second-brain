---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Runtimes"
themes: ["Runtime Containers", "Kubernetes Core"]
speakers: ["Alexander Jung", "Lancaster University"]
sched_url: https://kccncna2021.sched.com/event/lV2y/deploying-unikernels-in-production-with-kubernetes-alexander-jung-lancaster-university
youtube_search_url: https://www.youtube.com/results?search_query=Deploying+Unikernels+in+Production+with+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Deploying Unikernels in Production with Kubernetes - Alexander Jung, Lancaster University

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Runtimes]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Alexander Jung, Lancaster University
- Schedule: https://kccncna2021.sched.com/event/lV2y/deploying-unikernels-in-production-with-kubernetes-alexander-jung-lancaster-university
- Busca YouTube: https://www.youtube.com/results?search_query=Deploying+Unikernels+in+Production+with+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Deploying Unikernels in Production with Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2y/deploying-unikernels-in-production-with-kubernetes-alexander-jung-lancaster-university
- YouTube search: https://www.youtube.com/results?search_query=Deploying+Unikernels+in+Production+with+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cV-xawN9_cg
- YouTube title: Deploying Unikernels in Production with Kubernetes - Alex Jung, Lancaster University
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/deploying-unikernels-in-production-with-kubernetes/cV-xawN9_cg.txt
- Transcript chars: 25634
- Keywords: kernel, application, container, runtime, virtual, running, machine, kernels, operating, actually, components, performance, instance, containers, unikernel, create, images, platform

### Resumo baseado na transcript

hi everyone my name is alexander young and i'm the cpo at unicraft and i'm also a phd student at lancaster university focusing primarily on lightweight virtualization i'm very honored today to be able to give you a presentation today at kubecon on some of the work we've been cooking up at unicroft this has been an ongoing effort with the university of lancaster university of polytechnic bulcarest and nec labs europe and today's talk it's all about how we can introduce unikernels into the ecosystem but let's start with

### Excerpt da transcript

hi everyone my name is alexander young and i'm the cpo at unicraft and i'm also a phd student at lancaster university focusing primarily on lightweight virtualization i'm very honored today to be able to give you a presentation today at kubecon on some of the work we've been cooking up at unicroft this has been an ongoing effort with the university of lancaster university of polytechnic bulcarest and nec labs europe and today's talk it's all about how we can introduce unikernels into the ecosystem but let's start with our premise achieving higher cluster utilization whilst maintaining performance and security is fundamental to service operators such as infrastructures or service providers or devops engineers who wish to decrease operational expenditure we're actually seeing a lot of great work in this space recently on how to reduce the cost of services running in the cloud however virtualization strategies such as with containers have gained immense popularity thanks to orchestration frameworks such as kubernetes thanks to their ease of use containers and kubernetes have been adopted as the de facto industry standard for deployments of diverse workloads on heterogeneous infrastructure deployments vary from big data web services and edge computing some really awesome stuff and the mix is enabled in vast advancements in scheduling strategies deployment architectures and workload monitoring but let's take a look at what a typical deployment looks like with kubernetes and dive into the full stack to see what's going on you can see here in this figure that what may resemble a typical worker node in a cluster the node is provisioned in a cluster typically as a virtual machine itself running on top of a hypervisor the worker node has a fully functional general purpose operating system and the container runtime engine such as container d which manages a number of name space separated processes for both the system kubernetes services cube system as well as provision services and their actual pods but what's the problem well there are actually four degrees of virtualization and indirection there's of course the hypervisor which is hosting the virtual machine it's keeping the vm safe from other vms in what is probably the most secure way possible the os itself is managing a number of internal system processes along with the container runtime the container runtime is managing the lifecycle and managing the namespaces and isolation of all the services and all the pods
