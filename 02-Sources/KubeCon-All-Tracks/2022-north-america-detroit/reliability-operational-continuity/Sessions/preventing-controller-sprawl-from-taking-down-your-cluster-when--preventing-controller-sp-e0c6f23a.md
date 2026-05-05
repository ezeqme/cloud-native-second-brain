---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Madhu C.S.", "Robinhood Markets"]
sched_url: https://kccncna2022.sched.com/event/182GE/preventing-controller-sprawl-from-taking-down-your-cluster-when-a-scalable-pattern-stops-being-scalable-madhu-cs-robinhood-markets
youtube_search_url: https://www.youtube.com/results?search_query=Preventing+Controller+Sprawl+From+Taking+Down+Your+Cluster+-+When+a+Scalable+Pattern+Stops+Being+Scalable+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Preventing Controller Sprawl From Taking Down Your Cluster - When a Scalable Pattern Stops Being Scalable - Madhu C.S., Robinhood Markets

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Madhu C.S., Robinhood Markets
- Schedule: https://kccncna2022.sched.com/event/182GE/preventing-controller-sprawl-from-taking-down-your-cluster-when-a-scalable-pattern-stops-being-scalable-madhu-cs-robinhood-markets
- Busca YouTube: https://www.youtube.com/results?search_query=Preventing+Controller+Sprawl+From+Taking+Down+Your+Cluster+-+When+a+Scalable+Pattern+Stops+Being+Scalable+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Preventing Controller Sprawl From Taking Down Your Cluster - When a Scalable Pattern Stops Being Scalable.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GE/preventing-controller-sprawl-from-taking-down-your-cluster-when-a-scalable-pattern-stops-being-scalable-madhu-cs-robinhood-markets
- YouTube search: https://www.youtube.com/results?search_query=Preventing+Controller+Sprawl+From+Taking+Down+Your+Cluster+-+When+a+Scalable+Pattern+Stops+Being+Scalable+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fu5GXo7jmV0
- YouTube title: Preventing Controller Sprawl From Taking Down Your Cluster - When a Scalable Pattern... - Madhu C.S.
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/preventing-controller-sprawl-from-taking-down-your-cluster-when-a-scal/fu5GXo7jmV0.txt
- Transcript chars: 41506
- Keywords: server, logs, controllers, started, calico, controller, changes, components, little, desired, incident, called, resources, network, everything, getting, component, cluster

### Resumo baseado na transcript

hello everyone um I'm madhu CS I'm a software engineer at Robinhood we are a financial services company and I'm a tech lead for this team or our called as container orchestration which is responsible for running all of compute at Robinhood and Robin Hood has chosen kubernetes as the compute platform of choice so pretty much all of our compute except for some Legacy stuff is all on kubernetes um today I will be talking about controllers and how we push the limits of the controllers uh these are

### Excerpt da transcript

hello everyone um I'm madhu CS I'm a software engineer at Robinhood we are a financial services company and I'm a tech lead for this team or our called as container orchestration which is responsible for running all of compute at Robinhood and Robin Hood has chosen kubernetes as the compute platform of choice so pretty much all of our compute except for some Legacy stuff is all on kubernetes um today I will be talking about controllers and how we push the limits of the controllers uh these are production War Stories uh but before I get into the details of the agenda I want to say this um I've prepared or we have prepared the stock to be a talk for people at all levels um everybody is welcome but that said if you are an experienced cluster operator here um you might still some of the overview Concepts here might be a reputation for you but we really hope that you can take some of these things home as an inspiration or to your company back as an inspiration and pay a little bit more closer attention to some of these areas or um maybe do uh I mean revisit some of these Concepts and see what is working and what is not if you are a beginner there is definitely an overview in the beginning but some of these specifics may go over her head but that's okay um you don't have to take everything here but we still feel or hope that it will give you a solid grounding uh to the concept so that when you're ready to write your own controllers um you you can use all these lessons or learnings and hopefully it will it'll let open the hood a little bit and show the Machinery inside so that you know how exactly these things work um and coming back to the topic itself um nothing kubernetes controller pattern is a highly scalable pattern right we have seen how kubernetes scales but nothing is infinitely scalable not even slash never slash null right um so we I'll talk about how we have pushed the limits of this pattern and the incidents or outages that we ran into when we try to do that the lessons we have learned from it and um what we are do how how we solve those problems and the ongoing work right now to ensure that we don't we don't run into these limits again and again so we'll begin with a quick overview of overview of controllers and then we'll do two case studies that's where I'll be spending most of my time on case studies about where we went too far or when we hit the limits of the patterns and we'll talk about the best practices or Lessons Learned so this is the over
