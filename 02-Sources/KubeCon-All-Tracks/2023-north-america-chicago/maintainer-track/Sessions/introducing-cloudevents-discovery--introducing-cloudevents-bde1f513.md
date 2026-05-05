---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["David Baldwin", "Independent"]
sched_url: https://kccncna2023.sched.com/event/1R2rq/introducing-cloudevents-discovery-david-baldwin-independent
youtube_search_url: https://www.youtube.com/results?search_query=Introducing+CloudEvents+Discovery+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Introducing CloudEvents Discovery - David Baldwin, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: David Baldwin, Independent
- Schedule: https://kccncna2023.sched.com/event/1R2rq/introducing-cloudevents-discovery-david-baldwin-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Introducing+CloudEvents+Discovery+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Introducing CloudEvents Discovery.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rq/introducing-cloudevents-discovery-david-baldwin-independent
- YouTube search: https://www.youtube.com/results?search_query=Introducing+CloudEvents+Discovery+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9U4R9ELymbE
- YouTube title: Introducing CloudEvents Discovery - David Baldwin, Independent
- Match score: 0.797
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/introducing-cloudevents-discovery/9U4R9ELymbE.txt
- Transcript chars: 34599
- Keywords: events, actually, registry, little, perspective, specification, within, consume, associated, another, mentioned, discovery, additional, provide, definition, started, attributes, forward

### Resumo baseado na transcript

hello everybody how guys how are you doing today at the Wednesday of cucon uh towards the evening um so my name is uh David Baldwin I'm going to do a uh maintainer update on the cloud events Discovery and a little bit about X registry and so this will be about 25 minutes or so and if we have any questions I'm happy to take them at the end and we can go into more detail including uh um maybe a demo if time permits or depending what the new to this but uh it seems like you guys are um mostly defining like the end points and the schemas messages these kinds of things and I'm looking at some of the event driven architecture stuff that we've worked with and it seems like it's a natural fit except that maybe it doesn't support some of the uh Cooperative features like replay things like that have you guys considered the suitability of this for um event driven architectures or have you looked at like the iyn async API that

### Excerpt da transcript

hello everybody how guys how are you doing today at the Wednesday of cucon uh towards the evening um so my name is uh David Baldwin I'm going to do a uh maintainer update on the cloud events Discovery and a little bit about X registry and so this will be about 25 minutes or so and if we have any questions I'm happy to take them at the end and we can go into more detail including uh um maybe a demo if time permits or depending what the questions are so just a quick back of myself um just from an introduction perspective um I've been in product management for well over uh well over 12 years working at different uh SAS based companies VMware swun um and a lot of work I've done there has actually been been related to doing Integrations hundreds of Integrations which is kind of how I fell upon Cloud events and in the servus working group trying to find easier ways for me to be able to go through and do Integrations and be able to consume data um I've also a nine-time cuon cucon attendee they started in 2015 if anybody was there in San Francisco so heavily involved in terms of the growth of uh the cloud native community in terms of where it's been going so from an agenda perspective we're going to break it down into a couple different segments a little bit of a background in terms of the current state where Cloud events came from where they're going um also doing an introduction to Discovery uh this will Branch out into the topic of where the events and attributes which is kind of where the X registry Park will come into place then I'm going to talk a little bit just a quick update on the developer resources I'm going to point those out because a huge amount of work has been done especially over the last year regarding updating the tooling that's necessary for developers to be able to integrate Cloud events then we're going to tap into a little bit about going forward in terms of what we're asking for in terms of the help from the community perspective now from a timeline perspective uh we can go back to 2017 this is the cist working group um started uh started a new specification in terms of trying to build out a way to easy make it easier to be able to consume consume events and so from there they started to create what was called the the the cloud event specification uh and this continued to grow over time in 20 2018 uh uh the sandbox the project was converted into a Sandbox 2019 it moved into incubation and at the same time as incubation is when we actually
