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
speakers: ["Christian Posta", "Solo.io"]
sched_url: https://kccnceu2026.sched.com/event/2CW8C/enterprise-challenges-with-mcp-adoption-christian-posta-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Enterprise+Challenges+with+MCP+Adoption+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Enterprise Challenges with MCP Adoption - Christian Posta, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Christian Posta, Solo.io
- Schedule: https://kccnceu2026.sched.com/event/2CW8C/enterprise-challenges-with-mcp-adoption-christian-posta-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Enterprise+Challenges+with+MCP+Adoption+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Enterprise Challenges with MCP Adoption.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW8C/enterprise-challenges-with-mcp-adoption-christian-posta-soloio
- YouTube search: https://www.youtube.com/results?search_query=Enterprise+Challenges+with+MCP+Adoption+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ipKgoKSkBnc
- YouTube title: Enterprise Challenges with MCP Adoption - Christian Posta, Solo.io
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/enterprise-challenges-with-mcp-adoption/ipKgoKSkBnc.txt
- Transcript chars: 25471
- Keywords: gateway, server, enterprise, access, client, around, registry, servers, identity, everything, provider, enterprises, bricks, github, inside, probably, connect, directly

### Resumo baseado na transcript

Some of you may be here to try to find a nice quiet place to take a nap. Um we're going to be talking about MCP adoption in the organizations that I've been working with uh over the last year or so. Um by then is around when the spec kind of introduced more things around security. Even though they probably aren't targeted, the uh the you know, the spec uh what it says about security and off isn't targeted primarily at enterprise. And uh and a number of other, you know, um challenges that became evident, became clear. And they admit that yeah, up until now enterprises have run into some uh these predictable problems.

### Excerpt da transcript

First of all, thank you all so much. The KubeCon organizers for having me. Thank you all for showing up in the middle of the afternoon here. Um I know it's been a a long conference, maybe a long day. Uh I'll try to make it worth your while. Some of you may be here to try to find a nice quiet place to take a nap. I appreciate that also. Um we're going to be talking about MCP adoption in the organizations that I've been working with uh over the last year or so. And uh and some of the challenges that they've experienced going from pilot and and POC into how do we get this into production and enable more of the organization to adopt this type of technology to build AI agent uh type applications. Uh and and do this do this safely and do it at scale. So, uh let's get going. My name is is Christian Posta. I'm the global field CTO at a company called solo.io. Uh we work on cloud networking, API gateways, service mesh. We're creators of Istio. You may have heard of that. Um and then more recently over the last year, year and a half, uh K agent, agent gateway.

Uh this morning we announced our donation to the CNCF of our open source agent registry. So, everything we build around AI um um networking and security uh for platform engineers is rooted in open source. We are uh very heavy contributors to the open source communities. All right. So, we'll be talking about MCP or model context protocol. Some of you may have uh heard of it or may know of it, but it is a protocol to allow our AI models to talk to and use uh data and functionality that live outside of the uh of the AI model. And the idea is instead of custom writing code to talk to particular API or particular database or a a SAS uh set of endpoints or data, let's unify the protocol layer so that we don't have to have this custom code and we can just plug and play any of these adapters uh as we need. And uh and eventually the model could potentially discover these on the fly and and use data as it as it needs. Now, just like anything in AI these days, we've seen MCP hit the uh you know, the the hype wave.

And um you know, starting from it it's released in November 24 up through, you know, even even recently. I would say in in my own experience, around the middle of uh like let's say the summer of 2025 is when we saw enterprises start to go, you know, headfirst into MCP adoption trying to figure out what it looks like inside their enterprises. Um by then is around when the spec kind of introduced more things ar
