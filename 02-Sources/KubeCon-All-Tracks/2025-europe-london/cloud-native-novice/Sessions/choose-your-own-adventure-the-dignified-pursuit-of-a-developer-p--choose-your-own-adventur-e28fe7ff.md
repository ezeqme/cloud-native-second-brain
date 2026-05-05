---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["Platform Engineering"]
speakers: ["Whitney Lee", "CNCF Ambassador", "Viktor Farcic", "Upbound"]
sched_url: https://kccnceu2025.sched.com/event/1txFt/choose-your-own-adventure-the-dignified-pursuit-of-a-developer-platform-whitney-lee-cncf-ambassador-viktor-farcic-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Dignified+Pursuit+of+a+Developer+Platform+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Choose Your Own Adventure: The Dignified Pursuit of a Developer Platform - Whitney Lee, CNCF Ambassador & Viktor Farcic, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Whitney Lee, CNCF Ambassador, Viktor Farcic, Upbound
- Schedule: https://kccnceu2025.sched.com/event/1txFt/choose-your-own-adventure-the-dignified-pursuit-of-a-developer-platform-whitney-lee-cncf-ambassador-viktor-farcic-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Dignified+Pursuit+of+a+Developer+Platform+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Choose Your Own Adventure: The Dignified Pursuit of a Developer Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFt/choose-your-own-adventure-the-dignified-pursuit-of-a-developer-platform-whitney-lee-cncf-ambassador-viktor-farcic-upbound
- YouTube search: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Dignified+Pursuit+of+a+Developer+Platform+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hnmtjCkO8FE
- YouTube title: Choose Your Own Adventure: The Dignified Pursuit of a Developer Platf... Whitney Lee & Viktor Farcic
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/choose-your-own-adventure-the-dignified-pursuit-of-a-developer-platfor/hnmtjCkO8FE.txt
- Transcript chars: 28927
- Keywords: application, platform, developers, cluster, database, policy, backstage, already, argo, developer, interface, running, crossplane, scaling, resources, created, technology, repository

### Resumo baseado na transcript

Welcome to Choose Your Own Adventure, the dignified pursuit of a developer platform. Hero longs to be a real application running in production serving end users. So we need your help though because we're going to go through some system design choices, choose which ones to use, and Victor's going to build a live demo as we go. But we're going to even take a step back from that and say we should build our platform with Kubernetes APIs. And also we're going to take advantage of that Kubernetes synchronization loop. So we can use Kubernetes resources to declarative declaratively define states and then it's going to make that state an actual state.

### Excerpt da transcript

Welcome to Choose Your Own Adventure, the dignified pursuit of a developer platform. So glad you're here, y'all. Meet Hero. Hero is application source code on a developer's laptop. Hero longs to be a real application running in production serving end users. And we've been helping Hero along their way. So, we've helped Hero uh evaluate hundreds of CNCF projects, choose which ones to use, integrate them with one another so Hero can live their dream. I'm Whitney. This guy in a skirt is Victor. And uh together, I know, I know I'm messing with you, Chris. Uh together, we host a show called You Choose. So, it's a streaming show on Victor's DevOps Toolkit YouTube channel, and each episode represents a system design choice. So for each system design choice, we gather all the relevant CNCF technology that can do that thing. We invite a maintainer on from each technology and that maintainer gets only five minutes to present about what their technology does because we just want an overview. Then after that's done, we put it to a vote and the community chooses which technology we implement in our ongoing demo.

So so far in the show, what we've already chosen is here we go. Build packs for container images. Harbor for a registry. Carbell for application configuration. Search manager for certificates. Crossplane to declaratively define a database as a Kubernetes API. And then we're have this uh schema hero for schema for that database. Devspace for developing on Kubernetes. Argo CD for githops. We have contour for ingress. Cube armor for runtime security. External secrets operator for secrets. We have psyllium for network uh uh network policy. We have a cubecape for kubernetes scanning. We have notary project for signing. We have smithy spiffy inspire for workload identity. Kclo for authentication. Open fga for authorization. We have headlamp for kubernetes API. We have Thanos and uh Prometheus for collecting and scaling metrics. Open telemetry and jaggert for tracing. Isto for service mesh and open cost for cost management. Oh my god, this is too too much. How do we do this y'all? What have we done to ourselves? So that's why we have that's why platform engineering has gotten so popular.

So an internal developer platform is a set of integrated capabilities that are available to developers for them to use in their day-to-day work. So there are three types of people involved in making an internal developer platform. This is an overgeneralization but it's a good uh good
