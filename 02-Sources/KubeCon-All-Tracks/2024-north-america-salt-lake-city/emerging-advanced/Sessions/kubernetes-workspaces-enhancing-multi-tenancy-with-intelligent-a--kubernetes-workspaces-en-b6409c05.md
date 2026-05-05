---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["James Munnelly", "Andrea Tosatto", "Apple"]
sched_url: https://kccncna2024.sched.com/event/1i7nS/kubernetes-workspaces-enhancing-multi-tenancy-with-intelligent-apiserver-proxying-james-munnelly-andrea-tosatto-apple
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Workspaces%3A+Enhancing+Multi-Tenancy+with+Intelligent+Apiserver+Proxying+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Workspaces: Enhancing Multi-Tenancy with Intelligent Apiserver Proxying - James Munnelly & Andrea Tosatto, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: James Munnelly, Andrea Tosatto, Apple
- Schedule: https://kccncna2024.sched.com/event/1i7nS/kubernetes-workspaces-enhancing-multi-tenancy-with-intelligent-apiserver-proxying-james-munnelly-andrea-tosatto-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Workspaces%3A+Enhancing+Multi-Tenancy+with+Intelligent+Apiserver+Proxying+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Workspaces: Enhancing Multi-Tenancy with Intelligent Apiserver Proxying.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nS/kubernetes-workspaces-enhancing-multi-tenancy-with-intelligent-apiserver-proxying-james-munnelly-andrea-tosatto-apple
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Workspaces%3A+Enhancing+Multi-Tenancy+with+Intelligent+Apiserver+Proxying+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dQ4j5V6lqeo
- YouTube title: Kubernetes Workspaces: Enhancing Multi-Tenancy with Intelligent Apiserver... J. Munnelly, A. Tosatto
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-workspaces-enhancing-multi-tenancy-with-intelligent-apiserv/dQ4j5V6lqeo.txt
- Transcript chars: 36025
- Keywords: cluster, workspace, spaces, actually, request, controller, within, having, workspaces, resources, server, objects, scoped, access, trying, essentially, authorization, similar

### Resumo baseado na transcript

this presentation's on kubernetes workspaces enhancing multi tendency with intelligent API server proxying so um I'm James monley um field engineer at Apple working in all things kind of kubernetes and helping out customers and I'm andreato and I'm an necess at Apple working on the kubernetes platform as well so the kind of idea of this talk is really to um talk about workspaces um it is something that in the Community we've been talking about like for a long time like on around multi- tency but also like

### Excerpt da transcript

this presentation's on kubernetes workspaces enhancing multi tendency with intelligent API server proxying so um I'm James monley um field engineer at Apple working in all things kind of kubernetes and helping out customers and I'm andreato and I'm an necess at Apple working on the kubernetes platform as well so the kind of idea of this talk is really to um talk about workspaces um it is something that in the Community we've been talking about like for a long time like on around multi- tency but also like it's something that that surprised us preparing like this talk is that like a couple of weeks ago someone also posted like on R like asking like what is a feature that you really want kubernetes to be added of course people have opinion around Alm but also like many of the people really were bringing up like name spaces and like um additional con concept like around like multi tendency within name spaces as a as a kind of like topic and that really resonated with us and is why also it's very similar to why the motivation that let us like to talk about workspaces again and and think about this concept um the way we see workspaces and and this is maybe also something slightly different like from previous approaches is that we really see Works spaces as a view over uh a set of resources that are running across multiple name spaces in a kubernetes cluster and if we think about like this is a very simple scenario but if we think about like how uh teams operate in multitenant cluster they tend to have like a number of Nam spaces in this cluster where they Place their own application into and this is particularly important because kubernetes really like recommend user to use name spaces as boundaries of about their application identity is bounded by name spaces and like policies so um what we see we see thems like especially also from our internal experience having slowly like to have more and more n spaces but of course this comes with toll for them like because there are no good solution like that allow like to operate across multiple spaces some controller like they need like you always need to update like spaces you want to reconcile on um so the kind of idea that we have is had is really to introduce a kind of layer above that allow and this is what word spaces are that allow like to group resources that belong across multiple name spaces providing an experience which is way more similar to the one that operator or in cluster as a service model you give lik
