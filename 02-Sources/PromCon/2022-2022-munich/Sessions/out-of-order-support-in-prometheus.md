---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/out-of-order-support-in-promethe/
youtube_url: https://www.youtube.com/watch?v=qYsycK3nTSQ
youtube_search_url: https://www.youtube.com/results?search_query=Out+Of+Order+Support+in+Prometheus+PromCon+2022
video_match_score: 0.94
status: video-found
---

# Out Of Order Support in Prometheus

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/out-of-order-support-in-promethe/
- YouTube: https://www.youtube.com/watch?v=qYsycK3nTSQ

## Resumo

Speaker(s): Jesús Vázquez & Ganesh Vernekar Until Prometheus v2.38.0, Prometheus’ TSDB only accepted in-order samples if they were less than 1 hour old, discarding everything else. As Prometheus continues to be adopted in new fields this poses an increasingly hard problem. Several use cases need out-of-order support, for example: IoT devices waking up asynchronously and writing metrics complex metric delivery architectures using message buses like Kafka with randomized sharding and delay due to congestion standalone Prometheus instances isolated from a network connection for some time trying to push old samples.

## Abstract oficial

Speaker(s): Jesús Vázquez & Ganesh Vernekar

Until Prometheus v2.38.0, Prometheus’ TSDB only accepted in-order samples if they were less than 1 hour old, discarding everything else. As Prometheus continues to be adopted in new fields this poses an increasingly hard problem. Several use cases need out-of-order support, for example:


IoT devices waking up asynchronously and writing metrics
complex metric delivery architectures using message buses like Kafka with randomized sharding and delay due to congestion
standalone Prometheus instances isolated from a network connection for some time trying to push old samples.


Prometheus v2.39.0 comes with support for ingesting out of order samples up to a configurable time limit.

We will talk about how we designed the new system, challenges faced while extending Prometheus TSDB, interesting decisions such as adding a new “Write Behind Log” instead of reusing the traditional Write Ahead Log, etc.

We will also share our experience running this in production with millions of series at Grafana Labs and the performance characteristics at scale.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/out-of-order-support-in-promethe/
- YouTube: https://www.youtube.com/watch?v=qYsycK3nTSQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qYsycK3nTSQ
- YouTube title: PromCon EU 2022: Out Of Order Support in Prometheus
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/out-of-order-support-in-prometheus/qYsycK3nTSQ.txt
- Transcript chars: 26290
- Keywords: out-of-order, samples, sample, prometheus, write, series, in-order, blocks, little, ingest, experimental, future, perhaps, another, memory, compaction, always, reader

### Resumo baseado na transcript

Um so today we're going to talk about out of order support in Prometheus, um how we originally designed it and then implemented it. Um we should mention also that it was not only Ganesh and myself, but also Dieter Pletnik, which is not with us today. That is out of order for Prometheus and that is what we're trying to solve here. Um well, I think uh we should recapitulate a little bit and we should think that uh Prometheus has started with its pull-based approach and in that context, you you only went to your services to scrape for samples every um few seconds. But you know, as things move along um and things will scale up uh the architectures get trickier and many people in this room is managing clusters today where we not only have a single TSDB, but we have sets of of TSDBs writing into other TSDBs. And so it batches up the metrics it has and then suddenly the network comes in and you start sending everything, uh but because not all machines come at the same time, like you can run into into out of order.

### Excerpt da transcript

Um hello everyone. Um so today we're going to talk about out of order support in Prometheus, um how we originally designed it and then implemented it. Um we should mention also that it was not only Ganesh and myself, but also Dieter Pletnik, which is not with us today. Um so first thing, um round of introductions. Um so my name is Jesus Watke, I work at Grafana Labs right now as a software engineer. I have a past as uh devops / uh SRE / platform engineer um and a bit of software development, but for the past 2 years I've been exclusively working as a software engineer at Grafana. Um I work on the uh query squad, which is very close to Mimir. We do kind of do Mimir proxies, which are also open source. They are little components that sit on top of Mimir and allow you to um write um different uh metric formats into uh Mimir like DataDog, Influx, and Graphite. Um and um the the golden fellow in the picture is my best friend Guido. He couldn't make it today, um but he's been uh all the time with me doing these slides.

And for everyone watching the recording later, I'm Ganesh Vernekar. I'm a software engineer at Grafana Labs and also a Prometheus team member. All right, so what is out of order? Um big question. Um we thought about writing a quote and a paragraph um but we think it's best to illustrate it. But before we get to explain what this image means, uh I'd like to do this little exercise. Uh so we're going to talk about out of order within the TSDB and the TSDB is this um huge list of uh things and and little components that work together. So we're going to narrow our focus into the series level uh of the TSDB. So you can think it has um a lot of series. We're going to talk about specifically one series only. In this case is one known by all, I think, um HTTP request total. Um so this picture um is illustrating uh six samples that are coming one by one in chronological order um from value one to value six. Um the first sample has time stamp zero or T0 and then the subsequent time uh samples are coming with um a bigger um or a newer time stamp like T0 + 15 seconds, + 13 seconds, and so on.

The first five samples that we got uh are fortunately in order. So that's what you all see in your instances usually. Um but the sixth sample that we got um came with an older sample than the last sample that we appended, that is T0 + 50. So that is 10 seconds older than the last one that we appended. That is out of order for Prometheus and that is what we're trying to
