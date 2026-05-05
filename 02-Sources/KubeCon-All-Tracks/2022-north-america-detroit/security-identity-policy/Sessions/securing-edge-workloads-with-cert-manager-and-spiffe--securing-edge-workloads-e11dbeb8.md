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
themes: ["Security"]
speakers: ["Sitaram IYER", "Riaz Mohamed", "Jetstack Ltd"]
sched_url: https://kccncna2022.sched.com/event/182GZ/securing-edge-workloads-with-cert-manager-and-spiffe-sitaram-iyer-riaz-mohamed-jetstack-ltd
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Edge+Workloads+With+Cert-Manager+And+SPIFFE+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Securing Edge Workloads With Cert-Manager And SPIFFE - Sitaram IYER & Riaz Mohamed, Jetstack Ltd

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Detroit
- Speakers: Sitaram IYER, Riaz Mohamed, Jetstack Ltd
- Schedule: https://kccncna2022.sched.com/event/182GZ/securing-edge-workloads-with-cert-manager-and-spiffe-sitaram-iyer-riaz-mohamed-jetstack-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Edge+Workloads+With+Cert-Manager+And+SPIFFE+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Securing Edge Workloads With Cert-Manager And SPIFFE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GZ/securing-edge-workloads-with-cert-manager-and-spiffe-sitaram-iyer-riaz-mohamed-jetstack-ltd
- YouTube search: https://www.youtube.com/results?search_query=Securing+Edge+Workloads+With+Cert-Manager+And+SPIFFE+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ft8pvHg8iI4
- YouTube title: Securing Edge Workloads With Cert-Manager And SPIFFE - Sitaram IYER & Riaz Mohamed, Jetstack Ltd
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/securing-edge-workloads-with-cert-manager-and-spiffe/Ft8pvHg8iI4.txt
- Transcript chars: 33023
- Keywords: manager, spiffy, essentially, workload, certificate, obviously, workloads, across, cluster, driver, basically, specific, search, perspective, running, bundle, manage, application

### Resumo baseado na transcript

all right first of all thank you so much for being here um especially many of the maintainers and the members who have contributed to spiffy and cert manager who have enabled us to be here and talk about securing Edge workloads um with scruffy and set manager my name is Hitler Meyer and I'm here with Riaz Riaz Muhammad hi Al um and we our job obviously at jet stack is to talk to many of our customers and and one of the things that we have heard many

### Excerpt da transcript

all right first of all thank you so much for being here um especially many of the maintainers and the members who have contributed to spiffy and cert manager who have enabled us to be here and talk about securing Edge workloads um with scruffy and set manager my name is Hitler Meyer and I'm here with Riaz Riaz Muhammad hi Al um and we our job obviously at jet stack is to talk to many of our customers and and one of the things that we have heard many offer very often is you know the challenges around securing workloads especially as they are deployed across multiple different clusters multiple different you know domains and and as we sort of you know started to think about the motivation for this session we essentially wanted to look at it purely from a perspective of what does it take to provide a standard way of generating identities for workloads across clusters and essentially build trust that's a simple motivation that we started to look at this from securing workloads having an ability to generate an identity and distributing trust across multiple different trust domains that was the purpose with which we started thinking about the challenge that needs to be addressed and this actually started off purely from you know many of the conversations that we have had with some of the customers and specifically a customer that is in the financial space and and while this picture that you see here may look um very simple the challenge that um that the specific financial institution had um is is is massive and you know we will demonstrate you know with with some of the edge devices that we have here you know how we have addressed that how we have solved that and what does it mean to uh to uh to address and secure workloads so what you're seeing there on the picture is a bunch of terminals obviously and then a set of services that are core there the simplest way to sort of you know think about this is the bank here provides a set of services uh that are consumed by different merchants and and as part of that the merchant terminal that's out there science generates some kind of a private key pair sends it across with chart you know obviously the bank validates it and sends a token back so I'm describing this in a very very simple form and over a period of time this token is used to sort of you know manage payments refunds and things like that and this is the standard operating model in which various different Merchants work uh payment terminals core Bank Services
