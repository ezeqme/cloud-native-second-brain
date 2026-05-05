---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Mihail Mihaylov"]
source_url: https://promcon.io/2024-berlin/talks/agile-monitoring-at-scale-with-thanos/
youtube_url: https://www.youtube.com/watch?v=K91Y8MZpGfw
youtube_search_url: https://www.youtube.com/results?search_query=Agile+Monitoring+At+Scale+With+Thanos+PromCon+2024
video_match_score: 0.981
status: video-found
---

# Agile Monitoring At Scale With Thanos

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Mihail Mihaylov
- Página oficial: https://promcon.io/2024-berlin/talks/agile-monitoring-at-scale-with-thanos/
- YouTube: https://www.youtube.com/watch?v=K91Y8MZpGfw

## Resumo

A Prometheus environment is not cloud-specific. It extends beyond Kubernetes setups and in fact, it was not designed to be. It is not cloud-bound.

## Abstract oficial

A Prometheus environment is not cloud-specific. It extends beyond Kubernetes setups and in fact, it was not designed to be. It is not cloud-bound. The Prometheus ecosystem adapts to your unique needs, leveraging the breadth of your knowledge and skills. It is supposed to facilitate the need for visibility of the SRE team, not a particular environment or a project.

This is why, in MariaDB, we've created a Core Monitoring system based on Prometheus, Thanos, and Grafana that is as close to the SRE team as possible. It scales with the team's needs up and down from PoC to monitoring 1000+ Kubernetes clusters, simple cloud VMs, and potentially on-prem setups.

In this lecture, I will discuss the modifications that this system has undergone, including data migrations, topology changes, the shift from single to multi-tenancy, and plans for future hybrid cloud and on-premises environments. 

The key takeaway will be how Prometheus can scale with your needs and remain as agile as necessary.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/agile-monitoring-at-scale-with-thanos/
- YouTube: https://www.youtube.com/watch?v=K91Y8MZpGfw
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=K91Y8MZpGfw
- YouTube title: PromCon 2024 - Agile Monitoring At Scale With Thanos
- Match score: 0.981
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/agile-monitoring-at-scale-with-thanos/K91Y8MZpGfw.txt
- Transcript chars: 18890
- Keywords: actually, monitoring, environment, thanos, cluster, course, global, efficient, silence, alerting, cost, clusters, regional, observability, metrics, started, better, implemented

### Resumo baseado na transcript

[Music] thank you everyone so let's begin the infinity Saga nice so my name is m mov and I have spent the last six years of my life trying to persuade my top managers why we need observability so don't get me wrong yeah uh don't get me wrong people always know that they need observability but they are not always sure why now I work as as an S site reliability engineer uh at Marb and it has been a challenge to be given the time and money to

### Excerpt da transcript

[Music] thank you everyone so let's begin the infinity Saga nice so my name is m mov and I have spent the last six years of my life trying to persuade my top managers why we need observability so don't get me wrong yeah uh don't get me wrong people always know that they need observability but they are not always sure why now I work as as an S site reliability engineer uh at Marb and it has been a challenge to be given the time and money to actually uh produce the observability system that we have right now so I felt that many of you and your reaction just proved me that have uh the same issues as me and might share the same experience as I so in a sense this talk is uh the history the story of how I built how I fought the fight for observability the truths of the truths I found along the way and eventually the croud native uh Cloud agnostic cheap agile monitoring system that we've built so along the way I stumble on upon questions like for example why do we need metrics older than one day why do we need a global view of the data so when I joined Marb I started thinking how I can bridge this gap of understanding um yeah I focused primarily on the monitoring as the first part of observability as a starting point for the future development of of the observability system and by the way it always bumps me how people think of monitoring as a binary you either have it or you don't it's just simply more complex than that and this is something that I I wanted to address in my road map I started building a road map of a future stateof art monitoring system that we were going to create and it was comprehensive it was eight pages long it was uh supposed to be my starting point for advocation to the superiors uh the first part was what is the current situation and all the issues we have right now uh we had lack of uh efficient highly Ava High availability we have a lot of duplications in some cases up to eight times the data point we have uh limited we had limited scope so not everything was more we basically had no historical data or limited um cardinality was a daily thing and then alerting fatigue also so not many people were actually aing watching alerts uh simply because there were too many of them um and while the dashboards and alerts were um developed there were no methods like red or use used for actually um making sure that they are comprehensives nothing gets missed and last but not least the granity was not optimal so in some cases we even had uh retention
