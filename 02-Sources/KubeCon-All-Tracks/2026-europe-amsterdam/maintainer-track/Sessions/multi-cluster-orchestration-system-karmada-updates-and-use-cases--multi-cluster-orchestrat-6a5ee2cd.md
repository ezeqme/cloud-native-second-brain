---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Hongcai Ren", "Huawei", "Tessa Pham", "Michas Szacillo", "Wei-Cheng Lai", "Bloomberg", "Zongqing Li", "Trip.com"]
sched_url: https://kccnceu2026.sched.com/event/2EF6Z/multi-cluster-orchestration-system-karmada-updates-and-use-cases-hongcai-ren-huawei-tessa-pham-michas-szacillo-wei-cheng-lai-bloomberg-zongqing-li-tripcom
youtube_search_url: https://www.youtube.com/results?search_query=Multi-cluster+Orchestration+System%3A+Karmada+Updates+and+Use+Cases+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Multi-cluster Orchestration System: Karmada Updates and Use Cases - Hongcai Ren, Huawei; Tessa Pham, Michas Szacillo & Wei-Cheng Lai, Bloomberg; Zongqing Li, Trip.com

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Hongcai Ren, Huawei, Tessa Pham, Michas Szacillo, Wei-Cheng Lai, Bloomberg, Zongqing Li, Trip.com
- Schedule: https://kccnceu2026.sched.com/event/2EF6Z/multi-cluster-orchestration-system-karmada-updates-and-use-cases-hongcai-ren-huawei-tessa-pham-michas-szacillo-wei-cheng-lai-bloomberg-zongqing-li-tripcom
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-cluster+Orchestration+System%3A+Karmada+Updates+and+Use+Cases+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Multi-cluster Orchestration System: Karmada Updates and Use Cases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6Z/multi-cluster-orchestration-system-karmada-updates-and-use-cases-hongcai-ren-huawei-tessa-pham-michas-szacillo-wei-cheng-lai-bloomberg-zongqing-li-tripcom
- YouTube search: https://www.youtube.com/results?search_query=Multi-cluster+Orchestration+System%3A+Karmada+Updates+and+Use+Cases+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BU2XT2DpI2Q
- YouTube title: Multi-cluster Orchestration System: Karmada Updates and Use Cases - Hongcai Ren, Huawei
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/multi-cluster-orchestration-system-karmada-updates-and-use-cases/BU2XT2DpI2Q.txt
- Transcript chars: 12646
- Keywords: application, kamada, feature, cluster, another, applications, deploy, commada, command, clusters, release, provide, migrate, priority, scheduling, operator, running, search

### Resumo baseado na transcript

Uh I'm Hung Kai uh from uh I'm for I'm one of the maintainer of our Kamada project. Um today uh we'll explore uh how how Kamada manage applications uh across uh clusters and uh what's the updates um and the status of the Kamada community. Uh you can see uh commada link is consist of command API server, commada and uh uh the architecture is uh extremely similar to kubernetes and the difference between uh between kubernetes is kubernetes is managing nodes and deploy p to nodes but kamada managing So um what happens uh after the application is uh running in mult cluster uh one of one of the requirements uh is uh the administrator or the user need to uh query uh how the application running and where is the application running. So people can use uh like uh our kamada API or cook control to uh query uh the the results. So if you are going to learn more about about the the feature and how it works in Bloomberg, you can go to uh the section tomorrow morning.

### Excerpt da transcript

Hello, welcome to uh this talk. Uh I'm Hung Kai uh from uh I'm for I'm one of the maintainer of our Kamada project. Um today uh we'll explore uh how how Kamada manage applications uh across uh clusters and uh what's the updates um and the status of the Kamada community. Uh okay let's get started. First uh let's quickly go through the uh agenda. uh we'll start with uh what kamada is and it uh core features then uh I will share new updates from recent releases uh from 1 to 1.15 14. So uh and at last we'll look at the community growth and our future uh future roadm uh first the question is what exactly is Kamada? So, Kamada is um uh project that uh lets you deploy, scale, monitor your applications uh from one place. Uh think of uh it as a uh control center to your uh cloud native applications. uh no more repeated tasks uh just a unified management. Um mostly Kamada is used by uh infrastructure team and uh the the infrastructure team or with manage their clusters resources and provide a service to uh the business team.

So the business business team can deploy their uh AI training job um data processing job or workflow and uh uh Kubernetes deployments and so on. So this is a commada architecture. Uh you can see uh commada link is consist of command API server, commada and uh uh the architecture is uh extremely similar to kubernetes and the difference between uh between kubernetes is kubernetes is managing nodes and deploy p to nodes but kamada managing uh kubernetes this cluster and uh deploy application to cluster. So um uh most of people use kamada as a CD system. So they uh usually use kamada to to to deploy applications uh across multiple cluster. uh commander can help them help uh to uh deploy application to each of the cluster or uh or split the replicas between clusters. So um what happens uh after the application is uh running in mult cluster uh one of one of the requirements uh is uh the administrator or the user need to uh query uh how the application running and where is the application running. So they need a global resource view.

In Kamada we build the uh capacity by a com uh component named the commada search. Uh with that the commada search uh will cache all the resources from memor clusters and provide uh uh API. So people can use uh like uh our kamada API or cook control to uh query uh the the results. So uh one of our user you using this to build the global view with u elected search and here I show the open search that's the same. So uh ano
