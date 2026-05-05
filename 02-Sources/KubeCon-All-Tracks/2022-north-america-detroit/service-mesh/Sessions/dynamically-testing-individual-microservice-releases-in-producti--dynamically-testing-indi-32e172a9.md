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
speakers: ["Matt Turner", "Tetrate"]
sched_url: https://kccncna2022.sched.com/event/182Ep/dynamically-testing-individual-microservice-releases-in-production-matt-turner-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=Dynamically+Testing+Individual+Microservice+Releases+In+Production+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Dynamically Testing Individual Microservice Releases In Production - Matt Turner, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Matt Turner, Tetrate
- Schedule: https://kccncna2022.sched.com/event/182Ep/dynamically-testing-individual-microservice-releases-in-production-matt-turner-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=Dynamically+Testing+Individual+Microservice+Releases+In+Production+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Dynamically Testing Individual Microservice Releases In Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ep/dynamically-testing-individual-microservice-releases-in-production-matt-turner-tetrate
- YouTube search: https://www.youtube.com/results?search_query=Dynamically+Testing+Individual+Microservice+Releases+In+Production+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2xvs5QFbheU
- YouTube title: Dynamically Testing Individual Microservice Releases In Production - Matt Turner, Tetrate
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/dynamically-testing-individual-microservice-releases-in-production/2xvs5QFbheU.txt
- Transcript chars: 35328
- Keywords: version, actually, istio, little, testing, override, traffic, environment, header, database, request, deploy, virtual, probably, release, envoy, config, trying

### Resumo baseado na transcript

so welcome uh I'm Matt Turner I'm going to talk about dynamically testing individual microservice releases in production which is a bit of a mouthful but I wanted to get across what we're so actually going to be talking about which is to test on an ongoing basis you know new releases of an individual Service as part of a more complicated bigger set of micro services so let's let's dive into what that means so yeah lots to talk about a lot of these uh a lot of these

### Excerpt da transcript

so welcome uh I'm Matt Turner I'm going to talk about dynamically testing individual microservice releases in production which is a bit of a mouthful but I wanted to get across what we're so actually going to be talking about which is to test on an ongoing basis you know new releases of an individual Service as part of a more complicated bigger set of micro services so let's let's dive into what that means so yeah lots to talk about a lot of these uh a lot of these topics I'm only going to be touching on kind of briefly it's a bit of background the meat of this really is in sort of the istio config what we what we can do with this and the automation that I've started to build for it but I will just touch on a bit of background as well um I can't see my own slice in here so I'll have to lean in occasionally remember what I promised I was going to say um I won't have to leave that list out so a little bit about me um I am a software engineer at tetrate tetrate was founded to solve the problem of using service meshes to scale our management plane provides a layer on top of one or more hdmes's it'll install them for you upgrade them for you and it uses the tetrated studio distribution for that which is a build of Upstream is Joe we haven't forked it but it is fully fixed compliant and you can then use our UI or you can give simple high level config and we'll render that down to all the complicated istio config you need for secure cross-cluster communication and if you plug into your identity provider we'll also let you set up inheritable hierarchical permissions across all of that so that people can do mesh Ops in in controlled ways a little bit about you maybe uh who who's never used istio or another service mesh okay that's probably half of you cool who is sort of a beginner can make it do something that's probably the other half and anybody consider themselves sort of an expert like if I give you a problem you write the config to fix it okay a few people that's cool I guess I've sort of I've sort of got this about right then so I'm actually going to talk about this from the perspective of of the problem we're trying to solve and I would then introduce you know a service mesh uh SEO in My Demo as being the like the way to solve that but this is not like an istio talk this isn't a deep dive so hopefully this will take people uh through it who haven't seen it before so briefly microservices right what are they what do they look like in production it might look
