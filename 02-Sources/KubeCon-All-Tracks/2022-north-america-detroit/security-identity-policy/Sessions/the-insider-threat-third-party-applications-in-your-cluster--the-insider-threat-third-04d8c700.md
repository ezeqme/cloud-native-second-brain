---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Dagan Henderson", "Raft", "LLC", "Will Kline", "Dark Wolf Solutions"]
sched_url: https://kccncna2022.sched.com/event/182K3/the-insider-threat-third-party-applications-in-your-cluster-dagan-henderson-raft-llc-will-kline-dark-wolf-solutions
youtube_search_url: https://www.youtube.com/results?search_query=The+Insider+Threat%3A+Third-Party+Applications+In+Your+Cluster+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The Insider Threat: Third-Party Applications In Your Cluster - Dagan Henderson, Raft, LLC & Will Kline, Dark Wolf Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Dagan Henderson, Raft, LLC, Will Kline, Dark Wolf Solutions
- Schedule: https://kccncna2022.sched.com/event/182K3/the-insider-threat-third-party-applications-in-your-cluster-dagan-henderson-raft-llc-will-kline-dark-wolf-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=The+Insider+Threat%3A+Third-Party+Applications+In+Your+Cluster+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The Insider Threat: Third-Party Applications In Your Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182K3/the-insider-threat-third-party-applications-in-your-cluster-dagan-henderson-raft-llc-will-kline-dark-wolf-solutions
- YouTube search: https://www.youtube.com/results?search_query=The+Insider+Threat%3A+Third-Party+Applications+In+Your+Cluster+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t0buULC9-Y8
- YouTube title: The Insider Threat: Third-Party Applications In Your Cluster - Dagan Henderson & Will Kline
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-insider-threat-third-party-applications-in-your-cluster/t0buULC9-Y8.txt
- Transcript chars: 35937
- Keywords: application, running, security, cluster, applications, looking, container, longhorn, third-party, vulnerabilities, started, upstream, together, working, projects, vulnerability, actually, basically

### Resumo baseado na transcript

hi my name is Degen I'm a developer and occasionally a security researcher for the last couple of years I've been working primarily as a kubernetes platform engineer and I really enjoy working in kubernetes and compliant restricted environments so I think things like sock 2 and fedramp sort of my happy place my name is Will Klein I'm also a platform security engineer you know it's been really exciting for me to watch kubernetes grow over the last couple years you know I kind of started out doing containers

### Excerpt da transcript

hi my name is Degen I'm a developer and occasionally a security researcher for the last couple of years I've been working primarily as a kubernetes platform engineer and I really enjoy working in kubernetes and compliant restricted environments so I think things like sock 2 and fedramp sort of my happy place my name is Will Klein I'm also a platform security engineer you know it's been really exciting for me to watch kubernetes grow over the last couple years you know I kind of started out doing containers in kind of similar environments this is what day is described and we're you know orchestrating them with salt stack I don't know if you guys remember salt stack back in the day but like you know just seeing that grow over time has been incredible and I'm also kind of working with digging on different projects to help modernize deployments for different customers that we work together with today we're going to be talking about third-party applications um why we love them some of the dangers that they impose so what do we mean when we talk about a third-party application and basically ever since subroutines were invented in the 1940s people have been running other people's code so third party is code that you didn't write and the question is not do I use third-party applications it is an absolute surety that you are going to use a third-party application yeah and I think one of the best things about kubernetes in my experience has been you know going from that world where you know vendors would deliver you a random RPM file or even like a tarball and then you eventually it turned into like a VM that they would deliver to you and you'd have to figure out what's in this VM what does it need to run how do I need to network it together like what is it what is it bringing to my my network here what about when I install it how do I meet my security baselines and now with kubernetes we're delivering applications and getting applications from third-party vendors which have a full description of you know what kind of containers does it need what is the networking requirements what kind of service account access does it need and it brings all that together in a really beautiful API that I can use you know whether I'm deploying an Ingress on albs and AWS or I'm using metal lb on my bare metal servers I've got that one API that I can learn about and introspect and understand what I'm about to ingest and bring into my cluster so in addition to kubernetes itself what do
