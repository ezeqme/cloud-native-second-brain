---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "101 Track"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Jesus Angel Samitier", "David Lorite Solanas", "Sysdig"]
sched_url: https://kccncna2022.sched.com/event/182Ey/dont-be-greedy-rightsize-your-kubernetes-cluster-with-prometheus-jesus-angel-samitier-david-lorite-solanas-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=Don%27t+Be+Greedy%3A+Rightsize+Your+Kubernetes+Cluster+With+Prometheus+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Don't Be Greedy: Rightsize Your Kubernetes Cluster With Prometheus - Jesus Angel Samitier & David Lorite Solanas, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[101 Track]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Jesus Angel Samitier, David Lorite Solanas, Sysdig
- Schedule: https://kccncna2022.sched.com/event/182Ey/dont-be-greedy-rightsize-your-kubernetes-cluster-with-prometheus-jesus-angel-samitier-david-lorite-solanas-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=Don%27t+Be+Greedy%3A+Rightsize+Your+Kubernetes+Cluster+With+Prometheus+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Don't Be Greedy: Rightsize Your Kubernetes Cluster With Prometheus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ey/dont-be-greedy-rightsize-your-kubernetes-cluster-with-prometheus-jesus-angel-samitier-david-lorite-solanas-sysdig
- YouTube search: https://www.youtube.com/results?search_query=Don%27t+Be+Greedy%3A+Rightsize+Your+Kubernetes+Cluster+With+Prometheus+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SGGQytM-Nfw
- YouTube title: Don't Be Greedy: Rightsize Your Kubernetes Cluster... - Jesus Angel Samitier & David Lorite Solanas
- Match score: 0.794
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/dont-be-greedy-rightsize-your-kubernetes-cluster-with-prometheus/SGGQytM-Nfw.txt
- Transcript chars: 26432
- Keywords: limits, application, resources, request, requests, question, memory, applications, monitor, cluster, scenario, happens, wasting, depends, prometheus, workloads, amount, higher

### Resumo baseado na transcript

hi everyone thanks for joining us today here uh before we get started we have a couple of questions we'd like to to ask you today how many of you set their requests in your kubernetes workloads okay nice how many of you know people that doesn't do it yeah well-known people I've been one of them though so it's no big deal and how many of you say it sometimes higher requests just in case because you want your application to run smoothly you want you don't want problems lot of money okay so what are the conclusions here uh we learned that our application was lighter than we thought we we thought it was a more complex application and it runs with less resources we also saved 75 dollars a month for yes one wordload which is great but the most important thing from my perspective is that we are starting a workflow that is easily repeatable to monitor the resource usage we created some dashboards depending on its use case with those queries with those metrics we

### Excerpt da transcript

hi everyone thanks for joining us today here uh before we get started we have a couple of questions we'd like to to ask you today how many of you set their requests in your kubernetes workloads okay nice how many of you know people that doesn't do it yeah well-known people I've been one of them though so it's no big deal and how many of you say it sometimes higher requests just in case because you want your application to run smoothly you want you don't want problems there's a deadline you don't want surprises okay so we might have some greedy greedy developers here my name is Jesus and my name is David we work at systic we help our customers understand their kubernetes clusters and we are also the maintainers of promcad.io which is an open source project that gives you a curated lists of Prometheus exporters that are just ready to go you can go there search for the technology that you want to Monitor and it's very straightforward it helps you configuring your primitive jobs your exporter Etc so there is a problem with the real developers right and what what happens here is that knowing the exact amount of resources that your application needs to use is a really complicated matter right so we don't normally know how to do it so in this talk we are going to to show you guys how we uh right size the request of our clusters for a lot of benefits that we'll discuss later so first normally agree developer will set higher limits and higher requests so what happens when you set higher limits uh well first if you set lower limits you might kill your application your CPU might throttle you you might have some boss kills by the out of memory but on the other hand if you if you set two high limits you might be a starving other applications in the cluster if the usage are Rises right something really similar happens with requests if you set low requests is the same right CPU throttling memory kills but if you set higher requests at first your obligation runs smoothly but you might be doing core uh harder for kubernetes to allocate more pots and also you're wasting a lot of resources you are buying for more CPU and memory that you won't use so you are you you might be wasting some money right this is let's explain first what are the limits okay let's do a quick recap what are the limits okay the limits are the amount of the maximum amount of resources that your application can use but this resources are not guaranteed this resources depends on the available resource th
