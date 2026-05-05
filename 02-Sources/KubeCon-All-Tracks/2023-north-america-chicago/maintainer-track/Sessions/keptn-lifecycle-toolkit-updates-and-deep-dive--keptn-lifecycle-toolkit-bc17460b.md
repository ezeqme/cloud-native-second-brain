---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Giovanni Liva", "Anna Reale", "Dynatrace"]
sched_url: https://kccncna2023.sched.com/event/1R2t0/keptn-lifecycle-toolkit-updates-and-deep-dive-giovanni-liva-anna-reale-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Keptn+Lifecycle+Toolkit+Updates+and+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keptn Lifecycle Toolkit Updates and Deep Dive - Giovanni Liva & Anna Reale, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Giovanni Liva, Anna Reale, Dynatrace
- Schedule: https://kccncna2023.sched.com/event/1R2t0/keptn-lifecycle-toolkit-updates-and-deep-dive-giovanni-liva-anna-reale-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Keptn+Lifecycle+Toolkit+Updates+and+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keptn Lifecycle Toolkit Updates and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2t0/keptn-lifecycle-toolkit-updates-and-deep-dive-giovanni-liva-anna-reale-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Keptn+Lifecycle+Toolkit+Updates+and+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H3UxOwS06iI
- YouTube title: Keptn Lifecycle Toolkit Updates and Deep Dive - Giovanni Liva & Anna Reale, Dynatrace
- Match score: 0.8
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keptn-lifecycle-toolkit-updates-and-deep-dive/H3UxOwS06iI.txt
- Transcript chars: 17917
- Keywords: captain, analysis, metric, template, cluster, metrics, deployment, little, application, multiple, instance, provider, operator, observability, definition, objective, actually, second

### Resumo baseado na transcript

you guys hi thanks for the patience let's start now yeah so welcome to this talk about Captain uh Deep dive and an update on this cncf project we are an incubator project since one year I am Hanah one of the maintainer next to me here invisible is javanni which is actually right now at home sick so yeah sad but hey he is with us in hard so what can we do let's move on what do we do today we talk today about Captain I don't know

### Excerpt da transcript

you guys hi thanks for the patience let's start now yeah so welcome to this talk about Captain uh Deep dive and an update on this cncf project we are an incubator project since one year I am Hanah one of the maintainer next to me here invisible is javanni which is actually right now at home sick so yeah sad but hey he is with us in hard so what can we do let's move on what do we do today we talk today about Captain I don't know if you are familiar what Captain is so I want to start from why Captain why should you be interested in Captain and you have been until now at the boot and checking out cncf projects probably and uh we have been there also multiple times with our project and we like to listen to people and to see what people needs right especially devops and Sr and that's out of this this that uh we came out with uh a few tools and a few things that you can use as an S and as a devops to make your life easier so here are three things why Captain first of all is based to support SES second of all is actually a server plate of things it's a lot of uh tools that you can take pick and choose according to what is your use case and what is your need and finally we don't reinvent the will uh takes the joke with the helm actually we don't remember the helm uh we are based on kubernetes Primitives so we are something that you should be used to and it should be very easy and very simple immediate to to adopt if you find it interesting today I want to go through three typical use cases that we have talked with people about and that you may be interested in these are observability metrics and uh slos for each of these use cases I will present you you a part of the toolkit that you may use I will go a little bit in the details with the dirty yamel and stuff but I try to make this as funny and lightweight as possible because let's face it it's very late in the afternoon today yeah um but please after the talk feel free to come and discuss all The Nasty details so start with observability why do we need observability what have we seen in observability that may be useful for divs Sr I want to start and zoom in in a very typical scenario which is the typical black box kind of view of your deployment you may have your um repo where you your developers are pushing their new fresh new codes you may have your tool of choice such as Argo Jenkins or whatnot that is trying for your code to become something that is running in your cluster and then you have the the cluster r
