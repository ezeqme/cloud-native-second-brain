---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Andrea Tosatto", "James Munnelly", "Apple"]
sched_url: https://kccncna2025.sched.com/event/27Fc2/building-a-kubernetes-native-experience-for-your-multi-cluster-fleet-andrea-tosatto-james-munnelly-apple
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Kubernetes-native+Experience+for+Your+Multi-cluster+Fleet+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building a Kubernetes-native Experience for Your Multi-cluster Fleet - Andrea Tosatto & James Munnelly, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Andrea Tosatto, James Munnelly, Apple
- Schedule: https://kccncna2025.sched.com/event/27Fc2/building-a-kubernetes-native-experience-for-your-multi-cluster-fleet-andrea-tosatto-james-munnelly-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Kubernetes-native+Experience+for+Your+Multi-cluster+Fleet+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building a Kubernetes-native Experience for Your Multi-cluster Fleet.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fc2/building-a-kubernetes-native-experience-for-your-multi-cluster-fleet-andrea-tosatto-james-munnelly-apple
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Kubernetes-native+Experience+for+Your+Multi-cluster+Fleet+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=khUixjjwhAQ
- YouTube title: Building a Kubernetes-native Experience for Your Multi-cluster Fl... Andrea Tosatto & James Munnelly
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-a-kubernetes-native-experience-for-your-multi-cluster-fleet/khUixjjwhAQ.txt
- Transcript chars: 32420
- Keywords: cluster, multicluster, object, essentially, server, version, workload, multiq, resource, provide, across, platform, particular, specific, marker, resources, clusters, controller

### Resumo baseado na transcript

Thank you so much for coming uh to mine and James call talk about like uh our experience experiments with API server. Um unfortunately James is not going to be here like but I'll try to do my best to run you through what we've been playing with uh lately in the API server with a goal of like providing uh users with a native multicluster experience. to scale and and reliably and kind of like platform team found themselves like kind of like wrestling around like this software to protect essentially at CD like from the load generated from the uh users. uh there were there are very good and well doumented like best practices in the community around autoscale kubernetes for instance for large cluster that is to separate events which have a high churn rate from other resources into a separated CD cluster um h every CRD has strong validation in order to prevent like situation where like serialization began becomes again like a problem with memory. um in the most recent like Kubernetes releases like the community has been doing a fantastic job in kind of tackling some of this fundamental problem in the API server design and in particular the fact that the API server itself doesn't have like strong

### Excerpt da transcript

Thank you so much for coming uh to mine and James call talk about like uh our experience experiments with API server. Um unfortunately James is not going to be here like but I'll try to do my best to run you through what we've been playing with uh lately in the API server with a goal of like providing uh users with a native multicluster experience. Um so uh again this talk for the people that have seen maybe last year talk about workspaces from me and James is very much like a kind of continuation of this kind of like research in the API server that we've been doing. Um I like workspaces which was focus on multi-tenency. What we're going to be talking about today is more aggregation of resources across clusters and you will also like kind of see during the talk like some of the motivation for us like to build such features and I'll try to leave like five minutes at the very end like for a question. I've been told that you need to go here in the line. Uh but yeah otherwise we can just meet uh in the hallway truck I guess.

So to begin with the talk I really want to start talking about scalability. Uh the reason why is that for a very long time like for customer or platform team implementing Kubernetes like um the API server has been like a very complicated application to scale. This is because when you start exposing the Kubernetes API to your users and you don't control the interaction there with the API, uh the API server itself like for a long time lack some core features in order like to kind of enable it to scale and and reliably and kind of like platform team found themselves like kind of like wrestling around like this software to protect essentially at CD like from the load generated from the uh users. uh there were there are very good and well doumented like best practices in the community around autoscale kubernetes for instance for large cluster that is to separate events which have a high churn rate from other resources into a separated CD cluster um h prefer like binary encoding via protobuff of like uh like the objects that are returned like from uh the API server in order to reduce like memory utilization and also like drive really like work with your internal customer in order to make sure that every CRD has strong validation in order to prevent like situation where like serialization began becomes again like a problem with memory.

um in the most recent like Kubernetes releases like the community has been doing a fantastic job in kind of ta
