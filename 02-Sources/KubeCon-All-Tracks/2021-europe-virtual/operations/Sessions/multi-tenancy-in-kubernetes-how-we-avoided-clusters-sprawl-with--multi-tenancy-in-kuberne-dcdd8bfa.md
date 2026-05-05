---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Operations"
themes: ["Kubernetes Core"]
speakers: ["Dario Tranchitella", "CLASTIX", "Maksim Fedotov", "Wargaming.net"]
sched_url: https://kccnceu2021.sched.com/event/iE2c/multi-tenancy-in-kubernetes-how-we-avoided-clusters-sprawl-with-capsule-dario-tranchitella-clastix-maksim-fedotov-wargamingnet
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Tenancy+in+Kubernetes%3A+How+We+Avoided+Clusters+Sprawl+With+Capsule+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Multi-Tenancy in Kubernetes: How We Avoided Clusters Sprawl With Capsule - Dario Tranchitella, CLASTIX & Maksim Fedotov, Wargaming.net

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Operations]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Dario Tranchitella, CLASTIX, Maksim Fedotov, Wargaming.net
- Schedule: https://kccnceu2021.sched.com/event/iE2c/multi-tenancy-in-kubernetes-how-we-avoided-clusters-sprawl-with-capsule-dario-tranchitella-clastix-maksim-fedotov-wargamingnet
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Tenancy+in+Kubernetes%3A+How+We+Avoided+Clusters+Sprawl+With+Capsule+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Multi-Tenancy in Kubernetes: How We Avoided Clusters Sprawl With Capsule.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2c/multi-tenancy-in-kubernetes-how-we-avoided-clusters-sprawl-with-capsule-dario-tranchitella-clastix-maksim-fedotov-wargamingnet
- YouTube search: https://www.youtube.com/results?search_query=Multi-Tenancy+in+Kubernetes%3A+How+We+Avoided+Clusters+Sprawl+With+Capsule+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WWKat7NP0NM
- YouTube title: Multi-Tenancy in Kubernetes: How We Avoided Clusters Sprawl W... Dario Tranchitella & Maksim Fedotov
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/multi-tenancy-in-kubernetes-how-we-avoided-clusters-sprawl-with-capsul/WWKat7NP0NM.txt
- Transcript chars: 27138
- Keywords: capsule, tenant, cluster, multi-tenancy, resources, namespace, customers, customer, namespaces, internal, provide, resource, clusters, specific, network, ingress, additional, together

### Resumo baseado na transcript

hey people good morning or whatever the time is it and my name is dario and i'm here with max hi max how do you do hello everyone yeah i'm fine thanks how are you well well a little bit excited because it's my first time at cubecom as speaker and also as attendee and i'm really happy to be here with you because we are going to we did with capsule and it's really as astonishing i'm really free to be here and i'd like to thank all the

### Excerpt da transcript

hey people good morning or whatever the time is it and my name is dario and i'm here with max hi max how do you do hello everyone yeah i'm fine thanks how are you well well a little bit excited because it's my first time at cubecom as speaker and also as attendee and i'm really happy to be here with you because we are going to we did with capsule and it's really as astonishing i'm really free to be here and i'd like to thank all the people that is joining this session because we did a great job together as developers and also as architect of the software that we built so um yeah uh i'd like to show you how this presentation is made of so uh this is obviously the introduction and we are going to have two session because this is a presentation between me and max and i'm going to introduce you what is capsule because capsule is an open source project and it's able to provide a multi-tenancy also it's the topic of this session and after that max is going to share what they were able to achieve at wargaming.net with capsule and is going to share some really nice insights regarding the abilities of capsule and the platform that they built so i don't want to provide so much spoilers so i can just suggest you to enjoy it and see you later for the last session bye-bye goodbye and i hope you will be interested hi people my name is zero tranquitella and i'm an open source software engineer at classics an italian startup based in italy with the mission of bringing kubernetes everywhere in this section i'd like to introduce you to capsule the multi-tenancy operator but first i think i should give you a brief introduction about the multi-tenancy dilemma and the current state of multi-tenancy in kubernetes itself and the ecosystem multi-tenancy is nothing new if you're already familiar with the kubernetes the basic resources you are using is namespace allowing you to group application into an application logical group all the posts deployments services ingresses and so forth of each application or maybe team in big corporations is collect in namespaces it's pretty easy to understand this is common and best practice dividing components and applications in several name spaces but doing so doesn't mean you're adopting multi-tenancy there are some aspects you have to consider since it's like the sure dosing in the mid to thousands and i'm referring to the noisy neighbor effects we all know kubernetes is great at crafting distributed systems and provides out of the box some r
