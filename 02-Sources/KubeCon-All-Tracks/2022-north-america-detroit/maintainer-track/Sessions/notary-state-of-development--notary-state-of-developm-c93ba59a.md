---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Justin Cormack", "Docker"]
sched_url: https://kccncna2022.sched.com/event/182OP/notary-state-of-development-justin-cormack-docker
youtube_search_url: https://www.youtube.com/results?search_query=Notary%3A+State+Of+Development+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Notary: State Of Development - Justin Cormack, Docker

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Justin Cormack, Docker
- Schedule: https://kccncna2022.sched.com/event/182OP/notary-state-of-development-justin-cormack-docker
- Busca YouTube: https://www.youtube.com/results?search_query=Notary%3A+State+Of+Development+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Notary: State Of Development.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182OP/notary-state-of-development-justin-cormack-docker
- YouTube search: https://www.youtube.com/results?search_query=Notary%3A+State+Of+Development+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SMJRA8jiuSM
- YouTube title: Notary: State Of Development - Justin Cormack, Docker
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/notary-state-of-development/SMJRA8jiuSM.txt
- Transcript chars: 31424
- Keywords: actually, verify, signing, working, docker, registry, notation, ratify, support, identity, signed, around, standard, artifacts, certificate, public, notary, standards

### Resumo baseado na transcript

I'm Justin comac I'm the CTO Docker I'm a cncf technical oversight committee and maintainer of Nature and um I'm David tesser he wasn't on the bill but we uh we always like to do our presentations jointly and usually I've done them with Steve Alaska but it's good to have someone else for a change yeah yeah it's great to be here I'm a principal product manager at Microsoft and I work a lot with notary oraz ratify managing those projects so right um so really just getting started

### Excerpt da transcript

I'm Justin comac I'm the CTO Docker I'm a cncf technical oversight committee and maintainer of Nature and um I'm David tesser he wasn't on the bill but we uh we always like to do our presentations jointly and usually I've done them with Steve Alaska but it's good to have someone else for a change yeah yeah it's great to be here I'm a principal product manager at Microsoft and I work a lot with notary oraz ratify managing those projects so right um so really just getting started really with um you know what how did notary get to where it is today um you know we we naturally has always been a product a project that's been based around kind of firm foundations and standards um Nursery originally joined uh cncf back in 2017 alongside um the tough standard which it was based on says Justin's over there um who led that um and um originally it was a project it said Docker kind of which is where my original connection to it comes from but it um you know it's been a CNC project for a very long time now late in 2019 um there was a bunch of issues um we weren't seeing a lot of adoption um like um of notary back then there were kind of architectural issues in particular it was a sidecar that's out on the side of a registry that meant first of all many Registries didn't have support for notary at all because someone had to be run on the side it wasn't a native part of the registry protocol and it was kind of um there were other related problems with that there's a talk I did back in um in uh where are they did San Diego yeah where I talked about a lot of the issues that we had and the kind of problems and we and that really kind of started off as a whole set of streams of work to try and resolve some of these issues and you know find New Foundations and standards to build on um one of the things I think is kind of useful to talk about is um identity when we're talking about signing um what kind of identity what's the identity of the thing that we're actually kind of interested in um with these are kind of these are my terms for these things I don't think there's actually a very standard terminology for a lot of these things um we built um naturally originally aren't tough and tough has a kind of basically a root key which roughly corresponds to a repository or project I mean that you can have larger you know kind of larger scope route Keys than that but um kind of um which is a really great model but we did find it hard for people to adopt because they're not actually
