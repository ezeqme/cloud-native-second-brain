---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/best-practices-and-beastly-pitfalls/
youtube_url: https://www.youtube.com/watch?v=_MNYuTNfTb4
youtube_search_url: https://www.youtube.com/results?search_query=Best+Practices+and+Beastly+Pitfalls+PromCon+2017
video_match_score: 0.867
status: video-found
---

# Best Practices and Beastly Pitfalls

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/best-practices-and-beastly-pitfalls/
- YouTube: https://www.youtube.com/watch?v=_MNYuTNfTb4

## Resumo

Speaker: Julius Volz Julius gives an overview over the most important best practices and most treacherous pitfalls when starting to use Prometheus. Video link - Slides

## Abstract oficial

Speaker: Julius Volz

Julius gives an overview over the most important best practices and most treacherous pitfalls when starting to use Prometheus.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/best-practices-and-beastly-pitfalls/
- YouTube: https://www.youtube.com/watch?v=_MNYuTNfTb4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_MNYuTNfTb4
- YouTube title: PromCon 2017: Best Practices and Beastly Pitfalls  - Julius Volz
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/best-practices-and-beastly-pitfalls/_MNYuTNfTb4.txt
- Transcript chars: 34843
- Keywords: prometheus, metric, metrics, series, actually, labels, already, basically, server, create, alerts, values, single, generally, alerting, requests, counters, number

### Resumo baseado na transcript

[Music] next up we've gotta be secured who's most of you won't know him he's pretty new to Prometheus his coach Julius and he's be telling about he'll be talking about best practices and beastie controls yeah I'm probably actually the person with the longest years of Prometheus experience as well all right welcome to Prometheus best practices in beastly pitfalls I had to put the beastly in there for Brian because that's like it alliteration type kind of thing that makes it sound more exciting so as you might

### Excerpt da transcript

[Music] next up we've gotta be secured who's most of you won't know him he's pretty new to Prometheus his coach Julius and he's be telling about he'll be talking about best practices and beastie controls yeah I'm probably actually the person with the longest years of Prometheus experience as well all right welcome to Prometheus best practices in beastly pitfalls I had to put the beastly in there for Brian because that's like it alliteration type kind of thing that makes it sound more exciting so as you might know Prometheus the monitoring system was named after this person here Prometheus the ancient Greek Titan and was he most famous for for stealing the fire from the gods and bringing it to the humans and so that's amazing but you know oh let me just get rid of this mirror display kind of thing here yeah as a punishment for that he got tied to rock for all of eternity by the gods and basically got his liver picked out every day again and again and the tree grew again and again and as Richard here likes to say sometimes Prometheus feels more like in the first picture but on some days the fields you're like using from it just feels more like in the second picture and so the goal of this talk is to make it you feel at least somewhat more like in the you know make you feel more often like you're in the in the first picture like illuminating your systems it's kind of in I would say in entry level some intermediate kind of level talk stuff and you've already heard some of it today from other speakers I'm going to cover instrumentation alerting and querying I had architecture and topology in there earlier but then I noticed I only have a 20 minute slot so that's what we have for now so I'll start pretty general with instrumentation not really premiere specific but Prometheus is a very efficient metric storing system and it's all about having good white box instrumentation in your software so really one big recommendation is to add metrics through all throughout all of your major components of your software including libraries that that they use so that you don't have to wrap any libraries that you use with metrics spread the metric very liberally everywhere where you would traditionally have had or still have a lot line just add a dimensionless counter like you know Prometheus is very good at handling big dimension dimensional metrics but the ones that don't even have any dimensions they are so cheap just add them everywhere and it just makes it very easy to fi
