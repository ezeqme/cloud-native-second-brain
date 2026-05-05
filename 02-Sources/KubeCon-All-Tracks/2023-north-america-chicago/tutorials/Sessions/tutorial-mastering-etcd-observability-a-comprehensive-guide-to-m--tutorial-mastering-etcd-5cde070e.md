---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Tutorials"
themes: ["Observability", "Storage Data", "SRE Reliability"]
speakers: ["Bogdan Kanivets", "Vivek Patani", "Apple"]
sched_url: https://kccncna2023.sched.com/event/1R2rD/tutorial-mastering-etcd-observability-a-comprehensive-guide-to-metrics-monitoring-and-incident-handling-bogdan-kanivets-vivek-patani-apple
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Mastering+Etcd+Observability%3A+A+Comprehensive+Guide+to+Metrics%2C+Monitoring%2C+and+Incident+Handling+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Mastering Etcd Observability: A Comprehensive Guide to Metrics, Monitoring, and Incident Handling - Bogdan Kanivets & Vivek Patani, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Observability]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Bogdan Kanivets, Vivek Patani, Apple
- Schedule: https://kccncna2023.sched.com/event/1R2rD/tutorial-mastering-etcd-observability-a-comprehensive-guide-to-metrics-monitoring-and-incident-handling-bogdan-kanivets-vivek-patani-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Mastering+Etcd+Observability%3A+A+Comprehensive+Guide+to+Metrics%2C+Monitoring%2C+and+Incident+Handling+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Mastering Etcd Observability: A Comprehensive Guide to Metrics, Monitoring, and Incident Handling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rD/tutorial-mastering-etcd-observability-a-comprehensive-guide-to-metrics-monitoring-and-incident-handling-bogdan-kanivets-vivek-patani-apple
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Mastering+Etcd+Observability%3A+A+Comprehensive+Guide+to+Metrics%2C+Monitoring%2C+and+Incident+Handling+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GtAIwwJ5EJk
- YouTube title: Tutorial: Mastering Etcd Observability: A Comprehensive Guide to M... Bogdan Kanivets & Vivek Patani
- Match score: 0.794
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-mastering-etcd-observability-a-comprehensive-guide-to-metrics/GtAIwwJ5EJk.txt
- Transcript chars: 59726
- Keywords: compaction, leader, metrics, server, actually, benchmark, important, members, compact, database, cluster, little, dashboard, proposal, metric, scenario, running, client

### Resumo baseado na transcript

um hi folks uh let's get started so today my teammate Bogden and I VI are going to talk about mastering ET absorbability so let's just get into it first um there's a prerequisite that uh we would recommend that you kind of go through um is this something that we would recommend that you download because some are Docker compos images and Internet isn't really stable right now so if it's possible then uh just scan the barcode or just follow the link along and then uh we get

### Excerpt da transcript

um hi folks uh let's get started so today my teammate Bogden and I VI are going to talk about mastering ET absorbability so let's just get into it first um there's a prerequisite that uh we would recommend that you kind of go through um is this something that we would recommend that you download because some are Docker compos images and Internet isn't really stable right now so if it's possible then uh just scan the barcode or just follow the link along and then uh we get started I'll just give it a minute once we're done we can just move forward okay I think Bon's going to help you out uh so just uh raise your hand if you have a problem or anything like that uh but we strongly recommend you follow us follow us along while we go on this journey it' be fun okay um so just moving on uh just to kind of review what we're going to achieve today or what we're going to learn today um just the fundamentals of hcd um just talk about leader election in general and how it impacts that CD uh the architecture of how um how everything is placed how everything interacts um uh the meat of everything metrics and their fundamentals of how they're structured how you can access metrics how you can look at them and make sense of it and then we have a lab session after this uh just just after this brief intro uh we just run through a few scenarios of what problems you might run into and what metrics are really important for you to look at in these scenarios so let's just take a walk um so the basic fundamental question you'd ask is what is atcd atcd is just a simple key value store it's distributed in nature what does that mean it means that the computation like the storage layer is separated or like split up among different computers and not just one single computer um so all the computation the storage happens on uh in a distributed fashion the next thing is replication um a replic by replication it means that it replicates data on all the members of the node uh of of the cluster um HD is a cluster and it has multiple members within it so that's kind of the idea um consistency so getting and setting or like getting and putting data in happens in a consistent fashion which is what is primary or like very essential to a database so that's kind of what this um makes available and then highly available uh that just means that until and unless ET has Corum you're good to go so say for example if ET has like five members in the cluster and one of them was to go down you'd still get
