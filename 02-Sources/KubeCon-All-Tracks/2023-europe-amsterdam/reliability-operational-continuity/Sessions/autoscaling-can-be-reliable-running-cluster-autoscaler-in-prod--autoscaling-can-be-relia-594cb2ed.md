---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Maciej Pytel", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HycL/autoscaling-can-be-reliable-running-cluster-autoscaler-in-prod-maciej-pytel-google
youtube_search_url: https://www.youtube.com/results?search_query=Autoscaling+Can+Be+Reliable%3A+Running+Cluster+Autoscaler+in+Prod+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Autoscaling Can Be Reliable: Running Cluster Autoscaler in Prod - Maciej Pytel, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maciej Pytel, Google
- Schedule: https://kccnceu2023.sched.com/event/1HycL/autoscaling-can-be-reliable-running-cluster-autoscaler-in-prod-maciej-pytel-google
- Busca YouTube: https://www.youtube.com/results?search_query=Autoscaling+Can+Be+Reliable%3A+Running+Cluster+Autoscaler+in+Prod+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Autoscaling Can Be Reliable: Running Cluster Autoscaler in Prod.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HycL/autoscaling-can-be-reliable-running-cluster-autoscaler-in-prod-maciej-pytel-google
- YouTube search: https://www.youtube.com/results?search_query=Autoscaling+Can+Be+Reliable%3A+Running+Cluster+Autoscaler+in+Prod+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oBX0Duzc0SI
- YouTube title: Autoscaling Can Be Reliable: Running Cluster Autoscaler in Prod - Maciej Pytel, Google
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/autoscaling-can-be-reliable-running-cluster-autoscaler-in-prod/oBX0Duzc0SI.txt
- Transcript chars: 21818
- Keywords: cluster, autoscaler, issues, provider, pending, useful, number, scalar, however, logs, wanted, metrics, recommend, actually, already, metric, autoscale, common

### Resumo baseado na transcript

hi my name is Magic Patel and I'm a software engineer at Google I've been working on cluster autoscaler as part of the gke team and as a member of Open Source Community for slightly more than six years now and at gke I've been part of the team that is running a crushed autoscale in in thousands and thousands of clusters of our customers ranging from very small ones all the way to 15 000 note clusters and I wanted to share some of our experiences with you today

### Excerpt da transcript

hi my name is Magic Patel and I'm a software engineer at Google I've been working on cluster autoscaler as part of the gke team and as a member of Open Source Community for slightly more than six years now and at gke I've been part of the team that is running a crushed autoscale in in thousands and thousands of clusters of our customers ranging from very small ones all the way to 15 000 note clusters and I wanted to share some of our experiences with you today so in this talk I am going to focus on reliability aspect of planning cluster autoscaler I'm going to talk about metrics logs and other tools that I think are useful here I'm not going to focus too much on cost optimization and I'm also not going to Deep dive into how crust autoscaler Works internally I have done some deep Dives in the past and I recommend my recordings from past cubecons that they are on YouTube um so today I'm going to have three parts I'm going to start with a quick summary of how class Delta scale works and I'm going to only focus on the paths that I think that I think are relevant um from the perspective of understanding what can go wrong and maintaining it then I'm going to quickly discuss some of the tools tools like metrics or logs that I think are the most useful From perspective of monitoring and debugging cluster autoscaler and finally I'm going to try to illustrate some common issues and how the how those tools could be used to diagnose them so let's start and I want to start with a sort of quick let's say mission statement right so the problem I'm going to focus on in here is is the problem of making sure that all the pods can schedule I think this is really the primary job of cluster autoscale right if you don't have enough nodes in your cluster and the outputs cannot schedule when you want to run a badge job or it's traffic Spy Kids and then cluster Auto scale that just isn't doing its job and there is a problem that needs to be fixed and we're going to try to detect that problem and prevent it and so some key facts about how cluster autoscaler is achieving this first of all cluster autoscaler is actually reacting to pending pots so this is this is what triggers the outer scaling and whenever it sees those pending pots it's going to calculate how many VMS are needed to run those spots and it's going to go to cloud provider and request that those VMS are created however it's not really involved in starting those VMS in any way other than just triggering it it's not init
