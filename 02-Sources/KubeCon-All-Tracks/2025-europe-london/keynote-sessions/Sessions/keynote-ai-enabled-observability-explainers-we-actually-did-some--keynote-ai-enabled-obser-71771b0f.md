---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["AI ML", "Observability"]
speakers: ["Vijay Samuel", "Principal MTS", "Architect", "eBay"]
sched_url: https://kccnceu2025.sched.com/event/1txBX/keynote-ai-enabled-observability-explainers-we-actually-did-something-with-ai-vijay-samuel-principal-mts-architect-ebay
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+AI+Enabled+Observability+Explainers+-+We+Actually+Did+Something+With+AI%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: AI Enabled Observability Explainers - We Actually Did Something With AI! - Vijay Samuel, Principal MTS, Architect, eBay

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Vijay Samuel, Principal MTS, Architect, eBay
- Schedule: https://kccnceu2025.sched.com/event/1txBX/keynote-ai-enabled-observability-explainers-we-actually-did-something-with-ai-vijay-samuel-principal-mts-architect-ebay
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+AI+Enabled+Observability+Explainers+-+We+Actually+Did+Something+With+AI%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: AI Enabled Observability Explainers - We Actually Did Something With AI!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txBX/keynote-ai-enabled-observability-explainers-we-actually-did-something-with-ai-vijay-samuel-principal-mts-architect-ebay
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+AI+Enabled+Observability+Explainers+-+We+Actually+Did+Something+With+AI%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j0AqGpC_pp4
- YouTube title: Keynote: AI Enabled Observability Explainers - We Actually Did Something With AI! - Vijay Samuel
- Match score: 1.002
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-ai-enabled-observability-explainers-we-actually-did-something/j0AqGpC_pp4.txt
- Transcript chars: 13852
- Keywords: llm, explainer, triage, trace, analyze, critical, observability, everything, capabilities, actually, generate, basically, explainers, saying, roughly, engineering, worked, within

### Resumo baseado na transcript

This is usually when my kids give me a call through my wife's phone, but the good thing is they're they're in the audience today. Um when I say we actually did something with AI, it doesn't mean that we we're the only ones who have done something, but if you if you have listened to my talks in the past, I'm big on storytelling. And the scale of operations has exploded over the last uh 5 years or so. And uh from a scale perspective, we generate 15 pabytes of logs per day. The fundamental problem with the site becoming more and more complex is that as humans we have limits to how much we can comprehend um at at any given point in time. The amount of time it takes to see through terabytes worth of uh logs is a lot.

### Excerpt da transcript

Hello everyone. Good to see you all. This is usually when my kids give me a call through my wife's phone, but the good thing is they're they're in the audience today. I love the three of you a lot. We are here to talk about AI enabled explainers uh for observability. Um when I say we actually did something with AI, it doesn't mean that we we're the only ones who have done something, but if you if you have listened to my talks in the past, I'm big on storytelling. And over the next 10 to 15 minutes uh I'm going to tell a story about how uh we came up with the concept of explainers and how we are using it right now and where we see it go in the future. I keep saying we who are we are eBay. eBay today is uh present in a over uh in in 190 markets with 2.3 billion live listings, 134 million active buyers worldwide and the volume of uh money we transact just on mobile devices is uh roughly $13 billion. Who am I? Uh my name is Vijay Samuel. I'm a principal MTS architect for the reliability engineering organization uh at eBay.

uh uh my primary responsibilities are around observability s surite operations and I should say it's been an absolute blessing for me to be with eBay for over uh for around 13 years and I've been with eBay straight out of college. Uh I'm a big open source enthusiast. Uh started off with Drizzle DB. Shout out to anyone uh in the audience who has worked on Drizzle so far. Um since then I worked on worked with multiple communities like open telemetry, Prometheus and more. Let's start off by saying that observability is intense. Out of the 10 13 years at eBay, uh 10 of them I've spent uh on either logging or monitoring or now observability as we like to call it. And the scale of operations has exploded over the last uh 5 years or so. Complexity doesn't cease to slow down. Within eBay, we have roughly 4,600 microservices that power the actual eBay site. And uh from a scale perspective, we generate 15 pabytes of logs per day. Uh 10 billion active time series and 10 million spans per second that's sampled at roughly uh 2%.

So it's not a trivial amount of data that we have to deal with. And so uh incidents impact our ability to provide the highest quality experience to our customers. And that's what we we we tried to do. The fundamental problem with the site becoming more and more complex is that as humans we have limits to how much we can comprehend um at at any given point in time. So if you take manual triage as an example, the time it takes to
