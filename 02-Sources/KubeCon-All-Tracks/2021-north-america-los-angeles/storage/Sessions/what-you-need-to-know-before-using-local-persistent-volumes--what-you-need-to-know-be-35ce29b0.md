---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Storage"
themes: ["Storage Data"]
speakers: ["Sebastien Guilloux", "Elastic"]
sched_url: https://kccncna2021.sched.com/event/lV18/what-you-need-to-know-before-using-local-persistent-volumes-sebastien-guilloux-elastic
youtube_search_url: https://www.youtube.com/results?search_query=What+You+Need+to+Know+Before+Using+Local+Persistent+Volumes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# What You Need to Know Before Using Local Persistent Volumes - Sebastien Guilloux, Elastic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]]
- País/cidade: United States / Los Angeles
- Speakers: Sebastien Guilloux, Elastic
- Schedule: https://kccncna2021.sched.com/event/lV18/what-you-need-to-know-before-using-local-persistent-volumes-sebastien-guilloux-elastic
- Busca YouTube: https://www.youtube.com/results?search_query=What+You+Need+to+Know+Before+Using+Local+Persistent+Volumes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre What You Need to Know Before Using Local Persistent Volumes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV18/what-you-need-to-know-before-using-local-persistent-volumes-sebastien-guilloux-elastic
- YouTube search: https://www.youtube.com/results?search_query=What+You+Need+to+Know+Before+Using+Local+Persistent+Volumes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8TskPf51wgI
- YouTube title: What You Need to Know Before Using Local Persistent Volumes - Sebastien Guilloux, Elastic
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/what-you-need-to-know-before-using-local-persistent-volumes/8TskPf51wgI.txt
- Transcript chars: 31499
- Keywords: volume, volumes, stateful, persistent, create, storage, particular, cluster, controller, delete, another, automatically, recreated, usually, network, workload, basically, provision

### Resumo baseado na transcript

hey everyone this is kubcon and cloud native con north america 2021 and this session is about what you need to know before using local persistent volumes on kubernetes my name is sebastian most people call me seb so you can just do that i'm a software engineer at elastic um where i mostly work on our kubernetes operator for the elastic stack that we call eck as in elastic cloud on kubernetes so on the agenda today we'll mostly talk about local volumes and basically start with explaining how

### Excerpt da transcript

hey everyone this is kubcon and cloud native con north america 2021 and this session is about what you need to know before using local persistent volumes on kubernetes my name is sebastian most people call me seb so you can just do that i'm a software engineer at elastic um where i mostly work on our kubernetes operator for the elastic stack that we call eck as in elastic cloud on kubernetes so on the agenda today we'll mostly talk about local volumes and basically start with explaining how they work and how things are plugged together in the kubernetes world then we'll mention how you can provision those local volumes in different ways and finally i think the most important part of this presentation is going to be the last part about what i call operational gotchas which is basically a list of things you need to pay attention to to ensure you are using your local volumes and especially your stateful workloads along with them the right way so let's get started how do things work what are persistent volumes at all so usually when we talk about system volumes we associate that concept with the stateful set concepts which is a way to deploy stateful workloads in kubernetes so let's take an example here on the left in that pink box i'm deploying a stateful set with three replicas and let's imagine this is an elasticsearch cluster but it could really be any sort of distributed database in this example and in the stateful set i'm i'm specifying that i want 100 gig of storage per pods so the stateful side controller in turn will create three pods because i i want three replicas so the first part is gonna be with ordinal number zero all you know number one and then we have another one the last one with ordinal number two and because i requested a claim of 100 gigabytes each of this part is going to be associated to a persistent volume so a storage unit of 100 gigabytes and the nice part about the stateful set and the persistent volume concept is that we have a direct direct one-to-one relationship between the pod and a persistent volume here so for example this part my es cluster 0 is associated to this system volume called data my es cluster zero this property is very nice because whenever for example that pod number two gets deleted either unproposed because you want to upgrade it or either accidentally then the relationship with its volume stays intact so here the stateful set controller would just recreate that missing part for the stateful set and that pod wi
