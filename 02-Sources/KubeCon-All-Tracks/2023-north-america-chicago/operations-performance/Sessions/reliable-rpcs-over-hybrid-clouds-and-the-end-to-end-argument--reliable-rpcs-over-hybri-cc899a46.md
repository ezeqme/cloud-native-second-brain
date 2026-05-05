---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Wenbo Zhu", "Vinod Lasrado", "Google Inc."]
sched_url: https://kccncna2023.sched.com/event/1R2ty/reliable-rpcs-over-hybrid-clouds-and-the-end-to-end-argument-wenbo-zhu-vinod-lasrado-google-inc
youtube_search_url: https://www.youtube.com/results?search_query=Reliable+RPCs+Over+Hybrid+Clouds+and+the+End-to-End+Argument+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Reliable RPCs Over Hybrid Clouds and the End-to-End Argument - Wenbo Zhu & Vinod Lasrado, Google Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Wenbo Zhu, Vinod Lasrado, Google Inc.
- Schedule: https://kccncna2023.sched.com/event/1R2ty/reliable-rpcs-over-hybrid-clouds-and-the-end-to-end-argument-wenbo-zhu-vinod-lasrado-google-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Reliable+RPCs+Over+Hybrid+Clouds+and+the+End-to-End+Argument+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Reliable RPCs Over Hybrid Clouds and the End-to-End Argument.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ty/reliable-rpcs-over-hybrid-clouds-and-the-end-to-end-argument-wenbo-zhu-vinod-lasrado-google-inc
- YouTube search: https://www.youtube.com/results?search_query=Reliable+RPCs+Over+Hybrid+Clouds+and+the+End-to-End+Argument+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hoXaYP2BSOo
- YouTube title: Reliable RPCs Over Hybrid Clouds and the End-to-End Argument - Wenbo Zhu & Vinod Lasrado, Google Inc
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/reliable-rpcs-over-hybrid-clouds-and-the-end-to-end-argument/hoXaYP2BSOo.txt
- Transcript chars: 33424
- Keywords: connection, network, actually, question, second, looking, particular, latency, hybrid, application, pretty, actual, request, server, requests, number, google, basically

### Resumo baseado na transcript

okay we get get started thanks everyone uh we don't have a very large Cloud uh yeah thanks for coming to the talk and uh so I just quick quickly introduce ourselves so I'm wo is my colleague venon and we're software Engineers working at Google Cloud uh we work on the open source project GPC but we're also supporting the the Google's internal infrastructure that powers the gcp services uh sometimes we call this C apis and also the non-cloud uh Google you know set of external facing services

### Excerpt da transcript

okay we get get started thanks everyone uh we don't have a very large Cloud uh yeah thanks for coming to the talk and uh so I just quick quickly introduce ourselves so I'm wo is my colleague venon and we're software Engineers working at Google Cloud uh we work on the open source project GPC but we're also supporting the the Google's internal infrastructure that powers the gcp services uh sometimes we call this C apis and also the non-cloud uh Google you know set of external facing services like gmail search So today we're going to talk about a specific you know a case study we like to share with you some experience about how to harden in the data path uh over the hybrid Cloud sorry yeah so okay sorry about about this uh so yeah first we're going to talk about you know what I really mean by hybrid Cloud I do I do not have exact definition of hybrid Cloud specifically the uh the use case we're talking about here is when some large scale online applications they try to move their database layers storage layers into the public cloud and uh when the majority of the application will still stay on the in the on premise data center now this is a shifting Paradigm if you look at the picture on the left side it's a traditional on premise you know deployment when you have applications talking to database for example mycure and the N Network link is usually reliable and more importantly they they share the same Faith right when something goes wrong typically the database itself goes wrong first all together with the network but once you move everything move the storage layer the database layer to the public Cloud now the entire datab base is different now part of the reasons you they're moving the database to public cloud is that they want Leverage The scalability reliability of the So-Cal s service but then the data path suddenly become different it become longer the fair modes is also different which we'll talk about now that doesn't mean the hybrid cloud is harder it's impossible to you know to wrun or it's inherently unreliable it I think the the key problems that we like to address is here that when the application layer they're not adap Ed to this new sort of data path the longer RT the different fail modes and that's the you know that's basically the use case we're looking at today so we look at the the whole problem then we start realize that the end lineing problem the technical problem is pretty generic right it's not really anything application specific it'
