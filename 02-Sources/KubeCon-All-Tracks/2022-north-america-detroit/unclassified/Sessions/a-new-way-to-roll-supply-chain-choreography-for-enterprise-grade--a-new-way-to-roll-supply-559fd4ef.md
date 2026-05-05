---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["AI ML", "Security", "Kubernetes Core"]
speakers: ["Kirti Apte", "Steve Watkins", "VMware"]
sched_url: https://kccncna2022.sched.com/event/182HC/a-new-way-to-roll-supply-chain-choreography-for-enterprise-grade-kubernetes-kirti-apte-steve-watkins-vmware
youtube_search_url: https://www.youtube.com/results?search_query=A+New+Way+To+Roll%3A+Supply+Chain+Choreography+For+Enterprise+Grade+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# A New Way To Roll: Supply Chain Choreography For Enterprise Grade Kubernetes - Kirti Apte & Steve Watkins, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Kirti Apte, Steve Watkins, VMware
- Schedule: https://kccncna2022.sched.com/event/182HC/a-new-way-to-roll-supply-chain-choreography-for-enterprise-grade-kubernetes-kirti-apte-steve-watkins-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=A+New+Way+To+Roll%3A+Supply+Chain+Choreography+For+Enterprise+Grade+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre A New Way To Roll: Supply Chain Choreography For Enterprise Grade Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HC/a-new-way-to-roll-supply-chain-choreography-for-enterprise-grade-kubernetes-kirti-apte-steve-watkins-vmware
- YouTube search: https://www.youtube.com/results?search_query=A+New+Way+To+Roll%3A+Supply+Chain+Choreography+For+Enterprise+Grade+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oyCfoqsCd-Y
- YouTube title: A New Way To Roll: Supply Chain Choreography For Enterprise Grade... - Kirti Apte & Steve Watkins
- Match score: 0.934
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/a-new-way-to-roll-supply-chain-choreography-for-enterprise-grade-kuber/oyCfoqsCd-Y.txt
- Transcript chars: 30768
- Keywords: supply, cluster, basically, cartographer, source, template, workflow, flux, workload, config, output, little, application, github, actually, external, created, developers

### Resumo baseado na transcript

all right thank you everybody for coming showing up today very happy that you made it this afternoon uh this talk is a new way to roll we're talking about supply chain choreography for Enterprise kubernetes my name is Steve Watkins this is my colleague Kirito we're both uh um solution Architects with VMware with the tansu business unit so that means we work with all things modern apps and kubernetes and things like that so very happy to be here um let's kick it off so first thing why

### Excerpt da transcript

all right thank you everybody for coming showing up today very happy that you made it this afternoon uh this talk is a new way to roll we're talking about supply chain choreography for Enterprise kubernetes my name is Steve Watkins this is my colleague Kirito we're both uh um solution Architects with VMware with the tansu business unit so that means we work with all things modern apps and kubernetes and things like that so very happy to be here um let's kick it off so first thing why in the world would we even talk about Supply chains so our most important thing is dealing with our developers developers cost a lot of money right we want them to write code what the developers want to do they want to write code how do they want it deployed they don't care well we're at kubecon so we want it deploy to kubernetes kind of obviously but for those of you that have a little gray in your beard like me if you remember back all the way back about 15 years ago the book continuous delivery Jess humble and David Farley nailed what is the the preeminent challenge for us if somebody thinks there's a good idea how do we quickly get that in front of our users how can we make that happen and that is still the challenge that is the challenge that we're all moving towards get developers get something smart get something useful get it in front of users so that was 15 years ago even even up to today we're still running into this issue 15 years later we've built a bigger Cloud native infrastructure we're doing a lot more cool things but Joe beta if you know Joe one of the co-founders of kubernetes called out specifically our job is to manage complexity and unlock velocity for all the good features that we get out of kubernetes and Cloud native operations we're it still can create some drag so we're still struggling with with uh velocity getting things out okay so the traditional way of approaching under the way we have been approaching it is using a CI CD challenge or CI CD pretty straightforward right I identify some tasks that I need to do there's code build image run some tests build a release get it in deployed in operating Monitor and this has been around for a while it depends on an external orchestrator so an external orchestrator will start and start up each one of these tasks and it'll control them and there are some advantages for sure it's very mature it's been around for a long time there's a lot of great products out there you probably saw a lot of them on the Expo f
