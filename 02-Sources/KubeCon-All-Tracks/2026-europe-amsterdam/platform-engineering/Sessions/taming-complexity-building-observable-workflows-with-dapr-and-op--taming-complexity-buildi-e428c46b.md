---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Observability", "Platform Engineering"]
speakers: ["Mauricio \"Salaboy\" Salatino", "Diagrid", "Kasper Borg Nissen", "Dash0"]
sched_url: https://kccnceu2026.sched.com/event/2CW6J/taming-complexity-building-observable-workflows-with-dapr-and-opentelemetry-mauricio-salaboy-salatino-diagrid-kasper-borg-nissen-dash0
youtube_search_url: https://www.youtube.com/results?search_query=Taming+Complexity%3A+Building+Observable+Workflows+With+Dapr+and+OpenTelemetry+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Taming Complexity: Building Observable Workflows With Dapr and OpenTelemetry - Mauricio "Salaboy" Salatino, Diagrid & Kasper Borg Nissen, Dash0

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Observability]], [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mauricio "Salaboy" Salatino, Diagrid, Kasper Borg Nissen, Dash0
- Schedule: https://kccnceu2026.sched.com/event/2CW6J/taming-complexity-building-observable-workflows-with-dapr-and-opentelemetry-mauricio-salaboy-salatino-diagrid-kasper-borg-nissen-dash0
- Busca YouTube: https://www.youtube.com/results?search_query=Taming+Complexity%3A+Building+Observable+Workflows+With+Dapr+and+OpenTelemetry+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Taming Complexity: Building Observable Workflows With Dapr and OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6J/taming-complexity-building-observable-workflows-with-dapr-and-opentelemetry-mauricio-salaboy-salatino-diagrid-kasper-borg-nissen-dash0
- YouTube search: https://www.youtube.com/results?search_query=Taming+Complexity%3A+Building+Observable+Workflows+With+Dapr+and+OpenTelemetry+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XVEPKb0aCx8
- YouTube title: Taming Complexity: Building Observable Workflows... Mauricio "Salaboy" Salatino & Kasper Borg Nissen
- Match score: 0.775
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/taming-complexity-building-observable-workflows-with-dapr-and-opentele/XVEPKb0aCx8.txt
- Transcript chars: 35051
- Keywords: agents, running, actually, applications, instrumentation, little, protocol, basically, application, frameworks, complexity, workflows, skills, dapper, agentic, observe, drinks, working

### Resumo baseado na transcript

Um or we actually started taming complexity because there's a lot of complexity in this world today and when we originally designed this talk we were thinking about doing like talking about asynchronous workflows and stuff like that but then AI and MCP servers and Marishia went crazy with the demo. So >> so that's what we like basically ended up doing is like doing a lot of different things within agents MCP servers tool called skills >> LLMs all over the place. teams in the new landscape Cape again we were thinking okay we have microser eventdriven architectures what do we need to learn when we start thinking about building really distributed agentic applications first of all we need to start learning about agentic frameworks there are And I'm really interested about these things because again, it provides a way for us to like conceptualize how true agents can interact that are running in different let's say containers for the sake of of Kubernetes, right? And the protocol is being built on like enterprisegrade concerns like security uh you know communications resiliency user experience and discoverability for example uh I wanted to focus on two things about this protocol the A2A protocol uh because again this is a complement to The A2A protocol was designed to also cover audio and video, which is something that I haven't done before.

### Excerpt da transcript

Welcome to this talk building observable workflows. Um or we actually started taming complexity because there's a lot of complexity in this world today and when we originally designed this talk we were thinking about doing like talking about asynchronous workflows and stuff like that but then AI and MCP servers and Marishia went crazy with the demo. So >> so that's what we like basically ended up doing is like doing a lot of different things within agents MCP servers tool called skills >> LLMs all over the place. Yeah. >> So, uh I I tend to like building demos. The problem with this is like no matter how simple the demo that you're building is, it gets really complex really really fast. And we will show you something super simple, but it's at the same time very complicated to understand what's going on. >> Yeah. But before that, maybe just a quick introduction to who we are. My name is Casper. I work as a principal developer advocate at the zero. Um I do a lot of stuff in the community in the Nordics.

Uh help co-ounded cloud native Nordics and run some of the groups in in Denmark as well helped with that. Um that's a conference in November 1920th cloud native Denmark. So make sure to check that out. CFP is open. >> Yeah. And I'm Salatino. I work like as an ecosystem engineer for a company. It's called Diagrid. We work on the Dapper project. So if you're interested in that, feel free to visit the booth in the showcase room. >> So the TLTW too long to watch. Um as your applications grow uh in or infrastructure grow in complexity, you must have the right tools to understand what is going on at all times. That's kind of the thing we want to try and highlight in in this talk >> because architectures have been evolving like since the monolithic applications back in what the beginning of the 2000s earlier maybe also and then we had the microser coming then everything be became asynchronous event driven and now we are doing agents uh in the mix of our services doing all kinds of nondeterministic things so it's it's a little bit crazy what what is going to to happen right now.

Yeah. And with agents, it goes a little bit further down on the path of you don't know actually with this where these agents are running. Are they running all in the same application in the same container or are they like distributed agents as well which are pretty much closer to distributed applications. Last year we did the same presentation that we are doing today but mostly focused on d
