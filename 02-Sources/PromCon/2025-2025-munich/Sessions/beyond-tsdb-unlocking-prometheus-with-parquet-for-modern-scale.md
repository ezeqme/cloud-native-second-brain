---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "OpenTelemetry", "Scalability Reliability", "Visualization Dashboards", "Cost Optimization", "Community"]
speakers: ["Jesus Vazquez", "Alan Protasio", "Michael Hoffmann"]
source_url: https://promcon.io/2025-munich/talks/beyond-tsdb-unlocking-prometheus-with-parquet-for-modern-scale/
youtube_url: https://www.youtube.com/watch?v=wDN2w2xN6bA
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+TSDB%3A+Unlocking+Prometheus+with+Parquet+for+Modern+Scale+PromCon+2025
video_match_score: 1.035
status: video-found
---

# Beyond TSDB: Unlocking Prometheus with Parquet for Modern Scale

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[OpenTelemetry]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Cost Optimization]], [[Community]]
- Speakers: Jesus Vazquez, Alan Protasio, Michael Hoffmann
- Página oficial: https://promcon.io/2025-munich/talks/beyond-tsdb-unlocking-prometheus-with-parquet-for-modern-scale/
- YouTube: https://www.youtube.com/watch?v=wDN2w2xN6bA

## Resumo

Prometheus has been the main tool for time-series metrics in cloud-native world. Its TSDB format is used in many projects like Thanos, Cortex, and Mimir. But now, with OpenTelemetry’s need for an increased amount of time series dimensions, the well known limitations with high cardinality and slow queries from object storage are more pressing.

## Abstract oficial

Prometheus has been the main tool for time-series metrics in cloud-native world. Its TSDB format is used in many projects like Thanos, Cortex, and Mimir. But now, with OpenTelemetry’s need for an increased amount of time series dimensions, the well known limitations with high cardinality and slow queries from object storage are more pressing. In this talk, we want to share how we, from Grafana Labs (Mimir), AWS Managed Prometheus (Cortex), and Cloudflare (Thanos), tried to replace the Prometheus TSDB with Apache Parquet. Parquet is a columnar storage format that is already popular for big data analytics.

We will talk about what we learned from running Parquet storage in production. You will hear about the architecture, the problems we found, and the improvements we saw when we stored labels and chunks in Parquet. We hope you will see how Parquet can solve some old problems and help Prometheus go to the next level. We also want to invite you to help support Parquet in Prometheus directly.

All this work happened in the open, with conversations and code shared in CNCF Slack and on the Prometheus Community GitHub. We believe this open way is important, so everyone can join, give feedback, and help make Prometheus better for all.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/beyond-tsdb-unlocking-prometheus-with-parquet-for-modern-scale/
- YouTube: https://www.youtube.com/watch?v=wDN2w2xN6bA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wDN2w2xN6bA
- YouTube title: Promcon 2025 - Beyond TSDB: Unlocking Prometheus with Parquet for Modern Scale
- Match score: 1.035
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/beyond-tsdb-unlocking-prometheus-with-parquet-for-modern-scale/wDN2w2xN6bA.txt
- Transcript chars: 25537
- Keywords: series, prometheus, parket, column, offset, footer, storage, postings, object, library, amount, engine, chunks, better, format, labels, matcher, working

### Resumo baseado na transcript

We can finally share um what we've been working on for the most part of the year by now. Um which is about introducing Paret into the Prometheus ecosystem to see if we can handle long-term Prometheus data with it. Um, and in my case, it wasn't until March this year where I used one of the hackathon that we have at Grafana to kind of work on this a little bit and I joined Grajo and a few others in the company to to fork Prometheus and see where we could fit paret uh inside it. CNCF Slack channel Prometheus Park um and I went to sleep um and the day after people from Red Hat, Reddit and uh Amathon showed up on the channel um and that's when we met Alan and he also said he was running a PC We had to join forces and we created parket common which is a library that exists in the Prometheus community organization. But we thought it would be useful for people interacting with it to have like a queryable implementation primeus interface.

### Excerpt da transcript

[music] Yes. All right. Okay. Good morning everyone. I'm very happy to be with you here today. We can finally share um what we've been working on for the most part of the year by now. Um which is about introducing Paret into the Prometheus ecosystem to see if we can handle long-term Prometheus data with it. Um but before all that let's introduce ourselves. My name is Jesus Vadk. I'm a senior software engineer at Grafana and I am joined by Michael Hoffman, senior software engineer and Alan Protasio, senior software engineer at Amazon. Um what brought us here? Well, we the three of us are maintainers of uh three different downstream projects of Prometheus, Cortex, Mimir and Thanos. When I first joined the community, I remember watching a talk where they were sharing that um Thanos was influencing uh Cortex with ideas and vice versa. And I'm happy that that continues to happen today. Um uh throughout our experience running and maintaining um clusters of these technologies, we've all experienced similar pains on the gray path.

uh more on that later. But perhaps the thing that uh inspired us to work on this and talk about this today here is this talk about uh Philip Powski which did this awesome work at Shopify where he modified Thanos squers to use spit. So that talk happened around November last year. Um, and unfortunately the code is not open source, but the contents of the dog were great. And we didn't know at the time, but we were all working um on this separately. Um, and in my case, it wasn't until March this year where I used one of the hackathon that we have at Grafana to kind of work on this a little bit and I joined Grajo and a few others in the company to to fork Prometheus and see where we could fit paret uh inside it. Um that same week someone told me I believe it was Gotham that Cloudflare had open source a repository where they were trying to do a similar thing that Philip did and so I immediately reached out uh to to Michael and I created this CNCF Slack channel Prometheus Park um and I went to sleep um and the day after people from Red Hat, Reddit and uh Amathon showed up on the channel um and that's when we met Alan and he also said he was running a PC internally.

Um so the next step was clear for us. We had to join forces and we created parket common which is a library that exists in the Prometheus community organization. Um it passes 100% of the promql acceptant tests. So any any sort of promql queries should run. Um the library is low le
