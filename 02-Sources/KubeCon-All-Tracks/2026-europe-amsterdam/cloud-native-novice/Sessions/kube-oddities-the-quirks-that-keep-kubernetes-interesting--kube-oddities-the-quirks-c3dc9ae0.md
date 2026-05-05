---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["Kubernetes Core"]
speakers: ["Marcus Noble", "Monzo", "Márk Sági-Kazár", "Independent"]
sched_url: https://kccnceu2026.sched.com/event/2CW2p/kube-oddities-the-quirks-that-keep-kubernetes-interesting-marcus-noble-monzo-mark-sagi-kazar-independent
youtube_search_url: https://www.youtube.com/results?search_query=Kube-Oddities+-+The+Quirks+That+Keep+Kubernetes+Interesting+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Kube-Oddities - The Quirks That Keep Kubernetes Interesting - Marcus Noble, Monzo & Márk Sági-Kazár, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marcus Noble, Monzo, Márk Sági-Kazár, Independent
- Schedule: https://kccnceu2026.sched.com/event/2CW2p/kube-oddities-the-quirks-that-keep-kubernetes-interesting-marcus-noble-monzo-mark-sagi-kazar-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Kube-Oddities+-+The+Quirks+That+Keep+Kubernetes+Interesting+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Kube-Oddities - The Quirks That Keep Kubernetes Interesting.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2p/kube-oddities-the-quirks-that-keep-kubernetes-interesting-marcus-noble-monzo-mark-sagi-kazar-independent
- YouTube search: https://www.youtube.com/results?search_query=Kube-Oddities+-+The+Quirks+That+Keep+Kubernetes+Interesting+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ybxDYZ-9wHE
- YouTube title: Kube-Oddities - The Quirks That Keep Kubernetes Interesting - Marcus Noble & Márk Sági-Kazár
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/kube-oddities-the-quirks-that-keep-kubernetes-interesting/ybxDYZ-9wHE.txt
- Transcript chars: 21037
- Keywords: create, cluster, cuddle, containers, container, actually, default, cannot, called, arbback, little, cublet, control, policies, within, always, sidecar, running

### Resumo baseado na transcript

Um I'm also a CNCF ambassador and I run a monthly newsletter called cloudnative.now where I do like a roundup of everything happening in the cloudnative ecosystem within the past month um with KubeCon. Um, and I've now got about I think it's about seven years worth of experience in like the cloud native space over a bunch of different roles, different personas that I've that I've had over my career. And uh last year, I think it was last year in Munich, >> yep, >> where we got talking about our PTSD or the weird things in Kubernetes that you know the things that you always have to look up, the things that you always get wrong for the first time and you have to then fix it. But hopefully whether you are a um inexperienced Kubernetes operator or expert or whether you just ran your first uh cube cuttle command this morning. Like, if you touch Kubernetes, I'm pretty sure you come across pods at some point. are kind of essential in Kubernetes I'd say um but they do have some of their quirks.

### Excerpt da transcript

Good morning everybody. Uh thank you for coming today. We are going to talk to you today about uh cube oddities. Um for those of you that don't know me. I'm that chap at at the top. My name is Marcus Noble. I am a platform engineer at Monzo. Um I'm also a CNCF ambassador and I run a monthly newsletter called cloudnative.now where I do like a roundup of everything happening in the cloudnative ecosystem within the past month um with KubeCon. This month's going to be a fairly busy one for me I think. So, look out for that if you're interested. Um, and I've now got about I think it's about seven years worth of experience in like the cloud native space over a bunch of different roles, different personas that I've that I've had over my career. So, um, come across some some very interesting oddities within Kubernetes over that time. I'll pass over to my dear friend Mark. >> Yeah, my name is Mark Shagi Kazar. I'm well, don't try to pronounce it. I'm from Hungary. I'm also a CNCF ambassador and I've been doing uh lot of community organizing and open source projects.

Uh I'm also an organizer of KCD Budapest uh which is going to happen this year again. So if you want to attend or submit any talks, please do. And yeah, my last latest project is uh an online course called Kubernetes the very hard way. So if you want to learn the inner workings of Kubernetes, check it out. So before we get to the good stuff, uh why are we the ones delivering this talk? And uh last year, I think it was last year in Munich, >> yep, >> where we got talking about our PTSD or the weird things in Kubernetes that you know the things that you always have to look up, the things that you always get wrong for the first time and you have to then fix it. Uh and we thought we we we managed to gather quite a few things. So we thought we would share these things with you and maybe you can uh share your experience after the talk. But hopefully whether you are a um inexperienced Kubernetes operator or expert or whether you just ran your first uh cube cuttle command this morning. Hopefully we can we can uh share something new with you.

>> Just just want to quickly check with you Mark. It's pronounced uh coup control, right? Is that is that correct? >> No, I don't think so. I mean uh if anything, it's cube city, right? >> No, I'm pretty sure it's it's cube cuddle, right? Cube cuddle. >> Anybody? >> What do you think? Cube cuddle. >> Ah, we'll win you over. We'll win you I'll win you over. Right. Okay. Ri
