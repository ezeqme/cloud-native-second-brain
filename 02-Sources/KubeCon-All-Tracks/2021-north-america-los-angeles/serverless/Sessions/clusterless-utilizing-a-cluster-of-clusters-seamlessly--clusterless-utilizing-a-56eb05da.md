---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Serverless"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Fei Guo", "Alibaba", "Chris Hein", "Apple"]
sched_url: https://kccncna2021.sched.com/event/lV31/clusterless-utilizing-a-cluster-of-clusters-seamlessly-fei-guo-alibaba-chris-hein-apple
youtube_search_url: https://www.youtube.com/results?search_query=Clusterless+-+Utilizing+a+Cluster+of+Clusters+Seamlessly+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Clusterless - Utilizing a Cluster of Clusters Seamlessly - Fei Guo, Alibaba & Chris Hein, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Serverless]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Fei Guo, Alibaba, Chris Hein, Apple
- Schedule: https://kccncna2021.sched.com/event/lV31/clusterless-utilizing-a-cluster-of-clusters-seamlessly-fei-guo-alibaba-chris-hein-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Clusterless+-+Utilizing+a+Cluster+of+Clusters+Seamlessly+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Clusterless - Utilizing a Cluster of Clusters Seamlessly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV31/clusterless-utilizing-a-cluster-of-clusters-seamlessly-fei-guo-alibaba-chris-hein-apple
- YouTube search: https://www.youtube.com/results?search_query=Clusterless+-+Utilizing+a+Cluster+of+Clusters+Seamlessly+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iXRXhN5EKWQ
- YouTube title: Clusterless - Utilizing a Cluster of Clusters Seamlessly - Fei Guo, Alibaba & Chris Hein, Apple
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/clusterless-utilizing-a-cluster-of-clusters-seamlessly/iXRXhN5EKWQ.txt
- Transcript chars: 27494
- Keywords: cluster, clusters, workloads, actually, scheduling, single, scheduler, worker, workload, scheduled, control, across, deploy, objects, virtual, support, multi-cluster, architecture

### Resumo baseado na transcript

so hi everybody uh welcome to our talk about clusterless architectures uh this is a new design that's coming out of the virtual cluster space and it allows you to utilize clusters of clusters uh seamlessly to run workloads wherever wherever you need to uh faye and i uh we'll be talking to you about this and we're both the maintainers for the project along with some other folks um faye works at alibaba and i work at apple so uh why we're talking about this and why this is

### Excerpt da transcript

so hi everybody uh welcome to our talk about clusterless architectures uh this is a new design that's coming out of the virtual cluster space and it allows you to utilize clusters of clusters uh seamlessly to run workloads wherever wherever you need to uh faye and i uh we'll be talking to you about this and we're both the maintainers for the project along with some other folks um faye works at alibaba and i work at apple so uh why we're talking about this and why this is important so one of the things that as you start to use kubernetes you start to realize that when you started you initially started with at least a single cluster and you started to build out your architectures and you and you deployed workloads into that single environment you started to see some problems this is something that i feel like everybody experiences in their kubernetes journey and so where folks usually go is they turn to a multi-cluster management style and the whole idea behind this is it allows you to actually scale out your architecture so uh taking from a single cluster which has scale targets uh that are defined by sig scalability um and moving that into how do we make it so that we could run you know 4x the type of capacity that we currently have and and being able to do that and scale your workloads horizontally gets somewhat difficult uh on top of that uh customers really want to start to look at things like how to how to deploy and run workloads in specific regions and areas where their data might be located um if you're thinking like bachelor workloads where you're processing a lot of data you don't want to run that from completely opposite ends of uh the country for example uh in this environment you also get to a place where you're really taking you're bringing in a lot more compute resources and everything gets more difficult to actually manage and aggregate across those so what you end up doing is start to look at that multi-cluster space and then bring in things like uh aha strategies how would you actually increase the availability of your workloads how do you set up regions that you can actually fail over into uh when something goes wrong uh i imagine everybody here has experienced issues with etcd having key space problems and you get a corrupted key and you end up with an entire cluster that just doesn't function anymore and how do you actually recover for those things on top of this we get into a new world of how do you actually build out the security comp
