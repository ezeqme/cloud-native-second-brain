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
speakers: ["Xing Yang", "VMware", "Jan Šafránek", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE7S/kubernetes-sig-storage-intro-and-update-xing-yang-vmware-jan-safranek-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG-Storage+Intro+and+Update+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes SIG-Storage Intro and Update - Xing Yang, VMware & Jan Šafránek, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Xing Yang, VMware, Jan Šafránek, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE7S/kubernetes-sig-storage-intro-and-update-xing-yang-vmware-jan-safranek-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG-Storage+Intro+and+Update+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes SIG-Storage Intro and Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7S/kubernetes-sig-storage-intro-and-update-xing-yang-vmware-jan-safranek-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG-Storage+Intro+and+Update+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dedCB6kPJlc
- YouTube title: Kubernetes SIG-Storage Intro and Update - Xing Yang, VMware & Jan Šafránek, Red Hat
- Match score: 0.758
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-sig-storage-intro-and-update/dedCB6kPJlc.txt
- Transcript chars: 18431
- Keywords: volume, storage, feature, volumes, snapshot, capacity, features, snapshots, drivers, persistent, release, working, provides, generic, backup, tracking, expansion, please

### Resumo baseado na transcript

hello everyone today yeah and i will be giving an introduction and update to kubernetes sixth storage my name is shinya i work at the vmware at the cloud storage team i'm a co-chair of kubernetes storage along with sadali from google and i am jansha franek working for red hat and i am tech lead together with michelle oh from google so here is today's agenda first we'll talk about what is seek storage then we will talk about what we did in 1.20 and when dot 21 releases

### Excerpt da transcript

hello everyone today yeah and i will be giving an introduction and update to kubernetes sixth storage my name is shinya i work at the vmware at the cloud storage team i'm a co-chair of kubernetes storage along with sadali from google and i am jansha franek working for red hat and i am tech lead together with michelle oh from google so here is today's agenda first we'll talk about what is seek storage then we will talk about what we did in 1.20 and when dot 21 releases we'll talk about what we are working on for the future and talk about crosstic working groups and projects finally we will talk about how to get involved so what is sig storage sig storage is a special interest group that focuses on how to provide storage to parts in your kubernetes cluster sixth storage's scope is in the storage control plane it provides a way for containers in the pods to consume block of fire storage this can be persistent long-term storage that leaves beyond the pots lifecycle or it can be effemoral temporary storage which becomes available when the pot is started and goes away when pod goes down seek storage is responsible for the life cycle of volumes used by pots this includes provisioning a new volume attaching a volume to the node and mounting it so that part can use it i'll mounting detaching and deleting the volume when it is no longer needed taking snapshots so that it can be used to restore the volume if the original volume is corrupted for some reason six storage also looks at how to influence the scheduling decisions based on topology information to see whether the storage is accessible to a node and make sure one is scheduled to a node which can have access to the storage also storage is responsible for managing storage capacity managing quota based on the capacities or number of resources and provides ability to expand volume if a volume runs low in space slick throw reach owns the persistent volume and position volume claim feature this allows storage vendor to create a volume and possess data in a volume which can be preserved even if the pod goes away we have the suit class concept a student class provides a way for administrators to describe the classes of storage they offer different classes might map to different quality of service levels in dynamic provisioning student class is used to find out which provisioner should be used and what parameters should be passed to the provisioner when creating the volume sig storage has been working on migrating from
