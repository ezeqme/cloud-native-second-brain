---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Josue (Josh) Abreu", "Grafana Labs"]
sched_url: https://kccnceu2022.sched.com/event/ytpf/alerting-in-the-prometheus-ecosystem-the-past-present-and-future-josue-josh-abreu-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Alerting+in+the+Prometheus+Ecosystem%3A+The+Past%2C+Present+and+Future+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Alerting in the Prometheus Ecosystem: The Past, Present and Future - Josue (Josh) Abreu, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Josue (Josh) Abreu, Grafana Labs
- Schedule: https://kccnceu2022.sched.com/event/ytpf/alerting-in-the-prometheus-ecosystem-the-past-present-and-future-josue-josh-abreu-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Alerting+in+the+Prometheus+Ecosystem%3A+The+Past%2C+Present+and+Future+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Alerting in the Prometheus Ecosystem: The Past, Present and Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpf/alerting-in-the-prometheus-ecosystem-the-past-present-and-future-josue-josh-abreu-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Alerting+in+the+Prometheus+Ecosystem%3A+The+Past%2C+Present+and+Future+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9AX8u-bt4J8
- YouTube title: Alerting in the Prometheus Ecosystem: The Past, Present and Future - Josue (Josh) Abreu
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/alerting-in-the-prometheus-ecosystem-the-past-present-and-future/9AX8u-bt4J8.txt
- Transcript chars: 21102
- Keywords: manager, alerts, prometheus, replicas, grafana, cortex, notification, within, present, notifications, multiple, already, alerting, mimir, grouping, instance, tenant, moving

### Resumo baseado na transcript

awesome all right well the good thing about this is there's not going to be any questions so lucky me um good afternoon kubecon i'm super excited to be here welcome to alerting in the prometheus ecosystem the story of the past present and the future if we're going to spend the next 30 minutes together we might as well just get to know each other a little bit better i'm josue commonly known as josh or god josh yes is a reference to the 1993 advertisement of got milk

### Excerpt da transcript

awesome all right well the good thing about this is there's not going to be any questions so lucky me um good afternoon kubecon i'm super excited to be here welcome to alerting in the prometheus ecosystem the story of the past present and the future if we're going to spend the next 30 minutes together we might as well just get to know each other a little bit better i'm josue commonly known as josh or god josh yes is a reference to the 1993 advertisement of got milk when i'm not coding i'm usually snowboarding which wasn't the easy sport to catch on given i come from the caribbean i work as a software engineer leading the alerting team at grafana labs with a bunch of other folks from the prometheus community which you might know about such as like tom wilkie bjorn ravenstein ganesh bernakar kanesh has to talk just after this one in this room so please make sure you stick around because that's an interesting one i'm very lucky to have spent most of my turn here at grafana labs working with prometheus mimir cortex and the alert manager has this helped me form or alerts as a service offering a grafana before we begin i want to see a show of hands who here is familiar with prometheus and the alert manager cortex and mimir cool cool a sea of hands for the first one and not so much for the second one hopefully i get to explain a little bit about what mimir and quartus handle alerts today and you leave the room with that knowledge okay great um i'm going to be talking about the past the present and the future of the alert manager and i'm going to do that with four topics has groundwork i'll review the alert manager and remind you of its features then i'll guide you through how we achieve horizontal scalability for the alert manager in cortex and mimir moving to moving to the present i'll show you why grafana now includes the alert manager to power its alerting system and with eyes on the future i'm going to share my alert manager wishlist and what i hope to contribute back and if i can do it so can you so let's begin with the past originally started has a one file program by julius boats and matt proud the alert manager is a binary that's in charge of receiving alerts generated by prometheus or any other client application there you can configure and send notifications to other services including third parties simply put the prometheus is an alert generator and the alert manager is an alert receiver we have coined these terms as part of the alert generation compli
