---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Deepthi Sigireddi", "Manan Gupta", "PlanetScale"]
sched_url: https://kccncna2022.sched.com/event/182J8/one-vtorc-to-rule-them-all-high-availability-in-a-distributed-database-system-deepthi-sigireddi-manan-gupta-planetscale
youtube_search_url: https://www.youtube.com/results?search_query=One+VTOrc+To+Rule+Them+All+%E2%80%93+High+Availability+In+a+Distributed+Database+System+CNCF+KubeCon+2022
slides: []
status: parsed
---

# One VTOrc To Rule Them All – High Availability In a Distributed Database System - Deepthi Sigireddi & Manan Gupta, PlanetScale

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Deepthi Sigireddi, Manan Gupta, PlanetScale
- Schedule: https://kccncna2022.sched.com/event/182J8/one-vtorc-to-rule-them-all-high-availability-in-a-distributed-database-system-deepthi-sigireddi-manan-gupta-planetscale
- Busca YouTube: https://www.youtube.com/results?search_query=One+VTOrc+To+Rule+Them+All+%E2%80%93+High+Availability+In+a+Distributed+Database+System+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre One VTOrc To Rule Them All – High Availability In a Distributed Database System.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182J8/one-vtorc-to-rule-them-all-high-availability-in-a-distributed-database-system-deepthi-sigireddi-manan-gupta-planetscale
- YouTube search: https://www.youtube.com/results?search_query=One+VTOrc+To+Rule+Them+All+%E2%80%93+High+Availability+In+a+Distributed+Database+System+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=upmByX8uD6E
- YouTube title: One VTOrc To Rule Them All – High Availability In a Distributed Database System - Deepthi & Manan
- Match score: 0.997
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/one-vtorc-to-rule-them-all-high-availability-in-a-distributed-database/upmByX8uD6E.txt
- Transcript chars: 28281
- Keywords: primary, leader, tablets, tablet, durability, policy, replicas, failures, rights, accept, election, failure, enough, question, replica, semi-sync, actually, progress

### Resumo baseado na transcript

welcome everyone to this breakout session we are live in Detroit welcome also to our virtual audience our talk today is one VT org to rule them all high availability in a distributed system uh distributed database system and the distributed database we'll be talking about is with us my name is dipti sigredi I'm a maintainer and Technical lead for wittest which is a graduated cncf project and I'm a software engineer at Planet scale hello I am Anan I'm also a maintainer at offer desk and a software

### Excerpt da transcript

welcome everyone to this breakout session we are live in Detroit welcome also to our virtual audience our talk today is one VT org to rule them all high availability in a distributed system uh distributed database system and the distributed database we'll be talking about is with us my name is dipti sigredi I'm a maintainer and Technical lead for wittest which is a graduated cncf project and I'm a software engineer at Planet scale hello I am Anan I'm also a maintainer at offer desk and a software engineer at Planet scale we'll start with a witness overview s is a cloud native database but it originally started as a scaling solution for MySQL at YouTube and from those Beginnings in 2010 it has evolved to become a general purpose distributed database that is suitable for many workloads and many use cases wittus is massively scalable if we look at some of the numbers the largest instances of wittest run to 20 000 terabytes which is 20 petabytes 22 000 replicas 250 000 simultaneous connections though that is not a limit you could go higher and so on and one of the ways bitus achieves the massive scale is through sharding which we will not talk about in this talk but we have a maintainer talk tomorrow where you can learn more about how we test does sharding wittus is also highly available that is going to be the focus of this talk and witness is a MySQL compatible both 5.7 and 8.0 versions uh we'll now get a brief overview of the architecture of wittus so uh clients talk to with us through a proxy called vtgate and vtgate receives the client requests which can be either MySQL or grpc those are the two protocols it supports and routes them appropriately to the backend my sequels so in a sharded Witter system you may have multiple charts but in each Shard there is a primary MySQL and there are one or more replicas and vitigate figures out which shot to Route it to and when we run in this primary replica replicated mode we have to make sure that each Shard is highly available in addition to this query serving path through which vtgate receives the queries and routes them to the backend my sequels there is also a control plane and this is where VTR comes in there is a witness control Daemon which takes management commands from users through CLI or the web UI and executes them there is VT admin which Powers our web UI and then there's VT Arc so let's go through a little overview of VTR and then we will have a demo what is the problem that VTR is trying to solve the
