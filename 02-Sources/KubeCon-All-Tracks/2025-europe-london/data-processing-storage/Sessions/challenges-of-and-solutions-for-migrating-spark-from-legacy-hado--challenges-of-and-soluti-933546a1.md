---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Neha Singla", "Rasik Pandey", "Apple"]
sched_url: https://kccnceu2025.sched.com/event/1txH9/challenges-of-and-solutions-for-migrating-spark-from-legacy-hadoop-clusters-to-kubernetes-neha-singla-rasik-pandey-apple
youtube_search_url: https://www.youtube.com/results?search_query=Challenges+of+and+Solutions+for+Migrating+Spark+From+Legacy+Hadoop+Clusters+To+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Challenges of and Solutions for Migrating Spark From Legacy Hadoop Clusters To Kubernetes - Neha Singla & Rasik Pandey, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Neha Singla, Rasik Pandey, Apple
- Schedule: https://kccnceu2025.sched.com/event/1txH9/challenges-of-and-solutions-for-migrating-spark-from-legacy-hadoop-clusters-to-kubernetes-neha-singla-rasik-pandey-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Challenges+of+and+Solutions+for+Migrating+Spark+From+Legacy+Hadoop+Clusters+To+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Challenges of and Solutions for Migrating Spark From Legacy Hadoop Clusters To Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txH9/challenges-of-and-solutions-for-migrating-spark-from-legacy-hadoop-clusters-to-kubernetes-neha-singla-rasik-pandey-apple
- YouTube search: https://www.youtube.com/results?search_query=Challenges+of+and+Solutions+for+Migrating+Spark+From+Legacy+Hadoop+Clusters+To+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Q2ct5OXQ8fU
- YouTube title: Challenges of and Solutions for Migrating Spark From Legacy Hadoop Clu... Neha Singla & Rasik Pandey
- Match score: 0.884
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/challenges-of-and-solutions-for-migrating-spark-from-legacy-hadoop-clu/Q2ct5OXQ8fU.txt
- Transcript chars: 34020
- Keywords: resource, shuffle, interactive, kernel, cluster, workloads, running, storage, resources, tracking, allocation, configuration, configurations, unicorn, jupyter, dynamic, environment, scheduleuler

### Resumo baseado na transcript

Uh today Nay and I here from Apple, we're going to talk a little bit about the journey we had from moving our Spark workloads from legacy Hadoop clusters um and overall to the Kubernetes kind of um ecosystem a number of years ago when Kubernetes was maybe not as nice as it is today. So, so in in terms of agenda, we're going to talk a bit about, you know, going from bare metal to Kubernetes and how we had to evolve kind of Spark techniques over time to make that work. So interactive spark plays a cru crucial role in like big data processing, data science and machine learning workflows for faster uh data exploration, debugging and ML experiments and uh Jupyter notebook is one of the popular tool used in industry for interactive spark experiments. Um so interactive spark needs to provide uh low latency responses for querying and processing large data sets. Uh it can dynamically scale executors based on the workload demands and support shuffle with external shuffle service. Uh it is important to note that YAN was not designed to orchestrate any containerized application but specifically designed for orchestrating applications within Hadoop.

### Excerpt da transcript

Thanks folks for coming. Uh today Nay and I here from Apple, we're going to talk a little bit about the journey we had from moving our Spark workloads from legacy Hadoop clusters um and overall to the Kubernetes kind of um ecosystem a number of years ago when Kubernetes was maybe not as nice as it is today. So you'll hear some war stories there as well. So, so in in terms of agenda, we're going to talk a bit about, you know, going from bare metal to Kubernetes and how we had to evolve kind of Spark techniques over time to make that work. And you'll kind of see like we went we went through one other type of uh uh compute uh story in between going from bare metal to Kubernetes and then ultimately now being on Kubernetes with u advanceduler like unicorn also super excited to learn about all the developments in Q and that those have kind of come along in the last couple of weeks and then kind of key takeaways for like making Spark work well on Kubernetes because you know traditionally Kubernetes is not built for um let's a data inensive workloads.

So we'll talk a little bit about best practice and pitfalls and antiatterns to kind of stay away from in terms of objective objectives in the migration is like we have a lot of data engineers and um data analysts who are using spark and they need interactive access to large data sets. uh we really kind of want to separate storage and compute like kind of that disagregation over the last six or more years right being able to put your data in cloud storage or some uh storage system that doesn't have your compute coupled to it gives you a lot of flexibility then we also will talk about cluster autoscaling and then containerization and dependency management and then ultimately like better resource utilization is a very key part of this to allow us to kind of reduce cost and then automating as much of this as possible So with that, I'll hand it over to one of our best minds, Nha, to tell you more about this journey. Hey everyone, my name is Nha Singla. Uh I'm a software engineer at Apple. Um thanks for sticking with us uh this evening.

I appreciate it. I know it's been a long day. So uh I'm going to talk about uh some of the special requirements uh with interactive spark. So interactive spark plays a cru crucial role in like big data processing, data science and machine learning workflows for faster uh data exploration, debugging and ML experiments and uh Jupyter notebook is one of the popular tool used in industry for
