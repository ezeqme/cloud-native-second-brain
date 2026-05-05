---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Novice"
themes: ["Cloud Native Novice"]
speakers: ["Ivan Porta", "Phil Henderson", "Buoyant"]
sched_url: https://kccncna2025.sched.com/event/27FVq/dont-panic-a-beginners-guide-to-k8s-debugging-ivan-porta-phil-henderson-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Don%27t+Panic%21+A+Beginner%27s+Guide+To+K8s+Debugging+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Don't Panic! A Beginner's Guide To K8s Debugging - Ivan Porta & Phil Henderson, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Cloud Native Novice]]
- País/cidade: United States / Atlanta
- Speakers: Ivan Porta, Phil Henderson, Buoyant
- Schedule: https://kccncna2025.sched.com/event/27FVq/dont-panic-a-beginners-guide-to-k8s-debugging-ivan-porta-phil-henderson-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Don%27t+Panic%21+A+Beginner%27s+Guide+To+K8s+Debugging+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Don't Panic! A Beginner's Guide To K8s Debugging.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVq/dont-panic-a-beginners-guide-to-k8s-debugging-ivan-porta-phil-henderson-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Don%27t+Panic%21+A+Beginner%27s+Guide+To+K8s+Debugging+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2fRRYcugOh4
- YouTube title: Don't Panic! A Beginner's Guide To K8s Debugging - Ivan Porta & Phil Henderson, Buoyant
- Match score: 0.806
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dont-panic-a-beginners-guide-to-k8s-debugging/2fRRYcugOh4.txt
- Transcript chars: 31253
- Keywords: control, application, matrix, actually, having, graphana, linker, metrics, cluster, everything, dashboards, platform, working, little, questions, talking, troubleshooting, mesh

### Resumo baseado na transcript

Today, we're going to be talking about don't panic, a beginner's guide to troubleshooting Kubernetes. Um, I need everyone to kind of like knock on wood and hope my demo goes well. So as you can imagine there is a lot of reinventing the wheel like micros like because we have multiple teams like implementing matrix then we have to do the same thing across multiple microservices and the problem is sooner or later something will go wrong. So you have multiple microservices failing and you don't know why you don't know which one is the corpit and you find yourself having to troubleshoot checking the matrix checking the logs of them to try to find the corpit as soon as possible. The problem though is we're talking just on one cluster now and Kubernetes is evolving. As you can see, it's not just about loss in revenue, but there are a lot of like in indirect costs about downtime.

### Excerpt da transcript

Good afternoon. How's everyone doing today? Good. There's a lot more people in here than I thought I would. How many people would actually consider themselves a beginner here? Raise your hand. Oh, awesome. Good. So, I think you're all going to like this talk. My name is Phil Henderson. This is my friend and colleague Ivan Pora. Today, we're going to be talking about don't panic, a beginner's guide to troubleshooting Kubernetes. Um, and without further ado, Ivan's going to start on the slides. Um, I need everyone to kind of like knock on wood and hope my demo goes well. Otherwise, we're gonna be really troubleshooting Kubernetes. I'm just hoping I'm not troubleshooting my Mac or the wonderful Wi-Fi brought to you by uh Render ATL as it says on their Wi-Fi thing. So, uh without further ado, Ivan, go ahead and uh start talking about how to begin. >> Okay, so this is just an example of what a microser application looks like. We have multiple microservices. They can be written in different programming languages like Ras, Go, Node.js, JS and they're talking to each other and potentially even to data the database S3 and more.

They can also be maintained by different teams in the same organization. So you have team A, B, C, D taking care of different microservices. Each one implementing their matrix tracing circuit breaking timeouts and more. >> How many of y'all are platform engineers here developers? How many of you are writing different languages without your organization or you have one? Okay. So what I was describing here is you know relevant to some of you. So as you can imagine there is a lot of reinventing the wheel like micros like because we have multiple teams like implementing matrix then we have to do the same thing across multiple microservices and the problem is sooner or later something will go wrong. one one micros service down the line will eventually fail and that if not handled properly using circle breaking timeouts might actually create like a cascading failures. So you have multiple microservices failing and you don't know why you don't know which one is the corpit and you find yourself having to troubleshoot checking the matrix checking the logs of them to try to find the corpit as soon as possible.

The problem though is we're talking just on one cluster now and Kubernetes is evolving. More and more organizations are using multicluster architectures. So we are not just talking about troubleshooting one cluster. We are talking about troubl
