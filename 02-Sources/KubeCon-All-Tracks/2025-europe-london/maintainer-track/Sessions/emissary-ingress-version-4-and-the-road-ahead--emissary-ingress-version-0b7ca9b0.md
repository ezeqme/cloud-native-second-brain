---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccnceu2025.sched.com/event/1tczv/emissary-ingress-version-4-and-the-road-ahead-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+the+Road+Ahead+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Emissary-ingress: Version 4 and the Road Ahead - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Flynn, Buoyant
- Schedule: https://kccnceu2025.sched.com/event/1tczv/emissary-ingress-version-4-and-the-road-ahead-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+the+Road+Ahead+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Emissary-ingress: Version 4 and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczv/emissary-ingress-version-4-and-the-road-ahead-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Emissary-ingress%3A+Version+4+and+the+Road+Ahead+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aQLKdGqdrgw
- YouTube title: Emissary-Ingress: Version 4 and the Road Ahead - Flynn, Buoyant
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/emissary-ingress-version-4-and-the-road-ahead/aQLKdGqdrgw.txt
- Transcript chars: 21198
- Keywords: emissary, ambassador, gateway, actually, conversion, couple, cluster, envoy, anybody, little, maintainer, ingress, talking, developer, pretty, anything, company, working

### Resumo baseado na transcript

we may as well go ahead and get started then there are not a lot of people here can I assume that everybody here already knows what this project is or are there total newcomers there's one to there are a couple of total newcomers okay then I'm going to go over the bit with what the project is and then we will talk about a couple other things but yeah with this few people here I'm going to blame that completely on where we are in the convention center

### Excerpt da transcript

we may as well go ahead and get started then there are not a lot of people here can I assume that everybody here already knows what this project is or are there total newcomers there's one to there are a couple of total newcomers okay then I'm going to go over the bit with what the project is and then we will talk about a couple other things but yeah with this few people here I'm going to blame that completely on where we are in the convention center um it's a good opportunity to actually do this a little bit more interactively and hear about the things that y'all are concerned about and then hopefully we'll be able to talk about some of that in more detail if you don't already know who I am I'm Flynn I'm a tech evangelist at buyant these days I'm also the original author of emary and still the longest serving maintainer uh we can talk a bit about the purpose of the project for those who are new the past the present the future and the purpose the very first thing you run into in Cloud native is if you have a cluster you will then have people outside the cluster who want to use things inside the cluster this is not allowed by default this is one of the things that clusters try to prevent for security reasons so we need something to deal with that this is collectively called the Ingress problem as distinct from the Ingress resource or Ingress controllers because Ingress is totally not an overl reled term in kubernetes we need something that sits there on the edge of the cluster that can mediate access for these people coming in trying to use workloads inside the cluster and that is the problem that Emissary was created to solve it is an Ingress controller although you can configure it with the Ingress resource we do not recommend that technically speaking this function that we're talking about here is basically routing Ms can do a lot more than that for example it could decide that these users are actually not allowed to talk to workload B that's a basic authorization and authentication function Emissary doesn't really separate those two the way it does it you can use it for either or both we can do things like traffic splitting where we can send traffic between two different versions of a workload and thereby do AB testing or canaries uh we can do tries where if a given request fails we'll just keep doing it until it succeeds we can do rate limiting and circuit breaking and a bunch of other stuff that doesn't fit easily on slides so I didn't try to put them
