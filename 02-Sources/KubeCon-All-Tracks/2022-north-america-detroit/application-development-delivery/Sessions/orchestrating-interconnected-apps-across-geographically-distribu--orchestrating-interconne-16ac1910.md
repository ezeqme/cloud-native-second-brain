---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Application + Development + Delivery"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["John Belamaric", "Google"]
sched_url: https://kccncna2022.sched.com/event/182H0/orchestrating-interconnected-apps-across-geographically-distributed-kubernetes-clusters-john-belamaric-google
youtube_search_url: https://www.youtube.com/results?search_query=Orchestrating+Interconnected+Apps+Across+Geographically+Distributed+Kubernetes+Clusters+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Orchestrating Interconnected Apps Across Geographically Distributed Kubernetes Clusters - John Belamaric, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: John Belamaric, Google
- Schedule: https://kccncna2022.sched.com/event/182H0/orchestrating-interconnected-apps-across-geographically-distributed-kubernetes-clusters-john-belamaric-google
- Busca YouTube: https://www.youtube.com/results?search_query=Orchestrating+Interconnected+Apps+Across+Geographically+Distributed+Kubernetes+Clusters+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Orchestrating Interconnected Apps Across Geographically Distributed Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182H0/orchestrating-interconnected-apps-across-geographically-distributed-kubernetes-clusters-john-belamaric-google
- YouTube search: https://www.youtube.com/results?search_query=Orchestrating+Interconnected+Apps+Across+Geographically+Distributed+Kubernetes+Clusters+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ya1fUqAgvN8
- YouTube title: Orchestrating Interconnected Apps Across Geographically Distributed Kubernetes... - John Belamaric
- Match score: 0.969
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/orchestrating-interconnected-apps-across-geographically-distributed-ku/ya1fUqAgvN8.txt
- Transcript chars: 33127
- Keywords: configuration, little, clusters, workload, across, actually, cluster, package, management, deploy, particular, talked, address, platform, workloads, problems, single, config

### Resumo baseado na transcript

all right hello thank you everybody um welcome to Detroit this is kind of weird because I'm only looking at a few people and everybody's over there over there but I'll make the best of it I guess um so uh yeah I hope you're enjoying kubecon this year and uh let's get let's get started um my name is John Bel America I'm from Google Cloud um and I want you to um I want to set the stage a little bit um this is uh an image of

### Excerpt da transcript

all right hello thank you everybody um welcome to Detroit this is kind of weird because I'm only looking at a few people and everybody's over there over there but I'll make the best of it I guess um so uh yeah I hope you're enjoying kubecon this year and uh let's get let's get started um my name is John Bel America I'm from Google Cloud um and I want you to um I want to set the stage a little bit um this is uh an image of um many of Google Cloud's pops of various sorts but um it's not so important that it's Google Cloud just that you can see it's quite an array of of sites and you can imagine uh yourself being in a situation of needing to deploy a set of applications across this geographically distributed set of sites and um this isn't something we typically talk about here at kubecon at least we haven't over the last a few years actually I can take this off now the few years that we've been uh doing kubecon but it's becoming more and more common um you know it's for one it's it's exactly the type of scenario that you see faced by uh telcos who are trying to roll out 5G and um which often is built on kubernetes um but you know there's other use cases as well retail Edge uh where you have tens of thousands of of Stores um uh Factory Automation in fact there's enough demand for this that the various Cloud providers and others have been coming up with sort of new technologies they call multi-access Edge compute which is basically a rack you can drop in any sort of Pop anywhere on your own your own site your own data center your own location or in one of their pops and you wire it up to the cloud and you can use uh you can use your Cloud apis to to manage that compute resource out at the edge this is really really cool actually because one of the sort of great Revolutions of cloud is that you get this separation between um the capacity provisioning and the hardware provisioning of that capacity and the consumption so we have API on-demand driven consumption which means other people like Cloud providers can build that capacity and you can just you know rent it and consume it as you need it and so to be able to take that from just the data center to the edge and spread out across the world that same consumption model creates enormous opportunities for cloud providers and for our customers um as well as many many other people but what it does also that people don't really talk too much about is it creates an enormous and painful headache for managing the applicat
