---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Alerting", "OpenTelemetry", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Israel Blancas"]
source_url: https://promcon.io/2025-munich/talks/debugging-the-pipeline-observability-for-your-observability-with-otel--prometheus/
youtube_url: https://www.youtube.com/watch?v=uwQUnwQcP7I
youtube_search_url: https://www.youtube.com/results?search_query=Debugging+the+Pipeline%3A+Observability+for+Your+Observability+with+OTel+%2B+Prometheus+PromCon+2025
video_match_score: 1.055
status: video-found
---

# Debugging the Pipeline: Observability for Your Observability with OTel + Prometheus

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Alerting]], [[OpenTelemetry]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Israel Blancas
- Página oficial: https://promcon.io/2025-munich/talks/debugging-the-pipeline-observability-for-your-observability-with-otel--prometheus/
- YouTube: https://www.youtube.com/watch?v=uwQUnwQcP7I

## Resumo

So you've set up OpenTelemetry and Prometheus to observe your systems—but what happens when they start misbehaving? Collectors stop scraping, Target Allocators go AWOL, and metrics go missing just when you need them most. In this talk, we’ll go a layer deeper: how do you observe your observability stack?

## Abstract oficial

So you've set up OpenTelemetry and Prometheus to observe your systems—but what happens when they start misbehaving? Collectors stop scraping, Target Allocators go AWOL, and metrics go missing just when you need them most. In this talk, we’ll go a layer deeper: how do you observe your observability stack?
We'll walk through how to monitor and debug the OTel Collector pipeline using Prometheus itself, from understanding pipeline health signals to catching misconfigurations and performance bottlenecks. We’ll also cover Target Allocator quirks, Prometheus remote write issues, and how to set up practical alerts (before your SREs do it for you).
This is a hands-on, practical talk for folks running Prometheus + OTel in production or considering the combo. Come for the meta observability, stay for the real-world war stories and dashboards.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/debugging-the-pipeline-observability-for-your-observability-with-otel--prometheus/
- YouTube: https://www.youtube.com/watch?v=uwQUnwQcP7I
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uwQUnwQcP7I
- YouTube title: Promcon 2025 - Debugging the Pipeline: Observability for Your Observability with OTel + Prometheus
- Match score: 1.055
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/debugging-the-pipeline-observability-for-your-observability-with-otel/uwQUnwQcP7I.txt
- Transcript chars: 23194
- Keywords: pretty, metrics, collector, everything, happen, allocator, instance, targets, usually, target, sometimes, actually, prometheus, whatever, happening, receiving, exactly, pipeline

### Resumo baseado na transcript

Oh, thanks for for for these days because the thing is that I have learned a lot. Um, and it's pretty difficult to be almost the last one right after this presentations. up because you you heard something right about something called prometheus and these things right and or monitoring or whatever right so you know that you have to have that right so you set up a prometheus thing right and you also learn about something So some metrics right are like saying oh yeah everything is go going well but since you are not observing probably your uh infrastructure right uh you're not observing the server uh very likely you can be like missing data and things like that right and it could be like at some point it's very late for you right to to notice about these things so yeah some some problems some metrics and and many data could be could be lost right and and especially is because when I talk uh we are trying to solve some things related to uh spam metrics right uh to some bad instrumentation and also well things that have been causing us many many issues right and also even silent problems that well you know um you don't know

### Excerpt da transcript

hear me? Okay, awesome. Oh, thanks for for for these days because the thing is that I have learned a lot. Um, and it's pretty difficult to be almost the last one right after this presentations. So, well, my name is Israel. I am super engineer at Corologics and well, I come from from Spain. um usually in contributing to open telemetry. So I am not a a metric expert neither a Prometheus expert, right? So maybe there are things that are not like 100% uh you know accurate. So please don't just if you need to to tell me something do it outside or something, right? Uh and yeah also I participate on different community programs. So so it's pretty usual like you can see me on different conferences and things like that. Usually speaking about open. So yeah the things that why this talk um main things that I will share here in this talk very likely you know about them right uh but the things that I I am usually one of those people right who attract the the cows right and the problems um and well the things that many times I have been well I was working also on another company before right with open staff and everything right um it's like I was like pretty um let's say excited right about the project and everything right so I have been like pushing people for for for for using open telemetry it's not what I'm going to do today don't don't don't worry um and the thing is that sometimes I reject right because I forget to tell them some things right uh so the talk today is like a little bit right to talk that kind of things and situations that some people have has um had in the past right because just of my all my suggestions right about using open telemetry.

Uh next time I will stay quiet. But yeah, the things that imagine right you have you are a developer or something right and you have well you have many applications right some of them could be writing in golan or in python net whatever thing right um you also have set up because you you heard something right about something called prometheus and these things right and or monitoring or whatever right so you know that you have to have that right so you set up a prometheus thing right and you also learn about something called u open telemetry so you set up also bunch of open collectors to gather up many data and everything, right? And well, also you need right it is important because you need to visualize the data but also you know you have to write something to managers. Managers love to see things moving right on s
