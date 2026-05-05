---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/using-the-flux-query-engine-to-query-multiple-prometheus-servers/
youtube_url: https://www.youtube.com/watch?v=yO2X6oNba6k
youtube_search_url: https://www.youtube.com/results?search_query=Using+the+Flux+Query+Engine+to+Query+Multiple+Prometheus+Servers+PromCon+2018
video_match_score: 1.038
status: video-found
---

# Using the Flux Query Engine to Query Multiple Prometheus Servers

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/using-the-flux-query-engine-to-query-multiple-prometheus-servers/
- YouTube: https://www.youtube.com/watch?v=yO2X6oNba6k

## Resumo

Speaker: Paul Dix The new open source Flux query engine for InfluxDB is designed to be decoupled from storage. This makes it possible to query many different data sources, including Prometheus, with the new engine. The engine also decouples the representation of the query language from the execution representation.

## Abstract oficial

Speaker: Paul Dix

The new open source Flux query engine for InfluxDB is designed to be decoupled from storage. This makes it possible to query many different data sources, including Prometheus, with the new engine. The engine also decouples the representation of the query language from the execution representation. This makes it possible to add support for additional languages, like PromQL.

This talk will show how we've added support to the Flux engine to query multiple Prometheus servers at the same time, combining their results. This makes it trivial to query across a federated setup for scaling out the query. We'll also show how to query across two Prometheus servers configured for high availability, while guaranteeing a consistent query result.

We'll close out the talk by looking at how PromQL support is being added to the new engine. This will enable PromQL queries across a distributed system where the individual Prometheus and storage servers maintain their shared-nothing non-clustered failure modes.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/using-the-flux-query-engine-to-query-multiple-prometheus-servers/
- YouTube: https://www.youtube.com/watch?v=yO2X6oNba6k
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yO2X6oNba6k
- YouTube title: PromCon 2018: Using the Flux Query Engine to Query Multiple Prometheus Servers
- Match score: 1.038
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/using-the-flux-query-engine-to-query-multiple-prometheus-servers/yO2X6oNba6k.txt
- Transcript chars: 27382
- Keywords: prometheus, flux, basically, actually, language, tables, function, window, results, engine, thought, interesting, underscore, aggregate, result, saying, stream, whatever

### Resumo baseado na transcript

hey everybody alright uh so yeah I'm Paul Dix I'm the founder and CTO of influx data we are the makers of influx DB so this talk is quite a bit about flux which is a new language that we're building it started as a query language it was called previously I fql it has since been renamed because of a couple of things one it's no longer a query language and two it's no longer tied to M flux TB specifically so right now I'm thinking of it more

### Excerpt da transcript

hey everybody alright uh so yeah I'm Paul Dix I'm the founder and CTO of influx data we are the makers of influx DB so this talk is quite a bit about flux which is a new language that we're building it started as a query language it was called previously I fql it has since been renamed because of a couple of things one it's no longer a query language and two it's no longer tied to M flux TB specifically so right now I'm thinking of it more as like a data scripting language it will be turning complete you could write programs in it but we're scoping it to focus specifically on working with data it's functional in style all the code is MIT licensed and this applies not only to the language itself so the spec is is out there it's open source it's public but also the runtime and the engine that we're building all written in go so as most of you are probably Prometheus users I thought you know your question we so what I don't really care this has nothing to do with me and when I first proposed this talk there were a couple of things I thought might be interesting to this crowd one was I was thinking about high availability right if you could query multiple Prometheus servers in one engine you could engineer some sort of high availability thing that would be kind of cool and the thing is as I started writing code for this I was like okay there are far easier ways to create a high availability Prometheus set up that hits your requirements than this so I kind of scrapped that and then I thought okay well what about sharded data you have separate Prometheus servers running in different data centers and you could use this engine to combine that data and then I thought well actually and and this is my intuition I don't know if this is actually true but my thought was for most people that have sharded data with Prometheus they actually combined the data in graph on ax right they have multiple data sources and they graph it in their graphs and they can see it but they actually they rarely have need to query and process those pieces of data together as one cohesive unit so I thought okay well that's not very interesting although I will show that later uh and then maybe Federation but again I came back to this situation where I think most people show it in graph on ax so I went back to the drawing board and I thought okay what what can I say or what can I do that would be interesting for this crowd and I went to the Prometheus repo and I thought okay I'll look at issues
