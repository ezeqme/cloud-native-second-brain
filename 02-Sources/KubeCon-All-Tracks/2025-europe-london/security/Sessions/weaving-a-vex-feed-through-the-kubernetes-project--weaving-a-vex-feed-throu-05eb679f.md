---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Adolfo García Veytia", "Stacklok"]
sched_url: https://kccnceu2025.sched.com/event/1tx8d/weaving-a-vex-feed-through-the-kubernetes-project-adolfo-garcia-veytia-stacklok
youtube_search_url: https://www.youtube.com/results?search_query=Weaving+a+VEX+Feed+Through+the+Kubernetes+Project+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Weaving a VEX Feed Through the Kubernetes Project - Adolfo García Veytia, Stacklok

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Adolfo García Veytia, Stacklok
- Schedule: https://kccnceu2025.sched.com/event/1tx8d/weaving-a-vex-feed-through-the-kubernetes-project-adolfo-garcia-veytia-stacklok
- Busca YouTube: https://www.youtube.com/results?search_query=Weaving+a+VEX+Feed+Through+the+Kubernetes+Project+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Weaving a VEX Feed Through the Kubernetes Project.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8d/weaving-a-vex-feed-through-the-kubernetes-project-adolfo-garcia-veytia-stacklok
- YouTube search: https://www.youtube.com/results?search_query=Weaving+a+VEX+Feed+Through+the+Kubernetes+Project+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oCbJdcy3zzA
- YouTube title: Weaving a VEX Feed Through the Kubernetes Project - Adolfo García Veytia, Stacklok
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/weaving-a-vex-feed-through-the-kubernetes-project/oCbJdcy3zzA.txt
- Transcript chars: 21628
- Keywords: vulnerability, vulnerabilities, information, security, release, little, scanners, statement, software, generate, container, vexflow, dependencies, document, statements, affected, advisory, publish

### Resumo baseado na transcript

Thanks, uh, for coming to such a niche topic on the very last slot of the day. Um, hopefully um, you'll get something some good takeaways from the talk. So when you have a container image, you will usually point uh your security scanners at the image and over time you start seeing that CVS uh start showing up. Scanners will look find those dependencies compare them against security databases and give you a report on whether those apply those are found in your in your components. Um because VEX was defined by a community group uh hosted under CISA the cyber infrastructure security agency in the US. Um and then so there's a big flavor in CESAF the um the common security advisory framework.

### Excerpt da transcript

All right. Um, welcome everyone. Thanks, uh, for coming to such a niche topic on the very last slot of the day. Um, hopefully um, you'll get something some good takeaways from the talk. Um, so this talk is about how we're trying to build the and compose the VEX Kubernetes feed uh, to talk about so that we can communicate the vulnerability impact to our end users. Uh my name is Adulo Garcia or PCOM. That's my usual pig. If you see that on the internet, it's me. Um so I am a software engineer in a super new startup called Carabiner Systems. But more importantly for this talk, I am uh one of the uh tech leads on Kubernetes release with the release engineering team and I am also one of the uh technical leads in the open vec on the open source security foundation which is a sister of the CDNCF. Uh so you can think of me being here on this stage wearing those two hats uh for the day. Um so here's a quick rundown of what we'll well I'll try to touch on today because it's a lot to pack into half an hour. Uh so I'll do like a super quick intro on what VEX is.

Um we're uh also going to show how we're thinking uh on vexing the Kubernetes project and the challenges of doing that for such a large uh project and organization and finally show you a couple of new tools that we're working on uh to to make this a reality and it hopefully if the internet works because it it was failing very bad a couple half an hour ago. Uh I'll we'll get to the demo. So first up u vex. Um so what is vex? Uh if you had to define vex um you can think of vex as a system of documents that get chronologically ordered uh that communicate the impact that a vulnerability has on a piece of software. Uh in other words if there's a CVE does it affect me or not? And that's a channel of communication uh between you and your users and downstream tools and other processes that um enable you to uh make assessments on the on the exploitation capability like the exploitation possibility of that uh vulnerability. Um so to u go a little bit more into detail let's assume that you have a container image uh in in VEX slang this is called the product.

So when you have a container image, you will usually point uh your security scanners at the image and over time you start seeing that CVS uh start showing up. This is normal and completely expected uh and most of the time uh is because the your container image has dependencies and new vulnerabilities get reported uh on on those projects every time. Um so most of th
