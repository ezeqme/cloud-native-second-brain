---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Jennifer Strejevitch", "VMware", "Alois Reitbauer", "Dynatrace"]
sched_url: https://kccncna2021.sched.com/event/lV7r/introduction-and-deep-dive-into-tag-delivery-jennifer-strejevitch-vmware-alois-reitbauer-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Introduction+and+Deep-Dive+into+TAG+Delivery+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Introduction and Deep-Dive into TAG Delivery - Jennifer Strejevitch, VMware & Alois Reitbauer, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Jennifer Strejevitch, VMware, Alois Reitbauer, Dynatrace
- Schedule: https://kccncna2021.sched.com/event/lV7r/introduction-and-deep-dive-into-tag-delivery-jennifer-strejevitch-vmware-alois-reitbauer-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Introduction+and+Deep-Dive+into+TAG+Delivery+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Introduction and Deep-Dive into TAG Delivery.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7r/introduction-and-deep-dive-into-tag-delivery-jennifer-strejevitch-vmware-alois-reitbauer-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Introduction+and+Deep-Dive+into+TAG+Delivery+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JlFuKnhzVCs
- YouTube title: Introduction and Deep - Dive into TAG App Delivery - Hongchao Deng & Thomas Schuetz
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/introduction-and-deep-dive-into-tag-delivery/JlFuKnhzVCs.txt
- Transcript chars: 21187
- Keywords: delivery, working, application, projects, infrastructure, engineering, native, provide, solutions, workflow, incubation, software, please, thomas, trying, covers, patterns, operators

### Resumo baseado na transcript

welcome everyone in this talk we will give an introduction and deep dive into the app delivery tag we'll talk about who we are what we do and what progress have we made this year before we start talking about anything i would like to introduce the speakers a little bit i'm hong chao from alibaba and serve as the co-chair of app delivery tech my co-speaker thomas from diner chase served as the ted lee of app delivery tech we also have leaders from working groups of cooperative delivery

### Excerpt da transcript

welcome everyone in this talk we will give an introduction and deep dive into the app delivery tag we'll talk about who we are what we do and what progress have we made this year before we start talking about anything i would like to introduce the speakers a little bit i'm hong chao from alibaba and serve as the co-chair of app delivery tech my co-speaker thomas from diner chase served as the ted lee of app delivery tech we also have leaders from working groups of cooperative delivery chaos engineering and githubs so what does our tech do we basically held the cncf tlc managers projects under the domain of app delivery decides what projects go into incubation and graduation and analyze their maturity level we also write down materials about best practice and publish white papers about app delivery domain so what's included in app delivery domain the first thing is application definition we need to define what an application means for cloud native platforms how we can make obstructions on top of infrastructure and expose application centric apis like how to make sure that the api matches the majority of our user needs and more importantly how to extend it with more apis we have seen open source projects like coupe vela argo cd and flux cd are trying to provide such application abstractions and solve problems in this domain app delivery also covers how to design and develop applications we provide best practice guides on how an application architecture should do and will fit the cloud native patterns modern applications designed with such patterns would benefit from the community and the cloud better for example dapper has empowered modern applications talk to back-end services easily that includes open source components like mysql kafka redis and many other cloud services app delivery also covers application bundling and package management today we already have two top-level cncf projects ham and buildpack to provide solutions to application packaging but they have their own pitfalls and scenarios they don't fit for example in ham it couldn't provide me the needs to divide delivery workflow as new technologies keep coming up we believe there will be new solutions that can address previous problems and being compatible with existing software packages formats app delivery also covers the topics of delivery workflow kubernetes resource model is decorative but the delivery model is but the delivery workflow model is process dual and how to describe delivery wor
