---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Yan Wang", "VMware", "Vadim Bauer", "8gears Container Registry"]
sched_url: https://kccncna2023.sched.com/event/1R2sU/whats-new-in-harbor-and-how-can-you-make-harbor-even-better-yan-wang-vmware-vadim-bauer-8gears-container-registry
youtube_search_url: https://www.youtube.com/results?search_query=What%E2%80%99s+New+in+Harbor%2C+and+How+Can+You+Make+Harbor+Even+Better%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# What’s New in Harbor, and How Can You Make Harbor Even Better? - Yan Wang, VMware & Vadim Bauer, 8gears Container Registry

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Yan Wang, VMware, Vadim Bauer, 8gears Container Registry
- Schedule: https://kccncna2023.sched.com/event/1R2sU/whats-new-in-harbor-and-how-can-you-make-harbor-even-better-yan-wang-vmware-vadim-bauer-8gears-container-registry
- Busca YouTube: https://www.youtube.com/results?search_query=What%E2%80%99s+New+in+Harbor%2C+and+How+Can+You+Make+Harbor+Even+Better%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre What’s New in Harbor, and How Can You Make Harbor Even Better?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sU/whats-new-in-harbor-and-how-can-you-make-harbor-even-better-yan-wang-vmware-vadim-bauer-8gears-container-registry
- YouTube search: https://www.youtube.com/results?search_query=What%E2%80%99s+New+in+Harbor%2C+and+How+Can+You+Make+Harbor+Even+Better%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1QWy2zO0gBY
- YouTube title: What’s New in Harbor, and How Can You Make Harbor Even Better? - Yan Wang & Vadim Bauer
- Match score: 0.929
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/whats-new-in-harbor-and-how-can-you-make-harbor-even-better/1QWy2zO0gBY.txt
- Transcript chars: 22418
- Keywords: harbor, artifact, security, specify, registry, subject, scanner, select, features, artifacts, instance, course, scanning, garbage, nutation, images, vulnerability, distribution

### Resumo baseado na transcript

hello everybody thank you for joining our talk today about Harbor so if you're not interested in Harbor you're in the wrong session all right my name is Vin B I'm one of the co- maintainers of Harbor together with young M and today we're going to talk about haror and specifically we're going to talk about some haror superpowers that you maybe already know of maybe not and then Youngman is going to talk about some of the features that we developed in the last half year that already you cannot select it now because we have database enabled I can just let me quickly just delete all the users that's why it's a demo instance right and we can switch like the oidc provider for example and then we can of course set

### Excerpt da transcript

hello everybody thank you for joining our talk today about Harbor so if you're not interested in Harbor you're in the wrong session all right my name is Vin B I'm one of the co- maintainers of Harbor together with young M and today we're going to talk about haror and specifically we're going to talk about some haror superpowers that you maybe already know of maybe not and then Youngman is going to talk about some of the features that we developed in the last half year that already available and that you can use and you're going to dive a bit into details of those features and we going to give an Outlook about what to expect in from Harbor in the next release uh and then we'll close with ways how you can collaborate with us and also pick up some T-shirts here and okay so if you don't know it haror is a container registry right so it is existing since 2016 and it's uh graduated from The Graduate project in in the cncf it is a registry to you know store images and oci artifacts but more importantly it is a container image management solution so you really can manage the life cycle of your container images which makes you know hubber somewhat special compared to a simple storage solution where just storage images right so it has the policies role based Access Control vulnerability analytics and signing possibilities like notary and cosign um over the years Harbor has gained quite popularity and I'm confident to say that haror is probably today one of the most popular and widely used container registry specifically on Prem environment in the cloud is a bit different of course but on on Prem on self hosted Harbor is the defecto standard and Ian don't take my words for that because I'm obviously be but this is for example what the victor says about Harbor this is what he says about Harbor in one of his YouTube episodes so he knows what he what he talk about and as I said like har has a ton of features right so it has like Access Control artifact distribution security compliance but you know there like old features a bit difficult to to understand what it actually does so I'm going to focus a bit on the superpowers of Harbor and I picked up three of those today for you and one of the superpowers of Harbor is that it's remarkably well working for small teams like you know if you have a team of five five people three four people who needs uh who you know want to have a registry it works equally well for small teams as well as for large Enterprises right so for Enter
