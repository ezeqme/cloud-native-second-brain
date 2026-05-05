---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Aditya Bhave", "Apoorva Jindal", "Uber Technologies"]
sched_url: https://kccncna2023.sched.com/event/1R2qt/on-the-right-tack-kubernetes-at-uber-scale-aditya-bhave-apoorva-jindal-uber-technologies
youtube_search_url: https://www.youtube.com/results?search_query=On+the+Right+Tack%3A+Kubernetes+at+Uber+Scale+CNCF+KubeCon+2023
slides: []
status: parsed
---

# On the Right Tack: Kubernetes at Uber Scale - Aditya Bhave & Apoorva Jindal, Uber Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Aditya Bhave, Apoorva Jindal, Uber Technologies
- Schedule: https://kccncna2023.sched.com/event/1R2qt/on-the-right-tack-kubernetes-at-uber-scale-aditya-bhave-apoorva-jindal-uber-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=On+the+Right+Tack%3A+Kubernetes+at+Uber+Scale+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre On the Right Tack: Kubernetes at Uber Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qt/on-the-right-tack-kubernetes-at-uber-scale-aditya-bhave-apoorva-jindal-uber-technologies
- YouTube search: https://www.youtube.com/results?search_query=On+the+Right+Tack%3A+Kubernetes+at+Uber+Scale+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JxNysEES308
- YouTube title: On the Right Tack: Kubernetes at Uber Scale - Aditya Bhave & Apoorva Jindal, Uber Technologies
- Match score: 0.726
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/on-the-right-tack-kubernetes-at-uber-scale/JxNysEES308.txt
- Transcript chars: 30308
- Keywords: migration, cluster, container, platform, actually, deployment, clusters, developers, issues, updates, features, control, workloads, numerous, transparent, controller, support, changes

### Resumo baseado na transcript

thank you all for your interest in our work I'm Aur and this is Aditya we work in the compute platform team at Uber and today we are going to talk about our ongoing migration to kubernetes here is a brief summary of what we are going to talk about first we will introduce the compute platform team at Uber and what we work on then we will briefly capture the current status of our migration then we want to take this opportunity to give credit where it to you

### Excerpt da transcript

thank you all for your interest in our work I'm Aur and this is Aditya we work in the compute platform team at Uber and today we are going to talk about our ongoing migration to kubernetes here is a brief summary of what we are going to talk about first we will introduce the compute platform team at Uber and what we work on then we will briefly capture the current status of our migration then we want to take this opportunity to give credit where it to you with the community and talk about the unique features which we heavily use and have found to work really well without requiring any changes next we talk about a few features and customizations we Implement on top of kubernetes um why we Implement them so as to make it better suited for Uber's needs and finally we talk about some of the interesting uh learnings we had during the course of the migration first let me introduce the compute platform team at Uber today Uber manages its own on-prem data center as well as leverages capacity from Oracle and Google Cloud these providers are abstracted away from the platforms via layer we call crane which essentially implements host as a service it ingests capacity from these providers Provisions the host and the VMS with the right OS the Right image installs the right set of packages and essentially makes the node ready for use by platforms above crane we have the container orchestration layer which essentially provides container as a service to the rest of the company today this layer is built on top of misos and pettin where peltin is a custom framework on misos and we are in the process of migrating this layer to kubernetes this layer is or this platform is is used to run all the stateless microservices at Uber including the ones which run on shared infrastructure the ones which required its own dedicated infrastructure to run as well as lowlevel infrastructure Services which are required to boot up the rest of the infrastructure a number of batch workloads are also run on this platform including all machine learning workloads all Jupiter notebook sessions and a subset of spark workloads the spark workloads which run on this platform are the ones which don't run on Yan very well due to numerous reasons like requiring large containers or requiring customized features like gang scheding or custom Docker images Etc this talk is primarily going to focus on the stateless side of things we have another talk at 325 by Amit and Kevin uh which will talk about the bad sid
