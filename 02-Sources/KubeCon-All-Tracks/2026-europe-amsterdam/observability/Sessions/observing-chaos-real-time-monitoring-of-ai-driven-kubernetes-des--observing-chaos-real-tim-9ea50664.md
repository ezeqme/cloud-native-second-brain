---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["AI ML", "Observability", "Kubernetes Core"]
speakers: ["Josh Halley", "Cisco", "Ricardo Aravena", "CNCF"]
sched_url: https://kccnceu2026.sched.com/event/2CW1T/observing-chaos-real-time-monitoring-of-ai-driven-kubernetes-destruction-josh-halley-cisco-ricardo-aravena-cncf
youtube_search_url: https://www.youtube.com/results?search_query=Observing+Chaos%3A+Real-Time+Monitoring+of+AI-Driven+Kubernetes+Destruction+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Observing Chaos: Real-Time Monitoring of AI-Driven Kubernetes Destruction - Josh Halley, Cisco & Ricardo Aravena, CNCF

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Josh Halley, Cisco, Ricardo Aravena, CNCF
- Schedule: https://kccnceu2026.sched.com/event/2CW1T/observing-chaos-real-time-monitoring-of-ai-driven-kubernetes-destruction-josh-halley-cisco-ricardo-aravena-cncf
- Busca YouTube: https://www.youtube.com/results?search_query=Observing+Chaos%3A+Real-Time+Monitoring+of+AI-Driven+Kubernetes+Destruction+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Observing Chaos: Real-Time Monitoring of AI-Driven Kubernetes Destruction.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1T/observing-chaos-real-time-monitoring-of-ai-driven-kubernetes-destruction-josh-halley-cisco-ricardo-aravena-cncf
- YouTube search: https://www.youtube.com/results?search_query=Observing+Chaos%3A+Real-Time+Monitoring+of+AI-Driven+Kubernetes+Destruction+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KOM-PQNpcjk
- YouTube title: Observing Chaos: Real-Time Monitoring of AI-Driven Kubernetes Destr... Josh Halley & Ricardo Aravena
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/observing-chaos-real-time-monitoring-of-ai-driven-kubernetes-destructi/KOM-PQNpcjk.txt
- Transcript chars: 26242
- Keywords: actually, players, player, network, another, basically, trying, running, training, neural, communications, across, having, essentially, looking, ricardo, little, working

### Resumo baseado na transcript

Well, I hope you're having a good time and I hope me and Ricardo won't ruin your time here today. We're hoping that you're not going to can come back and say that was the worst 30 minutes of my life. Our Doom players are are actually it's a model running in a Kubernetes cluster and also being served by PyTorch and the model that that is being used is trained by PyTorch as well. your system and the resilient in your system and additionally we are using a lot of the cloudnative uh technologies one of them is open telemetry uh you probably heard of open telemetry so we primarily ally we're using this for metrics traces and logs Um then for the model training we tried several things and we settled on these three different things uh for impala was best for scaling and distributed uh learning. Uh so there's an MCP server and that MCP server scrapes metrics of that specific player and then we have uh MCP clients which we'll talk about a little bit later that you know are used in what we call um uh a supervisor module

### Excerpt da transcript

Welcome everybody. Who's here for the first time at CubeCon? Oh wow, look at that. Well, I hope you're having a good time and I hope me and Ricardo won't ruin your time here today. We're hoping that you're not going to can come back and say that was the worst 30 minutes of my life. So, Ricardo and myself are presenting on chaos engineering. I'm sure you all saw from the abstract that it's going to be an interesting session. So, buckle up and uh yeah, get ready. So, a little bit about myself. I I've been working with cloud native for the last eight or 10 years. I've been a lead in Tag runtime in a CNCF. I'm currently in the CNCF TOC and I worked in infrastructure for the last 15 years. And my name is Josh Halley. I'm a principal architect at Cisco. Um, my focus is in the CTO office on emergent technologies, up andcoming technologies, nent technologies, things that don't necessarily exist that well yet. Um I am one of the co-organizers of the CNCF technical community group for artificial intelligence um and active in the space with different deliverables and some of the projects.

So all right so let's we could get started with uh defining some of the basic concepts around the the problem we're trying to solve or the the little game that we're playing. So, uh, some of you might be familiar with this, but some of you might not. So, we're using this chaos monkey framework that was originally created at Netflix back in 2011. And yeah, it basically allows you to introduce chaos in your system, in your infrastructure, you know, kill things, uh, introduce delays in your network and and do all kinds of crazy things, right? So we we're also using the PyTorch project to host our players. Our Doom players are are actually it's a model running in a Kubernetes cluster and also being served by PyTorch and the model that that is being used is trained by PyTorch as well. So some example actions that uh you can do with the chaos monkey and just to give you a little bit of context. So you can introduce high CPU usage uh you know issues with GPU memory latency in the network outages you know things happening out of order uh so all these different aspects in in infrastructure so it's really useful for you know for testing your your system and the resilient in your system and additionally we are using a lot of the cloudnative uh technologies one of them is open telemetry uh you probably heard of open telemetry so we primarily ally we're using this for metrics traces and logs an
