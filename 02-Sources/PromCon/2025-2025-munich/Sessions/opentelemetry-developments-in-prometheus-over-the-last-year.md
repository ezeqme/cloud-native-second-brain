---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "OpenTelemetry", "Scalability Reliability"]
speakers: ["Arve Knudsen", "Owen Williams"]
source_url: https://promcon.io/2025-munich/talks/opentelemetry-developments-in-prometheus-over-the-last-year/
youtube_url: https://www.youtube.com/watch?v=l7vR-s3KA9w
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+developments+in+Prometheus+over+the+last+year+PromCon+2025
video_match_score: 1.031
status: video-found
---

# OpenTelemetry developments in Prometheus over the last year

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: Arve Knudsen, Owen Williams
- Página oficial: https://promcon.io/2025-munich/talks/opentelemetry-developments-in-prometheus-over-the-last-year/
- YouTube: https://www.youtube.com/watch?v=l7vR-s3KA9w

## Resumo

At the last PromCon in Berlin, general availability of the OpenTelemetry ingestion (OTLP) endpoint was announced. Since then, Prometheus developers have been very active in further improving support for the OpenTelemetry standard. Owen and Arve will be talking about the numerous improvements that have gone into Prometheus' OTLP endpoint in the meantime.

## Abstract oficial

At the last PromCon in Berlin, general availability of the OpenTelemetry ingestion (OTLP) endpoint was announced. Since then, Prometheus developers have been very active in further improving support for the OpenTelemetry standard.

Owen and Arve will be talking about the numerous improvements that have gone into Prometheus' OTLP endpoint in the meantime. Most of them are functional, but performance has also been significantly tuned!

We round off the talk with a quick demo.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/opentelemetry-developments-in-prometheus-over-the-last-year/
- YouTube: https://www.youtube.com/watch?v=l7vR-s3KA9w
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l7vR-s3KA9w
- YouTube title: Promcon 2025 - OpenTelemetry developments in Prometheus over the last year
- Match score: 1.031
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/opentelemetry-developments-in-prometheus-over-the-last-year/l7vR-s3KA9w.txt
- Transcript chars: 21191
- Keywords: prometheus, labels, metric, attributes, translation, version, metrics, histograms, default, resource, working, native, endpoint, another, metadata, queries, write, collector

### Resumo baseado na transcript

So um we are going to talk about uh open telemetry developments that have taken place in Prometheus since last year's uh prom. I'm also at graphana um in the databases upstream team working on open telemetry in Prometheus. Um and so one uh uh major sort of um piece of work in the past year has been the ability to allow for optionally untransated metric and label names um when ingesting into Prometheus. So this is for um often you know uh users who are used to open telemetry and the semantic conventions and they want to have those original names uh show up in Prometheus uh when they ingest using the OTLP endpoint. So uh previously the uh when when when doing the ingestion uh dots would always be converted to underscores and suffixes will always be would always be added as per sort of the Prometheus style and uh specification. Um for the new uh no translation option, uh this is since Prometheus 3.4.

### Excerpt da transcript

[music] Thank you. Um hello everyone. So um we are going to talk about uh open telemetry developments that have taken place in Prometheus since last year's uh prom. Uh I'm Arv Nudson. I'm a software engineer at Grafana Labs where I work on Grafana Mu. >> Uh and I'm Owen Williams. I'm also at graphana um in the databases upstream team working on open telemetry in Prometheus. Yes. So basically um for a um for a recap um at last year's prom which took place in Berlin um we announced general availability of the uh open telemetry ingestion endpoint uh in Prometheus and in the meantime we we have been very busy um adding improvements to to um Prometheus's support for the open terminal telemetry standard um both in terms of u functionality um and also uh open telemetry protocol ingestion performance. Um this but this uh this is not uh the end of course to the improvements. Uh there's plenty more to come um many of which are already in in prog progress. And so we have divided this talk into sections. the the first section is dedicated to the to the functional improvements which have gone into uh Prometheus's open telemetry ingestion.

>> Yeah. So, uh as we heard yesterday, there's still a lot of rough edges around integrating open telemetry uh with Prometheus. Um and we're sort of working on those things one at a time and trying to smooth um the experience. Um and so one uh uh major sort of um piece of work in the past year has been the ability to allow for optionally untransated metric and label names um when ingesting into Prometheus. So this is for um often you know uh users who are used to open telemetry and the semantic conventions and they want to have those original names uh show up in Prometheus uh when they ingest using the OTLP endpoint. So uh previously the uh when when when doing the ingestion uh dots would always be converted to underscores and suffixes will always be would always be added as per sort of the Prometheus style and uh specification. Um that is still the default. Uh there's no plans to change that from the default. Uh but for those users who know what they're doing and want uh those uh untransated names, they can set the translation strategy option.

Um for the new uh no translation option, uh this is since Prometheus 3.4. Um so no character conversion is performed. Everything just passes through unchanged. Um as as mentioned in the previous talk, uh this can cause problems with type and unit. if you have some sort of latency metric uh on
