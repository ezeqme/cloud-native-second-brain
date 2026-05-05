---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Service Mesh"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Mark Mandel", "Google Cloud"]
sched_url: https://kccnceu2023.sched.com/event/1HyZI/agones-+-quilkin-kubernetes-game-server-orchestration-and-udp-service-mesh-mark-mandel-google-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Agones+%2B+Quilkin%3A+Kubernetes+Game+Server+Orchestration+and+UDP+Service+Mesh+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Agones + Quilkin: Kubernetes Game Server Orchestration and UDP Service Mesh - Mark Mandel, Google Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mark Mandel, Google Cloud
- Schedule: https://kccnceu2023.sched.com/event/1HyZI/agones-+-quilkin-kubernetes-game-server-orchestration-and-udp-service-mesh-mark-mandel-google-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Agones+%2B+Quilkin%3A+Kubernetes+Game+Server+Orchestration+and+UDP+Service+Mesh+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Agones + Quilkin: Kubernetes Game Server Orchestration and UDP Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZI/agones-+-quilkin-kubernetes-game-server-orchestration-and-udp-service-mesh-mark-mandel-google-cloud
- YouTube search: https://www.youtube.com/results?search_query=Agones+%2B+Quilkin%3A+Kubernetes+Game+Server+Orchestration+and+UDP+Service+Mesh+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RHOHkIYdrqw
- YouTube title: Agones + Quilkin: Kubernetes Game Server Orchestration and UDP Service Mesh - Mark Mandel
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/agones-quilkin-kubernetes-game-server-orchestration-and-udp-service-me/RHOHkIYdrqw.txt
- Transcript chars: 31480
- Keywords: servers, server, actually, quilkin, dedicated, running, little, proxies, inside, information, routing, filters, source, talking, traffic, everything, basically, config

### Resumo baseado na transcript

hello everybody how are we doing today on the last day of kubecon good yeah I feel about the same yeah that was that was about as half-hearted as I was expecting wonderful uh thank you very much for joining me today we're going to talk about uh agones and quilkin uh open source multiplayer game server orchestration and service National kubernetes I think I managed to fit all the buzzwords in almost um thank you very much for hanging out with me uh a little about me before we

### Excerpt da transcript

hello everybody how are we doing today on the last day of kubecon good yeah I feel about the same yeah that was that was about as half-hearted as I was expecting wonderful uh thank you very much for joining me today we're going to talk about uh agones and quilkin uh open source multiplayer game server orchestration and service National kubernetes I think I managed to fit all the buzzwords in almost um thank you very much for hanging out with me uh a little about me before we get started uh my name is Mark Mandel or Mark Mandel depending on if I'm using my American or Australian accent I technically develop a relations for gaming on Google Cloud um I'm founder I'm one of the founders I should say and maintainers on both of the open source projects we're talking about today which is at corners and Culkin you can find all my details up here uh before we get started I would love to pull the room because this is going to be a distributed audience and possibly a little different from some of the normal people I give this to who here works in the video game industry small pocket of people over here okay cool that sounds fine who here went to uh Joseph's talk earlier today about agonism PlayStation okay a lot of you got some giving not everyone okay that's perfect who here likes video games okay now I understand what's going on awesome awesome no that's great that's great that's great okay cool um we're gonna be talking about some fun stuff today and we're we're we've got half an hour so some of it'll be a little surface but hopefully I'll be able to give you enough information to be able to go oh that's interesting cool so what do I want to talk about today um I want to talk about fast-paced real-time multiplayer games um your OverWatch is your fortnites your rocket leagues all those kind of fun stuff um and I want to talk about uh kind of two interesting kind of problems both a little bit about how we host and scale them but also how we look at securing and monitoring and doing interesting things that's on a service Meshi kind of stuff with the UDP traffic that also happens um with game server workloads and we'll dig a little bit into both and we'll talk about how some of that stuff works as well before we go too deep um I am going to be doing a live demo because I like being afraid um I'll be using a open source uh game called sonatic who here has heard of sonotic I'm guessing like three people yep okay I counted that about right perfect um I'm gonna use an ope
