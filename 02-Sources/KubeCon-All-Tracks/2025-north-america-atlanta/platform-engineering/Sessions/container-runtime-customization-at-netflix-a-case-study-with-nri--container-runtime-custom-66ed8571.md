---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Runtime Containers"]
speakers: ["Erikson Tung", "Netflix"]
sched_url: https://kccncna2025.sched.com/event/27Fbb/container-runtime-customization-at-netflix-a-case-study-with-nri-and-oci-hooks-erikson-tung-netflix
youtube_search_url: https://www.youtube.com/results?search_query=Container+Runtime+Customization+at+Netflix%3A+A+Case+Study+With+NRI+and+OCI+Hooks+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Container Runtime Customization at Netflix: A Case Study With NRI and OCI Hooks - Erikson Tung, Netflix

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Runtime Containers]]
- País/cidade: United States / Atlanta
- Speakers: Erikson Tung, Netflix
- Schedule: https://kccncna2025.sched.com/event/27Fbb/container-runtime-customization-at-netflix-a-case-study-with-nri-and-oci-hooks-erikson-tung-netflix
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Runtime+Customization+at+Netflix%3A+A+Case+Study+With+NRI+and+OCI+Hooks+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Container Runtime Customization at Netflix: A Case Study With NRI and OCI Hooks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fbb/container-runtime-customization-at-netflix-a-case-study-with-nri-and-oci-hooks-erikson-tung-netflix
- YouTube search: https://www.youtube.com/results?search_query=Container+Runtime+Customization+at+Netflix%3A+A+Case+Study+With+NRI+and+OCI+Hooks+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IPbamReWdss
- YouTube title: Container Runtime Customization at Netflix: A Case Study With NRI and OCI Hooks - Erikson Tung
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/container-runtime-customization-at-netflix-a-case-study-with-nri-and-o/IPbamReWdss.txt
- Transcript chars: 29504
- Keywords: runtime, container, actually, platform, workloads, systemd, workload, extensions, running, containers, netflix, extension, custom, migration, requirements, implementation, existing, events

### Resumo baseado na transcript

Um, and there were many interesting talks in the time slot, so I really appreciate you being here. And today I'll be talking to you about container runtime customizations at Netflix. And lastly, I hope to share some key learnings and takeaways from our modernization projects. Uh originally it was conceived in the early days of cloud native uh before Kubernetes was kind becoming more mainstream. Uh originally built on patch messos and when kubernetes became more dominant uh we swapped out the underlying control plane with kubernetes but critically uh during that time we decided to leave the data plane implementation intact. We also have data pipeline jobs and more recently uh more relevant today we have a lot of machine learning workloads uh that powers our recommendation systems.

### Excerpt da transcript

Hello everyone. Uh, thank you for being here today. I know it's been a long day. Um, and there were many interesting talks in the time slot, so I really appreciate you being here. Um, hope you've enjoying your time at CubeCon. My name is Erikson and I work on the computer runtime team at Netflix. And today I'll be talking to you about container runtime customizations at Netflix. Uh in terms of the gist, uh I'll be sharing how we use runtime extensions such as the node resource interface plugins and OCI hooks to handle some of the unique platform requirements of Netflix's compute platform, Titus. Okay, so here's the agenda of what I'll be going over today. Uh I'll start off by describing a problem we faced around the same time last year around this time where we were trying to migrate years of accumulated custom runtime uh code to a more standard Kubernetes data play implementation consisting of standard tooling like stock cublets and containerd. Then I'll kind of share some uh our guiding principles, philosophies, and strategies for kind of migrating user workloads to this new modern stack and how that kind of influence our implementation.

Next, I'll kind of go into detail of the runtime extensions we leveraged, chiefly the NRI plugins and OCI hooks. Then I'll give some concrete use case examples. uh think for things such as CPU isolation, trying to run systemd in a container and trying to uh control the workload life cycle. Then I'll share some uh experience of us running these runtime extensions at scale in production and some of the challenges we faced. And lastly, I hope to share some key learnings and takeaways from our modernization projects. And hopefully by the end of the talk, I'll have some time for questions. By the end of this talk, I hope you'll walk away uh with ideas on how to handle your own unique platform requirements using these runtime extensions. There's no need to for Kubernetes or rewrite your workloads. Uh there are tools available for you to to achieve what you need to do. So let me start off with some context. Uh you might have seen this slide in some of our uh previous presentations from Netflix. Um so what is Titus?

Uh Titus is Netflix's container platform. It's been running production workloads for almost nearly a decade. Uh originally it was conceived in the early days of cloud native uh before Kubernetes was kind becoming more mainstream. Uh originally built on patch messos and when kubernetes became more dominant uh we swa
