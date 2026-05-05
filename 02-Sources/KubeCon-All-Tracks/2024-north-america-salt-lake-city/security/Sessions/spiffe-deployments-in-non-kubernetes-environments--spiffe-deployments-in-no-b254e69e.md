---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Nadin El-Yabroudi", "Eli Nesterov", "SPIRL"]
sched_url: https://kccncna2024.sched.com/event/1i7rW/spiffe-deployments-in-non-kubernetes-environments-nadin-el-yabroudi-eli-nesterov-spirl
youtube_search_url: https://www.youtube.com/results?search_query=SPIFFE+Deployments+in+Non-Kubernetes+Environments+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SPIFFE Deployments in Non-Kubernetes Environments - Nadin El-Yabroudi & Eli Nesterov, SPIRL

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Nadin El-Yabroudi, Eli Nesterov, SPIRL
- Schedule: https://kccncna2024.sched.com/event/1i7rW/spiffe-deployments-in-non-kubernetes-environments-nadin-el-yabroudi-eli-nesterov-spirl
- Busca YouTube: https://www.youtube.com/results?search_query=SPIFFE+Deployments+in+Non-Kubernetes+Environments+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SPIFFE Deployments in Non-Kubernetes Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rW/spiffe-deployments-in-non-kubernetes-environments-nadin-el-yabroudi-eli-nesterov-spirl
- YouTube search: https://www.youtube.com/results?search_query=SPIFFE+Deployments+in+Non-Kubernetes+Environments+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sflwuM_baG4
- YouTube title: SPIFFE Deployments in Non-Kubernetes Environments - Nadin El-Yabroudi & Eli Nesterov, SPIRL
- Match score: 0.806
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/spiffe-deployments-in-non-kubernetes-environments/sflwuM_baG4.txt
- Transcript chars: 29398
- Keywords: spiffy, workload, identity, workloads, running, information, implementation, structure, systems, domain, identifiers, question, basically, systemd, server, software, security, everyone

### Resumo baseado na transcript

doors doors are closed I don't know folks we all dropped in here for the next 25 30ish minutes trying to be I'll try to [Music] be quick I don't want to hold or stay in between all of you and Friday drinks but thank you thank you all for coming for the I guess the last Talk of the day uh and the last talk of this cubec Con on Friday Friday night almost and today we're going to talk about uh spify deployments in non kubernetes environments I

### Excerpt da transcript

doors doors are closed I don't know folks we all dropped in here for the next 25 30ish minutes trying to be I'll try to [Music] be quick I don't want to hold or stay in between all of you and Friday drinks but thank you thank you all for coming for the I guess the last Talk of the day uh and the last talk of this cubec Con on Friday Friday night almost and today we're going to talk about uh spify deployments in non kubernetes environments I know that's probably when it talk when it comes to spify most most of you think about it as a something for kubernetes but spify is a standard build for basically beyond that and be able to be interoperable whether you're running on kubernetes or I don't know uh Linux VMS your windows barom metal micos server s Etc So today we're going to talk about like what it means and how to how to reason about spey on kubernetes environment start with a quick introductions hi um I'm n I'm a software engineer at spiral where uh we build an implementation of the spiffy spec um and I've been there for around a year now um before that I worked um uh in security and then in as a systems engineer at Cloud flare um and outside of work I like to go on runs um hike and travel awesome my name is Eli n and um I think 70% maybe of people here in person know me but for those who not I'm co-founder and CTO at spiral I used to run and I built the world largest deployment of spify Open Source implementation known as Spire in the past I'm also a co-author of the books called solving the bottom Turtle if you go to spy.

iBook it's a free PDF book that's I highly recommend everyone to read if you want to kind of get deep into topics of identity workload identity authentication all this stuff and uh yeah uh spiral building a commercial workload identity implementation so I do not certainly expect everyone who came to this talk know what SP is so I'll I'll do a quick recap of what is that why we need it how it works on a high level and then we kind of dive in NAD we will diving into all the kind of interesting details um so what is piy raise your hand if you don't know what Spy is all right perfect we have a few people so spif stands for secure production identity framework for everyone uh it is cncf graduated project for three plus years I think correct me if I'm wrong um it started on the shoulders of like how production secure production infrastructure build in a companies like Facebook Google Netflix and others and incorporates kind of trying to ge
