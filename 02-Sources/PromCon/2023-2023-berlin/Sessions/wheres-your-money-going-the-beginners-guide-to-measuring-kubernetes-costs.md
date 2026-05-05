---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Kubernetes", "Scalability Reliability", "Visualization Dashboards", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/where-your-money-going-the-beginners-guide-to-measuring-kubernetes-costs/
youtube_url: https://www.youtube.com/watch?v=Cm0VDMXnvNA
youtube_search_url: https://www.youtube.com/results?search_query=Where%27s+your+money+going%3F+The+Beginners+Guide+To+Measuring+Kubernetes+Costs+PromCon+2023
video_match_score: 1.049
status: video-found
---

# Where's your money going? The Beginners Guide To Measuring Kubernetes Costs

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/where-your-money-going-the-beginners-guide-to-measuring-kubernetes-costs/
- YouTube: https://www.youtube.com/watch?v=Cm0VDMXnvNA

## Resumo

Speaker(s): Erik Sommer Accurately attributing cloud costs has become a Sisyphean task many companies face. As both the cloud and your systems evolve, it's hard to figure out what exactly is eating up all that money, let alone optimize those costs. In this session, we'll take you over the journey that got us to trustworthy cost estimations for Kubernetes clusters at Grafana Labs.

## Abstract oficial

Speaker(s): Erik Sommer

Accurately attributing cloud costs has become a Sisyphean task many companies face. As both the cloud and your systems evolve, it's hard to figure out what exactly is eating up all that money, let alone optimize those costs. In this session, we'll take you over the journey that got us to trustworthy cost estimations for Kubernetes clusters at Grafana Labs.

You'll get to see how we started, with just the metrics collected from kube-state-metrics and stored within Prometheus. We'll step through crafting the queries to create recording rules that will attribute costs of clusters across many cloud service providers.

Measuring the trends in costs for k8s is easy to get started with. If you're operating a k8s cluster and collecting metrics from kube-state-metrics, you likely already collect enough metrics. Keeping an eye on this and being able to alert on cost changes will allow you to mitigate shock bills in cloud providers.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/where-your-money-going-the-beginners-guide-to-measuring-kubernetes-costs/
- YouTube: https://www.youtube.com/watch?v=Cm0VDMXnvNA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Cm0VDMXnvNA
- YouTube title: PromCon 2023 - Where’s Your Money Going? The Beginners Guide to Measuring Kubernetes Costs
- Match score: 1.049
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/wheres-your-money-going-the-beginners-guide-to-measuring-kubernetes-co/Cm0VDMXnvNA.txt
- Transcript chars: 22502
- Keywords: cost, cluster, metric, little, pretty, memory, resources, actually, simple, difficult, platform, typically, workloads, namespace, another, running, resource, question

### Resumo baseado na transcript

[Music] [Applause] hello my name is Eric Sumer I work with grafana laps at the platform team and it's good that we cut the intro talk to kubernetes short because everything knows it already that's good so where's your money going and this should really be the beginner's guide to measuring kuus costs um first what can you expect from the stock first when you run kubernetes on a hyperscaler you typically get at the end of a mon month bill it will typically doesn't match the metric that you

### Excerpt da transcript

[Music] [Applause] hello my name is Eric Sumer I work with grafana laps at the platform team and it's good that we cut the intro talk to kubernetes short because everything knows it already that's good so where's your money going and this should really be the beginner's guide to measuring kuus costs um first what can you expect from the stock first when you run kubernetes on a hyperscaler you typically get at the end of a mon month bill it will typically doesn't match the metric that you see in your kues cluster and we will get to the point why that is maybe uh we will get to point where we can build up a metal model of how attribute costs in a kubernetes cluster and because of is a promc con there should be some prom well and I'd like to finish up with some shortcomings and maybe some ideas where to go next so sorry sorry at the end of the month you get the typical bill from your CSP provider of choice and what happens to us a lot is that the finance department then comes around and ask us the question why have the costs doubled not doubled all the time but where why are there increases typically you can't see that directly from the bill there are some pointers there you see compute instances some abstract numbers and some would say they are abstract by the sign if you want to be nasty so the next step is maybe you go to the cloud exp power of the CSV CSP maybe you have attributed your workloads nicely with some Tex you can filter it down and you come to the conclusion okay it is a kubernetes cluster that has increased in size that what you not find here is something informations like Nam spaces or anything useful from what you know from your communi cluster so next step is of course you go there what you know metrics but the bad thing is it will not correlate metrics are typically not showing you it can show you of course how many nodes are there in your kubernetes cluster but that we did know already from the bill but not which workload typically was responsible for that only some usage poins and stuff but not how much money by which change was caed and this makes you sad and nobody wants to be sad so to recap the problems are we have typically a disconnect between the billing statement and the metric that we see in our premisus we have the need to attribute some costs of our workloads that are running in kubernetes and optimally pinpoint is down to the namespace level because we all use namespaces right we not just run everything in default I hope so u
