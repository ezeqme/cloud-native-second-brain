---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["AI ML", "Networking"]
speakers: ["Idit Levine", "Solo.io"]
sched_url: https://kccncna2024.sched.com/event/1i7nJ/harnessing-the-power-of-envoy-proxy-for-building-an-llm-gateway-idit-levine-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Harnessing+the+Power+of+Envoy+Proxy+for+Building+an+LLM+Gateway+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Harnessing the Power of Envoy Proxy for Building an LLM Gateway - Idit Levine, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Idit Levine, Solo.io
- Schedule: https://kccncna2024.sched.com/event/1i7nJ/harnessing-the-power-of-envoy-proxy-for-building-an-llm-gateway-idit-levine-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Harnessing+the+Power+of+Envoy+Proxy+for+Building+an+LLM+Gateway+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Harnessing the Power of Envoy Proxy for Building an LLM Gateway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nJ/harnessing-the-power-of-envoy-proxy-for-building-an-llm-gateway-idit-levine-soloio
- YouTube search: https://www.youtube.com/results?search_query=Harnessing+the+Power+of+Envoy+Proxy+for+Building+an+LLM+Gateway+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w9rOcy2tGr4
- YouTube title: Harnessing the Power of Envoy Proxy for Building an LLM Gateway - Idit Levine, Solo.io
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/harnessing-the-power-of-envoy-proxy-for-building-an-llm-gateway/w9rOcy2tGr4.txt
- Transcript chars: 35962
- Keywords: basically, actually, request, gateway, envoy, models, talking, application, typical, caching, understand, second, little, usually, semantic, access, customer, important

### Resumo baseado na transcript

so thanks so much for attending our session and this is all about AI gway specifically about Envoy and we're going to start by basically talk first of all about why you need gway then understand why AI adoption in Enterprise what we see working with all our customer what people doing there how it's usually come then we're going to talk oops about Envoy as a I gway what did we do there implementation DET and so on we'll have tons of demo and we're going to share with

### Excerpt da transcript

so thanks so much for attending our session and this is all about AI gway specifically about Envoy and we're going to start by basically talk first of all about why you need gway then understand why AI adoption in Enterprise what we see working with all our customer what people doing there how it's usually come then we're going to talk oops about Envoy as a I gway what did we do there implementation DET and so on we'll have tons of demo and we're going to share with you some of our learning so first of all we present ourselves so my name is ID LaVine I'm the founder in the SE of solo um and I'm Eton yarmush um I thought the formatting is wrong whatever I tried um I'm a senior architect here at solo and the AI Gateway lead exactly okay so and and should we represent SAA I think they know yeah okay SAA is a company basically doing a lot of stuff around networking API gway service Smash and and honestly everything we need to do in order to make our customer and user successful and scaling um okay so let's start with talking about it again just I think all of you know that but I just wanted to make the point is that you know the idea with a gway is pretty simple if we were not going to do the gway that mean that you need to put all those like operation code inside your micros service so or application and usually it's not healthy because then if you have any problem you need to upgrade a library for instance you will need to go and basically redeploy that application so it's really not healthy to put the business logic with the Core Business logic of your application so ideally we will want to separate it and by the way by doing this we kind of like nicely working with the with the um with the Persona because that way the application on user only need to work with the co- business USIC but they know they really do not care about security and all the other stuff and the platform engineering team getting back the power to their hand they can actually Force Security logging monitoring and everything else that went need in order to make sure that the application will run well in production okay so we understand this one let's first understand do we need a new gway is there anything that we need of course we don't need a gway a new gway but do we need a new is there a new use case even for a gway okay we can actually use a regular ones and I think that even in Solo honestly it took us time to understand that this is a real thing right we're working with our custome
