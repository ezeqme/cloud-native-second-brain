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
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Erik Godding Boye", "Zenior", "Tim Ramlot", "Venafi", "a CyberArk Company"]
sched_url: https://kccnceu2025.sched.com/event/1td0e/how-we-solved-tls-at-scale-self-service-multi-tenant-cert-manager-erik-godding-boye-zenior-tim-ramlot-venafi-a-cyberark-company
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Solved+TLS+at+Scale%3A+Self-Service%2C+Multi-Tenant+Cert-manager+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How We Solved TLS at Scale: Self-Service, Multi-Tenant Cert-manager - Erik Godding Boye, Zenior & Tim Ramlot, Venafi, a CyberArk Company

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Erik Godding Boye, Zenior, Tim Ramlot, Venafi, a CyberArk Company
- Schedule: https://kccnceu2025.sched.com/event/1td0e/how-we-solved-tls-at-scale-self-service-multi-tenant-cert-manager-erik-godding-boye-zenior-tim-ramlot-venafi-a-cyberark-company
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Solved+TLS+at+Scale%3A+Self-Service%2C+Multi-Tenant+Cert-manager+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How We Solved TLS at Scale: Self-Service, Multi-Tenant Cert-manager.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td0e/how-we-solved-tls-at-scale-self-service-multi-tenant-cert-manager-erik-godding-boye-zenior-tim-ramlot-venafi-a-cyberark-company
- YouTube search: https://www.youtube.com/results?search_query=How+We+Solved+TLS+at+Scale%3A+Self-Service%2C+Multi-Tenant+Cert-manager+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gWgagjHtnlE
- YouTube title: How We Solved TLS at Scale: Self-Service, Multi-Tenant Cert-manager - Erik Godding Boye & Tim Ramlot
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-we-solved-tls-at-scale-self-service-multi-tenant-cert-manager/gWgagjHtnlE.txt
- Transcript chars: 25503
- Keywords: manager, certificate, actually, search, company, certificates, cluster, bundle, client, policy, request, tenants, available, wanted, resource, created, basically, application

### Resumo baseado na transcript

So in this presentation we will be explaining how to do or how to solve TLS at scale. More specifically we'll actually be going into um Eric setup the setup that Eric created for one of his clients uh where he's actually using manager in a very advanced way. Um so before joining the our platform team uh this was a situation we have uh multiple Kubernetes clusters and multiple Kafka clusters running on VM so not running on on Kubernetes. Uh they typically use micros service architecture meaning we have a thousand of workloads running in our Kubernetes clusters. Um so we tried to set up Spy, but we had some challenges running it on our target Kubernetes clusters which are Open Shift. And uh here is one example on on how a a spiffy ID might look like for a Kubernetes workload.

### Excerpt da transcript

So in this presentation we will be explaining how to do or how to solve TLS at scale. More specifically we'll actually be going into um Eric setup the setup that Eric created for one of his clients uh where he's actually using manager in a very advanced way. Um he set it up such that it's usable within a multi-tenant environment and such that all these tenants can self-service their own certificates. My name is Tim. I work for Cyber Arc. Um, I'm a search management maintainer and so is Eric. And I'm Eric. Uh, I work as a contractor, but for many years I've been working for the startnet, the Norwegian TSO, which is responsible for the transmission of energy in the Norwegian power grid. Okay, so a bit more about manager. Third manager like probably most of you already know is a CNCF graduated project and we are very interested in solving X509 on Kubernetes and Open Shift. Um so if you look at search manager on GitHub this organization we have a couple projects that are very interesting and the most important one of course is search manager itself.

You have trust manager, approve a policy, uh, and a few others. We'll actually go into those, uh, later. Uh, we're a fairly popular project. I think we have almost 12,000 GitHub stars, uh, 400 contributors, and we are being downloaded many, many times per day. Um, and today we will actually be talking about how Eric is using Manager. Um, but that wasn't always the case, I think. So, when Eric started uh with this client, he actually didn't use any search manager at all. So, he went from zero to the point where he is at right now, which is actually being a search manager maintainer. It's like a amazing story basically. Um so in this presentation we'll try to actually uh take you through the journey that Eric made and kind of show also how he set up search manager for his client and how he um really got into this very advanced use case. Yeah. So first uh a bit of context here. Um I'm used to work as an application developer for many years uh also for startnet. Um so before joining the our platform team uh this was a situation we have uh multiple Kubernetes clusters and multiple Kafka clusters running on VM so not running on on Kubernetes.

Uh I was using this environment uh as a developer but uh after some time I I joined the application team. Um this setup was created by a project that uh had a lot of applications spin up in a cluster doing a lot of stuff. So but there was some challenges because of time constraint
