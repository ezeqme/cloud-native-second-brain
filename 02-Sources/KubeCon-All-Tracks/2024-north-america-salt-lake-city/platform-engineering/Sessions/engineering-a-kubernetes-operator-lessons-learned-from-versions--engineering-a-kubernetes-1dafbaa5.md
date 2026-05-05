---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Storage Data", "Kubernetes Core"]
speakers: ["Andrew L'Ecuyer", "Crunchy Data"]
sched_url: https://kccncna2024.sched.com/event/1i7n6/engineering-a-kubernetes-operator-lessons-learned-from-versions-1-to-5-andrew-lecuyer-crunchy-data
youtube_search_url: https://www.youtube.com/results?search_query=Engineering+a+Kubernetes+Operator%3A+Lessons+Learned+from+Versions+1+to+5+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Engineering a Kubernetes Operator: Lessons Learned from Versions 1 to 5 - Andrew L'Ecuyer, Crunchy Data

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Andrew L'Ecuyer, Crunchy Data
- Schedule: https://kccncna2024.sched.com/event/1i7n6/engineering-a-kubernetes-operator-lessons-learned-from-versions-1-to-5-andrew-lecuyer-crunchy-data
- Busca YouTube: https://www.youtube.com/results?search_query=Engineering+a+Kubernetes+Operator%3A+Lessons+Learned+from+Versions+1+to+5+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Engineering a Kubernetes Operator: Lessons Learned from Versions 1 to 5.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7n6/engineering-a-kubernetes-operator-lessons-learned-from-versions-1-to-5-andrew-lecuyer-crunchy-data
- YouTube search: https://www.youtube.com/results?search_query=Engineering+a+Kubernetes+Operator%3A+Lessons+Learned+from+Versions+1+to+5+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p2v7bPJkrVU
- YouTube title: Engineering a Kubernetes Operator: Lessons Learned from Versions 1 to 5 - Andrew L'Ecuyer
- Match score: 0.983
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/engineering-a-kubernetes-operator-lessons-learned-from-versions-1-to-5/p2v7bPJkrVU.txt
- Transcript chars: 37667
- Keywords: postgres, operator, cluster, upgrade, within, upgrades, solution, version, database, availability, recovery, process, volume, leader, learned, patron, disaster, running

### Resumo baseado na transcript

so great to be here with you today in Salt Lake City for cucon North America I'm really excited to be here today talking about kubernetes operators and some of my own experience at crunchy data engineering and operator for postres I've got quite a lot of content to cover today so let's get started first a quick note about myself my name is Andre lir and I am the senior director of kubernetes engineering at crunchy data at crunchy data our motto is postes anywhere we have a fully

### Excerpt da transcript

so great to be here with you today in Salt Lake City for cucon North America I'm really excited to be here today talking about kubernetes operators and some of my own experience at crunchy data engineering and operator for postres I've got quite a lot of content to cover today so let's get started first a quick note about myself my name is Andre lir and I am the senior director of kubernetes engineering at crunchy data at crunchy data our motto is postes anywhere we have a fully managed Cloud we support bare metal and VMS and of course we have crunchy postgres for kubernetes which I'll be talking about today in this talk I'll be covering Lessons Learned From crunchy data's experience building five versions of a postgres operator for kubernetes and to do this I will highlight three key areas of the operator architecture High availability upgrades and disaster recovery so why do we need operators operators not only help to manage the complexity of deploying and managing an application but they also reduce toil and invite new communities to take part in the kubernetes ecosystem and in 17 crunchy data recognized that operators could reduce the operational complexity of running posts at first it was simply a matter of containerizing post but once we were containerized we needed to orchestrate and to properly orchestrate especially in the areas of high availability upgrades and Disaster Recovery we wanted an operator so let's quickly rewind back to 2017 and the first pigo release pigo version one was released on March 27th 2017 and kubernetes version 1.6 was released just one day later as we all know we're now up to kubernetes version 1.31 with version 1.32 do out next month and safe to say quite a lot has changed over 7even years and 25 releases of kubernetes Frameworks for operators were limited as was support for stateful application within kubernetes so let's dive into the P architecture and talk about high availability or ha starting with the definition any application will experience failures or crashes during its operation by making an application highly available we ensure it remains available for use which means quickly recovering from issues when they do occur or even better prev Ving those issues from occurring in the first place so from a postgres perspective this means ensuring the database and therefore the user's data remains accessible in the early days of the operator we realized there are two types of high availability to consider availability
