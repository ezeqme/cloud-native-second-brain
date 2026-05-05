---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Connectivity"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Lionel Jouin", "Sebastian Scheinkman", "Red Hat", "Antonio Ojea", "Google", "Sunyanan Choochotkaew", "IBM"]
sched_url: https://kccnceu2026.sched.com/event/2CVz9/kubernetes-network-driver-unpacked-modularity-trade-offs-and-the-road-ahead-lionel-jouin-sebastian-scheinkman-red-hat-antonio-ojea-google-sunyanan-choochotkaew-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Network+Driver+Unpacked%3A+Modularity%2C+Trade-offs+and+the+Road+Ahead+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Kubernetes Network Driver Unpacked: Modularity, Trade-offs and the Road Ahead - Lionel Jouin & Sebastian Scheinkman, Red Hat; Antonio Ojea, Google; Sunyanan Choochotkaew, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Lionel Jouin, Sebastian Scheinkman, Red Hat, Antonio Ojea, Google, Sunyanan Choochotkaew, IBM
- Schedule: https://kccnceu2026.sched.com/event/2CVz9/kubernetes-network-driver-unpacked-modularity-trade-offs-and-the-road-ahead-lionel-jouin-sebastian-scheinkman-red-hat-antonio-ojea-google-sunyanan-choochotkaew-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Network+Driver+Unpacked%3A+Modularity%2C+Trade-offs+and+the+Road+Ahead+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Kubernetes Network Driver Unpacked: Modularity, Trade-offs and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVz9/kubernetes-network-driver-unpacked-modularity-trade-offs-and-the-road-ahead-lionel-jouin-sebastian-scheinkman-red-hat-antonio-ojea-google-sunyanan-choochotkaew-ibm
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Network+Driver+Unpacked%3A+Modularity%2C+Trade-offs+and+the+Road+Ahead+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xJ9R7NNZMyQ
- YouTube title: Kubernetes Network Driver Unpacked: Modularity, Tra... Lionel J, Sebastian S, Antonio O & Sunyanan C
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/kubernetes-network-driver-unpacked-modularity-trade-offs-and-the-road/xJ9R7NNZMyQ.txt
- Transcript chars: 24800
- Keywords: network, driver, drivers, device, devices, working, resource, bandwidth, multiple, support, capacity, sebastian, networks, networking, another, talking, question, allocate

### Resumo baseado na transcript

within the uh SIG network uh SIG network in Kubernetes and I've contributed a little bit to to DR and I think it's great project >> and hello my name is Sebastian I working at Reddit and I'm a maintainer for the Kubernetes network plumbing working group and the sub projects like multusv and things like that >> hello I'man from IBM research uh I'm maintainer of one of the CNI that we use in on our cloud and also I propose one kit related to the DRA for networks the problem we have is on the uh cost optimizations of like the nick selection stuff. So what we do is we develop our CNI ourself and we do the policies based n selection in our CNI to like to optimize the cost of like which uh n is good for this GPU for examples and also like we can do like dynamics metrics uh cost optimizations as well but it mean that we put the thing that scheduler should do in our CNI then we know about the DRA comes and then we see the opportunity is to put the right thing in the right Uh that's was one of the objective of the multin project that's to have the network represented as a a first class citizen Kubernetes and one of the overlapping that was uh that was uh noted or marked uh during the during the first proposal was the overlapping with DRS.

### Excerpt da transcript

Hello. It's super hard to see with the lights. Nice to meet you. Hello. We are here to talk about Kubernetes network drivers. And let's introduce ourselves. My name is Antonio H. I work in in Google and I'm S network and testing TL. I'm part of the Kubernetes steering committee. >> And I'm Yan. I'm working at Red Hat. I'm working I'm a sen maintainer. I'm working on the multinetics project. within the uh SIG network uh SIG network in Kubernetes and I've contributed a little bit to to DR and I think it's great project >> and hello my name is Sebastian I working at Reddit and I'm a maintainer for the Kubernetes network plumbing working group and the sub projects like multusv and things like that >> hello I'man from IBM research uh I'm maintainer of one of the CNI that we use in on our cloud and also I propose one kit related to the DRA for networks and implement some DRA drivers top of that. >> Okay, so let's get going. You see that we have a lot of networking people here, right? from different areas and you saw the the title of the of the talk is Kubernet network driver but we are mentioning DRA right and one of the origins of of DA for networking was that all these communities needed some more capabilities in core Kubernet right so we have people working in in different areas of the project especially on the accelerator stuff and they were doing the array and that's when networking people went to the array and I want our co-speakers to explain a bit more what problem is solving the the array that could was impossible to solve before right is why why did you need to use the what are the benefits >> yeah so I think I will start from my side first of all on the telco area if I'm looking one of the core requirement for telco is high performance networking that need for example SR RV devices and also low latency with using CPU pinning and memory.

So for that you can allocate with the extended resource that exists today using device plug-in and you can request using the cublet feature from device manager CPU manager and memory manager. You can require a single numa but the problem is that happened on the node itself. So on the allocation in cublet and you can get to a point where you still have available devices for example in the node but none of them is capable of doing a single numa so they are from different numa and what will happen your pod will get allocated there and get an ex an affinity error so with dra we can move that topology into theuler and it's
