---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/alert-on-all-the-things-integrating-quicksilver-with-prometheus/
youtube_url: https://www.youtube.com/watch?v=TRi822rw5b8
youtube_search_url: https://www.youtube.com/results?search_query=Alert+on+All+the+Things%3A+Integrating+Quicksilver+with+Prometheus+PromCon+2017
video_match_score: 0.959
status: video-found
---

# Alert on All the Things: Integrating Quicksilver with Prometheus

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/alert-on-all-the-things-integrating-quicksilver-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=TRi822rw5b8

## Resumo

Speaker: Lorenz Bauer Cloudflare provides its services from 115 data centres in 57 countries. One of the most critical systems is a key-value store that replicates configuration data to every single machine, which we recently rewrote from scratch. As developers we were early adopters of Prometheus at Cloudflare, and this talk will explain how we set up Grafana dashboards for monitoring and Alertmanager for alerting, giving us unprecedented insight.

## Abstract oficial

Speaker: Lorenz Bauer

Cloudflare provides its services from 115 data centres in 57 countries. One of the most critical systems is a key-value store that replicates configuration data to every single machine, which we recently rewrote from scratch. As developers we were early adopters of Prometheus at Cloudflare, and this talk will explain how we set up Grafana dashboards for monitoring and Alertmanager for alerting, giving us unprecedented insight. It’ll also cover the gotchas we encountered. Like that one time when we triggered 7000 alerts at once.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/alert-on-all-the-things-integrating-quicksilver-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=TRi822rw5b8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TRi822rw5b8
- YouTube title: PromCon 2017: Alert on All the Things: Integrating Quicksilver with Prometheus - Lorenz Bauer
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/alert-on-all-the-things-integrating-quicksilver-with-prometheus/TRi822rw5b8.txt
- Transcript chars: 16275
- Keywords: prometheus, single, actually, probably, histograms, histogram, inhibition, yesterday, center, metric, milliseconds, alerts, quicksilver, second, europe, global, metrics, working

### Resumo baseado na transcript

[Music] so as was foreshadowed yesterday several times by mash we have Lorenz talking more about cloud fare and how they're doing your tanks exactly hello great ok so the pressures on I'm Lawrence I work as a systems engineer for CloudFlare I'm a colleague of Matt's I'm going to be talking about Quicksilver which is an internal project we have and how we integrated that with the premium Prometheus set up that Matt talked about yesterday I'm going to briefly talk about what Quicksilver isn't how it works and

### Excerpt da transcript

[Music] so as was foreshadowed yesterday several times by mash we have Lorenz talking more about cloud fare and how they're doing your tanks exactly hello great ok so the pressures on I'm Lawrence I work as a systems engineer for CloudFlare I'm a colleague of Matt's I'm going to be talking about Quicksilver which is an internal project we have and how we integrated that with the premium Prometheus set up that Matt talked about yesterday I'm going to briefly talk about what Quicksilver isn't how it works and talk about the two most interesting metrics I think and how they use Prometheus histograms to give us a lot of insight into how the system is working and then I'm going to talk about all of the gotchas that we encountered while doing this work without further that worked one second sorry without further ado you've seen this I'll just point you to the blog which usually has interesting technical stuff so I advise you to check it out now what is Quicksilver it's an internal system that we use to provision configuration information from our that our customers create to our edge so this is the 110a data centers that you've seen yesterday it is what I would call a replicator database and I'll go into a bit of detail why I call replicated versus something else it runs on a few thousand machines it's written and go I was yet saying that and it's a team of three working on it my colleagues Jeffrey and Sami also known on an office so what is quickserver obviously I need a walk because it's such a great system or large I should say at any point in time there's a single what we call root node in Quicksilver and this root node serializes and kind of orchestrates all rights to the system and it takes the data that is written to the system puts it in a in a log entry put the timestamp on it and then there forwards that data on to other nodes which we call the followers which are spread all over the globe and how that is configured isn't always under our control and most of the time mister you will kind of work on that and we can also have a second tier of nodes which do not get that data from the root node but they get data from a different node so there's an intermediate step the whole thing is is basically a tree or a directed acyclic graph if you into that means we don't have any loops and there's a single source of truth and then there's loads more of these now why is this replicated and not distributed I call a replicator because there's actually no guarantee ab
