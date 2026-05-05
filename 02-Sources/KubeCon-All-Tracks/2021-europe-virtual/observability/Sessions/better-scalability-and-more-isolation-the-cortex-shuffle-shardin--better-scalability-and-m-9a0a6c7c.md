---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Tom Wilkie", "Grafana Labs"]
sched_url: https://kccnceu2021.sched.com/event/iE5o/better-scalability-and-more-isolation-the-cortex-shuffle-sharding-story-tom-wilkie-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Better+Scalability+and+More+Isolation%3F+The+Cortex+%E2%80%9CShuffle+Sharding%E2%80%9D+Story+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Better Scalability and More Isolation? The Cortex “Shuffle Sharding” Story - Tom Wilkie, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Tom Wilkie, Grafana Labs
- Schedule: https://kccnceu2021.sched.com/event/iE5o/better-scalability-and-more-isolation-the-cortex-shuffle-sharding-story-tom-wilkie-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Better+Scalability+and+More+Isolation%3F+The+Cortex+%E2%80%9CShuffle+Sharding%E2%80%9D+Story+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Better Scalability and More Isolation? The Cortex “Shuffle Sharding” Story.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5o/better-scalability-and-more-isolation-the-cortex-shuffle-sharding-story-tom-wilkie-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Better+Scalability+and+More+Isolation%3F+The+Cortex+%E2%80%9CShuffle+Sharding%E2%80%9D+Story+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1OVpogSKxyI
- YouTube title: Better Scalability & More Isolation? The Cortex “Shuffle Sharding” Story - Tom Wilkie, Grafana Labs
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/better-scalability-and-more-isolation-the-cortex-shuffle-sharding-stor/1OVpogSKxyI.txt
- Transcript chars: 24825
- Keywords: cortex, cluster, tenants, shuffle, tenant, sharding, prometheus, outage, isolation, clusters, single, number, grafana, scalable, series, better, global, federation

### Resumo baseado na transcript

hello everyone welcome to better scalability and more isolation the cortex shuffle sharding story hope everyone's having a good kubecon so far so my name's tom i am the vp product at grafana labs um in my what little spare time i have i guess i'm one of the prometheus team um my main contribution being the the remote write code there uh i also started the cortex project which is the horizontally scalable version of prometheus that's part of the cncf sandbox more recently i started loki which is

### Excerpt da transcript

hello everyone welcome to better scalability and more isolation the cortex shuffle sharding story hope everyone's having a good kubecon so far so my name's tom i am the vp product at grafana labs um in my what little spare time i have i guess i'm one of the prometheus team um my main contribution being the the remote write code there uh i also started the cortex project which is the horizontally scalable version of prometheus that's part of the cncf sandbox more recently i started loki which is a grafana labs log aggregation system in what you know in when i'm not looking after these projects i have a bunch of 3d printers sitting on my desk and i used to make beer as well but i haven't actually had a chance to to brew for a while so today we're going to talk about shuffle sharding and how it allows us to build a more scalable version of cortex with with better isolation but before we do that i'd like to spend some time just introducing you to cortex what it does what it is why it's important before we go on and talk about you know how we solved this problem before we added shuffle sharding we'll then talk about shuffle sharding what it does and and finally how good it is you know if it really delivers on um on what we said it would so without further ado cortex horizontally scalable prometheus so prometheus is an awesome monitoring system it's incredibly easy to use and we see a lot of people get started with prometheus very very easily you know you you deploy it alongside your applications you maybe instrument your applications or or add a few exporters to to adapt them to prometheus and very quickly you know you attach your grafana very quickly you can build some really awesome dashboards right and you can really get some great insight into your application's behavior and and start debugging it and start responding to any problems it might has you know it is a really powerful and flexible system the challenge we see uh in prometheus is really when you start to grow beyond the confines of a single location beyond the confines of a single data center a single region you know maybe you've got your application deployed in three different locations you know grafana labs we run 15 plus kubernetes clusters in in the first instance what we see is is users add data sources to grafana for each one of these instances um you know this allows you to build dashboards with with little dropdowns that you can select what region you're interested in i guess the reason pro
