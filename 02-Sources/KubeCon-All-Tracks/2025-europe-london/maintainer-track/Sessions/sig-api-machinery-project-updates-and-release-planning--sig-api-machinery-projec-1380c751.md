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
themes: ["AI ML", "Community Governance"]
speakers: ["Joe Betz", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tcz3/sig-api-machinery-project-updates-and-release-planning-joe-betz-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG+API+Machinery%3A+Project+Updates+and+Release+Planning+CNCF+KubeCon+2025
slides: []
status: parsed
---

# SIG API Machinery: Project Updates and Release Planning - Joe Betz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Joe Betz, Google
- Schedule: https://kccnceu2025.sched.com/event/1tcz3/sig-api-machinery-project-updates-and-release-planning-joe-betz-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+API+Machinery%3A+Project+Updates+and+Release+Planning+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre SIG API Machinery: Project Updates and Release Planning.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcz3/sig-api-machinery-project-updates-and-release-planning-joe-betz-google
- YouTube search: https://www.youtube.com/results?search_query=SIG+API+Machinery%3A+Project+Updates+and+Release+Planning+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VCmp--NcxeE
- YouTube title: SIG API Machinery: Project Updates and Release Planning - Joe Betz, Google
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sig-api-machinery-project-updates-and-release-planning/VCmp--NcxeE.txt
- Transcript chars: 27922
- Keywords: validation, version, machinery, support, server, resources, couple, controller, performance, actually, control, request, clients, change, working, provide, resource, running

### Resumo baseado na transcript

Um, so I just given a couple minutes for people to um, make their way over. Um, before I worked on API machinery, I also worked on uh, as a maintainer of CD for a couple years. Um, sometimes you'll hear the term KRM, which means Kubernetes of resource model. Um beyond that we um take responsibility for the reliability, scale and performance of most of the control plane. Um and that's I think that's benefited us both and has resulted in some opportunities to improve performance which is great. Um, so this this makes for a lot more predictable performance of your workload.

### Excerpt da transcript

Okay, let's get started. Um, thanks for waiting everybody. Uh, the keynotes got going a little bit late. Um, so I just given a couple minutes for people to um, make their way over. My name is Joe Betts. I work on SIG API machinery as a technical lead. I've been doing that for a couple years. Um, before I worked on API machinery, I also worked on uh, as a maintainer of CD for a couple years. So um, have a background in kind of both systems. So today's um agenda is kind of an intro level um session for API machinery. So if you don't know what API machinery is, um we're going to spend some time going over that. Then we're going to go over the updates um in the Kubernetes 1.33 release that we've been working on. Um and then we'll kind of finish out talking about some future plans and how to get involved in the SIG. So let's look at what API machinery is. It's a kind of a broad crosscutting SIG. Um so it's a lot of different responsibilities. Um our core responsibility is the rest mechanics of the Kubernetes API.

Um so that includes everything that is involved in defining a REST API, the versioning, um the serialization protocols, resources, sub resources, all of that. Um and at its core like one of the main things we do is we provide support for building resource definitions. Um, so that's how you build types like the built-in types, pod, node, those types of things. But also how you build custom resources, so CRDs and things like that. Um, sometimes you'll hear the term KRM, which means Kubernetes of resource model. So we kind of have an opinionated approach to what a resource is. Um, and a lot of that is supported by API machinery. Um, the various aspects of that include everything from defaulting to versioning to conversion. um the semantics of apply and patch mechanics, subresources, um all kinds of things like that. Um we have um a significant amount of investment into control plane extensibility. So that includes you know custom resources is one of the most prominent and obvious examples. Um but you can also add custom resources through aggregated API servers.

So we support that. Um we support extensibility of the admission control. What that means is anytime a request um is coming in a right request is coming in to the control plane you can intercept that um through admission control. You can either reject it or modify it. Um and so we have two mechanisms mechanisms for that. One is called web hooks. So admission web hooks you can validate or mutate u
