---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/observability-and-product-release/
youtube_url: https://www.youtube.com/watch?v=gNk7Y0AW9HI
youtube_search_url: https://www.youtube.com/results?search_query=Observability+and+Product+Release%3A+Leveraging+Prometheus+for+Building+and+Testing+New+Products+at+Digital+Ocean+PromCon+2018
video_match_score: 0.553
status: video-found
---

# Observability and Product Release: Leveraging Prometheus for Building and Testing New Products at Digital Ocean

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/observability-and-product-release/
- YouTube: https://www.youtube.com/watch?v=gNk7Y0AW9HI

## Resumo

Speaker: Sneha Inguva The pillars of observability have long been accepted as key components of any microservice-in-production. But what about those new products - those new features - that have yet to be released? Properly instrumenting and leveraging metrics at this stage is perhaps even more crucial; when a product is yet to be released, identifying and addressing early bugs is critical.

## Abstract oficial

Speaker: Sneha Inguva

The pillars of observability have long been accepted as key components of any microservice-in-production. But what about those new products - those new features - that have yet to be released? Properly instrumenting and leveraging metrics at this stage is perhaps even more crucial; when a product is yet to be released, identifying and addressing early bugs is critical.

Within this talk, I will discuss how we have leveraged Prometheus to properly instrument and test features within the software-defined networking pillar at Digital Ocean. I will highlight instrumentation, key visualizations, as well as takeaways from our experience. Perhaps even more importantly, I will touch upon areas that we can certainly improve upon. Listeners - especially those on product teams - will be able to utilize these learnings and hopefully apply them before their releases as well.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/observability-and-product-release/
- YouTube: https://www.youtube.com/watch?v=gNk7Y0AW9HI
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gNk7Y0AW9HI
- YouTube title: PromCon 2018: Observability and Product Release
- Match score: 0.553
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/observability-and-product-release-leveraging-prometheus-for-building-a/gNk7Y0AW9HI.txt
- Transcript chars: 22988
- Keywords: actually, prometheus, metrics, testing, alerts, product, request, monitoring, instances, number, measure, decided, observability, useful, latency, issues, sequel, rabbitmq

### Resumo baseado na transcript

great hi my name is Sneha and Guba I'm here to talk about Prometheus today as you can guess given that we are at prom con Soho my talk today is about observability and product release basically leveraging Prometheus to build and test new products it's a little bit about myself I'm a software engineer at digitalocean I'm currently on the networking services team and here's a photo of my cat in honor of international cat day which was actually yesterday so some stats um we use Prometheus at my

### Excerpt da transcript

great hi my name is Sneha and Guba I'm here to talk about Prometheus today as you can guess given that we are at prom con Soho my talk today is about observability and product release basically leveraging Prometheus to build and test new products it's a little bit about myself I'm a software engineer at digitalocean I'm currently on the networking services team and here's a photo of my cat in honor of international cat day which was actually yesterday so some stats um we use Prometheus at my company obvious at this point but we use it for you know both monitoring particular services as well as for data center wide like hypervisor and virtual machine monitoring so some stats we have about 90 million or more time series about 85 instances of Prometheus and we scrape at a rate about 1.7 million samples per second but that was not always the case in the olden dark days we didn't use Prometheus we were using Nagios on different plugins like van RP plug-in to do blackbox monitoring this was hard you know operationally and then we also didn't get a lot of introspection into our services we then at some point moved to using collecti stats t graphite this was okay but you know we didn't have great querying abilities and we didn't necessarily have enough dimensionality of our metrics there's also very briefly are actually not briefly enough an open TS DB cluster and the issue with that was it was also difficult to operationally maintain thankfully some kind soul discovered prometheus and we moved to that prometheus is great offers us you know white box monitoring there's multi-dimensional data a lot of labels there's a great querying language it just helps us for like analytical purposes and for just general alerting around the same time we also moved to kubernetes so pre kubernetes we were using chef and bash scripts and other unholy things to deploy services this was difficult once again for various reasons but then luckily moving to kubernetes allowed us to easily update services made it easier to scale up or scale down services and then also given the API service discovery method was very easy to set up Prometheus and alert manager and set up alerting so this is what I discussed last year over at the beginning of this year I joined the network services team at my company which was interesting because whereas in the past I focused on how we were using Prometheus for services that were already in production this year I started to see how we use Prometheus before w
