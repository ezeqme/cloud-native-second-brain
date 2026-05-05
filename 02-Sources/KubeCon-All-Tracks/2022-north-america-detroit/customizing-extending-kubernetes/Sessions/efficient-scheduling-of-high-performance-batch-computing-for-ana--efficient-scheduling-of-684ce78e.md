---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Krzysztof Adamski", "Tinco Boekestijn", "ING"]
sched_url: https://kccncna2022.sched.com/event/182HX/efficient-scheduling-of-high-performance-batch-computing-for-analytics-workloads-with-volcano-krzysztof-adamski-tinco-boekestijn-ing
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Scheduling+Of+High+Performance+Batch+Computing+For+Analytics+Workloads+With+Volcano+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Efficient Scheduling Of High Performance Batch Computing For Analytics Workloads With Volcano - Krzysztof Adamski & Tinco Boekestijn, ING

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Krzysztof Adamski, Tinco Boekestijn, ING
- Schedule: https://kccncna2022.sched.com/event/182HX/efficient-scheduling-of-high-performance-batch-computing-for-analytics-workloads-with-volcano-krzysztof-adamski-tinco-boekestijn-ing
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Scheduling+Of+High+Performance+Batch+Computing+For+Analytics+Workloads+With+Volcano+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Efficient Scheduling Of High Performance Batch Computing For Analytics Workloads With Volcano.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HX/efficient-scheduling-of-high-performance-batch-computing-for-analytics-workloads-with-volcano-krzysztof-adamski-tinco-boekestijn-ing
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Scheduling+Of+High+Performance+Batch+Computing+For+Analytics+Workloads+With+Volcano+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=brxJqOEjJ-c
- YouTube title: Efficient Scheduling Of High Performance Batch Computing For... Krzysztof Adamski & Tinco Boekestijn
- Match score: 0.814
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/efficient-scheduling-of-high-performance-batch-computing-for-analytics/brxJqOEjJ-c.txt
- Transcript chars: 23218
- Keywords: cluster, essentially, possible, platform, volcano, resources, available, resource, scheduling, little, running, itself, towards, scheduler, executors, performance, hadoop, actually

### Resumo baseado na transcript

hello welcome to our talk my name is Chris and together with Tinker we're gonna take you on a short Journey how we adapted Cloud native tools to build our data analytics platform and how the recent addition to that stack with those Advanced schedulers help us to you know achieve a bigger scale or operate in that multi-tenant environment so that's going to be our story but just to begin with we're going to introduce to you to our company so ing is a financial institution that operates globally

### Excerpt da transcript

hello welcome to our talk my name is Chris and together with Tinker we're gonna take you on a short Journey how we adapted Cloud native tools to build our data analytics platform and how the recent addition to that stack with those Advanced schedulers help us to you know achieve a bigger scale or operate in that multi-tenant environment so that's going to be our story but just to begin with we're going to introduce to you to our company so ing is a financial institution that operates globally with European Europe I have over 52 000 employees working for us yeah with our mission is to empower people to stay ahead in life and business and also the truths of the company are from the deep economic crisis of the 20s of the 20th century our mission right now is also to help to transition our world into the new era with uh to shift in a low carbon future and to speed up the innovation in finance being like over 10 years in that banking industry is also a fascinating area where a lot of regulations are there so it's adopting a new technology it's never easy but also gives you because one of the most important thing in the bank is trust that that was the way we want to handle data with respect to whatever it's only required to the data to be handled and to respect your rights in that regard the mission uh for the company but the mission for our platform is to become a data driven what we want to emphasize here is like support our employees with the self-service platform so we are in a platform economy and what what we built the mission is to empower you to build on top of that platform and to solve the business needs the growth factor so we started around 2018 the whole platform rules are in 2013 when we started adopting open source technology to bootstrap the product initiatives in 2018 we are starting to look in the new version of the platform when finally we see that the transition towards the cloud native tools help us to to build the platform with the new foundation on the infrastructure layer the numbers may be not impressive but we have a stable growth since then and the adoption rate is is growing and over 400 projects exist on our data index platform so that self-service Paradigm really helped with the adoption rate what we what we built is essentially a product of the product driven mindset is something that is embedded in our in our mindset using the model open source technology what you see here is like an entry point to our platform that allows users t
