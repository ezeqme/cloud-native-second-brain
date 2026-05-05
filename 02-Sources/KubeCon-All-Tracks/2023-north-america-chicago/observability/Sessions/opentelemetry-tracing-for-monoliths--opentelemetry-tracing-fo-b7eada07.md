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
themes: ["Observability"]
speakers: ["Phillip Carter", "Honeycomb"]
sched_url: https://kccncna2023.sched.com/event/1R2tM/opentelemetry-tracing-for-monoliths-phillip-carter-honeycomb
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Tracing+for+Monoliths+CNCF+KubeCon+2023
slides: []
status: parsed
---

# OpenTelemetry Tracing for Monoliths - Phillip Carter, Honeycomb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Phillip Carter, Honeycomb
- Schedule: https://kccncna2023.sched.com/event/1R2tM/opentelemetry-tracing-for-monoliths-phillip-carter-honeycomb
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+Tracing+for+Monoliths+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre OpenTelemetry Tracing for Monoliths.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tM/opentelemetry-tracing-for-monoliths-phillip-carter-honeycomb
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+Tracing+for+Monoliths+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kzXT0WlTBpw
- YouTube title: OpenTelemetry Tracing for Monoliths - Phillip Carter, Honeycomb
- Match score: 0.817
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/opentelemetry-tracing-for-monoliths/kzXT0WlTBpw.txt
- Transcript chars: 42855
- Keywords: actually, tracing, logs, instrumentation, distributed, trace, traces, database, application, necessarily, called, monolith, monoliths, context, process, structured, within, instrument

### Resumo baseado na transcript

It's Beginning time oh boy okay I think the doors are closing here um I will go ahead and start once a few more people get a chance to sit down hello everyone um hello to my co-workers sitting here in the front row to make sure that I'm extremely embarrassed if I crash and burn in this talk and hello to everyone else um this mic keeps on slipping down but I think it's doing okay uh hi my name is Phillip I am an open telemetry maintainer and

### Excerpt da transcript

It's Beginning time oh boy okay I think the doors are closing here um I will go ahead and start once a few more people get a chance to sit down hello everyone um hello to my co-workers sitting here in the front row to make sure that I'm extremely embarrassed if I crash and burn in this talk and hello to everyone else um this mic keeps on slipping down but I think it's doing okay uh hi my name is Phillip I am an open telemetry maintainer and I also work for a company called honeycomb we do observability and tracing observability so to the surprise of nobody I'm giving a talk about how you can trace with open Telemetry uh specifically for monoliths though which I think is something that doesn't um come up very often in the context of distributed tracing usually people talk about it when they're referring to microservices and big old distributed systems and stuff like that but I don't think that's really the reality that a lot of people live in and in particular I think I want to begin by um saying that I think modelist versus microservices is a pretty meaningless distinction um I think the messy reality that we all live in is that we're kind of living in some sort of in between World between microservices and monoliths and distributed monoliths and all that um and in particular uh over the past couple years that I've been working for honeycomb and helping people adopt tracing and observability for their system I've certainly noticed a few patterns uh a common monolith application like yes of course it's running in a single process but it's typically running behind a load balancer maybe there's a database server too that it's talking to maybe there's a message queue involved maybe it's calling an authentication server somewhere there's some thirdparty vendors maybe you've actually split out some of that monolith into separate services and created them as microservices at that point you have a distributed system already in fact I would wager that a true monolith that just talks to a database when that database is on a separate system that is already a distributed system um it may not be the most distributed of systems but it is still one and by definition it can benefit from from distributed tracing now it may not necessarily benefit as much as the largest spread of like thousands of services or something like that there's quite a bit of benefit to extract from that separately which I've observed uh plenty of times in my own career is that microservices grow i
