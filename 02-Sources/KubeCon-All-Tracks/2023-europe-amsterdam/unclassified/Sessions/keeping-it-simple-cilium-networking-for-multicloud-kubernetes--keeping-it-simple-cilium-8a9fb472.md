---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Liz Rice", "Isovalent"]
sched_url: https://kccnceu2023.sched.com/event/1Hyaz/keeping-it-simple-cilium-networking-for-multicloud-kubernetes-liz-rice-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Keeping+It+Simple%3A+Cilium+Networking+for+Multicloud+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keeping It Simple: Cilium Networking for Multicloud Kubernetes - Liz Rice, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Liz Rice, Isovalent
- Schedule: https://kccnceu2023.sched.com/event/1Hyaz/keeping-it-simple-cilium-networking-for-multicloud-kubernetes-liz-rice-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Keeping+It+Simple%3A+Cilium+Networking+for+Multicloud+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keeping It Simple: Cilium Networking for Multicloud Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyaz/keeping-it-simple-cilium-networking-for-multicloud-kubernetes-liz-rice-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Keeping+It+Simple%3A+Cilium+Networking+for+Multicloud+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fJiuqRY5Oi4
- YouTube title: Keeping It Simple: Cilium Networking for Multicloud Kubernetes - Liz Rice, Isovalent
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keeping-it-simple-cilium-networking-for-multicloud-kubernetes/fJiuqRY5Oi4.txt
- Transcript chars: 22597
- Keywords: cluster, psyllium, endpoints, resistance, address, mesh, workloads, external, clusters, network, jackie, actually, endpoint, running, connect, directly, workload, inside

### Resumo baseado na transcript

all right I think it's about time to get started thank you everyone so much for coming to the very last session of what I think has been an amazing week because everybody had a great week yeah glad to hear it so you have come to a session about psyllium networking uh was anybody at psylliumcon on Tuesday quite a few hands excellence and uh while you were at that you might have heard us talking about psyllium mesh yes we have lots of meshes so hopefully what I'm and then that gets load balanced or that request gets load balanced to one of those pod endpoints and the fundamental thing in kubernetes I probably haven't shown you anything new there psyllium knows about those services and it knows about those endpoints so I the demo Gods weren't smiling on us so we basically just got a service with an IP address and that IP address corresponds to an entering the service list in fact we could just look at that let's just make sure let's get the silly

### Excerpt da transcript

all right I think it's about time to get started thank you everyone so much for coming to the very last session of what I think has been an amazing week because everybody had a great week yeah glad to hear it so you have come to a session about psyllium networking uh was anybody at psylliumcon on Tuesday quite a few hands excellence and uh while you were at that you might have heard us talking about psyllium mesh yes we have lots of meshes so hopefully what I'm going to show today will clear up some of that mesh all right so I think we all are familiar with the idea of psyllium connecting pods within kubernetes cluster and a lot of you will have come across cluster mesh which is how we connect multiple clusters together and we've had a few features in psyllium for quite a while things like support for external workloads kind of simplifying all of this into one thing that we're calling psyllium mesh I'm going to explain to you how really we're using some very kind of fundamental basic concepts within kubernetes to connect workloads whether they're in the same cluster different clusters or not in kubernetes at all so psyllium mesh what are the requirements we want to connect workloads in multiple clusters and also in non-kubernetes environments we want to be able to connect in public cloud and in our own premises we want to be secure which involves both Network policies and authenticated and encrypted connections talk so it seems traditional that we should have some Star Wars references I'm not sure it's exactly Canon but we're basically going along the lines of force awakens right same services and endpoints are kubernetes Concepts and I think you're all pretty familiar with Services maybe we should just have a quick look at what we mean when we say endpoints so we're going to go to Jackie the planet Jackie and bb-8 is going to be able to talk to the resistance service on jakku I don't know if you remember the storyline in the force awakens but basically the resistance is the organization run by General Leia against the first order who are the bad guys so I have a kind cluster here that's called is that big enough we are okay at the back a bit more let's go with that all right all right so I have a kind cluster on Jackie and I currently have I think bb-8 is here yeah and I'm going to deploy the resistance in Jackie oh apply even it's all live right you'll tell me when I do things wrong okay and that is going to create some pods and we have a service okay an
