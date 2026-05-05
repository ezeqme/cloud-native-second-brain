---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Kubernetes", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/storing-16-bytes-at-scale/
youtube_url: https://www.youtube.com/watch?v=b_pEevMAC3I
youtube_search_url: https://www.youtube.com/results?search_query=Storing+16+Bytes+at+Scale+PromCon+2017
video_match_score: 0.763
status: video-found
---

# Storing 16 Bytes at Scale

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/storing-16-bytes-at-scale/
- YouTube: https://www.youtube.com/watch?v=b_pEevMAC3I

## Resumo

Speaker: Fabian Reinartz From the beginning, Prometheus was built as a monitoring system with Cloud Native environments in mind. Orchestration systems such as Kubernetes are rapidly gaining traction and unlock features of highly dynamic environments, such as frequent rolling updates and auto-scaling, for everyone. This inevitably puts new strains on Prometheus as well.

## Abstract oficial

Speaker: Fabian Reinartz

From the beginning, Prometheus was built as a monitoring system with Cloud Native environments in mind. Orchestration systems such as Kubernetes are rapidly gaining traction and unlock features of highly dynamic environments, such as frequent rolling updates and auto-scaling, for everyone. This inevitably puts new strains on Prometheus as well.

In this talk we explore what these challenges are and how we are addressing them by building a new storage layer from the ground up. The new design provides efficient indexing techniques that gracefully handle high turnover rates of monitoring targets and provide consistent query performance. At the same time, it significantly reduces resource requirements and paves the way for advanced features like hot backups and dynamic retention policies.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/storing-16-bytes-at-scale/
- YouTube: https://www.youtube.com/watch?v=b_pEevMAC3I
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=b_pEevMAC3I
- YouTube title: PromCon 2017: Storing 16 Bytes at Scale - Fabian Reinartz
- Match score: 0.763
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/storing-16-bytes-at-scale/b_pEevMAC3I.txt
- Transcript chars: 46397
- Keywords: series, actually, basically, pretty, memory, probably, prometheus, blocks, promises, course, single, compression, storage, samples, second, certain, thousand, values

### Resumo baseado na transcript

[Music] so now a man who needs no introduction [Music] thank you so I'm huggin because I didn't tell you and so I'm going to talk about storing 16 by that scale um if you've looked at the schedule realize that this is sort of like starting off the chorus track and this is because Korres does a bunch of work on from misses upstream and after short break we are now hiring people again so if you're interested in actually working on prometheus upstream and also integrating from easiest

### Excerpt da transcript

[Music] so now a man who needs no introduction [Music] thank you so I'm huggin because I didn't tell you and so I'm going to talk about storing 16 by that scale um if you've looked at the schedule realize that this is sort of like starting off the chorus track and this is because Korres does a bunch of work on from misses upstream and after short break we are now hiring people again so if you're interested in actually working on prometheus upstream and also integrating from easiest with kubernetes and also tectonic opposed I'm just visit our careers page and apply so we slip out of the way let's start so we try to start sixteen by that scale and why do we try that and we want to start time series and time spheres happen to be composed out of samples and simple just like streams of values and each value has a time so I've attached and it's basically the same problem just that we don't have a single time series but a lot of time series and to do this now we somehow I have to also sort of determine like what is the time series right we need a way to address a single series or a set of series and in Prometheus you probably know the data model we have metric names these are meant to sort of give a semantic meaning to the values that are in your time series and then you can sort of fan out or split up this metric using labels so a metric name plus a set of labels and a unique set of values for these navels is a single time series and this allows them to sort of partition this metric space and gain insight around different dimensions and to now select or query different time series you can just select the metric name which gets you all the time series that have this metric name but it can also add they limit us like method equals gets and they also recognize us are just a really powerful way to select across all these series in a multi-dimensional way and of course there's a sort of second dimension to it which is time and so we have this two dimensional plane of series in the vertical axis and time in the horizontal one and for the queer is something we a select series but also we constrain these series of a certain time range and this can be pretty much anything right we can just sort of curvy all series for the last minute or just the last sample we can just curry a single series or set of series for the entire time range we know or any rectangle on this plane reading and that's quite like a lot of degrees of freedom right like we have to basically support any
