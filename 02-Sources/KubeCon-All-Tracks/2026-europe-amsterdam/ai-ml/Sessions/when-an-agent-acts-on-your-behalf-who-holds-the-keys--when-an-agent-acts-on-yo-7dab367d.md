---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Mariusz Sabath", "Maia Iyer", "IBM Research"]
sched_url: https://kccnceu2026.sched.com/event/2CVxt/when-an-agent-acts-on-your-behalf-who-holds-the-keys-mariusz-sabath-maia-iyer-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=When+an+Agent+Acts+on+Your+Behalf%2C+Who+Holds+the+Keys%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# When an Agent Acts on Your Behalf, Who Holds the Keys? - Mariusz Sabath & Maia Iyer, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mariusz Sabath, Maia Iyer, IBM Research
- Schedule: https://kccnceu2026.sched.com/event/2CVxt/when-an-agent-acts-on-your-behalf-who-holds-the-keys-mariusz-sabath-maia-iyer-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=When+an+Agent+Acts+on+Your+Behalf%2C+Who+Holds+the+Keys%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre When an Agent Acts on Your Behalf, Who Holds the Keys?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxt/when-an-agent-acts-on-your-behalf-who-holds-the-keys-mariusz-sabath-maia-iyer-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=When+an+Agent+Acts+on+Your+Behalf%2C+Who+Holds+the+Keys%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kc2NuTUt5Os
- YouTube title: When an Agent Acts on Your Behalf, Who Holds the Keys? - Mariusz Sabath & Maia Iyer, IBM Research
- Match score: 0.812
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/when-an-agent-acts-on-your-behalf-who-holds-the-keys/kc2NuTUt5Os.txt
- Transcript chars: 31539
- Keywords: agents, identity, exchange, spiffy, access, workload, attributes, application, another, client, authorization, gateway, request, actually, everything, server, provide, target

### Resumo baseado na transcript

My name is Mario Sabat IBM research and this is >> and my name is Maya also IBM research and we've been working on security for a long time and today we're going to be talking about how to instrument security for agentic applications at the platform level. So to start I think it'll be oh this is us okay and then to start I think it'll be easiest to go into a use case right so when GitHub receives a request with an API key GitHub assumes that there is a user So that is going to be a problem for enforcing zero trust posture in your organization. In this project, what we've done is the idea was to build a platform completely using open source technologies and provide features in these four key pillars of life cycle orchestration, networking, security and observability and completely implement them using existing open source building blocks. And the first one is the fact that every time we made a change to the platform and added a new security layer, the application code had to change. However, there are a couple issues with using this for within our security framework.

### Excerpt da transcript

Yeah, let's start because we have a >> packed >> agenda. Yes, agent. Okay, thank you all for being here. This is such a privilege for us to being able to share uh our work. My name is Mario Sabat IBM research and this is >> and my name is Maya also IBM research and we've been working on security for a long time and today we're going to be talking about how to instrument security for agentic applications at the platform level. So to start I think it'll be oh this is us okay and then to start I think it'll be easiest to go into a use case right so when GitHub receives a request with an API key GitHub assumes that there is a user behind it right and for the most part that was the case but recently there is now this new workflow that you may have heard of called the agentic workflow where there are now agents involved and in this workflow users can now talk to agents using natural language and the agent will do some LLM magic and figure out the details of how to actually make the requests to downstream tools.

Right? So in this scenario, API keys are also typically used. And this is perfectly fine because when the agent runs locally, the user is going to be ultimately responsible for the behavior of that agent. So GitHub is not going to care about whether it's a user or an agent. But once we bring an agent to enterprise and try to host it multi-tenants for multiple users, things become more complicated. And the reason for this is because now that the agent is being run in an organization, the organization is going to be responsible for vetting the behavior of the agent. So this API key pattern is going to kind of break down. And the reason for this is several reasons. For example, there are this is a very very simple use case of like one agent and one tool. In reality, an agent can be talking to multiple other agents, multiple other tools, talking to other infrastructure, right? And in this case, if everything we're accepting API keys, then the user is going to have to pass all of the API keys to all of the for all upon all requests.

And also on top of that, these API keys tend to be long lived credentials, right? So that is going to be a problem for enforcing zero trust posture in your organization. And on top of that um the the issue here is that every every request to every application is only going to have the information that the user is making that request. It's not clear whether there's an agent in the middle, two agents in the middle. And really if we
