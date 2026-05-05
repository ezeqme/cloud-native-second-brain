---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Yan Wang", "Daojun Zhang", "Chenyu Zhang", "VMware", "Vadim Bauer", "8gears Container Registry"]
sched_url: https://kccncna2022.sched.com/event/182Nd/enterprise-cloud-native-artifact-registry-yan-wang-daojun-zhang-chenyu-zhang-vmware-vadim-bauer-8gears-container-registry
youtube_search_url: https://www.youtube.com/results?search_query=Enterprise+Cloud+Native+Artifact+Registry+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Enterprise Cloud Native Artifact Registry - Yan Wang & Daojun Zhang & Chenyu Zhang, VMware; Vadim Bauer, 8gears Container Registry

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Yan Wang, Daojun Zhang, Chenyu Zhang, VMware, Vadim Bauer, 8gears Container Registry
- Schedule: https://kccncna2022.sched.com/event/182Nd/enterprise-cloud-native-artifact-registry-yan-wang-daojun-zhang-chenyu-zhang-vmware-vadim-bauer-8gears-container-registry
- Busca YouTube: https://www.youtube.com/results?search_query=Enterprise+Cloud+Native+Artifact+Registry+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Enterprise Cloud Native Artifact Registry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Nd/enterprise-cloud-native-artifact-registry-yan-wang-daojun-zhang-chenyu-zhang-vmware-vadim-bauer-8gears-container-registry
- YouTube search: https://www.youtube.com/results?search_query=Enterprise+Cloud+Native+Artifact+Registry+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PmCCzyxMv8s
- YouTube title: Intro: Harbor - Enterprise Cloud Native Artifact Registry - Alex Xu & Steven Ren, VMware
- Match score: 0.758
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/enterprise-cloud-native-artifact-registry/PmCCzyxMv8s.txt
- Transcript chars: 23988
- Keywords: images, docker, registry, manifest, hardware, harbor, artifacts, distribution, harper, upload, features, manage, container, support, create, native, release, around

### Resumo baseado na transcript

good morning good afternoon or good evening depending on where you are um we're very happy that you can attend this session and today myself and my co-presenter will talk a little bit about the harper project so this is supposed to be an introductory session um it's gonna be fairly light and we'll give a sort of a high level overview of the hardware registry and you know what it is why you might need it and the current status of the project uh a couple some of the

### Excerpt da transcript

good morning good afternoon or good evening depending on where you are um we're very happy that you can attend this session and today myself and my co-presenter will talk a little bit about the harper project so this is supposed to be an introductory session um it's gonna be fairly light and we'll give a sort of a high level overview of the hardware registry and you know what it is why you might need it and the current status of the project uh a couple some of the things that we worked on for the last couple releases and then there's also a deep dive session where our engineers will go into more details on some of the specific features that are coming out um 2.1 release the upcoming release and then we have a demo prepared for you today as well and we'll leave the last time 10 minutes per q a so a quick introduction i'm alex chu i'm a product manager in the cloud native team at vmware leaking that harbor effort so i'm trying to responsible for trying to understand the requirements around the registry driving the roadmap collecting feedback and making sure we're constantly improving and seeing sustained growth within the community and with me today is my co-presenter steven grim stephen hi everyone nice to meet you and welcome come to join our harboring stock session my name is steven so i'm working for harbor as an engineer manager in winter so i'm mainly responsible for development feature and management release in the same time in vmware i also mentioned the uh telugu navigation product all right thank you steven um so what is harper well harvard is a trusted cloud native registry that can store sign and scan content and so it's the registry is basically just a place to hold host and manage your artifacts and so when we started this project we set out to build an on-prem registry leveraging the docker distribution which was the de facto standard for storing container images at the time but we also wanted to address on the issues that we came across while using docker hub and some of the other alternatives and then over time we've added more and more services and features to it like lifecycle management features security features like scanning and signing and so our missions right now is still to be the best cloud native registry for kubernetes uh and we started support for docker images and then expanded to helm charts in the 1.6 release and now with oci which is the main theme for the 2.0 release that i'll talk about in a little bit you can support any
