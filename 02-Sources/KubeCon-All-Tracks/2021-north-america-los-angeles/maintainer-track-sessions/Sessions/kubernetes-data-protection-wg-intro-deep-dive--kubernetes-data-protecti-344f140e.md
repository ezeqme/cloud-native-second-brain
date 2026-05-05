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
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Xiangqian Yu", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV6V/kubernetes-data-protection-wg-intro-deep-dive-xiangqian-yu-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes Data Protection WG Intro & Deep Dive - Xiangqian Yu, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Xiangqian Yu, Google
- Schedule: https://kccncna2021.sched.com/event/lV6V/kubernetes-data-protection-wg-intro-deep-dive-xiangqian-yu-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6V/kubernetes-data-protection-wg-intro-deep-dive-xiangqian-yu-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rHRhmi76Q4I
- YouTube title: Kubernetes Data Protection WG Intro & Deep Dive - Xiangqian Yu, Google
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-data-protection-wg-intro-deep-dive/rHRhmi76Q4I.txt
- Transcript chars: 21621
- Keywords: backup, application, snapshot, volume, storage, object, working, cluster, protection, restore, please, workload, repository, stateful, protect, basically, missing, slides

### Resumo baseado na transcript

hello everyone today shenzhen and i will give an introduction and develop for the kubernetes data production working group my name is xinyang i work at a vmware in the cloud storage team i'm a co-chair of cncf tech storage a co-chair of kubernetes sig storage i also co-lead the data protection wing group with shenzhen hi everyone thanks for coming uh my name is sean chen i work in for google i'm right now uh co-leading the data protection working group with shin next slides please uh today shin

### Excerpt da transcript

hello everyone today shenzhen and i will give an introduction and develop for the kubernetes data production working group my name is xinyang i work at a vmware in the cloud storage team i'm a co-chair of cncf tech storage a co-chair of kubernetes sig storage i also co-lead the data protection wing group with shenzhen hi everyone thanks for coming uh my name is sean chen i work in for google i'm right now uh co-leading the data protection working group with shin next slides please uh today shin and i will go through um these topics and listening on the agenda uh we will i will go through what what motivated us to establish this working group and who are the parties that are getting involved in this data protection working group and uh explain a little bit what do we think uh data protection is in the kubernetes context and go through what are the existing building blocks or modules that allows application owners or cluster owners to protect the stateful workloads and what exactly are the gaps that this working group is looking to build or propose to help providing data protection in the kubernetes context and the very last shin will go through how to get involved in this data working group that this working group next please um as you many of you may be or very well aware of um the day one operations for stateful workloads are actually pretty well supported in kubernetes context in order to uh there are persistent volume operations including probation in a volume attach a volume to a specific node to hold your data your workloads and data to the app orchestration apis like workload apis deployments and steadfast supports to use those persistent volumes in an application context it's been there for a couple of years and is very stable with that the direct impact is more and more stateful workloads like databases message queues etc etc are looking forward to utilize those constructs as well as kubernetes very nice feature of scanning scalability etc etc to move into the kubernetes environment however uh the day two maintenance operations for for example to how do i protect my stateful workload within the companies context is still uh in need is very limited at this moment for various of reasons kubernetes users as of today uses git apps to protect their stateful workloads config files but the story around how do i protect my uh stateful workload including the configs as well as the volume data is still yet to be is still yet to be discovered and also support
