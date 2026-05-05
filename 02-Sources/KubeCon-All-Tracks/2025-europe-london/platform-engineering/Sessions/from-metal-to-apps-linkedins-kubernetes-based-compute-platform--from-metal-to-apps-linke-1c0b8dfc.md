---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Ahmet Alp Balkan", "Ronak Nathani", "LinkedIn"]
sched_url: https://kccnceu2025.sched.com/event/1txGQ/from-metal-to-apps-linkedins-kubernetes-based-compute-platform-ahmet-alp-balkan-ronak-nathani-linkedin
youtube_search_url: https://www.youtube.com/results?search_query=From+Metal+To+Apps%3A+LinkedIn%E2%80%99s+Kubernetes-based+Compute+Platform+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Metal To Apps: LinkedIn’s Kubernetes-based Compute Platform - Ahmet Alp Balkan & Ronak Nathani, LinkedIn

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Ahmet Alp Balkan, Ronak Nathani, LinkedIn
- Schedule: https://kccnceu2025.sched.com/event/1txGQ/from-metal-to-apps-linkedins-kubernetes-based-compute-platform-ahmet-alp-balkan-ronak-nathani-linkedin
- Busca YouTube: https://www.youtube.com/results?search_query=From+Metal+To+Apps%3A+LinkedIn%E2%80%99s+Kubernetes-based+Compute+Platform+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Metal To Apps: LinkedIn’s Kubernetes-based Compute Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGQ/from-metal-to-apps-linkedins-kubernetes-based-compute-platform-ahmet-alp-balkan-ronak-nathani-linkedin
- YouTube search: https://www.youtube.com/results?search_query=From+Metal+To+Apps%3A+LinkedIn%E2%80%99s+Kubernetes-based+Compute+Platform+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dDkXFuy45EA
- YouTube title: From Metal To Apps: LinkedIn’s Kubernetes-based Compute Platform - Ahmet Alp Balkan & Ronak Nathani
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-metal-to-apps-linkedins-kubernetes-based-compute-platform/dDkXFuy45EA.txt
- Transcript chars: 43928
- Keywords: cluster, application, machine, applications, clusters, actually, maintenance, several, running, control, custom, thanks, systems, pretty, mentioned, stateful, resources, linkedin

### Resumo baseado na transcript

Uh, in the next 30 minutes, we'll walk you through how we are building a scalable compute platform all the way from metal bare metal to apps. We are part of the central comput team at LinkedIn serving thousands of engineers. mix of Kubernetes as well as as well as our in-house orchestrator and these applications run on one and a half million containers. And on top of that, we have a Kubernetes cluster management layer which are the concepts that you're kind of familiar with. Uh I want to start with the infrastructure as a service layer and then move on to the Kubernetes cluster management. Uh if you're using a cloud provider, you can think of it as your you know virtual machine scale set or you know autoscaling uh instance group API and so on so forth.

### Excerpt da transcript

All right. Um, hey everyone, welcome to our talk. Uh, in the next 30 minutes, we'll walk you through how we are building a scalable compute platform all the way from metal bare metal to apps. We are part of the central comput team at LinkedIn serving thousands of engineers. Uh, we don't use Kubernetes in the traditional way, but we extend it extremely heavily. Um, just a little warning, we'll have bunch of slides, bunch of text, and bunch of pictures. Feel free to take snapshots and we'll share slides towards the end as well. Uh, all right. Before we get started, a little bit about us. I'm Ron. I'm based out of Toronto. This is my third CubeCon, first one as a speaker. And 2022 Detroit was my first one. Outside of Kubernetes, I love to play racket sports, specifically badminton if someone wants to play. Uh, and I also host a podcast called Soft Misadventures. Yeah, I'm one of the top followers of Ron Next podcast. Uh, hello everyone. My name is Amit. I'm uh coming here from Seattle. I think this is my seventh or eighth CubeCon.

I actually I couldn't count. Uh I think this is my third time giving a talk. Outside Kubernetes, I like gardening in house plans, but actually still outside Kubernetes, I like to develop cubecado plugins for you all. Uh maybe you're using a few of them. So I want to I want to walk you through LinkedIn scale because without putting things in perspective, I don't think you'll get a full picture of why we're building what we're building. First of all, I assume you're all familiar with LinkedIn. Uh we have over a billion members on our site and these members are served by some 3,000 services and some of these are databases, stream processing services or microservices and these systems run on about 500,000 plus servers and these servers are again a mix of Kubernetes as well as as well as our in-house orchestrator and these applications run on one and a half million containers. Uh it's a pretty good number and they all get deployed pretty frequently. We have we're serving thousands of engineers internally at LinkedIn and they're doing deploys multiple times a day on these applications.

And one interesting thing about us is that we do not run on a cloud provider. We have our own data centers and we run everything on bare metal. We do not do virtualization uh for many reasons. One of them being performance. So today we'll walk you through our compute platform. Uh you here you'll see three layers. At the bottom we have an infrastructure as
