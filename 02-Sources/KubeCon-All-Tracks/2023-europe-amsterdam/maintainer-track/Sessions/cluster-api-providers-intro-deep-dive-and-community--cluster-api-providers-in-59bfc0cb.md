---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Ashutosh Kumar", "Ankita Swamy", "VMware", "Richard Case", "SUSE"]
sched_url: https://kccnceu2023.sched.com/event/1HyUb/cluster-api-providers-intro-deep-dive-and-community-ashutosh-kumar-ankita-swamy-vmware-richard-case-suse
youtube_search_url: https://www.youtube.com/results?search_query=Cluster+API+Providers%3A+Intro%2C+Deep+Dive%2C+and+Community%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cluster API Providers: Intro, Deep Dive, and Community! - Ashutosh Kumar & Ankita Swamy, VMware; Richard Case, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ashutosh Kumar, Ankita Swamy, VMware, Richard Case, SUSE
- Schedule: https://kccnceu2023.sched.com/event/1HyUb/cluster-api-providers-intro-deep-dive-and-community-ashutosh-kumar-ankita-swamy-vmware-richard-case-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Cluster+API+Providers%3A+Intro%2C+Deep+Dive%2C+and+Community%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cluster API Providers: Intro, Deep Dive, and Community!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUb/cluster-api-providers-intro-deep-dive-and-community-ashutosh-kumar-ankita-swamy-vmware-richard-case-suse
- YouTube search: https://www.youtube.com/results?search_query=Cluster+API+Providers%3A+Intro%2C+Deep+Dive%2C+and+Community%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QA4OhqLKJn4
- YouTube title: Cluster API Providers: Intro, Deep Dive, and Community!- Ashutosh Kumar & Ankita Swamy, Richard Case
- Match score: 0.793
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cluster-api-providers-intro-deep-dive-and-community/QA4OhqLKJn4.txt
- Transcript chars: 26369
- Keywords: cluster, provider, machine, create, infrastructure, resource, providers, network, actually, control, created, identity, machines, resources, configuration, specific, workload, support

### Resumo baseado na transcript

welcome to to the cluster API provider talk um I'm ashitosh and I work as an engineer at FM on cluster life cycle team uh I would like to invite Anita and Richard to introduce themsel and then we'll go forward in the talk hey folks uh I'm an I have been working with with VM for past two years and I have been an active contributor in cluster API and as provider I am also acting as a maintainer for cluster API provider AWS Richard you want to introduce

### Excerpt da transcript

welcome to to the cluster API provider talk um I'm ashitosh and I work as an engineer at FM on cluster life cycle team uh I would like to invite Anita and Richard to introduce themsel and then we'll go forward in the talk hey folks uh I'm an I have been working with with VM for past two years and I have been an active contributor in cluster API and as provider I am also acting as a maintainer for cluster API provider AWS Richard you want to introduce I have one my name is Richard I work as an engineer at Susa uh specifically on Rancher and cluster provisioning I'm also one of the maintainers of the cluster API providers for uh AWS gcp micro VM and RK to okay so this is what we're covering in the agenda uh we are going to see a quick intro of cluster API we'll see how cluster API provider works and then we'll give updates on cluster API provider what's going on recently and what's in the road map but before we go further into this can I see a raise of hands on how many people are using cluster API so far like okay that's great and how many of you have like recently learned about cluster API like any new audience here oh that's cool okay so with this I'll hand over to Anita to give us intro on cluster API an okay so let's get started then so the project was originally started based on the motivation that the cluster life cycle management is difficult historically there have been many provisioning tools uh depending on where do you want to create your cluster and there hasn't been much of consistencies in the user experience so cluster API is a solution for managing and automating the life cycle of your actual kubernetes cluster using the kuet style declarative apis cluster API is like a virtual kuet is in a box tool that provides you all the tools and components you need to assemble your own kuet cluster it's like a DIY project for you the kues en enthusiasts with endless possibilities of the cluster creativity so the cluster API with the help of its providers will create all the necessary supporting infrastructure that you may need so things like virtual machines load balances and network configurations and it will also handle the bootstrapping and configuration of the kuet cluster on the infrastructure so as mentioned before this is done using kuet style apis in a declarative way like we are used to do with the managing workload clusters inside the clust uh workloads within a cluster so extensibility is cod to Cluster API it should be relatively easy to ad
