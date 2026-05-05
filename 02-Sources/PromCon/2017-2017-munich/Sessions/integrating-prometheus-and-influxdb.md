---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/integrating-prometheus-and-influxdb/
youtube_url: https://www.youtube.com/watch?v=BZkHlhautGk
youtube_search_url: https://www.youtube.com/results?search_query=Integrating+Prometheus+and+InfluxDB+PromCon+2017
video_match_score: 0.891
status: video-found
---

# Integrating Prometheus and InfluxDB

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/integrating-prometheus-and-influxdb/
- YouTube: https://www.youtube.com/watch?v=BZkHlhautGk

## Resumo

Speaker: Paul Dix This talk will look at the different integrations between InfluxDB and Prometheus. We'll dive into using InfluxDB for remote long term storage. Other examples will show how to use Kapacitor to scrape Prometheus metrics targets to pull data into InfluxDB and transform it on the fly to different schemas.

## Abstract oficial

Speaker: Paul Dix

This talk will look at the different integrations between InfluxDB and Prometheus. We'll dive into using InfluxDB for remote long term storage. Other examples will show how to use Kapacitor to scrape Prometheus metrics targets to pull data into InfluxDB and transform it on the fly to different schemas. Finally, we'll take a look at the upcoming enhancements to the Influx Query Language and possible implementation of PromQL within Influx itself for better long term integration of the two projects.



Video link

## Links

- Página oficial: https://promcon.io/2017-munich/talks/integrating-prometheus-and-influxdb/
- YouTube: https://www.youtube.com/watch?v=BZkHlhautGk
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BZkHlhautGk
- YouTube title: PromCon 2017: Integrating Prometheus and InfluxDB - Paul Dix
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/integrating-prometheus-and-influxdb/BZkHlhautGk.txt
- Transcript chars: 20570
- Keywords: prometheus, basically, remote, actually, influx, language, series, storage, gateway, underscore, support, metric, engine, write, working, metrics, server, format

### Resumo baseado na transcript

[Music] in folks TV is a system which is often compared to Regis there are similarities I think we're both of the Turkish virtual restorer gingival yeah yeah about to launch it or something and you know it turns out that in folks started like a few insan for previous we know Infosys the better system because it has 172 more stars ok so right now we're talking about integrating influx I'm Prometheus thanks all right hey everybody uh so yeah this is my talk about influx to be in

### Excerpt da transcript

[Music] in folks TV is a system which is often compared to Regis there are similarities I think we're both of the Turkish virtual restorer gingival yeah yeah about to launch it or something and you know it turns out that in folks started like a few insan for previous we know Infosys the better system because it has 172 more stars ok so right now we're talking about integrating influx I'm Prometheus thanks all right hey everybody uh so yeah this is my talk about influx to be in Prometheus I'll cover a little bit about what exists now this is mostly thanks to the efforts of the Prometheus team Julius in particular but I'm also going to close with where we see the future of things like moving so just as an intro in case you don't know influx DB is an open source time series database we say time series instead of just metrics in my mind metrics are a subset of time-series metrics our samples have fixed intervals whereas in my mind a time series could be irregular time series data of like trades in a stock market or individual requests to an API not just summarizations so a little bit about influx QB it's open source it's MIT licensed it's written and go it has a query language that looks kind of like SQL we as Brian mentioned we're on our third version of our storage engine we rewrote the storage engine from scratch starting in the fall of 2015 we call it a time series merge tree it's heavily inspired by LS m trees and leveldb but it's specific to our use case and also actually we have an inverted index as well those bits are available for preview right now they're going in by default in the next release so it's basically an on disk inverted index for looking up time series and stuff and then obviously we have wear company so we have a commercial offering which offers high availability and scale out closer so the data model looks like this you have a measurement name which is a string you have tags so the measurement name is kind of like a metric in Prometheus you have tags which are key value pairs which are like Prometheus labels unlike Prometheus you then have fields which is just key value pairs you have the field identifier and then the value and then you have a nanosecond scale epoch which is again different than Prometheus which stores at the millisecond precision we support more than just float 64's we have float 64 in 64 boolean's and string types and we're adding U n 64 in the next release so a query looks like this basically we're getting the 90th p
