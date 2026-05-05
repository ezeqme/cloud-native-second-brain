---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Julius Volz", "PromLabs", "Björn Rabenstein", "Grafana Labs", "Matthias Rampke", "SoundCloud"]
sched_url: https://kccnceu2022.sched.com/event/ytpW/prometheus-intro-and-deep-dive-julius-volz-promlabs-bjorn-rabenstein-grafana-labs-matthias-rampke-soundcloud
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Intro+and+Deep+Dive+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Prometheus Intro and Deep Dive - Julius Volz, PromLabs; Björn Rabenstein, Grafana Labs; Matthias Rampke, SoundCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Julius Volz, PromLabs, Björn Rabenstein, Grafana Labs, Matthias Rampke, SoundCloud
- Schedule: https://kccnceu2022.sched.com/event/ytpW/prometheus-intro-and-deep-dive-julius-volz-promlabs-bjorn-rabenstein-grafana-labs-matthias-rampke-soundcloud
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus+Intro+and+Deep+Dive+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Prometheus Intro and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpW/prometheus-intro-and-deep-dive-julius-volz-promlabs-bjorn-rabenstein-grafana-labs-matthias-rampke-soundcloud
- YouTube search: https://www.youtube.com/results?search_query=Prometheus+Intro+and+Deep+Dive+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t3YFv20Ulnc
- YouTube title: Prometheus Intro and Deep Dive - Richard Hartmann, Grafana Labs
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/prometheus-intro-and-deep-dive/t3YFv20Ulnc.txt
- Transcript chars: 35489
- Keywords: prometheus, actually, basically, version, everything, remote, questions, already, storage, memory, within, little, metrics, course, promethus, anything, native, currently

### Resumo baseado na transcript

so uh welcome to the Prometheus update um I'm going to do the usual so show of hands who who knows what promethus actually is okay this is way more than in 2017 2018 like there was a full room and no one actually knew what it was so this is really good who's using it like just a little bit or and who's using it in production nice this is way more than a few years ago this is really nice so for um those of you who don't

### Excerpt da transcript

so uh welcome to the Prometheus update um I'm going to do the usual so show of hands who who knows what promethus actually is okay this is way more than in 2017 2018 like there was a full room and no one actually knew what it was so this is really good who's using it like just a little bit or and who's using it in production nice this is way more than a few years ago this is really nice so for um those of you who don't know uh the structure we always have with the Prometheus update is we have a short intro we have a little bit of a deeper dive session and we try to get through this as quickly as possible so we have enough time for questions at the end so you can just ask whatever you want to ask uh without us basically prescribing the content and just babbling until the very end so um the very quick version of what premesis is it is a metric engine metrics are numerical data which you can store about systems it might be temperature it might be uh how many how many requests your your web server gets how many sales you do through your web shop things like these uh you would normally instrument your applications where you have a variety of different uh instrumentation libraries and also Auto instrumentation you can also use open Telemetry you can use the Prometheus client libraries hooking into your applications and exposing the data which matters to you automatically Prometheus is the stuff which does the metx storage and collection and and basically all the computation of the data once it is in you can query the data you can alert you can dashboard everything through one single language uh for those deeper into math it is a vector Lang or it is a functional language for doing Vector math on your observability data in more simpler terms basically you can do actually at scale math on your data and this is part of why Prometheus is so successful because this was the first time that this this was actually uh available to anyone within open source and they could could just use those Advanced uh curing mechanisms you can use it for everything if you still have a data center you can use it for your diesel generators down to your microservices and everything in between um which is also very much different from previous generations of observability and monitoring tools and APM and all those things where you're usually limited to just Network or just infrastructure or just applications here you can do your whole stack with one single solution and also it is the absol
