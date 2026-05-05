---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Xinye Tao", "Jinpeng Zhang", "PingCAP"]
sched_url: https://kccnceu2022.sched.com/event/ytoM/adapting-tikv-for-cloud-storage-xinye-tao-jinpeng-zhang-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=Adapting+TiKV+for+Cloud+Storage+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Adapting TiKV for Cloud Storage - Xinye Tao & Jinpeng Zhang, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Xinye Tao, Jinpeng Zhang, PingCAP
- Schedule: https://kccnceu2022.sched.com/event/ytoM/adapting-tikv-for-cloud-storage-xinye-tao-jinpeng-zhang-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=Adapting+TiKV+for+Cloud+Storage+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Adapting TiKV for Cloud Storage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoM/adapting-tikv-for-cloud-storage-xinye-tao-jinpeng-zhang-pingcap
- YouTube search: https://www.youtube.com/results?search_query=Adapting+TiKV+for+Cloud+Storage+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hzzHn6oiOp8
- YouTube title: Adapting TiKV for Cloud Storage - Xinye Tao & Jinpeng Zhang, PingCAP
- Match score: 0.74
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/adapting-tikv-for-cloud-storage/hzzHn6oiOp8.txt
- Transcript chars: 6922
- Keywords: storage, hardware, engine, actually, performance, reduce, improve, limits, cost, multiple, resources, write, simple, priority, priorities, overflow, distributed, traditional

### Resumo baseado na transcript

hi everyone i am tau xin yue i'm a senior engineer from pincap which is a company behind thai tv in the past few months my team and i has putting a lot of efforts to make tech tv work better on cloud storage and today i'm going to share with you some of those new improvements that we are very excited about just before we dive in i think we should get a basic understanding of the situation first let's take a look at techyv long story short it strategy that we are pushing for low resources environments such as four core machines basically we want to smoothly apply that back pressure to the user before system is overloaded and the raft witness it is an attempt to reduce replication cost by using a

### Excerpt da transcript

hi everyone i am tau xin yue i'm a senior engineer from pincap which is a company behind thai tv in the past few months my team and i has putting a lot of efforts to make tech tv work better on cloud storage and today i'm going to share with you some of those new improvements that we are very excited about just before we dive in i think we should get a basic understanding of the situation first let's take a look at techyv long story short it is a distributed storage engine unlike traditional storage engines that serve on a single machine it have the capability to scale out normally to hundreds of nodes and we need to replicate both wall and data files to provide high availability which is actually one of the reason that we are willing to tolerate the complexity of a distributed system now let's move on to the hardware design nowadays most public cloud vendors provide virtualized disks and those disks can be mounted to a local file system and they appear like a local disk as well but internally they're forwarding the ios to multiple remote disks that are potentially shelled by multiple users ebs for instance will replicate any right ios to three different locations and this internal complexity can be a real problem for our systems because the latency for stutter is obviously higher than a local disk also since you are sharing hardware with other users anything that you use will be charged that includes disk bandwidth and iops finally we should all know that cloud infrastructure are not always as reliable as they claim it to be service degradation will be relatively frequent and it should be considered in our system design ideally we want to make a large type v cluster behave similarly to a traditional rdbms unfortunately it's actually hard to accomplish that on a cloud storage first we want to build a scalable service the scale means more failures to be more specific we are worried that as the system this hardware the storage hardware performance is more likely to degrade because on a larger scale a real event will not be so rare anymore the cost is a problem too because every storage operation is charged by the cloud vendors the users now have more reasons to care about exactly how and why our system is using those resources and by that i mean read and write amplification which is the amount of files the system needs to issue before finishing one user request here i drew a simple graph to demonstrate our system's runtime usage of io resources over time the
