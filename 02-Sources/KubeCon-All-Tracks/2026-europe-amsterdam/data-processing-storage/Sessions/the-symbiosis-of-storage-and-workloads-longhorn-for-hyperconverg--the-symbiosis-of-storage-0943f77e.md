---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Jinhong Kim", "Jangseon Ryu", "NAVER Corp"]
sched_url: https://kccnceu2026.sched.com/event/2CW48/the-symbiosis-of-storage-and-workloads-longhorn-for-hyperconverged-block-storage-jinhong-kim-jangseon-ryu-naver-corp
youtube_search_url: https://www.youtube.com/results?search_query=The+Symbiosis+of+Storage+and+Workloads%3A+Longhorn+for+Hyperconverged+Block+Storage+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Symbiosis of Storage and Workloads: Longhorn for Hyperconverged Block Storage - Jinhong Kim & Jangseon Ryu, NAVER Corp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jinhong Kim, Jangseon Ryu, NAVER Corp
- Schedule: https://kccnceu2026.sched.com/event/2CW48/the-symbiosis-of-storage-and-workloads-longhorn-for-hyperconverged-block-storage-jinhong-kim-jangseon-ryu-naver-corp
- Busca YouTube: https://www.youtube.com/results?search_query=The+Symbiosis+of+Storage+and+Workloads%3A+Longhorn+for+Hyperconverged+Block+Storage+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Symbiosis of Storage and Workloads: Longhorn for Hyperconverged Block Storage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW48/the-symbiosis-of-storage-and-workloads-longhorn-for-hyperconverged-block-storage-jinhong-kim-jangseon-ryu-naver-corp
- YouTube search: https://www.youtube.com/results?search_query=The+Symbiosis+of+Storage+and+Workloads%3A+Longhorn+for+Hyperconverged+Block+Storage+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qNxIebuifp8
- YouTube title: The Symbiosis of Storage and Workloads: Longhorn for Hyperconverged Bl... Jinhong Kim & Jangseon Ryu
- Match score: 0.942
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-symbiosis-of-storage-and-workloads-longhorn-for-hyperconverged-blo/qNxIebuifp8.txt
- Transcript chars: 20857
- Keywords: storage, capacity, scheduling, replicas, workload, replica, longhorn, already, application, placement, volume, locality, neighbor, performance, volumes, replication, available, placed

### Resumo baseado na transcript

Uh today we'd like to share our experience operating large scale stories and neighbor and this scale we faced the several challenges and cost efficiency performance interference and operational complexity. So in this talk we'll talk about uh how we apply a hyper composite model using longhorn and how it helped us improve our system. So but storage we operate a large stepbased platform with about 5,000 node and roughly 50,000 disk in total this provide around 100 pabytes lo capacities and today we served around 250,000 persistent volumes. Our infrastructure is built in on a centralized SE storage platform and SE works very well but however the centralized model doesn't fit every type of workload. So those application already handled replication at the application layer and when you place them on top of distributed storage some inefficiency and side effect began to appear. That's when we start to listen what kind of storage model would better fit these workload.

### Excerpt da transcript

Hi everyone, good afternoon. Thank you for joining us today. Uh today we'd like to share our experience operating large scale stories and neighbor and this scale we faced the several challenges and cost efficiency performance interference and operational complexity. So in this talk we'll talk about uh how we apply a hyper composite model using longhorn and how it helped us improve our system. Before we dive in let us briefly introduce ourselves. My name is Jang newu and I'm a senior technical lead on container storage team and neighbor. I'm joined today by my coreer Gino Kim from the same team. Today we'll walk you through the background and challenges and Chino will explain how we solve them in detail. So who is neighbor? Neighbor is one of leading internet company in South Korea providing a wide range digital services. Our services include such content, e-commerce, fintech and cloud services. Million of users use neighbor every day and generate massive traffic and data. So neighbor scale we operate kubernetes across roughly 60,000 node and running around 90 900,000 path in production.

So but storage we operate a large stepbased platform with about 5,000 node and roughly 50,000 disk in total this provide around 100 pabytes lo capacities and today we served around 250,000 persistent volumes. Our infrastructure is built in on a centralized SE storage platform and SE works very well but however the centralized model doesn't fit every type of workload. So especially distribute application like capka open source sheet and betest. So those application already handled replication at the application layer and when you place them on top of distributed storage some inefficiency and side effect began to appear. That's when we start to listen what kind of storage model would better fit these workload. So this led us to hyper converged approaching. So let's first look at the problem we faced and then we were trying to solve. So first major issue we faced was cost inefficiency. This inefficiency was caused by duplicate replication se by design use three-way replication or irre coding with roughly one and a half times redundancy.

So at at the same time many distributed application also replicate their data usually two copies sometimes three copies. So when you stack these layer together, replication quickly adds up. In the worst case, the same data stored up to nine time. It also affect performance through IO amplification. So I mean more copies means more IO. The sec
