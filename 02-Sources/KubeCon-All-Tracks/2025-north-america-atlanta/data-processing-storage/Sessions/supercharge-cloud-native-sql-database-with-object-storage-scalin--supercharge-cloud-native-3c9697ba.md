---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Jinpeng Zhang", "PingCAP"]
sched_url: https://kccncna2025.sched.com/event/27FeM/supercharge-cloud-native-sql-database-with-object-storage-scaling-tikv-with-s3-as-the-backbone-jinpeng-zhang-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=Supercharge+Cloud+Native+SQL+Database+With+Object+Storage%3A+Scaling+TiKV+With+S3+as+the+Backbone+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Supercharge Cloud Native SQL Database With Object Storage: Scaling TiKV With S3 as the Backbone - Jinpeng Zhang, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Jinpeng Zhang, PingCAP
- Schedule: https://kccncna2025.sched.com/event/27FeM/supercharge-cloud-native-sql-database-with-object-storage-scaling-tikv-with-s3-as-the-backbone-jinpeng-zhang-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=Supercharge+Cloud+Native+SQL+Database+With+Object+Storage%3A+Scaling+TiKV+With+S3+as+the+Backbone+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Supercharge Cloud Native SQL Database With Object Storage: Scaling TiKV With S3 as the Backbone.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FeM/supercharge-cloud-native-sql-database-with-object-storage-scaling-tikv-with-s3-as-the-backbone-jinpeng-zhang-pingcap
- YouTube search: https://www.youtube.com/results?search_query=Supercharge+Cloud+Native+SQL+Database+With+Object+Storage%3A+Scaling+TiKV+With+S3+as+the+Backbone+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jDlAdMEMZgs
- YouTube title: Supercharge Cloud Native SQL Database With Object Storage: Scaling TiKV With S3 as... Jinpeng Zhang
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/supercharge-cloud-native-sql-database-with-object-storage-scaling-tikv/jDlAdMEMZgs.txt
- Transcript chars: 19428
- Keywords: storage, object, latency, language, database, second, architecture, online, remote, background, natural, number, cost, perspective, introduce, engine, platform, databases

### Resumo baseado na transcript

Okay, let's start our sharing and welcome everybody to come to my sharing and um before I start this sharing I want to do a uh quick survey. And uh today's topic is um scaling tiqe with S3 at the backbone supercharge cloud native SQL database with object storage. is uh around 80 80% uh accuracy for the text to seco and uh so right now recently there is Another trying to to uh overcome this uh this this challenge is how about let the AI agent to generate multiple different seals and this So this is introduced a little bit like uh I I call it volatility and sometimes uh the generated SE query is not optimal and the second uh challenge we can see is the AI agent are generating vast volume of data at unprecedented speed. it's uh grows at a at a at a I believe it's a high number and how we you know can store such large amount of volume of data cost effectively in terms of like uh economic um to uh like your business value must be like higher or or way larger than the cost you uh you spend on store or keeping this datas and most of you have most used like chat GBT and uh I I use it daily and sometimes you can uh I use chat

### Excerpt da transcript

Okay, let's start our sharing and welcome everybody to come to my sharing and um before I start this sharing I want to do a uh quick survey. Have you heard Thai que before? Raise your hand. Okay. Yes. Have you heard Thai DB before? Okay, great. Um have you attended last year's my talk? raise your hand. Oh, old friend. Okay, great. Yeah. And uh today's topic is um scaling tiqe with S3 at the backbone supercharge cloud native SQL database with object storage. Yeah. And this is a little bit about me uh Jimong and I'm working for TADB right now and I'm the um maintainer of Tai Kiwi contributor of Rox DB and um have a few years of um experience with search engine natural language processing and recommendation system. But for the past nearly 11 years I was uh working in uh scalable data platform and the database area and uh for the past nine year and five months literally I uh build taq and tidb from scratch with other engineers and this is my github and my uh tech blog. Yeah. Uh today's sharing will cover three major topics.

The first topic is about the new challenges for databases in the age of AI. I know uh AI is a very hot topic right now. Uh and the second topic is about object storage is becoming the def facto of uh distributed file system on the cloud. And the third topic is about how we leverage object storage in our system. Okay, let's come to the first part is new challenges for databases in the age of AI. Um right now after the large language model and uh I can imagine that everything between I mean the interface between human and the and uh the computer is becoming the uh natural language and from the database area or data platform area there is a uh there is a um domain that is taxed to SEO because SEO is uh interface for like a data scientist and a data engineers to um send requests or send instructions to data platform or database and right now the uh because of the large language model and the natural language instructions or natural language become the new interface between human and the computer.

So when we come to uh the database or data platform area uh the because the natural language is a you know is a language that is ambiguous and uh it's not like a computer language or or SQL it's un ambigu un ambiguous. So when people send some uh natural language instructions to to the AI agent or to uh to your uh systems and the AI agent need to you know uh to know what you want to do with the data and because of the natural language is ambiguous. S
