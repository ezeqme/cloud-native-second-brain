---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Rajsimman Ravichandiran", "Independent"]
sched_url: https://kccnceu2023.sched.com/event/1HycU/using-devspace-to-usher-in-an-era-of-peace-for-our-developers-rajsimman-ravichandiran-independent
youtube_search_url: https://www.youtube.com/results?search_query=Using+DevSpace+to+Usher+in+an+Era+of+Peace+for+Our+Developers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Using DevSpace to Usher in an Era of Peace for Our Developers - Rajsimman Ravichandiran, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rajsimman Ravichandiran, Independent
- Schedule: https://kccnceu2023.sched.com/event/1HycU/using-devspace-to-usher-in-an-era-of-peace-for-our-developers-rajsimman-ravichandiran-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Using+DevSpace+to+Usher+in+an+Era+of+Peace+for+Our+Developers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Using DevSpace to Usher in an Era of Peace for Our Developers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HycU/using-devspace-to-usher-in-an-era-of-peace-for-our-developers-rajsimman-ravichandiran-independent
- YouTube search: https://www.youtube.com/results?search_query=Using+DevSpace+to+Usher+in+an+Era+of+Peace+for+Our+Developers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5iqAJq98EfE
- YouTube title: Using DevSpace to Usher in an Era of Peace for Our Developers - Rajsimman Ravichandiran
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/using-devspace-to-usher-in-an-era-of-peace-for-our-developers/5iqAJq98EfE.txt
- Transcript chars: 20995
- Keywords: environment, developers, deploy, developer, development, cluster, changes, simply, unique, create, branch, workflows, experience, end-to-end, deployments, command, devspace, develop

### Resumo baseado na transcript

hi welcome to oh oh using devspace to usher in an era of Peace for our developers my name is Raj Sim and ravichandran in short Raj I'm a software engineer that specializes in cloud computing I started my career as a site reliability engineer where I manage kubernetes clusters and ensure the Readiness of the systems and then I slowly pivoted towards developer experience I'm here to talk about the developer experience journey and how we improve them last year at my previous company so these are the following

### Excerpt da transcript

hi welcome to oh oh using devspace to usher in an era of Peace for our developers my name is Raj Sim and ravichandran in short Raj I'm a software engineer that specializes in cloud computing I started my career as a site reliability engineer where I manage kubernetes clusters and ensure the Readiness of the systems and then I slowly pivoted towards developer experience I'm here to talk about the developer experience journey and how we improve them last year at my previous company so these are the following developer challenges that I'll be talking about in this session and we really got to know about the these developer challenges by talking to the developers uh getting and putting out surveys in our organization trying to develop results regarding how they feel about our development clusters and we really try to understand from their point of view and I've marked them over a happiness over time graph so that we can showcase uh the developer experience journey and how we uh address each of these Point points and how it changes over time so starting from the top we have shared development environment in our cluster and that makes it really painful for our developers to test their changes in the environment they also face the problems with local environment setup hassles that they have to do a lot of complex setting up of their tools and packages to get things started in their local environment combined with those two pain points they they end up taking a longer cycle time to develop tests and push push code to production and finally they also tend to face a lot of problems with setting up the environment for running end-to-end tests in our system now quick show of hands how many of you are phase one or more of these problems at your organization it's good to know that um so let's start off with uh the start of the first pain point of our environment of share development cluster and before I start off with that I want to give a brief background of our developer environment so we have our kubernetes development cluster that's uh runs on kubernetes and our development cluster is shared with 100 developers in our organization and we have main or core services that are deployed on one namespace in our development cluster that says nay coordinate space and their name serves a b and c they are core services that power our main applications and they and most if not all the developers use these services in their day-to-day work and there are also other non-uh critic
