---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["Observability"]
speakers: ["Emma Wang", "Doordash", "Ben Raskin", "Chronosphere"]
sched_url: https://kccncna2022.sched.com/event/182IP/doordashs-journey-from-statsd-to-prometheus-with-10-million-metricssecond-emma-wang-doordash-ben-raskin-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=DoorDash%E2%80%99s+Journey+From+StatsD+To+Prometheus+With+10+Million+Metrics%2FSecond+CNCF+KubeCon+2022
slides: []
status: parsed
---

# DoorDash’s Journey From StatsD To Prometheus With 10 Million Metrics/Second - Emma Wang, Doordash & Ben Raskin, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Detroit
- Speakers: Emma Wang, Doordash, Ben Raskin, Chronosphere
- Schedule: https://kccncna2022.sched.com/event/182IP/doordashs-journey-from-statsd-to-prometheus-with-10-million-metricssecond-emma-wang-doordash-ben-raskin-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=DoorDash%E2%80%99s+Journey+From+StatsD+To+Prometheus+With+10+Million+Metrics%2FSecond+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre DoorDash’s Journey From StatsD To Prometheus With 10 Million Metrics/Second.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182IP/doordashs-journey-from-statsd-to-prometheus-with-10-million-metricssecond-emma-wang-doordash-ben-raskin-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=DoorDash%E2%80%99s+Journey+From+StatsD+To+Prometheus+With+10+Million+Metrics%2FSecond+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xkEGmPF0kCQ
- YouTube title: DoorDash’s Journey From StatsD To Prometheus With 10 Million Metrics/Second - Emma Wang & Ben Raskin
- Match score: 0.956
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/doordashs-journey-from-statsd-to-prometheus-with-10-million-metrics-se/xkEGmPF0kCQ.txt
- Transcript chars: 27767
- Keywords: metrics, prometheus, standard, dashboards, doordash, migration, series, actually, source, counters, labels, alerts, exporters, matrix, automatically, probably, statsd, second

### Resumo baseado na transcript

hello everyone and welcome I hope you are having a good week here at kubecon today we're going to be talking about doordasha's migration from statsd to Prometheus with over 10 million metrics per second before we get started I wanted to just do a quick poll of the room um how many people here work at companies that use stats d okay what about Prometheus all right and what about both okay all right try to catch some people in the middle of their migration right um cool so

### Excerpt da transcript

hello everyone and welcome I hope you are having a good week here at kubecon today we're going to be talking about doordasha's migration from statsd to Prometheus with over 10 million metrics per second before we get started I wanted to just do a quick poll of the room um how many people here work at companies that use stats d okay what about Prometheus all right and what about both okay all right try to catch some people in the middle of their migration right um cool so my name is Ben Raskin I'm a Solutions architect at chronosphere where I work on customer enablement and onboarding chronosphere is an observability company that focuses on focuses on cloud native companies prior to chronosphere I was a software engineer at Uber working on M3 an open source metrics platform about three and a half years ago after graduating from Canada University now I'm in our coin doctor of disability team and I have the whole organization to migrate from statistic platform to prometheus-based monitoring yeah cool so just a bit of an agenda um we're first going to look at some of the challenges that doordash faced with statsd we'll take a look at how Prometheus resolved those uh next we'll talk about the client-side migration effort from stats D to Prometheus next we'll talk about enablement sort of how we got you know the the end users and engineers and service teams up to speed and then finally we'll do a bit of a retro looking at some of the learnings and key results of this of this gigantic task so we want to begin by talking about some of the challenges that doordash faced with statsd so a lack of naming standardization and limited support for tags makes it hard to give context and meaning to underlying statsd metrics so we can see here we have two two metrics here coming from two different Services they're both tracking the same thing the number of page views but unless you have intimate knowledge of these services and the metrics that they're producing it's hard to know right that these two that these two metrics are in fact tracking the same thing we'll see in a bit with with tags and labels in Prometheus it's much easier to give context to these particular underlying Time series next the number of metric scales with user traffic in statsd this means if the number of user requests or traffic to the overall business goes up the number of metrics go up not necessarily the not necessarily the cardinality or unique number of metrics but the total volume this oftentimes
