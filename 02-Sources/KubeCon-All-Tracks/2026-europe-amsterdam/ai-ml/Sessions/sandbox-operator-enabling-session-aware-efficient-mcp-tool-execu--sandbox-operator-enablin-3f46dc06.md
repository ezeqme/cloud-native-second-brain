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
themes: ["AI ML", "Runtime Containers", "Kubernetes Core"]
speakers: ["Mingshan Zhao", "Zhen Zhang", "Alibaba"]
sched_url: https://kccnceu2026.sched.com/event/2CW1c/sandbox-operator-enabling-session-aware-efficient-mcp-tool-execution-in-kubernetes-mingshan-zhao-zhen-zhang-alibaba
youtube_search_url: https://www.youtube.com/results?search_query=Sandbox+Operator%3A+Enabling+Session-Aware%2C+Efficient+MCP+Tool+Execution+in+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution in Kubernetes - Mingshan Zhao & Zhen Zhang, Alibaba

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mingshan Zhao, Zhen Zhang, Alibaba
- Schedule: https://kccnceu2026.sched.com/event/2CW1c/sandbox-operator-enabling-session-aware-efficient-mcp-tool-execution-in-kubernetes-mingshan-zhao-zhen-zhang-alibaba
- Busca YouTube: https://www.youtube.com/results?search_query=Sandbox+Operator%3A+Enabling+Session-Aware%2C+Efficient+MCP+Tool+Execution+in+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1c/sandbox-operator-enabling-session-aware-efficient-mcp-tool-execution-in-kubernetes-mingshan-zhao-zhen-zhang-alibaba
- YouTube search: https://www.youtube.com/results?search_query=Sandbox+Operator%3A+Enabling+Session-Aware%2C+Efficient+MCP+Tool+Execution+in+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vi_VhZLWs9k
- YouTube title: Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution... Mingshan Zhao & Zhen Zhang
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sandbox-operator-enabling-session-aware-efficient-mcp-tool-execution-i/vi_VhZLWs9k.txt
- Transcript chars: 18319
- Keywords: sandbox, another, cruise, actually, checkpoint, sample, running, resource, capability, sandboxes, storage, container, agents, introduce, resume, training, useful, ensure

### Resumo baseado na transcript

Over the past year, I have been mapping Alibaba cloud user deploy AI agent applications on Kubernetes. They are AI scientists who don't know much about Kubernetes while solving their problems. That means agents need to manage their state well so we can keep cost under control. Based on the needs of state management and cost control, we divided the sandbox life cycle into six states. Three of those states pending, running and complete are consistent with the Kubernetes port. When sandbox is idle, we release it resource to save cost but we keep its data so it can resume later with the same context.

### Excerpt da transcript

Good morning everyone. I'm a developer from the Alibaba cloud container service team. Over the past year, I have been mapping Alibaba cloud user deploy AI agent applications on Kubernetes. Those user usually have the same needs large scale and low latency. But that's a big difference now. Many of them more are new are new to Kubernetes. They are AI scientists who don't know much about Kubernetes while solving their problems. We will learn a lot and that's exactly what I'm going to share with you today. Next, let's take a look at the outline. First, business challenge of agent sandbox with containers. Second, container based agent sandbox solution called open cruise agent. Third, how it fits into the weather ecosystem. Fourth, the key technologies that make it work. Finally, our future map road map with AI agent. AI has moved beyond just answer question. Now it can understand what users need, break down problems and actually get things done. is not just for chatting anymore. I can it can do a real work. Let me give you an example.

A user ask help me debug the code and select the uh environment. First the agent call RM to think through the problem and break it down into specific uh steps. Then it use a sandbox to run the code and do dynamic debugging. Based on the result, it calls RM again to try to optimize and fix the code. It runs the code again. And this loop continues continue the code works as expected. Finally, it shows updated code and a summary to the user. This is a typical agent use case. Let's uh uh let's take a look at the business of challenger this scenario brings. The first thing is the data security. In this example, the agent needs to access the user's code where is running. That code is a assert for the user. So it needs to be strictly as related to print any links. Also the agent needs to debug and run that code as the users requested. But that code could do harmful things. If we don't isolated it uh properly, attacker could generate and run malicious code like delete or try to break down to the host and do another uh bad stuff.

So the computer environment need to be safely isolated. Second, there are massive numbers of agents in the agent error. Every user will have multiple agents and each tool call will run it its own independent sandbox. So the number of agents will grow exponentially. The third thing is state management and cost control. A sandbox life cycle can be really short, just a few minutes, but it can also last hours, days,
