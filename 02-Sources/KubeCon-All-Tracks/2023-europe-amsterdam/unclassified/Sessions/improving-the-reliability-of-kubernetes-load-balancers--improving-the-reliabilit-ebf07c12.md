---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Alexander Constantinescu", "Confluent"]
sched_url: https://kccnceu2023.sched.com/event/1Hyc0/improving-the-reliability-of-kubernetes-load-balancers-alexander-constantinescu-confluent
youtube_search_url: https://www.youtube.com/results?search_query=Improving+the+Reliability+of+Kubernetes+Load+Balancers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Improving the Reliability of Kubernetes Load Balancers - Alexander Constantinescu, Confluent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Constantinescu, Confluent
- Schedule: https://kccnceu2023.sched.com/event/1Hyc0/improving-the-reliability-of-kubernetes-load-balancers-alexander-constantinescu-confluent
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+the+Reliability+of+Kubernetes+Load+Balancers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Improving the Reliability of Kubernetes Load Balancers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyc0/improving-the-reliability-of-kubernetes-load-balancers-alexander-constantinescu-confluent
- YouTube search: https://www.youtube.com/results?search_query=Improving+the+Reliability+of+Kubernetes+Load+Balancers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UvxEvua4zkw
- YouTube title: Improving the Reliability of Kubernetes Load Balancers - Alexander Constantinescu, Confluent
- Match score: 0.835
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/improving-the-reliability-of-kubernetes-load-balancers/UvxEvua4zkw.txt
- Transcript chars: 21903
- Keywords: balancer, essentially, health, balancers, traffic, cluster, specifically, connection, important, ingress, whenever, running, happens, provider, external, policy, mentioned, within

### Resumo baseado na transcript

so hi everyone my name is Alexander constantinescu I'm working as a software engineer for confluent and I'm going to be presenting essentially a Year's worth of work that me and my company and the Upstream kubernetes community have been working on with the goal of improving the reliability of kubernetes load balancers um quick note about me and my company essentially what I'm going to be presenting is kind of a niche problem that I hope that many of you have never experienced before and that you might however

### Excerpt da transcript

so hi everyone my name is Alexander constantinescu I'm working as a software engineer for confluent and I'm going to be presenting essentially a Year's worth of work that me and my company and the Upstream kubernetes community have been working on with the goal of improving the reliability of kubernetes load balancers um quick note about me and my company essentially what I'm going to be presenting is kind of a niche problem that I hope that many of you have never experienced before and that you might however experience in the future should you run a lot of load balancers in your clusters and when I mean a lot of load balancers I'm talking about roughly the same amount of load balancers as you would have nodes this is essentially kind of a scalability problem that arises during operations with services so I'm going to begin by presenting a bit of the background that exists within this problem space the problem in itself the solution that we've been working on and kind of some future work that we have on the Whiteboard for the future so so to begin with kubernetes load balancers I think it's good to be a bit more specific because the term load balancer in an ecosystem such as kubernetes can mean a lot of different things so to begin with it's doesn't have any relation to do with bare metal nodes which could lead to believe that it would have a relation to metal lb for those of you who are aware of that project it doesn't have anything to do with the Ingress class or any of the Gateway API that has been presented here at kubecon either so specifically what this aims at solving is a problem around the core V1 service and specifically when you specify one which is of type load balancer moreover this is also kind of tailored towards clusters that are running on the public Cloud so essentially load balancers that get provisioned by the kubernetes control plane and a term that I think is important to remember at least for the later uh part of this talk is the term connection draining I'm going to get back to what that concretely means later on but I think it's a good topic to have already in your minds off the bat so how do V1 service load balancers work today so the first part that I'm going to be presenting is kind of the general load balancer configuration and what happens whenever you create a service of type load balancer on a kubernetes cluster so these is kind of the general schematics of things and these are the main core kubernetes components that intera
