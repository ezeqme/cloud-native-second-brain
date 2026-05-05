---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Huichao Zhao", "Apple"]
sched_url: https://kccnceu2024.sched.com/event/1YeO8/faster-safer-serverless-empowering-apache-spark-standalone-cluster-on-kubernetes-huichao-zhao-apple
youtube_search_url: https://www.youtube.com/results?search_query=Faster%2C+Safer%2C+Serverless+-+Empowering+Apache+Spark+Standalone+Cluster+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Faster, Safer, Serverless - Empowering Apache Spark Standalone Cluster on Kubernetes - Huichao Zhao, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Huichao Zhao, Apple
- Schedule: https://kccnceu2024.sched.com/event/1YeO8/faster-safer-serverless-empowering-apache-spark-standalone-cluster-on-kubernetes-huichao-zhao-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Faster%2C+Safer%2C+Serverless+-+Empowering+Apache+Spark+Standalone+Cluster+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Faster, Safer, Serverless - Empowering Apache Spark Standalone Cluster on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeO8/faster-safer-serverless-empowering-apache-spark-standalone-cluster-on-kubernetes-huichao-zhao-apple
- YouTube search: https://www.youtube.com/results?search_query=Faster%2C+Safer%2C+Serverless+-+Empowering+Apache+Spark+Standalone+Cluster+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3IFzP1qZ24k
- YouTube title: Faster, Safer, Serverless - Empowering Apache Spark Standalone Cluster on Kubernetes - Huichao Zhao
- Match score: 1.005
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/faster-safer-serverless-empowering-apache-spark-standalone-cluster-on/3IFzP1qZ24k.txt
- Transcript chars: 25826
- Keywords: cluster, application, running, provide, leverage, operator, master, machine, support, status, platform, firstly, submit, process, question, manage, applications, mentioned

### Resumo baseado na transcript

hi foolx thanks for attending this session and uh how are you uh my name is and uh today I feel deeply honored to be here to share our learnings and Journeys regarding how to running spark on kubernetes and uh let me introduce myself firstly and uh and uh I have been working I I from Apple a ml Department I have been working on design develop and manage large scale spark cluster and Spark workload on kues around four years now and throughout um our journey most recently

### Excerpt da transcript

hi foolx thanks for attending this session and uh how are you uh my name is and uh today I feel deeply honored to be here to share our learnings and Journeys regarding how to running spark on kubernetes and uh let me introduce myself firstly and uh and uh I have been working I I from Apple a ml Department I have been working on design develop and manage large scale spark cluster and Spark workload on kues around four years now and throughout um our journey most recently we have encountered some new and uh very crucial new request from our internal and users which inspiring us try to exploring a new way to all user to running their spark workload on ktic which is running Apachi stand long cluster on top ofes and uh over the next uh 30 minutes I try to have a deep dive to this topic so I try to firstly introdu was our existing you know platform on our uh how to run Sparkle CL on kues and then why we need what kind of challenges we are facing right now and why we introduce this new way and then I try to give you some high level design principles we try to achieve and the detail implementation for that and last thing is like uh what's our ongoing work going to to do uh as you know apach spark is a open source software engineer software and which is kind of a distributed computation engine just in a field of lines of codes in either you know Pon scolar or even Circle data scientist and engineer can easily Define a spark application to process a huge amount of data and the spark will take care of paralyzing the work with the help of a cluster of machines however um sparkk itself cannot uh manage this kind of machines uh directly usually it will rely on some third party class managers to help it uh there are some popular you know class managers like haduan apach mosos or kues of course so around several years ago we have been exploring how to run in spark on kuber netics and uh um we uh through this kind of Journey we find there is quite lot of kind of advantages if we can take this design first of all uh the full containerization this kinds of capability makes spark application on is very agile and pable our data scientist and Engineers can easily install whatever packages to the container images and runs everywhere and uh this is really helpful and speed up our Dev developers you know development velocity and iterations um secondly and U by running spark workload on cloud with help of ktic we can easily apply the autoscaling features to uh Spar applications so
