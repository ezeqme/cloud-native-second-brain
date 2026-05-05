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
themes: ["Networking"]
speakers: ["Isaac Wilson", "The Trade Desk"]
sched_url: https://kccncna2025.sched.com/event/27FVe/on-prem-load-balancing-reimagined-serving-20-million-qps-with-gateway-api-and-envoygateway-isaac-wilson-the-trade-desk
youtube_search_url: https://www.youtube.com/results?search_query=On-Prem+Load+Balancing+Reimagined%3A+Serving+20+Million+QPS+With+Gateway+API+and+EnvoyGateway+CNCF+KubeCon+2025
slides: []
status: parsed
---

# On-Prem Load Balancing Reimagined: Serving 20 Million QPS With Gateway API and EnvoyGateway - Isaac Wilson, The Trade Desk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Isaac Wilson, The Trade Desk
- Schedule: https://kccncna2025.sched.com/event/27FVe/on-prem-load-balancing-reimagined-serving-20-million-qps-with-gateway-api-and-envoygateway-isaac-wilson-the-trade-desk
- Busca YouTube: https://www.youtube.com/results?search_query=On-Prem+Load+Balancing+Reimagined%3A+Serving+20+Million+QPS+With+Gateway+API+and+EnvoyGateway+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre On-Prem Load Balancing Reimagined: Serving 20 Million QPS With Gateway API and EnvoyGateway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVe/on-prem-load-balancing-reimagined-serving-20-million-qps-with-gateway-api-and-envoygateway-isaac-wilson-the-trade-desk
- YouTube search: https://www.youtube.com/results?search_query=On-Prem+Load+Balancing+Reimagined%3A+Serving+20+Million+QPS+With+Gateway+API+and+EnvoyGateway+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kHChbblwVwk
- YouTube title: On-Prem Load Balancing Reimagined: Serving 20 Million QPS With Gateway API and Envoy... Isaac Wilson
- Match score: 0.994
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/on-prem-load-balancing-reimagined-serving-20-million-qps-with-gateway/kHChbblwVwk.txt
- Transcript chars: 28531
- Keywords: envoy, gateway, haroxy, traffic, pretty, environment, running, cluster, actually, single, backends, default, connection, started, center, basically, console, available

### Resumo baseado na transcript

Uh specifically um what our on-prem load balancing environment looked like and what our migration was over to Kubernetes gateway API. Uh yeah, so for today I'll give you a little bit of the history of what Kubernetes has been like at the trade desk. Uh and then we also have pretty high scale uh roughly like o over 20 million QPS uh like queries per second which um may or may not include a single bid request but I don't want to dive too deep on that. Um as far as Kubernetes uh the team started in 2020 uh at the time like many C or many other uh companies we were just using it for green field applications and just trying to figure out how this thing could work. data centers uh which is where the majority of our our compute is uh and that's also where our more critical workloads run uh and we have some pretty big clusters and uh some interesting challenges to solve for uh so it's been a fun Uh and so if you're familiar with Kubernetes topology zones, that mostly translates to a rack in a data center for us.

### Excerpt da transcript

Yeah, thanks everybody for coming. My name is Isaac Wilson. I'm an engineer at the trade desk. And today I'm going to talk to you about load balancing. Uh specifically um what our on-prem load balancing environment looked like and what our migration was over to Kubernetes gateway API. Uh yeah, so for today I'll give you a little bit of the history of what Kubernetes has been like at the trade desk. Uh I'll walk through what our old architecture was as well as some of the challenges that we wanted to fix. uh a quick intro on gateway API and envoy gateway uh what our migration strategy looked like uh some lessons learned that hopefully you can take away and reuse in your own uh migrations and then finally go through some of the actual outcomes and things that made it worth doing. Uh yeah, so you guys have probably all seen other uh migration stories in in in general. Uh but for us, this was a a pretty big state, pretty big step. Uh the trade desk, we provide an objective, transparent, and an independent platform for ad buying.

Uh what that actually means is if you've ever gone to a website with ads on the side or if you use a streaming service and there's an ad break uh in a fraction of a second uh those providers reach out to real-time bidding platforms like ours and in less than 100 milliseconds we will run an auction and effectively whoever pays the most to serve some content in in front of your eyeballs they will typically win. Um so that 100 milliseconds that includes uh the like everything from the connection establishment time on the the client side as well as traversing all the network paths in between on our side we try to uh process those requests in under five milliseconds. Uh so just to like put some perspective around it uh like most of our requirements are rooted in very low latency needs. Uh and then we also have pretty high scale uh roughly like o over 20 million QPS uh like queries per second which um may or may not include a single bid request but I don't want to dive too deep on that. Um as far as Kubernetes uh the team started in 2020 uh at the time like many C or many other uh companies we were just using it for green field applications and just trying to figure out how this thing could work.

uh since then we are now running in uh multiple other cloud providers and we have a global footprint with uh like uh I think around 40 or 50 clusters now uh and then just last year we finally finished our expansion into our middle data centers uh
