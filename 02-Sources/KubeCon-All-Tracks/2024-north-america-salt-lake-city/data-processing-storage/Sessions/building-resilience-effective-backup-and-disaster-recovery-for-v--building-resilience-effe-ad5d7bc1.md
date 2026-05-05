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
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Pavan Navarathna", "Shwetha Subramanian", "Veeam"]
sched_url: https://kccncna2024.sched.com/event/1i7m3/building-resilience-effective-backup-and-disaster-recovery-for-vector-databases-on-kubernetes-pavan-navarathna-shwetha-subramanian-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Building+Resilience%3A+Effective+Backup+and+Disaster+Recovery+for+Vector+Databases+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building Resilience: Effective Backup and Disaster Recovery for Vector Databases on Kubernetes - Pavan Navarathna & Shwetha Subramanian, Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Pavan Navarathna, Shwetha Subramanian, Veeam
- Schedule: https://kccncna2024.sched.com/event/1i7m3/building-resilience-effective-backup-and-disaster-recovery-for-vector-databases-on-kubernetes-pavan-navarathna-shwetha-subramanian-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Resilience%3A+Effective+Backup+and+Disaster+Recovery+for+Vector+Databases+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building Resilience: Effective Backup and Disaster Recovery for Vector Databases on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7m3/building-resilience-effective-backup-and-disaster-recovery-for-vector-databases-on-kubernetes-pavan-navarathna-shwetha-subramanian-veeam
- YouTube search: https://www.youtube.com/results?search_query=Building+Resilience%3A+Effective+Backup+and+Disaster+Recovery+for+Vector+Databases+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kl32-01tXE4
- YouTube title: Building Resilience: Effective Backup and Disaster Recovery for Vec... P. Navarathna, S. Subramanian
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-resilience-effective-backup-and-disaster-recovery-for-vector/kl32-01tXE4.txt
- Transcript chars: 28754
- Keywords: vector, database, canister, backup, databases, action, applications, itself, blueprint, protection, called, application, postgress, controller, location, vectors, backups, profile

### Resumo baseado na transcript

thanks for joining us today and uh today in our talk we're going to learn how to build resilience in your AI applications with effective strategies for backup and disaster recovery for Vector databases on kubernetes my name is scheta and I'm a member of technical staff at viim I develop innovative solutions for data protection in various areas hey all uh my name is Pavan I'm an engineering manager at weim uh I lead a group of of cloud native Engineers building uh the data protection product for applications

### Excerpt da transcript

thanks for joining us today and uh today in our talk we're going to learn how to build resilience in your AI applications with effective strategies for backup and disaster recovery for Vector databases on kubernetes my name is scheta and I'm a member of technical staff at viim I develop innovative solutions for data protection in various areas hey all uh my name is Pavan I'm an engineering manager at weim uh I lead a group of of cloud native Engineers building uh the data protection product for applications on kubernetes I also maintain cncf sandbox project called canister uh we are going to use that project today in our talk welcome again so how many of you use AI in your applications see a lot of hand I mean some hands but uh this is expected uh this talk is going to be useful for all of you who raised your hands um so there are a lot of reasons you might be using AI uh in your applications but here are some um reasons why we thought AI is making a big impact uh by predicting and scaling resources dynamically uh AI can enhance Resource Management so this keeps performance cost uh performance and cost optimized uh then there is security so AI boosts security by detecting anomalies and blocking threats in real time uh this makes more uh like applications more resilient uh then there's also user experience I think by uh enabling personalization and natural interactions for example in customer support and uh uh even like interactions with people on the application itself it creates more engaging experiences uh finally it's uh not the least but uh it also helps with building self-healing abilities uh by predicting you know failures before they happen and reducing the downtime and interruptions so overall uh AI is becoming a critical part of all the applications today making them more efficient secure and uh engaging uh the next simple question is how many of you deploy these applications on kubernetes so again uh this is I think it's very much expected we've been seeing a lot of talks on uh rag and uh deploying these on kubernetes uh there are a lot of Reason again uh when you ask why uh it's mostly because of all these reasons we have listed here uh High availability and scalability uh features like automatic fail over load balancing Dynamic scaling uh this helps meet performance and data Integrity uh requirements for these AI ml applications uh then it improves uh speed of model training by making it easy to deploy distributed uh training workloads and uh D
