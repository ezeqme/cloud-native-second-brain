---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/what-prometheus-means-for-monitoring-vendors/
youtube_url: https://www.youtube.com/watch?v=kkbfO8Ycfk8
youtube_search_url: https://www.youtube.com/results?search_query=What+Prometheus+Means+for+Monitoring+Vendors+PromCon+2018
video_match_score: 1.001
status: video-found
---

# What Prometheus Means for Monitoring Vendors

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/what-prometheus-means-for-monitoring-vendors/
- YouTube: https://www.youtube.com/watch?v=kkbfO8Ycfk8

## Resumo

Speaker: Jorge Salamero Sanz Users have been looking for a better understanding of how Prometheus monitoring and other commercial monitoring tools compare and contrast when it comes to Docker and Kubernetes monitoring. Are they enemies? Lovers?

## Abstract oficial

Speaker: Jorge Salamero Sanz

Users have been looking for a better understanding of how Prometheus monitoring and other commercial monitoring tools compare and contrast when it comes to Docker and Kubernetes monitoring. Are they enemies? Lovers? Twins separated at birth? Let's go there. This talk will discuss the Prometheus ecosystem from a vendor perspective.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/what-prometheus-means-for-monitoring-vendors/
- YouTube: https://www.youtube.com/watch?v=kkbfO8Ycfk8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kkbfO8Ycfk8
- YouTube title: PromCon 2018: What Prometheus Means for Monitoring Vendors
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/what-prometheus-means-for-monitoring-vendors/kkbfO8Ycfk8.txt
- Transcript chars: 13972
- Keywords: prometheus, metrics, monitoring, vendor, server, source, metric, support, companies, started, custom, vendors, cystic, provide, everyone, technology, interface, approach

### Resumo baseado na transcript

okay well thanks everyone for coming my name is Jorge I work at the stake and this is probably one of the most difficult talks I have ever given this can be very polemic and it was easy to speak a lot about cystic but I wanted to do it like more generic more about what should be Prometheus not for cystic obviously I'll talk some details about cystic but more for any monitoring vendor out there but first of all probably wish a thing well what's up money train

### Excerpt da transcript

okay well thanks everyone for coming my name is Jorge I work at the stake and this is probably one of the most difficult talks I have ever given this can be very polemic and it was easy to speak a lot about cystic but I wanted to do it like more generic more about what should be Prometheus not for cystic obviously I'll talk some details about cystic but more for any monitoring vendor out there but first of all probably wish a thing well what's up money train vendor and I was thinking I was looking at the ecosystem and I could see at least three kinds of monitoring companies working around Prometheus people who started or companies who started to like more traditional in monitoring companies who build databases and they authority are all they expanded into the monitoring so things and companies that started after Prometheus and gizzard Prometheus as their base or base technology I'm going to focus on the first one first of all because as they probably fits into that category but also because it's probably the most challenging sector and next we need to talk about what's Prometheus I'm pretty sure everyone here knows what's Prometheus but when we talk to the general audience not folks here Prometheus means many things it's a metric server a time series database and should be only that where in reality or in practice means a few other things our entire monitoring stack built from many different components so they have different names but we understand that as a Prometheus as well a matrix interface and we just saw that like Prometheus metrics becoming open metrics and also wait instrument very cold the Prometheus library so there are many things that we just get together under the Prometheus name so let me talk to all these things that Prometheus means and how can as our monitoring vendor approach through the different areas when us how monitoring Mandir when I had to provide my customers a way to implement custom metrics I have a bunch of different options I have DMX for those who were using Java study recently even X bars for people using go and with most of the companies yesterday is to provide their own API and then either the company had to maintain a set of libraries for different languages or the end users have to do their own thing which was a pain in the ass but not for the customer but also for everyone like this over a vendor had to maintain a huge code base with very little value because it was not differentiating from any other vendor everyone ha
