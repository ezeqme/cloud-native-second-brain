---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Anirudha Jadhav", "Kyle Hounslow"]
source_url: https://promcon.io/2025-munich/talks/from-logs-to-metrics-opensearchs-prometheus-support-with-agentic-ai-and-natural-language-to-promql/
youtube_url: https://www.youtube.com/watch?v=m0CNEqfmOpc
youtube_search_url: https://www.youtube.com/results?search_query=From+Logs+to+Metrics%3A+OpenSearch%27s+Prometheus+support+with+Agentic+AI+and+Natural+Language+to+PromQL+PromCon+2025
video_match_score: 0.963
status: video-found
---

# From Logs to Metrics: OpenSearch's Prometheus support with Agentic AI and Natural Language to PromQL

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Anirudha Jadhav, Kyle Hounslow
- Página oficial: https://promcon.io/2025-munich/talks/from-logs-to-metrics-opensearchs-prometheus-support-with-agentic-ai-and-natural-language-to-promql/
- YouTube: https://www.youtube.com/watch?v=m0CNEqfmOpc

## Resumo

Prometheus has become the gold standard for metric collection and alerting in cloud-native environments. At the same time, OpenSearch Dashboards continues to evolve as a unified observability platform. This talk introduces the native support for Prometheus within OpenSearch Dashboards; covering everything from seamless data ingestion and schema compatibility to rich visualizations, alerting, and unified querying.

## Abstract oficial

Prometheus has become the gold standard for metric collection and alerting in cloud-native environments. At the same time, OpenSearch Dashboards continues to evolve as a unified observability platform. This talk introduces the native support for Prometheus within OpenSearch Dashboards; covering everything from seamless data ingestion and schema compatibility to rich visualizations, alerting, and unified querying.
We’ll showcase how users can now pivot from logs to metrics and back with ease, powered by intelligent agentic AI features that reduce toil in debugging and investigations. Most excitingly, we’ll demo our natural language to PromQL interface; enabling users to generate complex queries just by describing what they want to see.
Whether you’re an SRE, a platform engineer, or just tired of memorizing PromQL syntax, this session will show how OpenSearch is bringing intelligence, usability, and scale to Prometheus-powered environments.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/from-logs-to-metrics-opensearchs-prometheus-support-with-agentic-ai-and-natural-language-to-promql/
- YouTube: https://www.youtube.com/watch?v=m0CNEqfmOpc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m0CNEqfmOpc
- YouTube title: PromCon 2025 - From Logs to Metrics: OpenSearch's Prometheus support with Agentic AI and Natural ...
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/from-logs-to-metrics-opensearchs-prometheus-support-with-agentic-ai-an/m0CNEqfmOpc.txt
- Transcript chars: 23810
- Keywords: search, agents, actually, dashboards, prometheus, observability, context, logs, metrics, support, knowledge, investigation, language, promql, source, queries, traces, already

### Resumo baseado na transcript

Uh, welcome to the talk on Prometheus support and Agentic AI in Open Search. I've been with the open source observability or for about five years now. Open search is being used for search of course, but quite a large number of our users are also ingesting their logs and traces for observability and security analytics as well as their vector embeddings for machine learning. You can query, visualize your logs and traces, create custom dashboards, de monitoring, alerting. And we're working towards adding more like Prometheus so we can get all metrics, logs, and traces for observability. I did really want to demo the native Prometheus support today, but it's still in the works.

### Excerpt da transcript

All right. Thanks. Just making sure everybody can hear me in the back there. We're good. Right on. Okay. Thanks for having me. I hope everyone's now settled back in from lunch. Uh, welcome to the talk on Prometheus support and Agentic AI in Open Search. Uh, just a little introduction. My name is Kyle. I'm a senior software engineer at AWS. I've been with the open source observability or for about five years now. Uh I was part of the original team who launched Amazon manage graphana and I work closely with the manage Prometheus teams and open telemetry as well. Now I'm working with the open search team uh to bring native Prometheus support and agentic AI into open search dashboards. Quick survey show of hands. Who here uses open search or knows about open search? Okay, quite a few. Uh what about open search dashboards? A couple more than I thought. All right, great. Um so I'll be going through a brief overview of open search and open search dashboards first. Uh but then I'll dive into native Prometheus support and observability agents in open search dashboards.

I'll also show a demo. Let's make sure I'm good for time and um and leave some time at the end for Q&A. Uh so open search is an open source distributed search and analytics engine and a project of the Linux Foundation. We have a vibrant and fast growing community of over 3,000 contributors. So if you're interested, please check us out. Open search is being used for search of course, but quite a large number of our users are also ingesting their logs and traces for observability and security analytics as well as their vector embeddings for machine learning. uh the four main components of the project. Open search core which is the main uh search and analytics engine data prepper for ingesting data into your search engine or search index rather and the vector engine which powers AI features like semantic search retrieval augmented generation and dashboards for exploring and visualizing your data. So for search dashboards is an open source data visualization and exploration platform for observability and analytics.

You can query, visualize your logs and traces, create custom dashboards, de monitoring, alerting. There's also security and analytics and anomaly detection features. Um, well, the majority of our dashboard users uh use it for open search data. You can also connect to external data sources like S3 via the uh glue data catalog. And we're working towards adding more like Prometheus so we can ge
