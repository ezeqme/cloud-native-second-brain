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
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Vara Bonthu", "AWS", "Chaoran Yu", "Apple Inc"]
sched_url: https://kccncna2024.sched.com/event/1i7oq/elevating-kubeflow-spark-operators-future-best-practices-and-enhancements-vara-bonthu-aws-chaoran-yu-apple-inc
youtube_search_url: https://www.youtube.com/results?search_query=Elevating+Kubeflow+Spark+Operator%27s+Future%3A+Best+Practices+and+Enhancements+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Elevating Kubeflow Spark Operator's Future: Best Practices and Enhancements - Vara Bonthu, AWS & Chaoran Yu, Apple Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Vara Bonthu, AWS, Chaoran Yu, Apple Inc
- Schedule: https://kccncna2024.sched.com/event/1i7oq/elevating-kubeflow-spark-operators-future-best-practices-and-enhancements-vara-bonthu-aws-chaoran-yu-apple-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Elevating+Kubeflow+Spark+Operator%27s+Future%3A+Best+Practices+and+Enhancements+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Elevating Kubeflow Spark Operator's Future: Best Practices and Enhancements.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oq/elevating-kubeflow-spark-operators-future-best-practices-and-enhancements-vara-bonthu-aws-chaoran-yu-apple-inc
- YouTube search: https://www.youtube.com/results?search_query=Elevating+Kubeflow+Spark+Operator%27s+Future%3A+Best+Practices+and+Enhancements+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5m05fOVajto
- YouTube title: Elevating Kubeflow Spark Operator's Future: Best Practices and Enhancements- Vara Bonthu, Chaoran Yu
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/elevating-kubeflow-spark-operators-future-best-practices-and-enhanceme/5m05fOVajto.txt
- Transcript chars: 32021
- Keywords: operator, itself, metrics, apache, google, called, running, resources, applications, unicorn, controller, server, another, features, within, application, feature, cluster

### Resumo baseado na transcript

so ju just before we kick off the session uh just would like to Quick raise of hands how many of you are currently using spark operator on kubernetes today that's not a bad number that's good but we're going to cover bit of basics of the spark and then spark operator um so I think you should be okay right so with the my name is vuntu I'm a principal open source specialist sess working with AWS and I'm also a qflow spar operator maintainer and in my day-to-day

### Excerpt da transcript

so ju just before we kick off the session uh just would like to Quick raise of hands how many of you are currently using spark operator on kubernetes today that's not a bad number that's good but we're going to cover bit of basics of the spark and then spark operator um so I think you should be okay right so with the my name is vuntu I'm a principal open source specialist sess working with AWS and I'm also a qflow spar operator maintainer and in my day-to-day job I work with uh data and ml platforms and building these platforms highly scalable on kubernetes yeah uh that's me with me uh my co-presenter uh Sharon do you want to introduce yourself uh hello everyone uh thanks thanks for attending our talk my name is tan I lead the solutions engineering team at Apple I'm one of the early contributors of the spark operator project and also a maintainer glad to be here today thanks Shon right um so this is elevating Q FL par operator so we're going to talk about some of the best prct best practices and enhancements in today's session so with the um we're going to touch upon some of the basics of uh Apache spark and and how spark operator is evolved and we will also talk about the migration of spark operator from Google to qlow community which a qlow or and since we migrated to Q spark operator we added a lot of enhancements and features then we'll touch upon all the enhancements and features and we will discuss some of the best practices of running spark operator on kubernetes in any platform and finally uh we discuss some of the CU flow Community how you can join and become part of the community to work with the spark operator right so before I give an introduction to spark operator I want to touch upon Apache spark itself right so most of you are familiar with Apache spark Apache spark is very popular and distributed data processing framework which is used for both batch processing streaming and even machine learning worklet today right in Apache spark in 2018 uh in version 2.3 that is one Apaches spark added a support for running on kubernetes uh in addition to um Hado and you know msos so that's when things have changed a lot of customers and organizations started to run the spark on kuties So within the same year in 2018 uh the same contributors also started building the spark operator and they buil and some of the Google folks have built the Google Cloud I think they are from Google Cloud platform and they built this Google spark operator and they open sour
