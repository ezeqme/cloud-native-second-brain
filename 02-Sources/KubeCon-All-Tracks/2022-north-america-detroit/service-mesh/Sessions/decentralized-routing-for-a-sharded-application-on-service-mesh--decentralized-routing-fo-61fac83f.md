---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Vinay Gonuguntla", "Pankaj Sikka", "Intuit"]
sched_url: https://kccncna2022.sched.com/event/182KO/decentralized-routing-for-a-sharded-application-on-service-mesh-vinay-gonuguntla-pankaj-sikka-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Decentralized+Routing+For+a+Sharded+Application+On+Service+Mesh+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Decentralized Routing For a Sharded Application On Service Mesh - Vinay Gonuguntla & Pankaj Sikka, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Vinay Gonuguntla, Pankaj Sikka, Intuit
- Schedule: https://kccncna2022.sched.com/event/182KO/decentralized-routing-for-a-sharded-application-on-service-mesh-vinay-gonuguntla-pankaj-sikka-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Decentralized+Routing+For+a+Sharded+Application+On+Service+Mesh+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Decentralized Routing For a Sharded Application On Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182KO/decentralized-routing-for-a-sharded-application-on-service-mesh-vinay-gonuguntla-pankaj-sikka-intuit
- YouTube search: https://www.youtube.com/results?search_query=Decentralized+Routing+For+a+Sharded+Application+On+Service+Mesh+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cmTRWEcSEZM
- YouTube title: Decentralized Routing For a Sharded Application On Service Mesh - Vinay Gonuguntla & Pankaj Sikka
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/decentralized-routing-for-a-sharded-application-on-service-mesh/cmTRWEcSEZM.txt
- Transcript chars: 28114
- Keywords: filter, application, request, client, routing, lookup, mesh, virtual, admiral, istio, company, solution, clusters, little, cluster, policy, sharded, approach

### Resumo baseado na transcript

hey uh Welcome to our talk today uh we'll be talking about decentralized routing for a sharded application on service mesh I'm vinay gonogundlaf and this is pankajika so we are software engineers at Intuit and we work on the service mesh platform at into it so let me go over uh the agenda for today um we'll be talking about a little bit about what service mesh is and how it is set up at Intuit a little bit about the starter application and how routing is done on this is very a basic example of a virtual service and but then the virtual service did not work for us due to some limitations uh due to our use cases uh so there were maintainability problems what I mean by that is uh if exist so this is a lot of overhead and then also the size of the virtual service object itself can grow a lot which is again a management problem uh as I mentioned earlier uh we need near real-time updates imagine a new company getting across all the client clusters and then if the data can move among the shards as well virtual Service as you are aware it's a static mapping so we cannot make that decision in the virtual service so due to these limitations we started designing

### Excerpt da transcript

hey uh Welcome to our talk today uh we'll be talking about decentralized routing for a sharded application on service mesh I'm vinay gonogundlaf and this is pankajika so we are software engineers at Intuit and we work on the service mesh platform at into it so let me go over uh the agenda for today um we'll be talking about a little bit about what service mesh is and how it is set up at Intuit a little bit about the starter application and how routing is done on a starter application our design and some challenges we faced we'll go over the demo as well as uh some future investment we have on the solution so a little bit about Intuit uh into it is a leading fintech company um I would consider ourselves more of a bleeding edge a platform company uh we are really honored to have received the end user award for 2019 as well as 2022. if you look at the cncf portfolio into pretty much uses most of the products there we also are a big open source contributor uh we contribute to more than 75 plus projects and some of the projects we maintain and our open source are Argo Kiko Admiral and new approach so uh let me go into a little bit of the scale at which Intuit operates um Intuit has more than 245 plus kubernetes clusters running in production we spend about 16 000 name spaces in those clusters at Peak we recorded more than 77 000 nodes are running in production uh with more than 7 million pods and we have 2000 plus unique Services which are running among these clusters and these services are a mix of both um end user Services as well as internal services so next I want to just walk through service mesh how many of you here know what service mesh is I think most of you do so I can go a little fast on this section is an infrastructure layer to facilitate service to service communication I think the most popular approach right now is to use the sidecar to intercept traffic for Ingress and egress communication through the application this allows us to do few cool things with uh by adding a sidecars or using service mesh some of them are security by providing Mutual TLS observability by taking a snapshot of the entire system and finding the bottlenecks routing by providing things like Canary or traffic splitting and also reliability by automating retries some of the most popular service mesh offerings out there are istio linkery and console we had to use istio as our service mesh platform so there's a little bit about istio since most of you are familiar I'll just I'
