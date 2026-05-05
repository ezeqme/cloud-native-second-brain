---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Networking + Edge + Telco"
themes: ["Networking", "SRE Reliability"]
speakers: ["Kyoungho An", "Protima Banerjee", "Real-Time Innovations (RTI)"]
sched_url: https://kccncna2023.sched.com/event/1R2pd/advancing-real-time-performance-at-the-edge-cloud-dds-real-time-publish-subscribe-open-standards-kyoungho-an-protima-banerjee-real-time-innovations-rti
youtube_search_url: https://www.youtube.com/results?search_query=Advancing+Real-Time+Performance+at+the+Edge+Cloud%3A+DDS+%26+Real-Time+Publish+Subscribe+Open+Standards+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Advancing Real-Time Performance at the Edge Cloud: DDS & Real-Time Publish Subscribe Open Standards - Kyoungho An & Protima Banerjee, Real-Time Innovations (RTI)

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Kyoungho An, Protima Banerjee, Real-Time Innovations (RTI)
- Schedule: https://kccncna2023.sched.com/event/1R2pd/advancing-real-time-performance-at-the-edge-cloud-dds-real-time-publish-subscribe-open-standards-kyoungho-an-protima-banerjee-real-time-innovations-rti
- Busca YouTube: https://www.youtube.com/results?search_query=Advancing+Real-Time+Performance+at+the+Edge+Cloud%3A+DDS+%26+Real-Time+Publish+Subscribe+Open+Standards+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Advancing Real-Time Performance at the Edge Cloud: DDS & Real-Time Publish Subscribe Open Standards.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pd/advancing-real-time-performance-at-the-edge-cloud-dds-real-time-publish-subscribe-open-standards-kyoungho-an-protima-banerjee-real-time-innovations-rti
- YouTube search: https://www.youtube.com/results?search_query=Advancing+Real-Time+Performance+at+the+Edge+Cloud%3A+DDS+%26+Real-Time+Publish+Subscribe+Open+Standards+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=spGyYq80EM8
- YouTube title: Advancing Real-Time Performance at the Edge Cloud: DDS & Real-Time... Kyoungho An & Protima Banerjee
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/advancing-real-time-performance-at-the-edge-cloud-dds-real-time-publis/spGyYq80EM8.txt
- Transcript chars: 32310
- Keywords: latency, actually, performance, standards, message, messages, environments, applications, communications, protocol, around, within, realtime, specific, real-time, provide, multicast, subscribe

### Resumo baseado na transcript

good morning everyone good morning hi um thank you thank you so much for for coming to our talk uh this is this is our our first cubec con and and we're we're really excited to be here uh my my name is patima bannery I'm here with my colleague kangan uh we're both research Engineers from a small business called uh realtime Innovations which is based out of Sunny Bale California and we're here today to speak on the topic of bringing real-time performance to the edge Cloud uh

### Excerpt da transcript

good morning everyone good morning hi um thank you thank you so much for for coming to our talk uh this is this is our our first cubec con and and we're we're really excited to be here uh my my name is patima bannery I'm here with my colleague kangan uh we're both research Engineers from a small business called uh realtime Innovations which is based out of Sunny Bale California and we're here today to speak on the topic of bringing real-time performance to the edge Cloud uh more specific specifically we're we're here to introduce the data distribution service or or DDS and realtime publish subscribe or rtps standards uh to the to the cubec con audience here uh so I'm going to start the talk with an overview of DDS and rtps and the standards and the benefits that they bring to the edge Cloud um environment and then kyungho is going to conclude uh by showing some DDS performance benchmarks that really highlight the power that these Open Standards uh can can bring uh so before we get started uh just just a little bit of background about us uh so so realtime Innovations or RTI was founded um back in 1991 by a group of researchers from the robotics Lab at Stanford University so they were interested in building um software that could provide the the kind of fast reliable Communications that are needed by robots uh that that uh operate in ad hoc teams so uh you know for communicating things like sensor data control messages events and Status um and their work really became the foundation for what later became uh the DDS and and rtps standards so to continue on that thread uh today RTI provides communication software for domains such as autonomous systems uh including like commercial automotive healthc Care so including things like tele medicine and patient monitoring Industrial Automation so things like smart manufactur facturing and uh industrial robotics um energy uh with like smart grids renewable energy um and in defense and Aerospace so a few of these are highlighted um on the slide here but in addition to these product Solutions we've also been involved in a lot of um uh standards associated with these domains so things like autosar and abcc and the automotive space uh things like ice and open FMB and like the medical space and then in the robotic space uh for those of you who might be familiar with with Ros 2 or the or the Robot Operating System uh DDS is actually the underlying uh Communications protocol used by by the Ros 2 operating system so the intere
