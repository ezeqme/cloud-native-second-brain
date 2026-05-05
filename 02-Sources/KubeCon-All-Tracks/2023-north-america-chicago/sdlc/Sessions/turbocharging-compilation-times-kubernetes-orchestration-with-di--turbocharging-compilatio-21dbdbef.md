---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "SDLC"
themes: ["Kubernetes Core"]
speakers: ["Diogo Guerra", "CERN"]
sched_url: https://kccncna2023.sched.com/event/1R2sE/turbocharging-compilation-times-kubernetes-orchestration-with-distributed-compilation-tools-diogo-guerra-cern
youtube_search_url: https://www.youtube.com/results?search_query=Turbocharging+Compilation+Times%3A+Kubernetes+Orchestration+with+Distributed+Compilation+Tools+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Turbocharging Compilation Times: Kubernetes Orchestration with Distributed Compilation Tools - Diogo Guerra, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Diogo Guerra, CERN
- Schedule: https://kccncna2023.sched.com/event/1R2sE/turbocharging-compilation-times-kubernetes-orchestration-with-distributed-compilation-tools-diogo-guerra-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Turbocharging+Compilation+Times%3A+Kubernetes+Orchestration+with+Distributed+Compilation+Tools+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Turbocharging Compilation Times: Kubernetes Orchestration with Distributed Compilation Tools.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sE/turbocharging-compilation-times-kubernetes-orchestration-with-distributed-compilation-tools-diogo-guerra-cern
- YouTube search: https://www.youtube.com/results?search_query=Turbocharging+Compilation+Times%3A+Kubernetes+Orchestration+with+Distributed+Compilation+Tools+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uxCeqShs-MI
- YouTube title: Turbocharging Compilation Times: Kubernetes Orchestration with Distributed Compilati... Diogo Guerra
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/turbocharging-compilation-times-kubernetes-orchestration-with-distribu/uxCeqShs-MI.txt
- Transcript chars: 16632
- Keywords: actually, compilation, worker, distributed, compile, scheduler, basically, client, create, friend, resources, schedule, dependencies, native, trying, around, problems, machine

### Resumo baseado na transcript

uh thank you for coming to my presentation um we're going to talk about the distributed compilation tools and trying to implement them uh with kubernetes uh my name is dioa I'm a former Computing engineer um atern uh with the kubernetes team uh where I mainly focused on integrating tools ranging from monitoring logging and Driver configuration uh so that the users can launch a cluster with all these features and to be available uh with um our Central uh monitoring um on demand um so once upon a

### Excerpt da transcript

uh thank you for coming to my presentation um we're going to talk about the distributed compilation tools and trying to implement them uh with kubernetes uh my name is dioa I'm a former Computing engineer um atern uh with the kubernetes team uh where I mainly focused on integrating tools ranging from monitoring logging and Driver configuration uh so that the users can launch a cluster with all these features and to be available uh with um our Central uh monitoring um on demand um so once upon a time around four years ago I was a young Computing engineer at CERN and uh I was just discovering how awesome was kubernetes and uh how we could deploy and scale these applications that were load balance B it by a service and I used to live uh with a friend which was a software engineer and my friend who at a Saturday was trying to compile his tool I was complaining that uh the application compilation was taking too much time and uh I was turned to him man don't you have like a can't you use like a distributed comp compilation tool um for sure like there's something available but PD didn't know about anything and actually I had this idea like uh would it because I knew about these tools and I was fascinated with kubernetes so wouldn't it be nice to like uh use kubernetes to scale up and down this uh work work uh worker um workloads and uh like could we do a service with this and so um come we come to our motivation so at CERN um CERN actually has lots of many applications that are managed and contributed to by lots of manage lots of many teams small and big and these Solutions sometimes are not small and they are really they really take time to compile and here you have the two most common tools which uh is root which is a a tool that scientists use to analyze and uh visualize the large amounts of data produced by the L and also we have our own readon file system for software distribution so this has some uh problems is that um it's it's problematic for a team to actually uh manage this so it's expensive to set up and maintain uh in terms of um Manpower so if you have different teams doing the same thing you're actually losing resources and it's also expensive to run because uh if the resources just stay idle you're losing money so um also it's my experience and I hope I think yours too that uh users when they use something they opt for the easiest solution and uh sometimes it's uh not easy enough and users don't do exactly what they should um so from the challenges
