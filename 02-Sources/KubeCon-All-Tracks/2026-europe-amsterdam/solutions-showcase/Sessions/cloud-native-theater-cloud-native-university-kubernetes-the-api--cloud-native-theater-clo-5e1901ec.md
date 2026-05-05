---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Kubernetes Core"]
speakers: ["Tibo Beijen", "DPG Media Nederland"]
sched_url: https://kccnceu2026.sched.com/event/2EG0D/cloud-native-theater-cloud-native-university-kubernetes-the-api-of-everything-tibo-beijen-dpg-media-nederland
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Kubernetes%3A+The+API+of+Everything+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Cloud Native University: Kubernetes: The API of Everything - Tibo Beijen, DPG Media Nederland

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tibo Beijen, DPG Media Nederland
- Schedule: https://kccnceu2026.sched.com/event/2EG0D/cloud-native-theater-cloud-native-university-kubernetes-the-api-of-everything-tibo-beijen-dpg-media-nederland
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Kubernetes%3A+The+API+of+Everything+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Cloud Native University: Kubernetes: The API of Everything.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0D/cloud-native-theater-cloud-native-university-kubernetes-the-api-of-everything-tibo-beijen-dpg-media-nederland
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Kubernetes%3A+The+API+of+Everything+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kJCvn4LR5lM
- YouTube title: Cloud Native Theater | Cloud Native University: Kubernetes: The API of Everything - Tibo Beijen
- Match score: 1.008
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-cloud-native-university-kubernetes-the-api-of-eve/kJCvn4LR5lM.txt
- Transcript chars: 5755
- Keywords: controllers, controller, status, cluster, pattern, container, built-in, extend, everything, actually, containers, happens, basically, desired, deployment, replica, extending, conference

### Resumo baseado na transcript

It's called DPG Media, big uh media company in the Netherlands and Belgium. Uh, and I'm going to, you know, talk you a bit through Kubernetes from an API perspective. thing let's look at that custom resource definition on the left side you see uh a built-in Kubernetes deployment spec status extending the API in this case GDA sort of autoscaler on steroids. And it repeats and it repeats crossplane infrastructure everywhere but driven from your Kubernet Kubernetes cluster. So Kubernetes is not just about managing stuff inside Kubernetes but can also manage stuff outside of Kubernetes. So it's not just something you install on servers to run containers which happens to have an API but instead think of Kubernetes as an API that can be extended.

### Excerpt da transcript

Yeah, welcome. Uh, I'm Tibayian. Um, I work with Kubernetes for I think about eight years. Yeah, something like that. And doing text things way longer than that. Um, and I work for a media company. It's called DPG Media, big uh media company in the Netherlands and Belgium. So, you might know it if you're from around here. HLN DL Noodle L and also quite important Donald Duck. So yeah, that's also what we do. Uh, and I'm going to, you know, talk you a bit through Kubernetes from an API perspective. So you might think of Kubernetes as a container orchestrator, and that's true. It is a container orchestrator, but I'm going to, you know, change that perspective a little bit and help you around for the next coming couple of days. Uh, because it's way more than that. because it's actually at least in my opinion an API and not an API which is designed to orchestrate things and those things that include containers obviously but way more than that. So let's dive in. An API by itself is mostly about exchanging data, storing stuff, retrieving it.

Uh but then not a lot happens. So the API has machinery and in Kubernetes we call it controllers. Controllers are the brains that do things. Uh and here you see little example built-in controller that yeah controls and manages it manages stuff and what it does it takes those specifications that you might be familiar with uh you know all those YML you keep shoving into your cluster and that basically that has a desired state uh and you know an actual state which the controller will try to make happen. Uh and basically in every YAML you see that in the form of the spec what you desire and the status status that's reported back like hey did we succeed in accomplishing that desired state that's a machinery and one single machine doesn't operate in itself there's many of them and together you get orchestration so if we take that example of um the deployment that we just saw then there's a lot of things happening under the hood. There's the deployment controller and that spawns replicas. Those replica sets are picked up by the replica set controller.

Replica set controller says, "Oh, I need to run a bunch of pots and you get ports in your API landscape. Uh those ports get actually picked up by theuler that says, "Oh, you can put it on this or that node." And then the cubelet also a sort of controller on the node that says, "Who me? I got to run this container and then well it makes the container runtime work and it reports the st
