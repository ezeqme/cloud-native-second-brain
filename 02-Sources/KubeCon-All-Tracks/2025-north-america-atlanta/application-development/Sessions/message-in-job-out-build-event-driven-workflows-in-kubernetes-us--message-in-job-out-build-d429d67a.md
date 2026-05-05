---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Kubernetes Core"]
speakers: ["Colin Lacy", "Grace Brickley", "Cisco"]
sched_url: https://kccncna2025.sched.com/event/27FXI/message-in-job-out-build-event-driven-workflows-in-kubernetes-using-nats-cloudevents-and-sveltos-colin-lacy-grace-brickley-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Message+In%2C+Job+Out%3A+Build+Event-Driven+Workflows+in+Kubernetes+Using+NATS%2C+CloudEvents%2C+and+Sveltos+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Message In, Job Out: Build Event-Driven Workflows in Kubernetes Using NATS, CloudEvents, and Sveltos - Colin Lacy & Grace Brickley, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Colin Lacy, Grace Brickley, Cisco
- Schedule: https://kccncna2025.sched.com/event/27FXI/message-in-job-out-build-event-driven-workflows-in-kubernetes-using-nats-cloudevents-and-sveltos-colin-lacy-grace-brickley-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Message+In%2C+Job+Out%3A+Build+Event-Driven+Workflows+in+Kubernetes+Using+NATS%2C+CloudEvents%2C+and+Sveltos+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Message In, Job Out: Build Event-Driven Workflows in Kubernetes Using NATS, CloudEvents, and Sveltos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXI/message-in-job-out-build-event-driven-workflows-in-kubernetes-using-nats-cloudevents-and-sveltos-colin-lacy-grace-brickley-cisco
- YouTube search: https://www.youtube.com/results?search_query=Message+In%2C+Job+Out%3A+Build+Event-Driven+Workflows+in+Kubernetes+Using+NATS%2C+CloudEvents%2C+and+Sveltos+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IvvuZiTkGZU
- YouTube title: Message In, Job Out: Build Event-Driven Workflows in Kubernetes Using... Colin Lacy & Grace Brickley
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/message-in-job-out-build-event-driven-workflows-in-kubernetes-using-na/IvvuZiTkGZU.txt
- Transcript chars: 19680
- Keywords: cluster, actually, source, speltos, resources, create, customer, events, account, resource, clusters, managed, workflow, database, config, message, whatever, listen

### Resumo baseado na transcript

This is message in job out where we'll build event-driven workflows in Kubernetes using NATS cloud events and project spelts. So, yes, we work at Cisco as we just said, but we are also the software team for a disco services startup. Um, when it was initially created, it actually was purely in memory and fire and forget, but with the introduction of Jetream that provides event storage and consumer tracking. So we have our NAT server that is configured to save any message that it receives on disk storage. And so we can follow many of the standard event- driven architecture patterns including fan in, fan out, and saga. And what that does, project speltos acts as a management plane for kubernetes resources across multiple clusters.

### Excerpt da transcript

Welcome. This is message in job out where we'll build event-driven workflows in Kubernetes using NATS cloud events and project spelts. My name is Colin Lacy. I'm a software engineer at Cisco. >> My name is Grace Brickley. I am also a software engineer at Cisco. >> All right. So, who are we and why are we here? So, yes, we work at Cisco as we just said, but we are also the software team for a disco services startup. that disco it's coming back and as a disco company that is not quite popular as it used to be. We have to be costconscious and we are a customerfocused company right anyone who is into disco we want to support them and their interests and therefore we are a small team that relies on automation as much as possible and that's what we're going to talk about is how we automate things. >> Okay. So let's take a quick look at the tools that we'll be using to uh automate our uh disco services startup. The first of which is NATS which we'll use for event streaming and we'll use cloud events for event schema and spelts for event handling.

And let's dive a bit more into each of these service or tools. Um the first of which is NATS. So NATS is one of the most elegant lightweight messaging service systems sorry in the CNCF. It is a CNCF incubating project. So that means that it's proven adoption and maturity, but it is still working towards graduating. And at its core, NATS provides communication for distributed services. So it allows your microservices to communicate with one another rather than tightly coupling your services with REST requests or gRPC. They're able to just publish and subscribe to topics of data asynchronously. They don't even need to know about each other. They just send whatever message they want to send and whoever is interested can listen. And NATS can also act as a message bus. So it's often been compared to Kafka and Rabbit MQ, but it's faster and more lightweight. So if Kafka is your heavy duty freight train, think of Knots more like a fleet of race cars. It's faster, it's smaller, and it's incredibly responsive.

So, NATS provides event storage and consumer tracking. Um, when it was initially created, it actually was purely in memory and fire and forget, but with the introduction of Jetream that provides event storage and consumer tracking. Um, and it also supports authentication and authorization policies for both producers and consumers. So you're able to actually control who can publish, who can subscribe, and even what subject
