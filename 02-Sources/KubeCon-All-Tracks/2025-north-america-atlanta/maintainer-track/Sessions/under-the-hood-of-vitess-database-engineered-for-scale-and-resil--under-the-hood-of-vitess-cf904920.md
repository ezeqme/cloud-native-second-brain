---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Matt Lord", "Florent Poinsard", "PlanetScale"]
sched_url: https://kccncna2025.sched.com/event/27No9/under-the-hood-of-vitess-database-engineered-for-scale-and-resilience-matt-lord-florent-poinsard-planetscale
youtube_search_url: https://www.youtube.com/results?search_query=Under+the+Hood+of+Vitess%3A+Database+Engineered+for+Scale+and+Resilience+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Under the Hood of Vitess: Database Engineered for Scale and Resilience - Matt Lord & Florent Poinsard, PlanetScale

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Matt Lord, Florent Poinsard, PlanetScale
- Schedule: https://kccncna2025.sched.com/event/27No9/under-the-hood-of-vitess-database-engineered-for-scale-and-resilience-matt-lord-florent-poinsard-planetscale
- Busca YouTube: https://www.youtube.com/results?search_query=Under+the+Hood+of+Vitess%3A+Database+Engineered+for+Scale+and+Resilience+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Under the Hood of Vitess: Database Engineered for Scale and Resilience.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27No9/under-the-hood-of-vitess-database-engineered-for-scale-and-resilience-matt-lord-florent-poinsard-planetscale
- YouTube search: https://www.youtube.com/results?search_query=Under+the+Hood+of+Vitess%3A+Database+Engineered+for+Scale+and+Resilience+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2B0FB0A_c_Q
- YouTube title: Under the Hood of Vitess: Database Engineered for Scale and Resilien... Matt Lord & Florent Poinsard
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/under-the-hood-of-vitess-database-engineered-for-scale-and-resilience/2B0FB0A_c_Q.txt
- Transcript chars: 26552
- Keywords: shards, database, primary, queries, cluster, basically, pretty, cost, components, requests, across, failures, availability, everything, define, million, talked, little

### Resumo baseado na transcript

I'm a maintainer of the Vitz project and I'm a software engineer at Planet Scale and I'm with Matt who is also a maintainer of Vitz and also a software engineer at Planet Scale. Today we're going to give you a brief overview of what is Vitz for those of you who don't know what it is yet. So you never have to execute that query all the time which will take time. Um that also include point in time restore and for instance we yeah we have like a Kubernetes operator which is called the Vest operator and in that operator you can define a schedule. Instead of sending that query like those 1 million squares to the database, we're just going to send the query once and then return the result to the million requests that we got. It's going to see the sh the primary is no longer here and then it's going to see okay which replica is available which one has the least lag replication lag and then finally it's going to elect it as a primary and we have vtccll which is basically a demon running all the time.

### Excerpt da transcript

Hello, good afternoon. Welcome uh welcome to this talk in the afternoon after lunch. Um my name is Florent. I'm a maintainer of the Vitz project and I'm a software engineer at Planet Scale and I'm with Matt who is also a maintainer of Vitz and also a software engineer at Planet Scale. Today we're going to give you a brief overview of what is Vitz for those of you who don't know what it is yet. and then Matt is going to talk to you about resilience in Vest. So let's start. What is VES? First of all, it's obviously a cloud native project. We graduated I think in 2019. It was donated to CNCF by YouTube back then and it is basically a massively scalable database. It is also extremely it has like a very good high availability and it is compatible with my SQL 80 myQL 8.4. So you'll have basically two sides of V test. You'll have the operation side. So as an operator you can very easily scale your database. You can manage it really easily and you usually don't need that big of a team to manage your database.

Even though your database can be very big on the other side on the user side, it will feel like ex it will feel exactly like a normal MySQL even though you have a lot of abstractions, you have a lot of new components. So you'll be able to use the same OMS, the same applications, it will be the MySQL protocol, you'll have the same type of connection strings, everything. Um, like I say, we support the MySQL protocol. We also support the gRPC protocol if your application application wants to talk in gRPC. Some of the core features that we have in vit are highlighted on that screen and the first one my school compatibility it's we basically ensure that any queries you can run on my SQL you can also run it on vit even though you may have thousands of different shards. And then the other features are what differentiate us from just vanilla my SQL I will say. So in vit you can shard and reshard as much as you want. You can go from zero shard to two shards and then four etc etc. We [snorts] support materialization workflows.

So let's say you have I don't know hundred of 100 shards and you have one queries that have to scatter on all of those shards and it's a heavy one and it just returns let's say like one number one column. You may want to have a materialization workflow which will basically keep that column updated in real time. So you never have to execute that query all the time which will take time. you can just return the value that is stored in that materia
