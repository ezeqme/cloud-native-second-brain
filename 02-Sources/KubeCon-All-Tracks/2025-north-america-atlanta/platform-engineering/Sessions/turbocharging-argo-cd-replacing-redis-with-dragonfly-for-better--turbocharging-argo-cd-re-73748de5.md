---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery", "SRE Reliability"]
speakers: ["Soumya Ghosh Dastidar", "Justin Marquis", "Akuity Inc."]
sched_url: https://kccncna2025.sched.com/event/27Ff2/turbocharging-argo-cd-replacing-redis-with-dragonfly-for-better-performance-and-lower-bills-soumya-ghosh-dastidar-justin-marquis-akuity-inc
youtube_search_url: https://www.youtube.com/results?search_query=Turbocharging+Argo+CD%3A+Replacing+Redis+With+Dragonfly+for+Better+Performance+and+Lower+Bills+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Turbocharging Argo CD: Replacing Redis With Dragonfly for Better Performance and Lower Bills - Soumya Ghosh Dastidar & Justin Marquis, Akuity Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Soumya Ghosh Dastidar, Justin Marquis, Akuity Inc.
- Schedule: https://kccncna2025.sched.com/event/27Ff2/turbocharging-argo-cd-replacing-redis-with-dragonfly-for-better-performance-and-lower-bills-soumya-ghosh-dastidar-justin-marquis-akuity-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Turbocharging+Argo+CD%3A+Replacing+Redis+With+Dragonfly+for+Better+Performance+and+Lower+Bills+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Turbocharging Argo CD: Replacing Redis With Dragonfly for Better Performance and Lower Bills.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Ff2/turbocharging-argo-cd-replacing-redis-with-dragonfly-for-better-performance-and-lower-bills-soumya-ghosh-dastidar-justin-marquis-akuity-inc
- YouTube search: https://www.youtube.com/results?search_query=Turbocharging+Argo+CD%3A+Replacing+Redis+With+Dragonfly+for+Better+Performance+and+Lower+Bills+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_cUyqF6fyQg
- YouTube title: Turbocharging Argo CD: Replacing Redis With Dragonfly for... Soumya Ghosh Dastidar & Justin Marquis
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/turbocharging-argo-cd-replacing-redis-with-dragonfly-for-better-perfor/_cUyqF6fyQg.txt
- Transcript chars: 24345
- Keywords: reddus, dragonfly, itself, application, basically, argo, reddis, radius, number, actually, controller, running, containers, resources, replicas, memory, instance, resource

### Resumo baseado na transcript

Um, I know you all can be elsewhere, so thank you again for being here. I'm also an auxiliary maintainer for the past two and a half, three years. So QPI server is the Kubernetes API server that deals with the CRUD operations of all the other components. So if you want uh so ago server the ago controller and the appset controller talk with the cube API server to generate the resources and everything for your kubernetes server like API like cluster. [laughter] Okay, now that we know about the architecture, let's talk a bit more in details about Reddus in Argo CD. So if you're a heavy UI user uh using a city UI to debug or look at logs and stuff then it'll be inconvenience for you temporarily.

### Excerpt da transcript

Hello. >> Hello. Hello. Welcome. Welcome to Turbocharging Argo CD. Um, my name is Justin. I'm a support engineer here at Acuity. I'm also an Argo CD maintainer. And congratulations you all. You made it to the last talk of CubeCon. We're really excited to do this talk. Um, this is about two years in the making, testing, doing PC's. Um, so we're real glad you can make this. Um, I know you all can be elsewhere, so thank you again for being here. Um, I'm also a Argo CD maintainer. I've been working with the project for about 3 years now. Um, and I'm an avid scuba diver in Southern California. I've been diving for about 26 years. >> Hello everyone. Uh, I'm Shomo. I'm also an auxiliary maintainer for the past two and a half, three years. Uh, I'm also a founding engineer at QD. And as a pastime, you'll find me uh hopping burger joints. So if you have any suggestions, uh let me know. I'd love to give them a try. Okay, so that's a lot of food talk. Let's get in the talk itself. So uh let's talk about the agenda, what we'll be covering today.

Um so we'll start off with a quick introduction to AUCD. uh we'll talk about the architecture of AGO CD and then uh we'll talk about Reddis the star of the show or or the villain how however you want to put it um and we'll talk about what Reddus is in Argo CD what it's doing uh and the problems that we are faced with reddis once we know the problems we obviously need to know the solution so we'll talk about uh the solution Dragonfly uh and how it differs from reddis and what kind of performance benefits it can get you and finally we're going to close off uh with Justin showing some performance metrics and savings in general uh that hopefully will convince you guys to give Dragonfly a shot in your Argo City setup. Okay. Um let's talk about Argo City a bit. I'm pretty sure most of you guys here are already aware of what Ago City is, how it works and all of that. So, I'm going to keep it very short and simple. Oh, sorry. I think we jumped. There we go. So, I'm going to keep it very short. Uh if you want to know more about Ago CD there's a pretty good documentation online so you can just go up there read more about it.

It'll always be much more in detail than what I'll be covering today. So um in short ago is basically a githops uh based CD tool built for Kubernetes. So what you can do is with with arocid is like you can define your uh application resource manifests in git and tell argod where to deploy those resources to like wh
