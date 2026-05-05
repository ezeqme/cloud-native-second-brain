---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Deepthi Sigireddi", "Matt Lord", "Rohit Nayak", "PlanetScale"]
sched_url: https://kccncna2022.sched.com/event/182PH/vitess-introduction-and-new-features-deepthi-sigireddi-matt-lord-rohit-nayak-planetscale
youtube_search_url: https://www.youtube.com/results?search_query=Vitess%3A+Introduction+And+New+Features+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Vitess: Introduction And New Features - Deepthi Sigireddi, Matt Lord & Rohit Nayak, PlanetScale

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Deepthi Sigireddi, Matt Lord, Rohit Nayak, PlanetScale
- Schedule: https://kccncna2022.sched.com/event/182PH/vitess-introduction-and-new-features-deepthi-sigireddi-matt-lord-rohit-nayak-planetscale
- Busca YouTube: https://www.youtube.com/results?search_query=Vitess%3A+Introduction+And+New+Features+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Vitess: Introduction And New Features.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182PH/vitess-introduction-and-new-features-deepthi-sigireddi-matt-lord-rohit-nayak-planetscale
- YouTube search: https://www.youtube.com/results?search_query=Vitess%3A+Introduction+And+New+Features+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uRB-Qni_bCM
- YouTube title: Vitess: Introduction, New Features and the Vinted User Story
- Match score: 0.761
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/vitess-introduction-and-new-features/uRB-Qni_bCM.txt
- Transcript chars: 29795
- Keywords: queries, cluster, primary, actually, support, database, sharding, allows, running, clusters, version, started, schema, possible, shards, keyspace, replica, explain

### Resumo baseado na transcript

welcome everyone to the wit maintainer talk my name is deepti sigi and I'm uh the tech lead for vus and I'm a software engineer at Planet scale uh hello I'm kazimir Salis software relability engineer in Vitz databases team and we'll be presenting uh user story of VES invented and uh I'm Floren poar I'm a maintainer of the Vitz project and I'm also a software engineer at plan scal so today we're going to start by presenting to you what is vest we're going to give a brief users don't actually use foreign keys because at the scale at which people run vas it's simply not practical to use foreign key constraints uh there is a perceptible performance hit but there are uh smaller users of Wis who would like to keep the

### Excerpt da transcript

welcome everyone to the wit maintainer talk my name is deepti sigi and I'm uh the tech lead for vus and I'm a software engineer at Planet scale uh hello I'm kazimir Salis software relability engineer in Vitz databases team and we'll be presenting uh user story of VES invented and uh I'm Floren poar I'm a maintainer of the Vitz project and I'm also a software engineer at plan scal so today we're going to start by presenting to you what is vest we're going to give a brief overview of the project and then kazimieras will talk to you about the Vinted user story their adoption and how they're using Vitz and finally Dy we talk to you about the new and up and upcoming exciting features of vites and at the end we'll have some time for question and answers all right let's get started what is vitess so Vitz is a cloud name scat and distributed database it is built around my SQL in fact it started in 2010 at uh YouTube as a skating solution for my SQL later it was donated by YouTube to cncf in 2018 and then it became a graduate Project A year later in 2019 uh it is massively scalable because we have sharding in vest which allows you to partition your data across multiple primaries and then then it is highly available because we Whenever there is a failure on the primary we're going to we're going to detect it and repair it uh so vas is widely used in production by many many companies from small to extremely large and we have a few key adopters like slack who's running 100% on vest so every time you send a slack message it's going through vest we also have GitHub um they're running all of their issues and pro request on vitess and I think they have a little bit less than a million QPS on average we also have Vinted which kasimas will talk about soon but they do about 2.2 Millions QPS and finally we have Planet scale database Sav where they have approximately 10,000 different uh vs cluster running in production so of course we're uh an open source project we have about 15 maintainers working on the project and over the last year we had a little bit more than 250 contributors from which 115 were Cod contributors all of those came from 47 companies and the Cod contributors came from a little bit more than 20 companies so before I move into the move on to the more technical part of the talk we should introduce four key word for about vest so first one is a keyspace so a keyspace is basically the same as a myql logical database so you can have the user keyspace and inside
