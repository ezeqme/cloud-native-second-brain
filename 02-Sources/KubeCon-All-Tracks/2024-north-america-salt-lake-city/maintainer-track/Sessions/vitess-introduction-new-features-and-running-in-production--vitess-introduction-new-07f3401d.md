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
speakers: ["Deepthi Sigireddi", "PlanetScale", "Derek Perkins", "Nozzle", "Sudhi Vijayakumar", "Backblaze"]
sched_url: https://kccncna2024.sched.com/event/1hoxf/vitess-introduction-new-features-and-running-in-production-deepthi-sigireddi-planetscale-derek-perkins-nozzle-sudhi-vijayakumar-backblaze
youtube_search_url: https://www.youtube.com/results?search_query=Vitess%3A+Introduction%2C+New+Features+and+Running+in+Production+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Vitess: Introduction, New Features and Running in Production - Deepthi Sigireddi, PlanetScale; Derek Perkins, Nozzle; Sudhi Vijayakumar, Backblaze

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Deepthi Sigireddi, PlanetScale, Derek Perkins, Nozzle, Sudhi Vijayakumar, Backblaze
- Schedule: https://kccncna2024.sched.com/event/1hoxf/vitess-introduction-new-features-and-running-in-production-deepthi-sigireddi-planetscale-derek-perkins-nozzle-sudhi-vijayakumar-backblaze
- Busca YouTube: https://www.youtube.com/results?search_query=Vitess%3A+Introduction%2C+New+Features+and+Running+in+Production+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Vitess: Introduction, New Features and Running in Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxf/vitess-introduction-new-features-and-running-in-production-deepthi-sigireddi-planetscale-derek-perkins-nozzle-sudhi-vijayakumar-backblaze
- YouTube search: https://www.youtube.com/results?search_query=Vitess%3A+Introduction%2C+New+Features+and+Running+in+Production+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MZXToqM8mds
- YouTube title: Vitess: Introduction, New Features & Running in Production- D. Sigireddi, D. Perkins, S. Vijayakumar
- Match score: 0.81
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/vitess-introduction-new-features-and-running-in-production/MZXToqM8mds.txt
- Transcript chars: 28185
- Keywords: database, feature, schema, features, online, replication, improvements, running, production, primary, simple, topology, actually, adding, replica, everything, regular, always

### Resumo baseado na transcript

welcome to the vtest maintainer talk my name is dpti sigi I'm the technical lead for the vus open source project and I'm the vus engineering lead at Planet scale I'm Derek Perkins CEO of nozzle and my name is sui and I'm from back place today we'll start with a witus overview that Derek will give us and then sui will talk about production deployment of witus at back plays then I'll come back to talk about new and upcoming features in Vitus and then we'll do a Q&A

### Excerpt da transcript

welcome to the vtest maintainer talk my name is dpti sigi I'm the technical lead for the vus open source project and I'm the vus engineering lead at Planet scale I'm Derek Perkins CEO of nozzle and my name is sui and I'm from back place today we'll start with a witus overview that Derek will give us and then sui will talk about production deployment of witus at back plays then I'll come back to talk about new and upcoming features in Vitus and then we'll do a Q&A if there are any questions at that point so v test why would you choose to run vest obviously sharding is the number one feature that people think think about when they think about the tests and let's talk about what are the problems you're facing with your existing MySQL setup that might make you think oh sharding the test might be a solution first backup restore times for your Disaster Recovery uh the bigger your disc the longer physics requires for you to move that data around uh and do the whole backup process right contention uh is important to deal with deadlocks is a related uh problem that you'll be facing sping as you have more and more writers uh the despite how many CPUs you scale it to you're going to be limited by uh table contention uh iops especially if you're on the cloud uh you're going to be limited with the number of iops writing to your discs and one of the first things that you're going to do to offload some of your uh load is to start adding read replicas which brings up a couple of issues uh depend the more you're writing the harder it is for replication to keep up my sql's made some strides recently to enable some better parallel writing um but it's still generally is a lot slower than uh writing to your primary and then eventual consistency for me this is one of the biggest concerns that I see database wise around is because once you start moving to a read replica now every single app developer that you have has to understand eventual consistency and distributed systems are difficult and so but again if you're trying to scale that single node MySQL read replicas is kind of the only thing you can do and then finally you're going to eventually hit uh Max instant size and so it's not going to scale forever and the way that vess helped you with each of these uh fix dis sizes uh vest we recommend that you do about 250 GB per Shard not because that's a magic number but that kind of gets you into a 15minute restore window uh for Disaster Recovery just having multiple discs helps
