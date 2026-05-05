---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Storage"
themes: ["Networking", "Storage Data"]
speakers: ["Sébastien Han", "Rohan Gupta", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV1W/storage-and-networking-rook-on-multus-sebastien-han-rohan-gupta-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Storage+and+Networking%3A+Rook+on+Multus+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Storage and Networking: Rook on Multus - Sébastien Han & Rohan Gupta, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Storage]]
- Temas: [[Networking]], [[Storage Data]]
- País/cidade: United States / Los Angeles
- Speakers: Sébastien Han, Rohan Gupta, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV1W/storage-and-networking-rook-on-multus-sebastien-han-rohan-gupta-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Storage+and+Networking%3A+Rook+on+Multus+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Storage and Networking: Rook on Multus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1W/storage-and-networking-rook-on-multus-sebastien-han-rohan-gupta-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Storage+and+Networking%3A+Rook+on+Multus+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zIS5qaG_HRw
- YouTube title: Storage and Networking: Rook on Multus - Sébastien Han & Rohan Gupta, Red Hat
- Match score: 0.765
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/storage-and-networking-rook-on-multus/zIS5qaG_HRw.txt
- Transcript chars: 17889
- Keywords: network, storage, cluster, public, default, interfaces, attachment, interface, performance, definition, networking, running, essentially, multis, without, throughout, networks, random

### Resumo baseado na transcript

hello everyone and welcome to kubecon first cubecom to be in person as well as virtual i'm sebastian i'm joined with rohan we both work for red hat i'm acting as a rook maintainer and i'm part of the storage team so i am also a part of a storage team i may work making on roxa okay and today we will be discussing storage and networking with rooksef running on maltese so before we dive let's take a step back and discuss some of the storage challenges that come this additional replication network for dedicated for replication is really helping and we kind of see a 22 gain at the end of the spectrum as well so it's really something uh like i mean it's a really good performance boost in terms of random

### Excerpt da transcript

hello everyone and welcome to kubecon first cubecom to be in person as well as virtual i'm sebastian i'm joined with rohan we both work for red hat i'm acting as a rook maintainer and i'm part of the storage team so i am also a part of a storage team i may work making on roxa okay and today we will be discussing storage and networking with rooksef running on maltese so before we dive let's take a step back and discuss some of the storage challenges that come with kubernetes so as we all know kubernetes is a platform that manages distributed apps and also distributed controllers most of the time these apps are stateless but when they do need storage it's not so easy typically we have to rely on external storage so storage that leaves outside of kubernetes and with that comes some caveats like the storage is not fully portable if the environment changes for instance if you deploy on the cloud if you deploy on bermuda then you would have like different storage or nd the overall experience would be a bit broken obviously there is the deployment burden but this could just be the responsibility of the storage team and how about day two operations if you want to increase the capacity of the cluster like who is responsible who is actually managing that storage for you if you have to go and ask for like a different team to increase the capacity and how is the storage going to be allocated when these are all the the questions you and just to add to that um we also we we might be relying if you're not like relying on external storage when you run on griddle you might be relying on providers in many services like ebs but this means also that you have been the login too and also cloud providers comes with their own set of issues you might be limited to the number of pcbs you can request for each nodes and things like this so there are also limitations when you use the bear cloud provider managed services too and rook is essentially the response to that the response to how can i get this homogeneous experience across having storage that lives inside kubernetes and it's being provided by it so rook is open source rook also commonly known as rook ceph and is a rook is a storage operator for kubernetes so if you're familiar with the operator's pattern then you would you should know that typically operators are logical entities are responsible for bootstrapping software and managing them and automating their deployments their configuration and the upgrade so essentially the
