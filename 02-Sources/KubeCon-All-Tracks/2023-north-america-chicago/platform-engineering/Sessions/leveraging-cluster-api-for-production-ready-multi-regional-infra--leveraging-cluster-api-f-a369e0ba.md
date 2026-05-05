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
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Shotaro Gotanda", "Kotaro Inoue", "LY Corporation"]
sched_url: https://kccncna2023.sched.com/event/1R2qI/leveraging-cluster-api-for-production-ready-multi-regional-infrastructures-shotaro-gotanda-kotaro-inoue-ly-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Leveraging+Cluster-API+for+Production-Ready+Multi-Regional+Infrastructures+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Leveraging Cluster-API for Production-Ready Multi-Regional Infrastructures - Shotaro Gotanda & Kotaro Inoue, LY Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Shotaro Gotanda, Kotaro Inoue, LY Corporation
- Schedule: https://kccncna2023.sched.com/event/1R2qI/leveraging-cluster-api-for-production-ready-multi-regional-infrastructures-shotaro-gotanda-kotaro-inoue-ly-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Leveraging+Cluster-API+for+Production-Ready+Multi-Regional+Infrastructures+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Leveraging Cluster-API for Production-Ready Multi-Regional Infrastructures.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qI/leveraging-cluster-api-for-production-ready-multi-regional-infrastructures-shotaro-gotanda-kotaro-inoue-ly-corporation
- YouTube search: https://www.youtube.com/results?search_query=Leveraging+Cluster-API+for+Production-Ready+Multi-Regional+Infrastructures+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BDjhGEVJ0Gs
- YouTube title: Leveraging Cluster-API for Production-Ready Multi-Regional Infrast... Shotaro Gotanda & Kotaro Inoue
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/leveraging-cluster-api-for-production-ready-multi-regional-infrastruct/BDjhGEVJ0Gs.txt
- Transcript chars: 24149
- Keywords: cluster, provider, clusters, legacy, provisioner, machine, platform, another, infrastructure, resources, migration, managed, custom, created, actually, create, question, private

### Resumo baseado na transcript

hi um thank you for being here today so uh we are going to talk about our recent work with cluster API my name is Karo I am a software engineer at ly Corporation and I'm sharo I'm also a sof engineer from ly Corporation yeah nice to meet you and these are today's topic first let us briefly introduce our company and services then let us introduce our platform and its scale line is a communication app that connects people services and information through various Services especially free messages is prepared in front QB ADM have to know every members of Managed IT C in based cluster it C members are managed as kuet static Port which can be seen from kubernetes API uh like this kubernetes I mean QB ADM list the ports with Filter component equals FCD and tier equals control pre by this QB ADM get theity member however our Legacy ET City members are managed just as doer containers independently from kubernetes API this cannot be seen from kuet API so we needed a way

### Excerpt da transcript

hi um thank you for being here today so uh we are going to talk about our recent work with cluster API my name is Karo I am a software engineer at ly Corporation and I'm sharo I'm also a sof engineer from ly Corporation yeah nice to meet you and these are today's topic first let us briefly introduce our company and services then let us introduce our platform and its scale line is a communication app that connects people services and information through various Services especially free messages voice and video calls line was launched in 2011 and we now have over 178 million users in a total of four major markets almost all of our services are running in our data center centers Verda is our private Cloud platform that helps line service developers build and run their services on our infrastructure our mission is to build a platform that enables uh infrastructure automation for both provisioning and operation Verda consists of infrastructures of service like VM or BTO platform other service and a set of managed Services just like the various public Cloud platforms um this is the service catalog of Vera now we have over 40 services in Verda and users can use them easily via the Verda dashboard Verda is built on top of the Sal service principle users can manage their resources uh via a graphical interface but also use API to operate Vera Services Verda is now becoming larger we have three regions over over 100,000 VMS and over 30,000 B machines in total our team provides one of the managed services in Verda called Verda kubernetes service bks is a managed kubernetes platform for better our service aims not only to just simplify the cluster life cycle but also to provide native integration of various corporate platforms to reduce engineering costs our team has seven members and we manage over 1,000 clusters in total okay then let's move on to the next section about the story of why we chose cluster API and how to adopt it with minimizing users effort as much as possible this is the overview our our Legacy system we have a cluster provisioner that that is responsible for bootstrapping kubernetes clusters and machines used by those clusters machines are turned into kubernetes nose by cluster provisioner via SSH Connections in front of the provisioner we have an API server to abstract basic operations for the cluster itself like creation and deletion since we launched bks we have faced several issues with our Legacy provisioner the first thing is the management of
