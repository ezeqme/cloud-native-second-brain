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
themes: ["AI ML", "Networking"]
speakers: ["Luc Chmielowski", "Nirmata", "Nina Polshakova", "Solo.io"]
sched_url: https://kccnceu2026.sched.com/event/2CVxe/least-privilege-for-ai-authorizing-agents-and-mcp-tools-with-agentgateway-and-kyverno-luc-chmielowski-nirmata-nina-polshakova-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Least-Privilege+for+AI%3A+Authorizing+Agents+and+MCP+Tools+with+Agentgateway+and+Kyverno+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Least-Privilege for AI: Authorizing Agents and MCP Tools with Agentgateway and Kyverno - Luc Chmielowski, Nirmata & Nina Polshakova, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Luc Chmielowski, Nirmata, Nina Polshakova, Solo.io
- Schedule: https://kccnceu2026.sched.com/event/2CVxe/least-privilege-for-ai-authorizing-agents-and-mcp-tools-with-agentgateway-and-kyverno-luc-chmielowski-nirmata-nina-polshakova-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Least-Privilege+for+AI%3A+Authorizing+Agents+and+MCP+Tools+with+Agentgateway+and+Kyverno+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Least-Privilege for AI: Authorizing Agents and MCP Tools with Agentgateway and Kyverno.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxe/least-privilege-for-ai-authorizing-agents-and-mcp-tools-with-agentgateway-and-kyverno-luc-chmielowski-nirmata-nina-polshakova-soloio
- YouTube search: https://www.youtube.com/results?search_query=Least-Privilege+for+AI%3A+Authorizing+Agents+and+MCP+Tools+with+Agentgateway+and+Kyverno+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tEAkoZpdhSc
- YouTube title: Least-Privilege for AI: Authorizing Agents and MCP Tools with A... Luc Chmielowski & Nina Polshakova
- Match score: 0.829
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/least-privilege-for-ai-authorizing-agents-and-mcp-tools-with-agentgate/tEAkoZpdhSc.txt
- Transcript chars: 23613
- Keywords: gateway, authorization, policy, server, actually, cluster, basically, agents, called, traffic, access, cursor, supports, keycloak, resource, policies, connect, inspector

### Resumo baseado na transcript

Uh welcome everyone uh to our talk lease privilege for AI authorizing agents and MCP tools with agent gateway and Kyverno. And uh most recently I'm working on a project called agent gateway where I'm a maintainer and it's an AI gateway that integrates with Kyivero. On top of that, if you are a platform engineer trying to handle authorization at scale, um you going to have like audit trails that are in lots of different places and duplication of the authorization logic. So cell is like common expression language um and it allows you to do like usually for Kubernetes run policies on your cluster so that nothing bad happens. But recently uh we've been working on with other maintainers at making the kano rules apply at edge and um the idea was to use the same validating policies that we have for Kubernetes and to apply them um on native like HTTP or envoy So, it supports Kubernetes gateway API, the latest version of that 1.5.

### Excerpt da transcript

Uh welcome everyone uh to our talk lease privilege for AI authorizing agents and MCP tools with agent gateway and Kyverno. Um I'm Nina Pushkova. I'm a software engineer at Solo. I was also the Kubernetes 133 release lead. And uh most recently I'm working on a project called agent gateway where I'm a maintainer and it's an AI gateway that integrates with Kyivero. >> And hi everyone, my name is Luke Miroski. I'm a namatar engineer um and I a maintainer of Keano. Um, and I've been working for the past few months on a tool called Kevano authorization that we'll see later in this demo. Um, today we're going to talk about how to secure basically AI agents um via securing MC the MCP protocol. Uh, we'll see like the challenges of it and how we got a solution for it. Um recently in the news like if you watch the tech news there is a lot of news like that where a company deploys an agent in production the agent does something really bad and the company has a lot of problems. Um just a quick show of hands who deploys agents in production at the moment no one.

Oh yes some hands. Okay. Um yeah so this is like quite scary for a lot of companies and a lot of people. Um and this is where all of our like our talk started. But first before like getting into how to secure it we need to understand how they discuss with the world right. Um before uh having protocols like MCP and A2A agents had to talk the same language as us like use SQL use cubes or whatever to discuss with the world. uh it wasn't like really streamlined. So people researched and created those two languages and in fact now it's like a communication standards. Um everyone that is using uh cursor or whatever you you are using MCP servers to do stuff you know. Um so we're going to see why IM usual IM principles apply to MCP. If you look uh into the OASP just a bit, you see that there are a lot of things about authorization and overall like this is one of the main thing you do when you start creating an app, you work on the authorization, right? So why apply AM to MCP? So MCP is basically a JSON RPC based protocol uh with some key differences.

So it's not just design RPC. It also has like a semantic layer for the LLM so that the LLM knows like kind of what to do with it like every tool and stuff like that. Um it is also a stateful protocol and we'll see later what it's important and uh it has also stuff like capability negotiation uh for between the agent and the MCP server. So right now we are we are at the st
