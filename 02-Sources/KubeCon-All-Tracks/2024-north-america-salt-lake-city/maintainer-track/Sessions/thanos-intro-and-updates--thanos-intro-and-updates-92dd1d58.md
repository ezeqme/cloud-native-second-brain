---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Ben Ye", "Amazon Web Services"]
sched_url: https://kccncna2024.sched.com/event/1hoxi/thanos-intro-and-updates-ben-ye-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Thanos%3A+Intro+and+Updates+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Thanos: Intro and Updates - Ben Ye, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Ben Ye, Amazon Web Services
- Schedule: https://kccncna2024.sched.com/event/1hoxi/thanos-intro-and-updates-ben-ye-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Thanos%3A+Intro+and+Updates+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Thanos: Intro and Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxi/thanos-intro-and-updates-ben-ye-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Thanos%3A+Intro+and+Updates+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SR2sG4wno-s
- YouTube title: Thanos: Intro and Updates - Ben Ye, Amazon Web Services
- Match score: 0.72
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/thanos-intro-and-updates/SR2sG4wno-s.txt
- Transcript chars: 28920
- Keywords: premisus, compactor, basically, called, compaction, usually, receiver, component, server, storage, support, blocks, sample, single, remote, backlog, router, duplication

### Resumo baseado na transcript

yeah uh I think we are at time so first of all thanks everyone for joining the session and today uh we will have uh intro level uh session for the tunnel project I will also uh cover the project updates part briefly and for this talk I also want to talk talk about some common pitfalls uh as a maintainer I see Tel users having and I hope this can be some uh key takeaways for you if if you are using tunnels or you plan to use tunnels

### Excerpt da transcript

yeah uh I think we are at time so first of all thanks everyone for joining the session and today uh we will have uh intro level uh session for the tunnel project I will also uh cover the project updates part briefly and for this talk I also want to talk talk about some common pitfalls uh as a maintainer I see Tel users having and I hope this can be some uh key takeaways for you if if you are using tunnels or you plan to use tunnels so uh first of all a bit introduction about myself so uh I'm Ben and I'm a software engineer at AWS and I'm um a maintainer for both tunel and cortex project and you can find me on GitHub and I also have a p so let's start with the introduction um if you want to talk about SOS first we need to talk about premisus but since um people attend this talk I assume everyone probably already have some kind of background for SOS so I will sorry for for premisus so I will not dive too deep uh but the key thing to know here is that uh premisus is known to be designed to work as a single application in a single machine and it uses pool model to square Matrix it also have some uh cool feature like tsdb prom car engine and alerting feature Etc next uh I want to uh walk you through a user Journey who is using uh premisus and how he can gradually adopt the whole uh tunnel stack so first of all maybe everyone starts with premisus as a single uh server so you scrap some metrics from your exporter or application and you set up your uh visualization layer for example grafana and you can see your nice dashboard and graphs however you start to see some problems when there's a deployment going on for your premis server um if you if you only use a single premis server it during the deployment it will take down your premis server and it will take a few minutes to wait for it to get back and then you will have a few minutes of down time and you can see some gaps in your grafana dashboard so a common way to solve this is to uh set up premisus ha Pairs and basically it's you will deploy two preus parts and they both scrape the same data so even uh in this case even you have a single prisia going down you still have kind of the same snapshot in another prisia server because they are collecting the same data but this solution is not perfect and the problem sometimes uh can come from your data visual visualization layer site um because grafana usually you will just use a single data source s for premisus so you usually put a load balancer in front of your two
