---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Dave Smith-Uchida", "Veeam"]
sched_url: https://kccncna2025.sched.com/event/27NnH/kubernetes-data-protection-wg-intro-deep-dive-dave-smith-uchida-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes Data Protection WG Intro & Deep Dive - Dave Smith-Uchida, Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Dave Smith-Uchida, Veeam
- Schedule: https://kccncna2025.sched.com/event/27NnH/kubernetes-data-protection-wg-intro-deep-dive-dave-smith-uchida-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NnH/kubernetes-data-protection-wg-intro-deep-dive-dave-smith-uchida-veeam
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Intro+%26+Deep+Dive+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dKl_OaNlpOA
- YouTube title: Kubernetes Data Protection WG Intro & Deep Dive - Dave Smith-Uchida, Veeam
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-data-protection-wg-intro-deep-dive/dKl_OaNlpOA.txt
- Transcript chars: 18294
- Keywords: application, backup, snapshot, restore, volume, protection, metadata, storage, actually, running, working, impact, strategy, support, replication, operators, persistent, blocks

### Resumo baseado na transcript

Thank you for coming to our session on the data protection working group. I'm also co-chair of Kubernetes 6 storage and the data protection working group working with Dave. Those workloads moving to Kubernetes to take advantage Kubernetes self-healing ability, agile deployment, the built-in scalability and portability. So we need to have a better way to support data protection in Kubernetes. This figure shows the backup workflow with existing and missing building blocks in Kubernetes. Yellow means work in progress and orange means missing Kubernetes components.

### Excerpt da transcript

Hello everyone. Thank you for coming to our session on the data protection working group. My name is Shing Yang. I work at VML by Borcon. I'm also co-chair of Kubernetes 6 storage and the data protection working group working with Dave. >> Hi, I'm Dave Smith. I work at VH on our Kubernetes backup products. >> Here's our agenda today. We will give an update on what we did in this working group, who are involved, the motivation for establishing this working group and some projects we're working on and a white paper that we're working on. And finally, how to get involved. We wrote a white paper a while ago on the data protection workflows in Kubernetes. Here are also some links to our previous talks at CubeCons. Here are some companies that are supporting this uh data protection working group listed here. In Kubernetes, day one operations for stable workloads are well supported. We have persistent volumes and persistent volume claims to support the volume operations. We have workload APIs such as deployment and safe staple set to manage um the workload and more and more staple workloads are moving to Kubernetes.

Those workloads moving to Kubernetes to take advantage Kubernetes self-healing ability, agile deployment, the built-in scalability and portability. On the other hand, day two operations such as data protection are still limited. Git ops workflow has limitations on the support for stable workloads. Secrets, config maps and data stored in persistent volumes are not on the git. So we need to have a better way to support data protection in Kubernetes. That's why we formed this working group. This working group is sponsored by both SIG storage and SIG apps. This figure shows the backup workflow with existing and missing building blocks in Kubernetes. The blue color shows the process. The green color shows existing Kubernetes components. Yellow means work in progress and orange means missing Kubernetes components. To back up an application in Kubernetes, we need to back up two pieces of data. We need to back up Kubernetes metadata and we need back up the data stored in persistent volumes. For the volume backup, there are two approaches.

We can either use the native data dump such as my SQL dump or we could use controller coordinated approach to take a snapshot. To ensure application consistency, we need to quiet the luplication before taking the snapshot and unquest afterwards. Both the Kubernetes metadata and volume data needs to be exported to a backup
