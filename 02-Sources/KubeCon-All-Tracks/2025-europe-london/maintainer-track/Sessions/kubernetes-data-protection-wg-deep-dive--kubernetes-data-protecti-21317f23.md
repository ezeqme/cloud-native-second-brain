---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Dave Smith-Uchida", "Veeam"]
sched_url: https://kccnceu2025.sched.com/event/1tcyW/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes Data Protection WG Deep Dive - Dave Smith-Uchida, Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Dave Smith-Uchida, Veeam
- Schedule: https://kccnceu2025.sched.com/event/1tcyW/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyW/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=joOTwCatd9g
- YouTube title: Kubernetes Data Protection WG Deep Dive - Dave Smith-Uchida, Veeam
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-data-protection-wg-deep-dive/joOTwCatd9g.txt
- Transcript chars: 23725
- Keywords: application, backup, restore, actually, volume, protection, storage, working, volumes, consistency, replication, database, snapshot, multiple, impact, applications, strategy, everything

### Resumo baseado na transcript

Hello everyone, welcome to our data pro protection working group session. I'm also a co-chair of Kubernetes 6 storage and the data protection wing group working with Dave. So we need to have a better way to support data protection in kubernetes. This figure shows the backup workflow with missing and existing building blocks in Kubernetes. To back up an application in Kubernetes, we need to back up two pieces of data. We need to back up the Kubernetes metadata and we also need to back up the data stored in persistent volumes.

### Excerpt da transcript

Hello everyone, welcome to our data pro protection working group session. My name is Shinyang. I work at VML by BRCON. I'm also a co-chair of Kubernetes 6 storage and the data protection wing group working with Dave. Hi, I'm Dave Smith. I work at VH and I hand it back to you. Yeah. So, here's today's agenda. Uh we're going to discuss what we have done for the working group who are involved what is the motivation for establishing the working group and we will discuss some of the projects and the white paper that we are working on and finally how to get involved. Here are some key updates. We wrote a white paper on the data protection workflow in Kubernetes a while ago. We also rec recently updated the annual report for 2024. Here are some links to previous presentations at CubeCon. Uh here we listed companies who are supporting this data protection working group in Kubernetes. The day one operations for stay for workloads are well supported. We have persistent volumes and persistent volume claims for the volume operations and we have workload APIs such as deployment and stifle set for declarative management of your stafer workloads.

More and more stafer workloads are moving to Kubernetes. This workloads moving to Kubernetes to take advantage of Kubernetes self-healing abilities, agile deployment, the built-in scalability and port portability. However, D2 operations for stafer workloads such as data protection are still limited. The git ops workflow has limitation in supporting state for workload secrets, config maps and data stored in persistent volumes are not stored in the git. So we need to have a better way to support data protection in kubernetes. That's why we started this data protection working group. Uh this working group is sponsored by both sik storage and sik apps. This figure shows the backup workflow with missing and existing building blocks in Kubernetes. The blue color shows the process. The green color shows existing Kubernetes components. Yellow means it is work in progress. Orange means it is a missing Kubernetes component. To back up an application in Kubernetes, we need to back up two pieces of data. We need to back up the Kubernetes metadata and we also need to back up the data stored in persistent volumes.

To back up data in the persistent volumes, there are two ways. We can either do a uh native data dump such as my SQL dump or we can back it up using the controller coordinated approach while a volume snapshot is taken to ensure ap
