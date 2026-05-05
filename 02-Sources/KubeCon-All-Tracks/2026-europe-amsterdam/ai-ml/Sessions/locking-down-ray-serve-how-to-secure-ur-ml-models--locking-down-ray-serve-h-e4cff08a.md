---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Security"]
speakers: ["Kateryna Hrytsaienko", "Valtech"]
sched_url: https://kccnceu2026.sched.com/event/2CVyE/locking-down-ray-serve-how-to-secure-ur-ml-models-kateryna-hrytsaienko-valtech
youtube_search_url: https://www.youtube.com/results?search_query=Locking+Down+Ray+Serve%3A+How+to+Secure+Ur+ML+Models%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Locking Down Ray Serve: How to Secure Ur ML Models? - Kateryna Hrytsaienko, Valtech

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kateryna Hrytsaienko, Valtech
- Schedule: https://kccnceu2026.sched.com/event/2CVyE/locking-down-ray-serve-how-to-secure-ur-ml-models-kateryna-hrytsaienko-valtech
- Busca YouTube: https://www.youtube.com/results?search_query=Locking+Down+Ray+Serve%3A+How+to+Secure+Ur+ML+Models%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Locking Down Ray Serve: How to Secure Ur ML Models?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyE/locking-down-ray-serve-how-to-secure-ur-ml-models-kateryna-hrytsaienko-valtech
- YouTube search: https://www.youtube.com/results?search_query=Locking+Down+Ray+Serve%3A+How+to+Secure+Ur+ML+Models%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FLTKUAcuFyc
- YouTube title: Locking Down Ray Serve: How to Secure Ur ML Models? - Kateryna Hrytsaienko, Valtech
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/locking-down-ray-serve-how-to-secure-ur-ml-models/FLTKUAcuFyc.txt
- Transcript chars: 25180
- Keywords: actually, cluster, security, course, within, probably, already, resources, basically, another, virtual, access, additional, mesh, everyone, everything, source, workers

### Resumo baseado na transcript

So actually hey everyone it's such an honor today to stand in front of you. Thank you very much for joining in and for sharing the passion for the security and locking up your ray models. So actually also ray translate the needs of your model to the kubernetes via kubray with the three custom resources. So that's the part where you can submit something inside of your rake cluster for training for example and after the completion resources will be cleaned up and actually ray jobs is something that concerns from the security perspective quite a lot. So we're going to talk about it as well and here if you also dig into how ray cluster works under the hood you will find out that it's quite similar to the kubernetes as well. And it means that by default there is no security mechanism enabled within the cluster.

### Excerpt da transcript

So actually hey everyone it's such an honor today to stand in front of you. Thank you very much for joining in and for sharing the passion for the security and locking up your ray models. So basically this topics is something that you usually learn in hard way and that was the case for me that's why we are here today. So you wouldn't need to spend so much time on research and upgrades and everything. I will show you it today all. So before we start actually nice to meet you for those who don't know me my name is Katina I actually do quite lately a lot of envelopes with a security flavor in it and that's why I spend quite share of time making envelopes more accessible to everyone preparing the workshops to create your first envelop pipeline and etc. So today we're going to dig in into how actually make your way secure and I will in the end also share with you the runbook where you can use all the examples that I showed today. So please don't be worried that you will miss anything and let's dig.

So first of all I want to know about you. So please raise your hand if you heard about Ray or use it. Wow mean like there is the fans finally. I mean like I will still talk about it but that's fine. And who does envelopes for fun for work? Okay. Amazing. Amazing. I see those row. It's my favorite so far. Um, okay. That's awesome. So, just quickly because I wouldn't bug myself to not talk about Ray at all. Ray is awesome. You all know that it's open source. It's allows us to dig from our shoulders the issue of distributed computing and allows us to manage low-level processes with a high level APIs. That sounds already amazing. So actually also ray translate the needs of your model to the kubernetes via kubray with the three custom resources. That's also awesome and also nice but we already probably all know that just for making sure that everyone on the same page ray cluster is a huge box where all shenan is happening. Ray service is where actually have ray cluster combined with your model and in the end it's ray job.

That's my favorite one. So that's the part where you can submit something inside of your rake cluster for training for example and after the completion resources will be cleaned up and actually ray jobs is something that concerns from the security perspective quite a lot. So we're going to talk about it as well and here if you also dig into how ray cluster works under the hood you will find out that it's quite similar to the kubernetes as well. So in o
