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
speakers: ["Chris Hein", "Eric Ernst", "Apple", "Inc"]
sched_url: https://kccncna2022.sched.com/event/182I4/running-isolated-virtualclusters-with-kata-cluster-api-chris-hein-eric-ernst-apple-inc
youtube_search_url: https://www.youtube.com/results?search_query=Running+Isolated+VirtualClusters+With+Kata+%26+Cluster+API+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Running Isolated VirtualClusters With Kata & Cluster API - Chris Hein & Eric Ernst, Apple, Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Chris Hein, Eric Ernst, Apple, Inc
- Schedule: https://kccncna2022.sched.com/event/182I4/running-isolated-virtualclusters-with-kata-cluster-api-chris-hein-eric-ernst-apple-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Running+Isolated+VirtualClusters+With+Kata+%26+Cluster+API+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Running Isolated VirtualClusters With Kata & Cluster API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182I4/running-isolated-virtualclusters-with-kata-cluster-api-chris-hein-eric-ernst-apple-inc
- YouTube search: https://www.youtube.com/results?search_query=Running+Isolated+VirtualClusters+With+Kata+%26+Cluster+API+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=T6w3YrExorY
- YouTube title: Running Isolated VirtualClusters With Kata & Cluster API - Chris Hein & Eric Ernst, Apple, Inc
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/running-isolated-virtualclusters-with-kata-cluster-api/T6w3YrExorY.txt
- Transcript chars: 37326
- Keywords: cluster, tenant, actually, control, virtual, talking, running, tenants, basically, container, containers, deploy, workload, little, planes, workloads, access, single

### Resumo baseado na transcript

hi everybody uh thanks for coming to this uh pre-lo or after lunch post lunch uh talk please don't fall asleep I hope it's exciting hopefully you can stay awake uh to introduce myself I'm Chris I work for apple as a software engineer and I'm joined with hi I'm Eric I'm also a software engineer over at Apple cool uh as you can see we're gonna be talking about cotta containers and uh virtual cluster we're not really going to touch on cluster API but that's basis the basis

### Excerpt da transcript

hi everybody uh thanks for coming to this uh pre-lo or after lunch post lunch uh talk please don't fall asleep I hope it's exciting hopefully you can stay awake uh to introduce myself I'm Chris I work for apple as a software engineer and I'm joined with hi I'm Eric I'm also a software engineer over at Apple cool uh as you can see we're gonna be talking about cotta containers and uh virtual cluster we're not really going to touch on cluster API but that's basis the basis for this is all being provisioned through cluster API so to get us started we are in the multi-tenancy track right now so as I'm gonna just make an assumption that all of you are interested in running multi-tenant kubernetes uh if not hopefully it's still interesting to you but as everybody here knows multi-tenancy and kubernetes is it's hard it's not easy there's a lot of steps that you need to do and realistically out of the box it just doesn't work uh there's a lot of pieces that you want to use as a user of kubernetes that just aren't accessible and to make this even harder hard multi-tenancy actual isolation of workloads is very difficult on top of that and this is all based on the the amount of attack vectors that kubernetes has and the difference between the access levels that a data plane has versus a control plane and the pieces that are attached to a control plane that you have access to when you get something like cluster admin this talk is going to be split into two sections we're gonna first start talk about control plane multi-tenancy and then we're going to talk about data plane multi-tenancy and then we're going to talk about uh some some improvements that we've done or features that we've added to cada recently to make that multi-tenant story even more advanced in kubernetes itself so to get us started we're going to first talk about multi-tenant control planes and there's a bunch of tools in this space these days to do this and we're only going to focus on one uh it's one that I'm a maintainer for it's called virtual cluster there's another project called the cluster that you could use some of these same exact Technologies and tools to to implement with that um lots of other tools in this space as well so before we get started on that we're going to first talk about some issues that you have running multi-tenant control planes itself one of the biggest things that you run into or I hope a lot of you have run into is Clumsy and thrashy clients this is something that like if
