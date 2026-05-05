---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Tim Ebert", "STACKIT"]
sched_url: https://kccnceu2025.sched.com/event/1txFG/beyond-the-limits-scaling-kubernetes-controllers-horizontally-tim-ebert-stackit
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Limits%3A+Scaling+Kubernetes+Controllers+Horizontally+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Beyond the Limits: Scaling Kubernetes Controllers Horizontally - Tim Ebert, STACKIT

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Tim Ebert, STACKIT
- Schedule: https://kccnceu2025.sched.com/event/1txFG/beyond-the-limits-scaling-kubernetes-controllers-horizontally-tim-ebert-stackit
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Limits%3A+Scaling+Kubernetes+Controllers+Horizontally+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Beyond the Limits: Scaling Kubernetes Controllers Horizontally.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFG/beyond-the-limits-scaling-kubernetes-controllers-horizontally-tim-ebert-stackit
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Limits%3A+Scaling+Kubernetes+Controllers+Horizontally+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OTzd9eTtLRA
- YouTube title: Beyond the Limits: Scaling Kubernetes Controllers Horizontally - Tim Ebert, STACKIT
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/beyond-the-limits-scaling-kubernetes-controllers-horizontally/OTzd9eTtLRA.txt
- Transcript chars: 22501
- Keywords: controller, objects, instance, controllers, object, website, operator, sharder, another, hosting, create, instances, active, single, leader, running, websites, specific

### Resumo baseado na transcript

This is uh beyond the limits scaling Kubernetes controllers horizontally. I work at STEIT and I'm going to walk you through some crazy Kubernetes controller stuff in the next 30 minutes. Kubernetes controllers are what facilitate the declarative state management in Kubernetes so that you can just apply some YAML and the controller takes care for you to scale the deployment to the desired amount of replicas. So that could be recording a Kubernetes event that you see in cubectl describe but it could also be updating the status section of your object. So let me first introduce it to you and then we can see how we can make it scale. Uh and we want to do this declaratively with Kubernetes because there is simply no better way to host engine X than on Kubernetes, right?

### Excerpt da transcript

This is uh beyond the limits scaling Kubernetes controllers horizontally. My name is Tim Ebot. I work at STEIT and I'm going to walk you through some crazy Kubernetes controller stuff in the next 30 minutes. But before we start with an introduction, let's get a quick raise of hands. Who has ever used a Kubernetes operator in their classes before? Oh, wow. That's that's many. Let's say 70% of the audience. Okay, let's get another raise of hands. Who has ever implemented an own custom controller or Kubernetes operator? Wow, I didn't expect that. Almost 60% of the audience. That's great. Um, so let me tell you why this topic is so interesting to me. I work at the stick kubernetes engine team and we are running thousands of kubernetes clusters for our customers. This is based on open-source project gardener. Without it, that wouldn't be possible. So, shout out to the gardener folks in the audience and out there. Gardner uses controllers for managing the Kubernetes clusters, meaning the control planes and the worker nodes.

So you could say my day job is about running Kubernetes controllers at scale. And that's why I decided to put some effort into this topic in my master's thesis which was called horizontally scalable Kubernetes controllers. And this is what I'm going to talk to you about today. Let's review some controller basics so that we are all on the same page. Kubernetes controllers are what facilitate the declarative state management in Kubernetes so that you can just apply some YAML and the controller takes care for you to scale the deployment to the desired amount of replicas. Right? So for this controllers perform these typical steps. First of all they watch the API objects at the API server for changes. Then when receiving change events like watch events, they cache these objects in memory for fast retrieval. If there are any relevant changes, they will encue the object for later reconciliation. When they reconciled the objects, the first thing is they read the object from the cache from memory ideally to not put load on the API server and if necessary they perform the changes like creating new pots and so on and typically the last step is to report the observed status.

So that could be recording a Kubernetes event that you see in cubectl describe but it could also be updating the status section of your object. Okay, let's illustrate this. I've brought an example operator which I'm going to use throughout this talk. So let me first introduce it to
