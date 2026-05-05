---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Multi-tenancy"
themes: ["GitOps Delivery"]
speakers: ["Srinivas Malladi", "Adobe"]
sched_url: https://kccncna2022.sched.com/event/182Fw/multi-tenancy-for-argo-workflows-and-argo-cd-at-adobe-srinivas-malladi-adobe
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Tenancy+For+Argo+Workflows+And+Argo+CD+At+Adobe+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Multi-Tenancy For Argo Workflows And Argo CD At Adobe - Srinivas Malladi, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Srinivas Malladi, Adobe
- Schedule: https://kccncna2022.sched.com/event/182Fw/multi-tenancy-for-argo-workflows-and-argo-cd-at-adobe-srinivas-malladi-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Tenancy+For+Argo+Workflows+And+Argo+CD+At+Adobe+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Multi-Tenancy For Argo Workflows And Argo CD At Adobe.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fw/multi-tenancy-for-argo-workflows-and-argo-cd-at-adobe-srinivas-malladi-adobe
- YouTube search: https://www.youtube.com/results?search_query=Multi-Tenancy+For+Argo+Workflows+And+Argo+CD+At+Adobe+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aTgINAFV3T8
- YouTube title: Multi-Tenancy For Argo Workflows And Argo CD At Adobe - Srinivas Malladi, Adobe
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/multi-tenancy-for-argo-workflows-and-argo-cd-at-adobe/aTgINAFV3T8.txt
- Transcript chars: 37983
- Keywords: argo, workflows, cluster, access, client, clients, resources, workflow, actually, namespace, namespaces, deploy, resource, running, itself, remote, application, default

### Resumo baseado na transcript

uh we're gonna get started in a couple minutes thank you for coming uh all right okay okay great let's get started hello and welcome to my talk on multi-tenancy for Argo workflows in Argo CD at Adobe I'm Serena vasmati I'm a software engineer at Adobe who works on the internal developer platform at Adobe so before I get started I do want to give credit by emphasizing that the work I'll be preparing today is not just a product of my own efforts but a combined product of

### Excerpt da transcript

uh we're gonna get started in a couple minutes thank you for coming uh all right okay okay great let's get started hello and welcome to my talk on multi-tenancy for Argo workflows in Argo CD at Adobe I'm Serena vasmati I'm a software engineer at Adobe who works on the internal developer platform at Adobe so before I get started I do want to give credit by emphasizing that the work I'll be preparing today is not just a product of my own efforts but a combined product of efforts of many of my colleagues at Adobe and so with that let's get started so this is our agenda for today we will be starting with some background information about what my team does some terminology referenced in this presentation and an architecture overview before we dive into how we address multi-tenancy for Argo workflows and Argo CD let's get started with the internal developer platform so Adobe has three main categories of product offerings there's document Cloud Creative Cloud experience Cloud which are themselves comprised of different services and products that are developed by various internal teams at Adobe these products and services may be deployed and run using different internal platforms that serve their specific needs and in order to build and deploy and run successfully these different platforms leverage certain core mechanisms infrastructure tooling and services that are provided by the internal developer platform as part of its offering IDP internal developer platform uses and provides access to resources on various Cloud providers like AWS Azure and Adobe data centers the internal developer platform standardizes best practices and consolidates Engineering efforts across the various internal developer teams at Adobe while providing a CI CD experience that remains flexible for the different use cases you see on the screen here and next let's go over some terminology that we will be referencing for the rest of the presentation get Ops so git Ops is an architectural Paradigm where desired System state is first defined and tracked and get somewhere by some tooling that tooling then deploys that defined state to a live State on a running system the githapsulin regularly synchronizes the two states so that the live State can get automatically pulled in with any updates and it pulls in any changes made inside git Argo CDE is an example of one such git Ops tooling it supports tracking of kubernetes or Kates manifests in git and supports their deployment and synchronization to
