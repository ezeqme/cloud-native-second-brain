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
speakers: ["Iris Dyrmishi", "Rodrigo Fior Kuntzer", "Miro"]
sched_url: https://kccnceu2026.sched.com/event/2CW5m/cutting-metrics-traffic-cutting-costs-the-az-aware-observability-blueprint-iris-dyrmishi-rodrigo-fior-kuntzer-miro
youtube_search_url: https://www.youtube.com/results?search_query=Cutting+Metrics+Traffic%2C+Cutting+Costs%3A+The+AZ-Aware+Observability+Blueprint+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observability Blueprint - Iris Dyrmishi & Rodrigo Fior Kuntzer, Miro

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Iris Dyrmishi, Rodrigo Fior Kuntzer, Miro
- Schedule: https://kccnceu2026.sched.com/event/2CW5m/cutting-metrics-traffic-cutting-costs-the-az-aware-observability-blueprint-iris-dyrmishi-rodrigo-fior-kuntzer-miro
- Busca YouTube: https://www.youtube.com/results?search_query=Cutting+Metrics+Traffic%2C+Cutting+Costs%3A+The+AZ-Aware+Observability+Blueprint+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observability Blueprint.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5m/cutting-metrics-traffic-cutting-costs-the-az-aware-observability-blueprint-iris-dyrmishi-rodrigo-fior-kuntzer-miro
- YouTube search: https://www.youtube.com/results?search_query=Cutting+Metrics+Traffic%2C+Cutting+Costs%3A+The+AZ-Aware+Observability+Blueprint+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ycnDgULCHTA
- YouTube title: Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observ...  Iris Dyrmishi & Rodrigo Fior Kuntzer
- Match score: 0.827
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cutting-metrics-traffic-cutting-costs-the-az-aware-observability-bluep/ycnDgULCHTA.txt
- Transcript chars: 25933
- Keywords: observability, targets, metrics, course, cost, architecture, traffic, running, prometheus, network, actually, environment, quering, components, topology, collection, scrape, ingestion

### Resumo baseado na transcript

Really appreciate you staying with us until this very last day of CubeCon. Uh we are here today to talk you about cutting metric traffic and cutting uh costs and I'm delighted to share the stage with Iris. uh and then when we start dug uh dug into it, we found that 60 sometimes even 65% of that cost was coming from nodes running our observability components. Uh and the actual network cost of those components was often often equal or even higher than the compute costs needed for the compute uh for the for for the compute power of of those components. So when we start to research about the problem uh myself from a technical angle and ear is through her context uh context in the observability community it was interesting to find that even companies with mature phops practics and robust observability were also not able to handle this properly. Uh and we are here today uh to show you that and tell you that every architecture decision has a cost dimension and you can do something about it.

### Excerpt da transcript

Hello beautiful people. Good morning and thanks for stopping by. Really appreciate you staying with us until this very last day of CubeCon. Uh and I hope you are enjoying the show. Uh my name is Rodrigo. I'm a staff SR engineer at Miro. Uh we are here today to talk you about cutting metric traffic and cutting uh costs and I'm delighted to share the stage with Iris. >> Hello everyone and welcome. I'm Iris Durishi. I'm a senior observability engineer at Miro and also a CNCF ambassador. Happy to be here. Yeah. So, uh we have provided a link for some QA in the end. So, if you have any questions during our talk, please feel free to scan it. And if for some reason you cannot send your questions, don't worry. We have a mic. So, yeah, we're going to answer everything in the end. >> And you also find us elsewhere later. >> Absolutely. Yeah, we're open for discussion. So uh we have come here and we want to ask you a question. Who pays for your observability? Do you know? Well, we have a spoiler alert for you. Well, you do and probably even more than you think.

Sometimes there are some hidden costs that we bet you didn't take into consideration when you were evaluating the value of your observability stack. Uh over the past uh two years we have be uh have been ma uh being much more cautious uh about our uh cost uh uh our cloud costs. Uh at Miru we store a lot of data on behalf of our our customers especially in terms of storage and and databases that eats a lot of our cloud spends and then there is not that much left from for comput network and that's where we have to be really uh cautious about. So uh we have done many uh many good improvements uh in terms of compute optimization like uh right sizing workloads uh improving all the allocation radius and so on. Uh but there was one uh AWS bill that stay untouched in our uh billing reports and it was actually kept growing in a terrifying rates that item is the data transfer intra uh one. uh and then when we start dug uh dug into it, we found that 60 sometimes even 65% of that cost was coming from nodes running our observability components.

Uh and the actual network cost of those components was often often equal or even higher than the compute costs needed for the compute uh for the for for the compute power of of those components. uh so for us something was clearly clearly wrong and you have to do something about it. So when we start to research about the problem uh myself from a technical angle and ear is through he
