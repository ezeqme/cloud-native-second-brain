---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Kubernetes", "Scalability Reliability", "Cost Optimization"]
speakers: ["Nicolas Takashi"]
source_url: https://promcon.io/2024-berlin/talks/unbreakable-prometheus-leveraging-limits-for-consistent-monitoring/
youtube_url: https://www.youtube.com/watch?v=DoKaFPg_6Zc
youtube_search_url: https://www.youtube.com/results?search_query=Unbreakable+Prometheus%3A+Leveraging+Limits+for+Consistent+Monitoring+PromCon+2024
video_match_score: 1.04
status: video-found
---

# Unbreakable Prometheus: Leveraging Limits for Consistent Monitoring

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: Nicolas Takashi
- Página oficial: https://promcon.io/2024-berlin/talks/unbreakable-prometheus-leveraging-limits-for-consistent-monitoring/
- YouTube: https://www.youtube.com/watch?v=DoKaFPg_6Zc

## Resumo

Join us in this session where we’ll dive into implementing Prometheus limits using the Prometheus Operator to create a more stable and predictable monitoring system. We will see a set of practices to keep your Prometheus cluster resilient and reliable, helping you avoid common issues like high cardinality and unexpected alerts. This talk is ideal for anyone eager to optimize their monitoring setup and boost system reliability.

## Abstract oficial

Join us in this session where we’ll dive into implementing Prometheus limits using the Prometheus Operator to create a more stable and predictable monitoring system. We will see a set of practices to keep your Prometheus cluster resilient and reliable, helping you avoid common issues like high cardinality and unexpected alerts. This talk is ideal for anyone eager to optimize their monitoring setup and boost system reliability. Don’t miss out on the chance to enhance your Prometheus expertise!

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/unbreakable-prometheus-leveraging-limits-for-consistent-monitoring/
- YouTube: https://www.youtube.com/watch?v=DoKaFPg_6Zc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DoKaFPg_6Zc
- YouTube title: PromCon 2024 - Unbreakable Prometheus: Leveraging Limits for Consistent Monitoring
- Match score: 1.04
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/unbreakable-prometheus-leveraging-limits-for-consistent-monitoring/DoKaFPg_6Zc.txt
- Transcript chars: 20489
- Keywords: limits, series, labels, target, instance, single, amount, metric, samples, targets, pretty, decide, number, pritus, cardinality, default, length, promit

### Resumo baseado na transcript

[Music] hello everybody hope you're are not starving uh but I would try to be quicker and concer um how many of you is using cam stack like a lot of people right and how many of you is caring about setting limits think about like predicting okay one two three four okay just a few that's cool so I hope we have some learnings today or at least um review some based knowledge so um today I want to tell you a tale about a company named unbounded Matrix

### Excerpt da transcript

[Music] hello everybody hope you're are not starving uh but I would try to be quicker and concer um how many of you is using cam stack like a lot of people right and how many of you is caring about setting limits think about like predicting okay one two three four okay just a few that's cool so I hope we have some learnings today or at least um review some based knowledge so um today I want to tell you a tale about a company named unbounded Matrix so this is a very cool name right and the ounded metrix um was a fast growing tech company uh focused on Real Time data analytics it's a pretty fan business um and as they metrix uh expanded this their business operation they start to looking for um monitoring to where they could use to building an internal monitoring platform and these two needs to be extensible backed by community so everything that pritus is yes so they were amazed about promus and decide to install promeets on their kubernets clusters uh using Cube promus stack but here's the drama because they went ahead with a YOLO approach nothing think about about limits not think about like how many samples they could ingest or anything else and in the beginning everything seems pretty fine because it just works it's super amazing you have like with a simple helmet style you have alert manager prome meus and many other tools right but okay they are fine but they start facing some Challenge and now probably you might asking who this guy that's talking to me well my name is Nicholas takash uh I'm observability Tech lead at Coral a maintainer of the prome operator and also contributor to other open source projects like prome open Telemetry purses and tunos uh actually this is my first prom con as a speaker and attendee as well so a pleasure to be here and while I wasn't part of the unbounded metrics I've I've been working with closely with different organizations facing similar challenges so I hope today uh we learn something from their experience implementing limits and trying to make promeets more predictable and stable at least in terms of temples ingestion right so before we go to the to the journey a quick overview on their um on their stack they are just running kubernetes so they're using pritus operator because you know this is the easiest way to manage pritus in kubernetes they are deploying prome and alert manage like this is a pretty simple monitoring stack okay so they start facing the fa the first challenge the the label crisis so unbonded metr
