---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Tommy Li", "IBM"]
sched_url: https://kccncna2023.sched.com/event/1R2v9/the-complexity-on-scaling-ml-pipelines-on-kubernetes-using-tekton-tommy-li-ibm
youtube_search_url: https://www.youtube.com/results?search_query=The+Complexity+on+Scaling+ML+Pipelines+on+Kubernetes+Using+Tekton+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Complexity on Scaling ML Pipelines on Kubernetes Using Tekton - Tommy Li, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Tommy Li, IBM
- Schedule: https://kccncna2023.sched.com/event/1R2v9/the-complexity-on-scaling-ml-pipelines-on-kubernetes-using-tekton-tommy-li-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=The+Complexity+on+Scaling+ML+Pipelines+on+Kubernetes+Using+Tekton+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Complexity on Scaling ML Pipelines on Kubernetes Using Tekton.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2v9/the-complexity-on-scaling-ml-pipelines-on-kubernetes-using-tekton-tommy-li-ibm
- YouTube search: https://www.youtube.com/results?search_query=The+Complexity+on+Scaling+ML+Pipelines+on+Kubernetes+Using+Tekton+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ecx-yp4g7YU
- YouTube title: The Complexity on Scaling ML Pipelines on Kubernetes Using Tekton - Tommy Li, IBM
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-complexity-on-scaling-ml-pipelines-on-kubernetes-using-tekton/ecx-yp4g7YU.txt
- Transcript chars: 28254
- Keywords: actually, pipeline, pipelines, itself, controller, create, driver, publisher, execution, custom, multiple, parameter, reduce, produce, tecton, common, caching, python

### Resumo baseado na transcript

hello everyone I'm Tommy thank you for joining these sessions I'm the senior software developer at IBM working in the open technology teams and today we're going uh to go over the complexity on scaling Mii pipelines on C using tons so to begin with let's talk about what is ton pipelines so ton pipelines is a project that provides CID style resource for declaring cicd style pipelines and it's mainly you know construct with you know few main crds namely task pipeline task run pipeline run and custom runs

### Excerpt da transcript

hello everyone I'm Tommy thank you for joining these sessions I'm the senior software developer at IBM working in the open technology teams and today we're going uh to go over the complexity on scaling Mii pipelines on C using tons so to begin with let's talk about what is ton pipelines so ton pipelines is a project that provides CID style resource for declaring cicd style pipelines and it's mainly you know construct with you know few main crds namely task pipeline task run pipeline run and custom runs um these are three you know major CD that we use within P ton pipelines um for example the pipeline run it defines the execution of the pipeline itself that compos multiple tasks a task run that defines the execution of a task which is a a set of build steps and also we also have a custom runs that allows you to instantiate and execute Uh custom task which is able to implement with you know uh any custom Cass controller which you could Define your own um task Logics and why want to use ton pipeline to build our ml infrastructure well the main reason is that like we are need to build our ml infrastructure on top of open shift and open shift container platform is the industry leaders uh is the industry leading Enterprise ku8 platform which it brings out the box of many featur for developer including CICS uh and the cicd for open ship um platform is open ship pipelines and open ship pipeline is based onch te ton project which offers native Integrations with the open share platforms and provides smooth experience for the developers and out of the box uh open shift peline also certified by red hat for open shift and also have Enterprise version a available on open shift as well and that's why we have this is the main reason want to run you know secure pipelines for ML and AI on open shift and this is the option we have chosen and when we actually look into what techn have out the box we see a lot of the good things so techon will able to help us run anable floats a to construct and create new parts for each of the task that us have defined able to have like condition that um uh able to skip task when the condition you know is not match and able to pass PR very easily so any of the inputs and output can be passed in between multiple parts and it has like um API to connect you know custom controller so you want to have your custom Logic for your task you could also do that and were able to optimize you know workflow workflow very easily on the controller levels and
