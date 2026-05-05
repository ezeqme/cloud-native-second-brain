---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Yuan Tang", "Red Hat", "Eduardo Arango Gutierrez", "NVIDIA"]
sched_url: https://kccnceu2025.sched.com/event/1tcx7/advancements-in-aiml-inference-workloads-on-kubernetes-from-wg-serving-and-ecosystem-projects-yuan-tang-red-hat-eduardo-arango-gutierrez-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Advancements+in+AI%2FML+Inference+Workloads+on+Kubernetes+From+WG+Serving+and+Ecosystem+Projects+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Advancements in AI/ML Inference Workloads on Kubernetes From WG Serving and Ecosystem Projects - Yuan Tang, Red Hat & Eduardo Arango Gutierrez, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Yuan Tang, Red Hat, Eduardo Arango Gutierrez, NVIDIA
- Schedule: https://kccnceu2025.sched.com/event/1tcx7/advancements-in-aiml-inference-workloads-on-kubernetes-from-wg-serving-and-ecosystem-projects-yuan-tang-red-hat-eduardo-arango-gutierrez-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Advancements+in+AI%2FML+Inference+Workloads+on+Kubernetes+From+WG+Serving+and+Ecosystem+Projects+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Advancements in AI/ML Inference Workloads on Kubernetes From WG Serving and Ecosystem Projects.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcx7/advancements-in-aiml-inference-workloads-on-kubernetes-from-wg-serving-and-ecosystem-projects-yuan-tang-red-hat-eduardo-arango-gutierrez-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Advancements+in+AI%2FML+Inference+Workloads+on+Kubernetes+From+WG+Serving+and+Ecosystem+Projects+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=G8U141NkrDI
- YouTube title: Advancements in AI/ML Inference Workloads on Kubernetes From... Yuan Tang & Eduardo Arango Gutierrez
- Match score: 0.821
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/advancements-in-ai-ml-inference-workloads-on-kubernetes-from-wg-servin/G8U141NkrDI.txt
- Transcript chars: 26092
- Keywords: working, inference, serving, everyone, basically, projects, workloads, report, meetings, better, trying, running, autoscaling, multiple, support, stream, metrics, mentioned

### Resumo baseado na transcript

So uh we hope this is going to be rather a short talk and just an introduction for those that doesn't know the working group exist and hopefully we will get question for you mostly on like if you require new features or you if you have any pain points that you would like the working group to work on. I'm one of the co-chairs for working group serving and also a project lead for Argo and Coupflow and also maintain a couple of projects. there are some gaps in Kubernetes and during one of the unconference sessions at the at that time contributor summit now maintainer summit the name changings that we're going on uh we decided we needed two working groups so last year the working group device Uh one goal is to enhance Kubernetes controllers meaning we are proposing APIs we are proposing uh changes to main Kubernetes controllers and also low-level components as we are going to talk about things like DRA. So we can make it easier for everyone to run uh sering workloads on Kubernetes. So we can really understand what is happening when we run uh these large language models because uh last year when we started the working group serin we had a couple of very long meetings discussing what should we monitor when knowing how to autoscale

### Excerpt da transcript

Hi everyone. Uh welcome to this uh CubeCon talk. This is going to be a working group update. So uh we hope this is going to be rather a short talk and just an introduction for those that doesn't know the working group exist and hopefully we will get question for you mostly on like if you require new features or you if you have any pain points that you would like the working group to work on. So uh for starters uh who are we? Hi everyone. Uh thank you for being here. My name is Yan. I'm a senior principal software engineer at Red Hat. Uh working on our hybrid cloud AI platform. I'm one of the co-chairs for working group serving and also a project lead for Argo and Coupflow and also maintain a couple of projects. Uh one of the most active project we are working on is a llama stack project. So feel free to take a look at the project if you are interested. and I also uh authored a couple of books in case you are interested in reading as well. Yeah, thank you Joan and uh myself uh Eduardo Arango also a working group chair for the working group Serbin and I've been working in distributed uh systems using containers for a long time now and um I work mostly on the low-level container runtime bits and now I'm working on projects related to CDI and the array which are also of big importance for working group serving which we will talk in a Right.

So what is working group serbing? So uh actually just a minute ago I was thinking that we forgot one slide and is uh is one year now. So working group serbing was born in uh CubeCon Europe last year Paris and it basically was born out of the necessity where everyone wanted to uh collaborate on Serbian projects and Serbian needs for Kubernetes. there are some gaps in Kubernetes and during one of the unconference sessions at the at that time contributor summit now maintainer summit the name changings that we're going on uh we decided we needed two working groups so last year the working group device management and working group serving uh was born and now it's a full one year of the working group serving so we forgot the uh one year celebration is slide yeah but yeah happy birthday to working group serving So the working group observing is basically uh it has three main goals. Uh one goal is to enhance Kubernetes controllers meaning we are proposing APIs we are proposing uh changes to main Kubernetes controllers and also low-level components as we are going to talk about things like DRA.

So we can make it easier for everyon
