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
themes: ["Project Opportunities"]
speakers: ["Flynn", "Technical Evangelist"]
sched_url: https://kccnceu2026.sched.com/event/2EFyE/project-lightning-talk-mcp-routing-in-linkerd-flynn-technical-evangelist
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+MCP+Routing+In+Linkerd+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: MCP Routing In Linkerd - Flynn, Technical Evangelist

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Flynn, Technical Evangelist
- Schedule: https://kccnceu2026.sched.com/event/2EFyE/project-lightning-talk-mcp-routing-in-linkerd-flynn-technical-evangelist
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+MCP+Routing+In+Linkerd+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: MCP Routing In Linkerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyE/project-lightning-talk-mcp-routing-in-linkerd-flynn-technical-evangelist
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+MCP+Routing+In+Linkerd+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tb8rSQz1MGE
- YouTube title: Project Lightning Talk: MCP Routing In Linkerd - Flynn, Technical Evangelist
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-mcp-routing-in-linkerd/tb8rSQz1MGE.txt
- Transcript chars: 5028
- Keywords: interesting, request, routing, little, server, infrastructure, observability, protocol, access, remember, particular, linkertdee, mesh, application, actually, speaking, requests, linker

### Resumo baseado na transcript

If you are not familiar with LinkertDee, we are a service mesh, which is to say we're an infrastructure component. We worry about security, reliability, observability underneath your application so that your application has to worry less about it.

### Excerpt da transcript

I'm Flynn. I'm a technical evangelist for the Linkard project. I'm going to talk to you about MCP routing in LinkertDee. If you are not familiar with LinkertDee, we are a service mesh, which is to say we're an infrastructure component. We worry about security, reliability, observability underneath your application so that your application has to worry less about it. If you are unfamiliar with MCP, we are the first mesh that announced support for it back in Atlanta. MCP is a protocol that you've probably heard far too much about. The idea is that if we have an agent that is doing things on behalf of a user, MCP is a protocol that will allow the agent access to tools outside the agent. So it can do things that are more interesting than just stringing together text. If we drill into this a little bit, what we're actually doing is speaking MCP from the agents to an MCP server which in turn controls the tool. If we drill into it a little bit further in a link installation, all of these things are running in pods.

Every pod gets its own linky proxy. So the agent is actually speaking making MTP requests to its linker project proxy proxy. Wow. Which has to decide where to route that to another linker proxy to get access to an MCP server to get access to a tool. The first place that this gets interesting is that MCP is a stateful protocol. So if we have an agent that is doing things and it has just made a request that gets routed to the top MCP server, it is an error to route a second request in that session to a different MCP server. In itself, this is not a big deal if you're an infrastructure element like we are. Staple routing is a thing that we've had to deal with for decades. It's mostly just a thing we have to remember to do. Where it gets weirder is if we look down into the requests themselves. MCP uses JSON RCP inside HTTP. So we have all the usual HTTP goodness up front. But if you look a little closer, you find that the interesting things about this are buried in the body, not in the headers. Even more interesting, if something goes wrong, remember we want to do observability.

We want to let you know when things go wrong. If we get an error response from one of these tools, you're still going to see an HTTP 200, everything is fine, and you have to again look into the body to find out what went wrong or even that anything went wrong. So an infrastructure system that's only doing HTTP observability will tell you everything is great even though your tool
