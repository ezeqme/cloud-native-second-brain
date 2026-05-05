---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Callum Styan", "Grafana Labs", "Bartłomiej Płotka", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7kO/unlocking-cost-savings-new-possibilities-your-guide-to-prometheus-remote-write-20-callum-styan-grafana-labs-bartlomiej-plotka-google
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+Cost+Savings+%26+New+Possibilities%3A+Your+Guide+to+Prometheus+Remote+Write+2.0+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unlocking Cost Savings & New Possibilities: Your Guide to Prometheus Remote Write 2.0 - Callum Styan, Grafana Labs & Bartłomiej Płotka, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Callum Styan, Grafana Labs, Bartłomiej Płotka, Google
- Schedule: https://kccncna2024.sched.com/event/1i7kO/unlocking-cost-savings-new-possibilities-your-guide-to-prometheus-remote-write-20-callum-styan-grafana-labs-bartlomiej-plotka-google
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+Cost+Savings+%26+New+Possibilities%3A+Your+Guide+to+Prometheus+Remote+Write+2.0+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unlocking Cost Savings & New Possibilities: Your Guide to Prometheus Remote Write 2.0.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kO/unlocking-cost-savings-new-possibilities-your-guide-to-prometheus-remote-write-20-callum-styan-grafana-labs-bartlomiej-plotka-google
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+Cost+Savings+%26+New+Possibilities%3A+Your+Guide+to+Prometheus+Remote+Write+2.0+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=o5HpeMtpsTg
- YouTube title: Unlocking Cost Savings & New Possibilities: Your Guide to Prometheus Remote W... C. Styan, B. Płotka
- Match score: 0.97
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unlocking-cost-savings-new-possibilities-your-guide-to-prometheus-remo/o5HpeMtpsTg.txt
- Transcript chars: 33918
- Keywords: remote, prometheus, protocol, actually, metadata, format, features, promit, metrics, better, version, storage, itself, wanted, basically, pretty, histograms, question

### Resumo baseado na transcript

how are you everyone okay amazing hello everyone um we are extremely excited to be here on cucon and talk about the second major version of remote right protocol in the pruse ecosystem and I have to admit in a really context of distributed systems I personally have some some kind of weakness or respect towards Network protocols and and apis and I would love to learn if you have the same feelings but to me designing Network protocols for high volume data especially in open source pauses a lot build to generate a go client for a remote rate so in summary remote right 2.0 enables this great set of features features that perus itself already supports uh while also making some pretty significant performance improvements right uh over 60% for almost every um everything that we measured um it's pretty simple to configure only two lines within Prometheus um and if you're the owner of a third party project or some kind of community tool um we invite you to implement remote r2.0 support come to us if

### Excerpt da transcript

how are you everyone okay amazing hello everyone um we are extremely excited to be here on cucon and talk about the second major version of remote right protocol in the pruse ecosystem and I have to admit in a really context of distributed systems I personally have some some kind of weakness or respect towards Network protocols and and apis and I would love to learn if you have the same feelings but to me designing Network protocols for high volume data especially in open source pauses a lot of interesting questions how to make this API extensible but also stable how to make it flexible and Powerful but also simple efficient and consistent plus it takes really years to get it adopted and get feedback of whatever you change um and also you have to think about you know Common network problems and disputed system problems challenges like consistency and availability um so let's start with a short introduction to the promit remote right protocols so Prim primary role of promus if you're not familiar is to allow you to instrument collect store and query all your metrics and then do some kind of work on top of that for example alerting dashboarding and so on however if you are familiar with pruse a bit more you know that pritus also comes with those remote storage interfaces so why and literally from the beginning of promit the developers like Julius faults 11 years ago um Issue Number 10 like very very beginning when I was looking at it um we're thinking on how prudes can integrate with you know remote well like different databases and back then there wasn't much there um I I found that there were mentions about inflex DB integration open tdb um but still such need for remote right uh remote storage integration shouldn't come as a surprise if you are familiar with promus um promus was and still is a single node solution after all no built replication no buil clustering or so On By Design this is why the younger Protocol remote read was introduced so any client can ask for some historical retric samples in pritus format for example initially it was it was to enable promql uh quer language and and quering capabilities through promes against metrics stored in a different databases like in open tdb it wasn't long until re API the same read API was also Exposed on promus itself right allowing long-term storage solutions like Thanos to effectively query prom use for the fresh metric or row data in promit use format or for proxies like promy um to transparently De dup
