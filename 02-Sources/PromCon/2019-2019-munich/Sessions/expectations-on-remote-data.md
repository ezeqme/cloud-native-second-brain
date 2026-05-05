---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/expectations-on-remote-data/
youtube_url: https://www.youtube.com/watch?v=_asWX7RL2mg
youtube_search_url: https://www.youtube.com/results?search_query=Expectations+on+Remote+Data+PromCon+2019
video_match_score: 0.901
status: video-found
---

# Expectations on Remote Data

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/expectations-on-remote-data/
- YouTube: https://www.youtube.com/watch?v=_asWX7RL2mg

## Resumo

Speaker: Alfred Landrum Prometheus's remote storage API allows PromQL evaluation to work with stores other than TSDB, and with data that may not have originated via native Prometheus scraping. PromQL has expectations about the data served by the API, which must be met in order to give a "compatible" user experience with native Prometheus. I'll present my teams experience marrying an existing distributed time series database, originally designed around storing downsampled statsd-style metrics, with a PromQL evaluation engine.

## Abstract oficial

Speaker: Alfred Landrum

Prometheus's remote storage API allows PromQL evaluation to work with stores other than TSDB, and with data that may not have originated via native Prometheus scraping. PromQL has expectations about the data served by the API, which must be met in order to give a "compatible" user experience with native Prometheus. I'll present my teams experience marrying an existing distributed time series database, originally designed around storing downsampled statsd-style metrics, with a PromQL evaluation engine. I'll cover topics including: downsampling, counter aggregation, series staleness, and others. 



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/expectations-on-remote-data/
- YouTube: https://www.youtube.com/watch?v=_asWX7RL2mg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_asWX7RL2mg
- YouTube title: PromCon EU 2019: Expectations on Remote Data
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/expectations-on-remote-data/_asWX7RL2mg.txt
- Transcript chars: 19744
- Keywords: prompt, prometheus, difference, series, events, actually, samples, values, sample, evaluation, storage, aggregation, resets, queries, minutes, occurred, request, called

### Resumo baseado na transcript

[Music] hi all right I know it's been a long day the presentations have been great I also am suffering a little bit from jet lag so I'm trying to get myself up a bit here to make sure that I'm gonna do justice to the material so I'm an engineer at sisty egg if you haven't heard of us we make a security and monitoring platform and our tagline is that our goal is to help users confidently run cloud native workloads so recently myself and it's a few

### Excerpt da transcript

[Music] hi all right I know it's been a long day the presentations have been great I also am suffering a little bit from jet lag so I'm trying to get myself up a bit here to make sure that I'm gonna do justice to the material so I'm an engineer at sisty egg if you haven't heard of us we make a security and monitoring platform and our tagline is that our goal is to help users confidently run cloud native workloads so recently myself and it's a few engineers that are here have been working to add support for prom ql into our existing monitoring platform and I wanted to share a little bit about what we've learned about prompt well and the Prometheus data model and supporting the Prometheus remote read API so I need to give you a little bit of information about the system there we go so so assistance monitoring platform looks like this we have a software agent that runs on a host and a gathers date about this system and about the processes and containers that run on the system and then include system level info like CPU usage and memory usage but we also collect metrics from any applications that are running there and that includes JMX stat Z and of course Prometheus well the agent gathers this data and then pushes it up to our back in and we gather data roughly every 10 seconds we typically push it up to the back and immediately after we gather it so in our back end it's stored there both in the original form that we collected but we also down sample the data to make large queries more efficient so in our back in then users can view in slice that data in lots of different ways per cluster per deployment we do things like supporting our backs so if you're a user you have a very specific interest slice of the infrastructure that you could look at it any kind of time so we have a lot of features and we have like customers that like what we do however what we can't do today is that we can't perform arbitrary math operations on the data so hence that's why we wanted to add prompt well support and specifically we wanted to support the Prometheus HTTP API so that in our own UI inside the Cystic you we can make calls to that API but also our customers can use other visualization tools like Ravana and that API will connect to a prompt ul engine that uses the prom cue evaluation code from Prometheus the prom cue evaluation engine that we have named the prom cue later will talk with our data store via the remote read API so let's look at some examples of what prompt to
