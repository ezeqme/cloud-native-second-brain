---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Moad Zardab", "Red Hat", "Filip Petkovski", "Shopify"]
sched_url: https://kccnceu2022.sched.com/event/ytsT/distributing-promql-for-fast-and-efficient-kubernetes-fleet-monitoring-moad-zardab-red-hat-filip-petkovski-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Distributing+PromQL+for+Fast+and+Efficient+Kubernetes+Fleet+Monitoring+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Distributing PromQL for Fast and Efficient Kubernetes Fleet Monitoring - Moad Zardab, Red Hat & Filip Petkovski, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Moad Zardab, Red Hat, Filip Petkovski, Shopify
- Schedule: https://kccnceu2022.sched.com/event/ytsT/distributing-promql-for-fast-and-efficient-kubernetes-fleet-monitoring-moad-zardab-red-hat-filip-petkovski-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Distributing+PromQL+for+Fast+and+Efficient+Kubernetes+Fleet+Monitoring+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Distributing PromQL for Fast and Efficient Kubernetes Fleet Monitoring.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytsT/distributing-promql-for-fast-and-efficient-kubernetes-fleet-monitoring-moad-zardab-red-hat-filip-petkovski-shopify
- YouTube search: https://www.youtube.com/results?search_query=Distributing+PromQL+for+Fast+and+Efficient+Kubernetes+Fleet+Monitoring+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fD-j9u8hzgY
- YouTube title: Distributing PromQL for Fast and Efficient Kubernetes Fleet Monitor... Moad Zardab & Filip Petkovski
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/distributing-promql-for-fast-and-efficient-kubernetes-fleet-monitoring/fD-j9u8hzgY.txt
- Transcript chars: 25903
- Keywords: thanos, queries, series, prometheus, sharding, execute, single, across, memory, execution, actually, metric, wanted, cluster, vertical, engine, monitoring, implementation

### Resumo baseado na transcript

all right um thanks everyone for coming um today the so the title of this talk is distribute impromptual expressions um we'll focus in this session on some of the work that we've done uh with mod and with the thomas community on um implementing distributed query execution in the thanos project my name is philip i am a production engineer at shopify and with me today is moat who is a senior software engineer at red hat the agenda that we have today is the following one we'll briefly

### Excerpt da transcript

all right um thanks everyone for coming um today the so the title of this talk is distribute impromptual expressions um we'll focus in this session on some of the work that we've done uh with mod and with the thomas community on um implementing distributed query execution in the thanos project my name is philip i am a production engineer at shopify and with me today is moat who is a senior software engineer at red hat the agenda that we have today is the following one we'll briefly cover why prom ql and the primcal engine is kind of hard to scale at the moment specifically in prometheus and then we'll cover two different approaches that we are working on in thanos namely query push down what we call query push down and query sharding to speed up query execution and then we'll take a look at sharding in practice and at the end we'll cover kind of we'll give a brief outlook of where we hope thanos is going to develop in the future so if we take a look at the current state of prometheus i mean we've heard so many times here at kubecon that it's become very well adopted in the cloud native monitoring space basically anyone that's maybe used the kubernetes cluster has seen a primitive system lying around somewhere it's very effective for real-time monitoring and what's very good about prometheus is this promptql query query language that allows us to write all kinds of expressive queries against what we call time series data and so the ideal use case for prometheus is really the single cluster monitoring whenever we want to go beyond a single cluster there are different challenges that are non-trivial to overcome some of them being just the fact that scraping across boundary network boundaries can be it comes with its own challenges we have to rely on disks for retention this can be hard to move between acs regions clusters and so on and overall the story about how to scale prometheus horizontally is not there yet and that's a conscious design decision so there's nothing wrong with that um and as a result there are all these different projects like cortex thanos recently mimir that come in and uh try to solve some of the scalability issues that prometheus has and if we look at thanos we can essentially store data for as long as we want in s3 buckets in addition to that we get things like write replication multi-tenancy all of this kind of cloud native features that we take for granted today and now that we have all of the data all of this kind of long retention
