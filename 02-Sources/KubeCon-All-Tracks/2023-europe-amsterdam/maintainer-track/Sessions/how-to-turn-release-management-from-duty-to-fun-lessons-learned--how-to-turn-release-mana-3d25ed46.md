---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Yuvaraj Balaji Rao Kakaraparthi", "VMware", "Joe Kratzat", "Oracle"]
sched_url: https://kccnceu2023.sched.com/event/1HyTd/how-to-turn-release-management-from-duty-to-fun-lessons-learned-building-the-cluster-api-release-team-yuvaraj-balaji-rao-kakaraparthi-vmware-joe-kratzat-oracle
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Turn+Release+Management+from+Duty+to+Fun%3A+Lessons+Learned+Building+the+Cluster+API+Release+Team+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How to Turn Release Management from Duty to Fun: Lessons Learned Building the Cluster API Release Team - Yuvaraj Balaji Rao Kakaraparthi, VMware & Joe Kratzat, Oracle

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yuvaraj Balaji Rao Kakaraparthi, VMware, Joe Kratzat, Oracle
- Schedule: https://kccnceu2023.sched.com/event/1HyTd/how-to-turn-release-management-from-duty-to-fun-lessons-learned-building-the-cluster-api-release-team-yuvaraj-balaji-rao-kakaraparthi-vmware-joe-kratzat-oracle
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Turn+Release+Management+from+Duty+to+Fun%3A+Lessons+Learned+Building+the+Cluster+API+Release+Team+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How to Turn Release Management from Duty to Fun: Lessons Learned Building the Cluster API Release Team.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyTd/how-to-turn-release-management-from-duty-to-fun-lessons-learned-building-the-cluster-api-release-team-yuvaraj-balaji-rao-kakaraparthi-vmware-joe-kratzat-oracle
- YouTube search: https://www.youtube.com/results?search_query=How+to+Turn+Release+Management+from+Duty+to+Fun%3A+Lessons+Learned+Building+the+Cluster+API+Release+Team+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sgP3tyGJ5tQ
- YouTube title: How to Turn Release Management from Duty to Fun: Lessons... - Yuvaraj Kakaraparthi & Joe Kratzat
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-to-turn-release-management-from-duty-to-fun-lessons-learned-buildi/sgP3tyGJ5tQ.txt
- Transcript chars: 21750
- Keywords: release, releases, shadows, cluster, trying, knowledge, communicate, responsible, problems, months, basically, looking, documentation, automation, process, maintainers, failing, predictable

### Resumo baseado na transcript

today we'll be talking about the cluster API release team history about how why we started it how we assembled it and some of the learnings that we had from running a release team I am yuvraj I work at VMware and I mainly work on cluster API and I served as the release lead for the 1.4 release cycle yep and I'm Joe kratzit I'm one of the release leads for 1.5 and I'm currently one of the maintainers of the cluster API for oci provider and I work

### Excerpt da transcript

today we'll be talking about the cluster API release team history about how why we started it how we assembled it and some of the learnings that we had from running a release team I am yuvraj I work at VMware and I mainly work on cluster API and I served as the release lead for the 1.4 release cycle yep and I'm Joe kratzit I'm one of the release leads for 1.5 and I'm currently one of the maintainers of the cluster API for oci provider and I work at Oracle so today we'll roughly go over the problems that we had and the goals that we set for ourselves to address these problems the release team and some of the learnings that we had from running a release team so last year at kubecon EU we announced class API V1 and that was a huge milestone for the project because it signified a maturity level for the project that means there will be more and more other projects in the community that now start depending on cluster API and examples are for example the cluster provided for oci the plus API provided for AWS Azure and so on and this means that the cluster API had to get on to a predictable release cycle so that all of the other projects and softwares that are depending on it can base their own cycles and release planning according to the release schedule that was announced and other problems that we were trying to address were at that point until a few weeks until a few months ago clusteria is basically doing releases ad hoc as soon as we think that a release is ready we just used to cut it no dates announced ahead of time in most cases and the other problems were some of the other problems were the releases were mostly done by just a couple of folks within the community and it was generally the maintenance and this was generally chore work and the knowledge about how to cut releases for the project was in their minds but not really documented so they were the only ones who were able to do it they knew the know-how of how to cut these things and how to properly get releases out of out of the project so we wanted to address these problems and we set up set some goals for ourselves to address these things so the first one as I mentioned is to move cluster API to a predictable and deterministic release cycle and communicate this release cycle ahead of time with all uh with the community with the broader community so that they can plan their own work and their own Cycles based on the timeline that we announce and next is to basically spread the knowledge of how these
