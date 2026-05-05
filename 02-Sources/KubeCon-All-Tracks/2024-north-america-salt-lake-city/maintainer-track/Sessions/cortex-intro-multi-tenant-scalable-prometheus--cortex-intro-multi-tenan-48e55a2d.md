---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "SRE Reliability", "Community Governance"]
speakers: ["Charlie Le", "Apple", "Daniel Blando", "Amazon"]
sched_url: https://kccncna2024.sched.com/event/1howq/cortex-intro-multi-tenant-scalable-prometheus-charlie-le-apple-daniel-blando-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Cortex+Intro%3A+Multi-Tenant+Scalable+Prometheus+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cortex Intro: Multi-Tenant Scalable Prometheus - Charlie Le, Apple & Daniel Blando, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Charlie Le, Apple, Daniel Blando, Amazon
- Schedule: https://kccncna2024.sched.com/event/1howq/cortex-intro-multi-tenant-scalable-prometheus-charlie-le-apple-daniel-blando-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Cortex+Intro%3A+Multi-Tenant+Scalable+Prometheus+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cortex Intro: Multi-Tenant Scalable Prometheus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howq/cortex-intro-multi-tenant-scalable-prometheus-charlie-le-apple-daniel-blando-amazon
- YouTube search: https://www.youtube.com/results?search_query=Cortex+Intro%3A+Multi-Tenant+Scalable+Prometheus+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=by538PPSPQ0
- YouTube title: Cortex Intro: Multi-Tenant Scalable Prometheus - Ben Ye & Friedrich Gonzalez
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cortex-intro-multi-tenant-scalable-prometheus/by538PPSPQ0.txt
- Transcript chars: 25225
- Keywords: cortex, basically, queries, metrics, memory, storage, feature, configure, limits, called, actually, question, application, features, tenant, postings, familiar, thanos

### Resumo baseado na transcript

uh okay uh hello everyone uh so welcome to our session uh I hope everyone is having a great ccon so far so yeah let's get started uh so today our topic is about uh introduction to Cortex multi- scalable uh premisus so uh I'm Ben y uh I'm a software uh development engineer at AWS and uh uh I'm a maintainer of Cortex as well as SOS project and I'm also a contributor to some other cncf project like premisus ago CD Etc so I have a papy named

### Excerpt da transcript

uh okay uh hello everyone uh so welcome to our session uh I hope everyone is having a great ccon so far so yeah let's get started uh so today our topic is about uh introduction to Cortex multi- scalable uh premisus so uh I'm Ben y uh I'm a software uh development engineer at AWS and uh uh I'm a maintainer of Cortex as well as SOS project and I'm also a contributor to some other cncf project like premisus ago CD Etc so I have a papy named uh GUI and uh yeah so today with me I have uh I have kedish yeah I have um Fredick Gonzalez um I'm a software engineer at Adobe um I'm also a maintainer for cortex and what you see there is my puppy uh well she's not a puppy anymore she's Doberman so um I just want to excuse myself we in the last year presentation we had more puppies this year doesn't have that many I'm sorry for that but um so but what is cortex um let's talk a bit on cortex cortex is a horizontally scalable highly available multi-tenant long-term storage for Prometheus um is a community project it was created in 20 2016 it's part of the cncf incubating projects has seen a lot of contributors uh it has had a lot of maintainers over the years um these are the companies using cortex um or or that had used cortex um but I want to stop right here a bit um who's familiar with Prometheus can you raise your hand great and who's familiar with collectors up infammatory collectors anybody running out great okay awesome well back in when 2016 uh when cortex was created and started to work on we had this situation with Prometheus that as you might familiar with it it is a memory database right so the more metrics you you add to a Prometheus it it starts to increase in resources needs right so it needs more memory um so typically set up uh what people do they have more than one Peres right they have two peritas now um one per is for some applications one Peres for another application and uh you solve your problem but um this problem increases and now you have several preus and now your view of the metrics starts to become a little bit different right you have metrics some metrics here some metrics there U and this is when most people use Thanos right they have like a Thanos deployed that is able able to see if you're familiar with tanos um I'm just throwing out that that if you are familiar um and and is able to see all the views the thing with tanos though is is you have to configure it you have to decide where to put every metric uh that's how um Thanos solves that
