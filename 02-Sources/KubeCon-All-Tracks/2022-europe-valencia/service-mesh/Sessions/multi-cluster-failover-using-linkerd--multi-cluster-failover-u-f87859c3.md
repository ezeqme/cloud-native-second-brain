---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Service Mesh"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Charles Pretzer", "Buoyant", "Inc."]
sched_url: https://kccnceu2022.sched.com/event/ytkg/multi-cluster-failover-using-linkerd-charles-pretzer-buoyant-inc
youtube_search_url: https://www.youtube.com/results?search_query=Multi-cluster+Failover+Using+Linkerd+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Multi-cluster Failover Using Linkerd - Charles Pretzer, Buoyant, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Service Mesh]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Charles Pretzer, Buoyant, Inc.
- Schedule: https://kccnceu2022.sched.com/event/ytkg/multi-cluster-failover-using-linkerd-charles-pretzer-buoyant-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-cluster+Failover+Using+Linkerd+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Multi-cluster Failover Using Linkerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytkg/multi-cluster-failover-using-linkerd-charles-pretzer-buoyant-inc
- YouTube search: https://www.youtube.com/results?search_query=Multi-cluster+Failover+Using+Linkerd+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ieQ5eqd49BQ
- YouTube title: Multi-cluster Failover Using Linkerd - Charles Pretzer, Buoyant, Inc.
- Match score: 0.8
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/multi-cluster-failover-using-linkerd/ieQ5eqd49BQ.txt
- Transcript chars: 54187
- Keywords: cluster, traffic, linker, clusters, context, control, important, actually, failover, multi-cluster, linkery, deploy, linkedin, mesh, metrics, whatever, running, extension

### Resumo baseado na transcript

all right this is on so welcome to this session on multi-cluster fellow with lingard i'm not going to say much other than if you have any questions there's a microphone down here in the middle so please go up there and ask your questions um i'm sure charles is going to instruct how he wants his questions as well but without that i'm just gonna hand it over to ciao so please give him a big round of applause [Applause] well this is by far the biggest audience that

### Excerpt da transcript

all right this is on so welcome to this session on multi-cluster fellow with lingard i'm not going to say much other than if you have any questions there's a microphone down here in the middle so please go up there and ask your questions um i'm sure charles is going to instruct how he wants his questions as well but without that i'm just gonna hand it over to ciao so please give him a big round of applause [Applause] well this is by far the biggest audience that i've had the opportunity to speak with so first of all welcome everybody back to cubecon uh it's so exciting to see folks in person uh i you know we we've done the virtual thing for the last couple of years and i am just really energized by all of your presence right now so uh what are we gonna do today we're gonna talk about multiple kubernetes clusters we're going to talk about why we're going to do that and then we're going to talk about what it looks like to fail over your services your traffic between these two clusters i'll be honest with you i woke up in the middle of the night last night because i'm still on california time and uh i had this like vision of getting everybody up on the stage and involved like doing failover what's it what does it mean to have a single point of failure uh what how why do we need to rely on each other so if you will experiment with me on this journey i will in my head i will call out to you and maybe some of you can share this vision of relying on each other trusting each other that's what i think is really really tremendously important about being back here in person trusting each other and uh you know let's let's have fun so uh this is a workshop i think we didn't properly communicate to you like i hope that you all have a couple of kubernetes clusters that you can easily access if you don't you'll see me executing my commands up here on the screen i don't have a ton of slides we're to do a lot of walking through the terminal you'll see my aliases you'll probably see my secrets you'll see my passwords do your worst that's what i have to say so again but again trust i i'm so happy to see you all here if there are any questions during this the microphone as casper mentioned is just there um this is meant to be a dialogue i want to share this conversation with you share the space with you so anything that you want me to stop and pause let me know like i said i'm from california i have a tendency to talk very quickly uh if i'm talking too quickly slow me down rai
