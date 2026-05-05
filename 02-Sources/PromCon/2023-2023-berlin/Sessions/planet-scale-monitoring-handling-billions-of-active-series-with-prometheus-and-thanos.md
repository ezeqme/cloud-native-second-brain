---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Alerting", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/planet-scale-monitoring-handling-billions-of-active-series-with-prometheus-and-thanos/
youtube_url: https://www.youtube.com/watch?v=Or8r46fSaOg
youtube_search_url: https://www.youtube.com/results?search_query=Planet+scale+monitoring%3A+Handling+billions+of+active+series+with+Prometheus+and+Thanos+PromCon+2023
video_match_score: 1.053
status: video-found
---

# Planet scale monitoring: Handling billions of active series with Prometheus and Thanos

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/planet-scale-monitoring-handling-billions-of-active-series-with-prometheus-and-thanos/
- YouTube: https://www.youtube.com/watch?v=Or8r46fSaOg

## Resumo

Speaker(s): Sebastian Rabenhorst & Mikołaj Liberski Deploying and operating a highly available and distributed Prometheus setup at scale can present significant challenges. In this presentation, we will showcase an example of a globally distributed and highly scalable deployment at Shopify. This setup enables us to ingest billions of active time series with tens of millions of samples per second, coming from thousands of applications running in hundreds of Kubernetes clusters.

## Abstract oficial

Speaker(s): Sebastian Rabenhorst & Mikołaj Liberski

Deploying and operating a highly available and distributed Prometheus setup at scale can present significant challenges. In this presentation, we will showcase an example of a globally distributed and highly scalable deployment at Shopify. This setup enables us to ingest billions of active time series with tens of millions of samples per second, coming from thousands of applications running in hundreds of Kubernetes clusters.

The main part of the presentation will cover the architecture of our current solution. We will demonstrate how we use Prometheus agents with custom service discovery to scrape and write metrics into regional Thanos receiver deployments. We will also explain how we leverage Thanos's long-term storage and distributed querying capabilities to enable long-term querying of billions of time series. Additionally, we will provide insight into how thousands of developers can query, explore, and configure their metrics and alerts through a customized Grafana deployment, and how our setup evaluates rules and alerts across our entire metrics dataset.

At the end of the presentation, we will emphasize some of the challenges we encountered during the time-intensive migration from a third-party monitoring vendor to our current solution.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/planet-scale-monitoring-handling-billions-of-active-series-with-prometheus-and-thanos/
- YouTube: https://www.youtube.com/watch?v=Or8r46fSaOg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Or8r46fSaOg
- YouTube title: PromCon 2023 - Planetscale monitoring: Handling billions of active series with Prometheus and Thanos
- Match score: 1.053
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/planet-scale-monitoring-handling-billions-of-active-series-with-promet/Or8r46fSaOg.txt
- Transcript chars: 26190
- Keywords: receivers, metric, specific, prometheus, metrics, shopify, clusters, regions, multiple, cluster, thanos, challenges, distributed, global, tenant, everything, actually, sebastian

### Resumo baseado na transcript

[Music] so hello everyone uh Welcome to our short presentation of the planet scale monitoring handling billions of Time series with Prometheus and Thanos we are Sebastian and moo senior production Engineers from Shopify observability metric team and we want to share our experience building a truly Planet skill stack of metrics monitoring with you so we recently migrated from a SAS solution to in-house open source slack for metrix monitoring and in this presentation we want to show the system and share the challenges we encountered on the way

### Excerpt da transcript

[Music] so hello everyone uh Welcome to our short presentation of the planet scale monitoring handling billions of Time series with Prometheus and Thanos we are Sebastian and moo senior production Engineers from Shopify observability metric team and we want to share our experience building a truly Planet skill stack of metrics monitoring with you so we recently migrated from a SAS solution to in-house open source slack for metrix monitoring and in this presentation we want to show the system and share the challenges we encountered on the way learnings we had and how we had to adapt the system to the scale we run at so as we already introduced ourselves let me take a moment and guide you through what we want to show you today uh we will take uh you on a journey how we build it internally in the first place where we arrived with the solution at the end uh with a few quirks and challenges we encountered on the the way there and how we tackle them for the benefit of company but also wider Community uh we will also provide a bit of Shopify specific context first since the company profile presents few unique challenges to the whole system uh that we introduced here today so now let me fill you in on a bit on the context of Shopify unique challenges and infro choices so Sebastian can present the actual system architecture for you Shopify is one of the few biggest Ruby shops in the world and the stock is deployed as a significant portion of the company infrastructure on kubernetes uh so some specific context why this company may have unique characteristics that may provide for a tough set of constraints for a system like this it is very globally distributed it's a global company with millions of merchants around the world and believe me there is some great research available on how latency affects conversion rates of buyers so developers and Merchants are very much interested in a consistently low latency to their shops the scale of elasticity is a problem infrastructure is in motion all the time very dynamically responding to the merchant demands but also even during the periods of relative quiet we are dealing with billions of active time serus in the system hundreds of kubernetes clusters are present but we scale both in the number of them and uh how they how big they are uh we very clearly see the ab and FL of the day and night cycle in particular regions but also specifically for our company profile flash sales and big yearly events matter so Commerce happens
