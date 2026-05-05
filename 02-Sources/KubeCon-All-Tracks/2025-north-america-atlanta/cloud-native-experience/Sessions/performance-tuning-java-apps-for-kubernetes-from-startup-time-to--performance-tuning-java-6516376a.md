---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Experience"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Ryan Jarvinen", "Red Hat", "Daniel Oh", "IBM"]
sched_url: https://kccncna2025.sched.com/event/27FXX/performance-tuning-java-apps-for-kubernetes-from-startup-time-to-container-efficiency-ryan-jarvinen-red-hat-daniel-oh-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Performance+Tuning+Java+Apps+for+Kubernetes%3A+From+Startup+Time+To+Container+Efficiency+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Performance Tuning Java Apps for Kubernetes: From Startup Time To Container Efficiency - Ryan Jarvinen, Red Hat & Daniel Oh, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Ryan Jarvinen, Red Hat, Daniel Oh, IBM
- Schedule: https://kccncna2025.sched.com/event/27FXX/performance-tuning-java-apps-for-kubernetes-from-startup-time-to-container-efficiency-ryan-jarvinen-red-hat-daniel-oh-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Performance+Tuning+Java+Apps+for+Kubernetes%3A+From+Startup+Time+To+Container+Efficiency+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Performance Tuning Java Apps for Kubernetes: From Startup Time To Container Efficiency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXX/performance-tuning-java-apps-for-kubernetes-from-startup-time-to-container-efficiency-ryan-jarvinen-red-hat-daniel-oh-ibm
- YouTube search: https://www.youtube.com/results?search_query=Performance+Tuning+Java+Apps+for+Kubernetes%3A+From+Startup+Time+To+Container+Efficiency+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7sF5fiPtd24
- YouTube title: Performance Tuning Java Apps for Kubernetes: From Startup Time To Conta... Ryan Jarvinen & Daniel Oh
- Match score: 0.929
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/performance-tuning-java-apps-for-kubernetes-from-startup-time-to-conta/7sF5fiPtd24.txt
- Transcript chars: 24747
- Keywords: application, container, native, actually, little, memory, already, version, startup, automatically, performance, spring, circus, couple, developer, framework, docker, command

### Resumo baseado na transcript

All right, so we're going to talk a little bit about performance tuning about Java application on Kubernetes and then many practical tips. I'm longtime dev and develop AR kit and CSF ambassador and Java champion and here's Kevin and I we are uh reading some new tech the technical advisory group for developer experience so if you have any interesting contribution back to CNCF around developer experience your java application maybe quite slow to start up and response time and eagering a lot of resources is a memory for free and then when you packaging your application container and then oh there's something problem for example Ryan we really talk about that java developer around include me include you all guys so we don't want you guys to lose job today so how do you overcome this challenge for that Yeah. The blue line here is the typical um service level agreement that Kubernetes is going to expect when starting up a typical kind of stateless app. And uh eventually it'll usually have some higher throughput or a higher performance than a uh the blue line here but only after a certain amount of time.

### Excerpt da transcript

All righty, we're going to get starting and thanks for joining today. This is all about Java by the way. How many people are actually Java developer here? >> Very nice. Okay, if not over there. Okay, just kidding. All right, so we're going to talk a little bit about performance tuning about Java application on Kubernetes and then many practical tips. And my name is Daniel. I'm from Redhead IBM. I'm longtime dev and develop AR kit and CSF ambassador and Java champion and here's Kevin and I we are uh reading some new tech the technical advisory group for developer experience so if you have any interesting contribution back to CNCF around developer experience please let us know we are more than happy to chat and here's my colleague Ryan >> hi I'm Ryan Jarvin I'm also Red Hat uh previously currently at IBM M uh I've been going to KubeCon for quite a while. I'm wearing my 10-year-old KubeCon 1 shirt. Uh excited to be here and share our experiences with you. >> That's nice. By the way, I'm from Boston. My flight was delayed five hours on Sunday thanks to America by the way.

Anyway, so uh I'm still a little bit like a Tyanese and then if you feel something uncomfortable voice from me and then please understand that. Okay. So, uh before we jump into the actual uh performance tuning part. So everybody knows Java uh really quite slow for the decades because Java was born 30 years today and at a time Java was great for enterprise application with the JVM not cloud and for your business application enterprise application a little bit heavyweight nobody actually don't care uh it takes more than one minute to start up like a J boss or web logic and I was a pretty heavy weight putting a lot of business application services we can say monolithic application at a time and the things changed that everybody moving forward to microservices like a spring boot circus microno and any other spring like a java framework and then uh people try to uh like a uh refactoring all mon application to microservices and now you have a cloud and still your java application maybe quite slow to start up and response time and eagering a lot of resources is a memory for free and then when you packaging your application container and then oh there's something problem for example Ryan we really talk about that a little bit later so when you deploy Java on container and container startup and inside the container application also start up on JVM it takes time like a couple second maybe depends on h
