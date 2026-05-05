---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Observability", "Networking", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Steve Sloka", "VMware"]
sched_url: https://kccnceu2021.sched.com/event/iE8u/contour-a-high-performance-multitenant-ingress-controller-for-kubernetes-steve-sloka-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Contour%2C+a+High+Performance+Multitenant+Ingress+Controller+for+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Contour, a High Performance Multitenant Ingress Controller for Kubernetes - Steve Sloka, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Observability]], [[Networking]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Steve Sloka, VMware
- Schedule: https://kccnceu2021.sched.com/event/iE8u/contour-a-high-performance-multitenant-ingress-controller-for-kubernetes-steve-sloka-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Contour%2C+a+High+Performance+Multitenant+Ingress+Controller+for+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Contour, a High Performance Multitenant Ingress Controller for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8u/contour-a-high-performance-multitenant-ingress-controller-for-kubernetes-steve-sloka-vmware
- YouTube search: https://www.youtube.com/results?search_query=Contour%2C+a+High+Performance+Multitenant+Ingress+Controller+for+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2Gcf3Rs6q4o
- YouTube title: Contour, A High Performance Multitenant Ingress Controller for Kubernetes - Michael Michael
- Match score: 0.98
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/contour-a-high-performance-multitenant-ingress-controller-for-kubernet/2Gcf3Rs6q4o.txt
- Transcript chars: 23410
- Keywords: contour, envoy, authorization, cluster, ingress, server, password, external, request, michael, support, working, features, actually, deploy, extension, source, client

### Resumo baseado na transcript

hello everybody and welcome to our presentation today we will be talking about contour a high performance multi-tenant ingress controller for kubernetes uh first let's go ahead and introduce the team that's working on contour my name is michael michael i'm the product lead and a director of product management at vmware uh as part of our team but not present here is steve chris a staff engineer at vmware tong liu the engineering manager also at vmware and i'm going to pass the baton to nick go ahead and

### Excerpt da transcript

hello everybody and welcome to our presentation today we will be talking about contour a high performance multi-tenant ingress controller for kubernetes uh first let's go ahead and introduce the team that's working on contour my name is michael michael i'm the product lead and a director of product management at vmware uh as part of our team but not present here is steve chris a staff engineer at vmware tong liu the engineering manager also at vmware and i'm going to pass the baton to nick go ahead and i'm unique hi everyone i'm nick young i'm a teddy i'm the technical lead for contour i'm a staff man engineer at vmware and i am in charge of the overall direction and architecture of hey everyone i'm steve sloca i'm a senior member of technical staff here at vmware uh i work a lot on the envoy integrations to contour hi everyone i'm james peach i'm a staff engineer at vmware i've been working on contour for about a year and i contribute in most of the different areas cool thank you all and we have our slack channels ids on the bottom so if you need to reach us we're all available on the kubernetes slack channel as well so let's take a look at what contour is today so contour is an open source kubernetes ingress controller and it's providing a control plane for the envoy edge and service proxy we really aimed with a mission to be the best ingress controller for kubernetes and lately we've been accepted into the cmcf back last summer as an incubating project so we plan to kind of bring together a lot of the cloud native community within the cncf landscape and deliver an amazing english controller that meets your needs we support dynamic configuration updates and multi-team ingress delegation out of the box while maintaining a lightweight profile and i'm going to switch over to me young our technical lead to go through some of the highlights of contour yeah hi everyone um so yeah contour was started in september 2017 uh at heptio uh it was started by uh dave cheney and steve sokol the original members of the team um and at the time contour was aiming to be a high performance as uh michael said contours are aiming to be a high performance and gross controller with a focus on multi-tenancy simplicity and being able to source your ingress config from whatever objects you need whether that's ingress um our http proxy crd or the new service apis um a really key part of contour's philosophy and goals all along have been to really keep the unix philosophy in mind to
