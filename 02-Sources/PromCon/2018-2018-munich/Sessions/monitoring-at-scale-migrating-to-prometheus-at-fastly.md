---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/monitoring-at-scale-migrating-to-prometheus-at-fastly/
youtube_url: https://www.youtube.com/watch?v=ouLY973Ld24
youtube_search_url: https://www.youtube.com/results?search_query=Monitoring+at+Scale%3A+Migrating+to+Prometheus+at+Fastly+PromCon+2018
video_match_score: 0.898
status: video-found
---

# Monitoring at Scale: Migrating to Prometheus at Fastly

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/monitoring-at-scale-migrating-to-prometheus-at-fastly/
- YouTube: https://www.youtube.com/watch?v=ouLY973Ld24

## Resumo

Speaker: Marcus Barczak Over the past 6 months at Fastly we've migrated away from our legacy monitoring systems and have deployed Prometheus as our primary system for infrastructure and application monitoring. The Prometheus approach posed some unique challenges over traditional monitoring systems, whilst at the same time enabling us to easily scale our monitoring infrastructure alongside our global network growth. It hasn't been completely smooth sailing and deploying Prometheus across a globe spanning network serving over 10% of the world's internet traffic has raised its fair share of challenges both technical and cultural.

## Abstract oficial

Speaker: Marcus Barczak

Over the past 6 months at Fastly we've migrated away from our legacy monitoring systems and have deployed Prometheus as our primary system for infrastructure and application monitoring.

The Prometheus approach posed some unique challenges over traditional monitoring systems, whilst at the same time enabling us to easily scale our monitoring infrastructure alongside our global network growth.

It hasn't been completely smooth sailing and deploying Prometheus across a globe spanning network serving over 10% of the world's internet traffic has raised its fair share of challenges both technical and cultural.

In this presentation you will learn how we addressed these issues in ways that deviate slightly from conventional wisdom, the mistakes we made along the way, and how the new system has been received by our teams. We hope that our experiences can help you succeed in deploying Prometheus within your organization.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/monitoring-at-scale-migrating-to-prometheus-at-fastly/
- YouTube: https://www.youtube.com/watch?v=ouLY973Ld24
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ouLY973Ld24
- YouTube title: PromCon 2018: Migrating to Prometheus at Fastly
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/monitoring-at-scale-migrating-to-prometheus-at-fastly/ouLY973Ld24.txt
- Transcript chars: 35141
- Keywords: prometheus, metrics, infrastructure, monitoring, fastly, ganglia, systems, wanted, around, little, machine, network, running, engineers, applications, discovery, configuration, exporter

### Resumo baseado na transcript

[Applause] so yeah my name is Marcus I'm a principal engineer at fastly and at the moment I'm focusing on our sort of observability stack for those of you that aren't familiar with fastly and and I wouldn't be surprised if you aren't we power we're a content distribution network and edge cloud and we power but sort of hundreds of the largest web sites in the world so you probably use this every day but might not know exactly what the company is so our network spans the globe

### Excerpt da transcript

[Applause] so yeah my name is Marcus I'm a principal engineer at fastly and at the moment I'm focusing on our sort of observability stack for those of you that aren't familiar with fastly and and I wouldn't be surprised if you aren't we power we're a content distribution network and edge cloud and we power but sort of hundreds of the largest web sites in the world so you probably use this every day but might not know exactly what the company is so our network spans the globe we have 51 points of presence which are individual data centers scattered all around the world of those 51 data centers we have 22 terabits of connected network transit to support all of that customer traffic and to get all of the content to you as quickly as possible so as you can imagine the importance of us being able to monitor the performance and reliability of our network is absolutely paramount both not only for our customers that are allowing us to deliver their content but to all of you who want to browse reddit when you're not working so to set the stage let's have a little bit of a chat about how we were monitoring fastly so fastly is a relatively young company we've been around for seven years and we've been monitoring since day one so the original monitoring stack at fastly was ganglia who is familiar with ganglia fewer a few people who still runs it is their primary monitoring okay there's got to be one or two for sure okay so ganglia is an our ID based monitoring solution it was originally designed to support monitoring of high performance computing clusters so a lot of its functionality is centered around sort of this concept of clustering and having groups of machines that are mostly homogeneous so for us it was a pretty good fit because we have all of these data centers that are relatively the same but it did have some limitations so as we scaled as a company so from you know seven years starting seven years ago we started to have some growing pains with our ganglia infrastructure there's a pretty heavy operational overhead so ganglia is designed in sort of more traditional approach where you have a central aggregator and all of your infrastructure pushes its metrics to that central aggregator so as our infrastructure was growing we're just ABB's hammering this aggregator with it with more and more traffic it's also quite a complicated system to run there's a lot of components it doesn't provide a lot of observability out of the box for how you can introspect how itse
