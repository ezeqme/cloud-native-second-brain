---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/10x-improvement-for-kubernetes-performance/
youtube_url: https://www.youtube.com/watch?v=HS-a_RG7iX0
youtube_search_url: https://www.youtube.com/results?search_query=10x+Improvement+for+Kubernetes+Performance+PromCon+2016
video_match_score: 0.873
status: video-found
---

# 10x Improvement for Kubernetes Performance

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/10x-improvement-for-kubernetes-performance/
- YouTube: https://www.youtube.com/watch?v=HS-a_RG7iX0

## Resumo

Speaker: Jonathan Boulle Scalability is one of the important factors that make a successful distributed system. At CoreOS, we love Kubernetes and help drive the project forward through upstream contributions. Learn how we analyzed Kubernetes cluster performance to gain insight into cluster behavior under large workloads and learn where there are performance issues.

## Abstract oficial

Speaker: Jonathan Boulle

Scalability is one of the important factors that make a successful distributed
system. At CoreOS, we love Kubernetes and help drive the project forward
through upstream contributions. Learn how we analyzed Kubernetes cluster
performance to gain insight into cluster behavior under large workloads and
learn where there are performance issues. See how we used Prometheus for
improving Kubernetes scheduler performance by 10x.



Slides

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/10x-improvement-for-kubernetes-performance/
- YouTube: https://www.youtube.com/watch?v=HS-a_RG7iX0
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HS-a_RG7iX0
- YouTube title: PromCon 2016: 10x Improvement for Kubernetes Performance - Jonathan Boulle
- Match score: 0.873
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/10x-improvement-for-kubernetes-performance/HS-a_RG7iX0.txt
- Transcript chars: 24304
- Keywords: metrics, actually, prometheus, performance, schedule, pretty, cluster, looking, running, control, started, getting, little, better, already, within, seeing, having

### Resumo baseado na transcript

so my name is Jonathan I work at coros um as a bit of a disclosure I don't actually work on the kubernetes performance team at coros but um they're all in SF and they weren't able to make it so I'm just going to be talking kind of on their behalf um but I have been involved with this stuff a bit um and this also the title of this talk is a little bit of a track a little bit of a trick um everyone loves like you

### Excerpt da transcript

so my name is Jonathan I work at coros um as a bit of a disclosure I don't actually work on the kubernetes performance team at coros but um they're all in SF and they weren't able to make it so I'm just going to be talking kind of on their behalf um but I have been involved with this stuff a bit um and this also the title of this talk is a little bit of a track a little bit of a trick um everyone loves like you know 10x uh performance improvements that sounds great um but actually I want to use this as well to kind of argue a bit why you know metrics are important and why you should use more of them and use more of them with systems like kubernetes yeah so first kind of like uh start with a little bit of again trying to kind of persuade you like why metrics are important why we should instrument everything like the Prometheus guys keep telling us um and then the first like obviously the main two reasons that people often think about coming from you know devops or coming from older systems is like the first is Health monitoring right so um that allows you to you know easily kind of measure how healthy your system is performing whether at like an individual service level or maybe at a higher level um uh within kind of your stack and then also to do alerting based on that um and you know time series based alerting is obviously a bit more powerful than you know older kind of uh more sort of static systems like things like nagios and stuff with simp simple checks um but kind of looking trying to move beyond that to to seeing what other things that you know this new metrics kind of world allows us to do um something that I think someone touched on in a talk earlier today was maybe or I was also having a conversation with someone about it is you know you can start to use metrics maybe for for sort of business Insight things I mean obviously people do use metrics for business insight but even even something like Prometheus um maybe if you're trying to like capacity plan you can get an idea from the kind of metrics that prome Prometheus can expose about you know what your utilization is like in your cluster and when you might not start to need to think about getting more servers um or similarly you could could even if you want to track things like um you know how how users are interacting with your apps um autot tuning is is kind of a a a newer area I'd say um we're seeing this start to be explored in in kubernetes uh for example um the idea here is that you know o
