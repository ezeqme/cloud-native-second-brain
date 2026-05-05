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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Antonio Ojea", "Benjamin Elder", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1td12/ensuring-quality-in-kubernetes-the-graduation-process-from-alpha-to-ga-antonio-ojea-benjamin-elder-google
youtube_search_url: https://www.youtube.com/results?search_query=Ensuring+Quality+in+Kubernetes%3A+The+Graduation+Process+From+Alpha+To+GA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Ensuring Quality in Kubernetes: The Graduation Process From Alpha To GA - Antonio Ojea & Benjamin Elder, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Antonio Ojea, Benjamin Elder, Google
- Schedule: https://kccnceu2025.sched.com/event/1td12/ensuring-quality-in-kubernetes-the-graduation-process-from-alpha-to-ga-antonio-ojea-benjamin-elder-google
- Busca YouTube: https://www.youtube.com/results?search_query=Ensuring+Quality+in+Kubernetes%3A+The+Graduation+Process+From+Alpha+To+GA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Ensuring Quality in Kubernetes: The Graduation Process From Alpha To GA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td12/ensuring-quality-in-kubernetes-the-graduation-process-from-alpha-to-ga-antonio-ojea-benjamin-elder-google
- YouTube search: https://www.youtube.com/results?search_query=Ensuring+Quality+in+Kubernetes%3A+The+Graduation+Process+From+Alpha+To+GA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=d_9JNRkT7dg
- YouTube title: Ensuring Quality in Kubernetes: The Graduation Process From Alpha T... Antonio Ojea & Benjamin Elder
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ensuring-quality-in-kubernetes-the-graduation-process-from-alpha-to-ga/d_9JNRkT7dg.txt
- Transcript chars: 27784
- Keywords: feature, features, testing, quality, default, cluster, release, flakes, working, actually, important, depend, running, signal, pretty, depends, process, strong

### Resumo baseado na transcript

We are going to talk about how to manage the quality in Kubernetes and explaining how the graduation process go from alpha to G. And for all of you that that know Kubernetes, you may know this how Kubernetes work. That means that every Kubernetes user is going to run their cluster and it's going to have your new feature running. about features but you see one of the strongest points of Kubernetes are the APIs right most of the features depend on the APIs the the key of the APIs is that allow to provide contrast with all these thousand project that depend on Kubernet right so you don't need to absorb all the problems in Kubernetes you can create the right interfaces define the right semantics and allow all the ecosystem to grow based on your interfaces and that's why it's important and you see that if you go The problem with APIs is that if the APIs are better and are better forever, it's hard to graduate them, right?

### Excerpt da transcript

Hello everybody, thank you for coming. We are going to talk about how to manage the quality in Kubernetes and explaining how the graduation process go from alpha to G. My name is Antonio. I work at Google. Hi, I'm Benjamin Elder. I also work at Google. Okay. We are both of the sick testing and members of steering. And for all of you that that know Kubernetes, you may know this how Kubernetes work. Kubernetes is an important open source project with a large ecosystem, right? It's not only Kubernetes. You've been here, you go to the booth, you see, I don't know how thousands of projects depend on Kubernetes, right? And to handle the development of of this project, the way we are organized is technically we have a special interesting groups, right? So each group can be horizontal and handle things like API, machinery or CLI or can be vertical like networking or not. But what is more important for for the project and for the users is the project need to keep growing need to keep evolving right and this means adding new features.

So I don't remember when this started. H we are very large and we need to get organized right. So the the the way we organize the new feature development is via caps right. So the cat process is it can be a bit heavy for newcomers or for users but it has a purpose right has the purpose of communicating across it so everybody can look at the place oh I'm proposing this because it's impossible to understand beforehand all the radius that your f is going to have so it's important that we have a center plane a center point to communicate with with all the fus and also to be transparent we are an open source project this is about community right if I want to add something I need to get fib from the other six because you don't work in isolation we try to break all the silos so there is no network there is no node there is people that is interested in node that may work on network things and people that is interested in network that may work on on all things so let's let's d a bit uh a bit more in into the care process, right?

So when you want to add a new feature, then you need to to consider what is going to be the life cycle of this feature, right? We have three stages that are alpha. The expectation of alpha is okay, I have a a feature, a proposal, I know more or less how this is going to work. I discuss it with the six and all the stakeholders. And it's I wouldn't say a prototype because we want alpha to be usable, right? People can tr
