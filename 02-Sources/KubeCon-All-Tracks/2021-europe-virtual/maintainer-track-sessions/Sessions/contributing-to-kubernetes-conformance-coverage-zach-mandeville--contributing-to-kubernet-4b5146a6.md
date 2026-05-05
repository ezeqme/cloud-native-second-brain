---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["https://ii.coop/"]
sched_url: https://kccnceu2021.sched.com/event/iE77/contributing-to-kubernetes-conformance-coverage-zach-mandeville-caleb-woodbine-iicoop-httpsiicoop
youtube_search_url: https://www.youtube.com/results?search_query=Contributing+to+Kubernetes+Conformance+Coverage+-+Zach+Mandeville+%26+Caleb+Woodbine%2C+ii.coop+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Contributing to Kubernetes Conformance Coverage - Zach Mandeville & Caleb Woodbine, ii.coop - https://ii.coop/

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: https://ii.coop/
- Schedule: https://kccnceu2021.sched.com/event/iE77/contributing-to-kubernetes-conformance-coverage-zach-mandeville-caleb-woodbine-iicoop-httpsiicoop
- Busca YouTube: https://www.youtube.com/results?search_query=Contributing+to+Kubernetes+Conformance+Coverage+-+Zach+Mandeville+%26+Caleb+Woodbine%2C+ii.coop+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Contributing to Kubernetes Conformance Coverage - Zach Mandeville & Caleb Woodbine, ii.coop.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE77/contributing-to-kubernetes-conformance-coverage-zach-mandeville-caleb-woodbine-iicoop-httpsiicoop
- YouTube search: https://www.youtube.com/results?search_query=Contributing+to+Kubernetes+Conformance+Coverage+-+Zach+Mandeville+%26+Caleb+Woodbine%2C+ii.coop+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=05NMwOhD6Ks
- YouTube title: Contributing to Kubernetes Conformance Coverage - Zach Mandeville & Caleb Woodbine, ii.coop
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/contributing-to-kubernetes-conformance-coverage-zach-mandeville-caleb/05NMwOhD6Ks.txt
- Transcript chars: 13639
- Keywords: conformance, coverage, results, showing, writing, cluster, endpoints, ticket, certified, submit, endpoint, actually, vendor, process, happening, intended, untested, number

### Resumo baseado na transcript

hi and welcome to contributing to kubernetes conformance coverage i'm zach and i'm caleb and we are from ii and today we are going to be talking about what is conformance why it's valuable and the tools that we can use to help achieve it so to start a bit about ii we are a group of technical folk here in aotearoa new zealand with a focus on cooperative coding we believe that pairing is sharing and we pair in everything we do including these presentations and you can find

### Excerpt da transcript

hi and welcome to contributing to kubernetes conformance coverage i'm zach and i'm caleb and we are from ii and today we are going to be talking about what is conformance why it's valuable and the tools that we can use to help achieve it so to start a bit about ii we are a group of technical folk here in aotearoa new zealand with a focus on cooperative coding we believe that pairing is sharing and we pair in everything we do including these presentations and you can find out more about us at ii.coop the people that make up iii uh we're a small of a powerful bunch consisting of hippie hacker who is the founder and sort of vision of ii myself and caleb who you have met as well as stephen who is our resident test writer rhian who is our project manager and helps us keep us on track and focused brno who does a lot of the automation and proud jobs that we some of which we'll be seeing later on and brenda who ensures that all of us can actually function and now let's talk about kubernetes conformance what is conformance yeah kubernetes conformance is a program that enables every vendor to support the required apis as do the open source community versions it's valuable to have consistency across the platform wherever it's run and why is conformance important good question it enables portability of workloads freedom from vendor lock-in and stable apis it also allows consistency across providers really i expect my workloads to run the same regardless of where which whichever vendor it is or wherever it is there's a good background and rationale for conformance at cncf dot io ck here you'll also see some nicely detailed steps on how vendors can be certified as kate's conformant right now there are about 67 certified distributions the full list you can see at landscape.cncf.io and then click on the certified case link on the left but this list is great that means that you can have consistent unsurprising fully conforming behavior across a breadth of providers these vendors are certified and added to the list that we just saw through a transparent and open process on the cades conformance repo on github we will cover this process in the presentation shortly this process is enabled or is able to happen because in kubernetes the conformance is defined through the api and a test suite that allows for tools to be built that fit in within existing kubernetes workflows two great examples of that are sono buoy and api snoop how do i certify my distribution i use sonaboy sono
