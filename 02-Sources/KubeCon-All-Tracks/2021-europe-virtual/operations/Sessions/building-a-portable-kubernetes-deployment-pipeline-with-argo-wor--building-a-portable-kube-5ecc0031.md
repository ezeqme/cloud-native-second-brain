---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Operations"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Thomas Meadows", "Jetstack", "Ollie Young", "Improbable"]
sched_url: https://kccnceu2021.sched.com/event/iE1n/building-a-portable-kubernetes-deployment-pipeline-with-argo-workflows-and-events-thomas-meadows-jetstack-ollie-young-improbable
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Portable+Kubernetes+Deployment+Pipeline+with+Argo+Workflows+and+Events+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Building a Portable Kubernetes Deployment Pipeline with Argo Workflows and Events - Thomas Meadows, Jetstack & Ollie Young, Improbable

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Operations]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Thomas Meadows, Jetstack, Ollie Young, Improbable
- Schedule: https://kccnceu2021.sched.com/event/iE1n/building-a-portable-kubernetes-deployment-pipeline-with-argo-workflows-and-events-thomas-meadows-jetstack-ollie-young-improbable
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Portable+Kubernetes+Deployment+Pipeline+with+Argo+Workflows+and+Events+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Building a Portable Kubernetes Deployment Pipeline with Argo Workflows and Events.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1n/building-a-portable-kubernetes-deployment-pipeline-with-argo-workflows-and-events-thomas-meadows-jetstack-ollie-young-improbable
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Portable+Kubernetes+Deployment+Pipeline+with+Argo+Workflows+and+Events+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JvbwpiFnBuA
- YouTube title: Building a Portable Kubernetes Deployment Pipeline with Argo Workflo... Thomas Meadows & Ollie Young
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/building-a-portable-kubernetes-deployment-pipeline-with-argo-workflows/JvbwpiFnBuA.txt
- Transcript chars: 27184
- Keywords: platform, orchestrator, argo, improbable, cluster, environments, components, version, customer, deploy, developers, environment, events, changes, development, inside, workflows, defense

### Resumo baseado na transcript

so hello kubecon uh thank you very much for coming to our talk my name is tom and i'm a solutions engineer at jet stack i'm joined here by ollie so hello ollie hello yes i'm olly young software engineer improbable in the defense unit in the eve engineering velocity team today we're going to tell you the story of how improbable and jet stack worked to build deployment and release service using kubernetes technologies such as argo workflows and events this is a multifaceted story which includes many complexities

### Excerpt da transcript

so hello kubecon uh thank you very much for coming to our talk my name is tom and i'm a solutions engineer at jet stack i'm joined here by ollie so hello ollie hello yes i'm olly young software engineer improbable in the defense unit in the eve engineering velocity team today we're going to tell you the story of how improbable and jet stack worked to build deployment and release service using kubernetes technologies such as argo workflows and events this is a multifaceted story which includes many complexities and design challenges that we had to overcome in order to be able to achieve the ultimate goal of providing improbable with a platform that could be deployed anywhere under any circumstances whether that be on the edge on-prem or in public cloud so without further ado we want to kick off by talking to you about the problem at hand we needed to start out by determining what is the platform and what are the ultimate goals of what we need for it to be delivered so ollie what's the platform that we are building for um and and what were the sort of design challenges we needed to overcome to have the platform deployed and operational so improv we've built a synthetic environment platform and a synthetic environment is essentially just a highly scalable simulation or grouping of simulations that can be used to represent various movements across multiple domains so when i say a domain i actually mean in the defense sense of the word so we're talking land sea air space cyber and we can simulate vehicle movements civilian movements and we can package all of that together and enable our customers to build a virtual world containing all of that information so that's what our platform does it enables you to build a fully capable synthetic environment at scale so our platform is essentially made up of multiple components built by multiple people or multiple teams when we deploy it we cannot really assume that we're going to run on any specific flavor of kubernetes it could be you know running on a on a customer site and in a military context that could be a forward operating base with zero internet connectivity and so these are the sort of target deployment environments we need to deploy to and that's essentially one of the problems we're trying to solve here so i guess ollie you mentioned that the end goal of the platform was to be able to deploy on any kubernetes service uh it needs to be completely unbiased in that sense but also it can't rely on an external in
