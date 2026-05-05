---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Cat Morris", "Jake Klein", "Syntasso"]
sched_url: https://kccnceu2025.sched.com/event/1txGH/building-a-platform-framework-lessons-learned-from-developing-a-multi-cluster-kubernetes-operator-cat-morris-jake-klein-syntasso
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Platform+Framework%3A+Lessons+Learned+From+Developing+a+Multi-Cluster+Kubernetes+Operator+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building a Platform Framework: Lessons Learned From Developing a Multi-Cluster Kubernetes Operator - Cat Morris & Jake Klein, Syntasso

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Cat Morris, Jake Klein, Syntasso
- Schedule: https://kccnceu2025.sched.com/event/1txGH/building-a-platform-framework-lessons-learned-from-developing-a-multi-cluster-kubernetes-operator-cat-morris-jake-klein-syntasso
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Platform+Framework%3A+Lessons+Learned+From+Developing+a+Multi-Cluster+Kubernetes+Operator+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building a Platform Framework: Lessons Learned From Developing a Multi-Cluster Kubernetes Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGH/building-a-platform-framework-lessons-learned-from-developing-a-multi-cluster-kubernetes-operator-cat-morris-jake-klein-syntasso
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Platform+Framework%3A+Lessons+Learned+From+Developing+a+Multi-Cluster+Kubernetes+Operator+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AHY4IDlBhzE
- YouTube title: Building a Platform Framework: Lessons Learned From Developing a Multi-Cl... Cat Morris & Jake Klein
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-a-platform-framework-lessons-learned-from-developing-a-multi/AHY4IDlBhzE.txt
- Transcript chars: 26366
- Keywords: platform, cluster, clusters, complexity, actually, pretty, realized, started, ecosystem, product, working, already, manage, multiple, little, definitely, complicated, multicluster

### Resumo baseado na transcript

So we are here to talk to you a little bit about building a platform framework. And before that I worked on platform products uh at Thoughtworks and other companies working for five or six years in this platform Kubernetes domain. They're going to have different requirements, different scales, different compute power. We know the different clouds all offer Kubernetes, but they have different authentication models. And this problem grows even further when you get bigger and more effective and more successful as a business. They're working on that on-prem environment with not just those Kubernetes clusters, but you've got virtual machines.

### Excerpt da transcript

So we are here to talk to you a little bit about building a platform framework. Lessons learned from developing a multiclusters Kubernetes operator. So we are from Cintaso and we work on cratics. That was one of our original stickers. Let me know if you know the joke. I don't really get it. Um so I'm Cat Morris. I'm the product manager here at Centasto. I've been here for about year and a half, two years now. And before that I worked on platform products uh at Thoughtworks and other companies working for five or six years in this platform Kubernetes domain. I'm here with Jake. Yeah. Hi. Uh I'm Jake. Uh I'm an engineer here at Centaso. Been here almost three years. Um prior to that was working at WeWorks and all of their open source projects. And we're going to start with a little story that's definitely not based on fact or any of our previous experiences at all. And we've definitely just made it up for this conference talk. Uh there's a new product in the market, a new startup called AI, I'm a little teapot, and Jake and I have been roped in as new members of their infrastructure devops s sur platform team to start building out ways for their developers to be more efficient.

So we start with our teams. They need a way to deploy workloads, databases, anything into environments. How are they going to do that? Yeah, just a single Kubernetes cluster. It's a pretty easy thing to do when you're getting started. Maybe you go to the cloud provider of your choice, do some click ops in the UI, and get a cluster and you're good to go. Okay, we quickly realized that one cluster is not really going to do it. We're going to need production. We're going to need development. They're going to have different requirements, different scales, different compute power. Still pretty easy to manage, right? Yeah. Not not too difficult. Just do the same sets as before, get another cluster. It's a bit more operational overhead, but it's not too intimidating. Okay, we've had an outage. We've realized we need to be a little bit more robust and resilient. We want to look into availability zones so that we've got a replica of these things across our different environments now. Yeah. Okay. You've just doubled the number of clusters again.

Bit more operational overhead. You're starting to feel a bit more like a platform team looking after these clusters. Maybe you start to think about other tools in the ecosystem you could use to manage these clusters. But, you know, it's still early da
