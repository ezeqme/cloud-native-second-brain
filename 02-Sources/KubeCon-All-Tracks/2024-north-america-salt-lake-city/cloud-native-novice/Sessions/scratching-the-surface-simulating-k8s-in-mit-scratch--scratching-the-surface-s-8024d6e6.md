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
themes: ["Cloud Native Novice"]
speakers: ["Mitch Connors", "Microsoft", "Jude Connors", "Independent"]
sched_url: https://kccncna2024.sched.com/event/1i7nk/scratching-the-surface-simulating-k8s-in-mit-scratch-mitch-connors-microsoft-jude-connors-independent
youtube_search_url: https://www.youtube.com/results?search_query=Scratching+the+Surface%3A+Simulating+K8s+in+MIT+Scratch+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scratching the Surface: Simulating K8s in MIT Scratch - Mitch Connors, Microsoft & Jude Connors, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Cloud Native Novice]]
- País/cidade: United States / Salt Lake City
- Speakers: Mitch Connors, Microsoft, Jude Connors, Independent
- Schedule: https://kccncna2024.sched.com/event/1i7nk/scratching-the-surface-simulating-k8s-in-mit-scratch-mitch-connors-microsoft-jude-connors-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Scratching+the+Surface%3A+Simulating+K8s+in+MIT+Scratch+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scratching the Surface: Simulating K8s in MIT Scratch.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nk/scratching-the-surface-simulating-k8s-in-mit-scratch-mitch-connors-microsoft-jude-connors-independent
- YouTube search: https://www.youtube.com/results?search_query=Scratching+the+Surface%3A+Simulating+K8s+in+MIT+Scratch+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yTXVvY7gTR8
- YouTube title: Scratching the Surface: Simulating K8s in MIT Scratch - Mitch Connors, Microsoft & Jude Connors
- Match score: 0.818
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scratching-the-surface-simulating-k8s-in-mit-scratch/yTXVvY7gTR8.txt
- Transcript chars: 28035
- Keywords: replica, scratch, replicas, another, started, little, deployment, create, replicator, controller, couple, actually, screen, basically, declarative, objects, unschedulable, understand

### Resumo baseado na transcript

all right welcome everyone to scratching the surface uh we are going to be simulating kubernetes today using the MIT scratch programming language uh and before you ask yourself why in the world would anyone simulate kubernetes in the MIT scratch programming language uh let's set some context as we get started how many of you have ever uh engaged with a getting started with kubernetes guide an intro guide that looked something like this okay yeah I see a couple hands I think I've written a couple so guilty

### Excerpt da transcript

all right welcome everyone to scratching the surface uh we are going to be simulating kubernetes today using the MIT scratch programming language uh and before you ask yourself why in the world would anyone simulate kubernetes in the MIT scratch programming language uh let's set some context as we get started how many of you have ever uh engaged with a getting started with kubernetes guide an intro guide that looked something like this okay yeah I see a couple hands I think I've written a couple so guilty as charged I don't want to shame or blame any of these These are well-intentioned people but I think that the key problem to most getting started guides that I read is that they are written by people a lot like me my name is Mitch Connors I'm a principal software engineer for Microsoft I've been a maintainer on the iso project for six years now where I currently serve on the TOC I'm also a CNC Ambassador and that is a list of reasons why I should not be allowed to give an intro to kubernetes talk uh I have not been intro to kubernetes in quite some time I'm way too far down in the weeds and I immediately want to tell you about how cool validating admission policies are when you don't know what a pot is they're not that cool so what we need for a talk like this is someone who is indeed new to the community so that we can see kubernetes through new eyes uh I'm hopeful that this will help the those of us who are new to cubec con new to kubernetes to understand some of the fundamentals of the project and how it works what makes it great but I'm also hopeful that for those of us who have been around in the community for quite a long time this will give us a new perspective on what's important what matters and where the next generation will take kubernetes so for that I'd like to invite my designated expert non-expert also my son Jude coners up to the stage and just for the audience's sake Jude did I make you do this no all right are you turned on on your mic there okay good so Jude why don't you tell us a little bit about yourself hello I'm Jude I started coding about 2 years ago um in my free time I like to read books and play games currently my favorite games are MTG and Warhammer all right we got some fans in the room that's good and Jude how many years of experience do you have with kubernetes none okay okay well then we're in the right place there's a QR code on this slide that's going to connect you to our uh demo and I'm going to keep it up for the next
