---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security"]
speakers: ["Ahmet Soormally", "Letz Yaara", "Tyk"]
sched_url: https://kccnceu2024.sched.com/event/1YeLf/oauth2-token-exchange-for-microservice-api-security-ahmet-soormally-letz-yaara-tyk
youtube_search_url: https://www.youtube.com/results?search_query=OAuth2+Token+Exchange+for+Microservice+API+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OAuth2 Token Exchange for Microservice API Security - Ahmet Soormally & Letz Yaara, Tyk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Ahmet Soormally, Letz Yaara, Tyk
- Schedule: https://kccnceu2024.sched.com/event/1YeLf/oauth2-token-exchange-for-microservice-api-security-ahmet-soormally-letz-yaara-tyk
- Busca YouTube: https://www.youtube.com/results?search_query=OAuth2+Token+Exchange+for+Microservice+API+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OAuth2 Token Exchange for Microservice API Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeLf/oauth2-token-exchange-for-microservice-api-security-ahmet-soormally-letz-yaara-tyk
- YouTube search: https://www.youtube.com/results?search_query=OAuth2+Token+Exchange+for+Microservice+API+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=09GhdXhiv0Q
- YouTube title: OAuth2 Token Exchange for Microservice API Security - Ahmet Soormally & Letz Yaara, Tyk
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/oauth2-token-exchange-for-microservice-api-security/09GhdXhiv0Q.txt
- Transcript chars: 33576
- Keywords: access, exchange, gateway, identity, google, client, request, authorization, tokens, keycloak, server, security, authorized, little, internal, systems, external, provider

### Resumo baseado na transcript

okay today we'll take a deep dive into the complexity surrounding identity propagation and API Security in microservices environment we'll explore our current workarounds and their issues then we'll see how a novel relatively unknown and under implemented extension of o2 might help us to solve our problems at the end we'll also demo this solution so my name is Alit and I'm Yara and we're both from T an open source API Gateway and management platform I've been here for coming on seven years now uh starting as a

### Excerpt da transcript

okay today we'll take a deep dive into the complexity surrounding identity propagation and API Security in microservices environment we'll explore our current workarounds and their issues then we'll see how a novel relatively unknown and under implemented extension of o2 might help us to solve our problems at the end we'll also demo this solution so my name is Alit and I'm Yara and we're both from T an open source API Gateway and management platform I've been here for coming on seven years now uh starting as a Consulting engineer for our prospects and customers and then um moved into product leadership and now my focus is on R&D where my team and I are looking a little further ahead strategically uh to help shape the future of our product offering I was a SAS developer most of my career but I needed a change and decided to cross the lines and work with users directly I joined T three weeks before IIT and also also as a Consulting engineer later on I moved into product leadership as well as a head of developer experience we're focusing on creating sdks CIS and other Dev tools to enhance our users experience okay let's get started when I visit an online service an online store and wish to place an order as far as I'm concerned I'm just placing an order via some web app I'm completely oblivious to the different chains of event and communication between services or different providers that are involved in order to fulfill my transaction if we zoom in a little bit this slide shows what the world looks like from perspective of a service which is responsible for processing an order a service such as an order microservice can use and consume many other services some internal ones like inventory pricing and user account and other third apis such as for Checker shipping CRM and payments some Services um sorry but there are other services that might benefit sorry I'm a bit nervous some services such as shipping services are happy to just accept an a simple API key in order to integrate with the that service they don't need to know anything about the user apart from perhaps the deliver postcode but other services might benefit from knowing who the user is perhaps would include a this would include a CRM or a for Checker some services such as shipping need need the user's address book to add to book a delivery or make a payment While others third parties like a fraud Checker that are on less trusted domain would need to be downgraded to read only access rights we can s
