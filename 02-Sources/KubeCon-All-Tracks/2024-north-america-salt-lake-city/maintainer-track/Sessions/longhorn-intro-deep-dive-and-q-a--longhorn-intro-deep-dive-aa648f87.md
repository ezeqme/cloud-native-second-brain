---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Phan Le", "SUSE"]
sched_url: https://kccncna2024.sched.com/event/1hoxZ/longhorn-intro-deep-dive-and-q+a-phan-le-suse
youtube_search_url: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%2BA+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Longhorn: Intro, Deep Dive and Q+A - Phan Le, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Phan Le, SUSE
- Schedule: https://kccncna2024.sched.com/event/1hoxZ/longhorn-intro-deep-dive-and-q+a-phan-le-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%2BA+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Longhorn: Intro, Deep Dive and Q+A.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxZ/longhorn-intro-deep-dive-and-q+a-phan-le-suse
- YouTube search: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%2BA+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D67v0SpjJgQ
- YouTube title: Longhorn: Intro, Deep Dive and Q+A - Sheng Yang, SUSE
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/longhorn-intro-deep-dive-and-q-a/D67v0SpjJgQ.txt
- Transcript chars: 25202
- Keywords: engine, storage, volume, replica, object, cluster, workload, support, obviously, performance, replicas, backup, device, create, available, feature, maintain, snapshot

### Resumo baseado na transcript

hi welcome to this session and we talk about Longhorn so my name is Shong I'm engineering director for France sua and I'm the original author of Lorn and uh as you know Rancher as the also the original company behind longor has bought into the soua three two three years ago so I hope at least some of you here know what L horn is but just to recap Lorn is a way to give you you persistent story support for any kues clusters and you can easily instore spdk is a storage performance development kit developed by the Intel originally for its oown hard drive and this is very high performance using pooling instead of interrupt to getting the maximum IO possible and by like basically Rewritten the L engine based on S spdk we have achieved neon na performance for the V2 engine and for the window 6 release which is due to which is due um January next year we are going to have a core feature functionality priority like snapshot backup and those um features will be available we are also introducing the object storage volume which is provide you a S3 end point to using within the long for directly you can find out more road map information at GitHub Lor VK road map and let's talk about like

### Excerpt da transcript

hi welcome to this session and we talk about Longhorn so my name is Shong I'm engineering director for France sua and I'm the original author of Lorn and uh as you know Rancher as the also the original company behind longor has bought into the soua three two three years ago so I hope at least some of you here know what L horn is but just to recap Lorn is a way to give you you persistent story support for any kues clusters and you can easily instore it it's easy to use Easy to maintain and it's open source as no string attached and you can find out more details at L horn. and there are a few things when we design Lorn we take to our heart as a design principles and obviously when you design a new storage product from ground up there have to be some focus and some compromise to be made and the Lor focus on three things relability usability and maintainability so in the reliability side long form is essentially backing by the block devices created by the long storage layer and is Crash consistent we have also building a multiple layer of protection against the data loss so in Lor itself within the cluster you have the in cluster snapshot mechanism which able to like periodically snapshot your volumes whenever you need it and you have also a out of cluster backup mechanism build in and with no third party like software required to enable you to backup your data to outside the cluster like S3 or NFS endpoint in case like you have the whole clust that went down and you cannot find any copy of things like your data center in the worst case would uping fires you still have a copy of your data somewhere else to keep you safe and more than that in fact longor itself has been built to be very resilient and if you have the scenario you have the whole cluster R down with like say your control plane kubernetes everything is down as long as you still have the hard drive Le hor can recover your full data from that without like really have to go you don't need to go through very complicated recover step is very simple so those kind of protection we add in based on our experience on the previous other products that's is the one Focus that's the biggest Focus for the Lorn the second Focus for the Lorn as in fact for old products and pro projects from the raner labs is the usability so from day one L hornn is designed to be simple to use Simple to deploy you can deploy L horn in one click installation you can do the helm chart install you can do the like yam apply and obvious
