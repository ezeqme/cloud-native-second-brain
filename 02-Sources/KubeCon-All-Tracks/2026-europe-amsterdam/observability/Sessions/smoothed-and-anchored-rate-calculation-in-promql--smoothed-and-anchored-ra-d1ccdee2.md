---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["Observability"]
speakers: ["Björn Rabenstein", "Grafana Labs"]
sched_url: https://kccnceu2026.sched.com/event/2CVzy/smoothed-and-anchored-rate-calculation-in-promql-bjorn-rabenstein-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Smoothed+and+Anchored+Rate+Calculation+in+PromQL+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Smoothed and Anchored Rate Calculation in PromQL - Björn Rabenstein, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Björn Rabenstein, Grafana Labs
- Schedule: https://kccnceu2026.sched.com/event/2CVzy/smoothed-and-anchored-rate-calculation-in-promql-bjorn-rabenstein-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Smoothed+and+Anchored+Rate+Calculation+in+PromQL+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Smoothed and Anchored Rate Calculation in PromQL.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzy/smoothed-and-anchored-rate-calculation-in-promql-bjorn-rabenstein-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Smoothed+and+Anchored+Rate+Calculation+in+PromQL+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iN5vQjDuiWc
- YouTube title: Smoothed and Anchored Rate Calculation in PromQL - Björn Rabenstein, Grafana Labs
- Match score: 0.842
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/smoothed-and-anchored-rate-calculation-in-promql/iN5vQjDuiWc.txt
- Transcript chars: 28128
- Keywords: smooth, prometheus, calculation, actually, anchored, feature, change, smoothed, always, experimental, pretty, promql, minute, everything, anchor, increase, essentially, property

### Resumo baseado na transcript

I want to talk about rate calculation promql, which sounds like a really old chestnut, but we are doing something new now. It's a range selector over a range of 1 minute and then we take the rate very like 101 promql and I claim rate is the most used promql function. So you we need some uristics because Prometheus classicalally has no notion when the series starts and ends and this can go wrong and it's very confusing. We didn't really have this on the radar when we designed this, but now people create like distributed promul engines and stuff. Okay, so Prometheus team is maybe infamously conservative on many things. it goes into depth but uh Julian Pivoto he did the actual work he distilled this into a readable and actionable design doc and he even implemented it so he deserves all the praise he should actually be here and give this talk but he

### Excerpt da transcript

Hello, thanks for being here. My name is Bern. I work for Kofana Labs. I also do things on Prometheus. Um, I guess that's why I'm here. I want to talk about rate calculation promql, which sounds like a really old chestnut, but we are doing something new now. We are doing smooth and anchored rate calculation. So, let's see what this is. I mean, first of all, let's look at the old chestnut, right? You probably have all written an expression like this one, right? Rate request total over 1 minute. It's a range selector over a range of 1 minute and then we take the rate very like 101 promql and I claim rate is the most used promql function. Um at least if we include its friends um increase and delta right so in for the purposes of this talks these function are all doing the same thing I mean they are not right. So delta is just the delta over this range for gauge and then increase is the same thing for counters with counter resets and rate is syntactic sugar to divide the whole thing by the length of the range in seconds.

But what we are talking about here that doesn't all matter. We are just talking about how we do this fundamentally this calculation of an increase or rate. Um this is very fundamental to Prometheus. has been around forever essentially but also the discussion around it has been forever and people have suggested many different ways of uh calculating a rate they have even named it like x rate y rate h rate a rate m rate and these are just the proposals that got a name right um so something is wrong with rate you might say what's wrong tlddr nothing um it's a lot of all render into the classical current real official endorsed rate calculation but there's always a trade-off right it would take like 3 hours to explain this trade-off and all the aspects and edge cases and this talk is just like 20some minutes so I give you a very short version and I also focus on the downsides so we we we have actually a motivation to change something right so properties of the current existing rate implementation it strictly looks inside the range inside those one minute or whatever you picked and that's actually a very good property.

It it makes a lot of sense. It's easy to reason with but it has implication. The one thing is um hard to get full coverage for graphing and um if you have done this and you run into this you know what I'm talking about. If not we'll look at it a bit later in a bit more detail. Um the other thing you have certainly run into is since w
