---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability", "Cost Optimization"]
speakers: ["Raphaël Bizos"]
source_url: https://promcon.io/2025-munich/talks/a-history-of-automatic-aggregations/
youtube_url: https://www.youtube.com/watch?v=iy_PmgRTLqQ
youtube_search_url: https://www.youtube.com/results?search_query=A+History+of+Automatic+Aggregations+PromCon+2025
video_match_score: 0.973
status: video-found
---

# A History of Automatic Aggregations

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: Raphaël Bizos
- Página oficial: https://promcon.io/2025-munich/talks/a-history-of-automatic-aggregations/
- YouTube: https://www.youtube.com/watch?v=iy_PmgRTLqQ

## Resumo

At Criteo, we’ve relied on automatic aggregations for years. “Automatic aggregation” is the name we give to a system of recording rules that matches most metrics and removes certain dimensions, such as the instance emitting the metric, to reduce the cardinality (i.e. the number of metrics) and thus making queries faster.

## Abstract oficial

At Criteo, we’ve relied on automatic aggregations for years. “Automatic aggregation” is the name we give to a system of recording rules that matches most metrics and removes certain dimensions, such as the instance emitting the metric, to reduce the cardinality (i.e. the number of metrics) and thus making queries faster.

What started as a workaround has become a key part of how we ensure backend stability and reliability at scale, with hundreds of millions of active metrics, all without requiring users to write a single recording rule. It also significantly reduces the cost of metrics storage. Internally, we call this approach zero-effort Observability, as most teams don’t have to write/maintain recording rules.

In this talk, I’ll walk through how our approach to automatic aggregations has evolved over time, and how we’ve adapted it to fit naturally into our Prometheus-based stack. I’ll share the different implementations we’ve tried, the lessons we’ve learned, and how our latest version takes advantage of recent improvements in Prometheus (new type label) .

## Links

- Página oficial: https://promcon.io/2025-munich/talks/a-history-of-automatic-aggregations/
- YouTube: https://www.youtube.com/watch?v=iy_PmgRTLqQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iy_PmgRTLqQ
- YouTube title: Promcon 2025 - A History of Automatic Aggregations
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/a-history-of-automatic-aggregations/iy_PmgRTLqQ.txt
- Transcript chars: 16923
- Keywords: metrics, metric, actually, instance, prometheus, cluster, graphite, aggregated, alerts, instances, aggregations, recording, compatible, automatic, little, thousand, write, aggregation

### Resumo baseado na transcript

Uh my name is Rafael Visos and today I would like to talk about automatic aggregations. So I'm SE in the team in charge of observability whatever that means in crypto which is an tech company. Uh we want them to write metrics in their code and query metrics in graphana without having to go deeper within the internals. So, maybe we want to throw extra hardware so that the stack is very stable, but that will cost money obviously. uh again that looks maybe a good idea in the perspective but in term of cost and maybe in info it might not be so let me uh what I want to share today is our approach to find the middle ground between all those So it was a big problem because some teams couldn't actually uh query what they needed to have their dashboards and alerts.

### Excerpt da transcript

[music] Okay. >> All right. And there we go. All right. Again, welcome. Big round of applause. >> Thank you. So, hello everyone. Uh my name is Rafael Visos and today I would like to talk about automatic aggregations. Uh before we jump in uh let me shortly present myself. So I'm SE in the team in charge of observability whatever that means in crypto which is an tech company. Uh so far I've done many things such as uh migrating graphite to Prometheus and introducing open telemetry. So initially tracing and now a little bit in metrics. Um I would like also to start to give a bit of context uh on my team and give a few numbers that would be helpful to understand a bit where we are coming from. So my team manages the metrics logs and tracing infrastructure at crypto as well as we provide uh some SDKs so that the team can um send us their telemetry data. Uh metrics wise we ingest around 15 million data point per second which is roughly a billion active series. This is done by 1500 promeus more or less uh worldwide and uh those time series are aggregated to 100 millions then store for three months and down sample for a year.

Uh disclaimer, we're going to talk about that. And uh we have many users, so more than a thousand. Those are SRES, developers, um data scientists and and researchers. So our objectives are quite simple. The first one is to have a reliable platform meaning that we don't want our users to ask themselves is the metric platform having a trouble or my alert is firing for a good reason. Uh we want metric to be fast as well. So that at night during call they don't have to wait for a minute every time they change a variable in Gella. On the opposite we want to have our users to have a very simple experience possible so that they don't need to think too much in the internal of the metric platform. Uh we want them to write metrics in their code and query metrics in graphana without having to go deeper within the internals. Internally we call that the zeroeffort observability. And of course, yeah, we have the cost. If we had unlimited money, that would matter much less. So, as a first glimpse, uh those uh three objectives looks a little bit disjoint.

So, maybe we want to throw extra hardware so that the stack is very stable, but that will cost money obviously. Um maybe your user want to store every single metric for a limited amount of time. uh again that looks maybe a good idea in the perspective but in term of cost and maybe in info it might not be
