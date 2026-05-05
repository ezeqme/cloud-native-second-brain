---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Operations"
themes: ["Kubernetes Core"]
speakers: ["Matt Schallert", "Chronosphere", "Dominik Tornow", "Temporal"]
sched_url: https://kccncna2021.sched.com/event/lV5d/declarative-and-imperative-kubernetes-operations-with-temporal-and-m3-matt-schallert-chronosphere-dominik-tornow-temporal
youtube_search_url: https://www.youtube.com/results?search_query=Declarative+and+Imperative+Kubernetes+Operations+with+Temporal+and+M3+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Declarative and Imperative Kubernetes Operations with Temporal and M3 - Matt Schallert, Chronosphere & Dominik Tornow, Temporal

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Operations]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Matt Schallert, Chronosphere, Dominik Tornow, Temporal
- Schedule: https://kccncna2021.sched.com/event/lV5d/declarative-and-imperative-kubernetes-operations-with-temporal-and-m3-matt-schallert-chronosphere-dominik-tornow-temporal
- Busca YouTube: https://www.youtube.com/results?search_query=Declarative+and+Imperative+Kubernetes+Operations+with+Temporal+and+M3+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Declarative and Imperative Kubernetes Operations with Temporal and M3.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5d/declarative-and-imperative-kubernetes-operations-with-temporal-and-m3-matt-schallert-chronosphere-dominik-tornow-temporal
- YouTube search: https://www.youtube.com/results?search_query=Declarative+and+Imperative+Kubernetes+Operations+with+Temporal+and+M3+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8OCDPDGA_C0
- YouTube title: Declarative & Imperative Kubernetes Operations with Temporal & M3 - Matt Schallert & Dominik Tornow
- Match score: 0.842
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/declarative-and-imperative-kubernetes-operations-with-temporal-and-m3/8OCDPDGA_C0.txt
- Transcript chars: 16647
- Keywords: workflow, temporal, stateful, control, controller, deploy, actually, operator, controllers, deployment, resources, replica, custom, reconciliation, execution, cluster, workflows, platform

### Resumo baseado na transcript

all right thank you very much well we will uh jump right into it and we will start this presentation with a question that is almost as old as time itself what is kubernetes now let's jump down this rabbit hole we have two lovely tour guides rabbit number one that is matt senior engineer at chronosphere and then rabbit number two that is this guy dominic principal engineer at tempura so i would argue the answer to the question what is kubernetes we have at least as many answers

### Excerpt da transcript

all right thank you very much well we will uh jump right into it and we will start this presentation with a question that is almost as old as time itself what is kubernetes now let's jump down this rabbit hole we have two lovely tour guides rabbit number one that is matt senior engineer at chronosphere and then rabbit number two that is this guy dominic principal engineer at tempura so i would argue the answer to the question what is kubernetes we have at least as many answers as there are people in the room and probably also online but let me give it a shot so i would argue kubernetes may be characterized as a container orchestration platform that is a very agreeable definition however it should give us some pause because kubernetes does do more than just orchestrate containers there is at least networking and storage involved as well so let's broaden this definition a little bit and let's say kubernetes may be characterized as an infrastructure orchestration platform but again the defining characteristic of infrastructure orchestration is operation automation so i would say we may safely arrive at the conclusion that kubernetes can be characterized as an operation automation platform kubernetes implements operation automation with the help of kubernetes controller and kubernetes resources there are two types of controllers and there are two types of resources there are core controllers and core resources provided by kubernetes itself and then there are custom controllers and custom resources basically provided by anybody else so custom controllers are creatively named operators and custom resources are self-explanatory named custom resources so we let the historians decide which naming scheme is better and we focus on more important questions what do controllers do and how do controllers work well controllers perform reconciliation the very core of operation automation controllers transition your system from its current state to its desired state and for that a controller performs two distinct tasks first detection of state drift detection of state drift is the determination that the current state differs from the desired state and second mitigation mitigation of state drift that is the determination and the execution of a sequence of steps a sequence of actions that transition the system from its current state to its desired state now a kubernetes controller performs reconciliation continuously in a what we call a control loop we determine the current s
