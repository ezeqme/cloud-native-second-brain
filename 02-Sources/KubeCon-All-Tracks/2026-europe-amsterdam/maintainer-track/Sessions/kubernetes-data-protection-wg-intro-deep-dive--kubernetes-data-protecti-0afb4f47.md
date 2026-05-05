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
speakers: ["Dave Smith-Uchida", "Veeam"]
sched_url: https://kccnceu2026.sched.com/event/2EF40/kubernetes-data-protection-wg-intro-deep-dive-dave-smith-uchida-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Kubernetes Data Protection WG Intro & Deep Dive - Dave Smith-Uchida, Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Dave Smith-Uchida, Veeam
- Schedule: https://kccnceu2026.sched.com/event/2EF40/kubernetes-data-protection-wg-intro-deep-dive-dave-smith-uchida-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF40/kubernetes-data-protection-wg-intro-deep-dive-dave-smith-uchida-veeam
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=grE_GMC3PlI
- YouTube title: Kubernetes Data Protection WG Intro & Deep Dive - Dave Smith-Uchida, Veeam
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/kubernetes-data-protection-wg-intro-deep-dive/grE_GMC3PlI.txt
- Transcript chars: 17421
- Keywords: backup, bucket, snapshot, operator, restore, volume, access, application, operators, protection, resources, metadata, object, resource, storage, operations, custom, working

### Resumo baseado na transcript

Uh, thanks for coming to our session here for the Kubernetes data protection working group deep dive. I'm a technical leader at Veeam where I work on Kubernetes backup and recovery. This diagram shows the backup workflow with the existing and missing building blocks in Kubernetes. To backup a application in Kubernetes, we need to backup two pieces of data. Both the Kubernetes metadata and data will be exported to a backup repository. This diagram shows the restore workflow with the existing and missing building blocks in Kubernetes.

### Excerpt da transcript

Uh, thanks for coming to our session here for the Kubernetes data protection working group deep dive. I'm Dave Smith Uchida. I'm a technical leader at Veeam where I work on Kubernetes backup and recovery. And uh, this is Xing Yang. Hi everyone. My name is uh, Xing Yang. I work at VMware by Broadcom. I'm also co-chair of Kubernetes six storage and the data protection working group. Here's today's agenda. First, we'll talk about why we established this working group, who are involved, and some of the projects we are working on, and the white paper that we are working on, and finally, how to get involved. In Kubernetes, day one operations for stateful workloads are well supported. We have persistent volume claims, persistent volumes for the volume operations. We have workload APIs such as stateful set with deployment for the declarative management of your stateful workloads. More and more stateful workloads are moving to Kubernetes. On the other hand, day two operations for stateful workloads such as data protection are still limited.

That's why we formed this working group to find a better solution. Here are the companies supporting this initiative listed here. This diagram shows the backup workflow with the existing and missing building blocks in Kubernetes. The blue color shows the process. The green color shows existing Kubernetes components. And yellow means it is work in progress. Orange means it's a missing Kubernetes component. To backup a application in Kubernetes, we need to backup two pieces of data. We need to backup Kubernetes metadata. We need to backup the data stored in persistent volumes. There are two ways to backup the data stored in the volumes. You could use native data dump such as MySQL dump, or you could use controller coordinated approach while a volume snapshot is created. To ensure application consistency, you should quiesce the application before taking the snapshot and unquiesce afterwards. Both the Kubernetes metadata and data will be exported to a backup repository. A backup repository is a location or repo where you can store your data and metadata.

COSI is a project that can be used to support a backup repository such as an object store. I will talk more about COSI and a few other projects shown here later. This diagram shows the restore workflow with the existing and missing building blocks in Kubernetes. To restore application, we first need to import backup from the backup repository. We need to restore Kubernetes metadat
