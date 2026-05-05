---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Niko Smeds", "Grafana Labs"]
sched_url: https://kccnceu2022.sched.com/event/ytsi/kubernetes-everywhere-lessons-learned-from-going-multi-cloud-niko-smeds-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Everywhere%3A+Lessons+Learned+From+Going+Multi-Cloud+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes Everywhere: Lessons Learned From Going Multi-Cloud - Niko Smeds, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Niko Smeds, Grafana Labs
- Schedule: https://kccnceu2022.sched.com/event/ytsi/kubernetes-everywhere-lessons-learned-from-going-multi-cloud-niko-smeds-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Everywhere%3A+Lessons+Learned+From+Going+Multi-Cloud+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes Everywhere: Lessons Learned From Going Multi-Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytsi/kubernetes-everywhere-lessons-learned-from-going-multi-cloud-niko-smeds-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Everywhere%3A+Lessons+Learned+From+Going+Multi-Cloud+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZY5h8Atc14A
- YouTube title: Kubernetes Everywhere: Lessons Learned From Going Multi-Cloud - Niko Smeds, Grafana Labs
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-everywhere-lessons-learned-from-going-multi-cloud/ZY5h8Atc14A.txt
- Transcript chars: 24621
- Keywords: provider, providers, grafana, clusters, running, cluster, multiple, actually, managed, product, workloads, applications, number, regions, started, volumes, issues, products

### Resumo baseado na transcript

hello everybody thank you for joining i want to start by asking how many of you run kubernetes on at least one cloud provider pretty much everyone how many of you run kubernetes on two or more cloud providers probably like half the room so we're here to talk about going multi-cloud you've got one and you want another for those of you expanding to multiple providers i'm going to share some of our experiences on a recent project and the goal is to give you an idea of what region whereas aws the load balancers are all regional resources if we look at volumes so network attached volumes persistent volumes the prices and performance will differ slightly between provider and then finally object storage at grafana cloud we have three products mimir loki and tempo that use object storage as their primary data store it means that we read and write a lot to the gcs and s3 buckets and it turns out that these cloud providers actually rate limit access to object storage but based on different conditions

### Excerpt da transcript

hello everybody thank you for joining i want to start by asking how many of you run kubernetes on at least one cloud provider pretty much everyone how many of you run kubernetes on two or more cloud providers probably like half the room so we're here to talk about going multi-cloud you've got one and you want another for those of you expanding to multiple providers i'm going to share some of our experiences on a recent project and the goal is to give you an idea of what was required and what to watch out for for those of you already on multiple clouds i'm curious if you can relate to some of these experiences if you have different issues run into or suggestions i'd be interested to chat after the talk my name is nico i'm a sre on grafana's cloud platform team if you're not familiar with grafana we're an open source observability platform on top of the grafana dashboarding system we offer a number of cloud products things like hosted grafana grafana cloud metrics logs and traces incident management incident management on-call tools black stocks black box monitoring and more the platform team that i'm on manages the cloud infrastructure that all these products run on so we're looking after the kubernetes clusters internal monitoring systems ci cd and other internal tools and we're going to start by asking why you might opt for multi-cloud like why would any company consider doing this in the first place we'll go through an overview of a recent cloud expansion project at grafana walk through some of the hiccups in this project and look for the lessons we can learn we'll also review what went well and at the end there'll be time for any questions so let's start by asking why do this in the first place there are a number of reasons but i'll just touch on a few obvious one is you gain more regions right if you think of any cloud provider they have like a list of available regions you can deploy to and between multiple providers there's lots of over there's lots of overlap but there's a lot of unique locations as well and we have a use case for this at grafana we have a synthetic monitoring product which allows customers to deploy like health probes at different locations around the world think things like icmp or http health checks and to support specific locations we have to deploy this product across multiple providers there's also vendor lock-in if you run your internal services or customer facing products across multiple clouds you now have the freedom to ki
