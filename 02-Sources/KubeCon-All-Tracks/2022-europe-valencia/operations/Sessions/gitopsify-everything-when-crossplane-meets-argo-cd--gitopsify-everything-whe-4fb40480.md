---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Operations"
themes: ["GitOps Delivery"]
speakers: ["Ying Mo", "Ken Murray", "IBM"]
sched_url: https://kccnceu2022.sched.com/event/yts5/gitopsify-everything-when-crossplane-meets-argo-cd-ying-mo-ken-murray-ibm
youtube_search_url: https://www.youtube.com/results?search_query=GitOpsify+Everything%3A+When+Crossplane+Meets+Argo+CD+CNCF+KubeCon+2022
slides: []
status: parsed
---

# GitOpsify Everything: When Crossplane Meets Argo CD - Ying Mo & Ken Murray, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Operations]]
- Temas: [[GitOps Delivery]]
- País/cidade: Spain / Valencia
- Speakers: Ying Mo, Ken Murray, IBM
- Schedule: https://kccnceu2022.sched.com/event/yts5/gitopsify-everything-when-crossplane-meets-argo-cd-ying-mo-ken-murray-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=GitOpsify+Everything%3A+When+Crossplane+Meets+Argo+CD+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre GitOpsify Everything: When Crossplane Meets Argo CD.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yts5/gitopsify-everything-when-crossplane-meets-argo-cd-ying-mo-ken-murray-ibm
- YouTube search: https://www.youtube.com/results?search_query=GitOpsify+Everything%3A+When+Crossplane+Meets+Argo+CD+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9odjdVqJkws
- YouTube title: GitOpsify Everything: When Crossplane Meets Argo CD - Ying Mo & Ken Murray, IBM
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/gitopsify-everything-when-crossplane-meets-argo-cd/9odjdVqJkws.txt
- Transcript chars: 20200
- Keywords: ansible, cluster, provider, infrastructure, resource, deployment, clusters, application, native, pipeline, contents, argo, management, manage, basically, create, managed, configuration

### Resumo baseado na transcript

hi my name is karen murray i'm a ci city engineer at ibm working within the cloud pack for watson ai ops team my area of expertise is in the adoption of git ops in the development and operation of deployment pipelines today i'm joined with my colleague ying mo to present on the topic of git ups and crossplane and its application across both traditional non-cloud native it environments and cloud native applications so an overview of the agenda um first stage here i'm going to talk about the

### Excerpt da transcript

hi my name is karen murray i'm a ci city engineer at ibm working within the cloud pack for watson ai ops team my area of expertise is in the adoption of git ops in the development and operation of deployment pipelines today i'm joined with my colleague ying mo to present on the topic of git ups and crossplane and its application across both traditional non-cloud native it environments and cloud native applications so an overview of the agenda um first stage here i'm going to talk about the adoption of crossplane and argo cd um in ci cd pipelines i'm going to give a generic view of a deployment pipeline as it exists today and and and how we use our deployment pipelines in the uh infrastructure provisioning and life cycle management but also in application deployments i'm going to talk about cross plane as an abstraction platform for infrastructure provisioning so basically using githubs to both manage our infrastructure and also application deployments uh yingmo will then discuss ongoing development work in the area of ansible cross plane provider for more traditional i.t systems um he'll discuss the the provider in terms of of how it works and how people can use it how it can be adopted and and then finally a deep dive across the and across the ansible provider runtime life cycle some best practices in the in the use of of the provider and then finally comparing the the answer provider with the uh the ansible operator um so if we just look at a typical deployment pipeline a very generic view um you typically would have a build here coming in on the left-hand side of the plumbing pipeline and the first stage would typically be the acquisition of infrastructure onto which you would run your deployments um the second stage would typically be some kind of configuration you might want to do on that infrastructure so in terms of a kubernetes cluster for example you might want to set up some storage or some prerequisites before you do your application deployment um application deployment then you would deploy your your software components onto that infrastructure you may want to do some post deploy checks to ensure that the you know your applications have got are deployed to a sufficient level before you would trigger some downstream test pipelines you may want to export some deployment logs um trigger then downstream test pipelines export those test pipeline results to some location that could be you know downloaded by individuals at a later point and then final
