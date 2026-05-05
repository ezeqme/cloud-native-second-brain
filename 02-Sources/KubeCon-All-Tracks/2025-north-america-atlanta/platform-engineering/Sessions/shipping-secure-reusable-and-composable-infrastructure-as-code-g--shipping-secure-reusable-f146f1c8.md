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
themes: ["Security", "Platform Engineering"]
speakers: ["Feynman Zhou", "Microsoft", "Katherine Pitz", "GE HealthCare"]
sched_url: https://kccncna2025.sched.com/event/27FWZ/shipping-secure-reusable-and-composable-infrastructure-as-code-ge-healthcares-journey-with-oras-feynman-zhou-microsoft-katherine-pitz-ge-healthcare
youtube_search_url: https://www.youtube.com/results?search_query=Shipping+Secure%2C+Reusable%2C+and+Composable+Infrastructure+as+Code%3A+GE+HealthCare%E2%80%99s+Journey+With+ORAS+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Shipping Secure, Reusable, and Composable Infrastructure as Code: GE HealthCare’s Journey With ORAS - Feynman Zhou, Microsoft & Katherine Pitz, GE HealthCare

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Security]], [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Feynman Zhou, Microsoft, Katherine Pitz, GE HealthCare
- Schedule: https://kccncna2025.sched.com/event/27FWZ/shipping-secure-reusable-and-composable-infrastructure-as-code-ge-healthcares-journey-with-oras-feynman-zhou-microsoft-katherine-pitz-ge-healthcare
- Busca YouTube: https://www.youtube.com/results?search_query=Shipping+Secure%2C+Reusable%2C+and+Composable+Infrastructure+as+Code%3A+GE+HealthCare%E2%80%99s+Journey+With+ORAS+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Shipping Secure, Reusable, and Composable Infrastructure as Code: GE HealthCare’s Journey With ORAS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWZ/shipping-secure-reusable-and-composable-infrastructure-as-code-ge-healthcares-journey-with-oras-feynman-zhou-microsoft-katherine-pitz-ge-healthcare
- YouTube search: https://www.youtube.com/results?search_query=Shipping+Secure%2C+Reusable%2C+and+Composable+Infrastructure+as+Code%3A+GE+HealthCare%E2%80%99s+Journey+With+ORAS+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=u4zinRUhtw8
- YouTube title: Shipping Secure, Reusable, and Composable Infrastructure as Code... Feynman Zhou & Katherine Pitz
- Match score: 0.804
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/shipping-secure-reusable-and-composable-infrastructure-as-code-ge-heal/u4zinRUhtw8.txt
- Transcript chars: 21068
- Keywords: packages, healthcare, hospital, artifacts, infrastructure, application, container, registry, applications, package, manage, custom, artifact, process, solution, software, actually, registries

### Resumo baseado na transcript

Um, but if we can get another laptop in like during the middle of it, then we'll put up the slides. So, if you want to pull it up on your phones and look through it as we go through, you can also do that. They would have to design whatever container or package how they were going to ship and deliver that to the hospital. So, uh, my platform team at GU Healthcare outlined a list of problems that we wanted to solve when building our solution. The problems we wanted to solve were that every hospital has their own custom cloud infrastructure and environment configuration. The installations of this cloud infra and applications, it can have a lot of manual steps but also varying different processes based on what the application teams have written and designed for that application.

### Excerpt da transcript

We'll start the presentation without the slides. Apologize for that. Um, but if we can get another laptop in like during the middle of it, then we'll put up the slides. There are also a copy of the slides on this presentation as well. So, if you want to pull it up on your phones and look through it as we go through, you can also do that. Hey everyone, my name is Feman. I'm currently working at Microsoft Azure as a product manager. I'm also a maintainer for CNCF or project and not project. We're happy to be here and with my co-speaker Katie. >> Hi, I'm Katie Pittz. I am a software engineer for GE Healthcare. This is also my first CubeCon and I'm speaking at it. So, I'm very excited and I'm also a little nervous to be here today. I also brought some very nice AAS swags. So, if you have any questions after this session, reach out to us or just ask in the room. I'm gonna send this wax to to you. All right. So, today we don't have a slide because technical issues, but we can still tell the story. It's not that technical.

It's very friendly. So basically we're going to share what are the challenges and problems that G healthcare were facing in the past and how their cloud native transformation going with infrastructure as code OCI or such kind of cloud native technologies and I will be sharing more about the project related to ARAS OCI and recent updates in ORAS project. Before that, I will hand it over to Katie. So, Katie, would you want to share what are the problems and challenges that you were facing in the past? >> Sure, I would love to. So, this is the story of how Ora's helped GE Healthcare deliver the future of patient care. So, GE Healthcare has a whole suite of patient care applications and more and more of them are becoming cloudnative, which is really exciting for us. But currently our model of delivery for these patient care applications uh has some issues and we need to innovate on that. So before all of our application teams manage their application infrastructure independently. It was not centralized at all.

So when a hospital would order a subscription to one of our patient care applications, uh the process of actually deploying that cloud infra and the application to the hospital was all managed by the application team. They would have to design whatever container or package how they were going to ship and deliver that to the hospital. They would have to write the runbook for the service engineers on how to either do the manual deployments or
