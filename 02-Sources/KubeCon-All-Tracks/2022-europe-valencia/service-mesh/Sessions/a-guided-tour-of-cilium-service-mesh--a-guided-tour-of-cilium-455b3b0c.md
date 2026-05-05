---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Liz Rice", "Isovalent"]
sched_url: https://kccnceu2022.sched.com/event/yttj/a-guided-tour-of-cilium-service-mesh-liz-rice-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=A+Guided+Tour+of+Cilium+Service+Mesh+CNCF+KubeCon+2022
slides: []
status: parsed
---

# A Guided Tour of Cilium Service Mesh - Liz Rice, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: Spain / Valencia
- Speakers: Liz Rice, Isovalent
- Schedule: https://kccnceu2022.sched.com/event/yttj/a-guided-tour-of-cilium-service-mesh-liz-rice-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=A+Guided+Tour+of+Cilium+Service+Mesh+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre A Guided Tour of Cilium Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttj/a-guided-tour-of-cilium-service-mesh-liz-rice-isovalent
- YouTube search: https://www.youtube.com/results?search_query=A+Guided+Tour+of+Cilium+Service+Mesh+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=e10kDBEsZw4
- YouTube title: A Guided Tour of Cilium Service Mesh - Liz Rice, Isovalent
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/a-guided-tour-of-cilium-service-mesh/e10kDBEsZw4.txt
- Transcript chars: 31064
- Keywords: mesh, psyllium, network, envoy, traffic, kernel, already, networking, visibility, application, ingress, ebpf, pretty, security, sidecar, program, hubble, observability

### Resumo baseado na transcript

hi everyone thank you so much for being here at the end of what seems like a pretty full-on week anybody here feeling a bit tired me too yeah but we'll we can do this we can we can do this so my name's liz rice i'm the chief open source officer at i surveillance isovalent is the company that originally created psyllium and today i'm going to give a tour of the psyllium service mesh now i joined eye surveillance a bit over a year ago and i joined

### Excerpt da transcript

hi everyone thank you so much for being here at the end of what seems like a pretty full-on week anybody here feeling a bit tired me too yeah but we'll we can do this we can we can do this so my name's liz rice i'm the chief open source officer at i surveillance isovalent is the company that originally created psyllium and today i'm going to give a tour of the psyllium service mesh now i joined eye surveillance a bit over a year ago and i joined because i am fascinated by ebpf ebpf is the technology that psyllium uses this talk is not particularly about ebpf um but uh certainly isovenant has a ton of expertise in that area and when i first joined the company thomas graff who i'm sure many of you know uh explained to me that well selim already is kind of 80 of a service mesh so today i'm going to explain why he was saying that why it's actually not such a big leap from psyllium as a cni to psyllium as a service mesh show you some of the features just a little tiny dip into what we have today in service mesh and talk a bit about where we're going next and what still needs to be done so how many of you here are already using psyllium quite a few of you do i have anyone here who was part of the psyllium service mesh beta i see a hand back there so thank you very much oh couple of hands yeah awesome so when we uh i don't know why that thing's okay so when we announced the psyllium service mesh beta program and uh our artist vadim came up with this nice little uh bit of artwork about getting rid of side cars and i think some of that has been a little bit controversial so i hope i'm going to explain today why we're preferring a model that doesn't use sidecars and some of the advantages that that gives us and how we've been able to get there so psyllium as a cni it's based on ebpf that i mentioned it's a very high performance network plug-in for kubernetes you can also use it standalone but i think the majority of users are using it in a kubernetes environment it implements connectivity what else is networking for them to connect our workloads to each other and to the outside world it implements security features we have network policy we have network layer encryption and it provides load balancing whether that's as a cue proxy replacement so load balancing between the different pods that make up a service or also as a standalone load balancer there's also a component called hubble which gives us visibility into network flows so we can get detailed flow logs of ev
