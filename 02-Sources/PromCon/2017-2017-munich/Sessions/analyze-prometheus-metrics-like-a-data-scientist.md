---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/analyze-prometheus-metrics-like-a-data-scientist/
youtube_url: https://www.youtube.com/watch?v=aUOgPdaXOwQ
youtube_search_url: https://www.youtube.com/results?search_query=Analyze+Prometheus+Metrics+like+a+Data+Scientist+PromCon+2017
video_match_score: 0.937
status: video-found
---

# Analyze Prometheus Metrics like a Data Scientist

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/analyze-prometheus-metrics-like-a-data-scientist/
- YouTube: https://www.youtube.com/watch?v=aUOgPdaXOwQ

## Resumo

Speaker: Georg Öttl Gathering software metrics with Prometheus is great and easy. However, at some point there are too many timeseries to craft handwritten rule based alert systems. In this talk I will show how to export data from the Prometheus HTTP API, show how and what to analyze with open-source tools like R, Python SciPi and describe why DevOps and Whitebox Monitoring fits so great here.

## Abstract oficial

Speaker: Georg Öttl

Gathering software metrics with Prometheus is great and easy. However, at some point there are too many timeseries to craft handwritten rule based alert systems. In this talk I will show how to export data from the Prometheus HTTP API, show how and what to analyze with open-source tools like R, Python SciPi and describe why DevOps and Whitebox Monitoring fits so great here. As an outlook I will show how to integrate/export timeseries to machine learning services.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/analyze-prometheus-metrics-like-a-data-scientist/
- YouTube: https://www.youtube.com/watch?v=aUOgPdaXOwQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aUOgPdaXOwQ
- YouTube title: PromCon 2017: Analyze Prometheus Metrics like a Data Scientist - Georg Öttl
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/analyze-prometheus-metrics-like-a-data-scientist/aUOgPdaXOwQ.txt
- Transcript chars: 22485
- Keywords: actually, metrics, linear, improve, science, models, learning, prometheus, basically, prediction, matrix, export, predict, machine, alerts, analysis, format, function

### Resumo baseado na transcript

[Music] so next time we'll have George fo he'll talk about analyzing metrics like a data scientist and he'll be pleased to know that somewhere in our bucket list there's an our exporter from what we have in privy to our own assets hello everybody my name is gear acquittal and that start was to talk analyze Prometheus metrics like like a data scientist to my person itself so to put everything I say into context me I'm an enterprise software developer having a background in data science services and

### Excerpt da transcript

[Music] so next time we'll have George fo he'll talk about analyzing metrics like a data scientist and he'll be pleased to know that somewhere in our bucket list there's an our exporter from what we have in privy to our own assets hello everybody my name is gear acquittal and that start was to talk analyze Prometheus metrics like like a data scientist to my person itself so to put everything I say into context me I'm an enterprise software developer having a background in data science services and thinking around the last two years around the topic of death of deaf development and DevOps and Holmes know basically I'm a developer who likes math and I'm the second guy here will go to paternity leave in a few days so my employee will be a eight month old toddler and my daughter and next starting next week I would say good the objective of this talk is I wanna I wanted in the beginning pushing the limits of trauma tours and I wanted to know their models the alerting models the predictions I had in my dashboards are the good are not good is there a way to make it better than I have done so far and according to my background I actually took the chance and tried to use some data science methods and open source data science tools to improve and this was my goal and my aim to improve our rules and our model I have and the prediction they have and like Prometheus I wanted to bring a bit more light into the dark I wanted to bring I wanted to bring more light into the dark of what's going on in the software we were monitoring and this was my objective when I started with all this work at the beginning inert spoiler this is about the topic where you could drift off into official intelligence and machine learning and so on this is the warning should I do use advanced mathematics and should I use advanced methods to analyze the data from either this gathering or not it's a rule of thumb if you have an system that is doing well you're getting alerts you don't get awake at night without no reasons then keep it as it is stay with the rule-based systems on the other hand if you're not satisfied with your alerts your rules and your predictions data science might give you some insight into how your data is structured and what hidden patterns are in the data that you could use and could exploit to improve your your alerting and your data model so big thing where do you want you to be when you're of where was I or where I expect somebody to be when you start to think about doing
