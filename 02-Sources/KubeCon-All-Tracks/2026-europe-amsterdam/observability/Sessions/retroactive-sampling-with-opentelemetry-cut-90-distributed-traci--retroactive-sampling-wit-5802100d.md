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
themes: ["Observability"]
speakers: ["Roman Khavronenko", "Zhu Jiekun", "VictoriaMetrics"]
sched_url: https://kccnceu2026.sched.com/event/2CW83/retroactive-sampling-with-opentelemetry-cut-90-distributed-tracing-bandwidth-usage-roman-khavronenko-zhu-jiekun-victoriametrics
youtube_search_url: https://www.youtube.com/results?search_query=Retroactive+Sampling+with+OpenTelemetry%3A+Cut+90%25+Distributed+Tracing+Bandwidth+Usage+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Retroactive Sampling with OpenTelemetry: Cut 90% Distributed Tracing Bandwidth Usage - Roman Khavronenko & Zhu Jiekun, VictoriaMetrics

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Roman Khavronenko, Zhu Jiekun, VictoriaMetrics
- Schedule: https://kccnceu2026.sched.com/event/2CW83/retroactive-sampling-with-opentelemetry-cut-90-distributed-tracing-bandwidth-usage-roman-khavronenko-zhu-jiekun-victoriametrics
- Busca YouTube: https://www.youtube.com/results?search_query=Retroactive+Sampling+with+OpenTelemetry%3A+Cut+90%25+Distributed+Tracing+Bandwidth+Usage+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Retroactive Sampling with OpenTelemetry: Cut 90% Distributed Tracing Bandwidth Usage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW83/retroactive-sampling-with-opentelemetry-cut-90-distributed-tracing-bandwidth-usage-roman-khavronenko-zhu-jiekun-victoriametrics
- YouTube search: https://www.youtube.com/results?search_query=Retroactive+Sampling+with+OpenTelemetry%3A+Cut+90%25+Distributed+Tracing+Bandwidth+Usage+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ehKzt_kGEeM
- YouTube title: Retroactive Sampling with OpenTelemetry: Cut 90% Distributed Traci... Roman Khavronenko & Zhu Jiekun
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/retroactive-sampling-with-opentelemetry-cut-90-distributed-tracing-ban/ehKzt_kGEeM.txt
- Transcript chars: 30857
- Keywords: sampling, trace, decision, trying, retroactive, server, sample, memory, collector, traces, request, attributes, information, everything, second, traffic, buffer, result

### Resumo baseado na transcript

So, in the next 30 minutes, we are going to present retroactive sampling in OpenTelemetry and how this idea can help you to reduce your cost when using distributed tracing. So, we are the company behind open source metrics monitoring solutions also named VictoriaMetrics. Let's go into some basic understanding of what distributed tracing is and why we need it. Nowadays, we run microservice architectures where our service is represented as a bunch of separate processes. And all together, uh it becomes a distributed tracing, a tool that helps us to understand what happened within the distributed system to the user request. This is why tracing becomes one of the most expensive signals to process because like compare resources spent on processing 1 million samples metrics per second with 1 million spans per second.

### Excerpt da transcript

Thanks again for everyone to who joins here. This is the last session of today. So, in the next 30 minutes, we are going to present retroactive sampling in OpenTelemetry and how this idea can help you to reduce your cost when using distributed tracing. Um a little bit about the speakers. My name is Shu-Jie Khun. I am the software engineer working at VictoriaMetrics. And my name is Roman Khvoroenkov. I'm engineer manager at VictoriaMetrics. So, uh we are both from both of us are from VictoriaMetrics. So, we are the company behind open source metrics monitoring solutions also named VictoriaMetrics. And recently, we start to build our logs and traces solutions. And VictoriaMetrics is our trace solution and it's reason why this talk was here. Uh we start to trying to find some pain points from the user side, especially when doing some sampling. And hence this talk. Today's agenda, we are going to start from the beginner's section. Uh what is distributed tracing? How does it cost? And what what's the typical way people use to reduce the cost?

And we'll talk about tail sampling and what's the problem with tail sampling? Why is it expensive? And this helps introduce our idea the retroactive sampling. How does it work? And what components does it need? And we will show you some numbers with the benchmark comparing with other sampling or no sampling solutions. And you know, every solutions comes with with the trade-off. So, we are not going to hide anything from you. Uh we'll talk about the trade-off variants and alternative. And lastly, the summary. Um before we could go into the slide, uh maybe like uh there are a lot of experts here. We don't want to keep you from waiting. So, why not just show you the benchmark result? But with all those comparison objects name masked. So, you can maybe you can make a guess and come back later in the third and fourth session and see if you are uh making a correct guess. So, let's begin. Okay. Um hi. Let's go into some basic understanding of what distributed tracing is and why we need it. So, let's say we're writing a service that should accept user requests, do something with that, and respond with something funny or useful.

Um usually when running monolithic applications, we have all the context when processing this request. We can check them, our permissions, we can look into database, we can do whatever, but we keep it everything within one process, within one unified memory. If something goes funny with this request like
