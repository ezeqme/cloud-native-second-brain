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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Steven Wong", "Myles Gray", "VMware"]
sched_url: https://kccnceu2021.sched.com/event/iE7q/kubernetes-vmware-ug-whats-new-for-k8s-users-on-vmware-infrastructure-steven-wong-myles-gray-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+VMware+UG%3A+What%E2%80%99s+New+for+K8s+Users+on+VMware+Infrastructure+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes VMware UG: What’s New for K8s Users on VMware Infrastructure - Steven Wong & Myles Gray, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Steven Wong, Myles Gray, VMware
- Schedule: https://kccnceu2021.sched.com/event/iE7q/kubernetes-vmware-ug-whats-new-for-k8s-users-on-vmware-infrastructure-steven-wong-myles-gray-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+VMware+UG%3A+What%E2%80%99s+New+for+K8s+Users+on+VMware+Infrastructure+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes VMware UG: What’s New for K8s Users on VMware Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7q/kubernetes-vmware-ug-whats-new-for-k8s-users-on-vmware-infrastructure-steven-wong-myles-gray-vmware
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+VMware+UG%3A+What%E2%80%99s+New+for+K8s+Users+on+VMware+Infrastructure+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O9v0G5VXHZw
- YouTube title: Kubernetes VMware UG: What’s New for K8s Users on VMware Infrastructure - Steven Wong & Myles Gray
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-vmware-ug-whats-new-for-k8s-users-on-vmware-infrastructure/O9v0G5VXHZw.txt
- Transcript chars: 10997
- Keywords: storage, deprecation, channel, provider, driver, vsphere, running, vmware, session, little, version, feature, support, infrastructure, issues, probably, topics, features

### Resumo baseado na transcript

hi welcome to the kubecon europe session for the kubernetes vmware user group i'm steve wong co-chair of the group i'm a software engineer assigned to work on the kubernetes project i'm joined today by miles gray but he's had some internet access issues during this recording but he helped with material and he'll be joining us on the day of the presentation for q a miles is based in europe and he's an authority on the subject of storage and kubernetes we'll give a link to this deck at

### Excerpt da transcript

hi welcome to the kubecon europe session for the kubernetes vmware user group i'm steve wong co-chair of the group i'm a software engineer assigned to work on the kubernetes project i'm joined today by miles gray but he's had some internet access issues during this recording but he helped with material and he'll be joining us on the day of the presentation for q a miles is based in europe and he's an authority on the subject of storage and kubernetes we'll give a link to this deck at the end and we'll hang around for q a the plan for today is to start with some material on how deprecation of the entry cloud provider and the entry storage driver might impact you as a user by the way it's possible the answer will be that it won't impact you at all then we'll move on to cover recent and planned feature enhancements and changes third we'll quickly go over a top three list of do's and don'ts when running kubernetes on vmware infrastructure finally we'll wrap up with information on how to join the user group so we'll start with coverage of deprecation of entry both cloud provider and storage driver and what it means the expected time frame or should i say release frame for the entry removal is kubernetes 1.24 if you deployed kubernetes on vsphere recently you probably used the out of tree provider and the csi storage driver in this case the next few slides don't affect you but please hang around because we have coverage of other other topics coming right up if you are affected don't fret the new stuff has a lot of valuable features uh feature enhancements of going up have been going on exclusively in the out of tree components for over a year now so this shift to the new stuff is probably going to be a good experience ultimately even if there's a little work to do in the short term by the way if you're on a commercial distribution please follow your vendor's guidance regarding migration i'm covering this on a generic version that might apply if you're using pure upstream kubernetes but it's possible that your vendor has added features to support a migration and you'd be best advised to follow their advice if you're faced with a migration an important thing to note is you must first upgrade you must upgrade the cloud provider and the storage driver at the same time cross coupling an old version of one with a new version of another simply doesn't work also if you're unlucky enough to be hosting kubernetes on an old vsphere version or and or with old hardware it mi
