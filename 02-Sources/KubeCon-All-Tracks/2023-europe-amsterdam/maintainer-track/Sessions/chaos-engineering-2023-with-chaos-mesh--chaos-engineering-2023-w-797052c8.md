---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Saiyam Pathak", "Civo"]
sched_url: https://kccnceu2023.sched.com/event/1K6Ai/chaos-engineering-2023-with-chaos-mesh-saiyam-pathak-civo
youtube_search_url: https://www.youtube.com/results?search_query=Chaos+Engineering+2023+with+Chaos+Mesh+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Chaos Engineering 2023 with Chaos Mesh - Saiyam Pathak, Civo

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Saiyam Pathak, Civo
- Schedule: https://kccnceu2023.sched.com/event/1K6Ai/chaos-engineering-2023-with-chaos-mesh-saiyam-pathak-civo
- Busca YouTube: https://www.youtube.com/results?search_query=Chaos+Engineering+2023+with+Chaos+Mesh+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Chaos Engineering 2023 with Chaos Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1K6Ai/chaos-engineering-2023-with-chaos-mesh-saiyam-pathak-civo
- YouTube search: https://www.youtube.com/results?search_query=Chaos+Engineering+2023+with+Chaos+Mesh+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dlgQXrDfqzs
- YouTube title: Chaos Engineering 2023 with Chaos Mesh - Saiyam Pathak, Civo
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/chaos-engineering-2023-with-chaos-mesh/dlgQXrDfqzs.txt
- Transcript chars: 29191
- Keywords: cluster, mesh, particular, engineering, application, workflow, experiments, actually, create, production, already, running, dashboard, experiment, network, maintainers, adding, systems

### Resumo baseado na transcript

I mean you guys are really really awesome because the room is full packed so and it's the last session so you are really here to learn and I'm really happy about that uh so uh yeah let's start with the session uh today we'll be talking about chaos engineering chaos mesh that's what you're here for and I'll try my best to explain you uh what chaos engineering is by the way uh can you raise your hands how many of you know about chaos engineering like what it the future but as of now if you want to view you will be viewing it from the cluster 2's dashboard which is there moving on to the third demo uh which is the port Network latency so this is uh again the network chaos

### Excerpt da transcript

I mean you guys are really really awesome because the room is full packed so and it's the last session so you are really here to learn and I'm really happy about that uh so uh yeah let's start with the session uh today we'll be talking about chaos engineering chaos mesh that's what you're here for and I'll try my best to explain you uh what chaos engineering is by the way uh can you raise your hands how many of you know about chaos engineering like what it is and how it is being used awesome almost everyone so um so I my name is Saiyan Pathak and I'm working as director of technical evangelism at sibo I'm also a cncf Ambassador and yeah you can find me on Twitter either it's I am Pathak and tweet anything about the session that you learned or found interesting so the storyline for this session would be um introduction like what chaos engineering is where it fits in and what is what are the principles so these will be the general introduction um that applies to all the projects and then we'll move to the project chaos mesh what chaos mesh is what are some of the new features that the maintainers have been working on so I am not one of the maintainers of chaos mesh I am more of the Community member of chaos mesh and the user so I'll be talking from that perspective more and then we'll be looking at some of the demos um I think three demos uh in which I'll showcase one interesting one which is the multi-cluster chaos that is a new one that have been introduced so the the systems are have been moving moved from linear systems to the complex system so previously we used to have monolithic applications uh simple applications where even you know it happens like a single person also knows the end-to-end how system works you can go to them and ask okay how this works this is where it failed and this is where you'll be able to find a bug in that particular system over the period of time the systems have matured enough it has become non-linear you have moved to a distributed world where it is all micro Services microservices architecture if you know you have so many um smaller chunk of your apis running as a separate micro Services inside containers kubernetes and that is unpredictable Behavior you don't know where exactly things go wrong like you have so many hundreds of micro Services one thing fails in your application that it becomes very difficult to see where your application actually has failed so that unpredictable Behavior have made uh the even the systems c
