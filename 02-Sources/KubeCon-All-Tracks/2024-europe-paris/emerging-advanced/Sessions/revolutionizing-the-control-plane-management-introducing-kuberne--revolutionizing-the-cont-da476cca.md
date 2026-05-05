---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Katie Gamanji", "Apple", "Jussi Nummelin", "Mirantis", "Cesar Wong", "Red Hat", "Tyler Lisowski", "IBM", "Adriano Pezzuto", "CLASTIX"]
sched_url: https://kccnceu2024.sched.com/event/1YeQ1/revolutionizing-the-control-plane-management-introducing-kubernetes-hosted-control-planes-katie-gamanji-apple-jussi-nummelin-mirantis-cesar-wong-red-hat-tyler-lisowski-ibm-adriano-pezzuto-clastix
youtube_search_url: https://www.youtube.com/results?search_query=Revolutionizing+the+Control+Plane+Management%3A+Introducing+Kubernetes+Hosted+Control+Planes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Revolutionizing the Control Plane Management: Introducing Kubernetes Hosted Control Planes - Katie Gamanji, Apple; Jussi Nummelin, Mirantis; Cesar Wong, Red Hat; Tyler Lisowski, IBM; Adriano Pezzuto, CLASTIX

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Katie Gamanji, Apple, Jussi Nummelin, Mirantis, Cesar Wong, Red Hat, Tyler Lisowski, IBM, Adriano Pezzuto, CLASTIX
- Schedule: https://kccnceu2024.sched.com/event/1YeQ1/revolutionizing-the-control-plane-management-introducing-kubernetes-hosted-control-planes-katie-gamanji-apple-jussi-nummelin-mirantis-cesar-wong-red-hat-tyler-lisowski-ibm-adriano-pezzuto-clastix
- Busca YouTube: https://www.youtube.com/results?search_query=Revolutionizing+the+Control+Plane+Management%3A+Introducing+Kubernetes+Hosted+Control+Planes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Revolutionizing the Control Plane Management: Introducing Kubernetes Hosted Control Planes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQ1/revolutionizing-the-control-plane-management-introducing-kubernetes-hosted-control-planes-katie-gamanji-apple-jussi-nummelin-mirantis-cesar-wong-red-hat-tyler-lisowski-ibm-adriano-pezzuto-clastix
- YouTube search: https://www.youtube.com/results?search_query=Revolutionizing+the+Control+Plane+Management%3A+Introducing+Kubernetes+Hosted+Control+Planes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j3ARknQ6PoM
- YouTube title: Revolutionizing the Control Plane Management: Introducing Kubernetes Hosted Control Planes
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/revolutionizing-the-control-plane-management-introducing-kubernetes-ho/j3ARknQ6PoM.txt
- Transcript chars: 28563
- Keywords: control, planes, cluster, hosted, actually, running, management, working, managed, workloads, network, perhaps, clusters, infrastructure, recovery, within, course, question

### Resumo baseado na transcript

I am very happy to see such a full room for this panel we will aim to talk about hosted control planes and how we can revolutionize the control plane within kubernetes now we have a w very wide audience um before we start I would like to ask the audience how many of you have heard about hosted control planes right that's amazing how many of you are using this in production at the moment oh I can see some hands perfect um so before we going to start

### Excerpt da transcript

I am very happy to see such a full room for this panel we will aim to talk about hosted control planes and how we can revolutionize the control plane within kubernetes now we have a w very wide audience um before we start I would like to ask the audience how many of you have heard about hosted control planes right that's amazing how many of you are using this in production at the moment oh I can see some hands perfect um so before we going to start I would like to introduce myself and of course my panel my name is Katy ganji and currently I am a senior field engineer at Apple as well in addition to that I one of the TU or technical oversight Committee Member for cncf today we have a wonderful panel with experts within this area that will share their wisdom and their experience with hosted control planes and i' would like to ask them to introduce themselves so perhaps let's start with you Taylor and we just going to go around hey everyone to Super grateful for yall's time today U my name is Tyra lowski I'm the lead architect of IBM Cloud satellite and work um on the delivery of our manage services um on premise and in multicloud environments um super excited to speak with cl today hey I'm music from mes um one of the things that I'm working on at MES is our K Cube drro and the accom accompanying implementation of posted control PL called Co hi everyone so my name is Adriano I'm the founder of Classics um a company that started to investigate the hosted control plane uh model from the beginning from 2020 more or less and we in 2022 we uh released uh our uh implementation of the hoset control plane that is called kamagi it's uh open source and uh uh quite uh Ro poost and production ready thank you and hello uh I am Caesar Wong I'm an engineer at Red Hat I've been working on hosted control planes for about 5 years which is very long time for me uh most recently I am working on the hypershift project um which is an implementation of Hosta control planes for open shift um and I'm I'm super glad to be here amazing now as we have seen sorry uh some of you are familiar with hosted control planes and the notion of it some of you are running it in production however for the interest of being declarative into explaining this terminology and what it actually means I would like to ask Adriana to explain what hosted control planes are yeah thank you uh so uh the control plane is a design pattern is a new design pattern for bernes architecture uh well you have two layers
