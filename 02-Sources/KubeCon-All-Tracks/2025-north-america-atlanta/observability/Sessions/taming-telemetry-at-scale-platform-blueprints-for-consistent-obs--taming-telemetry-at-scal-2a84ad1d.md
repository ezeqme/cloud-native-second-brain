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
themes: ["Observability", "Platform Engineering", "SRE Reliability"]
speakers: ["Aakansha Priya", "Dash0", "Marino Wijay", "Kong Inc."]
sched_url: https://kccncna2025.sched.com/event/27FUv/taming-telemetry-at-scale-platform-blueprints-for-consistent-observability-aakansha-priya-dash0-marino-wijay-kong-inc
youtube_search_url: https://www.youtube.com/results?search_query=Taming+Telemetry+at+Scale%3A+Platform+Blueprints+for+Consistent+Observability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Taming Telemetry at Scale: Platform Blueprints for Consistent Observability - Aakansha Priya, Dash0 & Marino Wijay, Kong Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Aakansha Priya, Dash0, Marino Wijay, Kong Inc.
- Schedule: https://kccncna2025.sched.com/event/27FUv/taming-telemetry-at-scale-platform-blueprints-for-consistent-observability-aakansha-priya-dash0-marino-wijay-kong-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Taming+Telemetry+at+Scale%3A+Platform+Blueprints+for+Consistent+Observability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Taming Telemetry at Scale: Platform Blueprints for Consistent Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FUv/taming-telemetry-at-scale-platform-blueprints-for-consistent-observability-aakansha-priya-dash0-marino-wijay-kong-inc
- YouTube search: https://www.youtube.com/results?search_query=Taming+Telemetry+at+Scale%3A+Platform+Blueprints+for+Consistent+Observability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lE65oWLr-qA
- YouTube title: Taming Telemetry at Scale: Platform Blueprints for Consistent Obser... Aakansha Priya & Marino Wijay
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/taming-telemetry-at-scale-platform-blueprints-for-consistent-observabi/lE65oWLr-qA.txt
- Transcript chars: 24751
- Keywords: collector, actually, observability, backend, application, better, consider, within, mesh, information, collectors, agents, applications, metrics, running, organization, important, instrument

### Resumo baseado na transcript

Uh we're here to talk about telemetry at scale and we want to leave you with a few blueprints to consider when it comes to observability. How many of you have instrumented observability within your organization today? It could be manual like you are doing some code changes and then you're manually instrumenting and collecting your telemetry or it could be auto instrumentation and then you have your shared infrastructure which could be on Kubernetes any cloud providers Versel etc. The problem with this simplicity is that it is a very uh tightly coupled with your back end and it restricts you when you are trying to scale your infrastructure. Of course there are different uh ways that you can have the collector as a demon set or you can have it as a sidecar collector. It really depends on how your environment is like, what scale you want to get into, what are your business needs.

### Excerpt da transcript

Welcome to our talk. Uh we're here to talk about telemetry at scale and we want to leave you with a few blueprints to consider when it comes to observability. How many of you have instrumented observability within your organization today? >> Okay. >> Oh, for the ones that haven't, we need to chat afterwards. >> All right. So, we'll get started. My name is Marino Wij. I am a staff solutions architect at a company called Kong. So I work with end users to help them onboard APIs into modern platforms. And when it comes to APIs, you probably have heard of an API gateway. You've probably work with a service mesh before, might even work with a developer portal of sorts. And that's the full gamut of understanding how we do API life cycle management. If you want to follow along, scan that QR code so that you don't have to, you know, extra zoom in, if you will, or use a magnifying glass. Um, and you have access to the deck. So, feel free to share with your colleagues or any of your peers, but we're here to really dive into some of the observability details.

And I'm going to pass it over to my co-speaker. >> Yeah. So, hello everyone. I'm Akansa and I work as a solution architect for this company called D-Zero. So, we are anal native observability platform. So every day I'm like talking to the customers and helping them on board uh on their hotel journey. Um I'm also like very active in the CNCF um community and I'm a CNCF ambassador just like Marino and uh yeah so I really look forward to CubeCons and this one is extra special for me because this is my first time speaking at CubeCon US event and it's a pleasure to be speaking with Marino. Uh so yeah um I think we are good to start. So let's talk about open telemetry in a nutshell. So I would say that it's like a stand like it's an open standard and it helps you define a consistent standardization to know um how to collect your telemetry. It gives you the data model. It gives you the API specification, the semantic conventions and tells you how your telemetry should ideally look like. And you have the language libraries which implements on those ideas.

So basically tells you that hey these are the same rules that we going to follow everywhere. And that's why I love these open standards because it's consistent all across. Also it's not a very small project. It's the second largest project in the CNCF ecosystem just right after cubernetes. So you can imagine that this is a widely adopted project and organizations are
