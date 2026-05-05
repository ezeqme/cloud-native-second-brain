---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Cyril Corbon", "Alex Triquet", "Dailymotion"]
sched_url: https://kccnceu2023.sched.com/event/1Hyab/building-apache-druid-on-kubernetes-how-dailymotion-serves-partner-data-cyril-corbon-alex-triquet-dailymotion
youtube_search_url: https://www.youtube.com/results?search_query=Building+Apache+Druid+on+Kubernetes%3A+How+Dailymotion+Serves+Partner+Data+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building Apache Druid on Kubernetes: How Dailymotion Serves Partner Data - Cyril Corbon & Alex Triquet, Dailymotion

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Cyril Corbon, Alex Triquet, Dailymotion
- Schedule: https://kccnceu2023.sched.com/event/1Hyab/building-apache-druid-on-kubernetes-how-dailymotion-serves-partner-data-cyril-corbon-alex-triquet-dailymotion
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Apache+Druid+on+Kubernetes%3A+How+Dailymotion+Serves+Partner+Data+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building Apache Druid on Kubernetes: How Dailymotion Serves Partner Data.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyab/building-apache-druid-on-kubernetes-how-dailymotion-serves-partner-data-cyril-corbon-alex-triquet-dailymotion
- YouTube search: https://www.youtube.com/results?search_query=Building+Apache+Druid+on+Kubernetes%3A+How+Dailymotion+Serves+Partner+Data+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FYFq-tGJOQk
- YouTube title: Building Apache Druid on Kubernetes: How Dailymotion Serves Partner... - Cyril Corbon & Alex Triquet
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-apache-druid-on-kubernetes-how-dailymotion-serves-partner-dat/FYFq-tGJOQk.txt
- Transcript chars: 24955
- Keywords: basically, operator, running, historicals, cluster, clusters, database, pretty, queries, operators, change, storage, actually, especially, performances, caching, historical, configuration

### Resumo baseado na transcript

so thank you for coming to our talk about uh building up attitude on kubernetes or the immersion cells pattern data so first there won't be any line of yaml in this presentation so you can get out now if that's what you came for and also we're going to talk about what we are putting in our communities what workload we are running so maybe not the best one in in uh kubecon so I'm Alex Trek I work at Dailymotion as a senior devops engineer and and I'm

### Excerpt da transcript

so thank you for coming to our talk about uh building up attitude on kubernetes or the immersion cells pattern data so first there won't be any line of yaml in this presentation so you can get out now if that's what you came for and also we're going to talk about what we are putting in our communities what workload we are running so maybe not the best one in in uh kubecon so I'm Alex Trek I work at Dailymotion as a senior devops engineer and and I'm Sarah I'm devops architect I at the emotion we are the devops team and we are building kubernetes platform over uh different Cloud providers and on-premise we are also helping developers to uh to set in predictions all the workloads that means we use to deploy the chcds and to enforce best practices for them and we are we are also using we are also doing all the Encore stuff we are companies that build video platform you should not know us we have like four billion views per month and we have two main projects so the dailymotion.com service that is our main platform and uh a network of partners with an advertising platforms for other customers and we serve all the metrics and all the partners datas through to it and we will talk about that in this presentation so yes I introduced you uh what Apache do it is but first uh does anyone here run any Druid quick show of hands please really I'm sorry great so basically what do it is a it's a database you use it to for analytics capacities it's all up you want to use it for time series and that's a lot of benefits like time series and and the column it's a columnar database also so plenty of exciting capacities um the way here we have a presentation of the architecture it's pretty complex there are different ways to run it basically let's take a top-down approach you have zero query node at the top here which are with what we will interact basically they handle all the routing all the queries that are made to the historicals that has a nodes that will serve the data the indexer have the room the mirror walls of the historical is in that they ingest the data into your clusters to be served by the historicals uh underneath we have a layer of deep storage we are running on well S3 protocol at our CSP and on the side you have as a control plan which is a actually fairly complex because here we can see Apache zookeeper metadata storage actually it's a database we are running some MySQL and you have some other Druid nodes so I didn't know all the Persistence of the data also
