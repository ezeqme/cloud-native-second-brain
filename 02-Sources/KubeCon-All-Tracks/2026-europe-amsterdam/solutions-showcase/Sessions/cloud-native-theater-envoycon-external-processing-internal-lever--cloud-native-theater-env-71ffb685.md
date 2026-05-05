---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Networking"]
speakers: ["Jens Kat", "ING"]
sched_url: https://kccnceu2026.sched.com/event/2EFza/cloud-native-theater-envoycon-external-processing-internal-leverage-mcp-tool-calls-to-rest-with-envoy-jens-kat-ing
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+External+Processing%2C+Internal+Leverage%3A+MCP+Tool+Calls+to+REST+with+Envoy+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls to REST with Envoy - Jens Kat, ING

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jens Kat, ING
- Schedule: https://kccnceu2026.sched.com/event/2EFza/cloud-native-theater-envoycon-external-processing-internal-leverage-mcp-tool-calls-to-rest-with-envoy-jens-kat-ing
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+External+Processing%2C+Internal+Leverage%3A+MCP+Tool+Calls+to+REST+with+Envoy+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls to REST with Envoy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFza/cloud-native-theater-envoycon-external-processing-internal-leverage-mcp-tool-calls-to-rest-with-envoy-jens-kat-ing
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+External+Processing%2C+Internal+Leverage%3A+MCP+Tool+Calls+to+REST+with+Envoy+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4XciSKk-Rek
- YouTube title: Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls... Jens Kat
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-envoycon-external-processing-internal-leverage-mc/4XciSKk-Rek.txt
- Transcript chars: 16519
- Keywords: envoy, external, request, specific, processor, processing, mesh, agents, already, response, server, implement, filter, production, leverage, support, context, protocol

### Resumo baseado na transcript

I will talk about how we use Envoy to support AI agentic AI use cases in ING. I'm a senior software engineer at ING uh in the service mesh team and ING is a bank. Would we burden them with implementing MCP servers in in Python with fast MCP uh in Go in whatever language and have basically the the the begin state as we had with microservices issues with discoverability, security, reliability. So on top of that we would have to build observability, resiliency and security or do that in a sidecar fashion. So the use cases are not blocked by backlogs of uh we don't have the priority to uh work or implement MCP for this use case. And this man this means that we can scale down our custom efforts and go back to more um mainline envoy.

### Excerpt da transcript

Hello Envoy Con CubeCon. Thanks for having me today. I will talk about how we use Envoy to support AI agentic AI use cases in ING. So this won't be a talk about AI but about enabling AI. Um my name is Jen Scott. I'm a senior software engineer at ING uh in the service mesh team and ING is a bank. uh we service around 40 million customers uh worldwide. We have about 60,000 people of which a third are working in tech and my team service mesh team is uh providing support and uh making sure everything connects uh reliably secure in production for over 2,000 services. Uh indeed as uh Erica said last virtual envoy con uh in October we uh me and a colleague status explained how we started switching to envoy for all our production workloads um today. So I won't be talking about uh using AI or LLMs but I will sketch why we are using envoy and how we are using envoy to support agentic AI use cases using the external processing feature. ing has a mature service mesh. We have all kinds of services connecting together built with Spring Boot, built with Go, C#, Python, whatnot.

And uh the connectivity is made possible by Android. Now since last year the AI agents and the use cases for AI agents came along and those AI agents to be u to be doing something u meaningful need access to the world to our ing data. So the question was how can we connect the AI agent to the uh ING specific data that we already have. This is where the model context protocol could help us out. So MCP model context protocol is a standard uh to connect AI systems, AI agents with external systems. It's an open standard. It was um invented or proposed publicly uh over a bit over a year ago, end of 2024. It's now adopted by uh many more besides Enthropic, Google and others. It's already 60 months old or young. Well, time flies in the in the AI world. And basically, it's a JSON RPC protocol where you have a client MCP host that talks to an MCP server where tools, resources, prompts are being hosted. Um, and this would un unlock us and enable us to do a Gentic AI together with our service mesh. Now, the question was where do we enable this kind of MCP implementation?

Where do we put that? And what does that mean for the teams more than a few hundred teams that we have running in production? Would we burden them with implementing MCP servers in in Python with fast MCP uh in Go in whatever language and have basically the the the begin state as we had with microservices issues with discoverability, securi
