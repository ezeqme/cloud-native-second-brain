---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Xing Yang", "VMware", "Jan Šafránek", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HyS2/kubernetes-sig-storage-intro-and-deep-dive-xing-yang-vmware-jan-safranek-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage%3A+Intro+and+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes SIG Storage: Intro and Deep Dive - Xing Yang, VMware & Jan Šafránek, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Xing Yang, VMware, Jan Šafránek, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HyS2/kubernetes-sig-storage-intro-and-deep-dive-xing-yang-vmware-jan-safranek-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage%3A+Intro+and+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes SIG Storage: Intro and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyS2/kubernetes-sig-storage-intro-and-deep-dive-xing-yang-vmware-jan-safranek-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage%3A+Intro+and+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zZFN9KMs5sI
- YouTube title: Kubernetes SIG Storage: Intro and Deep Dive - Xing Yang, VMware & Jan Šafránek, Red Hat
- Match score: 0.774
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-sig-storage-intro-and-deep-dive/zZFN9KMs5sI.txt
- Transcript chars: 27178
- Keywords: storage, volume, volumes, snapshot, feature, default, classes, persistent, access, delete, actually, driver, change, minutes, question, maintain, create, snapshots

### Resumo baseado na transcript

uh today yeah and I will be giving an intran deep dive of cool native's sick storage my name is Xin Yang I work at VMware in the cloud native sports team I'm also a co-chair of six storage and I am yanchafronic I'm from Red Hat I work on openshift storage and I am techlete of kubernetes storage so what are we talk what are we going to talk about we will talk about what is sex storage what we did in couple of past releases what is being

### Excerpt da transcript

uh today yeah and I will be giving an intran deep dive of cool native's sick storage my name is Xin Yang I work at VMware in the cloud native sports team I'm also a co-chair of six storage and I am yanchafronic I'm from Red Hat I work on openshift storage and I am techlete of kubernetes storage so what are we talk what are we going to talk about we will talk about what is sex storage what we did in couple of past releases what is being developed right now and most importantly how to get involved in the end we would like to have some time for question and answers and so uh what actually is special interest group Dash storage it's a pretty loose group of people we don't have any onboarding process or graduation you just come and contribute and that's how you become part of six storage we have two code chairs Saturday from Google and xinjiang from VMware and we have two decades Michelle Orr from Google and me from Red Hat we have quite some CSI channels on kubernetes slack here are here are some numbers from the biggest one uh the main six storage channel has 5 000 people on them on it but that doesn't mean that everybody contributes like most people they just come and ask or find something in the history and never say anything on the channel and the group that actually does uh issues answer the questions write pull requests fixed issues work on new features this is pretty small group we have a regular bi-weekly storage Zoom meeting on average we have 24 25 attendees but again not everybody is speaking I would say like 30 percent is active and the last rest is just listening and throughout the time we accumulated a 30 unique sick approvers from our stick in our different repositories and directories and directories of different repositories uh what do we do uh we have a charger for that we basically maintain the storage apis for users like persistent volumes persistent volume claims snapshots snapshot contents storage classes volumes and short classes volume attachments uh storage capacities and so on so all the apis exposed in kubernetes related to storage we maintain them we also maintain the implementation of the SP apis and kubernetes and on the bottom and we maintain kubernetes volume plugins that are in kubernetes kubernetes repository like NFS like RBD and so on except for secret config Maps then download apis for projected and empty theirs we co maintain them with signals because sick node knows better than us how to get a secret in cubelet they alrea
