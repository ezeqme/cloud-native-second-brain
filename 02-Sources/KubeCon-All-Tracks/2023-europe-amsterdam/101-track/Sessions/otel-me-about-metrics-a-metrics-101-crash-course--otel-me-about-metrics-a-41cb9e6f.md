---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["Observability"]
speakers: ["Reese Lee", "New Relic"]
sched_url: https://kccnceu2023.sched.com/event/1Hya1/otel-me-about-metrics-a-metrics-101-crash-course-reese-lee-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=OTel+Me+About+Metrics%3A+A+Metrics+101+Crash+Course+CNCF+KubeCon+2023
slides: []
status: parsed
---

# OTel Me About Metrics: A Metrics 101 Crash Course - Reese Lee, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Reese Lee, New Relic
- Schedule: https://kccnceu2023.sched.com/event/1Hya1/otel-me-about-metrics-a-metrics-101-crash-course-reese-lee-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=OTel+Me+About+Metrics%3A+A+Metrics+101+Crash+Course+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre OTel Me About Metrics: A Metrics 101 Crash Course.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hya1/otel-me-about-metrics-a-metrics-101-crash-course-reese-lee-new-relic
- YouTube search: https://www.youtube.com/results?search_query=OTel+Me+About+Metrics%3A+A+Metrics+101+Crash+Course+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QDEpOV1kiio
- YouTube title: OTel Me About Metrics: A Metrics 101 Crash Course - Reese Lee, New Relic
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/otel-me-about-metrics-a-metrics-101-crash-course/QDEpOV1kiio.txt
- Transcript chars: 23715
- Keywords: metrics, measurements, instrument, counter, metric, number, instruments, application, aggregation, whether, histogram, useful, telescope, temporality, actually, called, monotonic, dimensions

### Resumo baseado na transcript

so as I said hopefully you all are in the right room um I was realizing that some of you may not realize that hotel is short for open Telemetry so this is just my play on the title um quick introduction my name is Rhys Lee can you guys hear me I can't tell this is awesome okay I am a developer relations engineer by day at New Relic I previously started actually in tech support and I mentioned that because I really enjoy working directly with end users

### Excerpt da transcript

so as I said hopefully you all are in the right room um I was realizing that some of you may not realize that hotel is short for open Telemetry so this is just my play on the title um quick introduction my name is Rhys Lee can you guys hear me I can't tell this is awesome okay I am a developer relations engineer by day at New Relic I previously started actually in tech support and I mentioned that because I really enjoy working directly with end users and so that's how I landed in the open slumption user working group when I was um switching for how I could best contribute to the project um we have two overarching goals which is to increase adoption implementation of the project as well as to maintain and facilitate a feedback loop to help improve the project um to that end we host various activities to connect end users and contributors um for the interest of time I won't get too much into those but definitely feel free to come find me after it or come to the open telemundry booth in the solution so showcase um a quick fun fact about myself is I'm already from Malaysia I have lived in the Pacific Northwest in the states for almost 20 years at this point um and the Netherlands is my 15th country that I've been to so yay okay I have can I use hello hi Evie can I actually use one of the handheld mics this is killing my vibe right now oh there we go okay so I've categorized today's content into four broad categories we're going to do a quick metrics overview followed by a quick open to another two overview and they'll get into the meat of the talk which is the metrics dip and then we'll look at some next steps for you to take after the session to learn more about metrics so first we'll start with a metrics overview we'll look at what is the metric and why are they useful what is the metric a metric is simply a measurement about a service that's captured at runtime and these measurements can be further aggregated over time to help us identify Trends and patterns oh also there's broad categories of metrics right you have application runtime metrics you've got infrastructure metrics and you probably also want to collect some custom or business metrics as well um to illustrate this as well as subsequent Concepts I'm going to use the open Telemetry Community demo application as a basis for of for our examples so the demo application is actually based off of gcp's hipster shop which I think is now called the online boutique so a lot of you may already be familiar w
