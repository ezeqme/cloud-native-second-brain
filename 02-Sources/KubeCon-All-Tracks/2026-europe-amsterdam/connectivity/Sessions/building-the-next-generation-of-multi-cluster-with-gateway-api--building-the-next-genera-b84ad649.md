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
speakers: ["Mike Morris", "Microsoft", "Alan Grosskurth", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW0D/building-the-next-generation-of-multi-cluster-with-gateway-api-mike-morris-microsoft-alan-grosskurth-google
youtube_search_url: https://www.youtube.com/results?search_query=Building+the+Next+Generation+of+Multi-Cluster+with+Gateway+API+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Building the Next Generation of Multi-Cluster with Gateway API - Mike Morris, Microsoft & Alan Grosskurth, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mike Morris, Microsoft, Alan Grosskurth, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW0D/building-the-next-generation-of-multi-cluster-with-gateway-api-mike-morris-microsoft-alan-grosskurth-google
- Busca YouTube: https://www.youtube.com/results?search_query=Building+the+Next+Generation+of+Multi-Cluster+with+Gateway+API+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Building the Next Generation of Multi-Cluster with Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0D/building-the-next-generation-of-multi-cluster-with-gateway-api-mike-morris-microsoft-alan-grosskurth-google
- YouTube search: https://www.youtube.com/results?search_query=Building+the+Next+Generation+of+Multi-Cluster+with+Gateway+API+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oRbdcHgHPbo
- YouTube title: Building the Next Generation of Multi-Cluster with Gateway API - Mike Morris & Alan Grosskurth
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/building-the-next-generation-of-multi-cluster-with-gateway-api/oRbdcHgHPbo.txt
- Transcript chars: 24816
- Keywords: gateway, cluster, clusters, endpoint, multi-cluster, across, working, resource, multiple, implementation, selector, address, actually, basically, gateways, inference, flexibility, traffic

### Resumo baseado na transcript

Uh welcome everyone, and thank you for sticking around for the last talk of the day, I believe. I'm a product manager at Microsoft working on upstream open source networking stuff, Gateway API and Istio. It is used by almost every user of Kubernetes, and it was designed 10 years ago. So, things have changed and evolved, and we have new constraints and new design patterns and new workflows that we're trying to enable, and we've kind of gotten to the point where we can stop just like patching things on top of service. Uh the maintainers of Kubernetes are also at a point where it's not really sustainable to even accept those kind of contributions to to keep just like duct taping additional things on top of it. So, you might have a dozen end points in one cluster and only two in another one depending on the size and scale that you're operating at.

### Excerpt da transcript

All right. Uh welcome everyone, and thank you for sticking around for the last talk of the day, I believe. >> [laughter] >> All right. Uh hi. I'm Mike. I'm a product manager at Microsoft working on upstream open source networking stuff, Gateway API and Istio. And >> Hi, I'm Alan. I'm a software engineer at Google working on service networking. And so today we'd like [clears throat] to talk to you a little bit about Gateway API and uh the data model and multi-cluster services. So, the agenda today we're going to go through some background and lessons learned about the history of services and how services have been used in the past. Um some of the lessons learned trying to do different things with services. Uh then we're going to talk about the desirable properties of what we want to have out of a solution for multi-cluster involving Gateway API. Uh we're going to go through some ideas for solutions, um talk about some experimental implementations and prototypes, and then leave with some closing thoughts.

All right. So, who here has ever regretted an API design decision they have made? And who has had to live with it because your users expected it to not change? So, we've had that same problem in Kubernetes. Uh service is one of the oldest APIs. It is very much a load-bearing API. It is used by almost every user of Kubernetes, and it was designed 10 years ago. So, things have changed and evolved, and we have new constraints and new design patterns and new workflows that we're trying to enable, and we've kind of gotten to the point where we can stop just like patching things on top of service. Uh the maintainers of Kubernetes are also at a point where it's not really sustainable to even accept those kind of contributions to to keep just like duct taping additional things on top of it. Um so, we need to start rethinking what we do with this uh and how we can kind of modernize some of the stuff under the hood uh to really allow the flexibility that we need for some of these modern demands that we're facing.

So, one of the things that we kind of discovered at service uh in through Gateway API when we were working on Gamma, so the Gateway API for mesh uh initiative, is that service really kind of has two facets to it. So, there's a front end, which is how you might be familiar with interacting with the service. It's a human-readable name, there's a FQDN hostname, the like .cluster.local address that you're using it to call that service from all of your other se
