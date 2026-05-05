---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Keynote Sessions"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Kevin Klues", "Distinguished Engineer", "Sanjay Chatterjee", "Engineering Manager", "NVIDIA"]
sched_url: https://kccnceu2024.sched.com/event/1YhI5/keynote-accelerating-ai-workloads-with-gpus-in-kubernetes-kevin-klues-distinguished-engineer-sanjay-chatterjee-engineering-manager-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Accelerating+AI+Workloads+with+GPUs+in+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keynote: Accelerating AI Workloads with GPUs in Kubernetes - Kevin Klues, Distinguished Engineer & Sanjay Chatterjee, Engineering Manager, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Kevin Klues, Distinguished Engineer, Sanjay Chatterjee, Engineering Manager, NVIDIA
- Schedule: https://kccnceu2024.sched.com/event/1YhI5/keynote-accelerating-ai-workloads-with-gpus-in-kubernetes-kevin-klues-distinguished-engineer-sanjay-chatterjee-engineering-manager-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Accelerating+AI+Workloads+with+GPUs+in+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keynote: Accelerating AI Workloads with GPUs in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhI5/keynote-accelerating-ai-workloads-with-gpus-in-kubernetes-kevin-klues-distinguished-engineer-sanjay-chatterjee-engineering-manager-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Accelerating+AI+Workloads+with+GPUs+in+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gn5SZWyaZ34
- YouTube title: Keynote: Accelerating AI Workloads with GPUs in Kubernetes - Kevin Klues & Sanjay Chatterjee
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keynote-accelerating-ai-workloads-with-gpus-in-kubernetes/gn5SZWyaZ34.txt
- Transcript chars: 12117
- Keywords: gpu, workloads, support, resources, topology, nvidia, cluster, placement, scheduling, components, application, training, provides, sharing, challenges, encourage, choose, access

### Resumo baseado na transcript

hey everyone welcome to ccon my name is Kevin Clues and this is my colleague sanj chaty and today we're going to be talking about accelerating AI workloads with gpus in kubernetes so let's Dive Right In we are in the midst of the next Industrial Revolution from self-driving cars to real-time Health monitoring and smart cities AI is powering it all and at the heart of this revolution are gpus and the platform that provides applications access to them for many kubernetes has already become this platform but we

### Excerpt da transcript

hey everyone welcome to ccon my name is Kevin Clues and this is my colleague sanj chaty and today we're going to be talking about accelerating AI workloads with gpus in kubernetes so let's Dive Right In we are in the midst of the next Industrial Revolution from self-driving cars to real-time Health monitoring and smart cities AI is powering it all and at the heart of this revolution are gpus and the platform that provides applications access to them for many kubernetes has already become this platform but we still have a lot of work to do before we can unlock the full potential of gpus to accelerate AI workloads on kubernetes this includes changes to both the low-level mechanisms used to request access to gpus as well as the higher level processes needed to map a set of gpus to a workload based on its requests where the biggest change in terms of resource management will be direct support for nonf funable and non-exclusive resources at the node level and the changes at the higher layers will take the form of things like topology aware placement strategies and advanced multi-dimensional scheduling so to kick things off I'm going to start with a brief overview of what it takes to enable GPU support in kubernetes today I'll then jump into the details of one very specific use case that could benefit from non-fungible and non-exclusive of resources namely GPU sharing I'll then introduce a new feature called Dynamic resource allocation or Dr for short which we see as the enabler for taking GPU support and kubernetes to the next level finally I'll hand things over to Sanjay who will walk us through some of the challenges with scaling out gpus on kubernetes so what does it take to actually enable GPU support in kubernetes today well it takes a mix of host level components such as the Nvidia container toolkit and the underlying Nvidia GPU driver as well as a set of kubernetes specific components such as the cad device plugin GPU feature Discovery and the Nvidia Mig manager with these in place one can make requests like the one seen on the right to inject GPU support into their workloads as well as direct those workloads to a particular type of GPU using a node selector if desired to ease the deployment of all these components Nvidia provides a GPU operator which I'm not going to go into the details of today but I encourage you to uh to watch the following talks later this week um to learn more one tomorrow at 3:25 p.m.

and one on Friday at 11:00 a.m. for history l
