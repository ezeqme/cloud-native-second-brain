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
themes: ["AI ML", "Community Governance"]
speakers: ["Shuo Wu", "SUSE"]
sched_url: https://kccncna2025.sched.com/event/27Nly/longhorn-intro-deep-dive-and-qa-shuo-wu-suse
youtube_search_url: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Longhorn: Intro, Deep Dive and Q&A - Shuo Wu, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Shuo Wu, SUSE
- Schedule: https://kccncna2025.sched.com/event/27Nly/longhorn-intro-deep-dive-and-qa-shuo-wu-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Longhorn: Intro, Deep Dive and Q&A.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nly/longhorn-intro-deep-dive-and-qa-shuo-wu-suse
- YouTube search: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NhllqYL0eBg
- YouTube title: Longhorn: Intro, Deep Dive and Q&A - Shuo Wu, SUSE
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/longhorn-intro-deep-dive-and-q-a/NhllqYL0eBg.txt
- Transcript chars: 26580
- Keywords: longhorn, volume, snapshot, backup, storage, cluster, corresponding, pretty, feature, engine, create, release, actually, latency, design, architecture, replica, blocks

### Resumo baseado na transcript

So today I'm going to do uh introduce the project status and then deep dive into some tech detail for uh for you guys. So basically uh Longhorn is a cloud native distributed uh block storage for Kubernetes and it's always an open resource project and it's already owned by CNCF for let's say over six years and uh Longhorn yeah is a general storage solution. So first there are three uh main uh design principle uh in longhorn system. First reliability that's the most important thing uh for the storage solution. So since longhorn is a uh block storage solution so we we we will follow the uh crash consistency uh with a bunch of uh data protection manager. And the last the maintainability since Longhorn architecture is uh relatively straightforward and simple is easy to understand and to maintain for for cluster admin or for for for the cluster manager and it's al uh and and is also easy to recover uh the data even in the worst case scenario happens.

### Excerpt da transcript

Welcome to the Longhorn session. I'm Shaw, a maintainer from uh project Longhorn. So I'm also a uh software engineer in SUSA. So today I'm going to do uh introduce the project status and then deep dive into some tech detail for uh for you guys. So let's get start. Here is uh today's agenda. Uh okay, first let's have a basic uh overview for this project. So basically uh Longhorn is a cloud native distributed uh block storage for Kubernetes and it's always an open resource project and it's already owned by CNCF for let's say over six years and uh Longhorn yeah is a general storage solution. It can be deployed in multiple kind of environments uh including AKS or lowspec uh cluster on premises cluster or public cloud vendors and yeah it can adopt you multiple uh use case uh as well in AI uh telecommunication data visualization and obserability related issue. Yeah. And it also has pretty good uh capability with multiple kind of operating systems not only uh with traditional OS but also for immutable OS.

Okay, let's so right now uh or uh in the past years Longhorn uh always keep a pretty good adoption in the community. We have solid growth in both g stars and active uh node usage all over the world and uh in the recent year our release cy become more and more stable. Right now we have uh four months uh feature release cadence and two months uh patch release cadence and internally we also have a uh twoe uh sprint release uh since we are using agile developing and our latest uh feature release is 1.10 10 uh in this uh September and since uh the release schedule is pretty quick. So we we also uh have a bunch of uh comprehensive uh quality assurance mechanism including regular end to end test and uh negative test case those are all automated and besides for every release we will we will scan the CVE issues and update the uh BCI image to guarantee uh all critical CV issues are uh are resolved in the latest version and in the daily development uh our QA will do lots of uh manual verification for each uh issues tickets or improvement.

Thus, uh uh really solidate our uh release quality and project quality. Okay, then let's uh talk more about uh the uh tech detail uh for the for this project. So first there are three uh main uh design principle uh in longhorn system. First reliability that's the most important thing uh for the storage solution. So since longhorn is a uh block storage solution so we we we will follow the uh crash consistency uh with a bunch of uh data p
