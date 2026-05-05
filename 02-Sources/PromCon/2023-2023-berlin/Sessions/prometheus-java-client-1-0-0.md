---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/prometheus-java-client/
youtube_url: https://www.youtube.com/watch?v=psyeJoETXug
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Java+Client+1.0.0+PromCon+2023
video_match_score: 0.942
status: video-found
---

# Prometheus Java Client 1.0.0

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/prometheus-java-client/
- YouTube: https://www.youtube.com/watch?v=psyeJoETXug

## Resumo

Speaker(s): Fabian Stäber At last year's PromCon we presented a lightning talk announcing a complete re-write of the Prometheus Java client library. Meanwhile the first releases are out (*), and we are proud to present the results: Native histogram support, awesome performance benchmarks, extensive runtime configuration options, automatic Exemplars for various tracing libraries, Exemplar markers for trace sampling, integration with OpenTelemetry metrics, and more. We will present the current status, migration path, and future plans.

## Abstract oficial

Speaker(s): Fabian Stäber

At last year's PromCon we presented a lightning talk announcing a complete re-write of the Prometheus Java client library. Meanwhile the first releases are out (*), and we are proud to present the results: Native histogram support, awesome performance benchmarks, extensive runtime configuration options, automatic Exemplars for various tracing libraries, Exemplar markers for trace sampling, integration with OpenTelemetry metrics, and more.

We will present the current status, migration path, and future plans.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/prometheus-java-client/
- YouTube: https://www.youtube.com/watch?v=psyeJoETXug
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=psyeJoETXug
- YouTube title: PromCon 2023 - Prometheus Java Client 1.0.0
- Match score: 0.942
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/prometheus-java-client-1-0-0/psyeJoETXug.txt
- Transcript chars: 24057
- Keywords: library, prometheus, metrics, histogram, client, metric, server, actually, traces, basically, feature, promethus, couple, standard, application, exemplars, course, question

### Resumo baseado na transcript

[Music] yeah thank you so that was fun with the quiz so really cool we should do that every promcon I think um yeah so um this one is not so much about fun and entertainment but hopefully about cool features and cool things happening in the Prometheus ecosystem the day before yesterday um the Prometheus Java client Library 1.0 came out and yeah I'm going to walk you through it present you the latest features and what happened and so forth few words words about me so I'm favian

### Excerpt da transcript

[Music] yeah thank you so that was fun with the quiz so really cool we should do that every promcon I think um yeah so um this one is not so much about fun and entertainment but hopefully about cool features and cool things happening in the Prometheus ecosystem the day before yesterday um the Prometheus Java client Library 1.0 came out and yeah I'm going to walk you through it present you the latest features and what happened and so forth few words words about me so I'm favian I work at grafana I'm member of the Prometheus team and um as you heard in the introduction so I'm maintainer or one of the maintainers of the Prometheus Java client so if you have anything in the release that you like or don't like or any wishes for the future so talk to me um always happy for feedback so the 1.0 release is not a regular release where you just you know update the dependency and then you're done it's basically a complete rewrite of the underlying data model and the way that the library worked and so forth and for that reason a lot of things changed and there are a lot of improvements and things that are slightly different and so forth so it's like hard to come up with a complete feature list or a complete list of things that are new but if I had to pick like two highlights or two like important things that come with the 1.0 release now I would say it's um Native histograms and it support for open Telemetry and I'm going to show you that and as it is more or less a complete rewrite um it's also not back backwards compatible but if you are a user of the previous version 0.6 or older you don't need to refactor all your code now because um we provide a migration module so you can use that and Bridge your previous metrics from the um collector registry with the new promethus registry and then you can kind of keep using your old metrics so no need to adopt all of your code at once right cool so let's get started talking about these features um let's start with um the histogram so this is how Java looks like in case you are coming from a different programming language so this creates a histogram pretty straightforward with a name help message unit couple of labels and it's an example of how you would use the histogram to observe a duration of course there's more API you have you know different ways to observe durations and so forth but this would be the most simple case and as I said in the introduction that native histograms are kind of one of the new features here I think
