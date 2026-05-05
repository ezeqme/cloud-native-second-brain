---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Connectivity"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Haiyan Meng", "Google", "Evaline Ju", "IBM"]
sched_url: https://kccnceu2026.sched.com/event/2CW5O/agentic-networking-securing-ai-agents-on-kubernetes-haiyan-meng-google-evaline-ju-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Agentic+Networking%3A+Securing+AI+Agents+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google & Evaline Ju, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Haiyan Meng, Google, Evaline Ju, IBM
- Schedule: https://kccnceu2026.sched.com/event/2CW5O/agentic-networking-securing-ai-agents-on-kubernetes-haiyan-meng-google-evaline-ju-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Agentic+Networking%3A+Securing+AI+Agents+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Agentic Networking: Securing AI Agents on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5O/agentic-networking-securing-ai-agents-on-kubernetes-haiyan-meng-google-evaline-ju-ibm
- YouTube search: https://www.youtube.com/results?search_query=Agentic+Networking%3A+Securing+AI+Agents+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KXmPxmNN0fc
- YouTube title: Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google & Evaline Ju, IBM
- Match score: 0.83
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/agentic-networking-securing-ai-agents-on-kubernetes/KXmPxmNN0fc.txt
- Transcript chars: 20418
- Keywords: gateway, access, agents, policy, traffic, server, engineer, agentic, denied, networking, support, essentially, default, basically, proposal, authorization, understand, earlier

### Resumo baseado na transcript

I'm really afraid you know there like 10 people show up but I'm glad so many people are interested in the topic. Um today's topic is about agentic networking securing AI agents on Kubernetes. Lastly, we have our security engineer who may want to build on all of this and be able to do pre-erequest, pre or post response filtering, avoiding attacks such as prompt injection and also data breaches. Um so let's start with the two code without restrictions and uh you have the Kubernetes cluster you have AI agent here and I have two MCP server. Like for example with the architecture we showed earlier I want to be able to allow this AI agent to access the get some get tiny image and read structure but all the other tools should be denied. And uh to verify our API design we also have a reference implementation.

### Excerpt da transcript

Hello everyone, welcome to the latest session. Uh thank you for showing up. I'm really afraid you know there like 10 people show up but I'm glad so many people are interested in the topic. Um today's topic is about agentic networking securing AI agents on Kubernetes. I'm Hayen. I'm a software engineer from Google. >> I'm Evelyn Ju. I'm a software engineer at IBM. Um cube agentic networking is a sub project under sig network. It aims to provide a standardized API for secure governed communication for the next generation of AI agents. The communication could be between agents and agents agents to tools and agents to LMS. And the traffic could be ingress traffic, egress traffic or traffic um east or west traffic. So now we'll talk a bit about the goals of the project. So we aim to have standardized APIs around userfacing goals here. So think user A can talk to tool B and less on specific AI protocols. As we all know the AI protocols today like MCP model context protocol, agent to agent, A2A are really popular today, but we all know how fast the field changes.

We want to make sure our APIs can persist despite how these protocols evolve over time. And next, we want to make sure our APIs can cover different parts of security and governance. So authorization policies, be able to control which agents can talk to which tools, be able to support external authorization, authentication, and also allow for auditable traffic management. And for all this in the wider ecosystem, we want to be able to maintain alignment with existing a APIs, existing protocols, and working groups as well. So we want to align and collaborate with our different groups, including the gateway API, gateway inference extension, and other AI related working groups. So now we want to make our goals a little bit more concrete for our personas in the ecosystem. So first off we have our AI engineer who may want to assign identities to agents, audit their agent actions and essentially understand why an agent gets denied on tool calls or even allowed on tool calls. The platform engineer may want to understand, oh, we want default denied agent traffic, but also be able to control access to these different tools and tool servers and then also observe platformwide failures or denials of tools across the system.

Lastly, we have our security engineer who may want to build on all of this and be able to do pre-erequest, pre or post response filtering, avoiding attacks such as prompt injection and also data
