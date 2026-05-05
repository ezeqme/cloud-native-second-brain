---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Jian Zhu", "Maintainer"]
sched_url: https://kccncchn2025.sched.com/event/1xjzH/project-lightning-talk-simplifying-multi-cluster-integrations-with-ocm-addon-jian-zhu-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Simplifying+Multi-Cluster+Integrations+with+OCM+Addon+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Simplifying Multi-Cluster Integrations with OCM Addon - Jian Zhu, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: China / Hong Kong
- Speakers: Jian Zhu, Maintainer
- Schedule: https://kccncchn2025.sched.com/event/1xjzH/project-lightning-talk-simplifying-multi-cluster-integrations-with-ocm-addon-jian-zhu-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Simplifying+Multi-Cluster+Integrations+with+OCM+Addon+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Simplifying Multi-Cluster Integrations with OCM Addon.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1xjzH/project-lightning-talk-simplifying-multi-cluster-integrations-with-ocm-addon-jian-zhu-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Simplifying+Multi-Cluster+Integrations+with+OCM+Addon+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=APCNu0PgBBs
- YouTube title: Project Lightning Talk: Simplifying Multi-Cluster Integrations with OCM Addon - Jian Zhu, Maintainer
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-simplifying-multi-cluster-integrations-with-ocm/APCNu0PgBBs.txt
- Transcript chars: 3486
- Keywords: add-on, cluster, mechanism, clusters, capabilities, management, framework, registration, access, develop, integrations, easier, across, resources, provides, library, behaviors, deployment

### Resumo baseado na transcript

In the next few minutes I want to show you how OCM makes it easier to build integrations in multicluster environment through its add-on mechanism. Uh, OCM is an opensource CNCF project focused on managing fleets of Kubernetes clusters. So you can focus only on your business logic and uh here is a add-on architecture.

### Excerpt da transcript

Hello everyone and uh thank you for joining this Latin talk. Uh I'm Jujian uh a minister of OCM project. In the next few minutes I want to show you how OCM makes it easier to build integrations in multicluster environment through its add-on mechanism. So what is OCM? Uh, OCM is an opensource CNCF project focused on managing fleets of Kubernetes clusters. It enables end to- end visibility and uh centralized control across your Kubernetes cluster. Uh, with OCM, you can register clusters, distribute workloads and manage resources across both cloud and uh, on-prem clusters from a central hub. So, OCM has many great features, but in this talk, let's focus on the extensible part. How does it serve as an integration point for making Kubernetes capabilities multiclass aware? The answer is addon mechanism. So, OCM provides an open class management. It's a Golan library. By using this library, it lets you uh build customer behaviors like monitoring, uh credential management, scheduling or any other things you want and deploy them as add-ons.

The framework the framework will take care of things like registration deployment house check and status reporting and class level ruling upgrades and so on. So you can focus only on your business logic and uh here is a add-on architecture. It's hub spoke with poor model and there are two flows in the diagram on the right side. Each addon has an addon manager on hub cluster which provides capabilities like deploying the agents on the many cluster and maintaining the status of the agent and the ruling upgrades for the agents. And after the agent is deployed on the manicer, it can do their business uh logic logic locally. And on the left side uh the registration component issue a certificate for the add-on agent to access the hub cluster with requested permissions. So the agent can uh with this the agent with this certificate can access the hub and subscribe configurations and do some reconciles and it also can report their uh healthiness to the hub. So from this we can see to develop an add-on the two main part are first defining what resources need to be deployed on the many cluster and as a add-on agent.

It usually contains a deployment a service count some rules and some rule bindings and the second defining how the agent access the hub and with what permissions. So in fact the main requirement to uh develop addon is to implement these two similar interface defined in the addon framework. But is it possible to make this deve
