---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Jonah Kowall", "Paessler"]
sched_url: https://kccnceu2025.sched.com/event/1tcyZ/jaeger-v2-opentelemetry-at-the-core-of-modern-distributed-tracing-jonah-kowall-paessler
youtube_search_url: https://www.youtube.com/results?search_query=Jaeger+V2%3A+OpenTelemetry+at+the+Core+of+Modern+Distributed+Tracing+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Jaeger V2: OpenTelemetry at the Core of Modern Distributed Tracing - Jonah Kowall, Paessler

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Jonah Kowall, Paessler
- Schedule: https://kccnceu2025.sched.com/event/1tcyZ/jaeger-v2-opentelemetry-at-the-core-of-modern-distributed-tracing-jonah-kowall-paessler
- Busca YouTube: https://www.youtube.com/results?search_query=Jaeger+V2%3A+OpenTelemetry+at+the+Core+of+Modern+Distributed+Tracing+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Jaeger V2: OpenTelemetry at the Core of Modern Distributed Tracing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyZ/jaeger-v2-opentelemetry-at-the-core-of-modern-distributed-tracing-jonah-kowall-paessler
- YouTube search: https://www.youtube.com/results?search_query=Jaeger+V2%3A+OpenTelemetry+at+the+Core+of+Modern+Distributed+Tracing+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_3fpZA-DqDU
- YouTube title: Jaeger V2: OpenTelemetry at the Core of Modern Distributed Tracing - Jonah Kowall, Paessler
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/jaeger-v2-opentelemetry-at-the-core-of-modern-distributed-tracing/_3fpZA-DqDU.txt
- Transcript chars: 22140
- Keywords: jerger, actually, metrics, feature, traces, joerger, version, tracing, trace, application, collector, working, search, basically, monitoring, little, pretty, couple

### Resumo baseado na transcript

I'm one of the maintainers of the Jerger project and I'm here to walk you through a little bit about Joerger is. I'm gonna probably go over some things that are familiar to many of you and then I'm going to drill into some of the really exciting stuff that we released just before the last CubeCon in the US which is Jerger version two. So uh distributed tracing is really important because we all build microservices architectures. We have lots of different teams and everyone is pointing at each other when there's a problem. So the issue that we try to solve with tracing is you could say whose fault is it but where did it break? And tracing gives you that unique ability to answer those questions and to get really deep into what's happening in your code.

### Excerpt da transcript

Uh, my name is Jonah Cowell. I'm one of the maintainers of the Jerger project and I'm here to walk you through a little bit about Joerger is. How many of you don't know what Joerger is? All right, that's pretty good. So, I guess maybe I Well, there's a couple people. I'm gonna probably go over some things that are familiar to many of you and then I'm going to drill into some of the really exciting stuff that we released just before the last CubeCon in the US which is Jerger version two. It's a very big multi-year effort. Then I'm going to talk about the reason why we did it, the benefit to all of you and uh and then I'm going to talk about some of the other things that we're working on and the road map and kind of where the project's going. So with that, uh, my name is Jonah. My day job is that I run product and design at a company called Passler. We do infrastructure monitoring. You may have heard of PRTG. That's our product. And then my not day job, I work on Open Search. I'm part of the technical steering committee.

And I'm also a maintainer of Jerger. So that's my volunteer job. And when I'm not working, that's where I'd rather be underwater. I spend a lot of time diving. I live in South Florida and dive all over the world. So that's what I like doing. That's my passion. Uh these are pictures from the last year, but I'm always taking new pictures and stuff. So um so let's talk a little bit about why we all need and love distributed tracing. I'm going to get into a couple of different demos and I'm going to show you what Jäger does in the basic demo and then we're going to dig into what it does with monitoring capabilities. So deriving metrics from traces and then uh we'll dig into Jerger V2 the architecture some of the changes and kind of why we did it. Uh so and then we'll have time for questions. I don't really have a clock but I'll keep an eye. So uh distributed tracing is really important because we all build microservices architectures. We have lots of different teams and everyone is pointing at each other when there's a problem.

So the issue that we try to solve with tracing is you could say whose fault is it but where did it break? Why did it break? And most importantly, who can fix it? So that our customer is back up and running. And tracing gives you that unique ability to answer those questions and to get really deep into what's happening in your code. So that's why it's important. We can also do other cool things like build dependency maps
