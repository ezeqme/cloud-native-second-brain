---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Robert Hodges", "Altinity"]
sched_url: https://kccncna2023.sched.com/event/1R2vr/adventures-in-data-leaning-on-kubernetes-storage-to-run-hundreds-of-real-time-analytic-databases-robert-hodges-altinity
youtube_search_url: https://www.youtube.com/results?search_query=Adventures+in+Data-+Leaning+on+Kubernetes+Storage+to+Run+Hundreds+of+Real-Time+Analytic+Databases+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Adventures in Data- Leaning on Kubernetes Storage to Run Hundreds of Real-Time Analytic Databases - Robert Hodges, Altinity

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Robert Hodges, Altinity
- Schedule: https://kccncna2023.sched.com/event/1R2vr/adventures-in-data-leaning-on-kubernetes-storage-to-run-hundreds-of-real-time-analytic-databases-robert-hodges-altinity
- Busca YouTube: https://www.youtube.com/results?search_query=Adventures+in+Data-+Leaning+on+Kubernetes+Storage+to+Run+Hundreds+of+Real-Time+Analytic+Databases+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Adventures in Data- Leaning on Kubernetes Storage to Run Hundreds of Real-Time Analytic Databases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vr/adventures-in-data-leaning-on-kubernetes-storage-to-run-hundreds-of-real-time-analytic-databases-robert-hodges-altinity
- YouTube search: https://www.youtube.com/results?search_query=Adventures+in+Data-+Leaning+on+Kubernetes+Storage+to+Run+Hundreds+of+Real-Time+Analytic+Databases+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ogN_DOHJTIY
- YouTube title: Adventures in Data- Leaning on Kubernetes Storage to Run Hundreds of Real-Time Anal... Robert Hodges
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/adventures-in-data-leaning-on-kubernetes-storage-to-run-hundreds-of-re/ogN_DOHJTIY.txt
- Transcript chars: 41617
- Keywords: storage, actually, database, volume, stateful, databases, interesting, systems, operator, pretty, another, running, performance, amazon, talking, controller, question, compute

### Resumo baseado na transcript

all right welcome everybody I'm so glad you're here I'm going to be talking about adventures in data and uh leaning on kubernetes storage to run hundreds of real-time analytic databases as you'll see in a moment I am a database person let's just jump into the intro Parts my name is Robert Hodges I've been working on databases for over 40 years and as a database person we love storage uh kubernetes has made it very interesting because it's quite different from the storage that we the things we

### Excerpt da transcript

all right welcome everybody I'm so glad you're here I'm going to be talking about adventures in data and uh leaning on kubernetes storage to run hundreds of real-time analytic databases as you'll see in a moment I am a database person let's just jump into the intro Parts my name is Robert Hodges I've been working on databases for over 40 years and as a database person we love storage uh kubernetes has made it very interesting because it's quite different from the storage that we the things we used to love about storage return things like battery back cash and firmware versions and raid and stuff like that there's a whole new set of of resources that we have to think about um been working on kubernetes for uh since 2018 my day job is I'm a CEO of a database startup called ality and what I'm going to be talking about here is actually based on our experience in that startup we are a service provider for click house 5 years ago we made a decision to move our processing to make a bet basically that kubernetes was going to be the wave of the future for uh management of data that has turned out to be true in Spades and among other things we as part of that bet we built an operator for first of all for click House popular data warehouse uh service that I'll be talking about a little bit here and um then built a cloud on top of it have there's now at this point thousands of clusters uh running on this we ourselves in our Cloud running are running about 200 40 prod clusters uh data warehouse clusters at this time um some of them are pretty big you know sort of 24 nodes 40 uh 40 terabytes of attached storage uh these are these are not small so uh that's the engineering and in fact as I go through here I will be talking about specifically about click house so that I know what I'm talking about but just about everything we do here is generalizes to other database systems so let's just talk a little bit about analytic databases and introduce click house so click house is what's called a real-time analytic database and there's some kind of marketing words here that explain it but what's simpler is to explain what it does imagine a security event and Incident Management System it could be a multi-tenant system say run by some big company like Cisco it could be reading tens of millions of events per second that are based on you know data from various types of sources and looking for trouble people breaking into systems uh you know calls to servers DNS uh requests to server
