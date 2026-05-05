---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Reese Lee", "New Relic"]
sched_url: https://kccnceu2022.sched.com/event/ytqp/why-how-to-and-issues-tail-based-sampling-in-the-opentelemetry-collector-reese-lee-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=Why%2C+How+to%2C+and+Issues%3A+Tail-Based+Sampling+in+the+OpenTelemetry+Collector+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Why, How to, and Issues: Tail-Based Sampling in the OpenTelemetry Collector - Reese Lee, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Reese Lee, New Relic
- Schedule: https://kccnceu2022.sched.com/event/ytqp/why-how-to-and-issues-tail-based-sampling-in-the-opentelemetry-collector-reese-lee-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=Why%2C+How+to%2C+and+Issues%3A+Tail-Based+Sampling+in+the+OpenTelemetry+Collector+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Why, How to, and Issues: Tail-Based Sampling in the OpenTelemetry Collector.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqp/why-how-to-and-issues-tail-based-sampling-in-the-opentelemetry-collector-reese-lee-new-relic
- YouTube search: https://www.youtube.com/results?search_query=Why%2C+How+to%2C+and+Issues%3A+Tail-Based+Sampling+in+the+OpenTelemetry+Collector+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l4PeclHKl7I
- YouTube title: Why, How to, and Issues: Tail-Based Sampling in the OpenTelemetry Collector - Reese Lee, New Relic
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/why-how-to-and-issues-tail-based-sampling-in-the-opentelemetry-collect/l4PeclHKl7I.txt
- Transcript chars: 30087
- Keywords: sampling, traces, trace, collector, sampler, tracing, always, random, sample, getting, decision, generator, processor, policy, distributed, default, sampled, tail-based

### Resumo baseado na transcript

testing it's on all right this is going to be my clicker so that's why i'm holding this mouse all right just a second hola bienvenido a todos um thank you all so much for coming out today i know it's been a long week probably for all of you um and it's a long day and i'm so flattered that you chose to come to my session for your last session of the day so just to make sure we're all in the same room my talk is why error traces which is interesting i've run this demo and had zero of the error traces show up i've had like one air trade show up so it really is randomized as you can see however i want to more efficiently see my error traces

### Excerpt da transcript

testing it's on all right this is going to be my clicker so that's why i'm holding this mouse all right just a second hola bienvenido a todos um thank you all so much for coming out today i know it's been a long week probably for all of you um and it's a long day and i'm so flattered that you chose to come to my session for your last session of the day so just to make sure we're all in the same room my talk is why how to and issues tail-based sampling in the open telemetry collector and yes i'm pretty sure i maxed out the number of letters allowed for a kubecon topic oh no why are you not clicking oh that's weird okay well i'm gonna have to stand here all right to start i'm gonna take you through our agenda for the session i'm going to start with a brief refresher on open telemetry collector and distribute tracing then we'll get into a sampling overview where i'll cover not just what is sampling but also why sampling and then we'll see sampling in action with a live demo by yours truly and we will wrap up with concerns and limitations so that you are aware of the challenges the first question i'm going to answer for you today is who am i my name is rhys lee i am a developer relations engineer on the open telemetry community team at new relic i am based in vancouver washington i am passionate about helping observability end users get and understand useful data from their systems so i'm very pleased to share this presentation with you today okay a first a quick refresher on these core concepts as i'm sure most of you are already familiar with these at this point if you do want more information i'll have some resources at the end that you can check out what is open telemetry in 2019 two competing open source instrumentation projects one called open census and then called open tracing will emerge forming open telemetry it is now the second most active cncf project after kubernetes and it is a unified standard for instrumenting generating collecting and exporting telemetry so metrics logs and traces to help you analyze your softwares performance and behavior and it does so by providing a set of apis sdks and tools including a component called a collector what is the collector it is essentially an extremely configurable system for processing telemetry data it's made of the there's three main components that access that telemetry data receivers processors and exporters and some of the things that a collector can be configured to do include sampling collecting hos
