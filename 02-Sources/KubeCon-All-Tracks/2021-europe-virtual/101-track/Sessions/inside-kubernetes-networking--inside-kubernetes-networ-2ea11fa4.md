---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Dominik Tornow", "Cisco"]
sched_url: https://kccnceu2021.sched.com/event/iE4A/inside-kubernetes-networking-dominik-tornow-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Inside+Kubernetes+Networking+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Inside Kubernetes Networking - Dominik Tornow, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Dominik Tornow, Cisco
- Schedule: https://kccnceu2021.sched.com/event/iE4A/inside-kubernetes-networking-dominik-tornow-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Inside+Kubernetes+Networking+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Inside Kubernetes Networking.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4A/inside-kubernetes-networking-dominik-tornow-cisco
- YouTube search: https://www.youtube.com/results?search_query=Inside+Kubernetes+Networking+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kgYcl6bXqMg
- YouTube title: Inside Kubernetes Networking - Dominik Tornow, Cisco
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/inside-kubernetes-networking/kgYcl6bXqMg.txt
- Transcript chars: 20144
- Keywords: switch, message, container, address, target, forward, information, network, context, executing, against, receive, hosted, networking, discuss, relevant, instructs, communication

### Resumo baseado na transcript

hello and welcome to inside kubernetes networking a kubecon and cloud nativecon europe 2021 presentation i am dominic torno principal engineer at cisco i focus on systems modelling specifically conceptual and formal modeling to support the development and documentation of complex software systems kubernetes networking is a core abstraction of kubernetes kubernetes networking ensures components within cluster boundaries and components across cluster boundaries can communicate kubernetes networking is split into the kubernetes networking specification and the kubernetes networking implementation in fact many alternative implementations called kubernetes network plugins exist today will send the message m via its edge to container c 1.1 and finally the container will receive the message next in this example we will discuss kubernetes services here cluster ip services some understanding of services will be beneficial kubernetes services is an anycast kubernetes will allocate an ip address for this service and configure the forward information base so that a message with a target address of the service ip address in the target port of 80 will be received by a container of any part matching the the node switch will call itself and match the new message against its forward information base and from here we already know what is going to happen next in this example we will discuss...

### Excerpt da transcript

hello and welcome to inside kubernetes networking a kubecon and cloud nativecon europe 2021 presentation i am dominic torno principal engineer at cisco i focus on systems modelling specifically conceptual and formal modeling to support the development and documentation of complex software systems kubernetes networking is a core abstraction of kubernetes kubernetes networking ensures components within cluster boundaries and components across cluster boundaries can communicate kubernetes networking is split into the kubernetes networking specification and the kubernetes networking implementation in fact many alternative implementations called kubernetes network plugins exist today the details of the kubernetes network implementation depend on the details of the kubernetes network plugin no two are alike therefore instead of discussing a complete picture based on one particular network plugin or an incomplete picture based on the least common denominator of all network plugins in this presentation we will discuss an idealized implementation accordingly this presentation is split into two parts the first part discussing the specification the second part discussing an idealized implementation so first up the kubernetes networking specification from the point of view of the kubernetes networking specification a kubernetes cluster consists of a set of nodes each node hosts a set of parts and each part executes a set of containers additionally each node hosts a set of processes called daemons in the context of kubernetes network addressable elements that is elements with an ip address consist of nodes and parts however keep in mind that the ultimate producers and consumers of messages are not nodes and parts but are instead containers and daemons the kubernetes networking specification is a set of constraints on the message exchange between containers and containers and containers and daemons the kubernetes network specification addresses three different concerns container to container communication part part-to-part communication and daemon to part communication first we will discuss container to container communication the specification requires that a container c1 that is executing in the context of a part p can communicate with any other container c2 that is also executing in the context of p via localhost or via the ip address of p again represented graphically a container c1 that is executing in the context of a part p can communicate with any other containe
