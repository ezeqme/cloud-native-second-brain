---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Networking"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Fernando Crespo", "Daniel Caballero", "Fastly"]
sched_url: https://kccnceu2022.sched.com/event/ytrM/observing-fastlys-network-at-scale-thanks-to-k8s-and-the-strimzi-operator-fernando-crespo-daniel-caballero-fastly
youtube_search_url: https://www.youtube.com/results?search_query=Observing+Fastly%E2%80%99s+Network+at+Scale+Thanks+to+K8s+and+the+Strimzi+Operator+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Observing Fastly’s Network at Scale Thanks to K8s and the Strimzi Operator - Fernando Crespo & Daniel Caballero, Fastly

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Fernando Crespo, Daniel Caballero, Fastly
- Schedule: https://kccnceu2022.sched.com/event/ytrM/observing-fastlys-network-at-scale-thanks-to-k8s-and-the-strimzi-operator-fernando-crespo-daniel-caballero-fastly
- Busca YouTube: https://www.youtube.com/results?search_query=Observing+Fastly%E2%80%99s+Network+at+Scale+Thanks+to+K8s+and+the+Strimzi+Operator+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Observing Fastly’s Network at Scale Thanks to K8s and the Strimzi Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrM/observing-fastlys-network-at-scale-thanks-to-k8s-and-the-strimzi-operator-fernando-crespo-daniel-caballero-fastly
- YouTube search: https://www.youtube.com/results?search_query=Observing+Fastly%E2%80%99s+Network+at+Scale+Thanks+to+K8s+and+the+Strimzi+Operator+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eYZO7n_o0OQ
- YouTube title: Observing Fastly’s Network at Scale Thanks to K8s and the Stri... Fernando Crespo & Daniel Caballero
- Match score: 0.882
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/observing-fastlys-network-at-scale-thanks-to-k8s-and-the-strimzi-opera/eYZO7n_o0OQ.txt
- Transcript chars: 31626
- Keywords: cluster, network, autopilot, clusters, create, actually, fastly, solution, operator, elevation, pretty, mostly, platform, control, deploy, workloads, pipeline, operators

### Resumo baseado na transcript

okay now it's time so we are going to be presenting one story essentially how we use several cloud native foundation projects to build a telemetry pipeline mostly with a network automation use case in mind and the key elements are kubernetes and some operators including the stream c1 and yes the idea is we will be introducing ourselves the context then we will describe a bit the project and the platform supporting that project to then cover some details about the solution as well as some associated problems and

### Excerpt da transcript

okay now it's time so we are going to be presenting one story essentially how we use several cloud native foundation projects to build a telemetry pipeline mostly with a network automation use case in mind and the key elements are kubernetes and some operators including the stream c1 and yes the idea is we will be introducing ourselves the context then we will describe a bit the project and the platform supporting that project to then cover some details about the solution as well as some associated problems and issues we had we will be using a slightly different format for this and before closing we will be also sharing some highlights about the impact in our organization but before that fernando hi everyone i hope you are all having a great conference so far so i'm fernando i'm working at fastly i'm basically enabling coordinates for fastly control playing applications kubernetes is not a new space to me i think i started on the early stages think thanks to companies like 20 niagara and vietnamese i had a great experience there and i also had the pleasure to contribute to the kubernetes open source community with bug fixes features and and even custom controllers like 20 secrets manager um so this is me then hand over to danny again and yes this is daniel just an engineer at fastly i been in the like doing lots of data devops stuff mostly in the barcelona area so also from spain and yes i also love open source and i try to contribute as much as i can and also let's introduce a bit our company fastly maybe you already know about us our mission in the end is to make internet users happy and how do we try to do this it's mostly by having a distributed architecture where our customers can can you hear me okay where our customers can execute code as close as possible to the end users and deliver contents beating in mind performance and reliability so yes we have like a relatively large network defined by software we let our customers to run applications in our edge and uh yeah the idea is to make our customers as autonomous as possible to let them just to create whatever they need in our platform and benefit from our infrastructure some numbers if you are more used to requests per second 8 billion requests per day means an average of 10 million requests per second so yeah the size is relatively high and that was quite clear probably almost one year ago with that we had an out as a one-hour autism we were on the news so that's scary but also interesting at the
