---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["Community Governance"]
speakers: ["Katie Gamanji", "Senior Field Engineer", "Apple"]
sched_url: https://kccnceu2025.sched.com/event/1zgHB/keynote-open-source-in-apples-private-cloud-compute-katie-gamanji-senior-field-engineer-apple
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Open+Source+in+Apple%E2%80%99s+Private+Cloud+Compute+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Open Source in Apple’s Private Cloud Compute - Katie Gamanji, Senior Field Engineer, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Katie Gamanji, Senior Field Engineer, Apple
- Schedule: https://kccnceu2025.sched.com/event/1zgHB/keynote-open-source-in-apples-private-cloud-compute-katie-gamanji-senior-field-engineer-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Open+Source+in+Apple%E2%80%99s+Private+Cloud+Compute+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Open Source in Apple’s Private Cloud Compute.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1zgHB/keynote-open-source-in-apples-private-cloud-compute-katie-gamanji-senior-field-engineer-apple
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Open+Source+in+Apple%E2%80%99s+Private+Cloud+Compute+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CEr3HECMgBk
- YouTube title: Keynote: Open Source in Apple’s Private Cloud Compute - Katie Gamanji, Apple (ISL)
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-open-source-in-apples-private-cloud-compute/CEr3HECMgBk.txt
- Transcript chars: 4192
- Keywords: private, compute, security, privacy, server, source, intelligence, models, silicon, within, device, leverage, performance, resilience, ecosystem, gamanji, technical, iphone

### Resumo baseado na transcript

Last year at Dubdubdc, we introduced Apple intelligence, a personalized intelligence system that brings powerful generative models to iPhone, iPad, and Mac. To deliver this advanced security architecture, whenever possible, Apple Intelligence processes tasks locally on the device. Since privacy and security is at the root of our components, we ensure the response payloads are encrypted by the user device and rooted using gRPC to the PCC gateway all the way to Apple silicon machines. From a performance standpoint, Swift has a very low memory footprint that keeps the system resource usage down. High resilience and performance of gRPC with the security properties of Swift enables us to bring industry-leading device security models into the cloud. If you'd like to learn more about our use cases in the cloud native space and how we engage with the wider ecosystem, you can attend one of the 10 other talks delivered by Apple engineers at this conference.

### Excerpt da transcript

Hello everyone and welcome to CubeCon and CloudNative Con London. My name is Katie Gamanji and I am a senior engineer at Apple. I'm also part of the TOC or technical oversight committee within CNCF. Last year at Dubdubdc, we introduced Apple intelligence, a personalized intelligence system that brings powerful generative models to iPhone, iPad, and Mac. Apple intelligence is designed to protect your privacy at every step. To deliver this advanced security architecture, whenever possible, Apple Intelligence processes tasks locally on the device. But more sophisticated tasks require additional processing power. Private cloud compute or PCC allows us to scale our computational capacity and draw on even larger serverbased models for these complex requests. These models run on servers we have especially created using Apple silicon and offer the privacy and security of your iPhone from the silicon on up. Private cloud compute is a great example of how we're investing in and adopting open source technologies.

We draw from the security properties of the swift programming language to run software with transparency built in and leverage the high performance and resilience of gRPC for the transportation layer. GRPC is a mature CNCF project with more than eight years of upstream development. It is a widely known framework that can efficiently connect services across distributed infrastructure and within private cloud compute. We heavily leverage the building blocks of gRPC for the transportation layer. Birectional streaming is a core part of gRPC that we use to communicate load information between the PCC gateway and a single Apple silicon server. Since privacy and security is at the root of our components, we ensure the response payloads are encrypted by the user device and rooted using gRPC to the PCC gateway all the way to Apple silicon machines. And finally, JRPC has a very robust livveness probing that is highly configurable. As JRPC controls its underlying transport, we lean into its resilience to ensure it is capable of performing these probes.

From a technical standpoint, some of the libraries we use are gRPC swift and swift protobuff, which in simple terms are the Swift implementation for gRPC and Protobuff. And at Apple, we've written all kinds of services in Swift from iCloud keychain to App Store processing pipelines and SharePlay file sharing. And when building out a service that supports Apple commitments to user privacy, Swift was a natural choice for
