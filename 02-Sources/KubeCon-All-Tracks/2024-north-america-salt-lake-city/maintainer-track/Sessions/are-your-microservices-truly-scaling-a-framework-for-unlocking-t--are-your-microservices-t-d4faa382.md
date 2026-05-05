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
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Matthew Penaroza", "PingCAP"]
sched_url: https://kccncna2024.sched.com/event/1hoyC/are-your-microservices-truly-scaling-a-framework-for-unlocking-the-stateful-backend-matthew-penaroza-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=Are+Your+Microservices+Truly+Scaling%3F+A+Framework+for+Unlocking+the+Stateful+Backend+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Are Your Microservices Truly Scaling? A Framework for Unlocking the Stateful Backend - Matthew Penaroza, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Matthew Penaroza, PingCAP
- Schedule: https://kccncna2024.sched.com/event/1hoyC/are-your-microservices-truly-scaling-a-framework-for-unlocking-the-stateful-backend-matthew-penaroza-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=Are+Your+Microservices+Truly+Scaling%3F+A+Framework+for+Unlocking+the+Stateful+Backend+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Are Your Microservices Truly Scaling? A Framework for Unlocking the Stateful Backend.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoyC/are-your-microservices-truly-scaling-a-framework-for-unlocking-the-stateful-backend-matthew-penaroza-pingcap
- YouTube search: https://www.youtube.com/results?search_query=Are+Your+Microservices+Truly+Scaling%3F+A+Framework+for+Unlocking+the+Stateful+Backend+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mm5lR0CqY8I
- YouTube title: Are Your Microservices Truly Scaling? A Framework for Unlocking the Stateful Backend - M. Penaroza
- Match score: 1.018
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/are-your-microservices-truly-scaling-a-framework-for-unlocking-the-sta/mm5lR0CqY8I.txt
- Transcript chars: 14435
- Keywords: databases, scalability, microservices, scaling, actually, application, number, systems, database, performance, throughput, latency, storage, challenges, having, single, linearly, looking

### Resumo baseado na transcript

hello everyone welcome to are your microservices truly scalable a framework for unlocking the stateful back end my name is Matthew penosa I a principal Solutions engineer at uh pinap and tidy B um a little bit about me I'm based in Austin Texas I was originally born in uh Eva Beach Hawaii and it's my job at tidb to solution uh technical challenges at scale for some of of our company's largest customers and a fun fact about me is I used to be a former streamer and competitive

### Excerpt da transcript

hello everyone welcome to are your microservices truly scalable a framework for unlocking the stateful back end my name is Matthew penosa I a principal Solutions engineer at uh pinap and tidy B um a little bit about me I'm based in Austin Texas I was originally born in uh Eva Beach Hawaii and it's my job at tidb to solution uh technical challenges at scale for some of of our company's largest customers and a fun fact about me is I used to be a former streamer and competitive DOTA two player all right so jumping right in um the key focus of this session is to discuss scaling stateful backends in microservices with a focus on the challenges that arise in Data Systems as you scale and why this matters is that application as applications scale backing components particularly data backing components often struggle to keep up affecting the uh agility and performance and data Integrity of the greater application so what you'll learn today is the impact of scaling on Data Systems challenges of maintaining data reliability as performance uh and performance as system grows and a framework for scaling your stateful layer uh to avoid pitfalls as you scale so everyone's probably very familiar with this architecture you know you have uh you have an API Gateway you have your microservices and Behind These microservices po potentially you can have it might have uh multiple databases per microservice or uh a few shared databases uh per microservices now if you want to scale out your stateless microservices it's fairly straightforward um sure there's some application developers be like no it's not so straightforward but relative to scaling the data side of things is actually is relatively straightforward you know you increase the the size of your instances uh your mic vert vertically scale your microservices you can horizontally scale your microservices and you don't have to worry too much about uh data Integrity but how do you scale your data layer so there's various options for this number one you can go with the old school option which is sharding you know dividing up uh uh the uh your database into small pieces into different in different instances and having them shared um then you you could take the nosql route which was the original uh solution to the the sharding problem um and that that potentially be a key Value Store a column family store a graph store document store or you can do primary secondary replication um or even uh going full regalia and doing a complete
