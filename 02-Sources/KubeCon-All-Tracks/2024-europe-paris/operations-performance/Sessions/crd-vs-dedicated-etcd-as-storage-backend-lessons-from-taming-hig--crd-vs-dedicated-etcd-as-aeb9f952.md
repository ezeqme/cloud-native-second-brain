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
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Hemanth Malla", "Datadog", "Marcel Zięba", "Isovalent"]
sched_url: https://kccnceu2024.sched.com/event/1YeOf/crd-vs-dedicated-etcd-as-storage-backend-lessons-from-taming-high-churn-clusters-hemanth-malla-datadog-marcel-zieba-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=CRD+Vs+Dedicated+etcd+as+Storage+Backend+%3A+Lessons+from+Taming+High+Churn+Clusters+CNCF+KubeCon+2024
slides: []
status: parsed
---

# CRD Vs Dedicated etcd as Storage Backend : Lessons from Taming High Churn Clusters - Hemanth Malla, Datadog & Marcel Zięba, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Hemanth Malla, Datadog, Marcel Zięba, Isovalent
- Schedule: https://kccnceu2024.sched.com/event/1YeOf/crd-vs-dedicated-etcd-as-storage-backend-lessons-from-taming-high-churn-clusters-hemanth-malla-datadog-marcel-zieba-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=CRD+Vs+Dedicated+etcd+as+Storage+Backend+%3A+Lessons+from+Taming+High+Churn+Clusters+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre CRD Vs Dedicated etcd as Storage Backend : Lessons from Taming High Churn Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOf/crd-vs-dedicated-etcd-as-storage-backend-lessons-from-taming-high-churn-clusters-hemanth-malla-datadog-marcel-zieba-isovalent
- YouTube search: https://www.youtube.com/results?search_query=CRD+Vs+Dedicated+etcd+as+Storage+Backend+%3A+Lessons+from+Taming+High+Churn+Clusters+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=o_LutIRlv-A
- YouTube title: CRD Vs Dedicated etcd as Storage Backend : Lessons from Taming High Churn Clusters
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/crd-vs-dedicated-etcd-as-storage-backend-lessons-from-taming-high-chur/o_LutIRlv-A.txt
- Transcript chars: 30268
- Keywords: endpoint, cluster, network, actually, celium, clusters, updates, scalability, policies, server, running, slices, identity, control, object, endpoints, changes, behind

### Resumo baseado na transcript

hello everyone uh thanks for joining us so today uh we'll be talking about crd versus dedicated at CD lessons from taming High churn clusters my name is hant I'm an engineer at dayto dog and I'm also a celum cncf maintainer and this is Marcel he works on celium at isovalent and he's also active in kubernetes six scaleability so crd versus KV star so if you're building an application that is kubernetes native or like a controller you have a decision to make if you have some state

### Excerpt da transcript

hello everyone uh thanks for joining us so today uh we'll be talking about crd versus dedicated at CD lessons from taming High churn clusters my name is hant I'm an engineer at dayto dog and I'm also a celum cncf maintainer and this is Marcel he works on celium at isovalent and he's also active in kubernetes six scaleability so crd versus KV star so if you're building an application that is kubernetes native or like a controller you have a decision to make if you have some state that you want to store you have a decision to make so do you use crds to store that data or do you use a dedicated KV store to store that data so in addition to the total volume that you want to store your data access patterns should also influence that decision right so in this talk we'll get into some details on some of the decisions celium had to make right so we'll discuss quickly some some aspects of kubernetes scalability and how kubernetes scalability impacts different features in celium and some of the current state and some of the options that exist in celium today to help you and how the road ahead looks like and some of the lessons we learned uh along the way so with that I'll let Marcel talk about kubernetes scalability okay so let's start talking about kubernetes scalability so usually when you think about kubernetes scalability what you have in mind is like what's the number of nodes right well wrong like scalability is not just the number of nodes when I think about scalability of kubernetes um it's important to think about multiple Dimensions um so number of nodes is just one dimension that you should care about when thinking about scalability and like the next thing that usually comes up to mind is the number of PODS right but this is not all so the question becomes like what are those other dimensions that we should care about when we are operating kubernetes cluster at scale so now we will talk about two different kubernetes features that probably all of you are familiar with and try to think about like how they affect scalability of kubernetes so let's start with kubernetes Services um so the idea is quite simple you define service the service gets virtual IP or cluster IP assigned and then you have bunch of backend pods right so um from client perspective when you want to connect to to the service H what happens is that you know you initiate the connection to to this virtual IP um but you need to have some kind of proxy and usually it's just Cube proxy that und
