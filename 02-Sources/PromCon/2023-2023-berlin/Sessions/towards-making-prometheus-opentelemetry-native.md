---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/towards-making-prometheus-opentelemetry-native/
youtube_url: https://www.youtube.com/watch?v=mcabOH70FqU
youtube_search_url: https://www.youtube.com/results?search_query=Towards+making+Prometheus+OpenTelemetry+native+PromCon+2023
video_match_score: 1.006
status: video-found
---

# Towards making Prometheus OpenTelemetry native

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/towards-making-prometheus-opentelemetry-native/
- YouTube: https://www.youtube.com/watch?v=mcabOH70FqU

## Resumo

Speaker(s): Goutham Veeramachaneni & Jesús Vázquez OpenTelemetry is coming up as the emerging standard for instrumenting and transporting telemetry data. There is good integration between Prometheus and OpenTelemetry, with the conversion between the two as part of the OpenTelemetry specification. However, the query experience and overall the usability of Prometheus when being used as an OTel metrics backend is quite lacking.

## Abstract oficial

Speaker(s): Goutham Veeramachaneni & Jesús Vázquez

OpenTelemetry is coming up as the emerging standard for instrumenting and transporting telemetry data. There is good integration between Prometheus and OpenTelemetry, with the conversion between the two as part of the OpenTelemetry specification.

However, the query experience and overall the usability of Prometheus when being used as an OTel metrics backend is quite lacking. The Prometheus community is working towards bridging the gaps and making sure that Prometheus is the best backend for OpenTelemetry metrics.

In this talk, we will present the current state and the solutions being implemented right now to address some of them. We will also present the longer road-map which will address some of the fundamental datamodel issues, putting us on the path to become 100% OTel native without compromising on the Pull model and what made Prometheus great.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/towards-making-prometheus-opentelemetry-native/
- YouTube: https://www.youtube.com/watch?v=mcabOH70FqU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mcabOH70FqU
- YouTube title: PromCon 2023 - Towards making Prometheus OpenTelemetry native
- Match score: 1.006
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/towards-making-prometheus-opentelemetry-native/mcabOH70FqU.txt
- Transcript chars: 25391
- Keywords: prometheus, metric, metrics, question, support, otel, probably, attributes, remote, resource, issues, protocol, basically, native, discovery, trying, without, request

### Resumo baseado na transcript

[Music] hello everyone hi I'm gam I'm a product manager by day but I still like uh writing code so I'm a software engineer by night or at least I like to think that I am um yeah hi I'm Jesus I'm a software engineer at grafana and uh Prometheus team member since this year and I've been over the last two years I've been working on maintaining the tsdb out of order support and now open Telemetry um or trying to make promis support open Telemetry natively um I'd defining their metrics or where these metrics are even defined cool so yeah we want to expand Prometheus uh to support most of the common use cases of the otel character set yeah yeah this topic keeps coming back uh to me U so out

### Excerpt da transcript

[Music] hello everyone hi I'm gam I'm a product manager by day but I still like uh writing code so I'm a software engineer by night or at least I like to think that I am um yeah hi I'm Jesus I'm a software engineer at grafana and uh Prometheus team member since this year and I've been over the last two years I've been working on maintaining the tsdb out of order support and now open Telemetry um or trying to make promis support open Telemetry natively um I'd like to start with this chart so I took this a screenshot uh couple of days ago this is the graan Cloud's growth um in terms of like the amount of organizations that are um adopting or trying to use odlp metrics so this is this does not include um traces or logs it's just metrics and we've seen like a 2.5 times increase uh without like much effort from our side so it seems that there's uh interest in the community for this um and we're also getting questions about like what's the status on the OT otel sdks like um their support for like sending metrics to Prometheus and so it's it's a topic that's gain inaction and and yeah but the thing is um for for those of you who don't know like open Telemetry is a spec so it defines like how you're supposed to observe met different observability signals such as metrics traces or logs um but it doesn't provide a back end and like users that want to use like their favorite um metrics back end PR mythus um when they try they see that it's sometimes not the perfect fit like there's some things that don't work as expected and and also yeah maybe sometimes there are some samples dropped that shouldn't be dropped and sometimes times it's hard to like see the actual data that you send it um yeah and that's the image where that's the P request that Julian was referring to earlier that's the very very very experimental um OTP native ingestion endpoint that we have just added to Prometheus um uh so we're getting there um and now I leave uh it to Gotham to like show you a quick demo where you can see some some of these issues I was referring to um yeah so basically uh open open Telemetry is a spec uh it has a data model um and this is kind of how the open Telemetry data model looks like for example if you have a service that's pushing data uh you have a bunch of attributes called resource attributes that kind of tell you details about where the service lives what the service is about and things like that and then when this uh service or instance pushes metrics these are norm
