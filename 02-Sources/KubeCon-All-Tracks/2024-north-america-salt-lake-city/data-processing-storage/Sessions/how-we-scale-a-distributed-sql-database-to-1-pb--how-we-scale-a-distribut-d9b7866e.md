---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Jinpeng Zhang", "PingCAP"]
sched_url: https://kccncna2024.sched.com/event/1i7pi/how-we-scale-a-distributed-sql-database-to-1-pb-jinpeng-zhang-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Scale+a+Distributed+SQL+Database+to+1+PB+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How We Scale a Distributed SQL Database to 1 PB - Jinpeng Zhang, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Jinpeng Zhang, PingCAP
- Schedule: https://kccncna2024.sched.com/event/1i7pi/how-we-scale-a-distributed-sql-database-to-1-pb-jinpeng-zhang-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Scale+a+Distributed+SQL+Database+to+1+PB+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How We Scale a Distributed SQL Database to 1 PB.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pi/how-we-scale-a-distributed-sql-database-to-1-pb-jinpeng-zhang-pingcap
- YouTube search: https://www.youtube.com/results?search_query=How+We+Scale+a+Distributed+SQL+Database+to+1+PB+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=c9eAU5DKR5c
- YouTube title: How We Scale a Distributed SQL Database to 1 PB - Jinpeng Zhang, PingCAP
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-we-scale-a-distributed-sql-database-to-1-pb/c9eAU5DKR5c.txt
- Transcript chars: 21997
- Keywords: database, single, multiple, backup, resource, around, application, distributed, applications, storage, metadata, center, question, perspective, change, result, scalable, latency

### Resumo baseado na transcript

okay hello hello everyone how you doing great yeah yeah yeah yeah okay uh today I'm going to uh give the talk how we scale a distributed Cal database to PB level yeah uh a little bit about myself um I'm working for tidb and uh I'm the I'm Mainer of Tai K and also Rock be contributor I used to wrote a book about DB internal and for the past decade I build Tai kwi and tidb from the scratch with other colleagues and this is my GitHub and

### Excerpt da transcript

okay hello hello everyone how you doing great yeah yeah yeah yeah okay uh today I'm going to uh give the talk how we scale a distributed Cal database to PB level yeah uh a little bit about myself um I'm working for tidb and uh I'm the I'm Mainer of Tai K and also Rock be contributor I used to wrote a book about DB internal and for the past decade I build Tai kwi and tidb from the scratch with other colleagues and this is my GitHub and the technical block yeah this is today's uh agenda we uh mainly have uh four sections the first one I'd like to uh briefly introduce the importance of database capability for your business growth and the second section I'm going to uh introduce a little bit about our product TB and its adoptions and the third part is uh focus on the challenges we have faced during uh the past decade we are build uh when we were building this product and uh when we uh support our customers and the last section is about uh QA if you have any question yeah we can and you know have competition so let's move to the first step first part um business growth is a great thing uh for companies yeah we have more users more tenance and we deliver new features for our customers for our new fe uh new users and existing users and uh definitely there are more datas collect from your uh users and from the technical perspective there might some like challenges because uh for your application server or for your backend database there are more connections there more it means more request more datas and U yeah more data need to maintain so uh let me give an uh real example to uh to show this more specific B is a fast growing Mobility company from the Europe and uh they have around 100 million users yeah it's a great great number and they provide service in uh more than 500 cities and uh since pandemic their business has 400% growth yeah this is a great thing for them but from the uh technical perspective they also um faced the you know some CH challenges in total they have hundreds of uh terabytes to uh PB level dat volume and uh every day they will have 100 service deployment and uh they need to uh do 100 you know more than 100 database change I mean the schema change or our dat migration every week and uh every month there are more than like uh around 5 to 10 terab new data generated and they use my sqle so um you can imagine definitely they hit the you know single my instance size limitation and for some large tables if they want to add some index it will take
