---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering", "Networking", "SRE Reliability"]
speakers: ["Shahar Azulay", "Groundcover", "Nirmal Mehta", "Amazon Web Services"]
sched_url: https://kccnceu2024.sched.com/event/1YeNc/troubleshooting-hidden-performance-and-costs-in-network-traffic-across-multiple-azs-with-ebpf-shahar-azulay-groundcover-nirmal-mehta-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Troubleshooting+Hidden+Performance+and+Costs+in+Network+Traffic+Across+Multiple+AZs+with+eBPF+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Troubleshooting Hidden Performance and Costs in Network Traffic Across Multiple AZs with eBPF - Shahar Azulay, Groundcover & Nirmal Mehta, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Networking]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Shahar Azulay, Groundcover, Nirmal Mehta, Amazon Web Services
- Schedule: https://kccnceu2024.sched.com/event/1YeNc/troubleshooting-hidden-performance-and-costs-in-network-traffic-across-multiple-azs-with-ebpf-shahar-azulay-groundcover-nirmal-mehta-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Troubleshooting+Hidden+Performance+and+Costs+in+Network+Traffic+Across+Multiple+AZs+with+eBPF+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Troubleshooting Hidden Performance and Costs in Network Traffic Across Multiple AZs with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNc/troubleshooting-hidden-performance-and-costs-in-network-traffic-across-multiple-azs-with-ebpf-shahar-azulay-groundcover-nirmal-mehta-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Troubleshooting+Hidden+Performance+and+Costs+in+Network+Traffic+Across+Multiple+AZs+with+eBPF+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CF0vAWhxKU4
- YouTube title: Troubleshooting Hidden Performance and Costs in Network Traffic Across Multiple AZs with eBPF
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/troubleshooting-hidden-performance-and-costs-in-network-traffic-across/CF0vAWhxKU4.txt
- Transcript chars: 31105
- Keywords: traffic, metrics, network, ebpf, availability, cluster, actually, specific, decision, resiliency, application, cost, running, across, deployment, decisions, talking, backend

### Resumo baseado na transcript

all right welcome to troubleshooting hidden performance and cost and network traffic across multiple azs with ebpf who here knows what ebpf is oh we're done you want to come up here yeah okay awesome uh the then uh we'll get right into it I'm Nala I'm a principal specialist solution architect at AWS and uh I work on containers and serverless services and focus on observ ility and a few months ago Shahar and myself we were talking about some of the customer problems some of your own problems

### Excerpt da transcript

all right welcome to troubleshooting hidden performance and cost and network traffic across multiple azs with ebpf who here knows what ebpf is oh we're done you want to come up here yeah okay awesome uh the then uh we'll get right into it I'm Nala I'm a principal specialist solution architect at AWS and uh I work on containers and serverless services and focus on observ ility and a few months ago Shahar and myself we were talking about some of the customer problems some of your own problems around visibility and network and we started coming up with this idea for this talk and so I'm joined by Shahar hey everyone I'm shakar oai and I'm uh the co-founder and CEO of gr cover guar is a full stack observability platform built for cloud native environments uh which uses ebpf which we're going to talk about and this talk in yeah it looks like there's a lot of EF fans here yeah who likes ebpf there we go louder louder yeah so why are we here why does ebpf matter why does visibility observability matter the Amazon CTO verer Vogal he said a few years ago everything fails all the time who's seen this slide before who's seen this quote it's true right this is our North Star like this is our architectural principle at AWS this this is what drives what we do at AWS and also what we tell our customers to do you have to be aware that everything fails all the time and so that leads to an architecture that centers around resilience you have to design your systems to be able to deal with those failures but resilience comes with tradeoffs sometimes it could be expensive or you you don't know the cost of it so what is resilience resilience refers to the ability of workloads to respond to and quickly recover from those failures and we think of a a mental model to help us think about resilience on one side we have high availability and that's the resistance of your system to those failures through the design of the of your system and then disaster recover so how fast can you recover when there was some kind of failure something out of some high impact failure so together this creates a spectrum that we think of as continuous resilience and one of the main components of continuous resilience architectures at AWS is availability zones who here knows what an availability zone is okay so this is just a quick recap this perfect audience say no ebpf they know azs they can come up here and do this talk um so azs are our availability zones are one of our core components for Designing f
