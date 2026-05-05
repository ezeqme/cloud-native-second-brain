---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Aya Ozawa", "CloudNatix Inc.", "Kohei Ota", "Apple"]
sched_url: https://kccnceu2024.sched.com/event/1YePO/to-infinity-and-beyond-seamless-autoscaling-with-in-place-resource-resize-for-kubernetes-pods-aya-ozawa-cloudnatix-inc-kohei-ota-apple
youtube_search_url: https://www.youtube.com/results?search_query=To+Infinity+and+Beyond%3A+Seamless+Autoscaling+with+in-Place+Resource+Resize+for+Kubernetes+Pods+CNCF+KubeCon+2024
slides: []
status: parsed
---

# To Infinity and Beyond: Seamless Autoscaling with in-Place Resource Resize for Kubernetes Pods - Aya Ozawa, CloudNatix Inc. & Kohei Ota, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Aya Ozawa, CloudNatix Inc., Kohei Ota, Apple
- Schedule: https://kccnceu2024.sched.com/event/1YePO/to-infinity-and-beyond-seamless-autoscaling-with-in-place-resource-resize-for-kubernetes-pods-aya-ozawa-cloudnatix-inc-kohei-ota-apple
- Busca YouTube: https://www.youtube.com/results?search_query=To+Infinity+and+Beyond%3A+Seamless+Autoscaling+with+in-Place+Resource+Resize+for+Kubernetes+Pods+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre To Infinity and Beyond: Seamless Autoscaling with in-Place Resource Resize for Kubernetes Pods.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePO/to-infinity-and-beyond-seamless-autoscaling-with-in-place-resource-resize-for-kubernetes-pods-aya-ozawa-cloudnatix-inc-kohei-ota-apple
- YouTube search: https://www.youtube.com/results?search_query=To+Infinity+and+Beyond%3A+Seamless+Autoscaling+with+in-Place+Resource+Resize+for+Kubernetes+Pods+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9lKa8bWU9II
- YouTube title: To Infinity and Beyond: Seamless Autoscaling with in-Place Resource Resize for Kubernetes Pods
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/to-infinity-and-beyond-seamless-autoscaling-with-in-place-resource-res/9lKa8bWU9II.txt
- Transcript chars: 22851
- Keywords: resource, request, feature, memory, container, resources, actually, change, restart, question, called, happens, recreate, number, management, resour, diagram, recommendation

### Resumo baseado na transcript

K uh we came from Japan and today we are going to talk about the uh new Alpha feature called um in place resources sites uh so among the attendees uh have you ever heard about this feature okay good number so over half of the people will learn about what it is um yeah let me start with self introduction my name is co and I work at Apple as a CIF field engineer and I work on open source and um yeah um my focus right now is

### Excerpt da transcript

K uh we came from Japan and today we are going to talk about the uh new Alpha feature called um in place resources sites uh so among the attendees uh have you ever heard about this feature okay good number so over half of the people will learn about what it is um yeah let me start with self introduction my name is co and I work at Apple as a CIF field engineer and I work on open source and um yeah um my focus right now is a cloud native Technologies hi I'm aawa I'm working at CL natics and working on ph Ops to like Auto scatterer and automate kubernetes operations thanks so how do we set the right po race resource resource management is key to smove the sing of maintaining kubernetes clusters both resource can be configured using request and limit request means minimum resource requirement and limit Capa resour it seems like to simple Fields but there are lots of complexity and the food to maintaining KU Crosser effectively it's important for us to understand them this is a rough diagram of pot creation we'll look into the detail later so you don't need to understand everything here but as you can see resource request and limit are used in several components like schedule check request and cubert combat request and limit to container settings and then one time set them to The Container now let's dive into what happens when we set these values at first let's think about scheduling scheduler uses resource request to check if the part fits the node as the left diagram shows if the poort request satisfy the available resource the scheduler assigns the to the node on the other hand the schuer does not con resource limit and actual usage but actually pot can use resource up to the limit so CPU and memory can be overcommitted as shown in the right diagram pot is allocated regardless of its resource limits next let's explore what happens when a running container hits a limit as you can see from the left diagram if a container goes over its memory limits it's cured by the O killer as for CPU you know it's a Time stress resource if a container exceed its limit it will be throttled and the Cod period ends of course it allows to resume in next quarter period but this DeRay leads to a performance delegation keep in mind reses can be committed this means if other container on the same node have already used up node resource your container run into the same station even before reaching its own limit now let's consider results of entire node if a node runs out of memory t
