---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Operations"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["David Morrison", "Evan Sheng", "Airbnb"]
sched_url: https://kccncna2021.sched.com/event/lUzs/what-kind-of-cpu-is-it-anyways-airbnbs-journey-to-heterogeneous-clusters-david-morrison-evan-sheng-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=What+Kind+of+CPU+is+it+Anyways%3F+Airbnb%27s+Journey+to+Heterogeneous+Clusters+CNCF+KubeCon+2021
slides: []
status: parsed
---

# What Kind of CPU is it Anyways? Airbnb's Journey to Heterogeneous Clusters - David Morrison & Evan Sheng, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Operations]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: David Morrison, Evan Sheng, Airbnb
- Schedule: https://kccncna2021.sched.com/event/lUzs/what-kind-of-cpu-is-it-anyways-airbnbs-journey-to-heterogeneous-clusters-david-morrison-evan-sheng-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=What+Kind+of+CPU+is+it+Anyways%3F+Airbnb%27s+Journey+to+Heterogeneous+Clusters+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre What Kind of CPU is it Anyways? Airbnb's Journey to Heterogeneous Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzs/what-kind-of-cpu-is-it-anyways-airbnbs-journey-to-heterogeneous-clusters-david-morrison-evan-sheng-airbnb
- YouTube search: https://www.youtube.com/results?search_query=What+Kind+of+CPU+is+it+Anyways%3F+Airbnb%27s+Journey+to+Heterogeneous+Clusters+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GCCSY7ERXj4
- YouTube title: What Kind of CPU is it Anyways? Airbnb's Journey to Heterogeneous... - David Morrison & Evan Sheng
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/what-kind-of-cpu-is-it-anyways-airbnbs-journey-to-heterogeneous-cluste/GCCSY7ERXj4.txt
- Transcript chars: 28115
- Keywords: cluster, instance, clusters, autoscaler, workloads, scheduler, scaler, expander, performance, single, topology, started, running, specific, scheduling, actually, priority, thanks

### Resumo baseado na transcript

um thanks thomas for the introduction uh thanks everyone for being here um hope you all had a good lunch also uh welcome to everyone who's online uh happy that you're able to participate as well um like thomas said my name is david this is my colleague evan we're both software engineers on the compute infrastructure team at airbnb um we're going to be talking about uh how we moved how our kubernetes clusters have been evolving into heterogeneous clusters over the past several years quick outline of our

### Excerpt da transcript

um thanks thomas for the introduction uh thanks everyone for being here um hope you all had a good lunch also uh welcome to everyone who's online uh happy that you're able to participate as well um like thomas said my name is david this is my colleague evan we're both software engineers on the compute infrastructure team at airbnb um we're going to be talking about uh how we moved how our kubernetes clusters have been evolving into heterogeneous clusters over the past several years quick outline of our presentation evan's going to talk a little bit about where we were before give you some historical context on what our clusters looked like two three four years ago and we're going to do a deep dive into uh three specific problems that we encountered we encountered a lot more than three but we picked three that we thought were sort of the most interesting these are both sort of technical and organizational hurdles that we had to overcome on this journey um i guess the other thing i'll mention here is this journey is ongoing some of the stuff that we're talking about is done some of it is in progress some of it's not complete yet but i think we've got a good plan at least and then lastly we're going to give you some future plans and lessons learned the tldr here is that heterogeneous clusters are great they've already been instrumental for airbnb and for our team so with that i'm going to hand it over to evan to talk a little bit about some historical context that's great thanks david yeah as david mentioned i'm going to start with a brief history of time of kubernetes at airbnb in 2016 and 2017 we started evaluating kubernetes for production use previously we were running chef on aws ec2 where each replica of each service would have its own machine in 2017 and 2018 we started building one touch which is airbnb's abstraction layer on top of kubernetes for developers the philosophy here is that all of a services config lives in one place in git and this config is then converted and applied as kubernetes manifests to the cluster um in 2018 2019 there was a huge effort across our engineering org to migrate uh 90 of our 700 plus services at the time um to kubernetes uh initially our clusters were separated out by environment so we had a prod cluster a staging cluster a dev cluster etc but this quickly grew out of hand as we hit kubernetes single node single cluster node size limits and we're forced to split these clusters into different cluster types so we had uh
