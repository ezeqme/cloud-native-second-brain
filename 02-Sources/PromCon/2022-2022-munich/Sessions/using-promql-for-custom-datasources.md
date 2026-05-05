---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/using-promql-for-custom-datasour/
youtube_url: https://www.youtube.com/watch?v=f_rHBUsf6AA
youtube_search_url: https://www.youtube.com/results?search_query=Using+PromQL+for+Custom+Datasources+PromCon+2022
video_match_score: 0.944
status: video-found
---

# Using PromQL for Custom Datasources

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/using-promql-for-custom-datasour/
- YouTube: https://www.youtube.com/watch?v=f_rHBUsf6AA

## Resumo

Speaker(s): Chris Marchbanks Have you wanted to use PromQL to analyze data that is not stored in Prometheus? Perhaps there is no way to scrape the data either, for example if it is not available for hours or may change. This talk will demonstrate how you can use Prometheus code to create a PromQL interface to any data you choose.

## Abstract oficial

Speaker(s): Chris Marchbanks

Have you wanted to use PromQL to analyze data that is not stored in Prometheus? Perhaps there is no way to scrape the data either, for example if it is not available for hours or may change. This talk will demonstrate how you can use Prometheus code to create a PromQL interface to any data you choose. A concrete example will be shown that queries data from Strava via PromQL.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/using-promql-for-custom-datasour/
- YouTube: https://www.youtube.com/watch?v=f_rHBUsf6AA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=f_rHBUsf6AA
- YouTube title: PromCon EU 2022: Using PromQL for Custom Datasources
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/using-promql-for-custom-datasources/f_rHBUsf6AA.txt
- Transcript chars: 15916
- Keywords: prometheus, actually, strava, series, custom, select, activities, create, return, iterator, promql, little, implement, samples, remote, interesting, queries, climbing

### Resumo baseado na transcript

[Music] foreign [Music] [Applause] so yeah so today I'm talking about using promql for custom data sources I've already had a couple of great talks about prom ql and queries this morning this is looking a bit more at the other side of instead of improving samples and that we're actually going to look at how we can get data back from any sort of data source you want and put it in a format that is available for promql to query so first off a bit about me I'm

### Excerpt da transcript

[Music] foreign [Music] [Applause] so yeah so today I'm talking about using promql for custom data sources I've already had a couple of great talks about prom ql and queries this morning this is looking a bit more at the other side of instead of improving samples and that we're actually going to look at how we can get data back from any sort of data source you want and put it in a format that is available for promql to query so first off a bit about me I'm a Prometheus maintainer for about three years now mainly focusing on remote right so the query side of Prometheus is a bit newer for me and I had a lot of fun learning about it I'm also working at grafana Labs on some of our machine learning projects and when I'm not at my desk you can find me out in the mountains of my home doing skiing hopefully very soon again climbing hiking things like that so what are some of the problems and motivation that I have for using promqql like at least two of you that I heard this morning I enjoy prom ql I'm also very familiar with it I use it every single day for running all of our systems and I want to use it to also explore data in other systems I'm show a quick demo in a little bit where I can look at some of my strav activity data with promql and just explore different visualizations that way we also as as part of the machine learning team we wanted the ability to use promql to actually query predictions into the future very similar to what Andrew at gitlab was doing yesterday we want to be able to display that data with promql um and we just found a lack of customizability in how we were managing to get data into existing Prometheus into mimir into Thanos anything like that and finally some of my motivation is just for fun and learning I like playing around with new tech and maybe there's cool things that you all want to visualize with prime ql as well so just a little bit about what are the sources of data that you can use to query with Prometheus today first is the most common direct instrumentation or an exporter Prometheus comes along scrapes that data it works for almost all of prometheus's core use cases but you can actually also do custom data with remote read remote read is typically used to retrieve data that was remote written to an external system for long-term storage or something like that but you don't need to do that first you can just Implement a remote read server that returns whatever you want and that can be used to do very interesting things lik
