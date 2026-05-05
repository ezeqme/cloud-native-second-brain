---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Christos Markou", "Elastic", "Jacob Aronoff"]
sched_url: https://kccncna2025.sched.com/event/27FZN/otel+k8s-vnulb-an-introduction-to-opentelemetry-for-kubernetes-users-christos-markou-elastic-jacob-aronoff
youtube_search_url: https://www.youtube.com/results?search_query=OTel%2BK8s%3D+%E2%9D%A4%EF%B8%8F%3A+An+Introduction+To+OpenTelemetry+for+Kubernetes+Users+CNCF+KubeCon+2025
slides: []
status: parsed
---

# OTel+K8s= ❤️: An Introduction To OpenTelemetry for Kubernetes Users - Christos Markou, Elastic & Jacob Aronoff

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Christos Markou, Elastic, Jacob Aronoff
- Schedule: https://kccncna2025.sched.com/event/27FZN/otel+k8s-vnulb-an-introduction-to-opentelemetry-for-kubernetes-users-christos-markou-elastic-jacob-aronoff
- Busca YouTube: https://www.youtube.com/results?search_query=OTel%2BK8s%3D+%E2%9D%A4%EF%B8%8F%3A+An+Introduction+To+OpenTelemetry+for+Kubernetes+Users+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre OTel+K8s= ❤️: An Introduction To OpenTelemetry for Kubernetes Users.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZN/otel+k8s-vnulb-an-introduction-to-opentelemetry-for-kubernetes-users-christos-markou-elastic-jacob-aronoff
- YouTube search: https://www.youtube.com/results?search_query=OTel%2BK8s%3D+%E2%9D%A4%EF%B8%8F%3A+An+Introduction+To+OpenTelemetry+for+Kubernetes+Users+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cCGNs7nyutU
- YouTube title: OTel+K8s= ❤️: An Introduction To OpenTelemetry for Kubernetes... Christos Markou & Jacob Aronoff
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/otel-k8s-an-introduction-to-opentelemetry-for-kubernetes-users/cCGNs7nyutU.txt
- Transcript chars: 31316
- Keywords: collector, metrics, configuration, cluster, logs, specific, operator, prometheus, component, useful, deployment, support, receiver, another, collectors, charts, important, otel

### Resumo baseado na transcript

Today we're going to tell you all about open telemetry and Kubernetes and why it's all about love. And I am Christo Marco, principal software engineer at elastic also approver for the open telemetry collector control project and approver for various areas in semant convention project. So observability in Kubernetes we're going to talk about the three main signals metrics traces and logs metrics explore the current and historical system state each point value at a time stamp with some attached metadata. Uh in Kubernetes pretty much all the time these are going to be emitted through Prometheus. Uh some Kubernetes services also now offer tracing through open telemetry. In OTEL as I mentioned earlier uh you know pods emit metrics through Prometheus.

### Excerpt da transcript

Hello everybody. Thank you very much for coming. Today we're going to tell you all about open telemetry and Kubernetes and why it's all about love. Uh it's going to be introductory going into some more advanced topics. That is the goal. Um my name is Jacob Areronoff. I'm a founding engineer at Tero. I'm a maintainer for the hotel operator. I'm also a maintainer for the hotel helm charts. And I am Christo Marco, principal software engineer at elastic also approver for the open telemetry collector control project and approver for various areas in semant convention project. CNCF ambassador as well. So super excited to be here today and yeah let's get started. >> Yeah, let's get going. So our goals today are to help you understand uh open telemetry basics for Kubernetes monitoring. We're going to demonstrate some reference architectures for observing Kubernetes and we'll also share some trade-offs that you may encounter. We'll start by introducing hotel introducing you know general telemetry concepts. We'll then go into telemetry collection in Kubernetes deployment strategies and implementation operators and Helm charts and then we'll end with those operational considerations.

So to begin, OTEL and Coupe. What's OTEL? Many of you are probably already aware. Uh we're the second largest project in the CNCF last time I checked. Uh it's an open source standard for telemetry, metrics, logs, and traces. I am not going to be talking about profiles today. I apologize. Uh we are a vendor neutral telemetry collection as well. Uh and it's a vast ecosystem of tooling uh maintained by a bunch of companies. So observability in Kubernetes we're going to talk about the three main signals metrics traces and logs metrics explore the current and historical system state each point value at a time stamp with some attached metadata. Uh in Kubernetes pretty much all the time these are going to be emitted through Prometheus. Uh and it's important that we consider that we'll talk about that later. Traces are I think the most powerful uh telemetry type. Uh they demonstrate the flow of a request through a set of services. It allows fine- grain understanding of why a behavior occurred. Uh some Kubernetes services also now offer tracing through open telemetry.

So you can capture those which is super helpful. Lastly, logs. They show diagnostic information. Uh you know, Kubernetes services log plenty. Um and Kubernetes has great support for this, right? We can tail logs. We can collect th
