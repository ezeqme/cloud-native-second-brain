---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Kusha Maharshi", "Bloomberg"]
sched_url: https://kccncna2025.sched.com/event/27Faj/building-scalable-end-to-end-latency-metrics-from-distributed-trace-kusha-maharshi-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Building+Scalable+End-to-end+Latency+Metrics+From+Distributed+Trace+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building Scalable End-to-end Latency Metrics From Distributed Trace - Kusha Maharshi, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Kusha Maharshi, Bloomberg
- Schedule: https://kccncna2025.sched.com/event/27Faj/building-scalable-end-to-end-latency-metrics-from-distributed-trace-kusha-maharshi-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Scalable+End-to-end+Latency+Metrics+From+Distributed+Trace+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building Scalable End-to-end Latency Metrics From Distributed Trace.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Faj/building-scalable-end-to-end-latency-metrics-from-distributed-trace-kusha-maharshi-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Building+Scalable+End-to-end+Latency+Metrics+From+Distributed+Trace+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6xxqm9LIhoU
- YouTube title: Building Scalable End-to-end Latency Metrics From Distributed Trace - Kusha Maharshi, Bloomberg
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-scalable-end-to-end-latency-metrics-from-distributed-trace/6xxqm9LIhoU.txt
- Transcript chars: 26453
- Keywords: trace, latency, metrics, dagger, systems, traces, distributed, publish, consume, approach, together, essentially, messages, partition, requests, actually, workflow, across

### Resumo baseado na transcript

I hope you all are on your second set of coffees and that it wouldn't be too boring and we'll make this fun. But with that said, I am Kosha Mahersi and I am a senior software engineer at Bloomberg. And as a result of that, we saw a recurring request pop up which was that teams and engineers wanted latency metrics for end toend workflows. that case engineers want to know well how long does it take for requests to go from A to C and that's your end to end workflow so previously what would happen is either teams would use some amalgamation of like servicewide metrics So your application level metrics or they would have some custom end-to-end uh tracking system. But then obviously with the increasing adoption of if you didn't already guess it distributed tracing we decided to adopt that as the unified centralized solution for doing this.

### Excerpt da transcript

Okay. Hello everyone. Good afternoon. I hope you all are on your second set of coffees and that it wouldn't be too boring and we'll make this fun. I know it's 3 p.m. But with that said, I am Kosha Mahersi and I am a senior software engineer at Bloomberg. Today I'll be talking about how we used distributed trace to generate end-to-end latency metrics at scale. And before I really get into the nitty-gritty of it all, I want to kick us off with a little story time. So I work on the telemetry infrastructure team, which means that our job is to provide observability and monitoring solutions to the rest of the firm through telemetry data. And that means that our clients are other engineering teams. So these teams are building and maintaining trading systems and messaging systems, news infrastructure, middleware, so on and so forth. And with all of these products, they must handle large volumes of super high stakes data with very low latency. And especially in the financial sphere, um just even milliseconds of delay or latency can equate millions of dollars lost.

And that is why engineers must make sure that they prevent latency from creeping in to these systems. And so they have to monitor the complex distributed systems that actually back the userfacing products. And as a result of that, we saw a recurring request pop up which was that teams and engineers wanted latency metrics for end toend workflows. So for example like let's say we have something super simple like this where you've got your users making some requests that hit service A service A talks to service B which talks to service C and then some users receive a response right in that case engineers want to know well how long does it take for requests to go from A to C and that's your end to end workflow so previously what would happen is either teams would use some amalgamation of like servicewide metrics So your application level metrics or they would have some custom end-to-end uh tracking system. So like maybe think passing around a session ID or a request ID some sort of state management that can let you kind of put together requests across different services.

But then obviously with the increasing adoption of if you didn't already guess it distributed tracing we decided to adopt that as the unified centralized solution for doing this. And very quickly as our team decided to build this out we realized that I will actually take a quick pause to do a quick interlude for what is distributed tracing
