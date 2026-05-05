---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/monitoring-cloudflares-planet-scale-edge-network-with-prometheus/
youtube_url: https://www.youtube.com/watch?v=ypWwvz5t_LE
youtube_search_url: https://www.youtube.com/results?search_query=Monitoring+Cloudflare%27s+Planet-Scale+Edge+Network+with+Prometheus+PromCon+2017
video_match_score: 0.963
status: video-found
---

# Monitoring Cloudflare's Planet-Scale Edge Network with Prometheus

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/monitoring-cloudflares-planet-scale-edge-network-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=ypWwvz5t_LE

## Resumo

Speaker: Matt Bostock Cloudflare operates a global anycast edge network serving content for 6 million web sites. This talk explains how we monitor our network, how we migrated from Nagios to Prometheus and the architecture we chose to provide maximum reliability for monitoring. We'll also discuss the impact of alert fatigue and how we reduced alert noise by analysing data, making alerts more actionable and alerting on symptoms rather than causes.

## Abstract oficial

Speaker: Matt Bostock

Cloudflare operates a global anycast edge network serving content for 6 million web sites. This talk explains how we monitor our network, how we migrated from Nagios to Prometheus and the architecture we chose to provide maximum reliability for monitoring. We'll also discuss the impact of alert fatigue and how we reduced alert noise by analysing data, making alerts more actionable and alerting on symptoms rather than causes.

This talk will cover:


The challenges of monitoring a high volume, anycast, edge network across 100+ locations
The architecture we chose to maximise the reliability of our monitoring
Why Prometheus excels as the new industry standard for modern monitoring
Approaches for reducing alert noise and alert fatigue
Triaging alerts into a ticket system
Analysing past alert data for continuous improvement
The pain points we endured
Effecting change across engineering teams




Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/monitoring-cloudflares-planet-scale-edge-network-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=ypWwvz5t_LE
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ypWwvz5t_LE
- YouTube title: PromCon 2017: Monitoring Cloudflare's Planet-Scale Edge Network with Prometheus - Matt Bostock
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/monitoring-cloudflares-planet-scale-edge-network-with-prometheus/ypWwvz5t_LE.txt
- Transcript chars: 34144
- Keywords: prometheus, metrics, actually, manager, monitoring, server, alerts, servers, multiple, presence, metric, exporter, network, monitor, moment, points, storage, deploy

### Resumo baseado na transcript

[Music] morning everyone hi so my name is Matt Bostock I work at CloudFlare and this morning I want stalky talk to you about how we're monitoring car flares planet-scale edge network using Prometheus and so I work on the platform operations team at CloudFlare I'm going to be talking you through basically I'm over a year and a half's work of I'm integrating Prometheus within CloudFlare to monitor our edge network and also our internal services so we use Prometheus for monitoring so by monitoring I mean alerting on

### Excerpt da transcript

[Music] morning everyone hi so my name is Matt Bostock I work at CloudFlare and this morning I want stalky talk to you about how we're monitoring car flares planet-scale edge network using Prometheus and so I work on the platform operations team at CloudFlare I'm going to be talking you through basically I'm over a year and a half's work of I'm integrating Prometheus within CloudFlare to monitor our edge network and also our internal services so we use Prometheus for monitoring so by monitoring I mean alerting on critical issues Incident Response and also post-mortem analysis Prometheus uses metrics for alerting which is really useful really flexible but we don't actually use Prometheus to store our application metrics in the long term so we set our data attention to 15 days which is just long enough for the monitoring use case and I'll explain a little bit more why we do that in just a moment so what does CloudFlare do so a lot of people know is there's a CDN but we also do a lot a lot more than that so we spot spots on lots of new protocols that allow you to speed up your websites for T less 1.3 HTTP 2 and we're also on the largest managed DNS providers in the world so I'm explaining all of this to give you an idea of what the scope is of what we actually have to monitor using using Prometheus so this is what our edge network looks like it's an anycast Network we have over 115 different points of presence around the world and we also serve around 6 million websites more than 6 million websites so we receive a lot of traffic we have a very widespread network and so there's a lot to monitor and this is what our Prometheus deployment looks like so we have a 185 from Easter service currently production we have 4 top level Prometheus servers that are collecting federated metrics we just about seven to two thousand samples per second maximum on any given Prometheus server and 4.6 million time series is is that the most time series we have on any server and for that those 4.6 time million time series over 15 days that takes about 250 gigabytes on disk and we're storing those metrics on rate and SSD storage so a little bit about our architecture so as this with so many points of presence every day Center is essentially configured in the same way we do routing via our anycast so the a user visiting a website will connect to the location closest to them and this is really important when you're thinking about how we deploy for meteors because a lot of these points
