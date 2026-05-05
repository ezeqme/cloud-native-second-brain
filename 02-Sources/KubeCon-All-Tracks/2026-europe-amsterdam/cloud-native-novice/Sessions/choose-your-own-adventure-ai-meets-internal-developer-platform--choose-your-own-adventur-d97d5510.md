---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["AI ML", "Platform Engineering", "Storage Data"]
speakers: ["Whitney Lee", "Datadog", "Viktor Farcic", "Upbound"]
sched_url: https://kccnceu2026.sched.com/event/2CVz6/choose-your-own-adventure-ai-meets-internal-developer-platform-whitney-lee-datadog-viktor-farcic-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+AI+Meets+Internal+Developer+Platform+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Choose Your Own Adventure: AI Meets Internal Developer Platform - Whitney Lee, Datadog & Viktor Farcic, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Whitney Lee, Datadog, Viktor Farcic, Upbound
- Schedule: https://kccnceu2026.sched.com/event/2CVz6/choose-your-own-adventure-ai-meets-internal-developer-platform-whitney-lee-datadog-viktor-farcic-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+AI+Meets+Internal+Developer+Platform+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Choose Your Own Adventure: AI Meets Internal Developer Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVz6/choose-your-own-adventure-ai-meets-internal-developer-platform-whitney-lee-datadog-viktor-farcic-upbound
- YouTube search: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+AI+Meets+Internal+Developer+Platform+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=k7ct4sW-97E
- YouTube title: Choose Your Own Adventure: AI Meets Internal Developer Platform - Whitney Lee & Viktor Farcic
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/choose-your-own-adventure-ai-meets-internal-developer-platform/k7ct4sW-97E.txt
- Transcript chars: 33588
- Keywords: database, deploy, agents, victor, cluster, platform, control, vector, whatever, cannot, search, probably, context, trying, available, choose, anything, knowledge

### Resumo baseado na transcript

That's uh I know you you're all into Kubernetes and all this stuff, right? But uh now everybody's moving to agency and you will start building agents for one reason or another. So, I want to be able to figure out what's going on with my application, why it's not running on Kubernetes. And honestly, as a developer, I don't want to have to know anything about Kubernetes. So what my platform team is providing to me is an agent that does have cluster access and that can access the cluster and figure out stuff on my behalf without me necessarily having to understand Kubernetes. And this is cube control get, cube control describe, and cube control uh logs.

### Excerpt da transcript

Okay, so let's talk about uh agents, right? That's uh I know you you're all into Kubernetes and all this stuff, right? But uh now everybody's moving to agency and you will start building agents for one reason or another. You you will need it, company will need it and so on and so forth and especially if you're pl into platform engineering because agents are the next evolution of platforms in a way. You want to give your developers tooling how to do stuff. Well, before it was backstage, now it's uh agents, right? That that's where we are going. Now, what we're going to do today uh is figure out how we can build agents. We will not have time to go through everything you need to know, but some essentials. And let's start with the beginning, right? Uh you probably most of you already have clo or cursor or something like that. You can come to a conclusion LMS know everything, agents can do everything, which is absolutely not true. uh and we will see what's missing in a second. But for now, what the important part is that you will be building agents yourself for whatever types of task operations you're doing in your company or you want others to to enable others to do.

Now, this is how agents work, right? It's relatively simple to explain. You have an agent and that agent accepts input from a user, right? That's intent. I want this and that whatever that something is or do this and that for me whatever that something is that agent uh gets the system context that's instructions who you are kind of what's your basic capabilities that's get gets combined with the user intent and it is sent to an LLM right to a model from here on starts what we call a genetic loop right LLM can respond right away and say here's the answer More often than not in our world, what LM will do is that it will request to execute some tool that is provided by the agent. Tool can be anything. It could be something baked into the agent. It could be MCP, it could be skill, it could be many different things. The only thing that matters is that agent provides some tools to LLM. Those tools have descriptions. Based on that, those descriptions, LLMs know when to call one of those tools depending on what you ask it to do, right?

and it calls the tools, gets a request, and then it repeats over and over and over and over again until it eventually responds back to you, right? This is how every single agent works, right? Uh unless you're in chat boxes or something like that and you don't maybe have t
