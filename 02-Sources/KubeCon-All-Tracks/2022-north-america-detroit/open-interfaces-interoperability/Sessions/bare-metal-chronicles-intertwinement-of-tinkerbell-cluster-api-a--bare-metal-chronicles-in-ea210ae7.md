---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Open Interfaces + Interoperability"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Katie Gamanji", "Apple"]
sched_url: https://kccncna2022.sched.com/event/182In/bare-metal-chronicles-intertwinement-of-tinkerbell-cluster-api-and-gitops-katie-gamanji-apple
youtube_search_url: https://www.youtube.com/results?search_query=Bare-Metal+Chronicles%3A+Intertwinement+Of+Tinkerbell%2C+Cluster+API+And+GitOps+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Bare-Metal Chronicles: Intertwinement Of Tinkerbell, Cluster API And GitOps - Katie Gamanji, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Katie Gamanji, Apple
- Schedule: https://kccncna2022.sched.com/event/182In/bare-metal-chronicles-intertwinement-of-tinkerbell-cluster-api-and-gitops-katie-gamanji-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Bare-Metal+Chronicles%3A+Intertwinement+Of+Tinkerbell%2C+Cluster+API+And+GitOps+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Bare-Metal Chronicles: Intertwinement Of Tinkerbell, Cluster API And GitOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182In/bare-metal-chronicles-intertwinement-of-tinkerbell-cluster-api-and-gitops-katie-gamanji-apple
- YouTube search: https://www.youtube.com/results?search_query=Bare-Metal+Chronicles%3A+Intertwinement+Of+Tinkerbell%2C+Cluster+API+And+GitOps+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NCFUUjTw6hA
- YouTube title: Bare-Metal Chronicles: Intertwinement Of Tinkerbell, Cluster API And GitOps - Katie Gamanji, Apple
- Match score: 0.96
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/bare-metal-chronicles-intertwinement-of-tinkerbell-cluster-api-and-git/NCFUUjTw6hA.txt
- Transcript chars: 36182
- Keywords: cluster, infrastructure, tinkerbell, deploy, however, provider, management, actually, pretty, machine, introduce, resource, control, clusters, changes, target, githubs, already

### Resumo baseado na transcript

hello everyone my name is Katie gamanji and currently I am a senior field engineer at Apple I have joined this role last year and in my role I'm trying to bring Cloud native and kubernetes expertise to different teams and products within apple as well I am one of the TOC or technical oversight Committee Member for cncf or Cloud native Computing foundation in this role I'm joining 10 other Champions within the industry and we try to provide a perspective and a tier of how to navigate the

### Excerpt da transcript

hello everyone my name is Katie gamanji and currently I am a senior field engineer at Apple I have joined this role last year and in my role I'm trying to bring Cloud native and kubernetes expertise to different teams and products within apple as well I am one of the TOC or technical oversight Committee Member for cncf or Cloud native Computing foundation in this role I'm joining 10 other Champions within the industry and we try to provide a perspective and a tier of how to navigate the landscape I have many other roles in the community one of them being an Advisory Board member for Captain which currently is an incubating cncf project and I am the creator of the cloud native fundamentals course which you can find on Udacity now this is a free course so completely selfless here however if you know anyone would be interested in pursuing a cloud native career I would definitely recommend to look at this course for them to navigate and understand the bus the fundamentals but to apply them in production as well now today however I would like to talk about Cloud bare metal Chronicles and more importantly the intertwine between cluster API Tinkerbell and githubs and to do so I would like to firstly introduce cluster API and how it provides one set of Standards to deployer infrastructure to any cloud provider next I'm going to focus on bare metal provisioning and here's what I'm going to introduce Tinkerbell but more importantly I'm going to focus on the Coalition between Tinkerbell and cluster API which is going to result with kpt or class JPI provider for Tinkerbell and lastly just to sprinkle it up a bit I'm going to introduce some githubs into the architecture that I'm going to show so pretty much when we deal with cluster provisioning we're never going to have one cluster we have to manage multiple clusters and we need to introduce automation to ensure a sustainable deployment of our infrastructure now Bobby show hands how many of you are familiar with cluster API just make sure that I introduce the fundamentals right cool action that's a very big show of hands how many of you are familiar with Tinkerbell and not the character okay some of you good and how many of you are using githubs or have heard about githubs at the moment okay that's good too and another question which is going to be very relevant how many of you do have a need for bare metal provisioning or are deploying the infrastructure infrastructure to Bare Metal okay that's actually a very short
