---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Alexander Matyushentsev", "Akuity"]
sched_url: https://kccncna2025.sched.com/event/27NnT/offline-not-off-limits-edge-fleet-management-with-argo-cd-alexander-matyushentsev-akuity
youtube_search_url: https://www.youtube.com/results?search_query=Offline%2C+Not+Off-Limits%3A+Edge+Fleet+Management+With+Argo+CD+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Offline, Not Off-Limits: Edge Fleet Management With Argo CD - Alexander Matyushentsev, Akuity

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Alexander Matyushentsev, Akuity
- Schedule: https://kccncna2025.sched.com/event/27NnT/offline-not-off-limits-edge-fleet-management-with-argo-cd-alexander-matyushentsev-akuity
- Busca YouTube: https://www.youtube.com/results?search_query=Offline%2C+Not+Off-Limits%3A+Edge+Fleet+Management+With+Argo+CD+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Offline, Not Off-Limits: Edge Fleet Management With Argo CD.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NnT/offline-not-off-limits-edge-fleet-management-with-argo-cd-alexander-matyushentsev-akuity
- YouTube search: https://www.youtube.com/results?search_query=Offline%2C+Not+Off-Limits%3A+Edge+Fleet+Management+With+Argo+CD+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rUy7c6OpjMk
- YouTube title: Offline, Not Off-Limits: Edge Fleet Management With Argo CD - Alexander Matyushentsev, Akuity
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/offline-not-off-limits-edge-fleet-management-with-argo-cd/rUy7c6OpjMk.txt
- Transcript chars: 29679
- Keywords: argo, cluster, application, clusters, applications, manage, solution, actually, server, customers, customer, version, administrator, question, directory, specific, github, running

### Resumo baseado na transcript

Welcome to Argo CD maintainers talk and um as you can guess from the name uh we're going to talk about using Argo CD to manage clusters that are running at age. So we're going to share our experience about how do you install workloads and manage those workloads on small clusters that don't have u a lot of connectivity and uh before I start the talk let me introduce myself by the way sorry for the knows how to use and we run into some challenges and then we come up with pretty much a solution. And so I will introduce uh not introduce actually it was introduced before but I will remind about not very popular feature called Argo CD core and then a set of solutions we implemented to help them manage applications keep uh visibility and also uh uh solve the problem of delivering artifacts to these clusters. And now let's talk a little bit about um running uh Kubernetes clusters at age. So through our journey while working with different customers, we learned that Kubernetes actually is not running only in big uh large data centers.

### Excerpt da transcript

Welcome to Argo CD maintainers talk and um as you can guess from the name uh we're going to talk about using Argo CD to manage clusters that are running at age. So we're going to share our experience about how do you install workloads and manage those workloads on small clusters that don't have u a lot of connectivity and uh before I start the talk let me introduce myself by the way sorry for the voice it's the first day of conference so I kind of lost it after speaking with lots of people so my name is uh Alexander Matense I prefer to gorgeous by Alex M and uh I'm one of the co-creators of Argo project. I've been working on Argo for like eight or nine years already and um I'm a my primary focus is Argo CD. So that's why I'm mostly speaking about Argo CD and also I'm a co co-founder and chief architect that company called Acuity where we help customers to take the maximum out of Argo CD and and help them manage Kubernetes. Uh this is the slide that marketing team asked me to add. So you might know two folks uh Andrew and uh Christopher uh they are very active in the community not just Argo CD and they recently published a book and uh this book is available for free.

Just scan the QR code and you can get an electronic copy and this that hope everyone took the screenshot. uh I want to talk about uh agenda of this uh talk and I will explain what I'm going to cover. So uh as I mentioned at Acuity we help multiple customers to use Argo CD and uh among just you know building products we also help them to come up with solutions. And so one of our customers uh came to us and asked for help to figure out how would they manage uh clusters at age that are running at age locations and they described you know what they want to do and explained us you know what use cases they want to solve and I I'm going to share all of that with you and next we kind of we try to just use uh Argo CD in a very traditional way that you know very well covered and everyone knows how to use and we run into some challenges and then we come up with pretty much a solution. So not a product but a set of decisions we had to make to make this experience good for them. And so I will introduce uh not introduce actually it was introduced before but I will remind about not very popular feature called Argo CD core and then a set of solutions we implemented to help them manage applications keep uh visibility and also uh uh solve the problem of delivering artifacts to these clusters.

And now let's tal
