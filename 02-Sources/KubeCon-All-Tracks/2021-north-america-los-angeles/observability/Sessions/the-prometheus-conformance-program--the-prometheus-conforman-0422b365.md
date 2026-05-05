---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Richard Hartmann", "Grafana Labs"]
sched_url: https://kccncna2021.sched.com/event/lV2v/the-prometheus-conformance-program-richard-hartmann-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=The+Prometheus+Conformance+Program+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Prometheus Conformance Program - Richard Hartmann, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Los Angeles
- Speakers: Richard Hartmann, Grafana Labs
- Schedule: https://kccncna2021.sched.com/event/lV2v/the-prometheus-conformance-program-richard-hartmann-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=The+Prometheus+Conformance+Program+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Prometheus Conformance Program.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2v/the-prometheus-conformance-program-richard-hartmann-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=The+Prometheus+Conformance+Program+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N_OkWRC-xQU
- YouTube title: The Prometheus Conformance Program - Richard Hartmann, Grafana Labs
- Match score: 0.774
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-prometheus-conformance-program/N_OkWRC-xQU.txt
- Transcript chars: 9202
- Keywords: prometheus, compatible, actually, compliance, results, write, conformance, little, obviously, design, compatibility, program, vendors, matter, yourself, everything, everyone, having

### Resumo baseado na transcript

hi and welcome to the prometheus conformance program you might never see this talk actually in fact i hope you don't because if you don't see this talk this means we figured out how to splice this in as a neotalk simply because we will have pretty fresh results which currently we don't know yet because it's a month before coupon so i'm kind of optimizing towards having a really short actual talk maybe you'll see maybe you don't and having an extended q a where i can share the

### Excerpt da transcript

hi and welcome to the prometheus conformance program you might never see this talk actually in fact i hope you don't because if you don't see this talk this means we figured out how to splice this in as a neotalk simply because we will have pretty fresh results which currently we don't know yet because it's a month before coupon so i'm kind of optimizing towards having a really short actual talk maybe you'll see maybe you don't and having an extended q a where i can share the actual results in a bit the 101 and all of this what we are doing here as of today october 14th we will start publishing an overview of of software of projects of products of as a service offerings which are compatible with prometheus if they are not compatible compatible with prometheus and if they claimed to be compatible with prometheus in the past we will most likely also end up publishing those results just to have a little bit of a fair level playing field between between all the different offers and and vendors and such as of this recording i don't know who is making that cut or was making the cut my we just don't know it's too early the intention obviously is that we want the end users you most likely to be able to choose between different implementations between different offerings with confidence without having any confusion about about what is actually compatible with purposes and what's not we have a little bit of a problem of success we are victims of our own success prometheus is the standard in cloud native uh metric monitoring and beyond and that's great but because prometheus is great obviously i'm kind of biased but i i think it's correct we have hundreds of thousands of installations we have millions of users this is great the market segment which we are leading is worth billions most likely even 10x that depending on who you ask and what analysts you read it's substantial as is commonly true it's a lot easier to claim that you're compatible with something as opposed to actually investing the work of being compatible with something some people honestly don't even realize if they're incompatible others maybe are more aware of this doesn't matter the point is we have confusion in the user base about who is actually doing things the prometheus way and who is just claiming to be doing them the promising way how does this work we created a suite of tests um you can see them here just in the promises or compliance and anyone can run them obviously part of the design cncf
