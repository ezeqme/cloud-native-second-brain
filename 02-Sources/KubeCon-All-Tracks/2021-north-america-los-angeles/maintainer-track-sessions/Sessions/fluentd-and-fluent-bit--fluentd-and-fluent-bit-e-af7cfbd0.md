---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Eduardo Silva", "Calyptia"]
sched_url: https://kccncna2021.sched.com/event/leYr/fluentd-and-fluent-bit-eduardo-silva-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Fluentd+and+Fluent+Bit+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Fluentd and Fluent Bit - Eduardo Silva, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Eduardo Silva, Calyptia
- Schedule: https://kccncna2021.sched.com/event/leYr/fluentd-and-fluent-bit-eduardo-silva-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Fluentd+and+Fluent+Bit+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Fluentd and Fluent Bit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/leYr/fluentd-and-fluent-bit-eduardo-silva-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Fluentd+and+Fluent+Bit+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J0dq3rZoLNs
- YouTube title: Fluentd and Fluent Bit - Eduardo Silva, Calyptia
- Match score: 0.737
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/fluentd-and-fluent-bit/J0dq3rZoLNs.txt
- Transcript chars: 29847
- Keywords: metrics, fluent, memory, prometheus, matrix, always, logs, performance, payload, output, information, fluency, metric, symmetrics, create, exporter, called, started

### Resumo baseado na transcript

thank you hey well my name is eduardo today we announced this session called about fluency and fluent bet originally description session we started talking about a our new journey to metrics right but before to jump into metric we're thinking okay maybe we need to go to a deep dive explanation why this is a good deal and how things work in logs how do we handle them before to jump into the metric space so anybody of you is new to fluentdm fluent bed if so please raise that also we are replicating not exporting metrics for windows this is also not play from prometheus but we're replicating the same functionality in fluent bet nginx metrics which is ready we're going to collect this.d also the ability to convert logs to metrics because there are many applications that ship logs as a json but you wanted to get them into prometheus so how do you handle that conversion that this filter called logs to matrix will a be a good place for that as an output site we're

### Excerpt da transcript

thank you hey well my name is eduardo today we announced this session called about fluency and fluent bet originally description session we started talking about a our new journey to metrics right but before to jump into metric we're thinking okay maybe we need to go to a deep dive explanation why this is a good deal and how things work in logs how do we handle them before to jump into the metric space so anybody of you is new to fluentdm fluent bed if so please raise your hand okay perfect no problem as the same enemies evado silva that's my hand on github twitter or most of the stuff and the creator of my intended this project called fluenbet i'm maintainer of the fluency ecosystem i'm the founder of this company called calyptia which we call the first mile observability company which was started on top of the open source ecosystem that we created and has been the cncf for a couple of years already and it came from the treasure data team where we created all this technology so the fluency ecosystem we have to start saying that fluentd is a graduated project from the cncf that means vendor neutral wide adoption in the market and where companies are contributing in a daily basis to the project a fluency started 10 years ago and after that well around 2016 we wanted to have a more lightweight solution than fluency not because fluent was bad but because we were targeting embedded linux at that time but at the same time well six seven years ago kubernetes was taken off the container space was growing and people started trying out fluent bed with continued containers because it was a light with solution that fluently flowing this within a ruby flume beat is written in c language right fluentd has a thousand plugins available in fluent bit we has just a hundred so both projects as part of the same ecosystem same license and are considered both graduated from the cncf and we're now in a journey where most of people do it to their workloads that they have in their environments sometimes fluency is not capable to solve all the challenges and that's why people are migrating from fluency to flowing bed nowadays so there's one big observability challenge right it doesn't matter if you are doing traces logins or metrics and they think that everybody wants more performance more performance but at zero cost right get it for free and such thing does not exist right there's nothing for free so this is a quite interesting challenge because when you have your environment yo
