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
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Joe Burnett‎", "Marcin Wielgus", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV8O/sig-autoscaling-introduction-+-hpavpa-updates-joe-burnett-marcin-wielgus-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG-Autoscaling%3A+Introduction+%2B+HPA%2FVPA+Updates+CNCF+KubeCon+2021
slides: []
status: parsed
---

# SIG-Autoscaling: Introduction + HPA/VPA Updates - Joe Burnett‎ & Marcin Wielgus, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Joe Burnett‎, Marcin Wielgus, Google
- Schedule: https://kccncna2021.sched.com/event/lV8O/sig-autoscaling-introduction-+-hpavpa-updates-joe-burnett-marcin-wielgus-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG-Autoscaling%3A+Introduction+%2B+HPA%2FVPA+Updates+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre SIG-Autoscaling: Introduction + HPA/VPA Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8O/sig-autoscaling-introduction-+-hpavpa-updates-joe-burnett-marcin-wielgus-google
- YouTube search: https://www.youtube.com/results?search_query=SIG-Autoscaling%3A+Introduction+%2B+HPA%2FVPA+Updates+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L4d7K83vq_0
- YouTube title: SIG-Autoscaling: Introduction + HPA/VPA Updates - Joe Burnett‎ & Marcin Wielgus, Google
- Match score: 0.801
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sig-autoscaling-introduction-hpa-vpa-updates/L4d7K83vq_0.txt
- Transcript chars: 19727
- Keywords: actually, scaling, cluster, metrics, scaler, target, create, configure, minutes, scales, recommendation, little, features, horizontally, capacity, traffic, pretty, custom

### Resumo baseado na transcript

welcome to cubecon 2021 north america sig auto scaling um presentation uh my name is joseph burnett i'm a contributor working on horizontal pad auto scaling and i'm going to walk you through a few basics of kubernetes auto scaling today i want to tell you a little bit about the sig as well give you an example of what kubernetes auto scaling does so you can understand some of the terminology and how to use it and i'm going to talk a few minutes about some upcoming features and quickly as possible it's sort of optimized for services uh not necessarily for patch um and i'll get to that in just a minute so you want to be able to scale up right away so you want to react quickly so you see that you see the the recommendation go up you go up immediately but you also don't want to flap because the metrics they kind of they kind of go up and down right you don't want to keep creating and deleting pods because it creates a

### Excerpt da transcript

welcome to cubecon 2021 north america sig auto scaling um presentation uh my name is joseph burnett i'm a contributor working on horizontal pad auto scaling and i'm going to walk you through a few basics of kubernetes auto scaling today i want to tell you a little bit about the sig as well give you an example of what kubernetes auto scaling does so you can understand some of the terminology and how to use it and i'm going to talk a few minutes about some upcoming features and i'll save some time at the end for questions so who are we sig auto scaling has the scope of horizontal and vertical polynomial scaling um this is changing the size of pods vertically or making more or fewer of them horizontally cluster proportional system component auto scaling is just a very simple auto scaler that adjusts the number of pods in a deployment based on the size of the cluster so for example cube dns uses this also stig auto scaling is responsible for cluster autoscaler which actually sizes up and down the cluster itself so i'll talk a little bit about how those interact with each other in a few minutes the chairs of segato scaling are guy templeton who works at sky scanner and marcin vigulus who works at google and here's a link here to the community page which should be linkable from the pdf uploaded with this presentation this will tell you all about the sig meetings and all the information about the uh this special interest group okay so let me start with a quick overview of the auto scaling space in kubernetes there is two dimensions here to consider horizontal and vertical and they are separated by two layers pods and nodes or workload and cluster of scheme so hpa scales in and out i mentioned already it makes more or fewer pods based on metrics that you predefine you can scale on more than one metric if you want for example cpu utilization maybe some pub sub uh queue length or something vertical pod auto scaling um is for those workloads which don't necessarily scale horizontally as well or maybe you would prefer to give more or fewer resources to a pod to adjust for usage or maybe you just don't know what to request vpa can actually give you recommendations in a read-only mode or you can tell it to just go full automatic and resize your pods for you cluster auto scaler has the same kinds of auto scan in and out making more or fewer nodes in any of the node pools that are configured uh vertical auto scaling in cluster auto scaler is more about selecting the right
