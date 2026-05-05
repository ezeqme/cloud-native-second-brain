---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability", "Visualization Dashboards", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/finding-useless-and-resource-hungry-prometheus-metrics/
youtube_url: https://www.youtube.com/watch?v=NRXAB_Ug8zo
youtube_search_url: https://www.youtube.com/results?search_query=Finding+useless+and+resource-hungry+Prometheus+metrics+PromCon+2023
video_match_score: 1.023
status: video-found
---

# Finding useless and resource-hungry Prometheus metrics

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/finding-useless-and-resource-hungry-prometheus-metrics/
- YouTube: https://www.youtube.com/watch?v=NRXAB_Ug8zo

## Resumo

Speaker(s): David Calvert Did you ever wonder which of your scrapped Prometheus metrics were actually used and which wasn’t? Or which labels were responsible for your metrics cardinality? And how this could impact the performance of your Prometheus setup?

## Abstract oficial

Speaker(s): David Calvert

Did you ever wonder which of your scrapped Prometheus metrics were actually used and which wasn’t? Or which labels were responsible for your metrics cardinality? And how this could impact the performance of your Prometheus setup?

As an engineer, you might need to understand, track cardinality issues or reduce resource usage of your Prometheus setup. First step is to understand and measure what you have in your Prometheus’s TSDB. Hopefully we have now great tools to do that!

In this talk, I will explain how Mimirtool and Grafana can help you achieve this in no time!

We’ll cover:


Analysing your Prometheus metrics usage with Mimirtool
Dropping unused metrics on the exporter, or using relabeling rules
Finding high-cardinality metrics on Prometheus
Finding high-cardinality labels using the Cardinality Explorer Grafana dashboard
A potential quick win to reduce Prometheus resource usage

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/finding-useless-and-resource-hungry-prometheus-metrics/
- YouTube: https://www.youtube.com/watch?v=NRXAB_Ug8zo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NRXAB_Ug8zo
- YouTube title: PromCon 2023 - Finding useless and resource-hungry Prometheus metrics
- Match score: 1.023
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/finding-useless-and-resource-hungry-prometheus-metrics/NRXAB_Ug8zo.txt
- Transcript chars: 14750
- Keywords: metrics, cardinality, metric, basically, instance, metrix, analyze, actually, course, resource, pretus, dashboards, dashboard, grafana, output, promus, mimir, operation

### Resumo baseado na transcript

[Music] so hi everyone uh I'm David I'm a cability engineer and I'm going to my talk is finding useless and resource angry pruse metrics so I've decided afterwards that useless is a negative tone so I've like that's why the the the title is like that um doesn't work okay so uh to give a bit of context so I've um I have at this talk ID by um I was recently given the task to um to fix a promus setup it was unstable it has uh a so you can have like maybe new panels new dashboards alerts so there can be like new stuff that you can you can have a look at and it could also be an opportunity to to clean to clean some some things up that you

### Excerpt da transcript

[Music] so hi everyone uh I'm David I'm a cability engineer and I'm going to my talk is finding useless and resource angry pruse metrics so I've decided afterwards that useless is a negative tone so I've like that's why the the the title is like that um doesn't work okay so uh to give a bit of context so I've um I have at this talk ID by um I was recently given the task to um to fix a promus setup it was unstable it has uh a lot of um P crashes things like that because it was running on under promius under Kutis it had many cardinality issues and it was also using a lot of resources uh so we we had to do something about that so this talk is divided into three parts the first we're going to see how we can use um mimir tool to analyze our pruse metrics uh then we're going to uh see how we can find and analyze hard cardinality metrics using pretus and grafana and finally I will share a potential quick win to reduce even further the paret resource usage so let's start with uh analyzing our metrics with MIM tool so when when I first uh had this task I I I was asking myself well what's what's coming into the the the promus instances so I've had a look using this Pro prom query to see all the metrics the the list of metrics that was uh that was here uh but there there was something missing like I didn't knew what we were actually using and what we didn't so I I did a a bit of research and I've come to mimir Tool which is a CLI tool that can be used to do various operation around pretus uh like the name implies it's of course part of the graph project uh so you so you have the the documentation link if you want to to learn more about the tool but we going to mainly focus on one part of the tool which is the analyze part so using using Mir tool analyze you can analyze graph um rulers or promus rules and also prous instances so when when you when you do that so you you need to give it uh the address of your pret instance and an API token so a service account token now um and it will if you if you do that it will output basically a file which is named metrix in graph.

Json and it will include all all the metrics uh sorted by um I mean all the all the metrics that is actually used in the in your dashboards and and panel and stuff like that um you can do the same thing for the promerus rules so basically what it does it would like go through all your alerting rules and recording rules and do the same thing like have a list of what's in there and finally uh when you te
