---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Medya Ghazizadeh", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyUz/minikube-from-cli-to-gui-medya-ghazizadeh-google
youtube_search_url: https://www.youtube.com/results?search_query=Minikube+from+CLI+to+GUI+%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Minikube from CLI to GUI ! - Medya Ghazizadeh, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Medya Ghazizadeh, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyUz/minikube-from-cli-to-gui-medya-ghazizadeh-google
- Busca YouTube: https://www.youtube.com/results?search_query=Minikube+from+CLI+to+GUI+%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Minikube from CLI to GUI !.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUz/minikube-from-cli-to-gui-medya-ghazizadeh-google
- YouTube search: https://www.youtube.com/results?search_query=Minikube+from+CLI+to+GUI+%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=74X1RmqfUzs
- YouTube title: Minikube from CLI to GUI ! - Medya Ghazizadeh, Google
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/minikube-from-cli-to-gui/74X1RmqfUzs.txt
- Transcript chars: 31271
- Keywords: docker, actually, driver, minicube, release, github, another, machine, called, happened, website, command, invested, add-ons, add-on, interesting, drivers, probably

### Resumo baseado na transcript

ah hello everyone uh good noon almost is almost noon uh happy to be in Amsterdam and I'm here to talk about mini cube with you uh first of all who am I my name is Media gazizadeh I've been maintaining mini cubes since 2019. I have released 86 versions of mini cube out of 140 total mini Cube versions I'm also a software engineer at Google slash manager um what is mini Cube uh by chop hand who here has used Mini Cube does everybody almost I think most because mini Cube the design of mini cube is you use it at that time use a virtual machine to start a kubernetes cluster and virtual machines could not be tested in prow or in a container or a regular testing you have to have user of it or maintainer of it another work stream of the mini cubes orbit is uh the official add-ons you might know that mini Cuba is more than 20 add-ons and we officially maintain some of these add-ons like Auto Parts storage provisioner JCPS Cube maintainer tooling you're going to learn about some of those tooling such as goproc flake rate csat trash party and other tooling the other work stream is the benchmarking tools that we have developed about three or four main benchmarking tools for kubernetes and well now we could actually talk about GUI I'm glad that we have time to to to look at the demo of it so mini Cube GUI uh um this is the how it looks like it's just a try icon oh my God I

### Excerpt da transcript

ah hello everyone uh good noon almost is almost noon uh happy to be in Amsterdam and I'm here to talk about mini cube with you uh first of all who am I my name is Media gazizadeh I've been maintaining mini cubes since 2019. I have released 86 versions of mini cube out of 140 total mini Cube versions I'm also a software engineer at Google slash manager um what is mini Cube uh by chop hand who here has used Mini Cube does everybody almost I think most of the people's hands are up so I don't think we need much intro to minicube in this talk we're just gonna go through years of my experience as a mini Cube painter going through a kind of like a history of mini Cube to the latest news of mini Q which is Mini kipkui main cube is a tool that quickly sets up a local kubernetes cluster and popular platforms such as Mac OS Linux and windows with a special focus on developers application developers and the new kubernetes users and our own survey data confirms that as well 42 of our users are the ones who use minicube to develop applications whenever I go to kubecon people recognize mini cube with the Emoji it's like oh that's the one with the Emojis right so I was like yeah yeah that's the one with the Emojis and who are the people Behind These emojis other than me they're Stephen Powell uh there is uh undersberg land rogovic and honorable mentions of previous maintenors Dan Lauren you probably know his name by Ching from chain guard and Thomas Stromberg and more than 800 individual contributors thank you to all of them uh mini cubes started with a GitHub issue in 2016.

so the idea was setting up kubernetes is hard can we have something that just users just set it up because you don't you don't need that most people don't have a Linux workstation you just want to play with kubernetes that was the original GitHub issue and Dan Lauren responds like hey I want to take this issue I want this and he actually said I have a physical Windows machine under my desk I could use this as test lab for that and the reason he said that because mini Cube the design of mini cube is you use it at that time use a virtual machine to start a kubernetes cluster and virtual machines could not be tested in prow or in a container or a regular testing you have to have actual physical machine that supports virtualization and at that time in the cloud providers there was no nested virtualization so you could not even use a uh cloud provider at that time but there's a uh to it by Dan Lauren that
