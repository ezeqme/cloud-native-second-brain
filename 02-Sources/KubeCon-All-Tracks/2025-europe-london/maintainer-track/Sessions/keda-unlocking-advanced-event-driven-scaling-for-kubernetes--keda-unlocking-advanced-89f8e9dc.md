---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Zbynek Roubalik", "Kedify", "Jorge Turrado", "SCRM Lidl International Hub"]
sched_url: https://kccnceu2025.sched.com/event/1tcxY/keda-unlocking-advanced-event-driven-scaling-for-kubernetes-zbynek-roubalik-kedify-jorge-turrado-scrm-lidl-international-hub
youtube_search_url: https://www.youtube.com/results?search_query=KEDA%3A+Unlocking+Advanced+Event-Driven+Scaling+for+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# KEDA: Unlocking Advanced Event-Driven Scaling for Kubernetes - Zbynek Roubalik, Kedify & Jorge Turrado, SCRM Lidl International Hub

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Zbynek Roubalik, Kedify, Jorge Turrado, SCRM Lidl International Hub
- Schedule: https://kccnceu2025.sched.com/event/1tcxY/keda-unlocking-advanced-event-driven-scaling-for-kubernetes-zbynek-roubalik-kedify-jorge-turrado-scrm-lidl-international-hub
- Busca YouTube: https://www.youtube.com/results?search_query=KEDA%3A+Unlocking+Advanced+Event-Driven+Scaling+for+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre KEDA: Unlocking Advanced Event-Driven Scaling for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxY/keda-unlocking-advanced-event-driven-scaling-for-kubernetes-zbynek-roubalik-kedify-jorge-turrado-scrm-lidl-international-hub
- YouTube search: https://www.youtube.com/results?search_query=KEDA%3A+Unlocking+Advanced+Event-Driven+Scaling+for+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=317rLOIKfDQ
- YouTube title: KEDA: Unlocking Advanced Event-Driven Scaling for Kubernetes - Zbynek Roubalik & Jorge Turrado
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keda-unlocking-advanced-event-driven-scaling-for-kubernetes/317rLOIKfDQ.txt
- Transcript chars: 33083
- Keywords: metrics, cluster, scaling, autoscaling, application, scaler, prometheus, basically, working, feature, workloads, workload, instead, thanks, perfect, little, custom, autoscaler

### Resumo baseado na transcript

Thanks everybody for joining us today in this session about KDA and how to unlock new visions and how to use KDA in production. I work as principal SR at CRM the international half of SWARS group and I'm one of KDA maintainers. First, we would like to save resources because we would like to run only the workloads uh when they are needed or and also at the same time we would like to improve performance of our applications. We can enable autoscaling because we can autoscale our workloads based on the actual demand. So the consumer application is consuming data and we would like to autoscale it because we just discussed that autoscaling is great, right? It's perfect tool and what it does it monitors CPU memory usage on the application and based on these metrics it scales out the application.

### Excerpt da transcript

Thanks everybody for joining us today in this session about KDA and how to unlock new visions and how to use KDA in production. First of all, I'm going to introduce myself. I'm Jorge Dorado. I work as principal SR at CRM the international half of SWARS group and I'm one of KDA maintainers. I'm also CNCF ambassador and Microsoft MVP and he is my employee. Nice. Introduce yourself. Thank you, Horge. Thank you. Great. So, Horge is done for for today and the rest of the talk is on me. So, my name is Beign. I know it's hard to pronounce and don't feel bad about it. U I'm also KA maintainer. Uh I'm with the project since the inception. So, uh already even it was before the CNCF donation. So, we together work with a couple of other folks on Ka. Um on on top of that, I'm also founder and CTO uh of Kifi. It's a company built around KDA and we provide enterprise autoscaling solutions uh around Kada for our customers. So let's talk about Ka today. This is the agenda we have. I hope we will be able to get it in time. So we will have some interaction, talk about some features, uh discuss best practices and some challenges that you can face with uh dealing with autoscaling.

So before we start uh may I ask uh the audience if you can raise your hand if you already use SCADA in production. Nice. It's like a more than half, right? Uh is there anybody who doesn't know what KDA is or maybe just heard the name but is not aware of the capabilities? Okay, we have bunch of folks and uh is there anybody who knows what KA is but doesn't use it would like to use it. Okay, perfect. So we have a coverage for all the stuff. Uh so let's start, right? So why do we need to use SCADA? Why do we need to use auto scaring? For the folks that already use SCADA, this will be repetition of the already known, but I would like to cover this kind of stuff in a in a short time. So why would we need autoscaling on our clusters? First, we would like to save resources because we would like to run only the workloads uh when they are needed or and also at the same time we would like to improve performance of our applications. How we can do that? We can enable autoscaling because we can autoscale our workloads based on the actual demand.

So let's take a look at this problem. We have a Kubernetes application. This application is consuming some data from some external source. It in this case it could be Rabbit MQ. So the consumer application is consuming data and we would like to autoscale it because we j
