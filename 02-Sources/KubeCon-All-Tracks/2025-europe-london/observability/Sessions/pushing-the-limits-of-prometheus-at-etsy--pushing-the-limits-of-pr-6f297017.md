---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability"]
speakers: ["Chris Leavoy", "Etsy", "Bryan Boreham", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1txHp/pushing-the-limits-of-prometheus-at-etsy-chris-leavoy-etsy-bryan-boreham-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Pushing+the+Limits+of+Prometheus+at+Etsy+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Pushing the Limits of Prometheus at Etsy - Chris Leavoy, Etsy & Bryan Boreham, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Chris Leavoy, Etsy, Bryan Boreham, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1txHp/pushing-the-limits-of-prometheus-at-etsy-chris-leavoy-etsy-bryan-boreham-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Pushing+the+Limits+of+Prometheus+at+Etsy+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Pushing the Limits of Prometheus at Etsy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHp/pushing-the-limits-of-prometheus-at-etsy-chris-leavoy-etsy-bryan-boreham-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Pushing+the+Limits+of+Prometheus+at+Etsy+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IWrd-pSojqg
- YouTube title: Pushing the Limits of Prometheus at Etsy - Chris Leavoy, Etsy & Bryan Boreham, Grafana Labs
- Match score: 0.72
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/pushing-the-limits-of-prometheus-at-etsy/IWrd-pSojqg.txt
- Transcript chars: 28841
- Keywords: prometheus, memory, server, blocks, number, another, remote, compaction, garbage, million, collection, second, shards, metrics, bigger, samples, amount, faster

### Resumo baseado na transcript

hello everyone our talk is about pushing the limits of Prometheus at Etsy today we'll share some of the lessons from operating one of the industry's largest Prometheus servers but before we get into it let us introduce ourselves my name is Chris Levoy and I'm an observability engineer at Etsy I'm based in waterl Canada and I've been with Etsy for the past four years Etsy is a global e-commerce Marketplace for unique and creative Goods it was founded in 2005 and is headquartered in Brooklyn New York now a diagram of Prometheus block layouts on top we have the Prometheus default and on the bottom is the block layout we used at at Etsy we made two changes the setting the minimum and maximum durations both to one to one hour setting the

### Excerpt da transcript

hello everyone our talk is about pushing the limits of Prometheus at Etsy today we'll share some of the lessons from operating one of the industry's largest Prometheus servers but before we get into it let us introduce ourselves my name is Chris Levoy and I'm an observability engineer at Etsy I'm based in waterl Canada and I've been with Etsy for the past four years Etsy is a global e-commerce Marketplace for unique and creative Goods it was founded in 2005 and is headquartered in Brooklyn New York now I'll invite my co-speaker Brian hello uh my name is Brian boram I am a distinguished engineer at grafana Labs grafana is the leading open-source software for visualizing operational data I had to read that um what I what I do on my day job is is I work on the uh scaling the massively scalable storage that we have for metrics logs and traces we store trillions of metric points and petabytes of logs I the reason I'm on this stage is I'm a Prometheus maintainer uh I've worked on that code for about seven years now uh so who knows Prometheus okay like 60% or something like that well good good um I just want to talk about the uh architecture um because we'll we'll return to this picture a number of times uh so basically uh data data starts off on the left uh what we call exporters so that could be data coming from the node or from containers or application specific metrics anything where the data is coming from that we call that an exporter and we pull the data in that's a process called scraping we put it in the time series database uh tsdb first of all in memory and then on disk and then uh to get data out there's the prom query language um and then usually visualization is done by something on on the outside like maybe grafana um the key thing that's important for this talk is everything in that box in the middle is one process uh that's what's really cool about Prometheus it's really easy to deploy one process and you're you're off um but the way it scales is get a bigger machine so this talk is about the biggest Prometheus I ever saw so uh what is this giant Prometheus server for well if you're looking for that perfect gift to Mark a special occasion you can try searching on etsy.com the server we'll be discussing monitors millions of metrics about searches on Etsy it's been around for about 8 years and it's just chalk full of alerts and recording rules but this server is just one of 30 Prometheus Stacks that we operate at Etsy each stack is isolated around
