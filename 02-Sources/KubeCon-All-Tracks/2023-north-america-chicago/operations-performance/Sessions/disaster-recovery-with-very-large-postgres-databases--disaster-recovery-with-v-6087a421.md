---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Gabriele Bartolini", "EDB", "Michelle Au", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2ml/disaster-recovery-with-very-large-postgres-databases-gabriele-bartolini-edb-michelle-au-google
youtube_search_url: https://www.youtube.com/results?search_query=Disaster+Recovery+with+Very+Large+Postgres+Databases+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Disaster Recovery with Very Large Postgres Databases - Gabriele Bartolini, EDB & Michelle Au, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Gabriele Bartolini, EDB, Michelle Au, Google
- Schedule: https://kccncna2023.sched.com/event/1R2ml/disaster-recovery-with-very-large-postgres-databases-gabriele-bartolini-edb-michelle-au-google
- Busca YouTube: https://www.youtube.com/results?search_query=Disaster+Recovery+with+Very+Large+Postgres+Databases+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Disaster Recovery with Very Large Postgres Databases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ml/disaster-recovery-with-very-large-postgres-databases-gabriele-bartolini-edb-michelle-au-google
- YouTube search: https://www.youtube.com/results?search_query=Disaster+Recovery+with+Very+Large+Postgres+Databases+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WGQq4MWzW6E
- YouTube title: Disaster Recovery with Very Large Postgres Databases - Gabriele Bartolini, EDB & Michelle Au, Google
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/disaster-recovery-with-very-large-postgres-databases/WGQq4MWzW6E.txt
- Transcript chars: 30493
- Keywords: volume, backup, cluster, snapshots, recovery, snapshot, backups, object, storage, actually, operator, native, database, persistent, restore, disaster, basically, databases

### Resumo baseado na transcript

um just wanted to start out with a quick show of hands how many people here run postgress in production on kubernetes awesome how many people run very large postgress clusters in production very cool and and another show of hands how many people think uh kubernetes is possible to run very large uh great cool well hopefully uh by the end of this we can get more of those hands raised and a quick spoiler alert um we're going to show some ways to make it possible to actually

### Excerpt da transcript

um just wanted to start out with a quick show of hands how many people here run postgress in production on kubernetes awesome how many people run very large postgress clusters in production very cool and and another show of hands how many people think uh kubernetes is possible to run very large uh great cool well hopefully uh by the end of this we can get more of those hands raised and a quick spoiler alert um we're going to show some ways to make it possible to actually restore very large kubernetes uh postgress clusters 300 times faster than you can today all right so welcome everybody uh my name is Michelle I am a software engineer at Google um I have been a kubernetes maintainer since 2017 and I a six storage I'm joined here and yeah thanks Michelle I'm Gabrielle Gabriel bolini I'm VP of cloud native ATB ITB is a company that um contributes to the pgus open source project I've been using pogus for more than 20 years and uh now I'm also do da on kubernetes Ambassador and uh uh an open source contributor in the past I I created um I don't know if you're are familiar with Barman anyone does anyone know Barman for posg here okay so I created Barman in 2011 it's a backup and restore manager for pgus and now I'm also maintainer of cloud npg which is an operator for uh to run Posas incub NES thank you cool yeah so first start off with a background in postgress Technologies on on how postgress does backup and Recovery um we're going to talk about the new volume snapshot backup and Recovery feature with the cloud native PG operator um we're going to dive a little bit into details on the actual apis and how you use it um we're going to show a demo and then we will wrap that up afterwards yeah so in this first section I will go through um some important Concepts behind this recovery with pogus databases so Disaster Recovery is together with high availability one of the core components in it to achieve business continuity planning a business continuity solution always starts with defining the goal to achieve as an organization so once these goals are defined we can shape our infrastructure and our system accordingly but how do we Define these business continuity goals so over the past years two primary metrics have emerged the first one is RPO or recovery Point objective which is the amount of time that we uh amount of uh data that we can afford to lose uh after a failure and RPO is primarily a disaster recovery metric the second one is RTO or recovery time object
