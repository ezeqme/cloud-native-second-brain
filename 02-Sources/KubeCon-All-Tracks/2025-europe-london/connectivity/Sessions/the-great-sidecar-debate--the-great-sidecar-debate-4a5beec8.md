---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Connectivity"]
speakers: ["William Morgan", "Buoyant"]
sched_url: https://kccnceu2025.sched.com/event/1txAu/the-great-sidecar-debate-william-morgan-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=The+Great+Sidecar+Debate+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Great Sidecar Debate - William Morgan, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Connectivity]]
- País/cidade: United Kingdom / London
- Speakers: William Morgan, Buoyant
- Schedule: https://kccnceu2025.sched.com/event/1txAu/the-great-sidecar-debate-william-morgan-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=The+Great+Sidecar+Debate+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Great Sidecar Debate.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAu/the-great-sidecar-debate-william-morgan-buoyant
- YouTube search: https://www.youtube.com/results?search_query=The+Great+Sidecar+Debate+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lVWUCUt6ZM8
- YouTube title: The Great Sidecar Debate - William Morgan, Buoyant
- Match score: 0.756
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-great-sidecar-debate/lVWUCUt6ZM8.txt
- Transcript chars: 26626
- Keywords: sidecar, application, container, containers, sidecars, ambient, linkerd, applications, mesh, sharing, restart, proxies, network, meshes, traffic, running, shared, called

### Resumo baseado na transcript

Okay, so this talk against my better judgment is called the great sidecar debate. So the real name of this talk which would not have been accepted is why KubeCon attendees need to take the time to understand a bunch of complicated engineering trade-offs instead of blindly jumping onto the new thing. And if you go back to like ancient blog posts from 2015, we've been talking about sidecars like even in the Kubernetes docs for for 10 years. Um, but we never really had like a an object in the in the API or in the Kubernetes spec, you know, that kind of formally was about uh sidecars or formally captured the idea of a sidecar until into 20 until 2023. We got the streaming container is like a another sidecar um that you know takes your logs and send your logs to like a a logging backend. it's it's kind of like independent right we have this we have this rust microproxy uh lets us do all this this fancy stuff we write it in rust we can avoid all the you know all the um kind of security uh bugs that

### Excerpt da transcript

Okay, I think we're ready for action. Welcome everyone. Whatever that previous talk was must have been a a real doozy. Hopefully this one will be uh boring and short. Okay, so this talk against my better judgment is called the great sidecar debate. Now I I didn't want to name it that. So the real name of this talk which would not have been accepted is why KubeCon attendees need to take the time to understand a bunch of complicated engineering trade-offs instead of blindly jumping onto the new thing. So that's what that's really what I'm going to talk about. Um, and hopefully, you know, we can lock the doors and you you're going to be forced to sit through this with me. So, I'm William Morgan. I'm the CEO of a company called Buoyant. We make a a service mesh called Linkerd. Uh, hopefully you're familiar with it by now. It's a graduated project, been graduated for years. Uh, one of the earliest projects ever. Uh, you know, part of the to to to join the CNCF, I think, uh, maybe fourth or fifth project. Um, linkerd has been around for almost uh almost 10 years at this point and uh I have opinions which which I'm going to share with you.

So yeah, get ready. So what's this talk about? You know, this is going to be a talk about sidecars and and I'm going to I'm going to provide some kind of like nonservice mesh, you know, sidecar content so we're all on the same page. It's also going to be a talk about engineering trade-offs and like how to think through some of the stuff. It's not really going to be a talk about right or wrong, old or new or or good or evil because um you know I think in some you know in some cases the answer is clear in some cases the answer is not and and in the vast the reality is in the vast majority of you know kind of engineering decisions the answer is not really that clear. You know the answer is like here are the trade-offs and you have to decide which one makes the most sense for you. Um, so I'll I'll try and present some data, some observations. Um, I'm going to present my opinions and and my conclusions, but I'll try and present it in a way where you can you can draw your own. That sound good? All right.

So, we're going to talk about sidecars. I'm I'm going to tell you what a sidecar is, which is the answer is it's it's just a pattern. And if you go back to like ancient blog posts from 2015, we've been talking about sidecars like even in the Kubernetes docs for for 10 years. Um, but we never really had like a an object in the in th
