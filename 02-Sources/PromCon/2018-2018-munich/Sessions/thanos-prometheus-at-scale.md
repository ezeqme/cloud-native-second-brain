---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Kubernetes", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/thanos-prometheus-at-scale/
youtube_url: https://www.youtube.com/watch?v=Fb_lYX01IX4
youtube_search_url: https://www.youtube.com/results?search_query=Thanos+-+Prometheus+at+Scale+PromCon+2018
video_match_score: 0.93
status: video-found
---

# Thanos - Prometheus at Scale

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/thanos-prometheus-at-scale/
- YouTube: https://www.youtube.com/watch?v=Fb_lYX01IX4

## Resumo

Speakers: Bartłomiej Płotka Fabian Reinartz The Prometheus Monitoring system has been thriving for several years. Along with its powerful data model, operational simplicity and reliability have been a key factor in its success. However, some questions were still largely unaddressed to this day.

## Abstract oficial

Speakers:


Bartłomiej Płotka
Fabian Reinartz


The Prometheus Monitoring system has been thriving for several years. Along with its powerful data model, operational simplicity and reliability have been a key factor in its success. However, some questions were still largely unaddressed to this day. How can we store historical data at the order of petabytes in a reliable and cost-efficient way? Can we do so without sacrificing responsive query times? And what about a global view of all our metrics and transparent handling of HA setups?

Thanos takes Prometheus' strong foundations and extends it into a clustered, yet coordination free, globally scalable metric system. It retains Prometheus's simple operational model and even simplifies deployments further. Under the hood, Thanos uses highly cost-efficient object storage that's available in virtually all environments today. By building directly on top of the storage format introduced with Prometheus 2.0, Thanos achieves near real-time responsiveness even for cold queries against historical data. All while having virtually no cost overhead beyond that of the underlying object storage.

We will show the theoretical concepts behind Thanos and demonstrate how it seamlessly integrates into existing Prometheus setups.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/thanos-prometheus-at-scale/
- YouTube: https://www.youtube.com/watch?v=Fb_lYX01IX4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Fb_lYX01IX4
- YouTube title: PromCon 2018: Thanos - Prometheus at Scale
- Match score: 0.93
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/thanos-prometheus-at-scale/Fb_lYX01IX4.txt
- Transcript chars: 24521
- Keywords: basically, actually, prometheus, storage, object, tunnels, blocks, cluster, another, single, resolution, server, series, multiple, global, sidecar, pretty, running

### Resumo baseado na transcript

[Applause] it's mine okay hello I think everyone I guess everyone is ready for some after lunch nap right but hopefully not so hello everyone I'm my name is Bartek and I work for the company called improbable and this is Fabian who worked with us for a short time between his role at the septic licked and caress and in the current role at Google and we are really really excited to introduce you to the tano's our open source project that we started in the by the end

### Excerpt da transcript

[Applause] it's mine okay hello I think everyone I guess everyone is ready for some after lunch nap right but hopefully not so hello everyone I'm my name is Bartek and I work for the company called improbable and this is Fabian who worked with us for a short time between his role at the septic licked and caress and in the current role at Google and we are really really excited to introduce you to the tano's our open source project that we started in the by the end of the last year we address this talk to those who are not yet familiar with the tunnels but also for those that maybe have seen our blog post improbable blog post about tunnels maybe experimented a little bit with tunnels already or even deployed that on their environments so by the end of this talk I would like you to know what a nose is what problem it solves and how to use it and how to deploy it so next 20 minutes we look as false first we will talk what problems are you it's worth to consider when running from to use at scale secondly we will cover how proton O's helps in those areas and by the end we will talk shortly about explained example deployment models so I need a clicker yep so everything starts with the single prompted server and I think it is safe to say that single prom to use server is extremely powerful it has variable it was it has proven to be reliable it has flexible query language and it is capable to scrape 5 million series time series at the same time we were out using too many resources so it's great and the primitives to is even more improved thanks of the hard work of the Proteus community for example retention can be a lot of longer even with just a local storage but how all of those things are features together when we are talking about scale and in fact when we talk when we are talking about the scale that is out of the scope for the single prompt used server we are not necessarily talking about the performance limits usually the usual reason why people scale out from to use servers are because the service that you want to monitor so monitor that monitoring targets are grouped within multiple of isolated clusters our data centers that are spread across the world within different geographical regions and if the recommended way to run Prometheus is within the same failure domain so the same network the same region we have no other choice than actually running one on more primitive server in each cluster so let's maybe focus on on the issues we can spot while using th
