---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Open Interfaces + Interoperability"
themes: ["Kubernetes Core"]
speakers: ["Daniel Mangum", "Upbound"]
sched_url: https://kccncna2022.sched.com/event/182DE/content-addressable-crds-type-uniqueness-across-kubernetes-clusters-daniel-mangum-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Content+Addressable+CRDs%3A+Type+Uniqueness+Across+Kubernetes+Clusters+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Content Addressable CRDs: Type Uniqueness Across Kubernetes Clusters - Daniel Mangum, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Daniel Mangum, Upbound
- Schedule: https://kccncna2022.sched.com/event/182DE/content-addressable-crds-type-uniqueness-across-kubernetes-clusters-daniel-mangum-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Content+Addressable+CRDs%3A+Type+Uniqueness+Across+Kubernetes+Clusters+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Content Addressable CRDs: Type Uniqueness Across Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182DE/content-addressable-crds-type-uniqueness-across-kubernetes-clusters-daniel-mangum-upbound
- YouTube search: https://www.youtube.com/results?search_query=Content+Addressable+CRDs%3A+Type+Uniqueness+Across+Kubernetes+Clusters+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4mmt-SbqMcU
- YouTube title: Content Addressable CRDs: Type Uniqueness Across Kubernetes Clusters - Daniel Mangum, Upbound
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/content-addressable-crds-type-uniqueness-across-kubernetes-clusters/4mmt-SbqMcU.txt
- Transcript chars: 44090
- Keywords: actually, cluster, behavior, package, define, programming, defined, content, instance, provider, higher, composition, definition, digest, namespace, saying, install, already

### Resumo baseado na transcript

um let's go ahead and get started um this is a a fairly jam-packed presentation so I want to make sure to jump into the content quickly I do promise to do some live demos um at the end so uh hopefully you all can finish out your kubecon with watching me break some stuff um but I appreciate you all sticking around uh to the very end I hope you all have had a great week today we're going to be talking about uh content addressable crds and that's

### Excerpt da transcript

um let's go ahead and get started um this is a a fairly jam-packed presentation so I want to make sure to jump into the content quickly I do promise to do some live demos um at the end so uh hopefully you all can finish out your kubecon with watching me break some stuff um but I appreciate you all sticking around uh to the very end I hope you all have had a great week today we're going to be talking about uh content addressable crds and that's really the solution uh to a problem and that problem generically is that we aren't able to establish uniqueness of types across kubernetes clusters and this has become more of an issue as we've moved to what you might call a cluster as cattle model right where we have lots and lots of kubernetes clusters and also when we have kind of new models of kubernetes I don't know if you all have seen any of the talks or demos around kcp this week but that's an example of kind of a newer model of kubernetes that forces us to think uh about a larger scope than just a single physical cluster so I generally like to start off by giving you a bit of an idea of where we're going to be going in this talk so you can stand up and go catch your flight if this doesn't look good to you but what we're going to start with is just generally talking about how you can extend the kubernetes API surface this is likely an area that lots of you folks are already familiar with but we want to set that that ground level for us to be able to build on top of then we're going to talk about two aspects of programming generically that are important that we don't really have in kubernetes today and that's internal versus user-facing types and programming in an abstract cluster sense and I know those may not mean anything quite yet so we'll make sure to define those terms as we go along and then we'll come up with a solution for these types spread across many clusters and round out with a demo so starting off with extending the kubernetes API surface there are a couple different ways to extend the kubernetes API but the kubernetes API comes with a set of built-in types you can really just think about these as endpoints if you want to think about a rest API server which is actually what the kubernetes API server is and these are the ones you know and love like pods deployments Services Etc et cetera things that are there to allow you to do the core job that kubernetes was created for which is container orchestration uh and this is usually the case I did ment
