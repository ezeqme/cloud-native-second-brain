---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Sunny Bains", "Yang Zhang", "PingCAP"]
sched_url: https://kccncna2022.sched.com/event/182P5/how-we-make-tikv-a-distributed-storage-more-cost-effective-on-the-cloud-sunny-bains-yang-zhang-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Make+TiKV+-+a+Distributed+Storage%2C+More+Cost-Effective+On+the+Cloud+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How We Make TiKV - a Distributed Storage, More Cost-Effective On the Cloud - Sunny Bains & Yang Zhang, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Sunny Bains, Yang Zhang, PingCAP
- Schedule: https://kccncna2022.sched.com/event/182P5/how-we-make-tikv-a-distributed-storage-more-cost-effective-on-the-cloud-sunny-bains-yang-zhang-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Make+TiKV+-+a+Distributed+Storage%2C+More+Cost-Effective+On+the+Cloud+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How We Make TiKV - a Distributed Storage, More Cost-Effective On the Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182P5/how-we-make-tikv-a-distributed-storage-more-cost-effective-on-the-cloud-sunny-bains-yang-zhang-pingcap
- YouTube search: https://www.youtube.com/results?search_query=How+We+Make+TiKV+-+a+Distributed+Storage%2C+More+Cost-Effective+On+the+Cloud+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vYMbmb01IsU
- YouTube title: How We Make TiKV- a Distributed Storage, More Cost-Effective On the Cloud - Sunny Bains & Yang Zhang
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-we-make-tikv-a-distributed-storage-more-cost-effective-on-the-clou/vYMbmb01IsU.txt
- Transcript chars: 19801
- Keywords: storage, called, process, traffic, resource, leader, engine, cost, architecture, reduce, actually, computational, groups, followers, around, ending, mentioned, another

### Resumo baseado na transcript

so I work on the storage side of things on Thai KV and prior to this I used to work for Oracle on MySQL and I was the lead on innodb and recently I joined incap and my experience is limited but I do work on the storage side of time KV and this is my colleague Andy he's been working longer on Thai caving and so he'll take it from here and we'll talk about you know how we make Thai caving more cost effective and that's okay uh

### Excerpt da transcript

so I work on the storage side of things on Thai KV and prior to this I used to work for Oracle on MySQL and I was the lead on innodb and recently I joined incap and my experience is limited but I do work on the storage side of time KV and this is my colleague Andy he's been working longer on Thai caving and so he'll take it from here and we'll talk about you know how we make Thai caving more cost effective and that's okay uh hello everyone um my name is Andy uh I'm a software engineer of pin cap and I work on TI TV prior to pin cap I worked for Google spanner team and so here I am um our topic today is about making TI TV our distribute storage engine more cost effective on the cloud so here's the agenda at first I'm going to give you like a brief overview of GI TV and then I will show you some of our own experience building a cloud service and yeah that's it and then last I will give you some examples like how we do like Cloud cost effective Works um and as well as some like Works we're doing and they will be down in the future uh so first uh what is Thai KV So Thai KV is an open source uh distributed distributed and transactional K Value Store so it's written in Rust program programming language from day one uh around like seven years ago so we were so glad we make the right decision and it was a tough decision to make and since as cubican and cncf Conference I'm honored to mention that pin cap donate tiqv to cnsf Foundation like three years ago and now as a graduated product of cncf and I gave the link below that's our GitHub link you can search it online so you know tikv as a storage engine has been um globally adopted by many users in many different scenarios so here are some examples um you know we are infrastructure for infrastructure in some cases like there's a file system called juice FS they use TI TV as their like metadata storage and the the TD Cloud object storage also use us as their metadata stories um so there's also like a blockchain company called like Harmony Harmony they use TI TV to store the blocking data as well uh I guess it's probably the super super node or something um I'm not sure like whether you guys play mobile games or not but uh I guess you know like Pokemon go uh and the company behind Pokemon go Niantic they use tikv as a like transactional key Value Story um so you know we are open source uh project so we have a large community and like many community members did a lot of great things like around techyv so they build a r
