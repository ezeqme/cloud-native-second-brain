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
themes: ["AI ML", "Community Governance"]
speakers: ["David Ko", "Joshua Moody", "SUSE"]
sched_url: https://kccncna2022.sched.com/event/182Ny/longhorn-intro-deep-dive-and-q+a-david-ko-joshua-moody-suse
youtube_search_url: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+And+Q%2BA+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Longhorn: Intro, Deep Dive And Q+A - David Ko & Joshua Moody, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: David Ko, Joshua Moody, SUSE
- Schedule: https://kccncna2022.sched.com/event/182Ny/longhorn-intro-deep-dive-and-q+a-david-ko-joshua-moody-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+And+Q%2BA+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Longhorn: Intro, Deep Dive And Q+A.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ny/longhorn-intro-deep-dive-and-q+a-david-ko-joshua-moody-suse
- YouTube search: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+And+Q%2BA+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NPRij3LsYUM
- YouTube title: Longhorn: Intro, Deep Dive and Q+A - Phan Le, SUSE
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/longhorn-intro-deep-dive-and-q-a/NPRij3LsYUM.txt
- Transcript chars: 24944
- Keywords: volume, engine, replica, storage, support, feature, cluster, multiple, create, snapshot, longan, backup, number, performance, process, question, running, forward

### Resumo baseado na transcript

all right get let get start hi everyone welcome to the longan introduction and deep dive my name is fley I'm the senior software engineer Su I'm also one of the cor maintainer of Lon I have been look working on Lon for almost 5 years now uh so on the screen you can find the lon website uh first we want to have a quick update about Community adoption so up on so far Lan have 141,000 note running globally and which represent 44% increase year over year which

### Excerpt da transcript

all right get let get start hi everyone welcome to the longan introduction and deep dive my name is fley I'm the senior software engineer Su I'm also one of the cor maintainer of Lon I have been look working on Lon for almost 5 years now uh so on the screen you can find the lon website uh first we want to have a quick update about Community adoption so up on so far Lan have 141,000 note running globally and which represent 44% increase year over year which is a very good grow rate and we have 3,700 uh user across multile slack channels we have 6.1k GitHub stars and you can find more magic more Magics are available at magic. long home.io and by the way the data collected over here are all Anonymous data and it is ZD uh zdp compliance and we also publ the source code uh uh at Lor SL upgrade responder so next slide I want to quickly uh intro introduce about uh Lon for the use case Lon is a reliable scalable storage solution for a kubernetes stateful golo so basically if you have uh stateful uh golo like if you have a port and if the port need a p kubernetes PV or PVC then you can use Lon to Dynam dynamically provision and manage those PV and PVC Lon is a hyper converge solution what it means is it it going to run on the same cluster as a golo and Lon is very reliable it is consistent it has multiple layers of protection against data loss including building uh building snapshot and external backups uh it is one of the I think one of the most noticeable feature of longan is very easy to use it's simple it is an oneclick installation you user can install longan using coup control ham or uh get op solution like Fleet or flux CD it is very easy to maintain and easy to understand and easy to recover from the worst case scenario for example if the cluster burn down you can recover the data from external backup or if you have data from uh from the disc you can you can also recover from it uh and lan can do live upgrade like like upgrade without interrupting the good load so basically when you upgrade Lon you don't have to scale down the good Lo uh Lon will uh be able to uh live upgrade underneath it uh so some biggest feature of Lon uh we for the kubernetes persistent uh volume support we support block PVC mode and we also support file system PVC mode for the assess mode we support read right once and re right many re read write ones mean uh one note can access the longan PVC at the time and rewrite many mean multiple notes can access Along on other other time uh we
