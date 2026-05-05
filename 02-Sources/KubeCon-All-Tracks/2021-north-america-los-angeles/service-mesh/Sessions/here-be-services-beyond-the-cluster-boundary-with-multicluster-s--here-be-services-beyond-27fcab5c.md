---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Service Mesh"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Laura Lorenz", "Google", "Stephen Kitt", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV67/here-be-services-beyond-the-cluster-boundary-with-multicluster-services-laura-lorenz-google-stephen-kitt-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Here+Be+Services%3A+Beyond+the+Cluster+Boundary+with+Multicluster+Services+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Here Be Services: Beyond the Cluster Boundary with Multicluster Services - Laura Lorenz, Google & Stephen Kitt, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Laura Lorenz, Google, Stephen Kitt, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV67/here-be-services-beyond-the-cluster-boundary-with-multicluster-services-laura-lorenz-google-stephen-kitt-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Here+Be+Services%3A+Beyond+the+Cluster+Boundary+with+Multicluster+Services+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Here Be Services: Beyond the Cluster Boundary with Multicluster Services.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV67/here-be-services-beyond-the-cluster-boundary-with-multicluster-services-laura-lorenz-google-stephen-kitt-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Here+Be+Services%3A+Beyond+the+Cluster+Boundary+with+Multicluster+Services+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_UJrSfmvlMA
- YouTube title: Here Be Services: Beyond the Cluster Boundary with Multicluster Servi... Laura Lorenz & Stephen Kitt
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/here-be-services-beyond-the-cluster-boundary-with-multicluster-service/_UJrSfmvlMA.txt
- Transcript chars: 27883
- Keywords: cluster, clusters, submariner, multi-cluster, export, across, namespace, endpoint, controller, slices, actually, endpoints, information, imports, create, import, records, addresses

### Resumo baseado na transcript

hi everyone thanks for joining us for hereby services my name is stephen and my name is laura and we're going to talk to you about the uncharted unexplored world of multi-cluster services let's start with the map shall we this is the linux globe famous for anachronistically representing an unknown region with the words here be dragons they're in the corner here where it says hickson draconis so this is a good setup for our conversation here about conversation about services across multiple clusters we can imagine it like

### Excerpt da transcript

hi everyone thanks for joining us for hereby services my name is stephen and my name is laura and we're going to talk to you about the uncharted unexplored world of multi-cluster services let's start with the map shall we this is the linux globe famous for anachronistically representing an unknown region with the words here be dragons they're in the corner here where it says hickson draconis so this is a good setup for our conversation here about conversation about services across multiple clusters we can imagine it like our kubernetes clusters our islands on this map separated by dangerous and uncharted seas you want to open trade routes but that means having open ports and sending ships which risk being attacked by pirates across those uncharted seas even if port access is controlled which is good because you can then collect taxes there's a lot of effort in each port and since the seas are uncharted how do other islands know about your ports now there are some other ways that people have been trying to do this we are at the service mesh track of this conference after all so istio is an option this is an open source service mesh that you can deploy across your kubernetes clusters and vms in any provider it's super powerful but not everyone chooses to implement a whole service mesh or it might have a smaller kubernetes deployment for which it feels too heavy other folks choose to roll their own solution so sometimes people will stand up a reverse proxy for example nginx between multiple clusters and handle the configuration to request multiple back-ends themselves the downside is that there's no general configuration pattern for this so you basically have to figure it out yourself but there is another way so sig multi-cluster which steven and i are both part of have been working on a standard that describes how to extend the existing kubernetes service concept to multiple clusters leading to the multi-cluster services or mcs api the whole idea sigmulti cluster is going for is to provide a multi-cluster solution that feels really natural to have people already use kubernetes services today everything is modeled around the existing service primitive and mcs defines the minimal amount of extra stuff needed to make them available across the clusters the goal is that client applications should have barely any changes in order to use a multi-cluster service instead of a cluster local service this api is based around the idea of a cluster set capital c capital s
