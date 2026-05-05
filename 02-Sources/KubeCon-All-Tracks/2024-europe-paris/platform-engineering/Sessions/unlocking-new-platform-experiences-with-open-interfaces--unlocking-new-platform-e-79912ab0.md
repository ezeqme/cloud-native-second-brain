---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Thomas Vitale", "Systematic", "Mauricio \"Salaboy\" Salatino", "Diagrid"]
sched_url: https://kccnceu2024.sched.com/event/1YeOr/unlocking-new-platform-experiences-with-open-interfaces-thomas-vitale-systematic-mauricio-salaboy-salatino-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+New+Platform+Experiences+with+Open+Interfaces+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unlocking New Platform Experiences with Open Interfaces - Thomas Vitale, Systematic & Mauricio "Salaboy" Salatino, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Thomas Vitale, Systematic, Mauricio "Salaboy" Salatino, Diagrid
- Schedule: https://kccnceu2024.sched.com/event/1YeOr/unlocking-new-platform-experiences-with-open-interfaces-thomas-vitale-systematic-mauricio-salaboy-salatino-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+New+Platform+Experiences+with+Open+Interfaces+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unlocking New Platform Experiences with Open Interfaces.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOr/unlocking-new-platform-experiences-with-open-interfaces-thomas-vitale-systematic-mauricio-salaboy-salatino-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+New+Platform+Experiences+with+Open+Interfaces+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DladPy_4aFE
- YouTube title: Unlocking New Platform Experiences with Open Interfaces- Thomas Vitale & Mauricio "Salaboy" Salatino
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unlocking-new-platform-experiences-with-open-interfaces/DladPy_4aFE.txt
- Transcript chars: 38005
- Keywords: application, actually, platform, applications, winner, infrastructure, pretty, developers, dapper, native, simple, running, client, basically, common, challenges, message, developer

### Resumo baseado na transcript

welcome uh this presentation is titled unlocking new platform experiences with open interfaces and I'm here with Thomas to talk a little bit about different tools that you can use uh if you are building platforms how do you combine them together and how can you uh face some interesting challenges while do so right let's yes let's get started let's let's go right into it like we will not spend time on crazy stuff right so challenges that you will face when you're building platforms or dealing with a

### Excerpt da transcript

welcome uh this presentation is titled unlocking new platform experiences with open interfaces and I'm here with Thomas to talk a little bit about different tools that you can use uh if you are building platforms how do you combine them together and how can you uh face some interesting challenges while do so right let's yes let's get started let's let's go right into it like we will not spend time on crazy stuff right so challenges that you will face when you're building platforms or dealing with a bunch of teams working with kubernetes clusters and infrastructure and all that stuff let's start with the first challenge the first Challenge on boarding process right how do you get people in newer teams to get faster to use all these crazy tools together it gets complicated because again the amount of tools that you will need is pretty large and each tool has been designed with different use cases in mind so you kind like need to learn all of them in order to be effective with so we need to do something about it right the Second Challenge is that you're building distributed system so how can you reduce the cognitive load around like developers building these more complicated systems that needs to be resilient from the GetGo and that they just need to scale in some way or another right because your business will too good so you need to be able to scale dyamic with that and finally how do you run this and how do you operate this in your production environments how do you promotion across environments and how you do you know the things that you need to do with your applications like observe them and figure it out what's going wrong when things are not working as expected right yeah so let's start uh with a very simple application I presented this this application app developer gone this year uh with the D folks I don't know if you know them but uh what we showed here is that even for very very simple architectures uh things gets complicated really really fast so this is like an application that uh was published by doer Locker fold uh to show how to containerize applications using different languages and using different infrastructure right simple application to cast them mode and then see the results while the data is been you know aggregated by the worker service this case we're using Java C and do just a very poly environment all of these things will need to be containerized and deployed into kubernetes clust but then you have the infrastructure layer also tha
