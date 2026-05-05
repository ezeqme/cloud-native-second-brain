---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Kruthika Prasanna Simha", "Charlie Le", "Apple"]
sched_url: https://kccncna2024.sched.com/event/1i7lJ/unifying-observability-correlating-metrics-traces-and-logs-with-exemplars-and-opentelemetry-kruthika-prasanna-simha-charlie-le-apple
youtube_search_url: https://www.youtube.com/results?search_query=Unifying+Observability%3A+Correlating+Metrics%2C+Traces%2C+and+Logs+with+Exemplars+and+OpenTelemetry+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unifying Observability: Correlating Metrics, Traces, and Logs with Exemplars and OpenTelemetry - Kruthika Prasanna Simha & Charlie Le, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Kruthika Prasanna Simha, Charlie Le, Apple
- Schedule: https://kccncna2024.sched.com/event/1i7lJ/unifying-observability-correlating-metrics-traces-and-logs-with-exemplars-and-opentelemetry-kruthika-prasanna-simha-charlie-le-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Unifying+Observability%3A+Correlating+Metrics%2C+Traces%2C+and+Logs+with+Exemplars+and+OpenTelemetry+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unifying Observability: Correlating Metrics, Traces, and Logs with Exemplars and OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lJ/unifying-observability-correlating-metrics-traces-and-logs-with-exemplars-and-opentelemetry-kruthika-prasanna-simha-charlie-le-apple
- YouTube search: https://www.youtube.com/results?search_query=Unifying+Observability%3A+Correlating+Metrics%2C+Traces%2C+and+Logs+with+Exemplars+and+OpenTelemetry+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zYF1JIZmpI4
- YouTube title: Unifying Observability: Correlating Metrics, Traces, and Logs with Exemplars an... K.P. Simha, C. Le
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unifying-observability-correlating-metrics-traces-and-logs-with-exempl/zYF1JIZmpI4.txt
- Transcript chars: 28754
- Keywords: exemplars, trace, logs, traces, metrics, metric, prometheus, exemplar, question, little, information, observability, enable, figure, tracing, request, finally, insights

### Resumo baseado na transcript

good afternoon everyone um thank you for being here today to listen to us talk about unifying observability correlating metrics traces and Logs with exemplars and open Telemetry um so before we get started we just want to take a quick moment to introduce ourselves hi I'm cria I'm a machine learning engineer at Apple I work with the observ observability team and my background is in machine learning data science and observability Charlie hi I'm Charlie um I'm a software engineer at Apple um I've been here for about

### Excerpt da transcript

good afternoon everyone um thank you for being here today to listen to us talk about unifying observability correlating metrics traces and Logs with exemplars and open Telemetry um so before we get started we just want to take a quick moment to introduce ourselves hi I'm cria I'm a machine learning engineer at Apple I work with the observ observability team and my background is in machine learning data science and observability Charlie hi I'm Charlie um I'm a software engineer at Apple um I've been here for about eight years and um I'm also a cortex maintainer I'm super happy to talk about exemplars today so um thanks for coming all right um we'll just do a quick walkr of our agenda so we'll start with a case study and a demo of what we're going to be talking about and then talk about what exemplars are and then go into a high level overview before diving deeper into the details of exemplars and how to set them up then we'll talk about the value of using exemplars for your service and finally open it up to question and answers so please think about your questions while we talk um so this talk is mainly geared towards um sres developers operations experts ml Engineers basically anyone who is interested in improving the reliability and observability of your service so what we're going to learn today is we're going to learn about what exemplars are talk about how to enable exemplars with open Telemetry how to configure your Prometheus back end so that you can store exemplars and finally how can you visualize exemplars to get the most actionable insights from them so Charlie do you want to get a started with the case study yeah thanks cria so um let's imagine that you uh run this uh store for selling telescopes um it's your pride and your joy and this is your let's say your primary source of income just by the way this isn't a real store but just say you had a store that sold telescopes and um one day this happens uh the telescope images aren't showing up anymore and uh the prices are all zeros and um what does that mean right like okay now there's going to be loss of Revenue because telescopes aren't being sold um there's this this there's this degraded user experience now because customers that are coming on to your site can't buy anything anymore and there's this potential loss of loyalty now because if your website isn't working what does that say about your telescopes um so the objective here is to be able to quickly um diagnose and resolve these kinds of
