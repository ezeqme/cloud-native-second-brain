---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Cost Optimization", "Community"]
speakers: ["Roman Khavronenko"]
source_url: https://promcon.io/2024-berlin/talks/aggregating-metrics-inflight-challenges-and-opportunities/
youtube_url: https://www.youtube.com/watch?v=AUGHrn3mjN4
youtube_search_url: https://www.youtube.com/results?search_query=Aggregating+metrics+in-flight%3A+challenges+and+opportunities+PromCon+2024
video_match_score: 1.029
status: video-found
---

# Aggregating metrics in-flight: challenges and opportunities

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Cost Optimization]], [[Community]]
- Speakers: Roman Khavronenko
- Página oficial: https://promcon.io/2024-berlin/talks/aggregating-metrics-inflight-challenges-and-opportunities/
- YouTube: https://www.youtube.com/watch?v=AUGHrn3mjN4

## Resumo

One of the common practices for improving the query speed in Prometheus is to create recording rules for commonly used queries. While this usually works great, recording rules have a cost: The raw metrics still need to be stored in the Prometheus, even if we don't need them Recording rule needs to be executed on interval basis, putting extra pressure on the Prometheus Adding a recording rule always means storing&processing more data But what if we could do the pre-aggregation before metrics get into the Prometheus? Can we aggregate on scrape time?

## Abstract oficial

One of the common practices for improving the query speed in Prometheus is to create recording rules for commonly used queries. While this usually works great, recording rules have a cost:


The raw metrics still need to be stored in the Prometheus, even if we don't need them
Recording rule needs to be executed on interval basis, putting extra pressure on the Prometheus
Adding a recording rule always means storing&processing more data


But what if we could do the pre-aggregation before metrics get into the Prometheus? Can we aggregate on scrape time? Or could clients do the aggregation before pushing data to Prometheus? At VictoriaMetrics we already started working on something we call Stream Aggregation. An ability for metrics collector to perform in-memory aggregations before forwarding data elsewhere (Prometheus including). It has many challenges related to time series nature of aggregated samples, network delays, horizontal scaling, etc. I'd like to share our experience with the community, as this may be a life-quality improving feature.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/aggregating-metrics-inflight-challenges-and-opportunities/
- YouTube: https://www.youtube.com/watch?v=AUGHrn3mjN4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AUGHrn3mjN4
- YouTube title: PromCon 2024 - Aggregating metrics in-flight: challenges and opportunities
- Match score: 1.029
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/aggregating-metrics-in-flight-challenges-and-opportunities/AUGHrn3mjN4.txt
- Transcript chars: 28457
- Keywords: series, aggregation, stream, labels, cardinality, database, pritus, interval, recording, metric, memory, aggregate, unique, samples, second, result, metrics, results

### Resumo baseado na transcript

[Music] um hello everyone and welcome to my talk and uh thanks for pritus Community for giving me uh this opportunity and I'm pretty excited to be here and my talk will be about aggregating metrics in flight so my name is Raman and I'm software engineer and last couple of years I'm working on the observability project called Victoria metric it's open source project uh similar to what pritus does and it has the similar application areas like it can be used for application performance monitoring for infrastructure monitoring

### Excerpt da transcript

[Music] um hello everyone and welcome to my talk and uh thanks for pritus Community for giving me uh this opportunity and I'm pretty excited to be here and my talk will be about aggregating metrics in flight so my name is Raman and I'm software engineer and last couple of years I'm working on the observability project called Victoria metric it's open source project uh similar to what pritus does and it has the similar application areas like it can be used for application performance monitoring for infrastructure monitoring from for collecting metrics from kubernetes deployments Etc and uh as for meus it also shares the same kind of problems and uh vulnerabilities as as as many as any other database time series database that I know so in order to engage the conversation with you um I have a quick question how do you guys deal with high cardinality issues yeah I I didn't expect the quick answer on this this is of course complete uh very complex topic so uh let's start from the basics what is cardinality that's basically the number of unique time series that you store in the database what is high cardinality it's when your database starts to becom slow or even unreliable why High cardinality matters because if your database is slow uh it means it's not it is not reliable anymore you can't uh have a critical pass depending on this monitoring solution so you either need to do something with the data or pay extra money to add more and more and more Hardware to deal with the high cardinality and uh if you try to Google uh what to do with the high cardinality you will probably find a bunch of Articles and they will suggest in the same um the same steps and the same actions to take so they will recommend you that you need to find the source of high cardinality metrics assuming that all of your sources are okay and only one of them is exposing High cardinality data so you need to find it and you need to optimize it and what are the optimization steps well you can use relabeling that's the prous native feature you can um drop some serious uh which you think are have high cardinality or you can drop some labels which contribute to cardinality this is cool protective approach to do this but the problem with that that when you drop in the metric uh the time series you're losing the information it brings so maybe you needed that information but you're dropping it and what is even worse you can drop the high grity label and if you know the unique label value pairs is what
