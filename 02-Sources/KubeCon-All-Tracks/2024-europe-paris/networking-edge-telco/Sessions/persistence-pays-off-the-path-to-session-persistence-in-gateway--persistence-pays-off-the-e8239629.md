---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking"]
speakers: ["Jung-Yu (Gina) Yeh", "Google", "Grant Spence", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YeNt/persistence-pays-off-the-path-to-session-persistence-in-gateway-api-jung-yu-gina-yeh-google-grant-spence-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Persistence+Pays+Off%3A+The+Path+to+Session+Persistence+in+Gateway+API+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Persistence Pays Off: The Path to Session Persistence in Gateway API - Jung-Yu (Gina) Yeh, Google & Grant Spence, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Jung-Yu (Gina) Yeh, Google, Grant Spence, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YeNt/persistence-pays-off-the-path-to-session-persistence-in-gateway-api-jung-yu-gina-yeh-google-grant-spence-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Persistence+Pays+Off%3A+The+Path+to+Session+Persistence+in+Gateway+API+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Persistence Pays Off: The Path to Session Persistence in Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNt/persistence-pays-off-the-path-to-session-persistence-in-gateway-api-jung-yu-gina-yeh-google-grant-spence-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Persistence+Pays+Off%3A+The+Path+to+Session+Persistence+in+Gateway+API+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5uoHQNkJC10
- YouTube title: Persistence Pays Off: The Path to Session Persistence in Gateway API
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/persistence-pays-off-the-path-to-session-persistence-in-gateway-api/5uoHQNkJC10.txt
- Transcript chars: 28288
- Keywords: session, persistence, policy, gateway, cookie, traffic, backend, configuration, request, persistance, specific, currently, object, affinity, header, client, persistent, question

### Resumo baseado na transcript

hello everyone welcome I'm so excited to see you all here at our presentation session uh persistant pays off the path to station persistence in gway API um I know it's been a long day and I'm probably standing between you and your Diner um so huge thank you for sticking with us at this presentation um for those of you who might be new to this concept um session persistence is a way to ensure that a users request are cons consistently routed to the SAG end throughout their

### Excerpt da transcript

hello everyone welcome I'm so excited to see you all here at our presentation session uh persistant pays off the path to station persistence in gway API um I know it's been a long day and I'm probably standing between you and your Diner um so huge thank you for sticking with us at this presentation um for those of you who might be new to this concept um session persistence is a way to ensure that a users request are cons consistently routed to the SAG end throughout their interactions with a website or application and this can be crucial for applications um who that needs to track the user preferences the states or even like shopping carts and um it was the top requested features for gway API at last year's ccom as Chicago so demonstrating that how important it is to this community we are incredible really excited to um share the latest updates um on the session persistence and um how this is going to be integrated into the gateway API my name is j um I'm software engineer at Google I'm leading the design and implementation effort of session persistance in JPC route and httv Route and today I'm presenting with Grant hey uh I'm Grant Spence I'm software engineer at redhead and I've been kind of leading and championing the uh soft uh the session proc system skip uh with G API so let's take a few minutes to talk about kubernetes G API before dive into session persistence the go API is a significant Evolution um in how we manage Network traffic in Comm environments it offers a powerful set of features to address the demands of the modern microservices architectures and the gway API designed several distinct roles for servicing different needs needs for different users it also provides a standardized way to ensure that your configurations will work similarly across different kubernetes environments and um Network infrasture providers the API give a fine two traffic with capabilities like haer based routing um weighted traffic split and advanced low balancing and the Gateway API primarily known for its North South traffic capabilities is involving to support East wayte use cases with the service measures so that is it can be used to Route the communication between services and the route will attach directly to the service representing the configuration mean to be all applied to any traffic directly to the surface the gway API also similarly integrated with the custom Solutions enabling the use uh enabling the use of the specialized LW balancers or service meses
