---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Bowen Li", "Huichao Zhao", "Apple"]
sched_url: https://kccnceu2022.sched.com/event/ytlq/spark-on-kubernetes-the-elastic-story-bowen-li-huichao-zhao-apple
youtube_search_url: https://www.youtube.com/results?search_query=Spark+on+Kubernetes%3A+The+Elastic+Story+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Spark on Kubernetes: The Elastic Story - Bowen Li & Huichao Zhao, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Bowen Li, Huichao Zhao, Apple
- Schedule: https://kccnceu2022.sched.com/event/ytlq/spark-on-kubernetes-the-elastic-story-bowen-li-huichao-zhao-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Spark+on+Kubernetes%3A+The+Elastic+Story+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Spark on Kubernetes: The Elastic Story.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlq/spark-on-kubernetes-the-elastic-story-bowen-li-huichao-zhao-apple
- YouTube search: https://www.youtube.com/results?search_query=Spark+on+Kubernetes%3A+The+Elastic+Story+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=n7WeoTJq-40
- YouTube title: Spark on Kubernetes: The Elastic Story - Bowen Li & Huichao Zhao, Apple
- Match score: 0.805
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/spark-on-kubernetes-the-elastic-story/n7WeoTJq-40.txt
- Transcript chars: 14676
- Keywords: scaling, resources, running, provide, native, cost, cluster, unicorn, support, interactive, control, feature, platform, infrastructure, workload, driver, elastic, massive

### Resumo baseado na transcript

hi everyone thank you for joining us today it's our pleasure to present you the elastic story of running spark on kubernetes natively at massive skill for apple my name is bowen lee i lead the batch processing and interactive analytics areas of the apple am ammo data platform my team builds and operates called native services like batch processing powered by spark on kubernetes interactive data science service with interactive spark and jupiter and interactive analytics service powered by presto and trino so we serve hundreds of data engineers

### Excerpt da transcript

hi everyone thank you for joining us today it's our pleasure to present you the elastic story of running spark on kubernetes natively at massive skill for apple my name is bowen lee i lead the batch processing and interactive analytics areas of the apple am ammo data platform my team builds and operates called native services like batch processing powered by spark on kubernetes interactive data science service with interactive spark and jupiter and interactive analytics service powered by presto and trino so we serve hundreds of data engineers and scientists every day to improve our ei and mml products like siri and apple search with best-in-class data and analytics and processing infrastructure which how is an engineering from engineer from my team who has been focusing on how to run spark elastically and cost efficiently on kubernetes so here's the agenda today we will first talk about the benefits of cloud and our design principles to elaborate those cloud native characteristics and then the architecture of our cloud native spark on kubernetes platform and why we need to like auto-scale our spark service based on cost saving and elasticity need now which i will dive deep into design of the reactive auto scaling and the productionization of it and our learnings and future work sounds good let's get in there so um you know why we are moving to cloud it's this may not be a new topic but i want to iterate our unique perspectives um so cloud and kubernetes can help solve lots of the problems of legacy infrastructure have for example it is igel resources are consumed on demand and the user can pay as you go second is elastic and scalable we can acquire resources we need and return them when we are done so that saves us lots of money and the compute and the storage are almost infinite skill then kubernetes enables us to build services in a container native way with strong resource isolation so users workload only impact each other this supports our like multi-tenancy and isolation guarantees with cloud and kubernetes we can leverage cognitive cutting-edge security techniques to build a privacy first the data infra and lastly you know kubernetes and the providers of the cloud took away lots of those heavy liftings from us which enabled our developers to focus on building and improve business critical batch processing service to achieve you know higher roi so it's a no-brainer a couple years ago for us to decide to all-in cloud and kubernetes with the benefits o
