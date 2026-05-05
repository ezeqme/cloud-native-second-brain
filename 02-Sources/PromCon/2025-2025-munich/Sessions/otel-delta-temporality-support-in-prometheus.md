---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability"]
speakers: ["Fiona Liao"]
source_url: https://promcon.io/2025-munich/talks/otel-delta-temporality-support-in-prometheus/
youtube_url: https://www.youtube.com/watch?v=5q2_BoRHwVo
youtube_search_url: https://www.youtube.com/results?search_query=OTEL+delta+temporality+support+in+Prometheus+PromCon+2025
video_match_score: 1.001
status: video-found
---

# OTEL delta temporality support in Prometheus

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: Fiona Liao
- Página oficial: https://promcon.io/2025-munich/talks/otel-delta-temporality-support-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=5q2_BoRHwVo

## Resumo

OpenTelemetry's metric model natively supports both delta and cumulative temporality, while Prometheus has historically only supported cumulative. In the past, this meant any delta metrics attempted to be ingested via Prometheus' OTLP endpoint were rejected. More recently however, there has been progress with delta support in Prometheus to improve OTEL interoperability.

## Abstract oficial

OpenTelemetry's metric model natively supports both delta and cumulative temporality, while Prometheus has historically only supported cumulative. In the past, this meant any delta metrics attempted to be ingested via Prometheus' OTLP endpoint were rejected. More recently however, there has been progress with delta support in Prometheus to improve OTEL interoperability. 

This talk will explore the journey of OTEL delta metric support in Prometheus: the historical context, current state, and potential future steps, highlighting the challenges encountered and open questions that remain.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/otel-delta-temporality-support-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=5q2_BoRHwVo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5q2_BoRHwVo
- YouTube title: Promcon 2025 - OTEL delta temporality support in Prometheus
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/otel-delta-temporality-support-in-prometheus/5q2_BoRHwVo.txt
- Transcript chars: 25543
- Keywords: prometheus, sample, increase, samples, deltas, cumitive, counter, metrics, counters, values, support, cumulative, resets, functions, reported, interval, series, temporarity

### Resumo baseado na transcript

[music] Now Fiona is going to tell us about Hotel Delta Temporality in Vegas. And yeah, I'm going to be talking about Delta temporality support in Prometheus. Um so we're just going to call that but yeah start time and uh cumulative temporarity hopefully we all know this we all love this right um because this is what Prometheus supports today. Um but yeah, so um yeah, the process we just described with all the pretty grass and stuff, that's basically how Prometheus does the um does the increase calculation. Um so unfortunately the first and last time stamps in a select range might not match with the boundaries of the time range we're querying for and this is this is fairly frequent I guess um how Prometheus deals with this is that it extrapolates to guess what the values at the boundaries are. So Prometheus does have that industri um but initially and by default it rejects deltas.

### Excerpt da transcript

[music] Now Fiona is going to tell us about Hotel Delta Temporality in Vegas. >> Cool. Uh is is the mic working? Checking. Yeah. Okay. Awesome. Uh yeah. So, hi, I'm Fiona >> with a mic >> like this. >> Yeah. >> Okay, cool. Yeah, I can hear my >> That's what the mic's for. >> Okay. >> Yeah, I just need to press it to my mouth like here. Here. This. Good. Okay, cool. Well, let me know if it goes wrong. Um, but yeah. Okay, let's start again then. I'm Fiona. I'm a software engineer at Grafana Labs. And yeah, I'm going to be talking about Delta temporality support in Prometheus. um today. So um let's first uh define temporality. So this is how additive data types like counters are expressed in time whether uh values incorporate previous measurements or not. So just as a bit of aside when I say counter here I mean something that records something like the number requests. So Prometheus cost is a counter and open telemetry calls like the closest equivalent a sum. Um but I'm just going to be using counter to refer to both Prometheus counters and hotel sums from uh the rest of the talk.

So in the hotel world uh a sample has two time stamps. It's got a mandary time stamp uh which is of when the measurement was taken just the tiny Unix nano and I'm just going to be calling that the reported time from now on. And it also has an optional start time stamp which indicates when the measurement started. Um so we're just going to call that but yeah start time and uh cumulative temporarity hopefully we all know this we all love this right um because this is what Prometheus supports today. So in cumitive mode this means each reported value is the running total since we started measuring and all the previous values are incorporated too and with the hotel start times this means successive samples share the same same start time until there's a reset like you can see how in this example all four samples share the same start time t0 and then you see at t time t1 the value is one at t2 it's five which means between uh t1 and t2 we've added uh four samples. No, sorry, not small samples. Um account form.

Um and in graph form, the samples will look something like this if you draw them by their reported time. Um in the case of counters, uh you want usually want to see how much the count has increased in a time range and maybe get a per second rate. So with pumitive ones you find the increase by taking the difference between the start and end values in the range. But one thing to take
