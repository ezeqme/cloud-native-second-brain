---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["AI ML", "Storage Data", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Laurent Bernaille", "Antoine Tollenaere", "Datadog"]
sched_url: https://kccnceu2024.sched.com/event/1YeOE/connecting-millions-of-containers-spanning-dozens-of-clusters-laurent-bernaille-antoine-tollenaere-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Connecting+Millions+of+Containers+Spanning+Dozens+of+Clusters+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Connecting Millions of Containers Spanning Dozens of Clusters - Laurent Bernaille & Antoine Tollenaere, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Storage Data]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Laurent Bernaille, Antoine Tollenaere, Datadog
- Schedule: https://kccnceu2024.sched.com/event/1YeOE/connecting-millions-of-containers-spanning-dozens-of-clusters-laurent-bernaille-antoine-tollenaere-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Connecting+Millions+of+Containers+Spanning+Dozens+of+Clusters+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Connecting Millions of Containers Spanning Dozens of Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOE/connecting-millions-of-containers-spanning-dozens-of-clusters-laurent-bernaille-antoine-tollenaere-datadog
- YouTube search: https://www.youtube.com/results?search_query=Connecting+Millions+of+Containers+Spanning+Dozens+of+Clusters+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yzhwISOGhVI
- YouTube title: Connecting Millions of Containers Spanning Dozens of Clusters
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/connecting-millions-of-containers-spanning-dozens-of-clusters/yzhwISOGhVI.txt
- Transcript chars: 32590
- Keywords: clusters, cluster, traffic, actually, course, balancer, multiple, clients, storage, client, running, single, limits, applications, another, discovery, pretty, providers

### Resumo baseado na transcript

hello everyone uh Welcome to our talk um this is Lauren I'm Anan we're both engineers at data dog and today we are going to talk about networking and service Discovery uh so I'll start with a few words about data dog for those that don't know us uh we are an observability product um with a bunch of Integrations uh we have quite a large customer base already and because of that um we have a pretty big infra in order to store and create all this data Lauren see a single IP that's extremely convenient because they don't have to care about the number of back ends the fact that this back end will scale up and down the fact that sometimes it will be unreachable everything is is totally masked to the two main ones in kubernetes which are load balancer Services first and and then we'll talk about another one I won't spoil you so load balancer Services allows you to expose Services across clusters so the only difference from the slide we had before from the step we had before in that in this case we have the intake workload running on one cluster and the storage workload working on another one so they can't rely on standard Services when you use load balancer Services what's going to happen is your client workload is going to do any GS query but instead of getting the IP of virtual IP in the cluster or the IP of the Pod is going to get the IP of a load balancer back and the traffic...

### Excerpt da transcript

hello everyone uh Welcome to our talk um this is Lauren I'm Anan we're both engineers at data dog and today we are going to talk about networking and service Discovery uh so I'll start with a few words about data dog for those that don't know us uh we are an observability product um with a bunch of Integrations uh we have quite a large customer base already and because of that um we have a pretty big infra in order to store and create all this data Lauren is going to start by introducing a bit more about our infra and that's going to be useful for the rest of the talk yes before we dive into the purpose of the talk which is service Discovery to give you context and the constraints we have uh we're going to present um a quick history of our infro so back in 2018 data dog was running in a single region on AWS and everything was managed with chef and Capistrano as we were reaching thousands of node they started to be a challenge in addition we had new customers in Europe we wanted us to send data to Europe and this got us the first one of the first big infra project we did which was creating a new region on a new provider and because we were seeing limits with Chef we started to deploy with kuber instead of uh Chef in Europe as you can see on this slide we also started to do this in in the initial region in the US but only a small part of it was running on kuties at the time fast forward to 2024 this is far more complex right we're running in six different regions on three different providers everything in running in kubernetes and and we run millions of containers what's important for this talk is we run thousand to tens of thousands of nodes in each region which means of course because of limits in kubernetes that we need to have multiple clusters in regions and in some regions we have dozens and what really matters for what we're going to discuss today are these three things the fact that we're 100% kubernetes that we run on three different providers and that regions can have up to dozens of clusters if we zoom in into a region because we have many clusters we need to assign workloads to clusters and in this very simple example here we can we can see three different clusters one that is dedicated to metrix application one that is dedicated to logs application and a third one that is dedicated to shared services such as Kafka or Cassandra this looks simple enough but for reliability in scalability reasons we tend to deploy stateless workloads in zonal clust
