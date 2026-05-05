---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/prometheus-monitoring-mixins/
youtube_url: https://www.youtube.com/watch?v=b7-DtFfsL6E
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Monitoring+Mixins%3A+Using+Jsonnet+to+Package+Together+Dashboards%2C+Alerts%2C+and+Exporters+PromCon+2018
video_match_score: 0.765
status: video-found
---

# Prometheus Monitoring Mixins: Using Jsonnet to Package Together Dashboards, Alerts, and Exporters

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/prometheus-monitoring-mixins/
- YouTube: https://www.youtube.com/watch?v=b7-DtFfsL6E

## Resumo

Speaker: Tom Wilkie Prometheus offers powerful open source monitoring and alerting - but that comes with higher degrees of freedom, making pre-configured monitoring "packages" hard to build. Simultaneously, it's becoming accepted wisdom that the developers of a given software package are best placed to operate said software, or at least construct the basic monitoring configuration. In this talk we present a technique for using Jsonnet (a configuration language from Google) for packaging and deploying "Monitoring Mixins" - extensible and customisable combinations of dashboards, alert definitions and exporters.

## Abstract oficial

Speaker: Tom Wilkie

Prometheus offers powerful open source monitoring and alerting - but that comes with higher degrees of freedom, making pre-configured monitoring "packages" hard to build. Simultaneously, it's becoming accepted wisdom that the developers of a given software package are best placed to operate said software, or at least construct the basic monitoring configuration.

In this talk we present a technique for using Jsonnet (a configuration language from Google) for packaging and deploying "Monitoring Mixins" - extensible and customisable combinations of dashboards, alert definitions and exporters. This technique allows developers of open source projects to publish best-practice monitoring configurations alongside their code, and for users to consume it, customise it and stay up to date. We will present example Mixins for Kubernetes and other services such as Consul, Vault, and Cassandra.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/prometheus-monitoring-mixins/
- YouTube: https://www.youtube.com/watch?v=b7-DtFfsL6E
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=b7-DtFfsL6E
- YouTube title: Using Jsonnet to Package Together Dashboards, Alerts and Exporters - Tom Wilkie
- Match score: 0.765
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/prometheus-monitoring-mixins-using-jsonnet-to-package-together-dashboa/b7-DtFfsL6E.txt
- Transcript chars: 33412
- Keywords: prometheus, dashboards, config, monitoring, called, alerts, mix-ins, basically, language, install, actually, package, working, configuration, pretty, operator, metrics, cluster

### Resumo baseado na transcript

hello everybody my name is Tom I work for the final apps now although every cube can I seem to be a different company I'm still working on Prometheus and and today I'm come to talk about Prometheus monitoring mix-ins so this is a way of packaging together dashboards and alerts in kind of reusable redistributable way and I'm here to talk to you about why the story behind this is we were doing we were helping people adopt Prometheus in Crafar know and do their monitoring setups for them

### Excerpt da transcript

hello everybody my name is Tom I work for the final apps now although every cube can I seem to be a different company I'm still working on Prometheus and and today I'm come to talk about Prometheus monitoring mix-ins so this is a way of packaging together dashboards and alerts in kind of reusable redistributable way and I'm here to talk to you about why the story behind this is we were doing we were helping people adopt Prometheus in Crafar know and do their monitoring setups for them we found we were copying and pasting the alerts we defined for kubernetes for you know for Cassandra for console for CD we were copy and paste them between customers and doing slight tweaks and when we got to like the sixth or seventh time we're like you know this has got to stop so we've been working a bunch of has been working over the past few months on a way of making this much more reusable hopefully we can avoid this this copy and paste nightmare and hopefully we can use this to kind of enforce best practices and like iteratively improve the status quo of like how monitoring is done just better health housekeeping I am currently on 980 990 followers on Twitter so if 10 of you could follow me make me really happy so there is already a way of sharing dashboards and this is fun labs just come here and I work for they have an online system that allows you to upload dashboards and then other people can really easily download them and I can't I can't say nasty things because they're now my employer but there there's some challenges with this approach most of the dashboards that I've got from Griffin comm give me things that look like this they basically just just haven't quite worked every single time I've gone to wow they're bright hunt they he's really lit up the screen every time I've got them I've had to go in and tweak with them and play with them to make them work for my install of communities or my install of of anything I'm going to turn that off and normally the things we've the problems we've had is kind of the queries that they've used have made assumptions about the labels that are being used for the targets and for the time series so this is trying to tell me how much memory I'm using in my entire cluster the sum of all of the container memory usage divided by the sum of all the machine and it's trying to do it for a particular node but in my prometheus kubernetes setup I don't put the hostname of the pods and containers as a label because that's actually a bad p
