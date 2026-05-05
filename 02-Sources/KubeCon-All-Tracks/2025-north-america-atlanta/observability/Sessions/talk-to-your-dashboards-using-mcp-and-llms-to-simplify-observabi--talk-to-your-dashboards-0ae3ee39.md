---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Prashant Gupta", "Raj Bhensadadia", "Apple"]
sched_url: https://kccncna2025.sched.com/event/27FVS/talk-to-your-dashboards-using-mcp-and-llms-to-simplify-observability-prashant-gupta-raj-bhensadadia-apple
youtube_search_url: https://www.youtube.com/results?search_query=Talk+To+Your+Dashboards%3A+Using+MCP+and+LLMs+To+Simplify+Observability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Talk To Your Dashboards: Using MCP and LLMs To Simplify Observability - Prashant Gupta & Raj Bhensadadia, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Prashant Gupta, Raj Bhensadadia, Apple
- Schedule: https://kccncna2025.sched.com/event/27FVS/talk-to-your-dashboards-using-mcp-and-llms-to-simplify-observability-prashant-gupta-raj-bhensadadia-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Talk+To+Your+Dashboards%3A+Using+MCP+and+LLMs+To+Simplify+Observability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Talk To Your Dashboards: Using MCP and LLMs To Simplify Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVS/talk-to-your-dashboards-using-mcp-and-llms-to-simplify-observability-prashant-gupta-raj-bhensadadia-apple
- YouTube search: https://www.youtube.com/results?search_query=Talk+To+Your+Dashboards%3A+Using+MCP+and+LLMs+To+Simplify+Observability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iS4-WC59a9s
- YouTube title: Talk To Your Dashboards: Using MCP and LLMs To Simplify Observab... Prashant Gupta & Raj Bhensadadia
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/talk-to-your-dashboards-using-mcp-and-llms-to-simplify-observability/iS4-WC59a9s.txt
- Transcript chars: 31374
- Keywords: dashboard, observability, context, dashboards, satellite, server, systems, control, source, language, mission, metrics, metric, graphana, client, servers, create, natural

### Resumo baseado na transcript

Welcome to our session today uh talk to your dashboards where we talk about using model context protocol and large language models to simplify observability. My focus areas are observability, machine learning and natural language processing. So instead of analyzing the mission, we often spend half of our day trying to figure out which dashboard even has the right query. And this is where observability can start to cost in engineering hours, alert fatigue, and slow incident responses. So each operator then builds their own dashboard, panels, queries, and alerts around these metrics. And the reason it has become so complex today is observability today is fragmented by design.

### Excerpt da transcript

Welcome to our session today uh talk to your dashboards where we talk about using model context protocol and large language models to simplify observability. So before we get started we'll take a moment to introduce ourselves. Uh I'm Prashant. I'm a machine learning engineer at Apple. My focus areas are observability, machine learning and natural language processing. >> Hi I'm Raj. I'm also a machine learning engineer at Apple. I am I work with obser observability team and my background is also in observability machine learning and data science. >> So let's start with what the session is really about demystifying how we work with our observability systems. So today our monitoring stacks are incredibly powerful but they are also fairly complex. So in this talk we'll focus on what is model context protocol and why it matters. um how we can make observability more accessible using natural language, how to make different tools work together crossplatform interoperability, and finally how we can add guardrails for safe automation.

So this talk is for anyone who's managing observability systems or monitoring pipelines or basically anyone who's ever said why my dashboards are not working again. So to talk about this, we thought it'd be interesting to take a scenario where you're responsible for a lot of critical systems which emit a lot of data and we're not having observability can be catastrophic. So let's imagine we're running a mission control for a space program. So we have got six satellites, three rovers, and 100 engineers who are monitoring power, communication, battery life across countless dashboards at any given time. So every spacecraft has its own signal, its own dashboards, panels, and its own quirks. So instead of analyzing the mission, we often spend half of our day trying to figure out which dashboard even has the right query. And this is where observability can start to cost in engineering hours, alert fatigue, and slow incident responses. So let's zoom into these satellites. Now, every satellite emits its own data.

That's like power, battery, altitude, latency, and a lot more. And in observability terms, these are our metrics, traces, and logs. So each operator then builds their own dashboard, panels, queries, and alerts around these metrics. Now, this is how observability often works in distributed environments. If each new mission means new data, new visualizations, new configs, it also means new potential breaking points. And this is how t
