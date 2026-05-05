---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Renana Yacobi", "Piaw Na", "Niantic"]
sched_url: https://kccncna2021.sched.com/event/lV5L/context-aware-traffic-routing-for-stateful-services-using-envoy-renana-yacobi-piaw-na-niantic
youtube_search_url: https://www.youtube.com/results?search_query=Context+Aware+Traffic+Routing+for+Stateful+Services+using+Envoy+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Context Aware Traffic Routing for Stateful Services using Envoy - Renana Yacobi & Piaw Na, Niantic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Los Angeles
- Speakers: Renana Yacobi, Piaw Na, Niantic
- Schedule: https://kccncna2021.sched.com/event/lV5L/context-aware-traffic-routing-for-stateful-services-using-envoy-renana-yacobi-piaw-na-niantic
- Busca YouTube: https://www.youtube.com/results?search_query=Context+Aware+Traffic+Routing+for+Stateful+Services+using+Envoy+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Context Aware Traffic Routing for Stateful Services using Envoy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5L/context-aware-traffic-routing-for-stateful-services-using-envoy-renana-yacobi-piaw-na-niantic
- YouTube search: https://www.youtube.com/results?search_query=Context+Aware+Traffic+Routing+for+Stateful+Services+using+Envoy+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0W7aYTjtVwM
- YouTube title: Context Aware Traffic Routing for Stateful Services using Envoy - Renana Yacobi & Piaw Na, Niantic
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/context-aware-traffic-routing-for-stateful-services-using-envoy/0W7aYTjtVwM.txt
- Transcript chars: 13632
- Keywords: client, server, routing, messages, protocol, already, envelope, message, request, buffer, actually, mapping, assigned, player, change, storage, context, interesting

### Resumo baseado na transcript

uh thank you for coming to the talk at the nearly the conference uh as randy said the title is context aware traffic routing uh here's the agenda for the talk uh we're gonna talk a little bit about ourselves explain to you what the motivation you might have for doing context-aware routing discuss the issues involved talk about the implementation look at results uh and then talk more about our prototype and we'll definitely have time at the end for questions uh my name is pial i'm a senior

### Excerpt da transcript

uh thank you for coming to the talk at the nearly the conference uh as randy said the title is context aware traffic routing uh here's the agenda for the talk uh we're gonna talk a little bit about ourselves explain to you what the motivation you might have for doing context-aware routing discuss the issues involved talk about the implementation look at results uh and then talk more about our prototype and we'll definitely have time at the end for questions uh my name is pial i'm a senior staff software engineer at niantic na i'm a soft staff software engineer at nandi uh let's jump right in uh you probably know about the usual context aware routing that nearly every website uses the url directs you your particular request to a backend that then serves your request nearly every website does this you can also get data from the request header about how to do routing is usually done by a load balancer you can also have side channels that are used to direct traffic this might be an application that tries to give smart load balancing by checking which servers can take the load and what this talk is about is using the actual content of the request message in order to do the routing why might you want to do this in our particular case what we wanted to do was to be able to retrofit smart routing based on the data that was already being passed into the packet and that that routing wasn't previously done and we figured we could do this without changing the application you can also do back-end mapping based on either personal information that's already in the packet so user x always goes to this server or based on whatever intellectual property you might have in one of our applications we actually peek back multiple protocol buffers into a single request and when the monolithic application is broken up into microservices one thing that's useful to do is you can hey now take each of these individual protocol sub messages in that protocol buffer and route them to different services simultaneously uh just what a the custom envoy filter looks like the client sends a protocol buffer or message and envoy captures it decodes the data deserializes the entire protocol buffer applies the routing algorithm and sends it to the correct backend we did two runs using this naive approach one with an average message size around half a megabyte and the other one with average sizes in the two megabyte ranges uh the entire test turned out to be bandwidth limited and what would happen w
