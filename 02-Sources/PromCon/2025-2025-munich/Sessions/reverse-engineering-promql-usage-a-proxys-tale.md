---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Visualization Dashboards", "Cost Optimization"]
speakers: ["Nicolas Takashi"]
source_url: https://promcon.io/2025-munich/talks/reverseengineering-promql-usage-a-proxys-tale/
youtube_url: https://www.youtube.com/watch?v=KKll20jb6aM
youtube_search_url: https://www.youtube.com/results?search_query=Reverse-Engineering+PromQL+Usage%3A+A+Proxy%E2%80%99s+Tale+PromCon+2025
video_match_score: 1.009
status: video-found
---

# Reverse-Engineering PromQL Usage: A Proxy’s Tale

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Cost Optimization]]
- Speakers: Nicolas Takashi
- Página oficial: https://promcon.io/2025-munich/talks/reverseengineering-promql-usage-a-proxys-tale/
- YouTube: https://www.youtube.com/watch?v=KKll20jb6aM

## Resumo

Prometheus provides you with metrics, but it doesn’t really explain how those metrics are being utilized. Which queries are lagging? Who’s running them?

## Abstract oficial

Prometheus provides you with metrics, but it doesn’t really explain how those metrics are being utilized. Which queries are lagging? Who’s running them? Which dashboards are bombarding the backend every 10 seconds? In many cases, it’s like trying to see into a black box. In this talk, I’ll dive into how we developed Prom Analytics Proxy to shed light on PromQL usage at scale, without needing to touch your Prometheus servers. I’ll take you through our technical journey: creating a low-overhead query proxy, monitoring metrics like latency, cardinality, and error rates, and organizing everything in a way that’s easy to query. You’ll find out what strategies worked, what didn’t go as planned, what caught us off guard, and how this initiative empowered teams to better understand and manage, how Prometheus is truly being utilized in production.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/reverseengineering-promql-usage-a-proxys-tale/
- YouTube: https://www.youtube.com/watch?v=KKll20jb6aM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KKll20jb6aM
- YouTube title: Promcon 2025 - Reverse-Engineering PromQL Usage: A Proxy’s Tale
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/reverse-engineering-promql-usage-a-proxys-tale/KKll20jb6aM.txt
- Transcript chars: 23810
- Keywords: queries, matrix, looking, expression, metric, running, metrics, question, questions, information, promql, pretty, already, understand, prometheus, getting, instance, context

### Resumo baseado na transcript

So how many of you already need to answer the question is like who is running this pretty expensive promo expression and breaking my monitoring system raise your hands yeah I think most of us right so let's try to understand how we can try to under like discover that because I've been this place few times now so who am I uh Nikos Takash first of all I'm Aonso's daddy, this cheeky little boy. uh we don't observe query age like we collect a bunch of data but we don't know how your users is using the data that we're collecting. query okay so you can get a lot of information about queries that being made through your promeus instance um queries from the recording rules engine and so on and you can get a lot of nice insights but like it you have some you You might have like many query instance ongoing and you can see and spotlight where what is the latence and so on. You you might need to understand if if you collect too much you might have lot of problems with data amount of data.

### Excerpt da transcript

[music] Yeah, let's go. Hello everyone. Um, good to be here. Uh, pretty excited, crowded room. Uh, little bit nervous as of course in the beginning of the talk. So, let's try to reverse engineering um like pro usage. So how many of you already need to answer the question is like who is running this pretty expensive promo expression and breaking my monitoring system raise your hands yeah I think most of us right so let's try to understand how we can try to under like discover that because I've been this place few times now so who am I uh Nikos Takash first of all I'm Aonso's daddy, this cheeky little boy. Uh, I'm a tech lead at Coral Logix. I'm doing like platform engineering and a lot of other things, but mostly focus on observability. Um, also maintainer from Prometheus operator and pers and contributing to different CNCF observability related projects like tennos, permitus, open telemetry and so on. Cool. So last year at PromCom I I gave a talk about unbreakable Promeus and how to make your permable Prometheus more predictable in terms of like memory consumption uh shape your your data and then so on.

Um and someone on the audience just raised a question say oh this is nice but there is yet another way to break your Prometheus. You can just have like pretty expensive queries going on. And that's true because if you have too many parallel queries, concurrent queries touching hundreds of samples, you will need a lot of memory. Okay, luckily Prometheus provides some limits to that. But this is not the the idea of today. I don't want to talk about limits. This resonates with me because I asked my I see myself needing to answer the same question that I I just asked you like how to identify those kind of things, right? uh we don't observe query age like we collect a bunch of data but we don't know how your users is using the data that we're collecting. We don't know the shape of the data. We don't know what are metrics being used and not used it. What are the common aggregations that people is doing on our system? How far in the past people is looking the data. Okay. So if we don't know all those things, we cannot optimize.

We cannot like answer those hard questions and hard moments. So first of all try to understand like how we can get in this kind of insights today. Okay. because we already have some some thing available like first of all we have Promeus quar log file for don't know the ones that don't know permit has a feature that allows you write into a
