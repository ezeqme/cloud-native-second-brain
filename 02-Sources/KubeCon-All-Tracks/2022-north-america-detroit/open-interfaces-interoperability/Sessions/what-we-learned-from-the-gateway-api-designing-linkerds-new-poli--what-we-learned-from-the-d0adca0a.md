---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Open Interfaces + Interoperability"
themes: ["Security", "Networking"]
speakers: ["Matei David", "Buoyant", "Inc"]
sched_url: https://kccncna2022.sched.com/event/182EU/what-we-learned-from-the-gateway-api-designing-linkerds-new-policy-crd-matei-david-buoyant-inc
youtube_search_url: https://www.youtube.com/results?search_query=What+We+Learned+From+the+Gateway+API%3A+Designing+Linkerd%E2%80%99s+New+Policy+CRD+CNCF+KubeCon+2022
slides: []
status: parsed
---

# What We Learned From the Gateway API: Designing Linkerd’s New Policy CRD - Matei David, Buoyant, Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[Security]], [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Matei David, Buoyant, Inc
- Schedule: https://kccncna2022.sched.com/event/182EU/what-we-learned-from-the-gateway-api-designing-linkerds-new-policy-crd-matei-david-buoyant-inc
- Busca YouTube: https://www.youtube.com/results?search_query=What+We+Learned+From+the+Gateway+API%3A+Designing+Linkerd%E2%80%99s+New+Policy+CRD+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre What We Learned From the Gateway API: Designing Linkerd’s New Policy CRD.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182EU/what-we-learned-from-the-gateway-api-designing-linkerds-new-policy-crd-matei-david-buoyant-inc
- YouTube search: https://www.youtube.com/results?search_query=What+We+Learned+From+the+Gateway+API%3A+Designing+Linkerd%E2%80%99s+New+Policy+CRD+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=okZq5yOB9Wc
- YouTube title: What We Learned From the Gateway API: Designing Linkerd’s New Policy CRD - Matei David, Buoyant, Inc
- Match score: 0.934
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/what-we-learned-from-the-gateway-api-designing-linkerds-new-policy-crd/okZq5yOB9Wc.txt
- Transcript chars: 22519
- Keywords: gateway, traffic, authorization, server, policy, mesh, linker, resources, allowed, ingress, routes, attach, identity, cluster, talking, resource, little, authorize

### Resumo baseado na transcript

uh hi everybody this is what we learned from the Gateway API designing linkerty's new policy crd it was so big I don't know where to look so this is a talk by my colleague mate David he was not able to make it unfortunately because of Visa issues so I'm giving this talk instead of him um so hopefully I do a good job with it so my name is Alex I'm a software engineer at buoyant we're the creators of linkerty I've been a Linker D maintainer since the Gateway API is for those who aren't familiar so the Gateway API is this set of kubernetes resources that are very useful for defining uh the behavior of gateways and one of the kind of key ideas here is that there are a bunch

### Excerpt da transcript

uh hi everybody this is what we learned from the Gateway API designing linkerty's new policy crd it was so big I don't know where to look so this is a talk by my colleague mate David he was not able to make it unfortunately because of Visa issues so I'm giving this talk instead of him um so hopefully I do a good job with it so my name is Alex I'm a software engineer at buoyant we're the creators of linkerty I've been a Linker D maintainer since the beginning of the project and it's something I'm really passionate about I think service meshes are very very cool and we have recently done a lot of really interesting stuff with the Gateway API that I want to talk about uh okay so show of hands who is familiar with linkerty here okay a lot of people great um what about who's familiar with the Gateway API uh still a good number but but fewer Okay cool so I I guess I don't have to spend too much time talking about linkready itself it's a service mesh it's a graduated project in the cncf it's used in production in many different places by many different people um and it's a very uh collaborative and active open source community uh so as a service mesh that means that there is a sidecar proxy uh in every pod that's part of the mesh that adds a lot of really interesting functionality like mtls uh between all your services uh reliability features like retries and timeouts and a lot of observability features like layer 7 metrics on success rate request rate and latency um and uh with a major focus on operational simplicity so the whole thing kind of works out of the box and and doesn't require you dedicating a lot of brain power to to making it work uh so the main focus is behind likerty are just that it's supposed to be very very lightweight both in terms of resource usage which means that it doesn't take up a lot of memory and it doesn't add a lot of latency uh but also lightweight uh conceptually in that it's a very simple model that you don't have to think too much about and you can operate it uh without getting bogged down in the details so being simple and secure right out of the box has been kind of a guiding principle for the project uh the control plane is written in this says go but it's actually now a combination of go and rust and the data plane is a custom built proxy uh written in Rust built to be ultralight okay so I'm going to give a little bit of background uh here about um how authorization Works in Linker d uh so this is a fairly new feature that wa
