---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Rainie Li", "Ang Zhang", "Pinterest"]
sched_url: https://kccnceu2026.sched.com/event/2CW61/from-idle-to-savings-building-a-global-scheduler-for-costefficient-data-processing-on-k8s-rainie-li-ang-zhang-pinterest
youtube_search_url: https://www.youtube.com/results?search_query=From+Idle+to+Savings%3A+Building+a+Global+Scheduler+for+Cost%E2%80%91Efficient+Data+Processing+on+K8s+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data Processing on K8s - Rainie Li & Ang Zhang, Pinterest

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rainie Li, Ang Zhang, Pinterest
- Schedule: https://kccnceu2026.sched.com/event/2CW61/from-idle-to-savings-building-a-global-scheduler-for-costefficient-data-processing-on-k8s-rainie-li-ang-zhang-pinterest
- Busca YouTube: https://www.youtube.com/results?search_query=From+Idle+to+Savings%3A+Building+a+Global+Scheduler+for+Cost%E2%80%91Efficient+Data+Processing+on+K8s+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data Processing on K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW61/from-idle-to-savings-building-a-global-scheduler-for-costefficient-data-processing-on-k8s-rainie-li-ang-zhang-pinterest
- YouTube search: https://www.youtube.com/results?search_query=From+Idle+to+Savings%3A+Building+a+Global+Scheduler+for+Cost%E2%80%91Efficient+Data+Processing+on+K8s+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8P2y_gyHQA8
- YouTube title: From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data P... Rainie Li & Ang Zhang
- Match score: 0.96
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-idle-to-savings-building-a-global-scheduler-for-cost-efficient-da/8P2y_gyHQA8.txt
- Transcript chars: 19293
- Keywords: cluster, capacity, platform, online, resource, pinterest, applications, global, available, cost, constantly, challenging, controller, application, adopted, everything, remote, scheduleuler

### Resumo baseado na transcript

Hello everyone, welcome to the talk and today I will talk about how we build cost efficient data processing platform on Kubernetes at Pinterest. Unfortunately my co-presenter on cannot join today but I will cover his part. We also adopted the Apache iceberg as a remote shuffling service to decouple the compute nodes and the storage nodes. Uh on top right side is our uh like querybook notebook dashboard which interact with um data scientists and business intelligence users. We use Presto and Trino and Spark SQL to query the data from the data lake. They own the ray and pytorch and the mocha platform top layer is the archer which is our job submission service on top of kubernetes.

### Excerpt da transcript

Hello everyone, welcome to the talk and today I will talk about how we build cost efficient data processing platform on Kubernetes at Pinterest. Unfortunately my co-presenter on cannot join today but I will cover his part. Uh I'm Rainey. I'm currently a senior engineering manager at Pinterest. I'm managing data process infra team and the big data storage platform team. Here is today's agenda. First I will talk about Pinterest data infra high level overview. Then I will talk about the key challenges of the resource management and then I will talk about how we utilize Kubernetes to manage resource uh in a cost efficient way and how we utilize unused reserved capacity for batch processing applications. I will leave some time at the end for Q&A. Before I dive into the data infra high level overview, I would like to quickly introduce Pinterest. Uh we are a visual discovery platform. Uh so user like piners can select pins and add to their board. Uh eventually they can turn these inspirations and ideas to the real life.

So we are datadriven company. We have a very large scale data needs to ingest and process. From this diagram you can see on the uh top left side these are the different data producers. Users can go to the app browser and even thirdarty data and these data will come to our uh Pinterest API services. On each host we have a login agent and this logging agent will constantly uh inject this data into our popsup service which we build on top of Apache Kafka and the Mammq. uh this pop sub service will constantly inject these events uh into uh topics. There's a real time ingestion service written in uh Flink streaming application. It will do real time ingestion from this Kafka topic to our data lake. We built our data lake on top of AWS S3. We store all the raw data on S3. We also adopted Apache iceberg as a metadata layer on top of the original data so that we can provide standardized table format for the users. It also provides a uh quickly indexing switch between uh different snapshots. So right now we basically ingest all the data from users.

Let's go to the right side. The bottom part of the right side is our data processing like compute platform. We built everything on top of Kubernetes. We use EKS. We also adopted the Apache iceberg as a remote shuffling service to decouple the compute nodes and the storage nodes. On top of that, we have the Frink as a streaming engine and the Spark at the batch engine. We support different use cases like indexin
