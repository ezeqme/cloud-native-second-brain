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
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Richard Hartman", "Josh Abreu", "Grafana Labs"]
sched_url: https://kccncna2024.sched.com/event/1howl/celebrating-prometheus-30-a-deep-dive-with-the-maintainers-richard-hartman-josh-abreu-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Celebrating+Prometheus+3.0%3A+A+Deep+Dive+with+the+Maintainers+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Celebrating Prometheus 3.0: A Deep Dive with the Maintainers - Richard Hartman & Josh Abreu, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Richard Hartman, Josh Abreu, Grafana Labs
- Schedule: https://kccncna2024.sched.com/event/1howl/celebrating-prometheus-30-a-deep-dive-with-the-maintainers-richard-hartman-josh-abreu-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Celebrating+Prometheus+3.0%3A+A+Deep+Dive+with+the+Maintainers+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Celebrating Prometheus 3.0: A Deep Dive with the Maintainers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howl/celebrating-prometheus-30-a-deep-dive-with-the-maintainers-richard-hartman-josh-abreu-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Celebrating+Prometheus+3.0%3A+A+Deep+Dive+with+the+Maintainers+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9ROvfBqpdu4
- YouTube title: Celebrating Prometheus 3.0: A Deep Dive with the Maintainers - Richard Hartman & Josh Abreu
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/celebrating-prometheus-3-0-a-deep-dive-with-the-maintainers/9ROvfBqpdu4.txt
- Transcript chars: 30962
- Keywords: prometheus, actually, promethus, trying, little, anything, histograms, question, metrics, native, support, version, remote, everything, exporter, almost, features, integrations

### Resumo baseado na transcript

hi um I'm Josh and um uh I'm commonly known as God Josh yet is a reference to a 1993 advertisement of of God milk and when I'm not coding I'm usually snowboarding as you can see over there in the picture um principal software engineer AG Graal Labs uh promethus maintainer and I'm internally known as a metrics I say alerting guy which is a title that I've been trying to shake off for a while now that I'm back on the metric team and I'm Richie uh also

### Excerpt da transcript

hi um I'm Josh and um uh I'm commonly known as God Josh yet is a reference to a 1993 advertisement of of God milk and when I'm not coding I'm usually snowboarding as you can see over there in the picture um principal software engineer AG Graal Labs uh promethus maintainer and I'm internally known as a metrics I say alerting guy which is a title that I've been trying to shake off for a while now that I'm back on the metric team and I'm Richie uh also Prometheus maintainer part of the office of the CTO at grafo um yeah so a little bit of a show of hands if you use Prometheus please raise your hands keep them up if you think you are like beginner level or or higher sorry like keep them up and only take them down if once it doesn't apply to you take them uh keep them up if you think you are intermediate to Advanced and keep them up if you think you're Advanced thank you this helps us roughly uh figure out how much intro versus versus Deep dive we do during the thing because we have some L here so thank you uh okay so what is Prometheus right Prometheus is a metric based monitoring system and a learning stack um we have a very rich instrumentation ecosystem for all kinds of applications and um systems in general um peritus in peritus itself is in charge of doing all the metric collection and storage and once it's collected you can do all the things of the cool things that you hear about right like you can do the quering of the metrics you can do alerting on them you can dashboard them in pretty graphs um there's a bunch of exporters for all levels of the stack so this is not just about your application it's like there's hundreds of different use cases for things you can monitor with Prometheus um and it's designed from the ground up to uh cater for Cloud Dynamic environments right so we can handle churn really really well and hence we're here at a cloud native event as a whole um a little bit about the architecture as you can see so first we have the exporters right so this is the thing where Prometheus will be collecting metrics from it can be your application it can be your database be an exporter all sorts of things the next step in that process is the scraping so this is when perus actually grabs the metrics from the given exporters and then inserts them into to what we call the tsdv time series databases for short um and this is where your metrics are EV essentially stored right uh you can then query them with promql in order to do PRD graphs and dashboard
