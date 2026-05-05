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
themes: ["Community Governance"]
speakers: ["Gabriele Quaresima", "Contributor"]
sched_url: https://kccnceu2026.sched.com/event/2EWIB/project-lightning-talk-five-minutes-by-cloudnativepg-river-gabriele-quaresima-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Five+Minutes+by+CloudNativePG+River+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Five Minutes by CloudNativePG River - Gabriele Quaresima, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Gabriele Quaresima, Contributor
- Schedule: https://kccnceu2026.sched.com/event/2EWIB/project-lightning-talk-five-minutes-by-cloudnativepg-river-gabriele-quaresima-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Five+Minutes+by+CloudNativePG+River+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Five Minutes by CloudNativePG River.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EWIB/project-lightning-talk-five-minutes-by-cloudnativepg-river-gabriele-quaresima-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Five+Minutes+by+CloudNativePG+River+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Cwz7WAOtr6w
- YouTube title: Project Lightning Talk: Five Minutes by CloudNativePG River - Gabriele Quaresima, Contributor
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-five-minutes-by-cloudnativepg-river/Cwz7WAOtr6w.txt
- Transcript chars: 3905
- Keywords: cluster, replicas, declarative, primary, minutes, define, another, management, gabriel, contributor, operator, sandbox, arbitrary, number, instances, common, storage, architecture

### Resumo baseado na transcript

So I am Gabriel Quarisima and I'm a staff engineer inb and also a clonetpg contributor. So it is uh an open-source operator uh designed to manage posgrql workloads on any supported kubernetes cluster. so we have a direct integration with uh Kubernetes API it's our source of truth um we have an high availability capability scale up and down capabilities is uh definition of um an arbitrary number of replicas as we said um also uh we have store rely on Barman cloud currently and we have a cubectl plug-in for class management able to uh retrieve logs um performance with um a lot of stuff and uh we have also a clusteration refencing if we need to debug the posgsql or if you need to switch off the kubernetes cluster to save money on the weekend and uh also we have a lot of most recent features like uh declarative databases and logical replication via declarative uh publication and subscription.

### Excerpt da transcript

Hello everyone, welcome. So I am Gabriel Quarisima and I'm a staff engineer inb and also a clonetpg contributor. And let's spend the next five minutes by the cloud nativep river. So let's start with the answer. Yes, you can run data on kubernetes. How many of you run that on kubernetes? Yeah, not a few. So nice. Do you run a cloud netPG or something else? Some some of you cloud netpg, some of you other thing. Okay. Very very nice. So what is clown netpg? So it is uh an open-source operator uh designed to manage posgrql workloads on any supported kubernetes cluster. is also a CNCF sandbox project applied for also for incubation during the CubeCon uh America the last one. It is an active community of people uh but is also the umbrella of several repositories you can contribute to. So in a nutshell uh CMPG define a a new Kubernetes CRD named cluster. We need another one another meaning for cluster. So uh we represent a posgrsql cluster uh made up of a single primary and an arbitrary number of instances of replicas.

So you can see on the right the cluster CD with a fancy name and also three instances that is yeah the pretty common way to deploy it and also yes the storage the dimension of the storage. So this is the suggested architecture. So basically we have uh a shared nothing architecture with uh three data centers. So basically three worker nodes in three different availability zone. Hopefully we have this distributed uh view topology and we have uh any Kubernetes worker node as its own instance. There will be a primary and the replicas we define the sandbox we define and uh also each one with the with its own local uh persistent volumes and also uh with services we can connect each other. We have uh read only read write services for primary read only uh for replicas and primary read um for replicas sorry and read only read for primary and replicas services and yeah we have a lot of features these are them most uh common so we have a direct integration with uh Kubernetes API it's our source of truth um we have an high availability capability scale up and down capabilities is uh definition of um an arbitrary number of replicas as we said um also uh we have the planets which uh a declarative management of posgressql configuration you you can add in the spec of the CRD a lot of parameters to configure your own posgress and also uh we have backup and recovery system via volume snapshot CRD but also object store rely on Barman cloud currently and we have a cu
