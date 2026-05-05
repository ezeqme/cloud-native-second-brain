---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/yet-another-streaming-promql-engine/
youtube_url: https://www.youtube.com/watch?v=3kM2Asj6hcg
youtube_search_url: https://www.youtube.com/results?search_query=Yet+Another+Streaming+PromQL+Engine+PromCon+2023
video_match_score: 0.973
status: video-found
---

# Yet Another Streaming PromQL Engine

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/yet-another-streaming-promql-engine/
- YouTube: https://www.youtube.com/watch?v=3kM2Asj6hcg

## Resumo

Speaker(s): György Krajcsovits Mimir is great at ingesting enormous amounts of time series data. But we think it can be even better at querying enormous amounts of time series data. So we’ve been working to improve Mimir’s query performance and resource consumption, with the goal to evaluate queries faster while also reducing CPU utilisation and peak memory consumption.

## Abstract oficial

Speaker(s): György Krajcsovits

Mimir is great at ingesting enormous amounts of time series data. But we think it can be even better at querying enormous amounts of time series data. So we’ve been working to improve Mimir’s query performance and resource consumption, with the goal to evaluate queries faster while also reducing CPU utilisation and peak memory consumption.

One of the key ways we believe we can achieve this goal is with a streaming PromQL engine. We experimented with Thanos’ new streaming engine, which streams results one time step at a time, but found it couldn’t tick all the boxes we needed. So we’ve recently begun prototyping an alternative engine that instead streams by series, with promising early results.

In this talk, I’ll:


demonstrate our prototype PromQL engine that computes results over streams of series, and share our preliminary benchmark results, the lessons we’ve learnt so far, and what we plan to try next
compare the pros and cons of the prototype engine, Prometheus’ default PromQL engine and Thanos’ streaming PromQL engine
explain how Mimir’s other query optimisation techniques, such as streaming chunks and time splitting of queries, uniquely complement a PromQL engine that computes results over streams of series

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/yet-another-streaming-promql-engine/
- YouTube: https://www.youtube.com/watch?v=3kM2Asj6hcg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3kM2Asj6hcg
- YouTube title: PromCon 2023 - Yet Another Streaming PromQL Engine
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/yet-another-streaming-promql-engine/3kM2Asj6hcg.txt
- Transcript chars: 18411
- Keywords: series, memory, streaming, engine, actually, basically, mimir, already, loading, utilization, latency, number, question, running, looking, reduce, queries, splitting

### Resumo baseado na transcript

[Music] [Applause] um hi there my name is De kovich but everybody calls me cryo for obvious reasons uh and I work as a son uh software engineer at graph Labs uh I work on uh mimir and currently mainly on Native histogram support and I see people filtering in so I say few words about Native histograms first uh which is not the topic here but everybody talked about Native histograms so I feel like I should mention it that uh mimir also supports native histograms ingestion both through

### Excerpt da transcript

[Music] [Applause] um hi there my name is De kovich but everybody calls me cryo for obvious reasons uh and I work as a son uh software engineer at graph Labs uh I work on uh mimir and currently mainly on Native histogram support and I see people filtering in so I say few words about Native histograms first uh which is not the topic here but everybody talked about Native histograms so I feel like I should mention it that uh mimir also supports native histograms ingestion both through pritus remote right and uh OTP so you can send exponential histograms as well and you can try it out uh with mimir uh in graphon Cloud it's still in preview so you need to send the support TI but we can enable it and you can you can try it out but that's not the topic I we'll talk about yet another streaming pritus uh engine uh first uh few disclaimers actually this work is very very experimental it was done by one person who uh during a a week long hackaton uh at graphon olabs and uh actually that person wasn't me so uh it was done by Charles corn but unfortunately he couldn't make the uh conference so uh if there are some mistakes then it's probably me explaining it wrong all right so let's get into the the problem that we are trying to solve um so I'm going to talk about this problem in the context of mimir uh mimir for the purposes this of this talk is a a scalable microservices arure uh time series database built on promit it provides promit API compa and it's great at ingesting huge amounts of Time series uh we demonstrated that you can uh ingest one billion that's a billion with a B time series uh in a single cluster of mimir um however uh it could be a little bit better at acquiring uh huge amounts of data and in particular uh we'll look at uh component called quier uh which is the bit that actually houses the promql engine and uh this is a graph of uh the memory consumption uh versus time of our quers uh this is from an actual production cluster and you can see that there's kind of a steady state but there are like uh peaks of double the memory use of the steady state and uh this is kind of an issue uh because we are uh paying for the memory that uh the uh the maximum memory that we use so basically we are paying for the Peaks but uh we are actually not using uh that much memory all the time so that's kind of wasted and uh the worst part is that memory isn't really elastic so when you go over the the memory limits uh your P will be oom killed and uh in the best case th
