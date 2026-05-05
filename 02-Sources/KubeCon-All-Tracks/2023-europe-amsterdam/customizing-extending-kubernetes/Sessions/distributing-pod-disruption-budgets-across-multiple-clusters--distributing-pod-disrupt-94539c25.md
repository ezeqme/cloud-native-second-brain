---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Illya Chekrygin", "Apple"]
sched_url: https://kccnceu2023.sched.com/event/1HyVE/distributing-pod-disruption-budgets-across-multiple-clusters-illya-chekrygin-apple
youtube_search_url: https://www.youtube.com/results?search_query=Distributing+Pod+Disruption+Budgets+Across+Multiple+Clusters+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Distributing Pod Disruption Budgets Across Multiple Clusters - Illya Chekrygin, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Illya Chekrygin, Apple
- Schedule: https://kccnceu2023.sched.com/event/1HyVE/distributing-pod-disruption-budgets-across-multiple-clusters-illya-chekrygin-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Distributing+Pod+Disruption+Budgets+Across+Multiple+Clusters+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Distributing Pod Disruption Budgets Across Multiple Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVE/distributing-pod-disruption-budgets-across-multiple-clusters-illya-chekrygin-apple
- YouTube search: https://www.youtube.com/results?search_query=Distributing+Pod+Disruption+Budgets+Across+Multiple+Clusters+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2IPf_AyKSsU
- YouTube title: Distributing Pod Disruption Budgets Across Multiple Clusters - Illya Chekrygin, Apple
- Match score: 0.925
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/distributing-pod-disruption-budgets-across-multiple-clusters/2IPf_AyKSsU.txt
- Transcript chars: 25956
- Keywords: policy, disruption, policies, cluster, workload, namespace, federation, essentially, distribute, database, multiple, clusters, eviction, controller, create, built-in, manager, disruptions

### Resumo baseado na transcript

all right that's a good slide to start with so disruption is not so great disruption word comes from Latin disruptors break apart split shatter break to pieces and we generally want to avoid A disruption of things we care about specifically our workloads kubernetes as a container orchestration system lays a solid foundation one comes down to operating high level workloads however kubernetes is not without the problems when dealing with the workload disruption hello my name is Ilya shukrigan today I would like to take a moment to

### Excerpt da transcript

all right that's a good slide to start with so disruption is not so great disruption word comes from Latin disruptors break apart split shatter break to pieces and we generally want to avoid A disruption of things we care about specifically our workloads kubernetes as a container orchestration system lays a solid foundation one comes down to operating high level workloads however kubernetes is not without the problems when dealing with the workload disruption hello my name is Ilya shukrigan today I would like to take a moment to talk to you about disruption in kubernetes and I'm a kubernetes enthusiast we're going to review a type of workload disruption as well as protection mechanism offered by kubernetes when dealing with disruption we will look at the protection mechanism of budget disruption policies or pdbs for short and we'll see where they work where they fall short and finally we'll do a quick introduction and demo of possible alternative solution and discuss changes discuss the challenges along the way kubernetes classifies disruption in two broad categories involuntary unavoidable cases where path can disappear due to various reasons Hardware failures backing up the node let's say we're running cubelet VM failures or VM disappearances let's say cluster administrative can delete VMS or VMS could disappear due to cloud provider or hypervisor failures Kernel Panic Network partition all this could lead to a workload disruption kubernetes at couple of its own reasons cubelet can remove iPads in response to uh resource pressures on the Node and taint manager can remove workloads paths in response to no executane volunteer disruptions are all other cases and again can be subdivided in categories some first category those ones which initiated or consented by the workload owners so we as a workloader workload owner can delete that paths manually through Cube CTL we can do the deployments or controllers which responsible for our parts as well as we can update our deployments which will cause rolling update and all paths will be removed and finally we can use different kinds of automation like horizontal parallel scalar where essentially can result in pad removal due to scale down events another category is caused by cluster administrator or infrastructure owners where class administrator can scale disrupt a workload by draining nodes in order to perform repair or maintenance upgrades on the nodes nodes can also be drained from the cluster when we use in re
