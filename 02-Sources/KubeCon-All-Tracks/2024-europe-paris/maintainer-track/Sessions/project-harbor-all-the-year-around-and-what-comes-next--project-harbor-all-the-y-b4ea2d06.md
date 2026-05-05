---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Vadim Bauer", "8gears Container Registry", "Yan Wang", "Broadcom"]
sched_url: https://kccnceu2024.sched.com/event/1YhgU/project-harbor-all-the-year-around-and-what-comes-next-vadim-bauer-8gears-container-registry-yan-wang-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Project+Harbor%2C+All+the+Year+Around%2C+and+What+Comes+Next+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Project Harbor, All the Year Around, and What Comes Next - Vadim Bauer, 8gears Container Registry & Yan Wang, Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Vadim Bauer, 8gears Container Registry, Yan Wang, Broadcom
- Schedule: https://kccnceu2024.sched.com/event/1YhgU/project-harbor-all-the-year-around-and-what-comes-next-vadim-bauer-8gears-container-registry-yan-wang-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Harbor%2C+All+the+Year+Around%2C+and+What+Comes+Next+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Project Harbor, All the Year Around, and What Comes Next.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhgU/project-harbor-all-the-year-around-and-what-comes-next-vadim-bauer-8gears-container-registry-yan-wang-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Project+Harbor%2C+All+the+Year+Around%2C+and+What+Comes+Next+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JG9cQC-sQPo
- YouTube title: Project Harbor, All the Year Around, and What Comes Next - Vadim Bauer & Yan Wang
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/project-harbor-all-the-year-around-and-what-comes-next/JG9cQC-sQPo.txt
- Transcript chars: 22506
- Keywords: harbor, artifact, currently, support, scanning, scanner, working, security, artifacts, create, trying, information, signature, registry, replication, accessory, images, access

### Resumo baseado na transcript

all right everyone hello good afternoon and welcome to project haror maintenance track uh I'm here today with wangyang and myself Vin B we are two of the maintenance of project Harbor and we would like to tell you today what we have planned for our next release and what other the things we're currently thinkering with uh so let's get started right with a quick introduction what are we currently working on what is the Outlook and what uh is going to be part of the next release in

### Excerpt da transcript

all right everyone hello good afternoon and welcome to project haror maintenance track uh I'm here today with wangyang and myself Vin B we are two of the maintenance of project Harbor and we would like to tell you today what we have planned for our next release and what other the things we're currently thinkering with uh so let's get started right with a quick introduction what are we currently working on what is the Outlook and what uh is going to be part of the next release in a couple of days or weeks and let's get started so if you're new to Harbor um Harbor is a cncf graduated project that is basically a container Registries with a few superpowers so it's not just about storing your images but really going the next level and managing your images with policies role based Access Control etc etc right so since um January Harbor turned eight and we're still growing and I can proudly say that Harbor is one of the most popular container Registries out there if you want to do something more and just store images and this is also some kind of reflected in the stars um some of the key features of Harbor you can do access control you can do artifact distribution you can do security and compliance policies maintainability this is like all bit of a buzzwords here so I think more interesting is it is look from a user perspective so what do you get as a user or in a different roles right so it's the good thing about hover is it works for small teams equally is for large teams so you can really start small with a few people and then you can add role based access control your IDP and you can grow uh with your yeah with your organization and in a more yeah mature project or mature setup over terabytes of of size uh for czu it's quite interesting because you can have a registry where you have all your images in one place so you can replication use replication where you can replicate images from different locations all to the central place you have vulnerability dashboards you have a vulnerability overview you have ai Trails so all the things that make ceso happy are included into Harbor so that's why it makes Caesar happy and my favorite is the Ops people's darling is because you can automate a lot of things you can Implement kops workflows you can use terraform to manage Harbor or plumi and you have like quotas so that it's not doesn't make AWS and Azure happy uh you have policies you have garbage collection and all the things that makes your operation of haror quite
