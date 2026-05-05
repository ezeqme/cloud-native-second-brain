---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/opentelemetry-metrics-is-ga-so-w/
youtube_url: https://www.youtube.com/watch?v=FT2diLb9KNY
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Metrics+is+GA%2C+So+What%3F+PromCon+2022
video_match_score: 0.944
status: video-found
---

# OpenTelemetry Metrics is GA, So What?

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/opentelemetry-metrics-is-ga-so-w/
- YouTube: https://www.youtube.com/watch?v=FT2diLb9KNY

## Resumo

Speaker(s): James Guthrie The OpenTelemetry Metrics data model was recently stabilized, but most of you will ask yourselves "Why should I care? I’m already using Prometheus". In this talk, we'll gain valuable insights into what’s new and different in OpenTelemetry Metrics, and the kinds of issues that you might encounter when trying to store and query both OTel and Prometheus data.

## Abstract oficial

Speaker(s): James Guthrie

The OpenTelemetry Metrics data model was recently stabilized, but most of you will ask yourselves "Why should I care? I’m already using Prometheus".

In this talk, we'll gain valuable insights into what’s new and different in OpenTelemetry Metrics, and the kinds of issues that you might encounter when trying to store and query both OTel and Prometheus data. We'll start by looking into which options you have to integrate OTel Metrics in your existing monitoring stack. Then we'll look at differences between the Prometheus and OpenTelemetry's metric types, how sums are different from counters, and why some sums are monotonic and some aren’t. We'll cover the tradeoffs between delta and cumulative temporality for Sums and Histograms in terms of both collection and analysis. Finally, we'll cover resets and gaps and how an explicit start time helps create more accurate analysis.

At the end of this talk, you'll be prepared to handle OpenTelementry metrics in your monitoring setup.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/opentelemetry-metrics-is-ga-so-w/
- YouTube: https://www.youtube.com/watch?v=FT2diLb9KNY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FT2diLb9KNY
- YouTube title: PromCon EU 2022: OpenTelemetry Metrics is GA, So What?
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/opentelemetry-metrics-is-ga-so-what/FT2diLb9KNY.txt
- Transcript chars: 23523
- Keywords: metrics, prometheus, basically, collector, metric, actually, cumulative, storage, remote, exporters, differences, answer, matrix, scrape, application, somebody, symmetry, histogram

### Resumo baseado na transcript

[Music] foreign [Music] good afternoon hi everyone so my name is James Guthrie I work at timescale I work on a product called prom scale you may have heard of it before you can probably tell by the name it started its life as a Prometheus remote Right Storage backend but nowadays it's kind of like becoming a storage backend for all sorts of observability data so we store traces with store metrics and we're going to do more stuff in the future but when we were looking into open

### Excerpt da transcript

[Music] foreign [Music] good afternoon hi everyone so my name is James Guthrie I work at timescale I work on a product called prom scale you may have heard of it before you can probably tell by the name it started its life as a Prometheus remote Right Storage backend but nowadays it's kind of like becoming a storage backend for all sorts of observability data so we store traces with store metrics and we're going to do more stuff in the future but when we were looking into open Telemetry metrics we kind of realized that there are some differences and that was kind of how the idea for this talk came about um so before I really get into things I kind of want to see what's going on in the audience about like what people actually know so the previous talk they asked how many people uh are using Prometheus in production I saw a lot of hands go up so um how many people are were aware that open tele open television metrics became generally available earlier this year or late last year okay so about a third of the audience okay how many of those people spend some time to think about like okay openstream extra metrics what am I going to do with this now five maybe okay how many people are actually running anything that uses open Geometry metrics one okay and uh how many people are using open temperature traces in their production setups okay quite a few more so about 15 I guess cool so when it came to uh putting together this talk I realized that uh open Telemetry metrics is kind of a jungle there is a lot that one could talk about and it would not fit into a 20-minute talk so I had to kind of like try and find a path that goes through that jungle and the point of view that I've chosen to take in this talk is uh as you can see in the title uh the operator's point of view so uh I'm basically not really going to cover anything about how do I instrument my application which sdks do I use how do I do all that stuff I'm not going to talk about any of that at all I'm basically going to talk about it from the point of view of if you are operating an existing Prometheus setup and somebody comes and says hey I have this thing it's doing open Geometry metrics what are things that you need to kind of think about or care about so a couple of questions that I'm going to try and answer today are what do I do with an app that's been instrumented with open time stream metrics uh can I just like plug this thing into what I already have and what things do I need to kind of be aware o
