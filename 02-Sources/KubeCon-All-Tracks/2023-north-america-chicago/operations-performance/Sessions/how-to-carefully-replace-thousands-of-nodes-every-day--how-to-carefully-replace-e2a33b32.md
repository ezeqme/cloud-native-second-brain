---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Adrien Trouillaud", "Ryan McNamara", "Datadog"]
sched_url: https://kccncna2023.sched.com/event/1R2qP/how-to-carefully-replace-thousands-of-nodes-every-day-adrien-trouillaud-ryan-mcnamara-datadog
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Carefully+Replace+Thousands+of+Nodes+Every+Day+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How to Carefully Replace Thousands of Nodes Every Day - Adrien Trouillaud & Ryan McNamara, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Adrien Trouillaud, Ryan McNamara, Datadog
- Schedule: https://kccncna2023.sched.com/event/1R2qP/how-to-carefully-replace-thousands-of-nodes-every-day-adrien-trouillaud-ryan-mcnamara-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Carefully+Replace+Thousands+of+Nodes+Every+Day+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How to Carefully Replace Thousands of Nodes Every Day.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qP/how-to-carefully-replace-thousands-of-nodes-every-day-adrien-trouillaud-ryan-mcnamara-datadog
- YouTube search: https://www.youtube.com/results?search_query=How+to+Carefully+Replace+Thousands+of+Nodes+Every+Day+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KQ1obaC-ht0
- YouTube title: How to Carefully Replace Thousands of Nodes Every Day - Adrien Trouillaud & Ryan McNamara, Datadog
- Match score: 0.806
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-to-carefully-replace-thousands-of-nodes-every-day/KQ1obaC-ht0.txt
- Transcript chars: 37061
- Keywords: eviction, controller, actually, disruption, delete, default, readiness, deletion, replace, running, solution, create, basically, unavailable, deployment, pressure, cluster, budgets

### Resumo baseado na transcript

hi everyone welcome to this uh talk on how to carefully replace thousands of nodes every day my name is Adrien Tuyo I'm an engineering manager at data dog I lead the compute node life cycle team and today I have the uh pleasure to be speaking with Ryan Hey folks I'm Ryan mcnamer I'm an engineer at data dog with uh same team as Adrien and I've been doing kubernetes things for a few years now data dog is an observability company every hour we ingest trillions of data

### Excerpt da transcript

hi everyone welcome to this uh talk on how to carefully replace thousands of nodes every day my name is Adrien Tuyo I'm an engineering manager at data dog I lead the compute node life cycle team and today I have the uh pleasure to be speaking with Ryan Hey folks I'm Ryan mcnamer I'm an engineer at data dog with uh same team as Adrien and I've been doing kubernetes things for a few years now data dog is an observability company every hour we ingest trillions of data points from our customers applications and infrastructure to process those data points uh we uh run hundreds of thousands of kubernetes pods on tens of thousands of notes in many clusters and to meet our customers where they are we run on multiple clouds also to uh better control the performance and reliability of our platform and as consistently as possible across Cloud providers we run cities from scratch part of our duties as cluster operators is to replace nodes when needed and at all scale this happens thousands of times a day uh and we do that without breaking applications if you use a manage distribution you may not fully control when noes need to be replaced uh but you are responsible for protecting your workloads when that happens so today we'll first explain why nodes need to be replaced how it's done generally uh and more specifically at data dog uh you'll learn about some of the strategies that we use to protect our workloads when we replace nodes and we uh we hope to uh start a conversation on turning some of those strategies into uh kubernetes enhancements so there are many reasons to replace notes when we uh started running kubernetes we needed a solution uh to uh first quickly react to Hardware failures like bad memory failing discs at our scale that's not so rare um and they don't necessarily break the nodes completely uh but they have negative impact on performance so we need to do something about it we also wanted to anticipate VM retirements uh that's when the cloud provider reclaims your virtual machines um and uh yeah we don't want those to uh come as a surprise uh but these days the main use Case by far of the solution that we built is to upgrade machine images uh we do that for kubernetes upgrades and also for operating system security security patches as you may have seen this morning uh in a a keynote presentation by my colleagues hant and lauron uh we had a good reason to disable unattended upgrades uh and we uh exclusively rely on node replacement for operating system
