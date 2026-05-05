---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Connectivity"
themes: ["AI ML"]
speakers: ["John Howard", "Solo.io"]
sched_url: https://kccncna2025.sched.com/event/27FWf/lessons-applied-building-a-next-generation-ai-proxy-john-howard-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Applied+Building+a+Next-generation+AI+Proxy+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Lessons Applied Building a Next-generation AI Proxy - John Howard, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: John Howard, Solo.io
- Schedule: https://kccncna2025.sched.com/event/27FWf/lessons-applied-building-a-next-generation-ai-proxy-john-howard-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Applied+Building+a+Next-generation+AI+Proxy+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Lessons Applied Building a Next-generation AI Proxy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWf/lessons-applied-building-a-next-generation-ai-proxy-john-howard-soloio
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Applied+Building+a+Next-generation+AI+Proxy+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qa5vSE86z-s
- YouTube title: Lessons Applied Building a Next-generation AI Proxy - John Howard, Solo.io
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/lessons-applied-building-a-next-generation-ai-proxy/qa5vSE86z-s.txt
- Transcript chars: 25490
- Keywords: envoy, gateway, external, requirements, control, request, wanted, actually, support, started, native, natively, functionality, authorization, networking, features, extension, directly

### Resumo baseado na transcript

I'm John Howard from Solo.io and I'm really excited to be here talking to you guys today about lessons applied building a next generation AI proxy. Uh, before we get into the new stuff, I think it's pretty important to look back on the kind of foundations on why we felt it was necessary to build a new thing in the first place. Um, so we started looking at the problems of why you may need an AI gateway. And I may have a single request that has a million tokens and cost me $5 for that one single request, right? Um, and how this worked was we took Envoy and it didn't natively solve these problems, but it has a lot of extensibility points. But we also saw that people just because they have AI use cases doesn't take away all the standard API gateway use cases like retries and timeouts and logging and tracing and authorization policies.

### Excerpt da transcript

All right. Hello everyone. Welcome. Uh, thanks for coming. I'm John Howard from Solo.io and I'm really excited to be here talking to you guys today about lessons applied building a next generation AI proxy. Uh, before we get into the new stuff, I think it's pretty important to look back on the kind of foundations on why we felt it was necessary to build a new thing in the first place. Uh and I want to start way back by giving a very probably very loosely accurate view of the kind of the history and evolution of proxies over time. Um this was all long before my time. So my understanding was back in the day Apache HP server was was kind of the popular thing and as requirements on infrastructure evolved uh things started to shift right we started to see larger scales in terms of number of requests and connections and some things like engine X started popping up to become more dominant positions solving things like scaling to 10,000 connections in a single proxy for instance a number that is now fairly small um fast forward another 10 12 years we start seeing microservices rising like crazy and putting more pressure on the infrastructure again to help solve observability connectivity dynamic programming as pods scale up down left and right uh and that's where envoy really started to take off envoy is you know largest most popular proxy in the CNCF widely adopted and now if we fast forward another 10 years or so we're starting to see AI dominate the infrastructure space in terms of new deployments and requirements and we started to look at what are the needs that infrastructure or that AI is bringing onto the network, right?

And can we meet these with Envoy or is this another step for an evolution? Um, so we started looking at the problems of why you may need an AI gateway. And there's it's kind of a long nuance topic. I had a talk at actually yesterday that was 30 minutes on this, but you guys get 30 seconds, so bear with me here. Um, some of the broad uh requirements may be things like deep native LM observability. So things that are like aware of the actual prompts and responses from LLMs so that I can understand not just that I got a 200 response from the AI model, but that I got this big body of text um and that it said something like, "Hey, you're ugly or something mean and we need to go audit to understand what was going on with this non-deterministic AI model, right? We may need LM aware rate limiting. So we're not just dealing with requests anymore. W
