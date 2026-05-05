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
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Xing Yang", "VMware", "Xiangqian Yu", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE8N/kubernetes-data-protection-wg-intro-and-deep-dive-xing-yang-vmware-xiangqian-yu-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+and+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes Data Protection WG Intro and Deep Dive - Xing Yang, VMware & Xiangqian Yu, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Xing Yang, VMware, Xiangqian Yu, Google
- Schedule: https://kccnceu2021.sched.com/event/iE8N/kubernetes-data-protection-wg-intro-and-deep-dive-xing-yang-vmware-xiangqian-yu-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+and+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Intro and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8N/kubernetes-data-protection-wg-intro-and-deep-dive-xing-yang-vmware-xiangqian-yu-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+and+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DBxOBzBkimo
- YouTube title: Kubernetes Data Protection WG Intro and Deep Dive - Xing Yang, VMware & Xiangqian Yu, Google
- Match score: 0.806
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-data-protection-wg-intro-and-deep-dive/DBxOBzBkimo.txt
- Transcript chars: 18420
- Keywords: backup, application, snapshot, volume, object, storage, restore, please, working, controller, repository, slides, missing, notification, blocks, stateful, design, container

### Resumo baseado na transcript

hello everyone thanks for joining us today today shin and i will give a deep dive and uh introduction to the data protection working group my name is john chiang exercise please i am a software engineer from google hello everyone my name is shin yang i work at vmware in the cloud surgery team i'm also a co-chair in kubernetes storage and co-chair of the data production wing group with xiangtian thank you shin next slides please today we're gonna go through a couple of topics uh first we'll

### Excerpt da transcript

hello everyone thanks for joining us today today shin and i will give a deep dive and uh introduction to the data protection working group my name is john chiang exercise please i am a software engineer from google hello everyone my name is shin yang i work at vmware in the cloud surgery team i'm also a co-chair in kubernetes storage and co-chair of the data production wing group with xiangtian thank you shin next slides please today we're gonna go through a couple of topics uh first we'll reiterate a little bit what is the motivation of this data protection working group and then we go a little bit glance over who are the organizations that get involved in this effort and then we talk about what we think about data about education it is in the kubernetes context and then what are the existing building blocks to support data protection in kubernetes and what are we amazing for the building blocks to support this feature better and how to get involved next slides please uh there were sufficient there were not sufficient fundamental kubernetes building blocks to easily allow users to do backup and snapshot of the stateful applications as of today day one operations for a deployment management role of stateful workload are well supported there are volume operations either through csi driver or entry drivers and they are working apis deployment stateful set etc just a product with more and more stateful workload moving to kubernetes the desire of providing fundamental building blocks to allow users protect the data it's getting hit hit it git ops could potentially be used for rolling back of stateless workloads it is still insufficient for stateful workloads as the data cannot easily be managed by githubs this working group has been built targeted at designing and implementing kubernetes native building blocks to allow backup vendors to quickly build backup solutions for the users that's to support the data operations for data protection specifically and this working group has two major stakeholders sick apps and seek storage and potentially seek note next slice piece so who are oregon world we have a bi-weekly meeting and those are just probably incomplete list of companies that are supporting this initiative we saw a lot of contributions from storage companies cloud providers backup windows etc etc and thanks to all the contributors we are making good progress over there next slides please so what exactly is data protection in our in kubernetes the main purp
