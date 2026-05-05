---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Serverless"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["William Denniss", "Google Cloud"]
sched_url: https://kccnceu2022.sched.com/event/ytnX/building-a-nodeless-kubernetes-platform-william-denniss-google-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Nodeless+Kubernetes+Platform+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Building a Nodeless Kubernetes Platform - William Denniss, Google Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Serverless]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: William Denniss, Google Cloud
- Schedule: https://kccnceu2022.sched.com/event/ytnX/building-a-nodeless-kubernetes-platform-william-denniss-google-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Nodeless+Kubernetes+Platform+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Building a Nodeless Kubernetes Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytnX/building-a-nodeless-kubernetes-platform-william-denniss-google-cloud
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Nodeless+Kubernetes+Platform+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H2iI9o-qwBE
- YouTube title: Building a Nodeless Kubernetes Platform - William Denniss, Google Cloud
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/building-a-nodeless-kubernetes-platform/H2iI9o-qwBE.txt
- Transcript chars: 39995
- Keywords: actually, platform, product, design, little, managed, running, basically, create, couple, security, probably, workloads, nodeless, autopilot, believe, resources, daemon

### Resumo baseado na transcript

i'm william dennis and thank you for coming to my session on building a nodeless kubernetes platform first a little background about me i'm a product manager in google cloud where i work on kubernetes engine in 2019 i co-founded gke autopilot and that's what i currently work on this is a new mode of operation for gke which i'll be talking a bit about today i'm a very big supporter of the kubernetes open source project and in 2017 i also co-founded the certified kubernetes conformance program which is

### Excerpt da transcript

i'm william dennis and thank you for coming to my session on building a nodeless kubernetes platform first a little background about me i'm a product manager in google cloud where i work on kubernetes engine in 2019 i co-founded gke autopilot and that's what i currently work on this is a new mode of operation for gke which i'll be talking a bit about today i'm a very big supporter of the kubernetes open source project and in 2017 i also co-founded the certified kubernetes conformance program which is still used today to ensure portability between vendors distributions of kubernetes i'm also writing a book published by manning called kubernetes for developers a little bit about this session i hope it's going to be useful for all of you um as you build or build on kubernetes platforms of your own in this session i plan to give you a behind-the-scenes look of the creation of gke autopilot which is a fully managed platform for kubernetes by my team i'll be giving throughout the presentation some arguments for and against uh the idea of having nodes in a so-called nodeless platform and at the end i'll talk a little bit about some of the future possibilities that can be enabled by this design firstly let me do a quick audience poll so i'd like to know raise your hand who believes that it's possible to have a noble kubernetes where there is still technically a node object show hands got a couple not too many who doesn't everyone else yeah and third option who believes i was just adding a bit of controversy to my kubecon talk to you know spruce up the marketing a bit all right um well the truth probably lies somewhere in the middle of of of those three um but let's let's dig in so what does you know as we look at building a fully managed kubernetes platform i think it's worth taking a step back and looking at a traditional kubernetes platform and i'll be using gke as the example here so a traditional kubernetes platform basically consists of two apis that you need to interact with as the developer the first one above is the kubernetes api that's what you're here for right that's what you're a kubecon for that's what you use kubernetes for you want to describe your you know stateless app in a deployment you want to maybe represent a reddest database or a marie db database as a stateful set you want to create jobs for your workloads etc that's that's what you're here for and then you have this other api under the line which is the platform api whether it's gke or on
