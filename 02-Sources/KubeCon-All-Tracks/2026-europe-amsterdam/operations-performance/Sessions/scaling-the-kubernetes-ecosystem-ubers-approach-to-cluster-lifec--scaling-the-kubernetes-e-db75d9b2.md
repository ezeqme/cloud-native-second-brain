---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Silvio Simunic", "Vadim Plakhtinskii", "Uber"]
sched_url: https://kccnceu2026.sched.com/event/2CW6h/scaling-the-kubernetes-ecosystem-ubers-approach-to-cluster-lifecycle-management-silvio-simunic-vadim-plakhtinskii-uber
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+the+Kubernetes+Ecosystem%3A+Uber%27s+Approach+to+Cluster+Lifecycle+Management+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Scaling the Kubernetes Ecosystem: Uber's Approach to Cluster Lifecycle Management - Silvio Simunic & Vadim Plakhtinskii, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Silvio Simunic, Vadim Plakhtinskii, Uber
- Schedule: https://kccnceu2026.sched.com/event/2CW6h/scaling-the-kubernetes-ecosystem-ubers-approach-to-cluster-lifecycle-management-silvio-simunic-vadim-plakhtinskii-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+the+Kubernetes+Ecosystem%3A+Uber%27s+Approach+to+Cluster+Lifecycle+Management+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Scaling the Kubernetes Ecosystem: Uber's Approach to Cluster Lifecycle Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6h/scaling-the-kubernetes-ecosystem-ubers-approach-to-cluster-lifecycle-management-silvio-simunic-vadim-plakhtinskii-uber
- YouTube search: https://www.youtube.com/results?search_query=Scaling+the+Kubernetes+Ecosystem%3A+Uber%27s+Approach+to+Cluster+Lifecycle+Management+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=neexk5RZoyw
- YouTube title: Scaling the Kubernetes Ecosystem: Uber's Approach to Cluster... Silvio Simunic & Vadim Plakhtinskii
- Match score: 0.84
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/scaling-the-kubernetes-ecosystem-ubers-approach-to-cluster-lifecycle-m/neexk5RZoyw.txt
- Transcript chars: 34648
- Keywords: cluster, actually, clusters, configuration, production, change, controllers, create, workloads, another, operator, source, provide, already, course, provisioning, process, everything

### Resumo baseado na transcript

Hello everyone, my name is Vadim and today with my colleague Sylvia, we're going to present you how we actually manage cluster tuber. Yesterday I was thinking why it's actually interesting for you right because Uber have a really big scale and not many company run on this scale but I think the idea that we first of all of course want to share you like what we're So our team is compute and what we do in Uber we uh responsible for control plane right for all native uh controllers which we running native companies which you run there how we deploy them how we scale them also we we responsible how stateful workloads there and we have a lot of custom things how to do it properly on our big number scale. So after we see this all these problems, we came up with ideas how we actually can solve all of this right. uh different point of our stack for example if your cluster is not fully active you don't want to get obserability you don't want to get alerts right if something doesn't work because it's still process so We have this all dimension and then we

### Excerpt da transcript

Hello everyone, my name is Vadim and today with my colleague Sylvia, we're going to present you how we actually manage cluster tuber. Yesterday I was thinking why it's actually interesting for you right because Uber have a really big scale and not many company run on this scale but I think the idea that we first of all of course want to share you like what we're doing there and like kind of show you our infrastructure and also we want to tell you that some problems which you can face can be super simple for you to solve but if you go in Uber scale it's actually really hard and we go through the different ideas uh we have a different problem there and we want to share what we figure out. Let's start and understand what this cluster life cycle is. So imagine you want to run different workload stateless stateful right you need kubernetes cluster where you're going to run all all of them and your cluster during its life go different stages first it start to be turn up then it's active and during active phase you can change your cluster setup differently right maybe you want to apply new controllers or you want to change node type which you run there and if your cluster is not really lucky it can be decommissioned at the U let's I want to tell you about one story imagine we have developer let's give him a name also Vadim I like this name and Vadim really want to run new batch workloads at Uber because he think it's really cool and it will give him really good promo so why not and then what happened next right he needs create cluster for testing for example only one cluster to just test his ideas and show the boss that oh looks Actually it's really working really well and many many years ago at Uber how it look like I think it's around one year ago actually uh Vadim will go to the 15 or maybe even more steps first he need to get capacity for his cluster right because it's like should be like out of nodes and stuff then he will deploy control planes there he needs to take care how it's going to run where it's going to run then he needs to apply configuration on his cluster of course somewhere it doesn't work well and he needs to repeat it again and again and it's super painful but at the end after several weeks he'll get his cluster actually where everything going to run but Vim is super unhappy because imagine to just to try some stuff it's require you like two or three weeks of manual work and it's actually really really not good I would say so let me tell you
