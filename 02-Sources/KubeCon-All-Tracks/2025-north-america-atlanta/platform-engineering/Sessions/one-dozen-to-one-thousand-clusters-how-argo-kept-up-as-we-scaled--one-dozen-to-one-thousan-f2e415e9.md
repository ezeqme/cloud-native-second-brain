---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Jérémy Albuixech", "Kahou Lei", "Okta"]
sched_url: https://kccncna2025.sched.com/event/27FcE/one-dozen-to-one-thousand-clusters-how-argo-kept-up-as-we-scaled-jeremy-albuixech-kahou-lei-okta
youtube_search_url: https://www.youtube.com/results?search_query=One+Dozen+To+One+Thousand+Clusters%3A+How+Argo+Kept+up+as+We+Scaled+CNCF+KubeCon+2025
slides: []
status: parsed
---

# One Dozen To One Thousand Clusters: How Argo Kept up as We Scaled - Jérémy Albuixech & Kahou Lei, Okta

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Jérémy Albuixech, Kahou Lei, Okta
- Schedule: https://kccncna2025.sched.com/event/27FcE/one-dozen-to-one-thousand-clusters-how-argo-kept-up-as-we-scaled-jeremy-albuixech-kahou-lei-okta
- Busca YouTube: https://www.youtube.com/results?search_query=One+Dozen+To+One+Thousand+Clusters%3A+How+Argo+Kept+up+as+We+Scaled+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre One Dozen To One Thousand Clusters: How Argo Kept up as We Scaled.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcE/one-dozen-to-one-thousand-clusters-how-argo-kept-up-as-we-scaled-jeremy-albuixech-kahou-lei-okta
- YouTube search: https://www.youtube.com/results?search_query=One+Dozen+To+One+Thousand+Clusters%3A+How+Argo+Kept+up+as+We+Scaled+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4yVSqDJm5RI
- YouTube title: One Dozen To One Thousand Clusters: How Argo Kept up as We Scaled - Jérémy Albuixech & Kahou Lei
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/one-dozen-to-one-thousand-clusters-how-argo-kept-up-as-we-scaled/4yVSqDJm5RI.txt
- Transcript chars: 28369
- Keywords: workflow, argo, control, deployment, application, customer, platform, basically, always, release, plug-in, change, upgrade, resources, customized, version, cluster, config

### Resumo baseado na transcript

Uh, my name is Kahal and I'm a principal software engineer in OCO platform at Octa. >> Hi, I am Jeremy and I'm a staff engineer with the Ozero platform at Octa. After a few months of research and proof of concept, we ended up on this design. So right now we have around 1,000 to 2,000 Argo CD application and among all of them we have two to three million resources Kubernetes resources that we to manage and we have like around 32 Ago CD application controller port and then 24 rile So for those who doesn't know what this feature is basically is a very powerful features such that like we ensure that like um the application in the Kubernetes cluster always mirror um what we have in our uh gig repo. So our release candidate is basically a bundle of our software stack which include all of our microser image version all the um terraform code uh kubernetes manifest terraform homegrown terform plug in and homegrown custom plug in and we bundle everything and call as a release manifest.

### Excerpt da transcript

Hey, good afternoon. Uh, my name is Kahal and I'm a principal software engineer in OCO platform at Octa. >> Hi, I am Jeremy and I'm a staff engineer with the Ozero platform at Octa. And today we will go over our usage of Argo CD and Argo workflow within our platform. Uh, first we will go through our platform history and our design. Then we will do a deep dive on Argo CD. Then Argo workflows and then we'll have a few minutes left for Q&A. So first we will go over the platform history and how we got to our current design. Uh in its first iteration the platform was mainly a way to host Ozero services for customers who wanted their infra and configuration stored in a private cloud account. It was targeted uh for a very small subset of customers and as a result uh was not built with high scale and automation as priorities. It had a snowflake config and infra. Uh the updates were done manually by an operator. Access was not as secure as it could be and it was using early days cloud infra. So basically code running in VMs.

With our private cloud solution becoming more successful and requested, we had to quickly iterate on a new platform that could cover the increasing demand. After a few months of research and proof of concept, we ended up on this design. So it leverages a lot of cloud native technologies with a highlight on Argo project with Argo CD used for the service provisioning. Argo workflows for the deploy for the deployments. uh Terraform with a provider that we maintain for all the infrared code and these are all orchestrated by control plane services that uh so with all of these we can manage all the customer environments. So uh thanks Jeremy to introduce our uh controlling platform. So as you can see right from the previous slides like um we use a lot of argo component to drive our deployment pipeline and they are the core component. So the next question is like we ask like why we want to use argo. So and it comes with a lot of reason. So the first reason is that like they very easy to install in use. Whenever we have a PC, we just like install them locally so that we can iterate, we can iterate the PC much faster also like a CD provides a very flex flexible customized integration.

So if even allow us to like um control our different uh customized plug-in version onto different um customer development environment. So also AGO workflow is a very flexible. So basically you can plug and pay different AGO workflow step and come up with different um um d
