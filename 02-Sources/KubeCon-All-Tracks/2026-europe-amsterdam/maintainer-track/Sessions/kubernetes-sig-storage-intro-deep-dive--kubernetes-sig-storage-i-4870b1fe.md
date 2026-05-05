---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Xing Yang", "VMware by Broadcom", "Jan Šafránek", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF70/kubernetes-sig-storage-intro-deep-dive-xing-yang-vmware-by-broadcom-jan-safranek-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, VMware by Broadcom & Jan Šafránek, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Xing Yang, VMware by Broadcom, Jan Šafránek, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF70/kubernetes-sig-storage-intro-deep-dive-xing-yang-vmware-by-broadcom-jan-safranek-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Kubernetes SIG Storage: Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF70/kubernetes-sig-storage-intro-deep-dive-xing-yang-vmware-by-broadcom-jan-safranek-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tGSEyEdh5ug
- YouTube title: Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, Michelle Au, Hemant Kumar
- Match score: 0.765
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/kubernetes-sig-storage-intro-deep-dive/tGSEyEdh5ug.txt
- Transcript chars: 47287
- Keywords: volume, driver, storage, actually, feature, basically, volumes, cluster, snapshot, features, working, health, question, drivers, object, topology, meetings, deployment

### Resumo baseado na transcript

We will talk about what is six storage, what we did in Kubernetes 1.33 and 1.34 release, what we're working on in 1.35 and beyond, and finally how to get involved in S storage. We maintain Kubernetes APIs related to storage like persistent volume claims, persistent volumes, storage classes, volume snapshots. Without this feature, the PV reclaim policy is ignored sometimes depending on whether you try to delete PVC first or try to delete PV first, leaving storage resources behind. th00and terabyte and that operation didn't work and previously you will be stuck actually you'll have to ask your cloud provider storage provider or cluster admin to bail you out and it required a bunch of manual intervention and it was not nice user experience So overall the operation should the uh resizing should be much more robust than uh kubernetes 134. The idea is that you let's say on you're running on AWS and you want to convert a GP3 volume to IO2 because your application needs more performance u more IOPS more throughput.

### Excerpt da transcript

Hello everyone. Thank you for coming to our session on seek storage. My name is Shinyang. I work at VMwell by Brocon. >> Hi, I'm Michelle. Um, I work at Google. >> I'm Hmon. I work at Redhead. >> Here's today's agenda. We will talk about what is six storage, what we did in Kubernetes 1.33 and 1.34 release, what we're working on in 1.35 and beyond, and finally how to get involved in S storage. Sad and myself are co-chairs. Michelle and Young are tech leads. Other than the leads, we also have many other contributors. What we do in six storage is defining our charter. We maintain Kubernetes APIs related to storage like persistent volume claims, persistent volumes, storage classes, volume snapshots. We also maintain code around those API objects like dynamic provisioning of volumes and snapshots. We maintain volume plugins like NFS, icecazzi plugins. We co-own projected volumes like secrets and config maps with sik node. We designed container storage interface CSI so that sushi vendor can write a driver that allows their storage system to be consumed by containers running in the Kubernetes cluster.

We maintain CSI set cards. CSS set cards watch Kubernetes API objects and trigger appropriate volume operations against a CSI driver. Most CSI drivers are owned by Sik cloud provider or other communities. We also designed container object storage interface coy that provides APIs so that you can provision a object bucket just like how APVC is provisioned. Now let me talk about what we did in 1.33 release. The volume populated feature multitude GA in 1.33. Previously you can create a PVC from a data source that is either a volume snapshot or another PVC. But there are use cases that require us to prepopulate volumes with other data sources. For example, during a backup, you first create a volume snapshot from a PBC. You upload that snapshot data to a object store. Then at the restore time, you want to be able to create a PVC from this backup. So this backup will be another external data source that is not a PVC or volume snapshot. That's why we introduced this feature that allows generic data populators by permitting any object from uh the data source for PBC.

We introduced a new data source ref field. If original data source is specified, it will be copied to the new data source ref field. The original data source will always be supported. There are some differences between those two fields. Data source is for local object only. Data source ref can be any object fr
