---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Christian Schlotter", "Broadcom", "Vince Prignano", "Apple"]
sched_url: https://kccncna2024.sched.com/event/1howc/cluster-api-deep-dive-roadmap-to-api-graduation-christian-schlotter-broadcom-vince-prignano-apple
youtube_search_url: https://www.youtube.com/results?search_query=Cluster+API+Deep+Dive+-+Roadmap+to+API+Graduation+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cluster API Deep Dive - Roadmap to API Graduation - Christian Schlotter, Broadcom & Vince Prignano, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Christian Schlotter, Broadcom, Vince Prignano, Apple
- Schedule: https://kccncna2024.sched.com/event/1howc/cluster-api-deep-dive-roadmap-to-api-graduation-christian-schlotter-broadcom-vince-prignano-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Cluster+API+Deep+Dive+-+Roadmap+to+API+Graduation+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cluster API Deep Dive - Roadmap to API Graduation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howc/cluster-api-deep-dive-roadmap-to-api-graduation-christian-schlotter-broadcom-vince-prignano-apple
- YouTube search: https://www.youtube.com/results?search_query=Cluster+API+Deep+Dive+-+Roadmap+to+API+Graduation+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=F2iO_cKKPuI
- YouTube title: Cluster API Deep Dive - Roadmap to API Graduation - Christian Schlotter & Vince Prignano
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cluster-api-deep-dive-roadmap-to-api-graduation/F2iO_cKKPuI.txt
- Transcript chars: 19788
- Keywords: cluster, machine, clusters, machines, fields, version, getting, possible, create, control, manage, already, controller, making, running, introducing, production, providers

### Resumo baseado na transcript

uh hello everyone this is the cluster API intro dip dive and future so it's a lot to to cover um but we'll start by introducing ourselves I'm Vince I'm a softare engineer at Apple um and I'm also s cluster life cycle co-chair and controller on time M controller time and cluster API maintainer I'm Christian I'm software engineer at broadcom and I'm all cluster API maintainer all right so what is the vision for this project this project started like almost like seven years ago um and the

### Excerpt da transcript

uh hello everyone this is the cluster API intro dip dive and future so it's a lot to to cover um but we'll start by introducing ourselves I'm Vince I'm a softare engineer at Apple um and I'm also s cluster life cycle co-chair and controller on time M controller time and cluster API maintainer I'm Christian I'm software engineer at broadcom and I'm all cluster API maintainer all right so what is the vision for this project this project started like almost like seven years ago um and the vision overall was to build the meta Cloud what we're getting really close to what it is today which is we have declarative apis they're production ready so you can use them today in your production workloads and we want to make managing these clusters and Fleet of clusters as easy as possible so you should be able to upgrade them you should be able to make sure that like your cluster and node will be always up so if you all are offering a cluster as a service solution or like for other which is a common use case CLP is your friend one of the key things I keep repeating I have another slide too about this um we make the 80% use case possible it simple and the 20% possible what does this mean if you go into the core of cluster API you will see that there's a lot of batters included we want to make sure that you can just start using the project as fast as possible and you can create a cluster so for example if you go to the quick start you can create a cluster in your local Docker environment using kind and that will look exactly the same as like a cluster using AWS extension points docking ports what does this means like a lot of times like a um a lot of people come in with new featured and use cases that they would like to add what we do usually is like we sit down and like we try to in in an open discussion forum we try to make these featur like making sure that like they're as generic as possible and if something doesn't fit in core we make sure that there is an extension for it so you can build it outside this is kind of the overall definition we have kubernetes style apis which means we use kubernetes to create kubernetes clusters the most beautiful thing about cluster API that I'll keep repeating that I love the most is that cluster API clusters can manage themselves so you can have one cluster that's managing itself and a fleet of other clusters we want to make cluster life cycle boring which kind of goes against you know as being a CH of clustal life cycle like okay w
