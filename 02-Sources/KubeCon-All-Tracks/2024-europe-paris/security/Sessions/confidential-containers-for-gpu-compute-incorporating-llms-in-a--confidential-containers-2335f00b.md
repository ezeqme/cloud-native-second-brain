---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Zvonko Kaiser", "NVIDIA"]
sched_url: https://kccnceu2024.sched.com/event/1YePm/confidential-containers-for-gpu-compute-incorporating-llms-in-a-lift-and-shift-strategy-for-ai-zvonko-kaiser-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Confidential+Containers+for+GPU+Compute%3A+Incorporating+LLMs+in+a+Lift-and-Shift+Strategy+for+AI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Confidential Containers for GPU Compute: Incorporating LLMs in a Lift-and-Shift Strategy for AI - Zvonko Kaiser, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: France / Paris
- Speakers: Zvonko Kaiser, NVIDIA
- Schedule: https://kccnceu2024.sched.com/event/1YePm/confidential-containers-for-gpu-compute-incorporating-llms-in-a-lift-and-shift-strategy-for-ai-zvonko-kaiser-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Confidential+Containers+for+GPU+Compute%3A+Incorporating+LLMs+in+a+Lift-and-Shift+Strategy+for+AI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Confidential Containers for GPU Compute: Incorporating LLMs in a Lift-and-Shift Strategy for AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePm/confidential-containers-for-gpu-compute-incorporating-llms-in-a-lift-and-shift-strategy-for-ai-zvonko-kaiser-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Confidential+Containers+for+GPU+Compute%3A+Incorporating+LLMs+in+a+Lift-and-Shift+Strategy+for+AI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=a3HzBmPuw5g
- YouTube title: Confidential Containers for GPU Compute: Incorporating LLMs in a Lift-and-Shift Strategy for AI
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/confidential-containers-for-gpu-compute-incorporating-llms-in-a-lift-a/a3HzBmPuw5g.txt
- Transcript chars: 26089
- Keywords: gpu, confidential, container, containers, running, runtime, environments, environment, enable, topology, architecture, sandbox, computing, enablement, kernel, meaning, features, essentially

### Resumo baseado na transcript

so H hello everyone my name is Zano Kaiser I'm from Nvidia I'm with the cloud native team um my current main responsibilities are working on Kata and confidential containers and um in this talk I I just want to give you also some history about sandbox environments um what we've done in the Kata space to enable our use cases um and how we can apply all those features that we added uh to Reg llms but also to any AI ml pipeline um agenda is talking about how

### Excerpt da transcript

so H hello everyone my name is Zano Kaiser I'm from Nvidia I'm with the cloud native team um my current main responsibilities are working on Kata and confidential containers and um in this talk I I just want to give you also some history about sandbox environments um what we've done in the Kata space to enable our use cases um and how we can apply all those features that we added uh to Reg llms but also to any AI ml pipeline um agenda is talking about how we came to confidential Computing um why we have chosen Kata as the main driver for enabling sandbox environments with the GPU um a little bit explanation about our GPU enablement stack because it's uh important for our lift and shift strategy where we said we don't want to have any code modification to run our GPU workloads on Kata or on confidential container um we added also a virtualization reference architecture to support Advanced use cases like GPU direct GDs or RDMA in virtualized sandbox environments um a small stop on confidential containers and then I'm going to talk a little bit about confidential Rec llms um but let me first set a stage why why are we even doing this right um if you're looking at a container that's just a process with namespace separation and and cgroup Resource Management um containers share the host kernel meaning if I have a container breakout it can take over the complete note it can take over the complete cluster um it's just a modern way of packaging and sharing and deploying uh applications it's a user space abstraction only and um the red part shows what we are most concerned about it's the weak security boundary between a container runtime and the host operating system we have things like selinux and armor uh to fortify it um but we don't have any H isolation and we are highly dependent on on the Kernel and what we are mostly worried about is that host changes may break our container stack because we are um deploying drivers and other components that we need to enable the GPU um as I said before container escapes take over a hold note um and we need to trust the container imges um and the manifests that we are pulling in into into our cluster in the past there were some techniques that were people are looking into to create sandbox environments um way back there were unic kernels unic kernels is a way to package uh parts of the kernel and parts of your user space into one binary without a memory protection unit so you have fast po times small etic surfaces and and a
