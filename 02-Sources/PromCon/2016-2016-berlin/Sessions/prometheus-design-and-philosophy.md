---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/prometheus-design-and-philosophy/
youtube_url: https://www.youtube.com/watch?v=4DzoajMs4DM
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Design+and+Philosophy+PromCon+2016
video_match_score: 0.696
status: video-found
---

# Prometheus Design and Philosophy

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/prometheus-design-and-philosophy/
- YouTube: https://www.youtube.com/watch?v=4DzoajMs4DM

## Resumo

Speaker: Julius Volz Prometheus is an opinionated monitoring system that chooses to do a lot of things differently from traditional monitoring systems. This leads to a culture clash for those used to other approaches, and raises questions as to why we didn't take a seemingly better approach. This talk focuses on the "why" behind many of the design decisions that are core to Prometheus, including pull vs.

## Abstract oficial

Speaker: Julius Volz

Prometheus is an opinionated monitoring system that chooses to do a lot of
things differently from traditional monitoring systems. This leads to a
culture clash for those used to other approaches, and raises questions as to
why we didn't take a seemingly better approach. This talk focuses on the "why"
behind many of the design decisions that are core to Prometheus, including
pull vs. push, the dimensional data model, relabeling, per-process exporters,
stateful client libraries, as well as aspects like metric naming conventions
and having a non-distributed storage as a design goal.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/prometheus-design-and-philosophy/
- YouTube: https://www.youtube.com/watch?v=4DzoajMs4DM

## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4DzoajMs4DM
- YouTube title: PromCon 2016: Prometheus Design and Philosophy - Why It Is the Way It Is - Julius Volz
- Match score: 0.696
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/prometheus-design-and-philosophy/4DzoajMs4DM.txt
- Transcript chars: 20482
- Keywords: prometheus, monitoring, labels, everything, series, actually, authentication, metric, usually, targets, relabeling, client, course, select, exactly, language, scrape, clustered

### Resumo baseado na transcript

uh all right um so uh I want to talk a bit about why Prometheus is the way it is as an opener for the conference or the second opener um as you might have known uh as you might have um experienced when you're coming from a different type of monitoring system like graphite or nagos gangas STD and so on um Prometheus does a lot of things very differently and sometimes that can lead to a bit of a culture Clash uh might take a while to understand

### Excerpt da transcript

uh all right um so uh I want to talk a bit about why Prometheus is the way it is as an opener for the conference or the second opener um as you might have known uh as you might have um experienced when you're coming from a different type of monitoring system like graphite or nagos gangas STD and so on um Prometheus does a lot of things very differently and sometimes that can lead to a bit of a culture Clash uh might take a while to understand why it does things differently and sometimes you might also think wow that's really a stupid way to do it why did they do it like that can isn't there a better way um so I just want to go into some of these decisions and show a bit our thinking behind them and why we think they're good uh approaches and principles so just as a disclaimer it's all kind of our opinionated way of looking at things we don't have to be right in every way and maybe don't fit to every use case but there is some thought behind everything as a perspective what is Prometheus really Prometheus is a Time series based monitoring system and it tries to cover the whole bread like from uh instrumentation getting metrics out of your processes storing them querying them and then doing useful stuff with them you know like graphs at hog debugging and so on and we really focused on two use cases back then really out of necessity which were we need needed operational systems monitoring so really a live view of what's happening in your system um and uh specifically it really needed to work for dynamic Cloud environments so these were kind of the pain points uh we were trying to solve um so this Focus means that we willfully really ignore some other use cases which we really do not intend to solve so if you want to for example store logs or raw events of something you use something like elastic search if you want to trace an individual user request through uh a stack of microservices use something like zipin and we don't do magic style anomaly detection you know that kind of fancy machine learning data mining statistics um we really only do explicit uh queries uh no durable long-term storage in Prometheus itself though there might be a decoupled way of doing that in the future um and so since we only have a local storage in every Prometheus server there's no automatic horizontal scaling either of course uh we're kind of ping on user and authentication features which are kind of Enterprise features from our view but I'll also go into that more later so let's
