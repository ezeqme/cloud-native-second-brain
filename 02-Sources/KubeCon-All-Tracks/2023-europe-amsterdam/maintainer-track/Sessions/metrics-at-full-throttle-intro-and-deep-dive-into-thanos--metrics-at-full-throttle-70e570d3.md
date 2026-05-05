---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Saswata Mukherjee", "Filip Petkovski", "Shopify"]
sched_url: https://kccnceu2023.sched.com/event/1HzdL/metrics-at-full-throttle-intro-and-deep-dive-into-thanos-saswata-mukherjee-filip-petkovski-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Metrics+at+Full+Throttle%3A+Intro+and+Deep+Dive+Into+Thanos+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Metrics at Full Throttle: Intro and Deep Dive Into Thanos - Saswata Mukherjee & Filip Petkovski, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Saswata Mukherjee, Filip Petkovski, Shopify
- Schedule: https://kccnceu2023.sched.com/event/1HzdL/metrics-at-full-throttle-intro-and-deep-dive-into-thanos-saswata-mukherjee-filip-petkovski-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Metrics+at+Full+Throttle%3A+Intro+and+Deep+Dive+Into+Thanos+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Metrics at Full Throttle: Intro and Deep Dive Into Thanos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HzdL/metrics-at-full-throttle-intro-and-deep-dive-into-thanos-saswata-mukherjee-filip-petkovski-shopify
- YouTube search: https://www.youtube.com/results?search_query=Metrics+at+Full+Throttle%3A+Intro+and+Deep+Dive+Into+Thanos+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2GokLB5_VfY
- YouTube title: Metrics at Full Throttle: Intro and Deep Dive Into Thanos - Saswata Mukherjee & Filip Petkovski
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/metrics-at-full-throttle-intro-and-deep-dive-into-thanos/2GokLB5_VfY.txt
- Transcript chars: 33002
- Keywords: thanos, prometheus, series, storage, object, gateway, global, metrics, engine, operators, receive, sidecar, blocks, across, request, queries, operator, samples

### Resumo baseado na transcript

all right um thank you everyone for coming we didn't expect such a full room um so this session will be uh both an introduction and a deep dive into Thanos so the first part we're going to do like an overview of Thanos what it is how you run it and then in the second part we will cover some of the improvements that have been done recently and then we'll talk about some more exciting stuff some concrete use cases and so on maybe just a quick show

### Excerpt da transcript

all right um thank you everyone for coming we didn't expect such a full room um so this session will be uh both an introduction and a deep dive into Thanos so the first part we're going to do like an overview of Thanos what it is how you run it and then in the second part we will cover some of the improvements that have been done recently and then we'll talk about some more exciting stuff some concrete use cases and so on maybe just a quick show of hands how many people here run Thanos in production already okay that's so for you you might find the first part of it boring but maybe you'll also learn something new before we get started uh just a quick round of introductions my name is Philip I'm a production engineer at Shopify I work in the infrastructure team also part of the towns maintainers team and also in the past I helped maintain Primitives operator and Cube State metrics and with me today's sauce water yeah so my name is I'm a software engineer at Red Hat where I work on an internal monitoring platform I'm also a maintenance Thanos and was previously a g-socumented under the same project I also helped maintain a couple of cncf adjacent projects like mdocs and observatorium you can find me as ATM code on Twitter GitHub or pretty much anywhere else all right um okay so now getting into the good stuff um it's kind of hard to talk about Thanos without mentioning Prometheus first um Prometheus I expect most of you to be to have heard at least about it it's a standalone monitoring server or system that you drop in your environment very close to your applications for me Tuesday scrapes metrics from applications and then stores them locally so Prometheus doesn't have any external dependencies which means you can't actually offload metrics data into an external database and as a result it has to store those metrics on disk it also has like a very flexible query language which we call pramcal and using that query language we can also write alerts which means we can have alerts that are constantly executed and they let us know when something goes wrong when if for example a threshold is violated uh prameters can fire on the Earth and so if we zoom into the Prometheus design and what it's composed of we see four kind of key modules which are present in the Prometheus code base and functionality which are very relevant for what Thanos is um for what we'll be speaking today so we have the rule manager which executes alerting rules we have the query engine which
