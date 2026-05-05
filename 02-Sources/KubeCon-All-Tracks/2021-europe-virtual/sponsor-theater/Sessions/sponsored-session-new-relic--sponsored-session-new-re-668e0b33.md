---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Observability"]
speakers: ["Flexible", "Open and Easy Observability for Developers"]
sched_url: https://kccnceu2021.sched.com/event/inNl/sponsored-session-new-relic-flexible-open-and-easy-observability-for-developers
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Session%3A+New+Relic+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Session: New Relic - Flexible, Open and Easy Observability for Developers

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Observability]]
- País/cidade: Virtual / Virtual
- Speakers: Flexible, Open and Easy Observability for Developers
- Schedule: https://kccnceu2021.sched.com/event/inNl/sponsored-session-new-relic-flexible-open-and-easy-observability-for-developers
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Session%3A+New+Relic+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Session: New Relic.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/inNl/sponsored-session-new-relic-flexible-open-and-easy-observability-for-developers
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Session%3A+New+Relic+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cRW1vt9TFP4
- YouTube title: New Relic Sponsored Session - Mike Panchenko, New Relic
- Match score: 0.764
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-session-new-relic/cRW1vt9TFP4.txt
- Transcript chars: 10419
- Keywords: platform, logs, cluster, product, particular, clusters, observability, tracing, distributed, internal, infrastructure, trace, basically, unique, powerful, enough, allows, container

### Resumo baseado na transcript

yeah so I'm Michaela panchenko or Mike or pancakes is what everybody really calls me I am the general manager for SATA engineering at New Relic which really just means that I'm responsible for the technical strategy and roadmap for our internal platforms and so real quick what is New Relic New Relic is an observability platform and what is that what even is observability I'm just kidding I only have 10 minutes but what we think of as an observability observability platform is a platform that absorbs the data

### Excerpt da transcript

yeah so I'm Michaela panchenko or Mike or pancakes is what everybody really calls me I am the general manager for SATA engineering at New Relic which really just means that I'm responsible for the technical strategy and roadmap for our internal platforms and so real quick what is New Relic New Relic is an observability platform and what is that what even is observability I'm just kidding I only have 10 minutes but what we think of as an observability observability platform is a platform that absorbs the data that is emitted by your apps in your infrastructure whether it be metrics events logs or trace it you emit it will consume it and will help you make sense of it that is our goal and the platform that we run is open connected and programmable and I'm gonna show you I'm gonna illustrate that with basically a case study of how we ourselves monitor New Relic with New Relic so neurotic aside from being an observability platform is also a complex infrastructure we have over 500 services I think that numbers trending down ish but until until recently the joke which wasn't a joke at all because it was the truth was that we had more services than engineers we think the humans have started to pull ahead recently so that's a good trend but the point is there's a lot of stuff to manage we also have an R DB which is a you know the New Relic database is a propriety proprietary analytics database that we built in-house which is for the intensive purposes of this talk is a complex distributed system there's several tiers to it there's a lot of state there's a lot of coordination going on so it is quite a complicated thing to monitor we have a maze dos marathon based platform that we use for deploying most of our stateless services like HTTP services and q consumers that we deployed around 2016 right before the choice became more obvious and however it's worked really well for us what we found though is that's been we've been unable to serve our internal customers that run some of these more complex stateful services trying to get that working on mazes is just too complicated too brittle and so as a result we're moving to kubernetes with an emphasis on those systems first and so we're doing all this by the way while we're processing 1.2 1.3 billion events per minute which is about 23 million per second so we're keeping pretty busy and you know so what are some things in our infrastructure that amid data one thing are obviously services and applications those things emi
