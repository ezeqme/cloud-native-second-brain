---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccnceu2024.sched.com/event/1Yhfo/emissary-ingress-present-and-future-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Emissary-Ingress%3A+Present+and+Future+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Emissary-Ingress: Present and Future - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Flynn, Buoyant
- Schedule: https://kccnceu2024.sched.com/event/1Yhfo/emissary-ingress-present-and-future-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary-Ingress%3A+Present+and+Future+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Emissary-Ingress: Present and Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhfo/emissary-ingress-present-and-future-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Emissary-Ingress%3A+Present+and+Future+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lJFU-N0OR-4
- YouTube title: Emissary-Ingress: Present and Future - Flynn, Buoyant
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/emissary-ingress-present-and-future/lJFU-N0OR-4.txt
- Transcript chars: 21395
- Keywords: emissary, gateway, envoy, ambassador, actually, developer, little, application, language, branch, python, interesting, developers, around, rather, cluster, important, question

### Resumo baseado na transcript

I will be talking to you about Emissary which is not a buoyant thing uh I would like to apologize in advance both for any strange wines that you might see on my face and also for the fact that this is probably the most boring slide deck I've ever put together in terms of Transitions and animations and Graphics I broke my collar bone a week and a half ago and so I'm a little a little behind on some of this we are here to talk about Emissary

### Excerpt da transcript

so welcome I am Flynn uh you can reach me at Flyn buy. I will be talking to you about Emissary which is not a buoyant thing uh I would like to apologize in advance both for any strange wines that you might see on my face and also for the fact that this is probably the most boring slide deck I've ever put together in terms of Transitions and animations and Graphics I broke my collar bone a week and a half ago and so I'm a little a little behind on some of this we are here to talk about Emissary the past the present and the future we will of course start with the past um quick show of hands how many of you are new to Emissary okay so this is going to be a little bit interesting uh let me go through this deck and then if you like we I'll pull up another one where we can go into a little more detail about how Emissary works and things like that but on this one The quick summary is that Emissary is an API Gateway it is an open source Gateway it's cncf incubating project it is a developer Centric thing meaning its entire Focus for its life has been on enabling application developers to get things done it is self-service in that it tries to arrange it so that the application Developers don't have to go off and talk to PE other people with Ops and Open tickets and all sorts of things like that and it is a very opinionated API gayway there are a number of things that we don't do that we could have done the developer Centric and self-service parts of this are very important um Emissary was actually designed from the start around these ideas that the application developer is the important person here and the other critical idea there is that application developers generally don't care very much about kubernetes they just want things to work so that's the way that Emissary has always been designed um it also is interesting that that idea is also important for being able to develop at scale when you have lots and lots of developers doing lots and lots of things all at the same time um that idea also ended up being influence on Gateway API later which is one of the things that's I found really fascinating about this um the bit that I said earlier about opinionation is also very important there are a number of things that we could have done in Emissary that we decided not to do because they don't fit this model of we just want the developer to be able to get stuff done without having to be a kubernetes expert um I feel compelled to point out that the opinions that we wer
