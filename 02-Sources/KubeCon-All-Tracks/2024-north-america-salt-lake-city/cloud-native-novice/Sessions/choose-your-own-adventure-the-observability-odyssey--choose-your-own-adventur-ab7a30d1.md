---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Novice"
themes: ["Observability", "Storage Data"]
speakers: ["Whitney Lee", "Datadog", "Viktor Farcic", "Upbound"]
sched_url: https://kccncna2024.sched.com/event/1i7lV/choose-your-own-adventure-the-observability-odyssey-whitney-lee-datadog-viktor-farcic-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Observability+Odyssey+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Choose Your Own Adventure: The Observability Odyssey - Whitney Lee, Datadog & Viktor Farcic, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: United States / Salt Lake City
- Speakers: Whitney Lee, Datadog, Viktor Farcic, Upbound
- Schedule: https://kccncna2024.sched.com/event/1i7lV/choose-your-own-adventure-the-observability-odyssey-whitney-lee-datadog-viktor-farcic-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Observability+Odyssey+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Choose Your Own Adventure: The Observability Odyssey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lV/choose-your-own-adventure-the-observability-odyssey-whitney-lee-datadog-viktor-farcic-upbound
- YouTube search: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Observability+Odyssey+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=R3CFETvCBFU
- YouTube title: Choose Your Own Adventure: The Observability Odyssey - Whitney Lee & Viktor Farcic
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/choose-your-own-adventure-the-observability-odyssey/R3CFETvCBFU.txt
- Transcript chars: 29106
- Keywords: application, prometheus, metrics, argo, tracing, minutes, deployment, production, jagger, version, choose, running, already, traces, working, traffic, observability, applications

### Resumo baseado na transcript

welcome to Choose Your Own Adventure The observability Odyssey meet hero Hero's application source code on a developer's laptop here alongs to be a real application running and production serving end users and we're going to help Hero on their Journey so my name oh we're going to help hero navigate hundreds of cncf projects choose which ones to use integrate them with one another so hero can live their dream my name is Whitney this is Victor together we host a streaming show called you choose on Victor's devops

### Excerpt da transcript

welcome to Choose Your Own Adventure The observability Odyssey meet hero Hero's application source code on a developer's laptop here alongs to be a real application running and production serving end users and we're going to help Hero on their Journey so my name oh we're going to help hero navigate hundreds of cncf projects choose which ones to use integrate them with one another so hero can live their dream my name is Whitney this is Victor together we host a streaming show called you choose on Victor's devops toolkit YouTube channel we have some stickers to give away after so come to us and each episode represents a system design choice and so for each episode We Gather all the relevant cncf technology that can do that thing we have a guest on from each technology and each guest gets only five minutes to present about their technology then at the end we have a vote and whatever the community chooses is the one that we Implement into our ongoing demo So based on choices the communities already made we have a demo environment going now so it is made up of an AWS eks cluster that's defined declaratively with crossplane resources it also has our heroes already deployed in a running application and it was deployed with gitops with Argo CD in particular we have Ingress already running and we have Contour because that's what you chose and so therefore end users can already access the application so hero is living their dream they are running a production what are we doing here we're done okay we don't have any observability it's hardly a production cluster at all so we don't know what's happening with applications we can't understand our system if something's broken we don't know how to fix it hero is not doing well so we're going to save the day please get out your phones please scan this QR code we're going to go through some system design choices as part of the talk today and whatever you choose is the one we're going to implement in our ongoing demo maybe so we're going to talk about metrics we're going to talk about traces and we're going to use that data to implement a progressive delivery so and we're going to help hero live their dream so let's start with metrics when we vote in a while I'm going to talk a bit first when we vote it's going to be between Prometheus and pixie but first let's talk about what is metrics what is a metric a metric is simply a numerical measurement at a point in time and so an example would be how long a database query takes o
