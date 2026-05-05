---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Amit Kumar", "Gaurav Kumar", "Uber"]
sched_url: https://kccnceu2024.sched.com/event/1YeQx/precision-matters-scheduling-gpu-workloads-on-kubernetes-amit-kumar-gaurav-kumar-uber
youtube_search_url: https://www.youtube.com/results?search_query=Precision+Matters%3A+Scheduling+GPU+Workloads+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Precision Matters: Scheduling GPU Workloads on Kubernetes - Amit Kumar & Gaurav Kumar, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Amit Kumar, Gaurav Kumar, Uber
- Schedule: https://kccnceu2024.sched.com/event/1YeQx/precision-matters-scheduling-gpu-workloads-on-kubernetes-amit-kumar-gaurav-kumar-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Precision+Matters%3A+Scheduling+GPU+Workloads+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Precision Matters: Scheduling GPU Workloads on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQx/precision-matters-scheduling-gpu-workloads-on-kubernetes-amit-kumar-gaurav-kumar-uber
- YouTube search: https://www.youtube.com/results?search_query=Precision+Matters%3A+Scheduling+GPU+Workloads+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9A1mU-EbXrE
- YouTube title: Precision Matters: Scheduling GPU Workloads on Kubernetes - Amit Kumar & Gaurav Kumar, Uber
- Match score: 0.874
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/precision-matters-scheduling-gpu-workloads-on-kubernetes/9A1mU-EbXrE.txt
- Transcript chars: 26100
- Keywords: gpu, workloads, cluster, plugin, clusters, federation, filter, resources, particular, device, container, utilization, nvidia, plug-in, multiple, admission, scheduling, support

### Resumo baseado na transcript

hello everyone my name is gorov Kumar I work for the Uber's compute platform team in Amsterdam uh unfortunately my colleague Amit uh couldn't be here today due to logistical reasons so I'll be leading this session solo uh in my roles and responsibilities at compute platform we are mostly focused on uh running different kinds of workloads and uh in this particular talk I'll be talking about uh scheduling GPU workloads on kubernetes and the kind of insights that we have had so far while scheduling such workloads so

### Excerpt da transcript

hello everyone my name is gorov Kumar I work for the Uber's compute platform team in Amsterdam uh unfortunately my colleague Amit uh couldn't be here today due to logistical reasons so I'll be leading this session solo uh in my roles and responsibilities at compute platform we are mostly focused on uh running different kinds of workloads and uh in this particular talk I'll be talking about uh scheduling GPU workloads on kubernetes and the kind of insights that we have had so far while scheduling such workloads so yeah let's get started uh as the outline of the talk I just want to clarify what this talk is not about so this talk is not about how to set up GPU workloads uh uh at the beginning so basically uh I'll not talk about how to set up your clusters to run GPU workloads rather once you've set your clusters up what sort of challenges and uh requirements that you face along the way I would go through a brief overview of how compute works at Uber and uh I'll give an overview of kubernetes clusters for gpus at Uber uh after that I'll covered the sections about efficiency and precision what are the goals and the challenges and the solutions uh that we implemented to achieve achieve uh these uh efficiency and precision targets I'll also cover a little bit about benefits for scheduling uh efficiently and precisely on the kubernetes Clusters we'll covers some common pitfalls that we encountered along the way uh to enable such GPU workloads I'll briefly touch on future work that we have in the plans and if we have times uh we'll cover like a short Q&A session as well this is the overview of compute at Uber at the top we have two Federation layers uh we have a stateless Federation layer and a badge Federation layers these Federation layers manage uh resources efficiently and uh they they are responsible for different types of workloads so for stateless we have a federation layer known as up for batch we have our own Federation layer known as batch federator I would recommend everyone to see the talk on batch Federation on cubec con uh 2023 North America which uh in which my colleagues talked about the batch Federation layer our uh compute platform has been con uh consistently evolving throughout uh we were based on uh msos and our in-house scheduler known as as uh pelaton and over the year we have transitioned to kubernetes below the stack we have our presence across multiple Cloud providers such as oci and gcp and we have our on Prem data centers as well where
