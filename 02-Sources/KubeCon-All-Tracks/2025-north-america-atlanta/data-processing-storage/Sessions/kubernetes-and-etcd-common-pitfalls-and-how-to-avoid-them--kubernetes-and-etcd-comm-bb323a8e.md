---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Arka Saha", "Nabarun Pal", "Broadcom"]
sched_url: https://kccncna2025.sched.com/event/27FWl/kubernetes-and-etcd-common-pitfalls-and-how-to-avoid-them-arka-saha-nabarun-pal-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+and+etcd%3A+Common+Pitfalls+and+How+To+Avoid+Them+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes and etcd: Common Pitfalls and How To Avoid Them - Arka Saha & Nabarun Pal, Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Arka Saha, Nabarun Pal, Broadcom
- Schedule: https://kccncna2025.sched.com/event/27FWl/kubernetes-and-etcd-common-pitfalls-and-how-to-avoid-them-arka-saha-nabarun-pal-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+and+etcd%3A+Common+Pitfalls+and+How+To+Avoid+Them+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes and etcd: Common Pitfalls and How To Avoid Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWl/kubernetes-and-etcd-common-pitfalls-and-how-to-avoid-them-arka-saha-nabarun-pal-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+and+etcd%3A+Common+Pitfalls+and+How+To+Avoid+Them+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wj9UQDcRSWA
- YouTube title: Kubernetes and etcd: Common Pitfalls and How To Avoid Them - Arka Saha & Nabarun Pal, Broadcom
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-and-etcd-common-pitfalls-and-how-to-avoid-them/wj9UQDcRSWA.txt
- Transcript chars: 23313
- Keywords: cluster, clusters, events, running, network, specific, compaction, metrics, pitfalls, objects, performance, common, issues, errors, database, leader, sequential, important

### Resumo baseado na transcript

Uh so thank you for coming to our session Kubernetes and CID common pitfalls and how to avoid them and especially for those large scale consumers who uh might be coming across all these uh issues. So before we start uh I want to talk about the code of conduct which basically boils down to being nice to everyone. So to avoid this problem uh Kubernetes and CCD has a very uh well-laidout contract which basically says that Kubernetes depends a lot on CD's underlying uh core logic and functions and this document mainly reinforces on that and makes the documentation and testing of both the projects more robust. But you might run into a few problems while doing that depending on uh from which version you are coming from. So one of those common errors is too many learner and member learner member in the cluster. What can happen is that uh one member which has become has been upgraded to 3.6 and it is a learner and it has caught up with all the data from the leader and is up for a promotion to the to a follower.

### Excerpt da transcript

Hello everyone. Uh I guess we are almost time to start. Uh so thank you for coming to our session Kubernetes and CID common pitfalls and how to avoid them and especially for those large scale consumers who uh might be coming across all these uh issues. So before we start uh I want to talk about the code of conduct which basically boils down to being nice to everyone. And a little about ourselves. Uh I'm Orco Shaha. Uh I work at Broadcom as a software engineer and I'm a contributor inc. Hi everyone, I'm Nabarun. I also work at Broadcom. Um I work on specific Kubernetes bits um for the Kubernetes distribution team at Broadcom. Um I also try to maintain a few areas of Kubernetes. Um so uh Henry from also from the HCD community was supposed to join the talk but he could not make it to um this cube pan so I joined or in the talk in explaining a few bits of how to avoid the uh common pitfalls. So I'll give to orgo to go through an journey of like what are the common issues that one might run into. >> Thanks.

Uh so let's see why ATCD is so important in uh the Kubernetes space. So as we all know CD is the her of Kubernetes and as this image is has been repeated multiple times over multiple uh talks it is the very small but very important building block of Kubernetes itself. And uh here we will be uh seeing what happens when ATCD uh breaks. So is dead, Kubernetes is broken, user is going crazy as what's going on with the cluster. So let's see what are the errors that can cause. So when series stops working the cluster becomes read only any kind of requests for creating or updating won't go through and any kind of API requests will also error out in that scenario and even if it is able to get through the data might not be updated across all the members of the city uh which will cause inconsistency in the data. So to avoid this problem uh Kubernetes and CCD has a very uh well-laidout contract which basically says that Kubernetes depends a lot on CD's underlying uh core logic and functions and this document mainly reinforces on that and makes the documentation and testing of both the projects more robust.

So let's look at the common pitfalls uh that one might run into uh in running their and running and managing their cumulator clusters. So say uh you have VMs to which you have attached 100 or 200 GB of disks and uh you want to run your XCD clusters on that and uh uh you think that you have 200 GB of space but that is not quite it because uh uh the default CD size w
