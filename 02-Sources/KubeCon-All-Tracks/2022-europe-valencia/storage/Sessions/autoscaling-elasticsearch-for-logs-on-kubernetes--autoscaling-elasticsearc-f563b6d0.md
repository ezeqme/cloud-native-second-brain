---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Storage"
themes: ["Observability", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Radu Gheorghe", "Sematext Group", "Ciprian Hacman", "polypoly"]
sched_url: https://kccnceu2022.sched.com/event/ytoD/autoscaling-elasticsearch-for-logs-on-kubernetes-radu-gheorghe-sematext-group-ciprian-hacman-polypoly
youtube_search_url: https://www.youtube.com/results?search_query=Autoscaling+Elasticsearch+for+Logs+on+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Autoscaling Elasticsearch for Logs on Kubernetes - Radu Gheorghe, Sematext Group & Ciprian Hacman, polypoly

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Storage]]
- Temas: [[Observability]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Radu Gheorghe, Sematext Group, Ciprian Hacman, polypoly
- Schedule: https://kccnceu2022.sched.com/event/ytoD/autoscaling-elasticsearch-for-logs-on-kubernetes-radu-gheorghe-sematext-group-ciprian-hacman-polypoly
- Busca YouTube: https://www.youtube.com/results?search_query=Autoscaling+Elasticsearch+for+Logs+on+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Autoscaling Elasticsearch for Logs on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoD/autoscaling-elasticsearch-for-logs-on-kubernetes-radu-gheorghe-sematext-group-ciprian-hacman-polypoly
- YouTube search: https://www.youtube.com/results?search_query=Autoscaling+Elasticsearch+for+Logs+on+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ONGqk3xXRTw
- YouTube title: Autoscaling Elasticsearch for Logs on Kubernetes - Radu Gheorghe & Ciprian Hacman
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/autoscaling-elasticsearch-for-logs-on-kubernetes/ONGqk3xXRTw.txt
- Transcript chars: 22606
- Keywords: cluster, scaling, elasticsearch, indices, operator, search, shards, template, logs, indexing, already, searches, replicas, pretty, typically, create, policy, percent

### Resumo baseado na transcript

hello and welcome in this session we're going to talk about elasticsearch or open search we're going to use the terms interchangeably for the most part we're going to talk about them in the context of logs and other time series data and we'll focus on using a kubernetes operator to manage elasticsearch clusters in this context but before we start let us introduce ourselves i'm radu i'm a search person at sematext and most of my time goes into consulting production support and training for elasticsearch open search and

### Excerpt da transcript

hello and welcome in this session we're going to talk about elasticsearch or open search we're going to use the terms interchangeably for the most part we're going to talk about them in the context of logs and other time series data and we'll focus on using a kubernetes operator to manage elasticsearch clusters in this context but before we start let us introduce ourselves i'm radu i'm a search person at sematext and most of my time goes into consulting production support and training for elasticsearch open search and solar and sometimes i contribute to our observability platform which is called semitex cloud okay hi my name is chiprian i'm a consultant for kubernetes and automation and also work as a software engineer for poly poly mostly on privacy related projects also in my spare time i'm an open source maintainer contributing to many of the projects in the kubernetes ecosystem so let's start with the agenda we'll talk about why we want to have such such an operator so the use cases we will talk about how how it should work when should it scale up and down and what should we do when it does that and available options and last a quick demo of our proof of concept let's start with the why if you have a small cluster then you don't want to think about elastic search to learn all about it the ins and outs and you would like to have as less maintenance as possible so ideally zero maintenance this kind of operator would help you get started with your logging without caring about learning elasticsearch too much for bigger clusters usually these clusters are multi-tenant and you you could split them easier because it's not such a big maintenance to have multiple clusters if you have the operator all right moving on to how so in other words what does the operator need to do in order to auto scale um in order to get there i want to talk about three things so one is using time-based indices so if you use for example logstash before you might have noticed that it creates one index per day um we're going to talk about why that's a good idea next i'm going to argue that for most use cases rotating by size instead of by time will work better and the third thing would be how would those indices behave when you scale your cluster up and down so let's start with with time-based indices you know they don't have to be daily you can have like one index per month or one index per hour but the idea is the same and the advantages are pretty big so when it comes to indexing ty
