---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Application + Development"
themes: ["AI ML", "GitOps Delivery"]
speakers: ["Hongchao Deng", "Alibaba Cloud"]
sched_url: https://kccnceu2021.sched.com/event/iE4S/zero-pain-microservice-development-and-deployment-with-dapr-and-kubevela-hongchao-deng-alibaba-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Zero+Pain+Microservice+Development+and+Deployment+with+Dapr+and+KubeVela+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Zero Pain Microservice Development and Deployment with Dapr and KubeVela - Hongchao Deng, Alibaba Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Application + Development]]
- Temas: [[AI ML]], [[GitOps Delivery]]
- País/cidade: Virtual / Virtual
- Speakers: Hongchao Deng, Alibaba Cloud
- Schedule: https://kccnceu2021.sched.com/event/iE4S/zero-pain-microservice-development-and-deployment-with-dapr-and-kubevela-hongchao-deng-alibaba-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Zero+Pain+Microservice+Development+and+Deployment+with+Dapr+and+KubeVela+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Zero Pain Microservice Development and Deployment with Dapr and KubeVela.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4S/zero-pain-microservice-development-and-deployment-with-dapr-and-kubevela-hongchao-deng-alibaba-cloud
- YouTube search: https://www.youtube.com/results?search_query=Zero+Pain+Microservice+Development+and+Deployment+with+Dapr+and+KubeVela+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ajc2ngGv0m8
- YouTube title: Zero Pain Microservice Development and Deployment with Dapr and KubeVela - Hongchao Deng, Alibaba
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/zero-pain-microservice-development-and-deployment-with-dapr-and-kubeve/Ajc2ngGv0m8.txt
- Transcript chars: 10500
- Keywords: application, resources, dapper, platform, basically, alibaba, write, component, matrix, applications, finally, projects, provides, object, deployment, source, called, developer

### Resumo baseado na transcript

hi everyone welcome to cubicon in this talk i'm going to talk about how we use cubevela and dapper to develop and build microservice applications before we start let me introduce myself my name is pronounced as hong chao den i'm currently working as a staff engineer at alibaba and focusing on cloud native application delivery i love open source and have been contributing quite a while i am a committer of cook vella oem and cosplay projects in the following i will first introduce cook valla's background and overview

### Excerpt da transcript

hi everyone welcome to cubicon in this talk i'm going to talk about how we use cubevela and dapper to develop and build microservice applications before we start let me introduce myself my name is pronounced as hong chao den i'm currently working as a staff engineer at alibaba and focusing on cloud native application delivery i love open source and have been contributing quite a while i am a committer of cook vella oem and cosplay projects in the following i will first introduce cook valla's background and overview then i will dive into its architecture and provide more detailed analysis i will conclude cuba section with some of its key features for application management and then i will give a brief introduction about dapper and finally i will talk about how alibaba uses cubic vela and dapper in production and do a case study on application monitoring first let's talk about cube vela let me start with talking about the background first like delivering applications on kubernetes needs composing a couple of kubernetes resources for example deployment stifles that ingress services etc usually we not only need to bundle all those resources into a package but we also need a composition model to parameterize and connect those resources together a few projects have been have been trying to solve these problems one is called application crd from the kubernetes sig why it's the earliest from upstream effort it doesn't resolve any developer operator concerns so far other than providing like basic metadata it doesn't work for application law for this reason and there isn't any active development on it as far as i can see another project that a lot of people use in production to manage applications is ham more specifically like users just write some templates of kubernetes resources and put them in a bundle called chart uh like white hamstring like a lot of people use it like they are two black box to users uh the hammer chart is built as parameter values which is hard to like understand and invert like operational resources uh underneath additionally the parameter values doesn't have api schemer define for them and finally like char doesn't have any composition model that you can use those more use of templates to just plug and play and and like we use across different projects so very often uh platform teams decide to build their in-house application crds to solve the problems i just discussed like for example pinterest has built its own pinterest service and robin
