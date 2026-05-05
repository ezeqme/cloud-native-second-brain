---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Hidde Beydals", "Michael Bridgen", "Weaveworks"]
sched_url: https://kccncna2021.sched.com/event/lV7o/fluxs-roadmap-to-general-availability-hidde-beydals-michael-bridgen-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Flux%27s+Roadmap+to+General+Availability+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Flux's Roadmap to General Availability - Hidde Beydals & Michael Bridgen, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Hidde Beydals, Michael Bridgen, Weaveworks
- Schedule: https://kccncna2021.sched.com/event/lV7o/fluxs-roadmap-to-general-availability-hidde-beydals-michael-bridgen-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Flux%27s+Roadmap+to+General+Availability+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Flux's Roadmap to General Availability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7o/fluxs-roadmap-to-general-availability-hidde-beydals-michael-bridgen-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Flux%27s+Roadmap+to+General+Availability+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8RFxYooMc5A
- YouTube title: Flux's Roadmap to General Availability - Hidde Beydals & Michael Bridgen, Weaveworks
- Match score: 0.723
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/fluxs-roadmap-to-general-availability/8RFxYooMc5A.txt
- Transcript chars: 18061
- Keywords: flux, automation, cluster, controllers, object, repository, version, commit, controller, running, update, updates, resource, source, command, images, possible, objects

### Resumo baseado na transcript

today we're going to talk about road map flux v2 through to general availability or ga and a peak beyond that i'm going to talk about the road map weighted somewhat towards future developments then here it will give you a demo of what you can do with flux v2 today first of all who am i or just some engineer let's move on to summarize the history of flux what's now called flux v1 was created at weaveworks to deploy new versions of services to a software as a

### Excerpt da transcript

today we're going to talk about road map flux v2 through to general availability or ga and a peak beyond that i'm going to talk about the road map weighted somewhat towards future developments then here it will give you a demo of what you can do with flux v2 today first of all who am i or just some engineer let's move on to summarize the history of flux what's now called flux v1 was created at weaveworks to deploy new versions of services to a software as a service implementation called wecloud prior to version 1.0 it concentrated mainly on upgrading upgrading container images but then we made a big change in june which turned it all around so that it applied everything from git and made updates by committing to git this was the big bang event for gitops flux was inducted into the cncf as a sandbox project in august but by then it was creaking it needed to be modernized things like custom resource definitions weren't around when it was created in early 2020 what became flux v2 was started with the same scope but using modern modern tooling like controller runtime and supporting multiplexing eg running more than one sink the flux project was classified as adopt in the cncf technology radar in 2020 and promoted to incubation status in 2021 here we are roughly 18 months after the inception of flux b2 looking forward to it being generally available what does that mean what does general availability mean usually it's taken to mean that a piece of software is considered ready to run in production within open source people have different appetites for risk so many would have already adopted a product before ga release but here is what it means flux v2 first of all it means covering the bases that flux v1 covered roughly speaking syncing from git to a cluster updating image wraps in yaml files and committing that to get sending no notifications eg to slack when things have been done and clarity declarative installation of helm charts most of these things have been improved and generalized in flux v2 and in particular as i said everything is now multiplexed you can define as many sources sinks updates and notifications as you need after a ga release the rule is usually backward compatibility public apis must be stable from this point on so it's a point of no return in a way there are a few areas that still need development before we're happy to make it generally available to have confidence that flux does what it says and the debug escape rate is under control we n
