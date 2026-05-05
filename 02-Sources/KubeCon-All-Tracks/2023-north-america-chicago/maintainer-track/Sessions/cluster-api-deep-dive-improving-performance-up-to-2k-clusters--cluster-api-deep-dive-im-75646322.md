---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Fabrizio Pandini", "Stefan Büringer", "VMware"]
sched_url: https://kccncna2023.sched.com/event/1R2py/cluster-api-deep-dive-improving-performance-up-to-2k-clusters-fabrizio-pandini-stefan-buringer-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Cluster+API+Deep+Dive%3A+Improving+Performance+up+to+2k+Clusters+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cluster API Deep Dive: Improving Performance up to 2k Clusters - Fabrizio Pandini & Stefan Büringer, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Fabrizio Pandini, Stefan Büringer, VMware
- Schedule: https://kccncna2023.sched.com/event/1R2py/cluster-api-deep-dive-improving-performance-up-to-2k-clusters-fabrizio-pandini-stefan-buringer-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Cluster+API+Deep+Dive%3A+Improving+Performance+up+to+2k+Clusters+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cluster API Deep Dive: Improving Performance up to 2k Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2py/cluster-api-deep-dive-improving-performance-up-to-2k-clusters-fabrizio-pandini-stefan-buringer-vmware
- YouTube search: https://www.youtube.com/results?search_query=Cluster+API+Deep+Dive%3A+Improving+Performance+up+to+2k+Clusters+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bRPfmviTi3s
- YouTube title: Cluster API Deep Dive: Improving Performance up to 2k Clusters - Fabrizio Pandini & Stefan Büringer
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cluster-api-deep-dive-improving-performance-up-to-2k-clusters/bRPfmviTi3s.txt
- Transcript chars: 31871
- Keywords: cluster, basically, controller, reconcile, essentially, metrics, client, actually, server, control, clusters, machine, performance, object, workers, create, running, number

### Resumo baseado na transcript

welcome everyone thank you for walking this long way to our talk and thank you for attending the talk uh late in in the day we know that the first day of kubon is yeah is challenging so today we um we talking about a cluster API Deep dive and we are talking about how we worked to improve the cluster API performance up to 2,000 clusters uh first let's introduce ourself I'm pandini I work at onew and I'm a see cluster life cycle Tech lead and a cluster

### Excerpt da transcript

welcome everyone thank you for walking this long way to our talk and thank you for attending the talk uh late in in the day we know that the first day of kubon is yeah is challenging so today we um we talking about a cluster API Deep dive and we are talking about how we worked to improve the cluster API performance up to 2,000 clusters uh first let's introduce ourself I'm pandini I work at onew and I'm a see cluster life cycle Tech lead and a cluster API maintainer yeah I'm St bu I also work work for y I'm CL contr maintainer good great uh before starting so um today what we're talking about is a work that we did uh for cluster API one uh 1.5.0 so it means more or less this summer and um what is interesting about this work is is that we are talking about um a series of con of concept or experience or lesser learning that not not only apply to clust thpi or clust thpi providers but can be useful for everyone developing controller on kubernetes um the presentation today is kind of dividing in two part the first part will be a very brief introduction on the tool that you need to do uh performance of scalability optimization the second part will be a deep dive on how we basically manage to scale cluster pii up to 2,000 clusters okay so let's get started so the first step is you have to get the right uh tools for the shop um we going relatively quickly over some of those so that we can focus on the more important parts later on so uh the first things you need is metrics uh profiling tracing and locks um ideally so we have like a priority list on the right side essentially so the first thing is definitely that you need metrics because otherwise you can measure anything um but what you also need is um Automation and what we mean with aut automation here is essentially that um you will have to run some sort of scale test and ideally you don't do it manually of course so you need um yeah automation for your scale test uh and if possible you should also use mock so in cluster API usually we we create clusters and machines and some real clouds and of course it's a lot better if you just use a mock because you don't don't actually have to pay for the infrastructure Etc so why do we need those tools so the first four metric profiling tracing and locks um we mostly need them to analyze performance um and to investigate bottlenecks uh the first two metrics in profiling they're more for getting like a rough overview or like a lot of reconciles just to get data like averag
