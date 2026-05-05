---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Jason DeTiberus", "Equinix Metal"]
sched_url: https://kccnceu2021.sched.com/event/iE4V/from-tweet-to-badidea-creating-an-embeddable-kubernetes-style-api-server-jason-detiberus-equinix-metal
youtube_search_url: https://www.youtube.com/results?search_query=From+Tweet+to+BadIdea%3A+Creating+an+Embeddable+Kubernetes+Style+API+Server+CNCF+KubeCon+2021
slides: []
status: parsed
---

# From Tweet to BadIdea: Creating an Embeddable Kubernetes Style API Server - Jason DeTiberus, Equinix Metal

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Jason DeTiberus, Equinix Metal
- Schedule: https://kccnceu2021.sched.com/event/iE4V/from-tweet-to-badidea-creating-an-embeddable-kubernetes-style-api-server-jason-detiberus-equinix-metal
- Busca YouTube: https://www.youtube.com/results?search_query=From+Tweet+to+BadIdea%3A+Creating+an+Embeddable+Kubernetes+Style+API+Server+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre From Tweet to BadIdea: Creating an Embeddable Kubernetes Style API Server.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4V/from-tweet-to-badidea-creating-an-embeddable-kubernetes-style-api-server-jason-detiberus-equinix-metal
- YouTube search: https://www.youtube.com/results?search_query=From+Tweet+to+BadIdea%3A+Creating+an+Embeddable+Kubernetes+Style+API+Server+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fxqV24h_ocs
- YouTube title: From Tweet to BadIdea: Creating an Embeddable Kubernetes Style API Server - Jason DeTiberus
- Match score: 0.98
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/from-tweet-to-badidea-creating-an-embeddable-kubernetes-style-api-serv/fxqV24h_ocs.txt
- Transcript chars: 18287
- Keywords: server, actually, resources, trying, application, create, infrastructure, little, components, basically, created, config, controller, cluster, applications, version, functionality, simple

### Resumo baseado na transcript

hello thank you for joining me for from tweet to bad idea creating an embeddable kubernetes style api server my name is jason detebros i am at equinix metal and i am working to bring cloud native infrastructure management into the data center um i am also one of the co-maintainers for the cluster api project and you can generally find me on twitter at dtipper so um going back to twitter is how this all started um i put out a call uh asking if anybody uh thought it

### Excerpt da transcript

hello thank you for joining me for from tweet to bad idea creating an embeddable kubernetes style api server my name is jason detebros i am at equinix metal and i am working to bring cloud native infrastructure management into the data center um i am also one of the co-maintainers for the cluster api project and you can generally find me on twitter at dtipper so um going back to twitter is how this all started um i put out a call uh asking if anybody uh thought it would be possible to go ahead and build this idea of a minimal kubernetes style api server that's port crds and that took me down quite a bit of a rabbit hole um but why would i want to case this rabbit hole um well because crds actually give you a lot to be able to build out applications pretty quickly provide a lot of value for example crds uh give you out of the box data persistence version semantics defaulting validation and clients and those clients don't just support crud applications they also give you the same list watch type semantics that kubernetes itself does however crds also come with a pretty steep cost for certain types of applications because it brings a dependency on kubernetes now for most things that's not generally too bad because you're generally deploying applications on infrastructure that already exist things like that but what if you're building applications that manage that underlying infrastructure for example in the cluster api project we work around that today by having the ability to use a kind of an ephemeral bootstrap cluster to be able to stand up the cluster api managed infrastructure and then kind of move those resources over to that cluster that you just created now that works okay for cluster api but what if you're trying to get something even deeper down in the infrastructure for example automating bare metal infrastructure in the data center uh like the tinkerbell project which is a cncfnbox project well you got a chicken and egg there that is very difficult to kind of resolve so is there a way to leverage crds in that type of environment well this rabbit hole got me doing a lot of research you know has somebody already done this you know there's been kind of rumblings back forth between people in the community about whether or not this is something that could be possible you know people talking about potentially doing it tim hawking was talking about this back in 2018 about trying to move more kubernetes resources themselves towards crds versus uh being bu
