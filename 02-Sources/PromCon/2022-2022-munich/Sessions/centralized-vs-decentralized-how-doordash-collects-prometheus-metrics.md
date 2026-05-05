---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/centralized-vs-decentralized---h/
youtube_url: https://www.youtube.com/watch?v=Kj3SEudIshQ
youtube_search_url: https://www.youtube.com/results?search_query=Centralized+vs.+Decentralized+-+How+DoorDash+Collects+Prometheus+Metrics+PromCon+2022
video_match_score: 1.026
status: video-found
---

# Centralized vs. Decentralized - How DoorDash Collects Prometheus Metrics

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/centralized-vs-decentralized---h/
- YouTube: https://www.youtube.com/watch?v=Kj3SEudIshQ

## Resumo

Speaker(s): Eric D. Schabell & Emma (Qixuan) Wang There are two primary approaches to scrape and collect metrics using Prometheus - using a centralized set of dedicated scrapers or decentralized scrapers that run as an agent. With centralized scraping, Prometheus is deployed as a central scraper to pull metrics from all discoverable endpoints and sometimes can be split across multiple centralized instances using a few different approaches.

## Abstract oficial

Speaker(s): Eric D. Schabell & Emma (Qixuan) Wang

There are two primary approaches to scrape and collect metrics using Prometheus - using a centralized set of dedicated scrapers or decentralized scrapers that run as an agent. With centralized scraping, Prometheus is deployed as a central scraper to pull metrics from all discoverable endpoints and sometimes can be split across multiple centralized instances using a few different approaches. However, with a decentralized approach, Prometheus runs as an agent, in Kubernetes is deployed as a DaemonSet on each node in a cluster, and only collects metrics from the node it runs on. Each model has pros and cons - especially when operating at large scale - which can make it difficult when deciding which model to use. 

In this session, Emma and Eric will provide an overview of Prometheus metrics collection at DoorDash, where having highly reliable resources, easy endpoint discovery, and real-time insights is critical. They will share insights and best practices into DoorDash’s decision to implement a decentralized model by offering pros and cons of each approach. Leave with a better understanding of the “right” model for your use case(s).

## Links

- Página oficial: https://promcon.io/2022-munich/talks/centralized-vs-decentralized---h/
- YouTube: https://www.youtube.com/watch?v=Kj3SEudIshQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Kj3SEudIshQ
- YouTube title: PromCon EU 2022: Centralized vs. Decentralized - How DoorDash Collects Prometheus Metrics
- Match score: 1.026
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/centralized-vs-decentralized-how-doordash-collects-prometheus-metrics/Kj3SEudIshQ.txt
- Transcript chars: 19330
- Keywords: actually, pretty, little, decentralized, collectors, collection, deployment, prometheus, approach, obviously, doordash, metrics, interesting, collect, thousands, collector, centralized, points

### Resumo baseado na transcript

[Music] foreign [Music] on this the idea was initially that we'd have the customer here but there was some family things that came up uh one of which was uh the speaker having a baby so fair enough right um so what we wanted to turn this into uh as a second best uh offer is I brought in my friend aless here who works very closely with the customer has intimate knowledge with the what they're doing their solution and was also at kubecon a couple weeks ago anybody

### Excerpt da transcript

[Music] foreign [Music] on this the idea was initially that we'd have the customer here but there was some family things that came up uh one of which was uh the speaker having a baby so fair enough right um so what we wanted to turn this into uh as a second best uh offer is I brought in my friend aless here who works very closely with the customer has intimate knowledge with the what they're doing their solution and was also at kubecon a couple weeks ago anybody here was at kubecon in the states couple okay this talk was given there together with another colleague from uh doordash and uh is recorded if you want to take a look at it but we thought it'd be nice to bring this over here and share it with you because it's a really interesting uh story so let's kick this off so we can get back on track my name is Eric D schvel um I work with chronosphere as uh the director of evangelism and this is alesh he's one of our sales Engineers who works very closely with a doordash among other customers so it should be really really interesting insights uh into what's going on go ahead and hit the next one so how many people here know what a data point is and this is more a check just to see if you're awake right any hands going up yeah so there's a little metaphor here just to build the story up to understand where we're coming from right so it's it's kind of nice you think about out there somewhere our flowers and there's a way to get to these data points in a timely fashion to scrape them to bring that back to next to bring that all the way back to and next again to The Hive where we're collecting all these things like bees right this is Prometheus in a nutshell right it's not not really exciting other than that you have to think about the data at the endpoints being most valuable when it's fresh and less valuable when it gets really old and there might be some disagreement from the from the presentation that you saw previously where they're talking about the out of order data where you want to go back and Aggregate and look at some of that old data then it has value again but ideally we want to be able to collect this data as fresh as possible get it into our systems and deal with this this is all fine when we're talking about one instance of scraping but when it starts getting into the thousands the ten thousands or even hundreds of thousands of scraping points it gets really interesting how this goes there's a couple of ways to look at it and that's what this talk
