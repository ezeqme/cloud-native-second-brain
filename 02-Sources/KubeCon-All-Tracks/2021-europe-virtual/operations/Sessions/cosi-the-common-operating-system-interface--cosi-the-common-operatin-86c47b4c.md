---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Operations"
themes: ["Operations"]
speakers: ["Steven Borrelli", "Mastercard", "Andrew Rynhard", "Talos-Systems"]
sched_url: https://kccnceu2021.sched.com/event/iE1h/cosi-the-common-operating-system-interface-steven-borrelli-mastercard-andrew-rynhard-talos-systems
youtube_search_url: https://www.youtube.com/results?search_query=COSI%3A+The+Common+Operating+System+Interface+CNCF+KubeCon+2021
slides: []
status: parsed
---

# COSI: The Common Operating System Interface - Steven Borrelli, Mastercard & Andrew Rynhard, Talos-Systems

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Operations]]
- Temas: [[Operations]]
- País/cidade: Virtual / Virtual
- Speakers: Steven Borrelli, Mastercard, Andrew Rynhard, Talos-Systems
- Schedule: https://kccnceu2021.sched.com/event/iE1h/cosi-the-common-operating-system-interface-steven-borrelli-mastercard-andrew-rynhard-talos-systems
- Busca YouTube: https://www.youtube.com/results?search_query=COSI%3A+The+Common+Operating+System+Interface+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre COSI: The Common Operating System Interface.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1h/cosi-the-common-operating-system-interface-steven-borrelli-mastercard-andrew-rynhard-talos-systems
- YouTube search: https://www.youtube.com/results?search_query=COSI%3A+The+Common+Operating+System+Interface+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=i6MQb8QsUdU
- YouTube title: COSI: The Common Operating System Interface - Steven Borrelli & Andrew Rynhard
- Match score: 0.81
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cosi-the-common-operating-system-interface/i6MQb8QsUdU.txt
- Transcript chars: 18772
- Keywords: operating, systems, another, container, kernel, engine, plugins, events, common, having, called, controller, itself, resource, plug-in, configuration, actually, finally

### Resumo baseado na transcript

hello everyone and welcome to our session on cozy here at kuchan eu we hope you're enjoying the conference so far i'm stephen pirelli and i'm andrew reinhart we're very excited to show cozy to a larger audience for the first time cozy is the result of developing talos for the last five years and distilling the lessons we've learned into a specification we would like to share with the world let's start at the very beginning and define what cozy is cozy it's an acronym for the common operating

### Excerpt da transcript

hello everyone and welcome to our session on cozy here at kuchan eu we hope you're enjoying the conference so far i'm stephen pirelli and i'm andrew reinhart we're very excited to show cozy to a larger audience for the first time cozy is the result of developing talos for the last five years and distilling the lessons we've learned into a specification we would like to share with the world let's start at the very beginning and define what cozy is cozy it's an acronym for the common operating system interface and what it concerns itself with is the configuration of the nodes that run in a kubernetes cluster so whenever you provision a new cluster first you provision the nodes whether they're bare metal or vm and then on the next thing is you actually have to configure those nodes for things like networking disk any processes that you want to run installing the kubernetes software that's what cozy concerns itself with it also gave us a chance to reimagine operating systems and for this is what we do in operating systems in a kubernetes world another thing about cozy that's actually been really fun is it given us the chance to rethink exactly what it means to be an operating system in the age of containers and distributed schedulers finally let's talk about the why cozy one of the reasons is that kubernetes and its ecosystem from cluster api to things like the storage and networking interfaces they're deeply intertwined with the underlying linux operating system in many ways and what we find is that kubernetes and linux they don't only differ in the way they're implemented technologically but there's also a difference in philosophy in the way the systems are composed and we're going to talk about this a little bit the philosophy of unix and what we see is that this causes problems at the boundary where kubernetes and linux interact with one another so now that we've talked about the motivation for this project let's talk about some of the things that we'd like to have as desired features the first thing one of our highest priorities is having an operating system that is completely api driven and what this means in practice is that we want an operating system that doesn't need to have a shell installed and we would not like to have people sshing into this box to configure things everything on the operating system should be configurable via an api another thing that we're really looking to implement in this operating system is having configuration settings have
