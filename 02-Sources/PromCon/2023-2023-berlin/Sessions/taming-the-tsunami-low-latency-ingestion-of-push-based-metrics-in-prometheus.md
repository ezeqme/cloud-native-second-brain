---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Cost Optimization", "Community"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/taming-the-tsunami-low-latency-ingestion-of-push-based-metrics-in-prometheus/
youtube_url: https://www.youtube.com/watch?v=W81x1j765hc
youtube_search_url: https://www.youtube.com/results?search_query=Taming+the+Tsunami%3A+low+latency+ingestion+of+push-based+metrics+in+Prometheus+PromCon+2023
video_match_score: 1.051
status: video-found
---

# Taming the Tsunami: low latency ingestion of push-based metrics in Prometheus

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Cost Optimization]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/taming-the-tsunami-low-latency-ingestion-of-push-based-metrics-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=W81x1j765hc

## Resumo

Speaker(s): Filip Petkovski & Pedro Tanaka Adopting an effective strategy for capturing metric data is a critical aspect of managing large-scale operations. At Shopify, our journey involved integrating push-based metrics into a Prometheus-based system, a challenge imposed by our applications that were already instrumented with Statsd. In this talk, we will share our journey of scaling our metric pipeline using a push-based approach and integrating it into a system that serves thousands of applications with throughput on the order of Gigabytes per second.

## Abstract oficial

Speaker(s): Filip Petkovski & Pedro Tanaka

Adopting an effective strategy for capturing metric data is a critical aspect of managing large-scale operations. At Shopify, our journey involved integrating push-based metrics into a Prometheus-based system, a challenge imposed by our applications that were already instrumented with Statsd.

In this talk, we will share our journey of scaling our metric pipeline using a push-based approach and integrating it into a system that serves thousands of applications with throughput on the order of Gigabytes per second. We'll delve into the benefits and challenges of push-based monitoring, offering insights into why it made sense in our context, despite being less conventional in the Prometheus community. In addition, we will discuss the introduction of native histograms in Prometheus 2.40 and how it significantly contributed to our success.

Lastly, we will provide an in-depth overview of our pipeline's architecture, focusing on the role of our custom-built Statsd Load Balancer and the adapted Statsd Exporter, an open-source tool from the creators of Prometheus. These key components have allowed us to effectively manage high cardinality metrics in a cost-effective manner, something which is still quite challenging with a pull-based approach. If you're managing a Prometheus stack with applications using push-based instrumentation, this talk could provide a fresh perspective and valuable insights.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/taming-the-tsunami-low-latency-ingestion-of-push-based-metrics-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=W81x1j765hc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=W81x1j765hc
- YouTube title: PromCon 2023 - Taming the Tsunami: Low Latency Ingestion of Push-Based Metrics in Prometheus
- Match score: 1.051
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/taming-the-tsunami-low-latency-ingestion-of-push-based-metrics-in-prom/W81x1j765hc.txt
- Transcript chars: 20573
- Keywords: metric, metrics, exporter, series, application, actually, stattic, cardinality, labels, target, applications, solution, exporters, counter, statsd, memory, balancer, pritus

### Resumo baseado na transcript

all right hello everyone uh so my name is Phillip uh Pedro was supposed to be in person here unfortunately he couldn't make it and a lot of the work that we're going to present he actually did a bunch of it the bulk of it so we've decided to make this a hybrid presentation where uh Pedro's part is pre-recorded we're going to play that in the first part and then I'll do the second part like live in person um before we get started I'll just briefly introduce

### Excerpt da transcript

all right hello everyone uh so my name is Phillip uh Pedro was supposed to be in person here unfortunately he couldn't make it and a lot of the work that we're going to present he actually did a bunch of it the bulk of it so we've decided to make this a hybrid presentation where uh Pedro's part is pre-recorded we're going to play that in the first part and then I'll do the second part like live in person um before we get started I'll just briefly introduce both of us so my name is Philip as I said I am a production engineer at Shopify where I work with Pedro on the on the metric team uh and we handle everything from kind of metric collection to ingestion alerting um dashboarding all of that stuff um also I I'm currently helping maintain the tanos project and in the past I've uh also been involved in Cube State metrix and pri's operator uh Pedro his obviously uh not not here uh he is originally from Brazil uh and he's currently mostly involved in the ker project um so what uh we'll talk about today is very closely related to what you heard about uh oel and push based and Delta yesterday um we'll um briefly talk about um how applications are instrumented at Shopify and spoiler alert we use still use TD uh we'll briefly explain the statsd protocol um maybe just a quick show of hands how many people here have heard of or use statsd wow okay um so yeah this will be very relevant for you and finally we've uh we'll kind of explain how we've we've um I would say successfully managed to merge these two worlds of push based Deltas with pull based uh absolute value scripts um so at this point I think I'm I'm going to kind of hand it off to Virtual Pedro to do the first part hello everyone I hope you're having an amazing program so far before I get started and talk about the solution we adopted for custom matric at Shopify it's important to understand how we work and how our developers interact with infrastructure at the company at chopy we have a long history with rubby and raos we also have one of the biggest rubby apps written in deploying production which is our monolith with over millions of lines of code we also use rubby as default for all of our product development and apart from that we use goong and rust for systems uh assistant programming languages we also have an in-house application platform where developers they don't need to think about kubernetes resources but rather they think about what the application needs to work properly like one web server one
