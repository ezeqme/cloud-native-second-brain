---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability", "Visualization Dashboards", "Community"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/prometheus-at-prezi-replacing-10-years-of-anti-patterns/
youtube_url: https://www.youtube.com/watch?v=2vnvmE3-HMM
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+at+Prezi%3A+Replacing+10+Years+of+Anti-patterns+PromCon+2019
video_match_score: 1.003
status: video-found
---

# Prometheus at Prezi: Replacing 10 Years of Anti-patterns

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/prometheus-at-prezi-replacing-10-years-of-anti-patterns/
- YouTube: https://www.youtube.com/watch?v=2vnvmE3-HMM

## Resumo

Speaker: David Guerrero This talk goes over how our micro-services infrastructure is set up at Prezi, how it used to be monitored with convoluted and unreliable solutions, how we introduced Prometheus to all of our services, what we learned, where we failed, how it improved our engineers' life and what it enables us to do now. We recently spent 8 months redesigning our entire monitoring infrastructure, replacing 10 years of unreliable organically grown solutions to a uniform and highly available Prometheus-based platform. Our services being mostly written in Django/Python, we spent a lot of time getting in right and contributed back to the community (see https://engineering.prezi.com/prometheus-unchained-331b7ab8737, https://github.com/prezi/django-exporter).

## Abstract oficial

Speaker: David Guerrero

This talk goes over how our micro-services infrastructure is set up at Prezi, how it used to be monitored with convoluted and unreliable solutions, how we introduced Prometheus to all of our services, what we learned, where we failed, how it improved our engineers' life and what it enables us to do now. We recently spent 8 months redesigning our entire monitoring infrastructure, replacing 10 years of unreliable organically grown solutions to a uniform and highly available Prometheus-based platform. Our services being mostly written in Django/Python, we spent a lot of time getting in right and contributed back to the community (see https://engineering.prezi.com/prometheus-unchained-331b7ab8737, https://github.com/prezi/django-exporter). This was also the opportunity to revise our alerting philosophy (using the famous "My Philosophy on Alerting") and had to re-educate all of our engineers on how to alert and how to make great dashboards (or not making any and just using generic alerts and dashboards). A key point was to measure the impact of these changes by counting the alerts and how engineer react to them (was the alert actionable?). Based on that, we can see how well our practices are performing and react if necessary.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/prometheus-at-prezi-replacing-10-years-of-anti-patterns/
- YouTube: https://www.youtube.com/watch?v=2vnvmE3-HMM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2vnvmE3-HMM
- YouTube title: PromCon EU 2019: Prometheus at Prezi: Replacing 10 Years of Anti-patterns
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/prometheus-at-prezi-replacing-10-years-of-anti-patterns/2vnvmE3-HMM.txt
- Transcript chars: 26140
- Keywords: actually, platform, monitoring, metrics, practices, primitives, second, custom, finally, matrix, quality, better, logs, alerts, already, provide, configuration, around

### Resumo baseado na transcript

[Music] so I am David sorry I'm a s3 at frizzy and I'm gonna talk about how we introduced primitives so I was the project lead doing that project so what's crazy we are an online platform where you can basically create and browse presentations like this one in terms of scale now we have over hundred million users registered and behind that 15 engineering teams around 100 back-end micro services most of them are in Python and Django some in Scala and very few in go and we also

### Excerpt da transcript

[Music] so I am David sorry I'm a s3 at frizzy and I'm gonna talk about how we introduced primitives so I was the project lead doing that project so what's crazy we are an online platform where you can basically create and browse presentations like this one in terms of scale now we have over hundred million users registered and behind that 15 engineering teams around 100 back-end micro services most of them are in Python and Django some in Scala and very few in go and we also have web desktop and mobile clients and we need to monitor all of these so monitoring the issue is like Prezi was born in 2009 and guess what happens if you build 10 years of organic build up and also if you have a huge lack of best practices what happens then what you end up with this huge mitering monster that we used to have it was very slow and stable we used to have to fix it often so we had a lot of issues with this but let me just walk you through how it used to look like someone walked you through the architecture let's say you have a microservice and if it needs behaves you want to get the page in our case we use a duty mostly and also slack so let's let's go through how it how it used to look like so the service didn't have any notion of metric there was only logs so debug logs these dogs will go down to a log processing node and that flow'd process signal every 60 second it used to process the last minute of logs actually we had a custom Python script for every one of our back-end services a different Python script and that would parse these logs and output matrix from them and then this matrix would end up into a graphite which is a time series database and then I know that you have matrix then you can create them if you want to evaluate errors so for that we had what we call a checker node which would every 60 second evaluate rules against our graphite and then from that you have an erecting state and now you can say okay I have my editing state I can just send that to parity or stack actually it's not that simple so every 60 seconds actually the chequered node would send the state of others as logs to another node which was caught this multiplexer node which would then convert this alert status logs back as a metric in through another graphite why a different one good question but I said it's a multiplexer so it was doing a second thing it was also sending finally the earth state to one lead singer which is an agarose fork if you don't know and finally yeah I think I can
