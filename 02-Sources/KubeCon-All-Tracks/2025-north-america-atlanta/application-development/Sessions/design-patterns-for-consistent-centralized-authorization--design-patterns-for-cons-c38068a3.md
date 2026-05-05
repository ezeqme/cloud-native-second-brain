---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Application Development"]
speakers: ["José Padilla", "Auth0", "Alice Gibbons", "Diagrid"]
sched_url: https://kccncna2025.sched.com/event/27Fek/design-patterns-for-consistent-centralized-authorization-jose-padilla-auth0-alice-gibbons-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Design+Patterns+for+Consistent+Centralized+Authorization+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Design Patterns for Consistent Centralized Authorization - José Padilla, Auth0 & Alice Gibbons, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United States / Atlanta
- Speakers: José Padilla, Auth0, Alice Gibbons, Diagrid
- Schedule: https://kccncna2025.sched.com/event/27Fek/design-patterns-for-consistent-centralized-authorization-jose-padilla-auth0-alice-gibbons-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Design+Patterns+for+Consistent+Centralized+Authorization+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Design Patterns for Consistent Centralized Authorization.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fek/design-patterns-for-consistent-centralized-authorization-jose-padilla-auth0-alice-gibbons-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Design+Patterns+for+Consistent+Centralized+Authorization+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=v-Qt6op7BLU
- YouTube title: Design Patterns for Consistent Centralized Authorization - José Padilla & Alice Gibbons
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/design-patterns-for-consistent-centralized-authorization/v-Qt6op7BLU.txt
- Transcript chars: 36034
- Keywords: workflow, dapper, database, within, application, running, actually, postgress, authorization, organization, wanted, activity, durable, essentially, workflows, engine, locally, question

### Resumo baseado na transcript

Hey everyone, welcome to our session on design patterns for centralized author authorization. We're going to talk a little bit about resiliency in computing as well as uh Dapper workflow which is one of the most popular APIs that uh we are seeing users use today. Making a user wait for two, three, four and number of uh different requests whe whether it's to a database or another service just creates high latency and now we're forcing us into asynchronous eventual consistency patterns and number three or seven from this list transport cost is zero. Now, the dual right problem exists because these common assumptions are false. Now, can I get a um raise of hands who has heard about this like dual right problems thing? >> The dual way problem occurs when two external systems must be updated in an atomic fashion.

### Excerpt da transcript

Hey everyone, welcome to our session on design patterns for centralized author authorization. Um, and can this I my name is Alice Gibbons. I am head of customer engineering at Diagrid. We are the folks behind the open source Dapper project. If you don't know about Dapper, that's okay. I will hopefully tell you about it today. And yeah, really excited to be here. We're going to talk a little bit about resiliency in computing as well as uh Dapper workflow which is one of the most popular APIs that uh we are seeing users use today. Jose >> I'm Jose Padija. I'm a core maintener for openf and I'm a staff software engineer at Ozero where we work with our our fine grain authorization product. >> Awesome. So imagine a user making an order online, but they also need to update their address. The system needs to update both the user database and the shipment service. If either fails, the shipment will not go where the user is expecting it to go. Distributed systems aim to remove bottlenecks or or central points of failure from a system.

While they provide significant benefits, they also present challenges. L. Peter Deutsch describes some false assumptions that people new to distributed systems invariably make. I'm going to zoom in to three of them. First one, the network is reliable. In real in reality, we know that network calls to your second service, be it an API, an off service, another database, can and will likely fail. This is the root of the inconsistency problem. Two, latency is zero. Reality is that network calls do take time. Making a user wait for two, three, four and number of uh different requests whe whether it's to a database or another service just creates high latency and now we're forcing us into asynchronous eventual consistency patterns and number three or seven from this list transport cost is zero. In reality, every network call cost CPU time, data transfer. These costs add up, forcing us to find other efficient patterns. Now, the dual right problem exists because these common assumptions are false. Now, can I get a um raise of hands who has heard about this like dual right problems thing?

Cool. >> And this is the application developer track. Just, you know, confirming. So, we have at least a few developers in here. One or two. Okay. I'm using sub nods. All right, we have one one developer in the back. >> The dual way problem occurs when two external systems must be updated in an atomic fashion. A classic example is updating an application's
