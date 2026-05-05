---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Aidan Delaney", "Bloomberg"]
sched_url: https://kccnceu2026.sched.com/event/2EF5w/buildpacks-towards-10-ai-and-other-things-aidan-delaney-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Buildpacks%3A+Towards+1.0%2C+AI+and+Other+Things+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Buildpacks: Towards 1.0, AI and Other Things - Aidan Delaney, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Aidan Delaney, Bloomberg
- Schedule: https://kccnceu2026.sched.com/event/2EF5w/buildpacks-towards-10-ai-and-other-things-aidan-delaney-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Buildpacks%3A+Towards+1.0%2C+AI+and+Other+Things+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Buildpacks: Towards 1.0, AI and Other Things.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5w/buildpacks-towards-10-ai-and-other-things-aidan-delaney-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Buildpacks%3A+Towards+1.0%2C+AI+and+Other+Things+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Gc4NZlv7F5A
- YouTube title: Buildpacks: Towards 1.0, AI and Other Things - Aidan Delaney, Bloomberg
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/buildpacks-towards-1-0-ai-and-other-things/Gc4NZlv7F5A.txt
- Transcript chars: 27844
- Keywords: builder, application, support, images, python, platform, custom, source, production, perspective, called, particularly, actually, native, developer, provide, stacks, questions

### Resumo baseado na transcript

Um I do tend to walk around so I don't know if this is a good thing or a bad thing but um why listen to me? Um Joe over there is also a build pack maintainer and there's a couple of others around and we're always happy to talk build packs with folks. Um, and what I'm really going to show you is that from a a build packs perspective, it does not matter if you're building a fast API application or if you're building a machine learning training uh model. In fact, I'll do a live demo as quickly as I can because people don't believe it unless you actually show them, do they? And I'll yeah demo with a Java application with a custom builder which allows me to introduce a bunch of build packs topics. If you've got Java Spring applications like the one that I'll demo today, if you do spring boot colon build image with Maven, it will build an image and under the hood it uses build packs.

### Excerpt da transcript

Welcome to the 2026 uh build packs uh maintainer track talk. Um I'm Aiden and they gave me a clicky thing. Look at that. It's brilliant. Um I do tend to walk around so I don't know if this is a good thing or a bad thing but um why listen to me? Uh I am one of the build packs maintainers. Um Joe over there is also a build pack maintainer and there's a couple of others around and we're always happy to talk build packs with folks. Um suppose I I had an academic background and then I have 20 years of industry experience which just tells you that I'm old and maybe you should listen to old people. Um uh and most of my work in the Bilpex project has been in helping and creating the documentation and we were lucky enough last year to receive the CNCF Laura Mipum award for that work which was fantastic and thank you to the CNCF for that. Um, I'm also going to put a plug in for my employers who are Bloomberg um, who give me time to work on this. Um, and particularly in Dublin, we're hiring right now. We're hiring globally, but I put up two QR codes.

Uh, the left one is to uh, early career hires. So, I know at the moment the job market is tough, particularly for early career folks. Have a look at it. And then the other one is just for general uh, positions, particularly in Dublin, uh, which is where I work, but we're we're hiring worldwide. London, New York, San Francisco, Frankfurt. And in this talk, I want to talk a little bit about two two kind of threads. The kind of road to 1.0. Uh where are we going? Uh what do we want to achieve out of a 1.0 version of the spec and then you have to have AI in your talk title these days. So, uh going to talk about AI and machine learning a little bit. Um, and what I'm really going to show you is that from a a build packs perspective, it does not matter if you're building a fast API application or if you're building a machine learning training uh model. It it's the same process. So there's nothing scary from a build packs perspective uh when we try and do AI. Um, so along the way here, we're going to do a live demo.

In fact, I'll do a live demo as quickly as I can because people don't believe it unless you actually show them, do they? Um, and I'm going to use a Java application. I know this is heresy at CubeCon, but I'm going to use a Java application because a lot of us may be infrastructure engineers, but we end up supporting Python or Java application developers um because they are very very popular programming languages. A
