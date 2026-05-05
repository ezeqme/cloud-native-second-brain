---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Kubernetes", "Scalability Reliability"]
speakers: ["Martin Chodur"]
source_url: https://promcon.io/2024-berlin/talks/gluing-it-all-together-aka-building-a-platform-around-prometheus/
youtube_url: https://www.youtube.com/watch?v=epbMpJKhmB0
youtube_search_url: https://www.youtube.com/results?search_query=%E2%80%9CGluing+it+all+together%E2%80%9D+aka+building+a+platform+around+Prometheus+PromCon+2024
video_match_score: 1.038
status: video-found
---

# “Gluing it all together” aka building a platform around Prometheus

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: Martin Chodur
- Página oficial: https://promcon.io/2024-berlin/talks/gluing-it-all-together-aka-building-a-platform-around-prometheus/
- YouTube: https://www.youtube.com/watch?v=epbMpJKhmB0

## Resumo

In a larger setup it becomes cumbersome for everyone to manage their own Prometheus instance, think about its HA, meta monitoring, how to do alerting, service discovery, getting some global view, visualizing the data, authentication and maintaining all of this. Even the prometheus-operator helps mostly on the happy path, but when it comes to debugging, it’s yet another level of complexity. This talk will show you the things you have to solve to build your own “monitoring platform” on top of Prometheus without (almost) any cloud services for over 500 developers in tens of different teams running apps in more than 150 k8s clusters so they just “don’t have to care”.

## Abstract oficial

In a larger setup it becomes cumbersome for everyone to manage their own Prometheus instance, think about its HA, meta monitoring, how to do alerting, service discovery, getting some global view, visualizing the data, authentication and maintaining all of this. Even the prometheus-operator helps mostly on the happy path, but when it comes to debugging, it’s yet another level of complexity.

This talk will show you the things you have to solve to build your own “monitoring platform” on top of Prometheus without (almost) any cloud services for over 500 developers in tens of different teams running apps in more than 150 k8s clusters so they just “don’t have to care”.

You will see the rainbow and unicorns of the so-called "platform engineering", but also that the rainbow does not always end with a pot of gold and even unicorns need to sometimes 💩

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/gluing-it-all-together-aka-building-a-platform-around-prometheus/
- YouTube: https://www.youtube.com/watch?v=epbMpJKhmB0
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=epbMpJKhmB0
- YouTube title: PromCon 2024 - “Gluing it all together” aka building a platform around Prometheus
- Match score: 1.038
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/gluing-it-all-together-aka-building-a-platform-around-prometheus/epbMpJKhmB0.txt
- Transcript chars: 22462
- Keywords: remote, metrics, storage, platform, developers, issues, promeets, central, actually, prometheus, tenant, monitoring, company, alerting, tenants, provide, centers, operator

### Resumo baseado na transcript

[Music] thank you very much for having me uh hi my name is Martin uh as a BK said I will be talking uh I will tell you the story how we built internal platform monitoring platform uh using Prometheus in our company just quick note uh there will be huge walls of text in the presentation I'm sorry about that I don't expect you to read that uh there's all uh I put there the QR to the slides I expect you to read it if you find it

### Excerpt da transcript

[Music] thank you very much for having me uh hi my name is Martin uh as a BK said I will be talking uh I will tell you the story how we built internal platform monitoring platform uh using Prometheus in our company just quick note uh there will be huge walls of text in the presentation I'm sorry about that I don't expect you to read that uh there's all uh I put there the QR to the slides I expect you to read it if you find it interesting to talk I just couldn't help myself and left over left out the information so who am I uh former developer uh now A Team lead uh building the monitoring platform in our company I'm from Czech Republic live in burner and I work with promethus since 1 1.6 and where do I work where I where we are building the platform what's the environment we are talking we will be talking about uh there's something like 800 developers we are something like so-called check Google uh we have our own full teex search uh news we provide free email we provide whole lots of ton of services uh all our infrastructure is running in uh on Prem and physical data centers two two of those are our own we are building third third I think and we have our own internal Cloud platform uh there are some stats uh 150 kubernetes clusters 14,000 physical machines this is our mascot D do it's called crusty so how it all started uh when I joined ssam there was no application monitoring it was uh you wrote some code package it as the B package went to the Ops and they deploy it install it on server and then you are both looking at locks tailing and waiting for the 500s to show up or not and then prome ured which was nice we we we could have Mone in so now the boom everyone is starting its own Prometheus and and it's all over the place and the setup evolves uh new projects are coming up like tunnels cortex at that those times those were the first uh we were quite heavy users of tunos there is plenty of tnos clusters deployed in the company uh but with great power comes also the difficult Parts you have to maintain this monitoring stack uh you have to upgrade it Deb back all the issues you need to follow the Upstream the like the news you have to come to the prom cone and and hear about the news you need to deploy and this was done multiple times in the company everyone was doing the same thing and the question question is who will maintain all those monitoring stacks of course it's fun to set it up but no one wants to run it in long term so uh we decided uh since we
