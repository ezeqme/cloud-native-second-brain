---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Multi-tenancy"
themes: ["Kubernetes Core"]
speakers: ["Stefan Schimanski", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182I7/kcp-towards-1000000-clusters-namewworkspaced-crds-stefan-schimanski-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kcp%3A+Towards+1%2C000%2C000+Clusters%2C+Name%5EWWorkspaced+CRDs+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kcp: Towards 1,000,000 Clusters, Name^WWorkspaced CRDs - Stefan Schimanski, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Stefan Schimanski, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182I7/kcp-towards-1000000-clusters-namewworkspaced-crds-stefan-schimanski-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kcp%3A+Towards+1%2C000%2C000+Clusters%2C+Name%5EWWorkspaced+CRDs+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kcp: Towards 1,000,000 Clusters, Name^WWorkspaced CRDs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182I7/kcp-towards-1000000-clusters-namewworkspaced-crds-stefan-schimanski-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kcp%3A+Towards+1%2C000%2C000+Clusters%2C+Name%5EWWorkspaced+CRDs+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fGv5dpQ8X5I
- YouTube title: Kcp: Towards 1,000,000 Clusters, Name^WWorkspaced CRDs - Stefan Schimanski, Red Hat
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kcp-towards-1-000-000-clusters-name-wworkspaced-crds/fGv5dpQ8X5I.txt
- Transcript chars: 33785
- Keywords: workspace, workspaces, basically, cluster, compute, server, clusters, million, everything, namespaces, everybody, export, another, nothing, objects, controller, generic, deployments

### Resumo baseado na transcript

all right so I I hope I can be hurt yes so when I come everybody to I think the last talk today in this track so I'm happy that so many people are here interested in a project a couple of people um work on for I know one and a half years or something kcp um it's complicated to understand there are many views you will see many views on this thing which is called kcp and everybody will find their own definition their own use of that

### Excerpt da transcript

all right so I I hope I can be hurt yes so when I come everybody to I think the last talk today in this track so I'm happy that so many people are here interested in a project a couple of people um work on for I know one and a half years or something kcp um it's complicated to understand there are many views you will see many views on this thing which is called kcp and everybody will find their own definition their own use of that and which way to inspire you to think about how you can use it and how it's different to the tools we have had in the past especially complementing kubernetes as we know it so about myself I'm Peter schumanski I'm looking at redhead I have been working long long time years on CID so I was implemented of many of the foundational features and cids and cids are everywhere in kcp so everything we we see here kcp cids are behind that it all started with an experiment or with a yeah with a prototype kubernetes added namespaces to kubernetes before that everything was basically cluster scoped nowadays everybody takes namespaces for granted there was discussion around whether they needed like whether this namespaces are necessary and yes the community concluded yes we want them and they were added and the isolation we get from those places is pretty weak everybody knows that like you cannot run multi-tenant workloads with high explanation via namespaces in namespaces our namespace is because they separate names it was never meant for anything more than that so the experiment we did was what if we did a different kind of partitioning of kubernetes what if namespace is provided more isolation than just names it's the most prominent example everybody in our cids are not namespaced right so if we want namespace crds we get something like a type space bad name maybe but not namespaces so the experiment is let's do more isolation than just names if we do that we get something we call it workspace and the workspace is a type space in this sense that crds are independent but basically everything else like Discovery open API all that is independent even namespaces are independent if you have two workspaces you will have two default namespaces on both sides so the result of that is basically a workspace is like a cluster the user thinks it's a cluster but expect by the same kubernetes API server if you want we put a Target so we built that like in one API server partitioning into workspaces so you can run it and you can have hundreds of workspaces
