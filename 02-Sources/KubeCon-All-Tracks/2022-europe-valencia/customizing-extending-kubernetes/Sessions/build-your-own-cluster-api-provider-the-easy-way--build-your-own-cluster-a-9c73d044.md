---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Anusha Hegde", "VMware", "Richard Case", "Weaveworks"]
sched_url: https://kccnceu2022.sched.com/event/ytp2/build-your-own-cluster-api-provider-the-easy-way-anusha-hegde-vmware-richard-case-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Build+Your+Own+Cluster+API+Provider+the+Easy+Way+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Build Your Own Cluster API Provider the Easy Way - Anusha Hegde, VMware & Richard Case, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Anusha Hegde, VMware, Richard Case, Weaveworks
- Schedule: https://kccnceu2022.sched.com/event/ytp2/build-your-own-cluster-api-provider-the-easy-way-anusha-hegde-vmware-richard-case-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Build+Your+Own+Cluster+API+Provider+the+Easy+Way+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Build Your Own Cluster API Provider the Easy Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytp2/build-your-own-cluster-api-provider-the-easy-way-anusha-hegde-vmware-richard-case-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Build+Your+Own+Cluster+API+Provider+the+Easy+Way+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HSdgmcAAXa8
- YouTube title: Build Your Own Cluster API Provider the Easy Way - Anusha Hegde, VMware & Richard Case, Weaveworks
- Match score: 0.766
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/build-your-own-cluster-api-provider-the-easy-way/HSdgmcAAXa8.txt
- Transcript chars: 25446
- Keywords: provider, cluster, infrastructure, create, resource, machine, controller, providers, control, actually, resources, bootstrap, creating, builder, podman, machines, operator, reconcile

### Resumo baseado na transcript

last year cluster api has been used rapidly and we have seen a lot of usage and there are plethora of cluster api providers for you to choose from but what if none of the existing providers suit your use case in this conversation we will learn about the different provider types and also we need to evaluate whether we really need to write a new provider if your answer is yes we can walk you through how to build your own classroom provider over to my co-presenter hi everyone

### Excerpt da transcript

last year cluster api has been used rapidly and we have seen a lot of usage and there are plethora of cluster api providers for you to choose from but what if none of the existing providers suit your use case in this conversation we will learn about the different provider types and also we need to evaluate whether we really need to write a new provider if your answer is yes we can walk you through how to build your own classroom provider over to my co-presenter hi everyone my name is richard i'm a principal engineer at weaveworks i'm currently one of the maintainers of the aws and micro vm cluster api providers this talk was uh how to build your own one the easy way it's turning into how to do it the hard way um so we'll see what we can do so just a recap on what cluster api provider is so it was originally designed with the the premise that actually provisioning clusters and it's that the life cycle of those classes is actually difficult um there's been many many ways to provision clusters depending on your target environment and very little is being done to provide consistency from a from a user experience point of view and this is really where cluster api comes into it so if you've been building or provisioning clusters for a very very long time i'm sure you you've played with things like papanetti's cops and various other things so cluster api provider tries to make that experience and the way that you provision clusters consistent and so it does this by having this concept of providers and providers are essentially the parts that do the infrastructure or environment specific operations and they they talk nicely with core cluster api and you perform your operations against the core cluster api types and so it handles that aspect for you so in this in this session we were going to walk you through some of the the main topics in in designing developing testing and then releasing your your provider so i'm doing this all for memory for my slides so as well as i guess the consistency in it from a user perspective the cluster api also brings in higher level functionalities so as well as just the pure provisioning of infrastructure and then kubernetes on top of those it has higher order functionality like automatically scaling or automatically doing the upgrades of kubernetes versions for example and the other area is automatically spreading machines across failure domains because you don't want all the machines in the same failure domain because if that rack
