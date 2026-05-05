---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Kubernetes Core", "Community Governance"]
speakers: ["Lance Austin", "Ambassador Labs", "Flynn", "Buoyant"]
sched_url: https://kccnceu2023.sched.com/event/1HzcW/emissary-ingress-self-service-apis-and-the-kubernetes-gateway-api-lance-austin-ambassador-labs-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Emissary-Ingress%3A+Self-Service+APIs+and+the+Kubernetes+Gateway+API+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Emissary-Ingress: Self-Service APIs and the Kubernetes Gateway API - Lance Austin, Ambassador Labs & Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Lance Austin, Ambassador Labs, Flynn, Buoyant
- Schedule: https://kccnceu2023.sched.com/event/1HzcW/emissary-ingress-self-service-apis-and-the-kubernetes-gateway-api-lance-austin-ambassador-labs-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary-Ingress%3A+Self-Service+APIs+and+the+Kubernetes+Gateway+API+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Emissary-Ingress: Self-Service APIs and the Kubernetes Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HzcW/emissary-ingress-self-service-apis-and-the-kubernetes-gateway-api-lance-austin-ambassador-labs-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Emissary-Ingress%3A+Self-Service+APIs+and+the+Kubernetes+Gateway+API+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UKc01HZasWc
- YouTube title: Emissary-Ingress: Self-Service APIs and the Kubernetes Gateway API - Hamzah Qudsi & Flynn
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/emissary-ingress-self-service-apis-and-the-kubernetes-gateway-api/UKc01HZasWc.txt
- Transcript chars: 31983
- Keywords: gateway, emissary, cluster, ingress, envoy, developers, actually, trying, developer, running, little, figure, resource, resources, traffic, application, basically, support

### Resumo baseado na transcript

hello everyone thank you for coming this is the maintainers track for mser Ingress uh I am hza I'm a senior engineer and Ambassador I'm Flynn I'm a technical evangelist for buyant I was the original author of emary engress loow these many years ago before I went over to the dark side to work in marketing thank you for that I'm still a maintainer though thank you for that and yeah we're just going to do like a little quick intro and just give a you know quick update just a good TBL you know we're just updating the minimum version for TLS to 13 a very long overdue security upgrade um but I mean we we we do take security and a lot of the bug fixes uh seriously and so and over

### Excerpt da transcript

hello everyone thank you for coming this is the maintainers track for mser Ingress uh I am hza I'm a senior engineer and Ambassador I'm Flynn I'm a technical evangelist for buyant I was the original author of emary engress loow these many years ago before I went over to the dark side to work in marketing thank you for that I'm still a maintainer though thank you for that and yeah we're just going to do like a little quick intro and just give a you know quick update on sort of the current state of the world of where we are with the project uh we're talk a little bit about self-service configuration and then we'll switch gears a bit talk a bit and give our thoughts about Gateway API want to go over from here uh quick to a hands who here is new to Emissary Ingress anybody all right got a few hands so I guess we're going to do the I guess we're not just going to skip the intro oh man um emary Ingress is an API Gateway so if you have a cluster full of microservices and you're trying to talk to them your users are going to be outside your cluster in a great many cases and you need something to allow them to reach into your cluster to see your services from outside the cluster because one of the points of a cluster is to protect you from this exact thing happening so you throw in an API Gateway so that you can both allow this and also control it Emissary Ingress is an open source Cloud native developer centc self-service opinionated API Gateway it's a cncf incubating project it is powered by Envoy specifically we have Envoy Wrangle all of the users data and then we let Emissary Wrangle the envoys one of the core functions of an API Gateway is traffic management so if you have a user named Jane out in the world and she wants to go and make a request to a SL quot endpoint then Emser can allow that and Route it through to some microser in the cluster if another user named Mark requests exactly the same thing the same thing will happen it might go to a different instance of that workload it doesn't really matter it might go to the same one on the other hand traffic management is not the only thing that goes on with API gateways this is one of the differences between an API Gateway and a simple proxy you can also do things like maybe Jane is allowed to update quotes but Mark is not allowed to so you can just look at that figure figure out who's doing it and block it rather than allowing it through there are a lot of things in here observability rate limiting resilienc
