---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Observability", "Kubernetes Core", "Community Governance"]
speakers: ["Joe Lanford", "Anik Bhattacharjee", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV7W/building-catalogs-of-operators-for-olm-the-declarative-way-joe-lanford-anik-bhattacharjee-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Building+Catalogs+of+Operators+for+OLM+the+Declarative+Way+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Building Catalogs of Operators for OLM the Declarative Way - Joe Lanford & Anik Bhattacharjee, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Joe Lanford, Anik Bhattacharjee, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV7W/building-catalogs-of-operators-for-olm-the-declarative-way-joe-lanford-anik-bhattacharjee-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Catalogs+of+Operators+for+OLM+the+Declarative+Way+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Building Catalogs of Operators for OLM the Declarative Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7W/building-catalogs-of-operators-for-olm-the-declarative-way-joe-lanford-anik-bhattacharjee-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Building+Catalogs+of+Operators+for+OLM+the+Declarative+Way+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3_MnWTuuMN8
- YouTube title: Building Catalogs of Operators for OLM the Declarative Way - Joe Lanford & Anik Bhattacharjee
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/building-catalogs-of-operators-for-olm-the-declarative-way/3_MnWTuuMN8.txt
- Transcript chars: 28921
- Keywords: catalog, operator, bundle, database, catalogs, package, operators, basically, cluster, command, version, bundles, channel, directory, install, upgrade, container, images

### Resumo baseado na transcript

hi everyone um welcome to this talk by the olem team for kubecon um north america 2021 in today's talk we'll be discussing om catalogs and how a paradigm shift from imperative to declarative in the context of building oil catalogs reduced the cost of building and maintaining catalog artifacts drastically my name is anik i'm a software engineer working at red hat primarily focusing on the orbital lifecycle manager project commonly referred to as olm i'm joined by my teammate joe who's a principal software engineer also working at

### Excerpt da transcript

hi everyone um welcome to this talk by the olem team for kubecon um north america 2021 in today's talk we'll be discussing om catalogs and how a paradigm shift from imperative to declarative in the context of building oil catalogs reduced the cost of building and maintaining catalog artifacts drastically my name is anik i'm a software engineer working at red hat primarily focusing on the orbital lifecycle manager project commonly referred to as olm i'm joined by my teammate joe who's a principal software engineer also working at red hat who's also a part of the welcome team in today's presentation i will be going over a short refresher on what an operator is then i'll be covering a short refresher on what the operator lifecycle manager project is about i will then talk about what oem catalogs are and then discuss what the current catalog building process looks like i'll also be showcasing some of the pain points involved in building catalogs in the current imperative way joe will then talk about the new declarative solution for building catalogs and how it manages to ease the pain points of building imperative catalogs and in the process showcase a significant reduction in cost the new solution enabled for everyone involved in building and maintaining catalogs finally we will close out with a demo of the new workflow for building catalogs so let's begin with a short refresher on operators um operas were first introduced by coreos as as a concept for a special class of software they're basically application specific controller that extends the kubernetes api to create configure and manage instances of stateful applications on behalf of kubernetes users it builds upon the basic kubernetes resource and controller concept but includes domain or application specific knowledge to automate common tasks so when you talk about any software you need a way to manage the lifecycle of the software at least in the context of enterprise softwares this is where the operator lifecycle manager project comes into play the opera lifecycle manager project is a component of the operative framework which is an open source toolkit to manage the lifecycle of operators in a streamlined and scalable way olm extends kubernetes to provide a declarative way to install manage and upgrade operators on a cluster it provides a way to make operators and their services available for cluster users to select and install essentially olm enables operators to behave like managed services provider
