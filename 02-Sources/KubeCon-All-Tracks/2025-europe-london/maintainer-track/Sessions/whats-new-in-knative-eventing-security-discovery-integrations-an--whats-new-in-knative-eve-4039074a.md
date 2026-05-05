---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Pierangelo Di Pilato", "Christoph Stäbler", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1tcy5/whats-new-in-knative-eventing-security-discovery-integrations-and-jobsink-pierangelo-di-pilato-christoph-stabler-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+in+Knative+Eventing%3A+Security%2C+Discovery%2C+Integrations%2C+and+JobSink+CNCF+KubeCon+2025
slides: []
status: parsed
---

# What's New in Knative Eventing: Security, Discovery, Integrations, and JobSink - Pierangelo Di Pilato & Christoph Stäbler, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Pierangelo Di Pilato, Christoph Stäbler, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1tcy5/whats-new-in-knative-eventing-security-discovery-integrations-and-jobsink-pierangelo-di-pilato-christoph-stabler-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+in+Knative+Eventing%3A+Security%2C+Discovery%2C+Integrations%2C+and+JobSink+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre What's New in Knative Eventing: Security, Discovery, Integrations, and JobSink.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcy5/whats-new-in-knative-eventing-security-discovery-integrations-and-jobsink-pierangelo-di-pilato-christoph-stabler-red-hat
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+in+Knative+Eventing%3A+Security%2C+Discovery%2C+Integrations%2C+and+JobSink+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6usWUdJMyHY
- YouTube title: What's New in Knative Eventing: Security, Discovery, Int... Pierangelo Di Pilato & Christoph Stäbler
- Match score: 0.824
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/whats-new-in-knative-eventing-security-discovery-integrations-and-jobs/6usWUdJMyHY.txt
- Transcript chars: 24895
- Keywords: events, broker, source, eventing, create, basically, policy, authorization, processing, namespace, security, support, resource, request, another, systems, transform, resources

### Resumo baseado na transcript

Um today we were going to talk about what we have been working on for like the 12 18 months ago. Um we're going to share what we are working on like security discovery integrations and job sync and also uh event transform. By default, canative eventing does not enforce security on event delivery, meaning traffic is unencrypted, unauthorized, and unauthenticated. And we all know this poses risks in not only production environments and enterprises need secure event- driven architectures. And to address those needs, Kative Eventing provides in its or provided in its latest or recent versions three new key security features and also transport encryption via TLS through HTTP endpoints to make sure event traffic is encrypted. As said, by default, Kative eventing does not um enforce security or does not encrypt um events.

### Excerpt da transcript

Thanks for joining us. Um today we were going to talk about what we have been working on for like the 12 18 months ago. Um we're going to share what we are working on like security discovery integrations and job sync and also uh event transform. I'm Pangelo and I'm software engineer radar. I also have um be the working group lead inventing and uh here's Kristoff. Yeah. Hello and welcome from my side as well. My name is Kristoff. I'm also working at Redhead as a software engineer on serverless topics and I'm also a maintainer of different Canative eventing projects. So let's see what we have on agenda for today and what we'll show you. First, we'll give you a quick update on the latest eventing security features, including support for transport encryption and authorization. Afterwards, um, we show you the latest updates on eventing integrations, how we, for example, can connect to third party services like AWS SQS now natively with eventing. Afterwards, Panchul will give us an update and introduction on event discovery and the new chopsync feature.

And finally, we'll give you an overview about the brand new event transform which helps which help which helps you to kind of reshape your events and which is an often asked feature from your site. Okay, let's first start with security in canative eventing. By default, canative eventing does not enforce security on event delivery, meaning traffic is unencrypted, unauthorized, and unauthenticated. And we all know this poses risks in not only production environments and enterprises need secure event- driven architectures. And to address those needs, Kative Eventing provides in its or provided in its latest or recent versions three new key security features and also transport encryption via TLS through HTTP endpoints to make sure event traffic is encrypted. Then authentication via Open ID connect to allow event consumers to verify who sent an event. And finally, authorization via event policies which plays together with authentication to allow you to restrict who can send events to your resources.

Okay, let's start with transport encryption. As said, by default, Kative eventing does not um enforce security or does not encrypt um events. And we all know that as soon as somebody has access to the network, they could potentially intercept those events and this poses risks. And by providing HTTPS endpoints for addressables, we now can or addressables now accept TLS encrypted and events. And this is done on two sides.
