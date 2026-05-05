---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Mark Lavi", "Carl Braganza", "Prasad Ghangal", "Veeam", "Xing Yang", "VMware by Broadcom"]
sched_url: https://kccnceu2025.sched.com/event/1txF7/kubernetes-backup-legitimized-csi-changed-block-tracking-has-arrived-mark-lavi-carl-braganza-prasad-ghangal-veeam-xing-yang-vmware-by-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Backup+Legitimized%3A+CSI+Changed+Block+Tracking+Has+Arrived+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived - Mark Lavi, Carl Braganza & Prasad Ghangal, Veeam; Xing Yang, VMware by Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Mark Lavi, Carl Braganza, Prasad Ghangal, Veeam, Xing Yang, VMware by Broadcom
- Schedule: https://kccnceu2025.sched.com/event/1txF7/kubernetes-backup-legitimized-csi-changed-block-tracking-has-arrived-mark-lavi-carl-braganza-prasad-ghangal-veeam-xing-yang-vmware-by-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Backup+Legitimized%3A+CSI+Changed+Block+Tracking+Has+Arrived+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txF7/kubernetes-backup-legitimized-csi-changed-block-tracking-has-arrived-mark-lavi-carl-braganza-prasad-ghangal-veeam-xing-yang-vmware-by-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Backup+Legitimized%3A+CSI+Changed+Block+Tracking+Has+Arrived+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=U9qwxp7Uv08
- YouTube title: Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived- M. Lavi, C. Braganza, X. Yang
- Match score: 0.925
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-backup-legitimized-csi-changed-block-tracking-has-arrived/U9qwxp7Uv08.txt
- Transcript chars: 25088
- Keywords: snapshot, driver, metadata, backup, volume, blocks, snapshots, application, change, sidecar, storage, feature, create, tracking, vendors, allocated, support, software

### Resumo baseado na transcript

I'm also a co-chair of Kubernetes 6 storage and the data protection working group. I'm uh the open source product manager at VH Casten and I'm joined by one of my colleagues. Well, I don't want to take a whole another backup, a whole another consumption of storage, network compute, and memory. So that is what change block tracking brings and we've brought this forward because everybody is coming to Kubernetes from the VM world right now. We've changed that and this is a critical unblocker for for Kubernetes adoption. Uh the design has gone through three major iterations and we've had lots of fun defending, improving, going backwards, improving again and defending over three major revisions.

### Excerpt da transcript

Hello everyone. Thank you for coming to our session on the change block tracking. My name is Shing Yang. Uh I work for VMware by Broadcom. I'm also a co-chair of Kubernetes 6 storage and the data protection working group. Uh Rob, can you help us with that? No. All right, we'll we'll talk over them. Hi, I'm Mark Lobby. I'm uh the open source product manager at VH Casten and I'm joined by one of my colleagues. He'll tell us about the other colleague just now. Hi, I'm KL Banza. I'm one of the technical staff at BH. Uh I'm one of the co-authors of the CBT cap in Kubernetes. Uh Prasad and Ivan are two others. Prasad was going to join us today but unfortunately couldn't make it. Um, I'm also one of the authors of the CSI edition for this cap. Right. All right. I'll just try to talk over him. All right. Today we're going to go over change block tracking, its motivation, history, architecture, implementation with respect to Kubernetes. We'll demonstrate a workflow and then leave you with resources and how to get involved.

We want you to adopt it and we'll answer any Q&A at the end. With that, let's get started. So, change block tracking is what everybody expects when it comes to Kubernetes and cloudnative storage and applications. However, it is a lacking feature when we compare to traditional storage. How do you do the difference between any two volume snapshots? Well, you need to take another full backup. But everybody else in traditional VMs and bare metal world already has this. So in in order to come down on what we measure RPO, RTO for all backup and recovery and disaster recovery, we need to be able to get to change block tracking in order to make sure that if the difference between any two volume snapshots is nothing. Well, I don't want to take a whole another backup, a whole another consumption of storage, network compute, and memory. No, I want a zero delta, zero metadata pointers, etc. Right. So that is what change block tracking brings and we've brought this forward because everybody is coming to Kubernetes from the VM world right now.

They want change block tracking because they expect it and you needed to go to a proprietary vendor's driver in order to get change block tracking or explain why it doesn't work with CSI. We've changed that and this is a critical unblocker for for Kubernetes adoption. We created kept 3314 to do this and we have now completed implementation. So the history is that we started this well over two years ago at the data prot
