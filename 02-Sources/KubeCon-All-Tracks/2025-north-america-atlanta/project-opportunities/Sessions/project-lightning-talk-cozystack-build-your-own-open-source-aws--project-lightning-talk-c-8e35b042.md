---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Andrei Kvapil", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/28ye3/project-lightning-talk-cozystack-build-your-own-open-source-aws-on-bare-metal-andrei-kvapil-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Cozystack%3A+Build+Your+Own+Open+Source+AWS+On+Bare+Metal+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Cozystack: Build Your Own Open Source AWS On Bare Metal - Andrei Kvapil, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Andrei Kvapil, Maintainer
- Schedule: https://kccncna2025.sched.com/event/28ye3/project-lightning-talk-cozystack-build-your-own-open-source-aws-on-bare-metal-andrei-kvapil-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Cozystack%3A+Build+Your+Own+Open+Source+AWS+On+Bare+Metal+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Cozystack: Build Your Own Open Source AWS On Bare Metal.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/28ye3/project-lightning-talk-cozystack-build-your-own-open-source-aws-on-bare-metal-andrei-kvapil-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Cozystack%3A+Build+Your+Own+Open+Source+AWS+On+Bare+Metal+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-Q2ZQuzvHH8
- YouTube title: Project Lightning Talk: Cozystack: Build Your Own Open Source AWS On Bare Metal - Andrei Kvapil
- Match score: 0.997
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-cozystack-build-your-own-open-source-aws-on-bar/-Q2ZQuzvHH8.txt
- Transcript chars: 4934
- Keywords: managed, actually, virtual, storage, workloads, platform, machines, provide, databases, talking, monitoring, objects, cozystack, already, focusing, access, install, kernel

### Resumo baseado na transcript

We built next generation cloud platform which is fully based on Kubernetes. Cozystack is focused on providing managed services not only virtual machines. With bare metal you have predictable costs and your data yon rules which is perfect for AI regulated and edge workloads. On the layer two we provide storage networking virtualization then some operators cluster IP monitoring and on the layer 4 you have kubernetes objects using which you can order your own managed services. Uh every service is actually Kubernetes YAML object which can also be configured in user-friendly interface. Um with cozy stack you can create databases, manage user rights and their access rights uh configure backups and have uh preconfigured monitoring dashboards and alerts uh to integrate with cozy stack after you get your cloud installed.

### Excerpt da transcript

Uh my name is Andre Quel. Let's talk about Cozy Stack. How many of you already heard about the Cozy Stack? Please raise your hand. Thank you. Uh Cozy Stack is CNCF sandbox project starting from March 2025. We built next generation cloud platform which is fully based on Kubernetes. Cozystack is focused on providing managed services not only virtual machines. Nowadays we say nobody needs just pure virtual machines and everybody is focusing looking for fully managed and fully controlled uh managed services like you have in cloud. Uh coyst provides ready infrastructure stack with minimum dependencies just like external storage system and you can also consider cozystack as a framework which you can use to build a platform and provide your own managed services to your customers. uh cozy stack already includes such services like managed kubernetes databases cues virtual machines persistent volumes and S3 storage. Talking about kubernetes managed kubernetes service uh we usually say that it works pretty similar like in every cloud.

So we have control plane separated users have no access to their control plane nodes and provide all the features like load balancers persistent volumes and cluster after scaling. Uh cozy tech focused at bare metal at most because bare metal is faster, cheaper and sovereign. With bare metal you have predictable costs and your data yon rules which is perfect for AI regulated and edge workloads. But rebuilding cloud-like experience on bare metal is hard. Not with the cozy uh you can take just few bunch of your servers install the platform on it and get ready interfaced ordering managed services. Uh to make it possible we start working on very low level. Uh actually we pre have pre-baked image for the system which contains already predefined kernel and kernel modu mod modules used by the system. On the layer two we provide storage networking virtualization then some operators cluster IP monitoring and on the layer 4 you have kubernetes objects using which you can order your own managed services. Uh you can simply install cozy stack with uh our installer and get this dashboard where you can install any services you want to.

Uh every service is actually Kubernetes YAML object which can also be configured in user-friendly interface. Uh under the hood we use cube and many other projects. Actually cube allows us to split the workloads between the tenants so they can't affect each other. Talking about databases service, we fully uh focusing on
