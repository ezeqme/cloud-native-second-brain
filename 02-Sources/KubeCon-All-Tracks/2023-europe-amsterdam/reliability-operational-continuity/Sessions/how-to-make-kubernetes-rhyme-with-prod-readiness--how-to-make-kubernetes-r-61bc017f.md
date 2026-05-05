---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Tiffany Jernigan", "VMware", "Matthias Haeussler", "Novatec Consulting GmbH"]
sched_url: https://kccnceu2023.sched.com/event/1Hydw/how-to-make-kubernetes-rhyme-with-prod-readiness-tiffany-jernigan-vmware-matthias-haeussler-novatec-consulting-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Make+Kubernetes+Rhyme+with+Prod-Readiness+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How to Make Kubernetes Rhyme with Prod-Readiness - Tiffany Jernigan, VMware & Matthias Haeussler, Novatec Consulting GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tiffany Jernigan, VMware, Matthias Haeussler, Novatec Consulting GmbH
- Schedule: https://kccnceu2023.sched.com/event/1Hydw/how-to-make-kubernetes-rhyme-with-prod-readiness-tiffany-jernigan-vmware-matthias-haeussler-novatec-consulting-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Make+Kubernetes+Rhyme+with+Prod-Readiness+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How to Make Kubernetes Rhyme with Prod-Readiness.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hydw/how-to-make-kubernetes-rhyme-with-prod-readiness-tiffany-jernigan-vmware-matthias-haeussler-novatec-consulting-gmbh
- YouTube search: https://www.youtube.com/results?search_query=How+to+Make+Kubernetes+Rhyme+with+Prod-Readiness+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KhB9BmFKIAc
- YouTube title: How to Make Kubernetes Rhyme with Prod-Readiness - Tiffany Jernigan, VMware & Matthias Haeussler
- Match score: 0.771
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-to-make-kubernetes-rhyme-with-prod-readiness/KhB9BmFKIAc.txt
- Transcript chars: 33840
- Keywords: basically, workloads, course, cluster, actually, probably, little, infrastructure, running, security, managed, network, pretty, certainly, container, application, observability, provide

### Resumo baseado na transcript

so yeah first of all thank you all very much for coming in here um there's way more people than we ever would have expected um yeah and we know it's late in the conference the last couple of days were pretty hard and we really appreciate yeah your stamina here and um see it coming holding on until the the final end um yeah one thing before we dive in I wanted to ask real quick um on the first aid keynote Chris mentions that 58 of the participants

### Excerpt da transcript

so yeah first of all thank you all very much for coming in here um there's way more people than we ever would have expected um yeah and we know it's late in the conference the last couple of days were pretty hard and we really appreciate yeah your stamina here and um see it coming holding on until the the final end um yeah one thing before we dive in I wanted to ask real quick um on the first aid keynote Chris mentions that 58 of the participants of this year's cubecoin were like first-time participants so can I just check again who in here is here for in equipment for the first time all right that's good cool well thanks uh yeah and so and and two of you currently on in the process of going towards kubernetes and considering as a productive platform for the for the workloads still a few okay uh yeah so that that's perfect we um this is as this has been described and an intro level talk and um I hope we can share some of our experience and um and things we've learned so far with you so this is the the title how to make kubernetes rhyme with uh prod readiness um my name is Matthias I come from uh smaller uh or medium-sized company in Germany we are focused on on software engineering like modern software distributed Cloud native and microservices-based software um and I'm here with my colleague hi um I'm Tiffany Jernigan and I'm way shorter so this is a actually I'm curious who here has ever heard of the title developer Advocate before okay not so much but still kind of yeah we do stuff like this as part of it um yeah so uh it's kind of VMware is kind of the opposite sense we don't have like the Consulting but we have a bunch of our own products that are used in this whole Cloud native kubernetes and a lot more space and uh if you still use Twitter we have our Twitter handles at the bottom there and I think on my Twitter is my Mastodon link to so there's just there's things all right thanks so before we dive into the details we first of all wanted to like share with you how we came to think of of doing this talk and there's also also a bit to do with what we just said like what our working backgrounds is so so Tiffany is working for a company that basically provides a product um for running like a form having kubernetes production ready with all the things it should contain whereas I'm more from like a technology consultancy side where we help people to get their workloads onto the cloud but also to build their their stacks and and maintain them so with that
