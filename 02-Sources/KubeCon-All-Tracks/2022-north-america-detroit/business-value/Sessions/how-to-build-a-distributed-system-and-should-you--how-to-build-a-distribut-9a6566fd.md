---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Business Value"
themes: ["Business Value"]
speakers: ["Rebecca Bilbro", "Patrick Deziel", "Rotational Labs"]
sched_url: https://kccncna2022.sched.com/event/182H6/how-to-build-a-distributed-system-and-should-you-rebecca-bilbro-patrick-deziel-rotational-labs
youtube_search_url: https://www.youtube.com/results?search_query=How+To+Build+a+Distributed+System+%28And+Should+You%3F%29+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How To Build a Distributed System (And Should You?) - Rebecca Bilbro & Patrick Deziel, Rotational Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Business Value]]
- Temas: [[Business Value]]
- País/cidade: United States / Detroit
- Speakers: Rebecca Bilbro, Patrick Deziel, Rotational Labs
- Schedule: https://kccncna2022.sched.com/event/182H6/how-to-build-a-distributed-system-and-should-you-rebecca-bilbro-patrick-deziel-rotational-labs
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+Build+a+Distributed+System+%28And+Should+You%3F%29+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How To Build a Distributed System (And Should You?).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182H6/how-to-build-a-distributed-system-and-should-you-rebecca-bilbro-patrick-deziel-rotational-labs
- YouTube search: https://www.youtube.com/results?search_query=How+To+Build+a+Distributed+System+%28And+Should+You%3F%29+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=39JqNkqxP3M
- YouTube title: How To Build a Distributed System (And Should You?) - Rebecca Bilbro & Patrick Deziel
- Match score: 0.842
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-to-build-a-distributed-system-and-should-you/39JqNkqxP3M.txt
- Transcript chars: 31534
- Keywords: distributed, actually, systems, question, coming, working, probably, across, source, happens, google, routing, information, singapore, together, basically, events, problems

### Resumo baseado na transcript

welcome to kubecon Welcome to our talk on how to build a distributed system and also should you um we are very excited to be here uh this is my first kubecon uh so I'm just as excited to learn as I am to sort of tell you about what we've been working on so who are we we are Patrick desil and Rebecca bilbro we both work for a company called rotational labs and rotational Labs builds small to medium-sized geodistributed systems so these are not kind of like

### Excerpt da transcript

welcome to kubecon Welcome to our talk on how to build a distributed system and also should you um we are very excited to be here uh this is my first kubecon uh so I'm just as excited to learn as I am to sort of tell you about what we've been working on so who are we we are Patrick desil and Rebecca bilbro we both work for a company called rotational labs and rotational Labs builds small to medium-sized geodistributed systems so these are not kind of like Netflix Facebook Twitter scale distributed systems but they're distributed throughout the world and uh and because of that we encounter a lot of interesting problems uh in this space and we're going to talk about some of those with you today there's a lot of overlap between uh the problems that we encounter and probably a lot of the solutions that you are working on or thinking about in your work so we're also hoping that you'll come up and chat with us later hopefully you'll be able to recognize us and you'll come find us and to tell us about what you do and what kinds of systems that you're working on so I would be remiss not to mention our team so the rotational Labs team is also geo-distributed so we're from all over the world and I wanted to give a special shout out to Karen and Benjamin who did a lot of the experimentation that kind of led to us coming up with this talk uh so the the geoping project that we'll talk about is something that they kind of incubated and so I want to give them a special shout out and if you're curious about what we and the rest of the team are working on I would encourage you to check out uh rotational.app and you can get a little sneak peek so uh our talk is a talk in four movements so I'm going to start by setting the scene and telling you about a geodistributed system that we've been building and maintaining for the last two years or so and then we're going to kind of go back a little bit into well what is a distributed system and what are some of the kind of key problems you have to solve when you are building and maintaining uh distributed systems then we're going to talk about some of the hard one lessons the things that we messed up um and we'll sort of show our cards and be honest about things that didn't go so well the first time and we'll talk about how we work through those problems and then we're going to talk a little bit about what we think is coming next based on the experiences that we've had at rotational Labs what we think is sort of coming to an open so
