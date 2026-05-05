---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Sahdev Zala", "Richard Theis", "Guang Ya Liu", "Brad Topol", "IBM"]
sched_url: https://kccncna2021.sched.com/event/lV8p/kubernetes-cloud-provider-ibm-project-overview-and-deep-dive-sahdev-zala-richard-theis-guang-ya-liu-brad-topol-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Cloud+Provider+IBM+project+Overview+and+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes Cloud Provider IBM project Overview and Deep Dive - Sahdev Zala & Richard Theis & Guang Ya Liu & Brad Topol, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Sahdev Zala, Richard Theis, Guang Ya Liu, Brad Topol, IBM
- Schedule: https://kccncna2021.sched.com/event/lV8p/kubernetes-cloud-provider-ibm-project-overview-and-deep-dive-sahdev-zala-richard-theis-guang-ya-liu-brad-topol-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Cloud+Provider+IBM+project+Overview+and+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes Cloud Provider IBM project Overview and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8p/kubernetes-cloud-provider-ibm-project-overview-and-deep-dive-sahdev-zala-richard-theis-guang-ya-liu-brad-topol-ibm
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Cloud+Provider+IBM+project+Overview+and+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UxxK3hNVGYU
- YouTube title: Kubernetes Cloud Provider IBM project Overv... Sahdev Zala, Richard Theis, Guang Ya Liu & Brad Topol
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-cloud-provider-ibm-project-overview-and-deep-dive/UxxK3hNVGYU.txt
- Transcript chars: 21190
- Keywords: openshift, provider, cluster, support, providers, security, provides, releases, managed, version, running, source, manager, container, moment, features, repositories, various

### Resumo baseado na transcript

um hello everyone uh thank you for joining this virtual talk uh on puberty's cloud provider ibm project overview and deep dive my name is sadie zala i am a senior software engineer at ibm and colleague for this project uh richard would you like to introduce yourself sure richard teiss i'm a senior software engineer and i'm the open shift and kubernetes release lead for our managed services for open shifting kubernetes okay uh brad would you like to introduce quickly sure santa hi everyone i'm brad topel i'm what the community calls the cloud controller manager which is the control loop within kubernetes um owned by the uh the cloud provider sig which is the interface for this control loop to manage um an interface with the cloud to deliver certain features to the kubernetes cluster that kubernetes itself doesn't implement because um they're cloud provider specific and that the cloud controller manager is then responsible for implementing those key features for the cloud now this view here shows the ccm architecture which is the new architecture out

### Excerpt da transcript

um hello everyone uh thank you for joining this virtual talk uh on puberty's cloud provider ibm project overview and deep dive my name is sadie zala i am a senior software engineer at ibm and colleague for this project uh richard would you like to introduce yourself sure richard teiss i'm a senior software engineer and i'm the open shift and kubernetes release lead for our managed services for open shifting kubernetes okay uh brad would you like to introduce quickly sure santa hi everyone i'm brad topel i'm ibm's distinguished engineer for open technologies and developer advocacy um all right thank you brad um all right so uh i will provide an overview and you know the activities uh structure of the project and then we will you know straight deep dive into [Music] uh the three uh repositories the main reapers we have uh actually it's four repositories uh but the three main repositories for uh cluster api provider driving cloud uh there is one for ppc block storage and then we have two under ibm cloud provider all right so uh let me just brief about uh the broader special interest group cloud provider uh this c cloud provider is a group of people interested in various aspects of running kubernetes on different cloud provider clouds it owns cloudborder provider interface code which is responsible for running all the cloud provider specific control groups right uh you can read more about uh the code uh on the link i have provided the siege also ensures that the kubernetes ecosystem evolve in a way that is neutral to various cloud providers and the same time it ensures that uh it provides consistent and high quality experience to the users the sea gowns uh different sub projects they were formally had their own specific uh sig but now they're part of the sig cloud order and the provider ibm cloud is one of the sub-project uh you can read more about the sig cloud provider uh on the link i have provided at the bottom of this slide all right so the broader ibm cloud sub project it's it's all about development and discussions around uh various aspects of running kubernetes on ibm cloud we also participates in various activities happening in the sig cloud provider and you know uh as a member of this uh project uh or you're just following it you basically are staying on top of what's going on in the ibm cloud platform with respect to kubernetes and related cncf projects we strictly don't discuss any commercial uh kind of uh you know activities or any discussions rel
