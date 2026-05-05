---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/whats-new-in-prometheus-and-its-/
youtube_url: https://www.youtube.com/watch?v=lNoFuVScpyg
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+in+Prometheus+and+Its+Ecosystem+PromCon+2023
video_match_score: 0.996
status: video-found
---

# What's New in Prometheus and Its Ecosystem

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/whats-new-in-prometheus-and-its-/
- YouTube: https://www.youtube.com/watch?v=lNoFuVScpyg

## Resumo

Speaker(s): Julien Pivotto & Matthias Loibl Let's have a look at all the recent features and changes in the Prometheus server and the community. We will introduce the new features and see how you can integrate them in your workflows to get a better Prometheus experience.

## Abstract oficial

Speaker(s): Julien Pivotto & Matthias Loibl

Let's have a look at all the recent features and changes in the Prometheus server and the community. We will introduce the new features and see how you can integrate them in your workflows to get a better Prometheus experience.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/whats-new-in-prometheus-and-its-/
- YouTube: https://www.youtube.com/watch?v=lNoFuVScpyg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lNoFuVScpyg
- YouTube title: PromCon 2023 - What's New in Prometheus and Its Ecosystem
- Match score: 0.996
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/whats-new-in-prometheus-and-its-ecosystem/lNoFuVScpyg.txt
- Transcript chars: 23005
- Keywords: prometheus, exporter, client, histograms, actually, always, native, configuration, ecosystem, metrics, exciting, promcon, metric, looking, queries, coming, database, language

### Resumo baseado na transcript

[Music] I guess we can start prob yes have more time for Q&A all right please welcome to the stage with me Julian um he is a longtime Prometheus maintainer and we're going to talk you through Prometheus and its ecosystems and what has happened in the last year since last promcon uh in Munich uh in 2022 so quick show of hands we already did quick show fans who has been here for the first time or a second time at a promc con but who has just recently kind of a special label it's actually just a label under the hood as well but we have a metric name and then we have these labels um that that are used to identify some more specific uh um metrics uh by doing that and it's it's really good because it's super flexible and you don't have an hierarchy so you can uh slice and dice the data as you need it to be um for your queries um yeah and prom is the query language it's a functional query questions there uh we are really open to uh to discuss with you to get the feedback from the community and not only during promcon but like all the year it's really super important for us to learn for the users and to get your

### Excerpt da transcript

[Music] I guess we can start prob yes have more time for Q&A all right please welcome to the stage with me Julian um he is a longtime Prometheus maintainer and we're going to talk you through Prometheus and its ecosystems and what has happened in the last year since last promcon uh in Munich uh in 2022 so quick show of hands we already did quick show fans who has been here for the first time or a second time at a promc con but who has just recently started using Prometheus like for for whom is it like quite new um as a as a thing to use okay couple of hands um but um we'll we'll talk about what is Prometheus regardless so those uh who who know it very well um you can correct me later but um otherwise we'll we'll talk about what Prometheus is so it is a metric based monitoring and alerting stack um you can use it for instrumentation and application uh for for system monitoring as well um it collects metrics uh and stores them and after storing it it makes it queriable um efficiently and you can use all of that to alert on certain things in your system that you don't want to occur and obviously we all love dashboards uh and looking at dashboards so you can put those um queries into into dashboards and make make your um yeah metrics look really really nice um it is for all levels of the stack so whether you're running on bare metal or something like kubernetes or serverless whatever um it it just uses HTTP for the most part um so it it basically runs everywhere these days um quick history as Frederick mentioned in the intro um it started at SoundCloud um you can ask Julius if you want any more details uh he's around um by by Julius and and met PR um they started it after uh coming coming to SoundCloud and wanting something like Prometheus but nothing really existed back in 2012 so they started working on it and it was fully open sourced in 2015 and then in 2016 the cncf was brand new and Prometheus was one of the very first projects who got adopted into the cncf and then also was released as a first uh version uh back in 2016 pretty exciting times I vividly remember this um and then in uh 2017 shortly after Prometheus 2.0 with a full rewrite of the storage happened um and that's kind of the foundation of what Prometheus um still uses and the tsdb um is is since then uh yeah what what we're using in in the way it works like cutting blocks every two hours and stuff that was introduced back then um and in 2018 I think right after uh kubernetes Prometheus graduat
