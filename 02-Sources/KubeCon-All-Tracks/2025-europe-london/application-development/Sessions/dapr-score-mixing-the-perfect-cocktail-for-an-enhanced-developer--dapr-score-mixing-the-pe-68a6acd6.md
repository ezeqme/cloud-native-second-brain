---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Mathieu Benoit", "Humanitec", "Kendall Roden", "Diagrid"]
sched_url: https://kccnceu2025.sched.com/event/1txGi/dapr-+-score-mixing-the-perfect-cocktail-for-an-enhanced-developer-experience-mathieu-benoit-humanitec-kendall-roden-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Dapr+%2B+Score%3A+Mixing+the+Perfect+Cocktail+for+an+Enhanced+Developer+Experience+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Dapr + Score: Mixing the Perfect Cocktail for an Enhanced Developer Experience - Mathieu Benoit, Humanitec & Kendall Roden, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Mathieu Benoit, Humanitec, Kendall Roden, Diagrid
- Schedule: https://kccnceu2025.sched.com/event/1txGi/dapr-+-score-mixing-the-perfect-cocktail-for-an-enhanced-developer-experience-mathieu-benoit-humanitec-kendall-roden-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr+%2B+Score%3A+Mixing+the+Perfect+Cocktail+for+an+Enhanced+Developer+Experience+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Dapr + Score: Mixing the Perfect Cocktail for an Enhanced Developer Experience.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGi/dapr-+-score-mixing-the-perfect-cocktail-for-an-enhanced-developer-experience-mathieu-benoit-humanitec-kendall-roden-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Dapr+%2B+Score%3A+Mixing+the+Perfect+Cocktail+for+an+Enhanced+Developer+Experience+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-fGztPUuD8k
- YouTube title: Dapr + Score: Mixing the Perfect Cocktail for an Enhanced Develope... Mathieu Benoit & Kendall Roden
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dapr-score-mixing-the-perfect-cocktail-for-an-enhanced-developer-exper/-fGztPUuD8k.txt
- Transcript chars: 31984
- Keywords: dapper, developer, platform, workflow, docker, actually, application, implementation, engineer, component, running, developers, essentially, inventory, compose, ultimately, reddus, basically

### Resumo baseado na transcript

If this is your first talk of the day of the conference, um we're happy to kick it off for you. Previously was at Microsoft and has have been working on the open source Dabber project for about four years now. Um so yeah and then we have yeah and I'm a platform engineer and I have a mandate with my team to build a platform an internal developer platform for my company right the goal is to collaborate with cloud engineer network engineer security engineer with observability team and the goal is to make sure we have standard we are standardizing template we are standardizing governance security and we are going to have more automation the goal for this is better collaboration as well as enabling the developer to focus I'm building an internal developer platform but there is already existing tools security observability how they connect to each other how the team and the processes are interacting with each other. And Dapper and score um are very a good fit for that and we will demonstrate that today.

### Excerpt da transcript

Welcome to CubeCon. Super excited. If this is your first talk of the day of the conference, um we're happy to kick it off for you. Um my my name is Kendall Rhoden. I am a product manager at Diagrid. Previously was at Microsoft and has have been working on the open source Dabber project for about four years now. Hi, I'm Meno. I'm Clative Ambassador. Oh, could you hear me now? Yeah. Hi everyone. I'm Mat Benoa. I'm Clative Ambassador, score maintainer and customer success engineer at humanity. very glad and excited to be here with you today. Awesome. So, today you've come to hear about mixing the perfect cocktail. A little too early to actually give you one unfortunately, but we'll make sure that you have a good time today and learn a lot about Dapper and Score. So, just want to set the context a little bit about the current state of the world as I know it and as probably many of you know it as well, right? platform and infrastructure concerns have become progressively more apparent to developers and bleed into the interloop development process.

Right? Additional dependencies, new libraries, new concerns that come when you break an application across the network. And when you introduce largecale development, you have to start to find ways to help abstract away some of the complexity that's happening at the runtime and infrastructure level from your developers. So this is sort of just setting the scene of of where we are today. So depending on what messaging infrastructure you're using, what databases you're using, where you're deploying your applications, typically that's going to end up bleeding into your developers inner loop and slowing down their productivity. So for today's uh for today's talk, um Matt and I are Can I call you can I call you that? Is that okay? Yeah. Yeah. Uh we're going to be we're going to be uh playing two different roles. Um and these are two roles that work very much together in the in the cloud native space and on most teams. uh I'll be playing the role of basically an application developer and ultimately uh let's say I'm a full stack developer and I care about being productive.

I want to be able to build innovative applications quickly and I don't really care necessarily what the underlying infrastructure is that I'm using. I don't want to be rewriting common patterns. I don't want to be implementing complex resiliency logic. I don't want to be rewriting stateful processes and workflows and actors when those things already exist
