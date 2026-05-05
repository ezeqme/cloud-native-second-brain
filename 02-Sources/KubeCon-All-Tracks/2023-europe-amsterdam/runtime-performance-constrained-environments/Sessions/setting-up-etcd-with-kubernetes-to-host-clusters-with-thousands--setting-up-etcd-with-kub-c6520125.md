---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Storage Data", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Marcel Zięba", "Isovalent", "Laurent Bernaille", "Datadog"]
sched_url: https://kccnceu2023.sched.com/event/1Hycg/setting-up-etcd-with-kubernetes-to-host-clusters-with-thousands-of-nodes-marcel-zieba-isovalent-laurent-bernaille-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Setting+up+Etcd+with+Kubernetes+to+Host+Clusters+with+Thousands+of+Nodes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Setting up Etcd with Kubernetes to Host Clusters with Thousands of Nodes - Marcel Zięba, Isovalent & Laurent Bernaille, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Storage Data]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marcel Zięba, Isovalent, Laurent Bernaille, Datadog
- Schedule: https://kccnceu2023.sched.com/event/1Hycg/setting-up-etcd-with-kubernetes-to-host-clusters-with-thousands-of-nodes-marcel-zieba-isovalent-laurent-bernaille-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Setting+up+Etcd+with+Kubernetes+to+Host+Clusters+with+Thousands+of+Nodes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Setting up Etcd with Kubernetes to Host Clusters with Thousands of Nodes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hycg/setting-up-etcd-with-kubernetes-to-host-clusters-with-thousands-of-nodes-marcel-zieba-isovalent-laurent-bernaille-datadog
- YouTube search: https://www.youtube.com/results?search_query=Setting+up+Etcd+with+Kubernetes+to+Host+Clusters+with+Thousands+of+Nodes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_Zhf_iJMqwE
- YouTube title: Setting up Etcd with Kubernetes to Host Clusters with Thousands of Nodes - M Zięba & L Bernaille
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/setting-up-etcd-with-kubernetes-to-host-clusters-with-thousands-of-nod/_Zhf_iJMqwE.txt
- Transcript chars: 38261
- Keywords: server, cluster, actually, priority, resource, basically, version, control, events, running, course, clusters, requests, request, default, servers, components, controller

### Resumo baseado na transcript

very nice to be here with you today and it's it's really nice to see so many of you are interested in hcd and control plane performance So today we're going to talk about HD performance but in a much more General way about the performance of control planes and interactions between API servers and nhcd and I'm Lauren Bernard I work at datadog I'm Martin from isobond and so to get started we're going to talk about scaling the control planes and one of the reason I can talk can so let's get back to our to our incident so we know that the problem was coming from new schools right and because we saw the number of requests with these calls and the next step was to understand which application was making business goals and on our cluster we we use all these logs extensively to know what's happening in the cluster and all these logs are very helpful because I can give you an idea what what's happening in your cluster you can see all the queries yeah also I would add that you know like for large clusters um the kubernetes actually recommends 30 pots per note like the maximum supported is 110 so with 500 you know like anything can happen basically hello question here so assuming that we keep the limit of 120 parts per node and we still have a large cluster and even we try to go with the best practices that you presented uh what is the bottle like how much can we scale a city database...

### Excerpt da transcript

very nice to be here with you today and it's it's really nice to see so many of you are interested in hcd and control plane performance So today we're going to talk about HD performance but in a much more General way about the performance of control planes and interactions between API servers and nhcd and I'm Lauren Bernard I work at datadog I'm Martin from isobond and so to get started we're going to talk about scaling the control planes and one of the reason I can talk about it is because at datadog we run a large numbers a large number of very large community clusters to give you an idea we have hundreds of clusters from like between 1 000 to 6000 nodes and as you reach like thousands of notes in a cluster you start to find interesting challenges and we started like everybody right we started with a very simple control plane where you have a single master I'm sure you're all familiar with these components where you have a single node where you have hcd which is responsible for storing the resource in your cluster you have the API server which is responsible for the abuse the kubernetes apis and then you have two core controllers the scheduler which is responsible for scheduling workloads and nodes and controllers which are running very reconcile loops and making sure that the state of the cluster is what what's expected and of course we have all the components interacting with the Masters uh so you start with this but of course this is not very resilient right if you lose uh the node running all these components you lose your cluster so the next step is usually to have multiple Masters right so exactly the same setup but instead of having a single Master with our stream Masters running the same components this slide is a bit misleading though because all these components are stateless except for LCD because this is the data store of the cluster so I have three LCD boxes but it's actually an SD cluster and you can see here that all the components are stateless exact entity which is stateful and so it's kind of weird that you designed this way so a very common optimization is to actually get hcd outside of the Masters and so the next optimization is to do it this way right so you have a net City cluster where you have a utility nodes and then you have your Masters when you're on API servers controllers and scheduler they're the next thing that's interesting which is if you're familiar with kubernetes you know that schedulers and controllers are actually r
