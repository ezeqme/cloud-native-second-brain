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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Stephen Heywood", "Caleb Woodbine", "ii.nz"]
sched_url: https://kccncna2021.sched.com/event/lV8X/conformance-testing-the-kubernetes-api-tooling-that-makes-the-difference-stephen-heywood-caleb-woodbine-iinz
youtube_search_url: https://www.youtube.com/results?search_query=Conformance+Testing+the+Kubernetes+API%3A+Tooling+that+Makes+the+Difference+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Conformance Testing the Kubernetes API: Tooling that Makes the Difference - Stephen Heywood & Caleb Woodbine, ii.nz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Stephen Heywood, Caleb Woodbine, ii.nz
- Schedule: https://kccncna2021.sched.com/event/lV8X/conformance-testing-the-kubernetes-api-tooling-that-makes-the-difference-stephen-heywood-caleb-woodbine-iinz
- Busca YouTube: https://www.youtube.com/results?search_query=Conformance+Testing+the+Kubernetes+API%3A+Tooling+that+Makes+the+Difference+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Conformance Testing the Kubernetes API: Tooling that Makes the Difference.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8X/conformance-testing-the-kubernetes-api-tooling-that-makes-the-difference-stephen-heywood-caleb-woodbine-iinz
- YouTube search: https://www.youtube.com/results?search_query=Conformance+Testing+the+Kubernetes+API%3A+Tooling+that+Makes+the+Difference+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IQsBahak7PQ
- YouTube title: Conformance Testing the Kubernetes API: Tooling that Makes the D... Stephen Heywood & Caleb Woodbine
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/conformance-testing-the-kubernetes-api-tooling-that-makes-the-differen/IQsBahak7PQ.txt
- Transcript chars: 13407
- Keywords: conformance, endpoints, testing, cluster, instance, writing, working, around, information, running, document, markdown, export, tooling, stephen, sharing, current, coverage

### Resumo baseado na transcript

hello and welcome to conformance testing the kubernetes api tooling that makes the difference i'm caleb hello i'm stephen we're with ii a group in new zealand with a focus on cooperative coding pairing is sharing for us you can find us at ii.nz who is iii i has made up of the following humans myself and stephen who are your speakers brenda who makes ii function hippie who's the founder of ii rian who's the project manager and zack who's the data wizard so let's talk about conformance and

### Excerpt da transcript

hello and welcome to conformance testing the kubernetes api tooling that makes the difference i'm caleb hello i'm stephen we're with ii a group in new zealand with a focus on cooperative coding pairing is sharing for us you can find us at ii.nz who is iii i has made up of the following humans myself and stephen who are your speakers brenda who makes ii function hippie who's the founder of ii rian who's the project manager and zack who's the data wizard so let's talk about conformance and its tooling what is kubernetes conformance a program by the cncf to ensure that kubernetes is the same everywhere with it you get stable apis no vendor lock-in and portability of workloads when i run my workloads i expect them to run the same wherever no matter the vendor the general current conformance information about the program its vendors and distributions check out cncf dot io ck pulling that makes the difference we define and verify conformance through tests today we'll show some tooling that ii uses to help improve kubernetes conformance coverage the primary tools we'll focus on are api snip and pedo sharing data first we have the api snip suite the suite is responsible for collecting and processing the data that makes up the definition of conformance thus allowing community members to generate the data that displays the results for conformance progress and also build out tests are three components that we'll walk through first is snoop db which is a postgres database that processes the kubernetes open api spec and any etowedo log that you wish to make it ingest it runs as a job or it runs live in your cluster for querying and it also statically renders that data which is then later picked up by web which we'll talk about soon next is audit logger this is useful for live test writing it is a shim that sits between the api server and snip db it captures logs using api server audit sync and audit policy to point to itself and it's also what we use for our live conformance testing development finally we have web which you might be most familiar with it's available at apisnoop.cncf.io this is what picks up that statically rendered data and displays it as some very pretty dashboards and uh useful statistic information for sharing with the community next we have peer.sharing.io over the last year iii has built an open source development environment that runs in kurdman kubernetes we think it's pretty cool to be working inside of a cluster here given its name is about pe
