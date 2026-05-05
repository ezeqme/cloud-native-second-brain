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
themes: ["AI ML", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Matt Lord", "Deepthi Sigireddi", "PlanetScale"]
sched_url: https://kccncna2023.sched.com/event/1R2qj/scale-your-mysql-database-by-migrating-to-vitess-matt-lord-deepthi-sigireddi-planetscale
youtube_search_url: https://www.youtube.com/results?search_query=Scale+Your+MySQL+Database+by+Migrating+to+Vitess+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Scale Your MySQL Database by Migrating to Vitess - Matt Lord & Deepthi Sigireddi, PlanetScale

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Matt Lord, Deepthi Sigireddi, PlanetScale
- Schedule: https://kccncna2023.sched.com/event/1R2qj/scale-your-mysql-database-by-migrating-to-vitess-matt-lord-deepthi-sigireddi-planetscale
- Busca YouTube: https://www.youtube.com/results?search_query=Scale+Your+MySQL+Database+by+Migrating+to+Vitess+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Scale Your MySQL Database by Migrating to Vitess.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qj/scale-your-mysql-database-by-migrating-to-vitess-matt-lord-deepthi-sigireddi-planetscale
- YouTube search: https://www.youtube.com/results?search_query=Scale+Your+MySQL+Database+by+Migrating+to+Vitess+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vvDhlv3zxWM
- YouTube title: Scale Your MySQL Database by Migrating to Vitess - Matt Lord & Deepthi Sigireddi, PlanetScale
- Match score: 0.786
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/scale-your-mysql-database-by-migrating-to-vitess/vvDhlv3zxWM.txt
- Transcript chars: 31535
- Keywords: database, actually, tables, customer, replication, shards, instance, application, single, allows, support, primary, typically, cluster, running, changes, pretty, basically

### Resumo baseado na transcript

hello everyone uh welcome to this session where we will be doing our vtus maintainer talk and the talk is titled scaling my squl with vtus my name is dpti sigi I'm the technical lead and um a maintainer of vtus he everybody thanks for coming uh my name is Matt Lord I also work at Planet scale and uh I'm a vest maintainer been focusing on V replication which is one of the the things we'll be talking about today we'll start with an overview of witus and then

### Excerpt da transcript

hello everyone uh welcome to this session where we will be doing our vtus maintainer talk and the talk is titled scaling my squl with vtus my name is dpti sigi I'm the technical lead and um a maintainer of vtus he everybody thanks for coming uh my name is Matt Lord I also work at Planet scale and uh I'm a vest maintainer been focusing on V replication which is one of the the things we'll be talking about today we'll start with an overview of witus and then we will go on to the migration part of it and a demo so these maintainer talks are typically structured as an intro and a deep dive and the first part will be an intro some of you may have already heard of witus so you can feel free to let your attention wander in that case until we get to new features because we will be talking about what's new to start with what is witus witus is a cloud native database it's massively scalable and the way it achieves scalability is through sharding and there are really no uh theoretical limits to how big you your Wiest cluster can be or how uh much you can scale with it it is also highly available and it's compatible with my SQL both 5.7 and 8 AO so vtis was built as a scaling solution for my SQL and that is its origin story vus works with various data database Frameworks with ORS with Legacy code which uh talks directly to my SQL and with thirdparty applications what witus does is that it presents a logical database view of many physical MySQL instances to Applications and this logical database is what we call a key space and the physical databases are basically representing partitions of your data so if you have a large amount of data they are being the data is being split up into multiple shards and these terms keyspace and Shard are important because we'll come back to them and the way to think about A Shard is that every row in a table lives in ex exactly one Shard and if you combine all of your shards that is your entire set of data what witus is doing when you have an architecture like that is that queries are being routed to the correct correct physical database so as far as application is concerned it looks like a single monolithic MySQL instance but behind the scenes queries are going to be routed to the appropriate MySQL instance Wiest supports uh both grpc and MySQL clients basically it speaks the uh MySQL protocol and clients can have a single connection to aest Cluster which behind the scenes results in multiple connections to individual MySQL databases t
