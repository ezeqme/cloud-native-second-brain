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
themes: ["Storage Data"]
speakers: ["Leonardo Cecchi", "EDB", "Xing Yang", "VMware by Broadcom"]
sched_url: https://kccnceu2025.sched.com/event/1tx8g/consistent-volume-group-snapshots-unraveling-the-magic-leonardo-cecchi-edb-xing-yang-vmware-by-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Consistent+Volume+Group+Snapshots%2C+Unraveling+the+Magic+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Consistent Volume Group Snapshots, Unraveling the Magic - Leonardo Cecchi, EDB & Xing Yang, VMware by Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: United Kingdom / London
- Speakers: Leonardo Cecchi, EDB, Xing Yang, VMware by Broadcom
- Schedule: https://kccnceu2025.sched.com/event/1tx8g/consistent-volume-group-snapshots-unraveling-the-magic-leonardo-cecchi-edb-xing-yang-vmware-by-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Consistent+Volume+Group+Snapshots%2C+Unraveling+the+Magic+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Consistent Volume Group Snapshots, Unraveling the Magic.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8g/consistent-volume-group-snapshots-unraveling-the-magic-leonardo-cecchi-edb-xing-yang-vmware-by-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Consistent+Volume+Group+Snapshots%2C+Unraveling+the+Magic+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=urRefZ0KnU4
- YouTube title: Consistent Volume Group Snapshots, Unraveling the Magic - Leonardo Cecchi, EDB & Xing Yang
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/consistent-volume-group-snapshots-unraveling-the-magic/urRefZ0KnU4.txt
- Transcript chars: 24949
- Keywords: snapshot, volume, snapshots, feature, object, content, driver, restore, volumes, everything, storage, create, database, backup, controller, consistent, application, created

### Resumo baseado na transcript

I'm a posgress user since a lot of time and I I'm a contributor to the Kubernetes CSI project and a maintainer of the cloud native PG project. We will discuss why we need warning group snapshots, explain how it works and how to use it. Volume snapshot API was introduced back in Kubernetes 1.12 release and moved to G in Kubernetes 1.20 release. It provides a basic building block to protect your applications running in Kubernetes. Suppose you have an application running that uses multiple volumes to store its data logs and so on. Now after restore you may run into problems because the snapshots were taken at different times and you get inconsistent data.

### Excerpt da transcript

Hello everyone. Thank you for coming to our session on waring group snapshots. My name is Shining. I work at VML by Bortcon. I'm also co-chair of Kubernetes six storage. And my name is Leonardo. I'm a principal software engineer working in EDB. I'm a posgress user since a lot of time and I I'm a contributor to the Kubernetes CSI project and a maintainer of the cloud native PG project. Here's today's agenda. We will discuss why we need warning group snapshots, explain how it works and how to use it. At the end, we will do a demo. When I was preparing for this presentation, I asked Chad GBT to show me why disaster recovery is important. Here's what I got. It looks chaotic and dangerous all around, but in the middle of this picture, it looks calm and safe. This is definitely better than what I can draw here. We have a data center being protected from disasters such as fire, flood, cyber attacks. A shield that safeguards your critical data. A contrast between chaos and security. Disaster can happen at any time.

How do we protect our precious data from a potential loss? Here I listed what could cause a disaster. Actually human error is one of the leading factors as shown in this picture. If this data center is burned down, your data stored there will be lost for sure. However, if you have your data backed up in a different location, you can always restore your data back. So data protection and disaster recovery are very important for your mission critical applications. Volume snapshot API was introduced back in Kubernetes 1.12 release and moved to G in Kubernetes 1.20 release. It allows you to take a crash consistent snapshot of a persistent volume and use that to restore your data back at a later time if a disaster strikes. It provides a basic building block to protect your applications running in Kubernetes. We already have a volume snapshot API for inter video volumes. So why do we need volume group snapshots? Now let's take a look at an example. Suppose you have an application running that uses multiple volumes to store its data logs and so on.

You want to protect your application. To ensure application consistency, you need to quiet your application before taking a snapshot and unquest afterwards. But quas takes a long time and it is very expensive. So you may not want to do it frequently. But you still want to be able to back up your data more frequently. Without application quas, you take a snapshot of the first volume at time one. Then you take a snap
