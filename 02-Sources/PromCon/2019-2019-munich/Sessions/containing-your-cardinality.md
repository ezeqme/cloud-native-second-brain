---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Cost Optimization", "Community"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/containing-your-cardinality/
youtube_url: https://www.youtube.com/watch?v=49BGvC1coG4
youtube_search_url: https://www.youtube.com/results?search_query=Containing+Your+Cardinality+PromCon+2019
video_match_score: 0.901
status: video-found
---

# Containing Your Cardinality

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Cost Optimization]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/containing-your-cardinality/
- YouTube: https://www.youtube.com/watch?v=49BGvC1coG4

## Resumo

Speaker: Chris Marchbanks Spending time in the Prometheus community quickly instills a fear of high cardinality metrics; however, cardinality provides immense value for certain workloads. Learn when to use high cardinality metrics, how to reduce unnecessary cardinality, and how to find the sources of excessive cardinality in your data. Video link - Slides

## Abstract oficial

Speaker: Chris Marchbanks

Spending time in the Prometheus community quickly instills a fear of high cardinality metrics; however, cardinality provides immense value for certain workloads. Learn when to use high cardinality metrics, how to reduce unnecessary cardinality, and how to find the sources of excessive cardinality in your data.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/containing-your-cardinality/
- YouTube: https://www.youtube.com/watch?v=49BGvC1coG4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=49BGvC1coG4
- YouTube title: PromCon EU 2019: Containing Your Cardinality
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/containing-your-cardinality/49BGvC1coG4.txt
- Transcript chars: 18526
- Keywords: prometheus, series, cardinality, actually, metrics, carnality, metric, pretty, single, number, memory, queries, buckets, histogram, operational, finally, hundred, instances

### Resumo baseado na transcript

[Music] hello everyone Brian said I'm Chris talking about something that I've been working struggling with possibly a lot over the last few months which is containing our cardinality in for me yes so a bit about me I don't know why this is being weird yeah so as Brian said I'm engineer at spunk we work on the internal observability platform for splint cloud providing something similar to the last presentation so that was super neat to see also the most recent newest team member prometheus which I'm very

### Excerpt da transcript

[Music] hello everyone Brian said I'm Chris talking about something that I've been working struggling with possibly a lot over the last few months which is containing our cardinality in for me yes so a bit about me I don't know why this is being weird yeah so as Brian said I'm engineer at spunk we work on the internal observability platform for splint cloud providing something similar to the last presentation so that was super neat to see also the most recent newest team member prometheus which I'm very excited about just having a great time working with this community and giving back we do all things observability step tracing metrics all that stuff it's all super exciting and I love uphill skiing on the weekends get away from lift lines pretty great I recommend it get a good workout in so yeah so first questions who is concerned about cardinality in their system that is a lot of people me too so next off who has seen this warning I wish I could figure out was up with that on the Prometheus Docs it's a good one it provides some decent information don't store things like user IDs email addresses unbounded sets of data yeah definitely avoid that but what about if you're running a multi-tenant system what about things like tenon ID is that okay is it not there's there's a lot of fuzzy areas and even if you do avoid all of this I've been in situations where I have hundreds of thousands of individual series for one metric so what can you do about that that's what I'm hoping to address today so what is cardinality so for this talk I really define it as the number of series held in Prometheus over a given timeframe typically that is at least okay at least how long sort of series are in memory for that's the at least two three hours something like that contributes a lot to the memory uses of Prometheus it's up to however long you commonly do queries for maybe you do queries that are a week long you should kind of consider how many series will be in that week-long query oh and then a few different sources of cardinality targets series on a target and then also just how those change over time so if you're running kubernetes something like that targets are constantly coming up and down that adds a lot to cardinality that isn't necessarily reflected at any one point in time and finally carnality is valuable like yes it's kind of a scary thing but it's incredibly valuable and things you can do with it are amazing but yes excessive carnality is expensive so how does ca
