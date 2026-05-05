---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Richard Hartmann", "Grafana Labs", "Julien Pivotto", "Inuits"]
sched_url: https://kccnceu2021.sched.com/event/iE6p/prometheus-what-it-is-what-is-new-and-what-is-coming-richard-hartmann-grafana-labs-julien-pivotto-inuits
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+%E2%80%93+What+it+is%2C+What+is+New%2C+and+What+is+Coming+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Prometheus – What it is, What is New, and What is Coming - Richard Hartmann, Grafana Labs & Julien Pivotto, Inuits

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Richard Hartmann, Grafana Labs, Julien Pivotto, Inuits
- Schedule: https://kccnceu2021.sched.com/event/iE6p/prometheus-what-it-is-what-is-new-and-what-is-coming-richard-hartmann-grafana-labs-julien-pivotto-inuits
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus+%E2%80%93+What+it+is%2C+What+is+New%2C+and+What+is+Coming+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Prometheus – What it is, What is New, and What is Coming.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE6p/prometheus-what-it-is-what-is-new-and-what-is-coming-richard-hartmann-grafana-labs-julien-pivotto-inuits
- YouTube search: https://www.youtube.com/results?search_query=Prometheus+%E2%80%93+What+it+is%2C+What+is+New%2C+and+What+is+Coming+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UsxIDNNIwa0
- YouTube title: Prometheus – What it is, What is New, and What is Coming - Richard Hartmann & Julien Pivotto
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/prometheus-what-it-is-what-is-new-and-what-is-coming/UsxIDNNIwa0.txt
- Transcript chars: 19825
- Keywords: prometheus, everything, metrics, write, remote, basically, coming, already, actually, certain, storage, matrix, whatever, always, thanos, enables, directly, primitives

### Resumo baseado na transcript

welcome to this talk about prometheus when we see what it is what is new and what's coming i am jean pivotto i work at inuits and i have joined the primitives team in 2020 and i'm richard i work at grafana labs and i have joined the team i think in 2016. so let's talk about what prometheus is that is the quick 101 it's inspired by google sporkman it's a time series database internally working with 64 64-bit values for um for all numerical data there is over a thousand community-created instrumentations and exporters um way

### Excerpt da transcript

welcome to this talk about prometheus when we see what it is what is new and what's coming i am jean pivotto i work at inuits and i have joined the primitives team in 2020 and i'm richard i work at grafana labs and i have joined the team i think in 2016. so let's talk about what prometheus is that is the quick 101 it's inspired by google sporkman it's a time series database internally working with 64 64-bit values for um for all numerical data there is over a thousand community-created instrumentations and exporters um way more non-public ones it is for metrics not for logs dashboarding is done by grafana even before i joined cofounder labs it's a highly dynamic and built-in service discovery which means that you have a lot of different ways to put data or information about what systems to monitor into prometheus quite easily it's built in with kubernetes you can do zone transfer transfers through dns you can have a firebase service discovery where you can put in your own stuff from your own systems and there's dozens of other things how you can get the information about what to monitor into prometheus without any additional work on your it's literally taking it from your your operators from your orchestration from everything which which you might have it doesn't have a hierarchical data model it has an in-dimensional label set what that means is normally if you have hierarchical models you might have continent country and customer and then you need to select your your data by customer across all all continents and all of the sudden your hierarchy data model is already wrong for that type of query so by just attaching labels and allowing you to slice and dice your n-dimensional matrix however you want you can simply select by whatever you want for this you are using prompyo which is a functional language which is basically doing vector math what that means is you set your language up once or your calculations and then you just toss whatever amount of data into into this into this calculation and get the results set up no matter how much data comes or goes away you always get out what you want that's similar to how uh weather predictions and such are made this language is used for everything within prometheus for processing graphing alerting exporting everything where you work with the data you always go through control super nice it's really simple to operate you don't need teams upon teams or anything it is a monolith even though it's cloud native and is
