---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Peter Jausovec", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyr/project-lightning-talk-whats-new-and-exciting-in-kagent-peter-jausovec-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+And+Exciting+In+Kagent%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: What's New And Exciting In Kagent? - Peter Jausovec, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Peter Jausovec, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyr/project-lightning-talk-whats-new-and-exciting-in-kagent-peter-jausovec-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+And+Exciting+In+Kagent%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What's New And Exciting In Kagent?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyr/project-lightning-talk-whats-new-and-exciting-in-kagent-peter-jausovec-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+And+Exciting+In+Kagent%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O8DslhC1ApU
- YouTube title: Project Lightning Talk: What's New And Exciting In Kagent? - Peter Jausovec, Maintainer
- Match score: 0.889
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-whats-new-and-exciting-in-kagent/O8DslhC1ApU.txt
- Transcript chars: 3894
- Keywords: agents, basically, either, running, support, templates, server, releases, cluster, couple, deploy, declarative, write, reference, skills, models, gateways, images

### Resumo baseado na transcript

Since then we had 100 20 plus releases, a bunch of stars, and I'll tell you first what K agent is. So K agent is an open source framework for basically running AI agents in Kubernetes. And then lastly, the model config, which is basically you're telling us what the provider is, what's the model, and you point to uh your secret in Kubernetes that stores your API key. Long-term memory storage, built-in prompts and templates that I showed. We do distributed tracing, A2A trace propagation, voice support, and bunch of other things.

### Excerpt da transcript

Hi, my name is Peter. I'm from solo and one of the maintainers of K agent. So K agent is an incubating project. We uh are part of the CNCF since last year. Since then we had 100 20 plus releases, a bunch of stars, and I'll tell you first what K agent is. So K agent is an open source framework for basically running AI agents in Kubernetes. So very simple. Uh here's a more detailed look into um the infrastructure uh sorry of the architecture of the project itself. So it comprises of a go controller that's installed into your uh cluster. Uh there's a database, there's a UI portion, and there's a CLI. Um the nice thing about it is we also configure a couple of CRDs for you to use. So if you want to create an agent and deploy it in Kubernetes, you can you have two options. You can use a declarative agent, meaning you don't have to write any code. You just write your instructions. You reference specific tools from MCP servers that you want to use. Uh you can reference skills, and then you you basically pick a model that you want your uh agent to use.

We support multiple model models, everything from OpenAI, Anthropic, Azure, AWS Bedrock, Llama, as well as AI Gateways. So if you're running any of the AI Gateways that front your models, you can point your K agent's agent through that as well. If you want more uh control over your agents, we also have a BYO option where you can build your own agents using either ADK, LangGraph, or QAI uh CrewAI, and then build your agents as docker images, and we can run that as well. Uh so here's how the CRDs uh look like. Uh so left side agent uh is the agent CRD uh where you can pick a model that you want to use uh that you deployed earlier on your cluster. You define your system message. We also support uh uh prompt templates, so you can define your templates and then reuse them between different agents. And then after that we have a tools definition where you basically pick and choose which tools you want your agents to use. On the right-hand side, we have an MCP server uh definition where you can uh either point to an existing MCP server that's already running somewhere.

In this case, we have the one that's deployed in the K agent namespace. And then as you deploy this resource, it will automatically discover the tools for you uh from the MCP server. And then lastly, the model config, which is basically you're telling us what the provider is, what's the model, and you point to uh your secret in Kubernetes that stores your A
