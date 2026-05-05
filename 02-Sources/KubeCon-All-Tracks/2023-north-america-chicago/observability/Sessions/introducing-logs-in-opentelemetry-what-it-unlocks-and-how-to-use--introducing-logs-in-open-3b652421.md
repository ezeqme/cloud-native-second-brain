---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability"]
speakers: ["Morgan McLean", "Splunk", "Dan Jaglowski", "observIQ"]
sched_url: https://kccncna2023.sched.com/event/1R2r4/introducing-logs-in-opentelemetry-what-it-unlocks-and-how-to-use-it-morgan-mclean-splunk-dan-jaglowski-observiq
youtube_search_url: https://www.youtube.com/results?search_query=Introducing+Logs+in+OpenTelemetry%3A+What+It+Unlocks+and+How+to+Use+It+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Introducing Logs in OpenTelemetry: What It Unlocks and How to Use It - Morgan McLean, Splunk & Dan Jaglowski, observIQ

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Morgan McLean, Splunk, Dan Jaglowski, observIQ
- Schedule: https://kccncna2023.sched.com/event/1R2r4/introducing-logs-in-opentelemetry-what-it-unlocks-and-how-to-use-it-morgan-mclean-splunk-dan-jaglowski-observiq
- Busca YouTube: https://www.youtube.com/results?search_query=Introducing+Logs+in+OpenTelemetry%3A+What+It+Unlocks+and+How+to+Use+It+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Introducing Logs in OpenTelemetry: What It Unlocks and How to Use It.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2r4/introducing-logs-in-opentelemetry-what-it-unlocks-and-how-to-use-it-morgan-mclean-splunk-dan-jaglowski-observiq
- YouTube search: https://www.youtube.com/results?search_query=Introducing+Logs+in+OpenTelemetry%3A+What+It+Unlocks+and+How+to+Use+It+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=a1KZwfLr2PQ
- YouTube title: Introducing Logs in OpenTelemetry: What It Unlocks and How to Use It - Morgan McLean & Dan Jaglowski
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/introducing-logs-in-opentelemetry-what-it-unlocks-and-how-to-use-it/a1KZwfLr2PQ.txt
- Transcript chars: 39283
- Keywords: logs, collector, logging, metrics, traces, sampling, actually, trace, instrumentation, information, pretty, cemetry, capture, metadata, important, process, across, application

### Resumo baseado na transcript

hello everyone for those who are still getting seated there are still plenty of seats up front there's five amusing ones here but there's actually legitimately like more seats here so if you Shuffle forward you can actually find a place to sit so please do uh while you do that we'll introduce ourselves my name is Morgan mlan I'm a director of product management on Splunk I'm one of the co-founders of open cemetry I still spend a huge amount of my time on the project every single day

### Excerpt da transcript

hello everyone for those who are still getting seated there are still plenty of seats up front there's five amusing ones here but there's actually legitimately like more seats here so if you Shuffle forward you can actually find a place to sit so please do uh while you do that we'll introduce ourselves my name is Morgan mlan I'm a director of product management on Splunk I'm one of the co-founders of open cemetry I still spend a huge amount of my time on the project every single day I'm Dan jaglowski I'm a principal software developer at observe IQ and a maintainer of the open Telemetry collector I've been developing observability softare for for over a decade and contributing to open chemetry for the last 3 years or so and we're talking about logs today so open cemetry started 2019 we added traces then we added metrics uh today we made an announcement earlier today that we've added logs logs have actually been present in open Telemetry in some form for the last two two years roughly uh but a couple months ago things started actually reaching maturity and so we declared 1.0 for various components of logging in open cemetry so we had a big celebration this morning a big announcement about that but today at this session we actually get to dive into the details about what that means if you're not familiar with open slimmetry open slimmetry is a collection of tools apis and software development kits that are used to instrument generate and Export Telemetry data that help you analyze your software's performance and behavior and in Practical terms that actually means it captures traces and metrics and logs and other types of data from your applications and your infrastructure and it sends them to backends for storage and Analysis part of the Beauty from open cemetry is you can send that data to effectively anywhere you want which is very very nice gives you a lot of flexibility gives you ownership over your own data the most used component of open Telemetry there are many but probably the most popular is the open Telemetry collector this is typically deployed as an agent on each host so deployed on Windows or on Linux or deployed onto kubernetes clusters and The Collector does a couple things it captures logs which is what we're talking about today it also captures system metrics so host metrics CPU memory consumption things like that uh it also captures metrics from thirdparty applications you might be running databases message cues things where you didn't writ
