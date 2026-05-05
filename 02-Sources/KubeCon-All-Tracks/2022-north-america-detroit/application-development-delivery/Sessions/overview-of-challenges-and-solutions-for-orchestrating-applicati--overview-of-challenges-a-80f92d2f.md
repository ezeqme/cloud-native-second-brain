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
speakers: ["Ritu Sood", "Cathy Zhang", "Intel Corp"]
sched_url: https://kccncna2022.sched.com/event/182Gr/overview-of-challenges-and-solutions-for-orchestrating-applications-to-multiple-dc-and-edge-clusters-ritu-sood-cathy-zhang-intel-corp
youtube_search_url: https://www.youtube.com/results?search_query=Overview+Of+Challenges+And+Solutions+For+Orchestrating+Applications+To+Multiple+DC+And+Edge+Clusters+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Overview Of Challenges And Solutions For Orchestrating Applications To Multiple DC And Edge Clusters - Ritu Sood & Cathy Zhang, Intel Corp

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Ritu Sood, Cathy Zhang, Intel Corp
- Schedule: https://kccncna2022.sched.com/event/182Gr/overview-of-challenges-and-solutions-for-orchestrating-applications-to-multiple-dc-and-edge-clusters-ritu-sood-cathy-zhang-intel-corp
- Busca YouTube: https://www.youtube.com/results?search_query=Overview+Of+Challenges+And+Solutions+For+Orchestrating+Applications+To+Multiple+DC+And+Edge+Clusters+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Overview Of Challenges And Solutions For Orchestrating Applications To Multiple DC And Edge Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Gr/overview-of-challenges-and-solutions-for-orchestrating-applications-to-multiple-dc-and-edge-clusters-ritu-sood-cathy-zhang-intel-corp
- YouTube search: https://www.youtube.com/results?search_query=Overview+Of+Challenges+And+Solutions+For+Orchestrating+Applications+To+Multiple+DC+And+Edge+Clusters+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ic88CjUTOv0
- YouTube title: Overview Of Challenges And Solutions For Orchestrating Applications To... - Ritu Sood & Cathy Zhang
- Match score: 0.882
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/overview-of-challenges-and-solutions-for-orchestrating-applications-to/ic88CjUTOv0.txt
- Transcript chars: 20465
- Keywords: clusters, cluster, application, microservices, deployed, orchestrator, requirements, applications, across, microservice, multiple, computing, require, policies, argo, challenges, another, network

### Resumo baseado na transcript

hello everyone welcome to work to our session on challenges and solutions for orchestrating applications to multiple data center and age clusters my name is Kathy Zhang I'm a senior principal engineer at Intel leading the company-wide contributions to the cloud native Computing Foundation I have over you 10 years of experience in the Cloud area I co-authored several cncf white paper and specifications I was recently elected to the CSF technical oversight committee along with me is written yeah Ritu want to introduce yourself hello everyone my name is

### Excerpt da transcript

hello everyone welcome to work to our session on challenges and solutions for orchestrating applications to multiple data center and age clusters my name is Kathy Zhang I'm a senior principal engineer at Intel leading the company-wide contributions to the cloud native Computing Foundation I have over you 10 years of experience in the Cloud area I co-authored several cncf white paper and specifications I was recently elected to the CSF technical oversight committee along with me is written yeah Ritu want to introduce yourself hello everyone my name is Ritu suit I'm A Cloud engineer slash architect working at Intel and I've been working in the Cloud area for over uh last seven years and I have contributed to a few of the open source projects related to Cloud covered in today's presentation and first we will touch a little bit on the current industry trend on geo-distributed Computing and multi-cloud then we will go through several use cases after that we will talk about the requirements and challenges to support multi-cloud last we will Deep dive into some existing Solutions sharing their architecture and functionality as well as analyzing their pros and cons the industry is moving from a centralized cloud computing model to a distributed to a geodistributed cloud computing model with many workloads running under age clusters there are several drivers behind the geodesic Geo distributed computing Trend one is the need for low latency response time which requires the application to run closer to the to its data sources another is a need to reduce the bandwidth costs associated with information passing between the public cloud data center and the Aged device and to avoid the network bandwidth caused a network congestion more and more applications run locally at the age sites in addition some legal and privacy considerations also require the applications to not leave a Enterprise permits as showing the right diagram it is now very common for very common to have some applications that require a lot of computing resources to run in the public cloud while having other applications that are latency sensitive or privacy sensitive run at the age site and dedicated network channels can be set up between public cloud and age cloud and this slide shows the three use cases for geodetributed computing of course there are many other use cases the first one is a 5G use case in the 5G scenario there are tens of thousands of distributed 5G units that need to run at the age si
