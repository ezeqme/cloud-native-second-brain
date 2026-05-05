---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Yang Che", "Alibaba", "Yuandong Xie", "Tencent"]
sched_url: https://kccncna2021.sched.com/event/lV2U/fluid-build-data-orchestration-in-kubernetes-yang-che-alibaba-yuandong-xie-tencent
youtube_search_url: https://www.youtube.com/results?search_query=Fluid+-+Build+Data+Orchestration+in+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Fluid - Build Data Orchestration in Kubernetes - Yang Che, Alibaba & Yuandong Xie, Tencent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Yang Che, Alibaba, Yuandong Xie, Tencent
- Schedule: https://kccncna2021.sched.com/event/lV2U/fluid-build-data-orchestration-in-kubernetes-yang-che-alibaba-yuandong-xie-tencent
- Busca YouTube: https://www.youtube.com/results?search_query=Fluid+-+Build+Data+Orchestration+in+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Fluid - Build Data Orchestration in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2U/fluid-build-data-orchestration-in-kubernetes-yang-che-alibaba-yuandong-xie-tencent
- YouTube search: https://www.youtube.com/results?search_query=Fluid+-+Build+Data+Orchestration+in+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Pjt8v4GYvRQ
- YouTube title: Fluid - Build Data Orchestration in Kubernetes - Yang Che, Alibaba & Yuandong Xie, Tencent
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/fluid-build-data-orchestration-in-kubernetes/Pjt8v4GYvRQ.txt
- Transcript chars: 16115
- Keywords: storage, training, runtime, scheduling, application, information, computing, architecture, applications, second, accelerate, workload, elastic, access, introduce, creating, platform, companies

### Resumo baseado na transcript

all right hello everyone welcome to join our session this session is about cognitive native data observation framework flow fruit is an open source project which is started from september last year the founders and the maintainers are from alibaba cloud and university a lecture they have a lot of experiences in kubernetes in big data and areas first let me introduce the presenters today my name is young chung i'm from alibaba cloud communities team and i'm the founder of the i'm the co-founder of the through the community

### Excerpt da transcript

all right hello everyone welcome to join our session this session is about cognitive native data observation framework flow fruit is an open source project which is started from september last year the founders and the maintainers are from alibaba cloud and university a lecture they have a lot of experiences in kubernetes in big data and areas first let me introduce the presenters today my name is young chung i'm from alibaba cloud communities team and i'm the founder of the i'm the co-founder of the through the community another speaker is he is the key contributor of flute project and he is working at times in the club now both of us contributed to fluid projects from very beginning in this session first i will talk about food projects itself including the history of the project why we want to start creating such a project and what problems we'd like to solve and and you know we'll go through the overall architecture as well some major design thinking behind the architecture and he will also give a demo to show how full speed up the development applications in the end we also will discuss the roadmap of the fluid project we'd like to invite all of you if you are in turn interested in this project now let's start it in this session in in the recent years we noticed that there is a big trend in big data and air areas according to partners prediction 70 percent of the ai applications will run on containers on the kubernetes platform by 2020 in addition the new stack technology reported that google will replace scheduling spark applications from ya to kubernetes by reviewing the the changes in data driven application companies we found we found that the changes took place to places in architectural level from three dimensions first the location relationship between the computing resources and the storage service second the diversity of the storage and workload types third the deployment mode of computing is changing from fixed mode to dynamic mode let's let's take a look in mapreduce tasks run on hdfs is mainstream and they are coupled time tightening in 2015 task tabs are gradually extended extended from hadoop to spark flink and test flow the storage tabs were also enriched to various tabs such as hdfs and saf computing and storage were separated but at this time the ability the application is still on fixed mode deployment without ina flexibility and containerization capabilities now in 2020 we can see there are also a lot of changes tasks and storage tab
