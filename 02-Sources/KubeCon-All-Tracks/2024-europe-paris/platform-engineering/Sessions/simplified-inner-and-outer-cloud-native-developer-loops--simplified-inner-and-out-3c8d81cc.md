---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Oleg Šelajev", "AtomicJar", "Alice Gibbons", "Diagrid"]
sched_url: https://kccnceu2024.sched.com/event/1YeMJ/simplified-inner-and-outer-cloud-native-developer-loops-oleg-selajev-atomicjar-alice-gibbons-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Simplified+Inner+and+Outer+Cloud+Native+Developer+Loops+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Simplified Inner and Outer Cloud Native Developer Loops - Oleg Šelajev, AtomicJar & Alice Gibbons, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Oleg Šelajev, AtomicJar, Alice Gibbons, Diagrid
- Schedule: https://kccnceu2024.sched.com/event/1YeMJ/simplified-inner-and-outer-cloud-native-developer-loops-oleg-selajev-atomicjar-alice-gibbons-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Simplified+Inner+and+Outer+Cloud+Native+Developer+Loops+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Simplified Inner and Outer Cloud Native Developer Loops.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMJ/simplified-inner-and-outer-cloud-native-developer-loops-oleg-selajev-atomicjar-alice-gibbons-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Simplified+Inner+and+Outer+Cloud+Native+Developer+Loops+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xAprZWSi2y4
- YouTube title: Simplified Inner and Outer Cloud Native Developer Loops - Oleg Šelajev, AtomicJar & Alice Gibbons
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/simplified-inner-and-outer-cloud-native-developer-loops/xAprZWSi2y4.txt
- Transcript chars: 36144
- Keywords: application, dapper, containers, production, developer, running, container, development, environment, feature, configuration, actually, kitchen, essentially, number, client, locally, docker

### Resumo baseado na transcript

we are happy to see you here and we're going to talk about simplified inner and outer Cloud native developer Loops we're going to talk about developer experience we're going to talk about some tools and we're going to show you the live demos of how we think the the inner loop and outer loop can could work for for some environments um I hope we you're going to enjoy that why are we talking about this in general is because we want to talk about productivity developer time is

### Excerpt da transcript

we are happy to see you here and we're going to talk about simplified inner and outer Cloud native developer Loops we're going to talk about developer experience we're going to talk about some tools and we're going to show you the live demos of how we think the the inner loop and outer loop can could work for for some environments um I hope we you're going to enjoy that why are we talking about this in general is because we want to talk about productivity developer time is a very very expensive resource and well the more productive you are the the better it is for the business the so you you save money right which is good we all would like to save money yes we all would like to get more money and improve the margins and everything so how do we waste time one of the most kind of sort of in an abstract sense biggest bottlenecks is when we do things again and again but they're slightly different and we are we need to solve the problem again and again and again um but but like we we cannot reuse the existing Solutions right and we need to change small things and we get the tooling that doesn't fit us that we maybe are not fully embracing for working with it and uh that is that is not great I think that's called Reinventing the wheel right yes we Reinventing the wheel is one of the biggest uh time SC so today we would like to look at the workflows for your typical devops uh pipeline uh for your software development cycle in a loop from code going to production uh and see how some tools interact and how you can enable maybe better application developer experiences without sacrificing the needs and your interest in production let's do it my name is Alex I work at as a developer uh relations person and I work on the test containers project and this is what we're going to use later for the demos as well you can find me by at life almost universally online and if you are into that sort of thing uh check out my YouTube channel I do short videos with people is there any more fun facts on those videos maybe I'll check them out hi everyone thanks so much for coming my name is Alice Gibbons I am head of customer success at diagrid if you haven't heard of us we are we enable uh tools and apis for developers building distributed systems and uh yeah we are big supporters of the Dapper project which I'm going to talk about today and how it enables productivity so you know as o mentioned how do we enable developer productivity right developer time equals money you all saw the
