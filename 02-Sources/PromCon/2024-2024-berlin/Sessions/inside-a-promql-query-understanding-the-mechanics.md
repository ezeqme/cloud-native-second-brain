---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: ["Bryan Boreham"]
source_url: https://promcon.io/2024-berlin/talks/inside-a-promql-query-understanding-the-mechanics/
youtube_url: https://www.youtube.com/watch?v=t53-7vUhbqY
youtube_search_url: https://www.youtube.com/results?search_query=Inside+a+PromQL+Query%3A+Understanding+the+Mechanics+PromCon+2024
video_match_score: 1.013
status: video-found
---

# Inside a PromQL Query: Understanding the Mechanics

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: Bryan Boreham
- Página oficial: https://promcon.io/2024-berlin/talks/inside-a-promql-query-understanding-the-mechanics/
- YouTube: https://www.youtube.com/watch?v=t53-7vUhbqY

## Resumo

Ever wondered what happens under the hood when you execute a PromQL query? Join us for a deep dive into the internals of Prometheus as we trace the data flow from its origin to its final destination at the API. In this session, we will explore: How selectors are looked up in the "postings" index, How samples are selected for instant and range queries, How functions take different types of input, The three different styles of aggregations, How operators join rows from different series, Final sorting and formatting into JSON This talk aims to equip Prometheus users with a deeper understanding of query efficiency.

## Abstract oficial

Ever wondered what happens under the hood when you execute a PromQL query? Join us for a deep dive into the internals of Prometheus as we trace the data flow from its origin to its final destination at the API.

In this session, we will explore:


How selectors are looked up in the "postings" index,
How samples are selected for instant and range queries,
How functions take different types of input,
The three different styles of aggregations,
How operators join rows from different series,
Final sorting and formatting into JSON


This talk aims to equip Prometheus users with a deeper understanding of query efficiency. We'll also highlight recent optimizations that have significantly improved query performance. Whether you're a seasoned user or just getting started, this session will provide valuable insights into making your PromQL queries more effective.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/inside-a-promql-query-understanding-the-mechanics/
- YouTube: https://www.youtube.com/watch?v=t53-7vUhbqY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t53-7vUhbqY
- YouTube title: PromCon 2024 - Inside a PromQL Query: Understanding the Mechanics
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/inside-a-promql-query-understanding-the-mechanics/t53-7vUhbqY.txt
- Transcript chars: 20073
- Keywords: series, promql, prometheus, points, labels, numbers, called, inside, function, always, pretty, engine, happens, status, number, looking, grafana, picture

### Resumo baseado na transcript

[Music] [Applause] hello um so yeah I'm going to talk about inside promql oh here we go right slides are up good um yeah so my name is Brian boram I work for grafana labs I have worked on Prometheus it's pretty much seven years to the day since my first PR on Prometheus and I am a maintainer um I committed to do this talk because every time I work inside the promql engine I have to figure it out from scratch it's it's pretty complicated um and uh

### Excerpt da transcript

[Music] [Applause] hello um so yeah I'm going to talk about inside promql oh here we go right slides are up good um yeah so my name is Brian boram I work for grafana labs I have worked on Prometheus it's pretty much seven years to the day since my first PR on Prometheus and I am a maintainer um I committed to do this talk because every time I work inside the promql engine I have to figure it out from scratch it's it's pretty complicated um and uh I thought you know someone should write this down um and so that's someone is me uh what happened is this is basically a 90-minute talk um but the slot is only 25 minutes incidentally if you could put the time remaining up that would be helpful I don't know if uh whoever did that yesterday um so uh yeah so the talk is going to be very very high level there will be a blog post um because I I've that is running about 12 Pages currently um so you can read all the detail anyway uh lot to get through let's get going um so this is the big picture uh this is what I'm going to be talking about I thought that's kind of a boring picture this is what we're this is what we're doing uh we have all the information we have all the data we are controlling the world with our dashboards we are uh in at the Nexus of the universe with full information uh but uh this this is the way the software Works um so we'll come back to uh to this picture a few times um let me see if I can uh yeah so we're going to start with the promql language it it goes through a parer creates this thing called a abstract syntax tree then we'll get very deep into the engine and how it interacts with storage and it produces results hopefully um so very high level promql as a query language is built up from a a series of building blocks uh selectors which fetch the raw data the metrics functions uh like abs and rate aggregations some Max things like that uh and operators and that's it it is nominally a a a pretty simple language um so just to take an example uh for the for the sake of illustration uh if I feed this into the promu AL parser I get a tree uh computer trees grow downwards from the root um the whole thing is driven by walking this tree when a promu query is executing inside the engine everything that happens happens by by walking uh down this tree kind of get to the the leaves of the tree fetch the data and then come up the tree compute things come up the tree compute things there is no query planner nothing happens in a different order to the way y
