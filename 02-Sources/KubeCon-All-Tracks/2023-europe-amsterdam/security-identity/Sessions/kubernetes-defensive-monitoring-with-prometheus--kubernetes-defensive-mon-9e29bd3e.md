---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Observability", "Security", "Kubernetes Core"]
speakers: ["David de Torres Huerta", "Mirco De Zorzi", "Sysdig"]
sched_url: https://kccnceu2023.sched.com/event/1HyWv/kubernetes-defensive-monitoring-with-prometheus-david-de-torres-huerta-mirco-de-zorzi-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Defensive+Monitoring+with+Prometheus+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes Defensive Monitoring with Prometheus - David de Torres Huerta & Mirco De Zorzi, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Observability]], [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: David de Torres Huerta, Mirco De Zorzi, Sysdig
- Schedule: https://kccnceu2023.sched.com/event/1HyWv/kubernetes-defensive-monitoring-with-prometheus-david-de-torres-huerta-mirco-de-zorzi-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Defensive+Monitoring+with+Prometheus+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes Defensive Monitoring with Prometheus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWv/kubernetes-defensive-monitoring-with-prometheus-david-de-torres-huerta-mirco-de-zorzi-sysdig
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Defensive+Monitoring+with+Prometheus+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ammf8oJhPkY
- YouTube title: Kubernetes Defensive Monitoring with Prometheus - David de Torres Huerta & Mirco De Zorzi, Sysdig
- Match score: 0.756
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-defensive-monitoring-with-prometheus/Ammf8oJhPkY.txt
- Transcript chars: 20934
- Keywords: metrics, cluster, monitoring, prometheus, trying, access, someone, anomaly, important, events, detection, detect, actually, introduce, metric, attacker, threshold, defensive

### Resumo baseado na transcript

my name is David de Torres I work as engineer manager at cesdec but I am also maintainer of the open source project pronka.io and I come here with my friend I'm Mirko de zordi I'm a software engineer assistant and I work on the read path of monitor well as I said this is an exploratory talk and we want to introduce the concept of defensive monitoring but first we want to give some context because here for sure there are some people that works in security and other

### Excerpt da transcript

my name is David de Torres I work as engineer manager at cesdec but I am also maintainer of the open source project pronka.io and I come here with my friend I'm Mirko de zordi I'm a software engineer assistant and I work on the read path of monitor well as I said this is an exploratory talk and we want to introduce the concept of defensive monitoring but first we want to give some context because here for sure there are some people that works in security and other people that works in monitoring we want to introduce a bit some of the tools that we will use and compare first to have some context for the talk how many of you have used products in production Prometheus or have some knowledge about Prometheus well great I'm happy to see that cncf project it is the de facto standard for monitoring metrics improve in kubernetes and well what it does is simple it gets metrics and stores and visualize the results of the metrics I will not get into the details on this but what you need to know is that almost everything in your cluster expose Prometheus metrics especially the kubernetes elements so knowing this you are interested to see the metrics they seem something like this Prometheus is using a human readable format that is called open metrics that you can access to any of these endpoints of these kubernetes elements that are exposing metrics and you can see something like this this is great because you can see what they are exposing the name of the labels the value whatever but this is not useful what Prometheus makes is that this reads every 60 seconds this endpoints it store these and then through a query language that it is called prompt ql you can query that as a database and make application make mats and make a lot of different manipulation of data to get different results and this is and this is something that you can see in Prometheus for example so there is another tool that we will talk about during this talk so let's say introduce Falco for who whoever hasn't ever heard of it um it's as open source sensitive project that joined the cncf a couple of years ago and it was born as a way to look into what's happening inside of our kernel of a machine Creator rules upon these events and alert as an example you can create an alert whenever someone opens a shell instead of a container or through some plugins you can also create rules based on kubernetes events and AWS events for example if someone is modifying a config map with some determined values you ca
