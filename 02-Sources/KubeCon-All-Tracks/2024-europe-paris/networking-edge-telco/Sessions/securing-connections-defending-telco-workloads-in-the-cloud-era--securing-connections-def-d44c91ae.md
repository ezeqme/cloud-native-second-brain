---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking"]
speakers: ["Barun Acharya", "Accuknox"]
sched_url: https://kccnceu2024.sched.com/event/1YeQN/securing-connections-defending-telco-workloads-in-the-cloud-era-barun-acharya-accuknox
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Connections%3A+Defending+Telco+Workloads+in+the+Cloud+Era+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Securing Connections: Defending Telco Workloads in the Cloud Era - Barun Acharya, Accuknox

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Barun Acharya, Accuknox
- Schedule: https://kccnceu2024.sched.com/event/1YeQN/securing-connections-defending-telco-workloads-in-the-cloud-era-barun-acharya-accuknox
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Connections%3A+Defending+Telco+Workloads+in+the+Cloud+Era+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Securing Connections: Defending Telco Workloads in the Cloud Era.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQN/securing-connections-defending-telco-workloads-in-the-cloud-era-barun-acharya-accuknox
- YouTube search: https://www.youtube.com/results?search_query=Securing+Connections%3A+Defending+Telco+Workloads+in+the+Cloud+Era+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tTsZijbmvm8
- YouTube title: Securing Connections: Defending Telco Workloads in the Cloud Era - Barun Acharya, Accuknox
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/securing-connections-defending-telco-workloads-in-the-cloud-era/tTsZijbmvm8.txt
- Transcript chars: 18223
- Keywords: security, policy, network, intent, workloads, access, attack, inside, policies, probably, around, vectors, application, create, perspective, information, already, created

### Resumo baseado na transcript

I know I prepared that so I thought I'll talk about that uh I'll talk about securing connections for defending Tel over cloes in the cloud era so primarily before diving into the topic a bit about myself I'm Barun aara I go by demon 1024 over the Internet over Twitter LinkedIn wherever you want me to uh look for I'm a maintainer and I lead the development for cuer which is a ncf sandbox project I work as a software engineer at acox and I'm actively mentoring over Google entities but the malicious actor is not able to do anything but some other uh concerns could be but it's not just about securing entities inside your Port you need you need to have multi-layer security you need to have Security on on your uh Services itself like they they communicate over TLS or not so this is a report it's a demo application so it's obvious that it's using plain text but ideal case in your production environment you need to look for these things that okay you are

### Excerpt da transcript

I know I prepared that so I thought I'll talk about that uh I'll talk about securing connections for defending Tel over cloes in the cloud era so primarily before diving into the topic a bit about myself I'm Barun aara I go by demon 1024 over the Internet over Twitter LinkedIn wherever you want me to uh look for I'm a maintainer and I lead the development for cuer which is a ncf sandbox project I work as a software engineer at acox and I'm actively mentoring over Google summer of code and Linux Foundation mentorship also I'm a proud cncf Ambassador so what to expect out of this card talk we it's been a long day we have been digesting a lot of information so I just want to give you some context about what more you are going to learn today so primly two things what kind of attack vectors are there for 5G and te Telco workloads and how you can prevent them but that's one of the things the other thing is how do you orchestrate this security against this attack factors because Telco workloads are dynamic in nature you are creating clusters there are multiple clusters who manage across I don't know how many regions so orchestrating is also an important aspect so we are going to De dive deep into both of them uh how many of you in folks know about nephu neph is a Linux Foundation networking project that's good to see so I'm going to base my entire talk about around workloads running on nefo uh nefo is uh kubernetes uh orchestration where it helps you do Telco domain Automation in in an intent driven way it manages a lot of infrastructure and has a lot of design considerations around automating actual Telco workloads uh the Dem the demo application today will be free 5gc uh it's a standard demo application used across nefo as well as other 5G Telco Telco demos so I thought I'd use that uh the free 5gc deployment contains a management cluster some Regional clusters some Edge clusters orchestrated across control plane and work on planes so how do you enforce Security on that we have maybe hundreds of tools in the cncf security landscape do I just start using everything but uh before trying to decide on what exactly to use I'm going to take one tool from that Cube armor you you might have already predicted that being I'm part of cube armor so I'm going to use Cube armor to Showcase some of the attack vectors and prevention of those attacks and inside this nef plus free 5gc demo scenario we are going to see how to observe things through Cube armor how to secure endpoi
