---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Multi-tenancy"
themes: ["Kubernetes Core"]
speakers: ["Joshua Packer", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182IA/multicluster-kubernetes-management-made-easy-with-open-cluster-management-joshua-packer-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Multicluster+Kubernetes+Management+Made+Easy+With+Open+Cluster+Management+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Multicluster Kubernetes Management Made Easy With Open Cluster Management - Joshua Packer, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Joshua Packer, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182IA/multicluster-kubernetes-management-made-easy-with-open-cluster-management-joshua-packer-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Multicluster+Kubernetes+Management+Made+Easy+With+Open+Cluster+Management+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Multicluster Kubernetes Management Made Easy With Open Cluster Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182IA/multicluster-kubernetes-management-made-easy-with-open-cluster-management-joshua-packer-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Multicluster+Kubernetes+Management+Made+Easy+With+Open+Cluster+Management+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pohOtvPu_3c
- YouTube title: Multicluster Kubernetes Management Made Easy With Open Cluster Management - Joshua Packer, Red Hat
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/multicluster-kubernetes-management-made-easy-with-open-cluster-managem/pohOtvPu_3c.txt
- Transcript chars: 23353
- Keywords: cluster, clusters, manage, managed, controllers, management, running, server, placement, control, add-on, resource, inventory, created, account, controller, namespace, status

### Resumo baseado na transcript

hello my name is Joshua Packer and I'm a developer at Red Hat I'm excited to be here with you today at kubecon 2022 to talk about the open dash cluster-management.io Community I've been involved in this community since its Inception and now at its present status as a cncf Sandbox project its core focus is on multi-clustered fleet scenarios while being Cloud vendor agnostic at its core this project enables you to inventory your clusters distribute work while being vendor neutral again it works with almost any cncf compliant

### Excerpt da transcript

kubecon plus Cloud native North America 2022. hello my name is Joshua Packer and I'm a developer at Red Hat I'm excited to be here with you today at kubecon 2022 to talk about the open dash cluster-management.io Community I've been involved in this community since its Inception and now at its present status as a cncf Sandbox project its core focus is on multi-clustered fleet scenarios while being Cloud vendor agnostic at its core this project enables you to inventory your clusters distribute work while being vendor neutral again it works with almost any cncf compliant distro with this inventory of Fleet though you can extend your day to management using our policy configuration and application add-ons that are also a part of the community you can still build your own add-ons though as well and distribute those out into your Fleet as needed there will be a separate presentation covering both these areas of policy and application in the kubecon virtual presentation catalog but in the next 30 minutes I'm going to do a demo of how to get started with open classstar management and talk about some of the future work that's being done lastly this is a community of many and our governance board reflects that as well as we have new developers and or contributing companies joining every day and so I encourage you to come visit us at open dash cluster Dash management dot IO which is the page you see now in the presentation or in our GitHub organization where you can actually contribute and so again open Dash starter desk management Dash IO is the organization there's the ocm repo that has details our community repo where you can find the schedule for our weekly calls as well as our API definition for that inventory control and our enhancement repository if you'd like to submit an enhancement and or contribute in general to the project so over the next 25 minutes now we will dive into open cluster management and take a look let's get started all right let's dig a Little Deeper let's look at how open cluster management works with your Fleet of clusters when we look at this diagram we see the layout of how open cluster management is deployed within your Fleet we start with what is a hub cluster this is a single entry point where you're able to manage your Fleet which could be one two three or many clusters on that Hub cluster we run the registration controller which takes care of making sure we have the inventory we also run controllers like placement and work these all
