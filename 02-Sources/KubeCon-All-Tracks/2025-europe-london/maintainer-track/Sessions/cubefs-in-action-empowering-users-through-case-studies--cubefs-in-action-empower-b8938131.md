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
themes: ["AI ML", "Community Governance"]
speakers: ["Leon Chang", "OPPO"]
sched_url: https://kccnceu2025.sched.com/event/1td0z/cubefs-in-action-empowering-users-through-case-studies-leon-chang-oppo
youtube_search_url: https://www.youtube.com/results?search_query=CubeFS+in+Action%3A+Empowering+Users+Through+Case+Studies+CNCF+KubeCon+2025
slides: []
status: parsed
---

# CubeFS in Action: Empowering Users Through Case Studies - Leon Chang, OPPO

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Leon Chang, OPPO
- Schedule: https://kccnceu2025.sched.com/event/1td0z/cubefs-in-action-empowering-users-through-case-studies-leon-chang-oppo
- Busca YouTube: https://www.youtube.com/results?search_query=CubeFS+in+Action%3A+Empowering+Users+Through+Case+Studies+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre CubeFS in Action: Empowering Users Through Case Studies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td0z/cubefs-in-action-empowering-users-through-case-studies-leon-chang-oppo
- YouTube search: https://www.youtube.com/results?search_query=CubeFS+in+Action%3A+Empowering+Users+Through+Case+Studies+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_rDE1PD5Z5I
- YouTube title: CubeFS in Action: Empowering Users Through Case Studies - Leon Chang, OPPO
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/cubefs-in-action-empowering-users-through-case-studies/_rDE1PD5Z5I.txt
- Transcript chars: 19840
- Keywords: storage, several, performance, cost, architecture, business, subsystem, process, training, second, capability, distribution, computing, transfer, client, support, consistency, distributed

### Resumo baseado na transcript

uh uh I'm the maintainer of open source project Kubas and uh I also in charge of the file system of OPPO uh well let's get started now today my topic is Kuba in action empowering users through case studies my speech will include uh three parts first I will introduce the architecture of cubef. Uh finally uh let's review the future prospect of cubef is a next generation cloud native uh storage system. On the top right is the object access zone uh different from the traditional object storage architecture. The system in the bottom right storage subsystem uh is a data subsystem. One is a multi-replica uh engine and another is the usual coding subsystem which is independent storage subsystem using the coding algorithm. Secondly uh has two engine storage engines including multi-replica and coding uh storage engine.

### Excerpt da transcript

Uh hello everyone. Uh I'm Li Chong from OPPO. Uh and I appreciate the opportunity to attend this conference. Uh this is my first English speech. Uh so for uh excuse me if I I have any grammar issues or bad accent. uh uh I'm the maintainer of open source project Kubas and uh I also in charge of the file system of OPPO uh well let's get started now today my topic is Kuba in action empowering users through case studies my speech will include uh three parts first I will introduce the architecture of cubef. Uh second I will introduce several end user cases. Uh finally uh let's review the future prospect of cubef is a next generation cloud native uh storage system. uh uh kubas joined the saf in uh 2019 uh after about uh f five years of development. Uh we released around a dozen versions in the past few years. Finally at the end of the last year we graduated from CNCF. The picture is from the CCF website. Uh in terms of the uh architecture uh cubs is a independent and uh self-governing storage system. Uh as can be seen from the diagram it includes several parts.

Uh the part uh in the top left is the client subsystem. The client is actually a very complex component. uh it provides capabilities for different interfaces such as S3, ADFS and posics. Meanwhile, the client side interacts with the back end frequently uh and even gets the whole process of our system. The middle part on the left is the catch subsystem. Uh the catch system is a new designed system uh for adapting to different uh acceleration scenarios. uh currently to support uh AI uh the catch system is becoming more and more important. This is a main point in my topic. The lower left corner is a metadata uh metadata subsystem. It's carefully designed. It has strong consistency and be can be scaled easily. uh many system level functions like the trash audit and autonomic posics interfaces uh need support from the meditative subsystem. On the top right is the object access zone uh different from the traditional object storage architecture. CubeFS achieves a capability based on the file system engine and this system can be considered as as a city proxy system.

The system in the bottom right storage subsystem uh is a data subsystem. The storage subsystem uh uh contains two engines. One is a multi-replica uh engine and another is the usual coding subsystem which is independent storage subsystem using the coding algorithm. It it has its own metad data management uh including the inspection and management sys
