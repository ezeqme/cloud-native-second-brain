---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Runtimes"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core"]
speakers: ["Kevin Klues", "NVIDIA"]
sched_url: https://kccnceu2021.sched.com/event/iE4n/a-deep-dive-on-supporting-multi-instance-gpus-in-containers-and-kubernetes-kevin-klues-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=A+Deep+Dive+on+Supporting+Multi-Instance+GPUs+in+Containers+and+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# A Deep Dive on Supporting Multi-Instance GPUs in Containers and Kubernetes - Kevin Klues, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Runtimes]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Kevin Klues, NVIDIA
- Schedule: https://kccnceu2021.sched.com/event/iE4n/a-deep-dive-on-supporting-multi-instance-gpus-in-containers-and-kubernetes-kevin-klues-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=A+Deep+Dive+on+Supporting+Multi-Instance+GPUs+in+Containers+and+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre A Deep Dive on Supporting Multi-Instance GPUs in Containers and Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4n/a-deep-dive-on-supporting-multi-instance-gpus-in-containers-and-kubernetes-kevin-klues-nvidia
- YouTube search: https://www.youtube.com/results?search_query=A+Deep+Dive+on+Supporting+Multi-Instance+GPUs+in+Containers+and+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xNY9cbaLuGk
- YouTube title: A Deep Dive on Supporting Multi-Instance GPUs in Containers and Kubernetes - Kevin Klues, NVIDIA
- Match score: 0.966
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/a-deep-dive-on-supporting-multi-instance-gpus-in-containers-and-kubern/xNY9cbaLuGk.txt
- Transcript chars: 27513
- Keywords: gpu, nvidia, device, instance, devices, compute, container, support, single, running, access, command, slices, actually, components, memory, installed, instances

### Resumo baseado na transcript

hello everyone my name is kevin cluse and i'm a principal software engineer at nvidia today i'm going to be talking about the support i built for multi-instance gpus in containers and kubernetes multi-instance gpus or mig for short is a new hardware feature of the latest nvidia ampere gpus so everything i talk about today is specific to this type of gpu before i begin i'd like to remind you that i am available for chat during this talk so as questions come up please feel free to drop

### Excerpt da transcript

hello everyone my name is kevin cluse and i'm a principal software engineer at nvidia today i'm going to be talking about the support i built for multi-instance gpus in containers and kubernetes multi-instance gpus or mig for short is a new hardware feature of the latest nvidia ampere gpus so everything i talk about today is specific to this type of gpu before i begin i'd like to remind you that i am available for chat during this talk so as questions come up please feel free to drop them on slack and i'll make sure to answer them as best i can i imagine if you're at this talk you probably already understand the benefits of supporting gpus and kubernetes so i'm only going to spend a few minutes highlighting some of their more important use cases first and foremost supporting gpus in kubernetes lets us scale up ai training and inference jobs to a cluster of gpu machines using the same underlying infrastructure we use to deploy all of our cpu-based workloads such as web servers databases streaming data servers etc using the tools we've built as a community users are able to take a kubernetes pod spec specify some number of gpus and direct their application to a particular class of gpus that can meet their workload demands a typical gpu cluster then looks something like this where you have a bunch of servers each hosting some number of possibly heterogeneous gpus all being managed under a single kubernetes instance where training jobs tend to require multiple more powerful gpus and inference or development jobs tend to only require a single instance of a less powerful gpu but what if you don't have the luxury of having such a diverse mix of gpus in your cluster or as is often the case you have a small cluster with only the most powerful gpus you can get your hands on and want to be able to efficiently use them for all types of workloads and even if you do have a bunch of nodes at your disposal wouldn't it be better to have your cluster full of the most powerful gpus possible so that you have them when you need them but then have a way of sharing an individual gpu for jobs that only require a fraction of its full power well this is where multi-instance gpus come in it's hardware support for taking a full gpu and dividing it into several smaller what we call gpu instances each of which have their own dedicated set of memory and compute resources additionally each gpu instance gets a dedicated percentage of the overall memory bandwidth and any faults that occur
