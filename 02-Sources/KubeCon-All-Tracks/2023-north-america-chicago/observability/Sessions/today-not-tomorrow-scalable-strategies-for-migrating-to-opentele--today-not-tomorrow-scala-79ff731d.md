---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Jason Anderson", "Kevin Broadbridge", "Cruise"]
sched_url: https://kccncna2023.sched.com/event/1R2uc/today-not-tomorrow-scalable-strategies-for-migrating-to-opentelemetry-jason-anderson-kevin-broadbridge-cruise
youtube_search_url: https://www.youtube.com/results?search_query=Today%2C+Not+Tomorrow%3A+Scalable+Strategies+for+Migrating+to+OpenTelemetry+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Today, Not Tomorrow: Scalable Strategies for Migrating to OpenTelemetry - Jason Anderson & Kevin Broadbridge, Cruise

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Jason Anderson, Kevin Broadbridge, Cruise
- Schedule: https://kccncna2023.sched.com/event/1R2uc/today-not-tomorrow-scalable-strategies-for-migrating-to-opentelemetry-jason-anderson-kevin-broadbridge-cruise
- Busca YouTube: https://www.youtube.com/results?search_query=Today%2C+Not+Tomorrow%3A+Scalable+Strategies+for+Migrating+to+OpenTelemetry+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Today, Not Tomorrow: Scalable Strategies for Migrating to OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uc/today-not-tomorrow-scalable-strategies-for-migrating-to-opentelemetry-jason-anderson-kevin-broadbridge-cruise
- YouTube search: https://www.youtube.com/results?search_query=Today%2C+Not+Tomorrow%3A+Scalable+Strategies+for+Migrating+to+OpenTelemetry+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iPGd9_aYu-A
- YouTube title: Today, Not Tomorrow: Scalable Strategies for Migrating to Open... Jason Anderson & Kevin Broadbridge
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/today-not-tomorrow-scalable-strategies-for-migrating-to-opentelemetry/iPGd9_aYu-A.txt
- Transcript chars: 34540
- Keywords: metrics, basically, collector, otel, actually, observability, trace, instrumentation, vendor, systems, prometheus, cluster, scrape, collectors, little, migration, clusters, attributes

### Resumo baseado na transcript

so my name is Jason I'm here with my colleague Kevin we both work on the observability team at Cruz uh which is under site reliability engineering and um just by way of kind of understanding the audience a little bit here I wanted to just get a sense of a few things can you just like raise your hand or otherwise visually you know inform me if you feel like you have a good understanding of open Telemetry all right so that's about uh 50% now same question what uh to our Central injust uh next we have a lot of pro uh local Prometheus scrape Targets on our clusters so you know a lot of utility deployments like sto and open policy agent uh have Prometheus endpoints also our Legacy system supported Prometheus

### Excerpt da transcript

so my name is Jason I'm here with my colleague Kevin we both work on the observability team at Cruz uh which is under site reliability engineering and um just by way of kind of understanding the audience a little bit here I wanted to just get a sense of a few things can you just like raise your hand or otherwise visually you know inform me if you feel like you have a good understanding of open Telemetry all right so that's about uh 50% now same question what about specific the open Telemetry collector thing that you can deploy to manage signals all right slightly less okay cool um that's good because the this talk is going to get pretty technical um this is kind of a report From The Trenches of uh somebody who's doing a kind of a large scale migration um using open Telemetry shifting a lot of existing instrumentation to it and um so we're going to get in the weeds but at the same time it's going to be kind of not so much exactly about how we do it because we don't want to be necessarily prescriptive just kind of showing you some ways you can think about doing this in your organization and hopefully it kind of is um applicable to organizations of various different shapes and sizes and you know um maturities so as an overview in this talk we're going to walk you through the thought process that we followed and executing a wholesale migration from one observability vendor to another in our case uh we had historically used dead dog and are migrating um to chronosphere it's actually funny I think on Tuesday there's a panel with a uh charity Majors kind of referred to observability teams as doing vendor engineering and uh that felt actually a little too accurate um because that's a lot of what we do is we manage our the relationship between the infrastructure and the teams and ultimately a lot of vendor products that we are leveraging for you know opportunity cost you don't have to spend all this time owning all aspects of um observability internally because it doesn't make sense a lot of the time um that said we're not talking specifically about vendors in this talk it's more about just the process of migrating and why open Telemetry is a great assist in helping you kind of have more technical choice to allow you to make this kind of shift in the future um we're going to tell you some lessons we learned along the way Kevin is going to give you a deep dive into how we run the LEL collector at scale for a lot of different use cases at Cru and ultimately what we h
