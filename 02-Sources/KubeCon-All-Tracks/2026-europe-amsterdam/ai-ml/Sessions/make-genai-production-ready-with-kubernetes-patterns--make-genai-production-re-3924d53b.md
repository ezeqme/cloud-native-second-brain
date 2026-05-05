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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Roland Huss", "Red Hat", "Bilgin Ibryam", "Diagrid"]
sched_url: https://kccnceu2026.sched.com/event/2CVyl/make-genai-production-ready-with-kubernetes-patterns-roland-huss-red-hat-bilgin-ibryam-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Make+GenAI+Production-Ready+With+Kubernetes+Patterns+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Make GenAI Production-Ready With Kubernetes Patterns - Roland Huss, Red Hat & Bilgin Ibryam, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Roland Huss, Red Hat, Bilgin Ibryam, Diagrid
- Schedule: https://kccnceu2026.sched.com/event/2CVyl/make-genai-production-ready-with-kubernetes-patterns-roland-huss-red-hat-bilgin-ibryam-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Make+GenAI+Production-Ready+With+Kubernetes+Patterns+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Make GenAI Production-Ready With Kubernetes Patterns.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyl/make-genai-production-ready-with-kubernetes-patterns-roland-huss-red-hat-bilgin-ibryam-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Make+GenAI+Production-Ready+With+Kubernetes+Patterns+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tLK5jyhQOgA
- YouTube title: Make GenAI Production-Ready With Kubernetes Patterns - Roland Huss, Red Hat & Bilgin Ibryam, Diagrid
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/make-genai-production-ready-with-kubernetes-patterns/tLK5jyhQOgA.txt
- Transcript chars: 26377
- Keywords: patterns, pattern, request, actually, container, volume, course, running, already, routing, application, specific, typically, workload, gpu, within, minutes, controller

### Resumo baseado na transcript

So welcome everybody to this session about how Kubernetes patterns meet geni. working since for Reddit since 10 years nowadays and uh yeah and also on the field of AI and actually we have written also some books together with Bill but also with with Danielle so we come tell a little bit more about that. Uh right um so this will be a bit of high level but um probably most of you here are either running uh lms on Kubernetes or actually interested in doing that. So before we dive into that we want to start with the traditional Kubernetes pattern. So here I have a typical web application that you would run on Kubernetes. Uh maybe you're running a posgress on Kubernetes with multiple replica.

### Excerpt da transcript

So welcome everybody to this session about how Kubernetes patterns meet geni. Um yeah first of all let us introduce ourself for a second. You >> go first. >> Yeah but my name is Rulen Hus. I'm a software architect distinguished engineer working for Redhead. working since for Reddit since 10 years nowadays and uh yeah and also on the field of AI and actually we have written also some books together with Bill but also with with Danielle so we come tell a little bit more about that. Um yeah Pat >> yeah hello everybody my name is Bill Gin Ibraham I am principal product manager at DIG grid where we are the primary maintainers of the Dapper project so that spells DAPR it's one of the CNCF graduated projects that lets you create uh durable resilient agents yeah okay so so back to this two books so the both books are available nowadays so you see the QR codes already so they are also available for free for download so if you if you like and the talk here is about really about a a blend of both books actually.

So actually we actually we've just finished. So when I say we in this case Danielle and and I so maybe we can see the the next ones I think this this meme clarified a little bit. So actually we could stay here uh with three persons. So Danielle as well but okay we we created this book on how to run generative AI on Kubernetes and but also have this previous book about patterns which describes a set of repeatable solutions for common problems and we thought about it's a good idea to present how you can apply those common patterns to the field of genai um and this is what we are trying to do in this 30 minutes um I said you can of course buy this this new book on generative AI on Kubernetes is but you can also download it for for free. But before we we start and go into details about generative a quick recap what we mean with patterns what they are and um how they are used these days. Uh right um so this will be a bit of high level but um probably most of you here are either running uh lms on Kubernetes or actually interested in doing that.

So before we dive into that we want to start with the traditional Kubernetes pattern. So here I have a typical web application that you would run on Kubernetes. Probably many of you have run this. Um it has a bunch of patterns. If we if we zoom in for example you see the controller pattern. Uh the job of the controller pattern is to look at the desired state which is your deployment manifest and makes that uh happen. In th
