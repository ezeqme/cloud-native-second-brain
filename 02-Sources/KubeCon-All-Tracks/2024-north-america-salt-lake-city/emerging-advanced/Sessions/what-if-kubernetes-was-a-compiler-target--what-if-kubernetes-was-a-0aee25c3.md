---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["David Morrison", "Applied Computing Research Labs", "Tim Goodwin", "UC Santa Cruz"]
sched_url: https://kccncna2024.sched.com/event/1i7pc/what-if-kubernetes-was-a-compiler-target-david-morrison-applied-computing-research-labs-tim-goodwin-uc-santa-cruz
youtube_search_url: https://www.youtube.com/results?search_query=What+if+Kubernetes+Was+a+Compiler+Target%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What if Kubernetes Was a Compiler Target? - David Morrison, Applied Computing Research Labs & Tim Goodwin, UC Santa Cruz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: David Morrison, Applied Computing Research Labs, Tim Goodwin, UC Santa Cruz
- Schedule: https://kccncna2024.sched.com/event/1i7pc/what-if-kubernetes-was-a-compiler-target-david-morrison-applied-computing-research-labs-tim-goodwin-uc-santa-cruz
- Busca YouTube: https://www.youtube.com/results?search_query=What+if+Kubernetes+Was+a+Compiler+Target%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What if Kubernetes Was a Compiler Target?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pc/what-if-kubernetes-was-a-compiler-target-david-morrison-applied-computing-research-labs-tim-goodwin-uc-santa-cruz
- YouTube search: https://www.youtube.com/results?search_query=What+if+Kubernetes+Was+a+Compiler+Target%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QcYsGytNBe8
- YouTube title: What if Kubernetes Was a Compiler Target? - David Morrison & Tim Goodwin
- Match score: 0.828
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/what-if-kubernetes-was-a-compiler-target/QcYsGytNBe8.txt
- Transcript chars: 31696
- Keywords: application, programming, multi-tier, compiler, program, actually, running, distributed, write, applications, question, message, pretty, little, language, client, framework, cluster

### Resumo baseado na transcript

is our talk about what if kubernetes was a compiler Target um I'm pretty excited about this um I think it's kind of a Nifty novel idea um so hopefully we can kind of show off some of these ideas and uh influence the uh direction of distributed computing uh for the next decade or so um so first off who are we uh my name is David um I'm a founder and research scientist at applied Computing research Labs uh previously I was at Yelp and at Airbnb doing

### Excerpt da transcript

is our talk about what if kubernetes was a compiler Target um I'm pretty excited about this um I think it's kind of a Nifty novel idea um so hopefully we can kind of show off some of these ideas and uh influence the uh direction of distributed computing uh for the next decade or so um so first off who are we uh my name is David um I'm a founder and research scientist at applied Computing research Labs uh previously I was at Yelp and at Airbnb doing uh Cloud operations uh kubernetes MOS All That Jazz um I'm a contributor to Cluster a scaler and to Carpenter I'm also the maintainer of the simcube project um we're not talking about any of that today um you can find me on slack or on hacky uh or on Blue Sky um my GitHub handles slightly different um I do want to point out uh so this is my colleague Tim I'll let him introduce himself but uh he's on the job market for internships so uh if you want to hire him he's really great I also have a team of undergrads that I'm working with out there uh who are also all fantastic and on the job market so uh if you're hiring come talk to me and I'll point you to good people okay cool yeah so as David said I'm Tim um I'm currently a PhD student at UC Santa Cruz um and my current research is on the controller programming model focusing on how to make it easier to debug and ultimately a little more developer friendly um and online or on Mastadon in GitHub you can find me at T goodwi um so let's get into it so we all know that programming distributed systems is hard and of course part of this stems from the challenges that are inherent to the nature of distribution so things like partial failure and asynchrony um but a lot of it also comes from the way that we typically write these applications so consider some really conventional user facing application that has a structure that looks something like this diagram over here we have a presentation layer some data layer and um Core Business logic connecting the two to go about implementing such an application a developer typically has to spread application logic across some front end um they have to write some serers side code and then some additional code to handle interactions with a database um so there's a lot of components here to keep track of um and to get these components working together correctly a developer has to handle things like network communication um data serialization and format conversion and in this process they may have to develop or sorry use multiple progr
