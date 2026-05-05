---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "OpenTelemetry", "Scalability Reliability", "Community"]
speakers: ["Arve Knudsen", "Jesus Vazquez"]
source_url: https://promcon.io/2024-berlin/talks/practical-opentelemetry-with-prometheus-30/
youtube_url: https://www.youtube.com/watch?v=nUFSugrTGW8
youtube_search_url: https://www.youtube.com/results?search_query=Practical+OpenTelemetry+with+Prometheus+3.0+PromCon+2024
video_match_score: 0.999
status: video-found
---

# Practical OpenTelemetry with Prometheus 3.0

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[OpenTelemetry]], [[Scalability Reliability]], [[Community]]
- Speakers: Arve Knudsen, Jesus Vazquez
- Página oficial: https://promcon.io/2024-berlin/talks/practical-opentelemetry-with-prometheus-30/
- YouTube: https://www.youtube.com/watch?v=nUFSugrTGW8

## Resumo

A lot of hard work has gone into making Prometheus 3.0 a great OpenTelemetry (OTel) metrics store. In this talk we dive into the new features and what you need to effectively store and query OTel data inside Prometheus. OTLP ingestion is now GA.

## Abstract oficial

A lot of hard work has gone into making Prometheus 3.0 a great OpenTelemetry (OTel) metrics store. In this talk we dive into the new features and what you need to effectively store and query OTel data inside Prometheus.

OTLP ingestion is now GA.


This means no more feature flag. But you need to enable it via another flag.
This means we are committed to making this work at scale and is a major focus of future development.
OTLP performance has been improved massively:


Benchmarks show ~49% faster request translation on average.


Effectively storing and querying OTLP data


To make OTLP useful, copy some resource attributes. Here is a good starting list.
Don't copy too many as it will cause issues.
To make this even more seamless, there is the experimental info function.
Proper metadata storage is being worked on too.


Support for delta temporality


OTLP is not just cumulative, but there is not the delta to cumulative processor to help convert your deltas before storing.
Proper support for delta in Prometheus is being worked on as well.


A community mixin for popular semantic conventions


There is also a community mixin now available (TBD but will likely exist by Sept.)




3.0 is not the end, we are actively working on more improvements. Our goal is to make Prometheus the best OSS store for OTel metrics.


up metric implementation in push
. in metric names and how that'll look like

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/practical-opentelemetry-with-prometheus-30/
- YouTube: https://www.youtube.com/watch?v=nUFSugrTGW8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nUFSugrTGW8
- YouTube title: PromCon 2024 - Practical OpenTelemetry with Prometheus 3.0
- Match score: 0.999
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/practical-opentelemetry-with-prometheus-3-0/nUFSugrTGW8.txt
- Transcript chars: 21765
- Keywords: labels, prometheus, promethus, attributes, metric, resource, basically, cumulative, target, processor, series, collector, metrics, actually, temporality, already, version, instead

### Resumo baseado na transcript

[Music] [Applause] hello everyone I'm arvic nson I'm a senior soft engineer with the graphon labs where I work on on the graphon Mir uh but I'm also a maintainer of the OTP endpoint in Prometheus uh together with hesus hello everyone I am Jesus also a senior software engineer atral apps and I've been working with promethus a few years now lately I've been spending time with the odlp endpoint myself um before we get started I'd like to ask how many of you a quick uh hand raise

### Excerpt da transcript

[Music] [Applause] hello everyone I'm arvic nson I'm a senior soft engineer with the graphon labs where I work on on the graphon Mir uh but I'm also a maintainer of the OTP endpoint in Prometheus uh together with hesus hello everyone I am Jesus also a senior software engineer atral apps and I've been working with promethus a few years now lately I've been spending time with the odlp endpoint myself um before we get started I'd like to ask how many of you a quick uh hand raise how many of you have worked with open Telemetry uh in the last year like any kind of work maybe working with the SDK setting up a collector receivers exporters okay maybe 10% 15% of the people that's good it's just uh to keep track of that percentage it's growing over time we we would like to see what happens next year all right so last year around this time Gotham and I brought you a talk about um how promethus wanted to commit into becoming more Hotel native and some of the challenges that we were facing uh some of those challenges were um properly handling resource attributes what were resource attributes in the yotel spec how to handle that in promus and then udf8 support for nric names and attribute uh names and values um the push versus the pull model because as you know Prometheus is pull based but oel is push based and how to blend that in and then the differences between cumulative and Delta temporality which both are valid according to the spec but Prometheus is just cumulative temporality so this time what we're bringing you is a few updates on each of these topics and I give it to arv to give you the first one thanks so the the thing with open Telemetry is that it has this concept which um it calls resource and the resource basically corresponds to The Entity producing the metrics so um it has a set of uh attributes uh describing each uh resource and those attributes are basically uh um key value pairs metad data so um in so the the problem when ingesting uh open Elementary metric in promethus kind of becomes how do you how do you keep uh these uh resource attributes so um one method we can recommend is um is to copy or to promote uh these attributes um to metric labels although just a select set of them because uh otherwise if you would copy all of them they would would be too many and um this basic this m this method basically corresponds to to how historically um prome Prometheus has uh copied um me promoted metadata about um scraping targets as uh as labels um so as I
