---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Matei David", "Buoyant", "Mike Beaumont", "Kong"]
sched_url: https://kccnceu2024.sched.com/event/1YeS0/sidecar-containers-in-kubernetes-past-present-and-future-matei-david-buoyant-mike-beaumont-kong
youtube_search_url: https://www.youtube.com/results?search_query=Sidecar+Containers+in+Kubernetes%3A+Past%2C+Present%2C+and+Future+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sidecar Containers in Kubernetes: Past, Present, and Future - Matei David, Buoyant & Mike Beaumont, Kong

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Matei David, Buoyant, Mike Beaumont, Kong
- Schedule: https://kccnceu2024.sched.com/event/1YeS0/sidecar-containers-in-kubernetes-past-present-and-future-matei-david-buoyant-mike-beaumont-kong
- Busca YouTube: https://www.youtube.com/results?search_query=Sidecar+Containers+in+Kubernetes%3A+Past%2C+Present%2C+and+Future+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sidecar Containers in Kubernetes: Past, Present, and Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeS0/sidecar-containers-in-kubernetes-past-present-and-future-matei-david-buoyant-mike-beaumont-kong
- YouTube search: https://www.youtube.com/results?search_query=Sidecar+Containers+in+Kubernetes%3A+Past%2C+Present%2C+and+Future+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Fhfr5PyvnUo
- YouTube title: Sidecar Containers in Kubernetes: Past, Present, and Future - Matei David, Buoyant & Mike Beaumont
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sidecar-containers-in-kubernetes-past-present-and-future/Fhfr5PyvnUo.txt
- Transcript chars: 27558
- Keywords: container, containers, sidecar, actually, running, feature, basically, traffic, little, termination, mesh, started, application, resource, restart, functionality, always, mentioned

### Resumo baseado na transcript

hi everybody thanks for coming um so first thing can I get a show of hands who's using side cars at the moment so all of you okay um who is using version already oh yeah uh and are any of you using the new native sidec cars feature with 129 No Hands okay cool uh so I guess after this presentation maybe you'll be convinced to either try out the new feature or convince the authors of your Upstream projects to add support for the feature um my name feature and how it solves some of the problems that Mata just mentioned um in particular I'm going to go into how side cars actually worked in kubernetes before this feature and how they work now um so yeah you might be wondering what's this

### Excerpt da transcript

hi everybody thanks for coming um so first thing can I get a show of hands who's using side cars at the moment so all of you okay um who is using version already oh yeah uh and are any of you using the new native sidec cars feature with 129 No Hands okay cool uh so I guess after this presentation maybe you'll be convinced to either try out the new feature or convince the authors of your Upstream projects to add support for the feature um my name is Mike I'm a software engineer at Kong I work on Kuma and and I'm joined by uh matate I'm a linardy maintainers software engineer at buyant and also I cannot crop pictures as you can see uh both of them have different dimensions but yeah thank you so much for joining us it's uh great to see that we have a full audience especially on a Friday so um yeah I guess let's get started we're uh here to talk about side cars uh past present and future so uh maybe let's talk with what a side car actually is and uh we'll go in the past first um the first reference that we could actually dig up uh Mike and I was from 2015 uh side cars were featured in a kubernetes blog post um about how to actually augment your main container with additional capabilities and all of that good stuff um so yeah they're a design pattern that has essentially been there since the start of kubernetes but uh let's dig a little bit deeper what actually is a side car well it's just a container right in kubernetes you have a pod it's your smallest unit of scheduling work that you can basically deploy in a cluster to have an application running and a pod can have an arbitrary number of containers um and in this case in this diagram we have two containers they're both in the same pod they share the same network Nam space uh but they both have their own uh process trees and they both have their own file systems of course they can still interact with each other they can still share a file system through volume mounts and and all of that stuff but essentially they're isolated and that's exactly what a sidecar container is it's a container that runs in a pod um in the same network names space so it can communicate uh with the other containers via the network over lupac they share the same c groups so resource requirements and resource usages definitely get shared between the two of them uh and then they can share the file system but uh the file system is otherwise isolated um all of these things matter because uh sidecars as we'll see can uh add some additiona
