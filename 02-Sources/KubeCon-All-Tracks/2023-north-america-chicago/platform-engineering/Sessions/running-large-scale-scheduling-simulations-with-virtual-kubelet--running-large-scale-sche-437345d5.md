---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["David Morrison", "Applied Computing Research Labs"]
sched_url: https://kccncna2023.sched.com/event/1R2pX/running-large-scale-scheduling-simulations-with-virtual-kubelet-david-morrison-applied-computing-research-labs
youtube_search_url: https://www.youtube.com/results?search_query=Running+Large-Scale+Scheduling+Simulations+with+Virtual+Kubelet+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Running Large-Scale Scheduling Simulations with Virtual Kubelet - David Morrison, Applied Computing Research Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: David Morrison, Applied Computing Research Labs
- Schedule: https://kccncna2023.sched.com/event/1R2pX/running-large-scale-scheduling-simulations-with-virtual-kubelet-david-morrison-applied-computing-research-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Running+Large-Scale+Scheduling+Simulations+with+Virtual+Kubelet+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Running Large-Scale Scheduling Simulations with Virtual Kubelet.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pX/running-large-scale-scheduling-simulations-with-virtual-kubelet-david-morrison-applied-computing-research-labs
- YouTube search: https://www.youtube.com/results?search_query=Running+Large-Scale+Scheduling+Simulations+with+Virtual+Kubelet+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=epII6_JwQSA
- YouTube title: Running Large-Scale Scheduling Simulations with Virtual Kubelet - David Morrison
- Match score: 0.974
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/running-large-scale-scheduling-simulations-with-virtual-kubelet/epII6_JwQSA.txt
- Transcript chars: 28392
- Keywords: cluster, simulation, running, actually, little, trace, production, simulated, replay, important, deployment, virtual, started, controller, tracer, scheduling, working, custom

### Resumo baseado na transcript

uh okay cool it's 11 o'clock um I think we'll go ahead and get started um sorry before we begin uh I just have one thing I need to do real quick um I've been working on this uh custom controller uh I was kind of hoping to have it uh you know done before now uh but I didn't so uh if you don't mind I'm just going to take a couple minutes and deploy this thing real quick um cool uh Ah that's going to be a problem

### Excerpt da transcript

uh okay cool it's 11 o'clock um I think we'll go ahead and get started um sorry before we begin uh I just have one thing I need to do real quick um I've been working on this uh custom controller uh I was kind of hoping to have it uh you know done before now uh but I didn't so uh if you don't mind I'm just going to take a couple minutes and deploy this thing real quick um cool uh Ah that's going to be a problem um yeah live demos right um see if this works cool uh we're good um sorry uh this is a thing I've been working on it's uh supposed to help me out during conferences like this um I called it a uh con job um it's kind of like a crown job but it's for conferences anybody thank you thank you thank you all right um yeah uh all right let's go ahead and get started um uh my name's David uh I am a research scientist at applied Computing research Labs um I'm going to be talking today about uh running large scale scheduling simulations using virtual cuet um so uh let's go ahead and jump in I want to give you a quick overview of what applied Computing is uh so we're a small business doing research and development in distributed systems um I'm particularly interested in scheduling and modeling and optimization uh I've been doing this sort of in industry for the last eight or nine years uh earlier this year I decided you know I kind of uh my background's in Academia um really passionate about open source I kind of want to take the stuff I've been doing uh and not do it for a company but kind of like put it out there into the open um so that's what applied computing's been doing it's been a great journey so far um I'm sure some of you know uh when you're running a small business uh you have to wear a lot of different hats um so uh this is my developer hat uh uh uh today I want to talk to you about a project I've been building for the last few months uh called simcube um this is a project that uh I initially uh started just kind of for myself it was a tool that I thought I was going to need in order to uh get to my real goal around scheduling and uh optimization and these sorts of things um but as I started chatting with more and more folks I'm like oh uh this is something that other people actually care about and are interested in as well uh maybe this can be like a thing on its own um so uh to hopefully motivate this talk a little bit I want to answer the question why simulation uh I want to talk a little bit about what kind of simulation I actually mean because
