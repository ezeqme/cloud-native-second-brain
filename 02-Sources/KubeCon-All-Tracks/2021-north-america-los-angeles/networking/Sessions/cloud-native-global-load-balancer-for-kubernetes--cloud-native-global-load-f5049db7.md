---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Yury Tsarev", "Zak Anderson", "Absa Group"]
sched_url: https://kccncna2021.sched.com/event/lV4Q/cloud-native-global-load-balancer-for-kubernetes-yury-tsarev-zak-anderson-absa-group
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Global+Load+Balancer+for+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud Native Global Load Balancer for Kubernetes - Yury Tsarev & Zak Anderson, Absa Group

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Yury Tsarev, Zak Anderson, Absa Group
- Schedule: https://kccncna2021.sched.com/event/lV4Q/cloud-native-global-load-balancer-for-kubernetes-yury-tsarev-zak-anderson-absa-group
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Global+Load+Balancer+for+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud Native Global Load Balancer for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4Q/cloud-native-global-load-balancer-for-kubernetes-yury-tsarev-zak-anderson-absa-group
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Global+Load+Balancer+for+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-lkKZRdv81A
- YouTube title: Cloud Native Global Load Balancer for Kubernetes - Yury Tsarev & Zak Anderson, Absa Group
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-native-global-load-balancer-for-kubernetes/-lkKZRdv81A.txt
- Transcript chars: 19510
- Keywords: cluster, already, workload, ingress, global, clusters, standard, traffic, resource, running, exactly, primary, europe, thanks, strategy, application, failover, healthy

### Resumo baseado na transcript

hello everybody i'm yuri uh principal engineer in apsa group and zac together with me uh we are today and we are going to talk about our experience of building and maintaining and operating cloud-native global load balancer for kubernetes in production yeah hello everyone it's zac anderson i run the kubernetes service for apta nice to see you all yeah excited um and i'll give it back to yuri that we can carry on cool thanks zach so let's jump straight away the presentation so well where are and

### Excerpt da transcript

hello everybody i'm yuri uh principal engineer in apsa group and zac together with me uh we are today and we are going to talk about our experience of building and maintaining and operating cloud-native global load balancer for kubernetes in production yeah hello everyone it's zac anderson i run the kubernetes service for apta nice to see you all yeah excited um and i'll give it back to yuri that we can carry on cool thanks zach so let's jump straight away the presentation so well where are and how it all started somewhere in 2019 uh apsa group uh figured out that organization needs open source global service load balancing function some cloud native solution to steer the traffic in a smart way over geographically dispersed kubernetes clusters and we needed to uh solution to be able uh uh to be aware of internal workflow workload state inside this cluster uh avoiding standard http end-to-end checks so to be a real cloud native and we didn't find any existing proprietary vendor solutions uh and there were no also appropriate uh open source uh alternatives so that's why we created kgb uh the project started in december 2019 uh it stands for kubernetes global balancer and it was developed in an open source in a github as a repository from day zero so in totally open minor uh as a open source project uh from the very beginning uh slightly more than one year fast forward we managed to attract a small community uh built to mature enough projects and to reach the cncf sandbox level acceptance which we are very really proud of and we are using in kgb in production for more than one year maybe already year and a half so let's talk about some kubernetes sorry kgb concepts that are very important uh from architecture around perspective so it is cloud native uh global service load balancing it is built on top of operator pattern meaning that it is a controller which resides on kubernetes clusters and it's backed by associated custom resource definition we don't have any single point of failure so there is no control cluster and kgb is deployed next to gslb enabled workflows uh kgb uh utilizes uh standard awareness primitives for its own operation so it's a ingress services and associated both blindness and readiness checks overall operations is based on battle tested dns protocol which enables us to be highly reliable and to operate in a global scale dns is used both for traffic steering and cross cluster state exchange we're trying to be as environment agnostic as po
