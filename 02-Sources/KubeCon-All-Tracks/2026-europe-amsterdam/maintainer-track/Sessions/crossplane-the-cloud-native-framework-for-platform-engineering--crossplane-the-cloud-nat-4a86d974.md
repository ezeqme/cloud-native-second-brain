---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Jared Watts", "Adam Wolfe Gordon", "Upbound"]
sched_url: https://kccnceu2026.sched.com/event/2EF3o/crossplane-the-cloud-native-framework-for-platform-engineering-jared-watts-adam-wolfe-gordon-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+-+The+Cloud+Native+Framework+for+Platform+Engineering+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Crossplane - The Cloud Native Framework for Platform Engineering - Jared Watts & Adam Wolfe Gordon, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jared Watts, Adam Wolfe Gordon, Upbound
- Schedule: https://kccnceu2026.sched.com/event/2EF3o/crossplane-the-cloud-native-framework-for-platform-engineering-jared-watts-adam-wolfe-gordon-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+-+The+Cloud+Native+Framework+for+Platform+Engineering+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Crossplane - The Cloud Native Framework for Platform Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF3o/crossplane-the-cloud-native-framework-for-platform-engineering-jared-watts-adam-wolfe-gordon-upbound
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+-+The+Cloud+Native+Framework+for+Platform+Engineering+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zu6V34BFksk
- YouTube title: Crossplane - The Cloud Native Framework for Platform Engineering - Jared Watts & Adam Wolfe Gordon
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/crossplane-the-cloud-native-framework-for-platform-engineering/zu6V34BFksk.txt
- Transcript chars: 31289
- Keywords: crossplane, metrics, resources, platform, functions, function, basically, cluster, resource, language, control, composition, write, clusters, simple, instance, pipeline, developer

### Resumo baseado na transcript

Uh and we're going to basically let you know everything you need to know about Crossplane in this session right here. Okay, so we know that's um you know, there's going to be lots of people here who have never even used Crossplane before. Kubernetes is a control plane and it's fantastic at orchestrating containers, right? So, Crossplane basically extends Kubernetes to be a control plane for everything else. Um there's it was a great opportunity for us to learn from uh a number of years of running Crossplane, getting feedback from users, and you know, basically fixing some of the things that we didn't get right the first time, and to make it easier for everybody to use. If it's part of the Kubernetes API, you can use it with Crossplane now.

### Excerpt da transcript

All right, everybody, we're going to get started here now. Thanks for everybody for coming. So, my name is Jared. This is Adam. We're both core maintainers on the Crossplane project. Uh and we're going to basically let you know everything you need to know about Crossplane in this session right here. Okay, so we know that's um you know, there's going to be lots of people here who have never even used Crossplane before. So, as usual, we're going to start with some foundational knowledge, explain what Crossplane is, and then we'll get into the details about latest things we've been building and all that sort of stuff. So, let's start with a platform story. So, imagine a developer, they or an AI agent, whatever, that builds a new service and they want to deploy it. They want to get it out there. That service probably needs some infrastructure. Uh it's probably going to need to do some compliance and some sort of like scaling and you know, best practices and all sorts of complicated things. Um so, they've got a lot of things in front of them still to get out there and deployed.

And if they have some sort of DevOps team or platform team, whatever, maybe they'll file a ticket and they'll wait to get all that complexity. Days, maybe weeks sometimes. And we know that's true because we've talked to many Crossplane users who have basically told us that before they started using Crossplane, they would have to wait for weeks in order to be able to deploy things and get infrastructure. So, we know that's a thing. So, basically, we have this developer, they just want to ship something, but they're blocked by not only process, but complexity as well. They don't necessarily even have the skills to do this stuff anyways, right? So, they're waiting. We would like to say that there's a better way to do this. So, think about a platform, building a platform, and then exposing or offering an API to your developers so that they can do what we just talked about them doing on the last slide, uh but do it in a very easy way. So, here's maybe an API for an app. Um this is not a Crossplane concept.

This is something you can do, you can build this yourself with Crossplane. But your developer could just say, "Hey, here's my container image. Um I need database. I want Postgres, make it 100 gigs." This is the simple interface that they get. And from this very simple platform API, they get all this instead. Uh so, they you know, start with an app and then it it fans out and creates a dep
