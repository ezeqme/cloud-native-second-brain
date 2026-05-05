---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Scott Rigby", "Independent", "Andrew Block", "Karena Angell", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HyV2/learn-the-helm-code-base-and-pr-review-process-scott-rigby-independent-andrew-block-karena-angell-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Learn+the+Helm+Code+Base+and+PR+Review+Process+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Learn the Helm Code Base and PR Review Process - Scott Rigby, Independent; Andrew Block & Karena Angell, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Scott Rigby, Independent, Andrew Block, Karena Angell, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HyV2/learn-the-helm-code-base-and-pr-review-process-scott-rigby-independent-andrew-block-karena-angell-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Learn+the+Helm+Code+Base+and+PR+Review+Process+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Learn the Helm Code Base and PR Review Process.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyV2/learn-the-helm-code-base-and-pr-review-process-scott-rigby-independent-andrew-block-karena-angell-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Learn+the+Helm+Code+Base+and+PR+Review+Process+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ULw33QRMuNE
- YouTube title: Learn the Helm Code Base and PR Review Process - Scott Rigby, Andrew Block & Karena Angell
- Match score: 0.782
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/learn-the-helm-code-base-and-pr-review-process/ULw33QRMuNE.txt
- Transcript chars: 31297
- Keywords: maintainer, probably, basically, actually, charts, maintainers, testing, github, requests, request, command, important, projects, process, package, certain, someone, triage

### Resumo baseado na transcript

okay cool hey everybody uh you're here because you are interested in learning the helm code base for various reasons hopefully part of it is to help review pull requests so that you can get the features that you want into Helm that are already in open pull requests and they're probably about there are probably about 300 of the 300 something now so so we appreciate uh your interest and your help so I'm Scott Rigby um I am a developer Advocate currently working nowhere and um I I'm

### Excerpt da transcript

okay cool hey everybody uh you're here because you are interested in learning the helm code base for various reasons hopefully part of it is to help review pull requests so that you can get the features that you want into Helm that are already in open pull requests and they're probably about there are probably about 300 of the 300 something now so so we appreciate uh your interest and your help so I'm Scott Rigby um I am a developer Advocate currently working nowhere and um I I'm a hill maintainer I have been since 2016 or so um when I really started working with the charts repo if any of you remember the stable incubator charts repos that was really a big part of what I initially did um but you know involved in various levels of Helm and uh yeah I'm current angel I'm one of the helm web maintainers um been involved for a couple of years now I don't know time time is a weird construct right now um and point of this time I currently work for red hat and Andy yeah hey everyone Andy block a distinguished architect at Red Hat all with Karina um I have been a chart maintainer for about for a year been in the Care Community for a few years my focus in the project is enhancing and improving oci integration so using oci and storing charts within oci Registries is my primary focus as well as every as well as this General contribution to the project I do want to quickly point out that we have two other maintainers that I can see right now they're in the front row so if you have more questions you can find them later too well she just threw under the bus and Martin if you don't know Martin he was a huge influence on the three to four of migration two to three sorry yeah yeah so um so we're gonna start with it this is just the agenda for today um most of this we're going to go rather quickly through and we're going to focus most of our time on um on exploring the helm code based on depth but it's important to like set up a few of these things a bit and then kind of like help say well then what do you do next um so yeah so uh so what is Helm so Helm is a package manager it sounds like okay every who doesn't wait who who knows what Helm is and who uses Helm already okay when you come to an event like kubecon you never know who's going to show up it might be their first foray into kubernetes let's go ahead and let's start with The Primitives exactly who here has not heard or used Helm raise your hand okay so for the people that are are watching this recording later just
