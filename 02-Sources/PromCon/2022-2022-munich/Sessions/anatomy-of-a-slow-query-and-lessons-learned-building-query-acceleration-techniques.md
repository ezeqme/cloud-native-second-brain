---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability", "Visualization Dashboards", "Community"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/anatomy-of-a-slow-query-and-less/
youtube_url: https://www.youtube.com/watch?v=t9dw698NMvs
youtube_search_url: https://www.youtube.com/results?search_query=Anatomy+of+a+Slow+Query%2C+and+Lessons+Learned+Building+Query+Acceleration+Techniques+PromCon+2022
video_match_score: 1.041
status: video-found
---

# Anatomy of a Slow Query, and Lessons Learned Building Query Acceleration Techniques

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/anatomy-of-a-slow-query-and-less/
- YouTube: https://www.youtube.com/watch?v=t9dw698NMvs

## Resumo

Speaker(s): Susana Ferreira & Marco Pracucci Have you ever experienced a slow query and wondered how it could be accelerated? This talk is for you! In this presentation, Susana and Marco, Open Source contributors from Grafana Labs, will dissect the anatomy of a slow query, and walk through the execution steps from when you click “Run query” until you get the query result.

## Abstract oficial

Speaker(s): Susana Ferreira & Marco Pracucci

Have you ever experienced a slow query and wondered how it could be accelerated? This talk is for you!

In this presentation, Susana and Marco, Open Source contributors from Grafana Labs, will dissect the anatomy of a slow query, and walk through the execution steps from when you click “Run query” until you get the query result.

We’ll then explore the options to speed up a query in Prometheus and the acceleration techniques adopted by Grafana Mimir, like query results caching, query sharding by time and series, and storage sharding. We’ll share our lessons learned, including successes and failures, for the benefit of the Prometheus community.

Finally, we’ll share further ideas on additional techniques Prometheus and Prometheus-compatible systems could adopt to further speed up the queries execution, like a query planner and query optimizer.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/anatomy-of-a-slow-query-and-less/
- YouTube: https://www.youtube.com/watch?v=t9dw698NMvs
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t9dw698NMvs
- YouTube title: PromCon EU 2022: Anatomy of a Slow Query, and Lessons Learned Building Query Acceleration Techniques
- Match score: 1.041
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/anatomy-of-a-slow-query-and-lessons-learned-building-query-acceleratio/t9dw698NMvs.txt
- Transcript chars: 23461
- Keywords: queries, samples, series, partial, process, number, matching, actually, basically, interval, prometheus, techniques, instant, result, results, sample, minutes, multiple

### Resumo baseado na transcript

[Music] foreign [Music] [Applause] So today we're going to talk about slow queries and in particular we would like to share with you some lessons learned building some query acceleration techniques shared between Griffin Mir and Thanos my name is Marco I'm a software engineer at graphene labs hello my name is Susanna also a software engineer at grafana now this topic is not new actually three years ago Tom was on the stage of kubecon North America to present what I think at that time was the first queer to keep in mind uh when you're going to run your next range query so in uh it's actually very easy to write hyperdenality queries so as you see queries that can touch over billions of samples and we as users expect these results to so you have thousands of queries to run I mean it would be even way slower than just running the query as is without any optimization at all um so we we dynamically compute the number of shards to use based on right now based on the time range of the query and the portion of the query which have not been cached yet so if you run a query I don't know over the last three days and the last two days of query are actually picked up from the cache the LA we have just run the last one day of query so we can run at full parallelization um with the query chart but if the last three days of queries um are not cached we reduce the number of shards for

### Excerpt da transcript

[Music] foreign [Music] [Applause] So today we're going to talk about slow queries and in particular we would like to share with you some lessons learned building some query acceleration techniques shared between Griffin Mir and Thanos my name is Marco I'm a software engineer at graphene labs hello my name is Susanna also a software engineer at grafana now this topic is not new actually three years ago Tom was on the stage of kubecon North America to present what I think at that time was the first queer acceleration technique in cortex which is the range query time splitting we will share in details later on how it works and this talk is a sort of follow-up so you know fast forwarding two years later what's the current state of the queer acceleration techniques we use in systems like grafanimir Thanos and cortex as well now to understand these techniques first of all we have to understand why a query could be slow and this talk is intentionally oversimplified we just want to focus on the key Concepts and we are just going to focus on one single query what's probably the most common query the sum rate of a metric so when we run a query in Prometheus graphene or Thanos the first step is always to parse the query and in particular we want to find all the instant orange Vector selectors so in this case for this query we have the range Vector selector metric namespace SQL app then given our range Vector selector we want to get our label measures in order to find all the matching series all the series matching these labeled matches so the way this is lookup in storage is first we will look up all the series matching name equal metric then all the series matching namespace equal app we intersect the two sets and the result of the intersection will be our matching series then for each of our matching series we want to fetch the samples within the queries time range so in this case our samples will be our data points our value timestamp pairs such as we have here uh once we fetch all of our samples we will process them so we will run the query in this case we will run the sum rate over all the samples of our matching series and just to note that this process is done sequentially because from ql The Prompt QR engine is single threaded once the query completed we can send the result back to the client which can be grafana or princess of Prometheus UI where is the time actually spent you know in this process well the answer is it depends it depends on the query you ru
