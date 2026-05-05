---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Erik Lindblad", "Erica Manno", "Spotify"]
sched_url: https://kccnceu2025.sched.com/event/1txEU/how-we-moved-spotify-to-a-proxyless-grpc-service-mesh-erik-lindblad-erica-manno-spotify
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Moved+Spotify+To+a+Proxyless+gRPC+Service+Mesh+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How We Moved Spotify To a Proxyless gRPC Service Mesh - Erik Lindblad & Erica Manno, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Erik Lindblad, Erica Manno, Spotify
- Schedule: https://kccnceu2025.sched.com/event/1txEU/how-we-moved-spotify-to-a-proxyless-grpc-service-mesh-erik-lindblad-erica-manno-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Moved+Spotify+To+a+Proxyless+gRPC+Service+Mesh+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How We Moved Spotify To a Proxyless gRPC Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEU/how-we-moved-spotify-to-a-proxyless-grpc-service-mesh-erik-lindblad-erica-manno-spotify
- YouTube search: https://www.youtube.com/results?search_query=How+We+Moved+Spotify+To+a+Proxyless+gRPC+Service+Mesh+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2_ECK6v_yXc
- YouTube title: How We Moved Spotify To a Proxyless gRPC Service Mesh - Erik Lindblad & Erica Manno, Spotify
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-we-moved-spotify-to-a-proxyless-grpc-service-mesh/2_ECK6v_yXc.txt
- Transcript chars: 28730
- Keywords: discovery, spotify, traffic, nameless, control, configuration, protocol, client, running, region, shameless, mesh, clients, called, proxyless, around, features, design

### Resumo baseado na transcript

So this talk is about how Spotify outgrew its service discovery shoes and how we went about finding a new pair of shoes and instead of 1 million DNS shoes, we now have 1 million XDS shoes. So, we'll cover what problems we were facing and why we ended up designing around XDS um design and implementation choices and how we transparently rolled this out without any adverse effects. uh it controls regional redirects on a uh per service and per protocol level and then it subscribes to endpoint slice changes in our Kubernetes clusters to provide service discovery to services running in Kubernetes. The the component that does the this Kubernetes business is is a later addition to nameless and we call it shameless. And we were considering mainly stuff around reliability, scalability and extensibility. Uh and uh it needed to fit the hetrogenous service architecture we have at Spotify.

### Excerpt da transcript

Hello everyone. So this talk is about how Spotify outgrew its service discovery shoes and how we went about finding a new pair of shoes and instead of 1 million DNS shoes, we now have 1 million XDS shoes. This will all make sense. Uh give a minute. Yes. So, we'll cover what problems we were facing and why we ended up designing around XDS um design and implementation choices and how we transparently rolled this out without any adverse effects. There's an asterisk here after that, but I'm sure we'll get to that as well. I'm Eric. I work as a staff engineer in Spotify's core infrastructure um product area. And with me I have Erica who's a senior engineer and subject matter expert in service our service networking team. So first off a little technical context about Spotify stack. So it's a micros service architecture that runs on GKE. We were originally on prem and moved to GCP in I think 2017. uh the first running VM with the custom orchestration and first first we're running on VMs with a custom orchestration uh layer and then sorry yeah um then we move to GKE and and Kubernetes so and yeah the majority of services are written in Java and using an in-house Java framework but there's also a smaller set of services written in other languages like Python and and NodeJS and yeah and yeah we're really big you can see some numbers on the slide here that should give you some kind of sense of scale.

Uh most of the service to service traffic is gRPC I think 75% give or take and then we use proxyless gpc which means then that gc clients connect directly to servers as opposed to traditional service measures where uh that might make use of forwarding proxies and sidecars. 25% of uh the traffic that remains after GC is a proprietary protocol which we're migrating off and while most of our internet ingress is in HTTP there's very little HTTP that goes between services. Um what else? We're deployed in five GCP regions and we have a regional regional failure domain uh where each region can provide most of the end user services independently. But it's possible for us to make for services to make cross region calls for example when a service has a regional outage or if the service isn't deployed in all regions which happens for our smaller services. So here's a basic sketch of Spotify's service discovery system. It's called Nameless. It was created in 2013 to replace a bunch of bash scripts that were managing DNS zone files.

Uh and why it's called nameless, we don't remembe
