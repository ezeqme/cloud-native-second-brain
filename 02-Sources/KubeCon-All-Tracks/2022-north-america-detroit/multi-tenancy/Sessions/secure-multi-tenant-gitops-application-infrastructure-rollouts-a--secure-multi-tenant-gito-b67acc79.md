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
themes: ["Security", "GitOps Delivery"]
speakers: ["Vikram Sethi", "Adobe", "Manabu McCloskey", "Amazon Web Services"]
sched_url: https://kccncna2022.sched.com/event/182Hy/secure-multi-tenant-gitops-application-infrastructure-rollouts-at-adobe-vikram-sethi-adobe-manabu-mccloskey-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Secure+Multi-Tenant+GitOps+Application+%26+Infrastructure+Rollouts+At+Adobe+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Secure Multi-Tenant GitOps Application & Infrastructure Rollouts At Adobe - Vikram Sethi, Adobe & Manabu McCloskey, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Security]], [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Vikram Sethi, Adobe, Manabu McCloskey, Amazon Web Services
- Schedule: https://kccncna2022.sched.com/event/182Hy/secure-multi-tenant-gitops-application-infrastructure-rollouts-at-adobe-vikram-sethi-adobe-manabu-mccloskey-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Secure+Multi-Tenant+GitOps+Application+%26+Infrastructure+Rollouts+At+Adobe+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Secure Multi-Tenant GitOps Application & Infrastructure Rollouts At Adobe.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Hy/secure-multi-tenant-gitops-application-infrastructure-rollouts-at-adobe-vikram-sethi-adobe-manabu-mccloskey-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Secure+Multi-Tenant+GitOps+Application+%26+Infrastructure+Rollouts+At+Adobe+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y_AmsPaWLYg
- YouTube title: Secure Multi-Tenant GitOps Application & Infrastructure Rollouts...- Vikram Sethi & Manabu McCloskey
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/secure-multi-tenant-gitops-application-infrastructure-rollouts-at-adob/Y_AmsPaWLYg.txt
- Transcript chars: 34140
- Keywords: resources, platform, tenant, workflow, cluster, namespace, resource, provider, argo, composite, actually, provisioning, infrastructure, config, remote, account, manifest, requirements

### Resumo baseado na transcript

thank you everyone for coming for this session good morning good afternoon good evening depending on where you're logged in from and it's so good to be back at kubecon in person the last one that I attended in person was that San Diego in 2019 how many of you were there in San Diego wow it's great good to see repeat audience and how many of you are actually aware of Argo and cross-plane projects great that's a really good note to start on so let's get started my

### Excerpt da transcript

thank you everyone for coming for this session good morning good afternoon good evening depending on where you're logged in from and it's so good to be back at kubecon in person the last one that I attended in person was that San Diego in 2019 how many of you were there in San Diego wow it's great good to see repeat audience and how many of you are actually aware of Argo and cross-plane projects great that's a really good note to start on so let's get started my name is Vikram and I'm a senior architect at Adobe I work in the developer platforms organization and these days I'm actually working on introducing Advanced capabilities into our internal developer platform and these capabilities include GitHub space CI CD it also includes GitHub space infrastructure provisioning and also building an AI Ops foundation for an internal developer platform with me with me I have manabu from AWS hey guys my name is Solutions architect for AWS and I focus on open source Technologies especially around infrastructure excited to be here cool thanks so today we're going to talk about how Adobe it enabled GitHub space infrastructure provisioning and application rollouts in a secure and a multi-tenant way let's get started so if we have a really packed agenda today we're going to start by talking about the pain points needs and requirements thereafter we're going to have a 10 000 feet overview of adobe's services landscape and we'll do a quick overview of the internet developer platform and then Dive Right In into the deployments using our good projects and infrastructure provisioning using cross plane and Argo thereafter manapu is going to walk us through the multi-tenancy and security requirements and how we solved some of these requirements uh you know with the existing tooling that we had and finally uh to wrap it up we're going to compare the developer experience with the previous and the new States and talk a little bit about the challenges and the unknowns okay let's get started so let's just quickly have a look at the previous state and the pain points associated with it so if you're a service developer you would be able to resonate with a lot of these and we have been talking to a lot of service developers you know as part of our you know Outreach to the to the clients and we realized that each of the teams are doing infrastructure provisioning in their own way they do need infrastructure provisioning but the platform does not help them they have custom tooling they
