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
themes: ["AI ML", "Community Governance"]
speakers: ["Anusha Ramineni", "NEC Corporation India Private Ltd", "Lingxian Kong", "Catalyst Cloud"]
sched_url: https://kccncna2021.sched.com/event/lV8C/cloud-provider-openstack-intro-update-anusha-ramineni-nec-corporation-india-private-ltd-lingxian-kong-catalyst-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Provider+OpenStack+Intro+%26+Update+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud Provider OpenStack Intro & Update - Anusha Ramineni, NEC Corporation India Private Ltd & Lingxian Kong, Catalyst Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Anusha Ramineni, NEC Corporation India Private Ltd, Lingxian Kong, Catalyst Cloud
- Schedule: https://kccncna2021.sched.com/event/lV8C/cloud-provider-openstack-intro-update-anusha-ramineni-nec-corporation-india-private-ltd-lingxian-kong-catalyst-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Provider+OpenStack+Intro+%26+Update+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud Provider OpenStack Intro & Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8C/cloud-provider-openstack-intro-update-anusha-ramineni-nec-corporation-india-private-ltd-lingxian-kong-catalyst-cloud
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Provider+OpenStack+Intro+%26+Update+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ceQC2i1DOFc
- YouTube title: Cloud Provider OpenStack Intro & Update - Anusha Ramineni & Lingxian Kong
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-provider-openstack-intro-update/ceQC2i1DOFc.txt
- Transcript chars: 20236
- Keywords: openstack, driver, provider, controller, manager, volume, cluster, plugin, support, release, octavia, latest, plugins, cinder, ingress, magnum, component, balancer

### Resumo baseado na transcript

hello everyone welcome to join this session about introduction and project update of provider openstack my name is lin xiang kung from catalyst cloud together with me today is anusha ramneni from nec and we are both maintainers of provider openstack in this session we will first talk about some overview of provider openstack and then we will go through its components and their features their design and their updates and finally we will give you some information about how to get involved maybe some of you have already heard

### Excerpt da transcript

hello everyone welcome to join this session about introduction and project update of provider openstack my name is lin xiang kung from catalyst cloud together with me today is anusha ramneni from nec and we are both maintainers of provider openstack in this session we will first talk about some overview of provider openstack and then we will go through its components and their features their design and their updates and finally we will give you some information about how to get involved maybe some of you have already heard of openstack which is an open source cloud computing platform actually before kubernetes was born openstack was one of the most active open source project in the world and then kubernetes just came from behind so some people may say they are competitors but from my perspective that doesn't necessarily mean that one is replacement for the other actually the two can can be both capable of working in tandem in order to bring greater values to organizations and better service to the users so actually they are friends and most importantly they are both open source cloud provider openstack was created as a sub-project of seek cloud provider the responsibility of c cloud provider is to establish standards and the requirements that should be meant by other cloud providers to ensure their integration with with kubernetes so basically provider openstack is just like provider aws provider gcp or provider azure if you are more familiar with those public clouds so they are at the same layer so there are actually a bunch of components in provider openstack in order to implement some kubernetes resources and functions so here is a list of all the components in provider openstack the two important ones are openstack cloud controller manager and the csi plugins other than those we also have octavia ingress controller which is implementing the ingress resource in kubernetes and we have magnum auto healer to achieve high availability of the cluster nodes in security area we have keystone house webhook for rbic and we have barbican kms plugin for the secret data encryption and we will go through them one by one shortly so here is a diagram showing that the kubernetes resource and functions each provider openstack component has implemented and the interaction between each component and openstack services actually openstack has lots of projects lots of services and you can see here some service is required by by some particular provider openstack component fo
