---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jens Freimann", "Red Hat"]
sched_url: https://kccncna2023.sched.com/event/1R2sa/the-next-frontier-exploring-the-confidentiality-of-kubernetes-control-planes-jens-freimann-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=The+Next+Frontier%3A+Exploring+the+Confidentiality+of+Kubernetes+Control+Planes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Next Frontier: Exploring the Confidentiality of Kubernetes Control Planes - Jens Freimann, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Jens Freimann, Red Hat
- Schedule: https://kccncna2023.sched.com/event/1R2sa/the-next-frontier-exploring-the-confidentiality-of-kubernetes-control-planes-jens-freimann-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=The+Next+Frontier%3A+Exploring+the+Confidentiality+of+Kubernetes+Control+Planes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Next Frontier: Exploring the Confidentiality of Kubernetes Control Planes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sa/the-next-frontier-exploring-the-confidentiality-of-kubernetes-control-planes-jens-freimann-red-hat
- YouTube search: https://www.youtube.com/results?search_query=The+Next+Frontier%3A+Exploring+the+Confidentiality+of+Kubernetes+Control+Planes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QsGaGiqf6F4
- YouTube title: The Next Frontier: Exploring the Confidentiality of Kubernetes Control Planes - Jens Freimann
- Match score: 0.996
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-next-frontier-exploring-the-confidentiality-of-kubernetes-control/QsGaGiqf6F4.txt
- Transcript chars: 24227
- Keywords: confidential, control, container, containers, provider, infrastructure, basically, server, runtime, memory, threat, components, hypers, computing, cluster, course, running, hardware

### Resumo baseado na transcript

okay hi and welcome everyone my name is yans I work for rad and uh I prepared this presentation together with my colleague prip he can't be here today so this talk is about how we can leverage confidential Computing technology to enhance the security and the resilience of data and use in the kubernetes control plane so before we jump in um I'd just like to get a feeling for the audience who here has heard of confidential Computing can you show your hand okay who has heard of

### Excerpt da transcript

okay hi and welcome everyone my name is yans I work for rad and uh I prepared this presentation together with my colleague prip he can't be here today so this talk is about how we can leverage confidential Computing technology to enhance the security and the resilience of data and use in the kubernetes control plane so before we jump in um I'd just like to get a feeling for the audience who here has heard of confidential Computing can you show your hand okay who has heard of uh CER containers also quite a few and uh who are sort of confidential containers oh still also a few hands great so um let's jump in but let's see why the control plane what it does and why it needs to be protected in the beginning um so the control plane you know I think it's already in the name um it controls your cluster and if you own it you're basically root in your cluster so what does it do well it does orchestrates all major cluster activities um like deploying applications controlling pods and nodes scaling resources up and down so really complex tasks and it also houses sensitive data um it houses secrets that could be passwords or API Keys um it has state data which represents the current state of the cluster and many more things that need to be protected it has access control um and it also the API is the big part of it um it's the primary interface through which users and external systems interact with the cluster and it receives requests for operations then translates it into internal communication protocols and ensures the correct execution so it has a really pivotal role really um and its security is uh of great importance of course so there's a subset of control components that we want to focus on here and it's those that are end user facing so we call it I call it request serving control plane components and these include of course the API server but there's also others like ingros or o and there then there also um kubernetes dist specific services so these components are all critical because handle requests from users directly um now let's take a closer look um the bottom line is we need to protect those parts from unauthorized access and from manipulation so that trust can be established um it's they are very exposed that's in the nature of these components they need to be accessible at all times and listen for incoming requests so this Direct exposure um to external entities losers and software um makes them basically the first line of defense and also a prime tar
