---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Brandon Smith", "Howard Hao", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HyaA/making-legacy-modern-how-to-monitor-and-fine-tune-the-performance-of-your-windows-clusters-brandon-smith-howard-hao-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Making+Legacy+Modern%3A+How+to+Monitor+and+Fine+Tune+the+Performance+of+Your+Windows+Clusters+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Making Legacy Modern: How to Monitor and Fine Tune the Performance of Your Windows Clusters - Brandon Smith & Howard Hao, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Brandon Smith, Howard Hao, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HyaA/making-legacy-modern-how-to-monitor-and-fine-tune-the-performance-of-your-windows-clusters-brandon-smith-howard-hao-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Making+Legacy+Modern%3A+How+to+Monitor+and+Fine+Tune+the+Performance+of+Your+Windows+Clusters+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Making Legacy Modern: How to Monitor and Fine Tune the Performance of Your Windows Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyaA/making-legacy-modern-how-to-monitor-and-fine-tune-the-performance-of-your-windows-clusters-brandon-smith-howard-hao-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Making+Legacy+Modern%3A+How+to+Monitor+and+Fine+Tune+the+Performance+of+Your+Windows+Clusters+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l5yWjocVOmY
- YouTube title: Making Legacy Modern: How to Monitor and Fine Tune the Performance of...- Brandon Smith & Howard Hao
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/making-legacy-modern-how-to-monitor-and-fine-tune-the-performance-of-y/l5yWjocVOmY.txt
- Transcript chars: 29944
- Keywords: windows, container, application, running, server, performance, containers, actually, technology, issues, deploy, working, traces, modern, pretty, effectively, execute, looking

### Resumo baseado na transcript

okay welcome everyone um it's great to be here with all of you this week um it's pretty exciting to see where this technology has come what we're here to do today is to talk to you about how to make the most of it while also showing off some of the recent advancements that we've made and what we've got cooking for the future so let's get started so my name is Brandon I'm a product manager at Microsoft working on the Windows container core technology there's a good be able to scale things as more manually especially with um you know hyper-v and VMware and then eventually we're in the space we're in now where applications are at the highest layer of abstraction and the focus is becoming more on the application itself

### Excerpt da transcript

okay welcome everyone um it's great to be here with all of you this week um it's pretty exciting to see where this technology has come what we're here to do today is to talk to you about how to make the most of it while also showing off some of the recent advancements that we've made and what we've got cooking for the future so let's get started so my name is Brandon I'm a product manager at Microsoft working on the Windows container core technology there's a good chance you've seen me in some of the Sig Windows meetings or GitHub issues or bugs or wherever else and so I've been around a lot in the windows kubernetes Community right now my primary focus is working on the advancement of performance within Windows containers and windows containers on kubernetes and here we've got Howard who is one of our chief perform performance analysts yeah my name is Howard Howe and I've been working with the windows container since day one my passion is like to look into the tough customer issues and working with them closely to understand the performance issues reliability issues and glad to be here and thank you guys for joining us but we're really here is representatives of the amazing group of people both at Microsoft and across the windows containers in kubernetes community who are building and innovating with this technology we've got a pretty massive effort running around this product and it's with the primary purpose of empowering you to more effectively scale your business and I know that's that's the common Microsoft tagline but it's true what inspires us to do what we do every day are the amazing stories that we hear of what people can do with the technology that we create so today we'll focus on some of the most common stories and struggles we see when it comes to container performance and how you can mitigate them and more effectively scale your business so we'll kind of go into some of the the background of why that is and then we'll go into some history and then do a demo and troubleshooting of how to solve performance with your containers so let's enter a hypothetical scenario where I'm one of the many many customers who are looking to bring their legacy applications into the modern era of infrastructure most often the generalized need can be summarized as I have a legacy application and I need to find a way to bring it into the modern cloud while reducing costs all without requiring a massive rewrite of a technology that may have poor documentation or c
