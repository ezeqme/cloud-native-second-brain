---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Joe Nathan Abellard", "Domain Owner"]
sched_url: https://kccnceu2026.sched.com/event/2EFxe/project-lightning-talk-multi-cluster-orchestration-system-karmada-updates-and-use-cases-joe-nathan-abellard-domain-owner
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Orchestration+System%3A+Karmada+Updates+And+Use+Cases+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Multi-Cluster Orchestration System: Karmada Updates And Use Cases - Joe Nathan Abellard, Domain Owner

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joe Nathan Abellard, Domain Owner
- Schedule: https://kccnceu2026.sched.com/event/2EFxe/project-lightning-talk-multi-cluster-orchestration-system-karmada-updates-and-use-cases-joe-nathan-abellard-domain-owner
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Orchestration+System%3A+Karmada+Updates+And+Use+Cases+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Multi-Cluster Orchestration System: Karmada Updates And Use Cases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxe/project-lightning-talk-multi-cluster-orchestration-system-karmada-updates-and-use-cases-joe-nathan-abellard-domain-owner
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Cluster+Orchestration+System%3A+Karmada+Updates+And+Use+Cases+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IlXsx4lMrQU
- YouTube title: Project Lightning Talk: Multi-Cluster Orchestration System: Karmada Updates A... Joe Nathan Abellard
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-multi-cluster-orchestration-system-karmada-upda/IlXsx4lMrQU.txt
- Transcript chars: 3784
- Keywords: across, clusters, multicluster, orchestration, bloomberg, kamata, platform, entire, kamada, lightning, multi-cluster, currently, started, general, workloads, become, management, enables

### Resumo baseado na transcript

I work at Bloomberg as a senior software engineer and I'm also one of the core owners of the comma project. Um and in this lightning talk I'll provide you with a high level overview of the project. In the control plane, the central component um here labeled as comma API server is just the standard cube API server which enables seamless integration with the existing Kubernetes tool chain. um global resource view which provides a unified entry point to query resources across your entire fleet of clusters as well as multi-cluster service discovery. So tomorrow I'll be doing a talk on how we executed a zero downtime migration from the now retiring engineext project to multicluster Kubernetes platform built at top commada um at Bloomberg. Um and then we're going to have a talk by one of the tenants of that platform um for running disaster resilient Chino on multicluster Kubernetes powered by Kada um in gateway.

### Excerpt da transcript

Welcome everyone. I'm Joe. I work at Bloomberg as a senior software engineer and I'm also one of the core owners of the comma project. Um and in this lightning talk I'll provide you with a high level overview of the project. But before I begin um who here has heard or currently is using Kamata. Oh nice. Okay. So let's get started. Um so as organizations scale AI general compute um and analytics work workloads across um clusters, regions and clouds uh multicluster orchestration has become a critical building block of the modern um platform engineering stack. And this is exactly where Kamata short for Kubernetes or comes into the picture. It's a CNCF project for um Kubernetes native multicluster management that enables you to run your workloads across your entire fleet of clusters. Um architecturally a comma setup looks very similar to that of a Kubernetes cluster setup. It's basically a control plane that is joined to a set of um member clusters. And Kata is cloud agnostic. So those clusters could either belong in your private cloud on prem or across multiple um cloud providers.

In the control plane, the central component um here labeled as comma API server is just the standard cube API server which enables seamless integration with the existing Kubernetes tool chain. And instead of cubeuler, you have comma scheduler responsible for making intelligent placement decisions across your entire fleet um of clusters. Um some features that are of note are obviously very powerful multicluster management um very advanced um policies to meet different type of scheduling requirements and scenarios um crosscluster application failover um to handle failover of applications and disaster scenarios. Um unified authentication authorization and auditing. um global resource view which provides a unified entry point to query resources across your entire fleet of clusters as well as multi-cluster service discovery. Um the project was published as open source in 2021 we became a CNCF sandbox project that same year. Um in 2023 we became a CNCF incubating project. Um and last year we applied to become a CNCF graduate project and we're currently on track to be a graduate project this year.

Um we have a very fast growing and vibrant community with sustained contributions from contributors across many different companies and the project itself has been widely adopted. Um, on here I have a list of public adapters in production. And some of the companies that you may recognize on her
