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
themes: ["AI ML", "Community Governance"]
speakers: ["Jorge Castro", "Kapil Thangavelu", "Stacklet Inc."]
sched_url: https://kccnceu2023.sched.com/event/1HyUe/state-of-the-mop-cloud-custodian-in-2023-jorge-castro-kapil-thangavelu-stacklet-inc
youtube_search_url: https://www.youtube.com/results?search_query=State+of+the+Mop%3A+Cloud+Custodian+in+2023+CNCF+KubeCon+2023
slides: []
status: parsed
---

# State of the Mop: Cloud Custodian in 2023 - Jorge Castro & Kapil Thangavelu, Stacklet Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jorge Castro, Kapil Thangavelu, Stacklet Inc.
- Schedule: https://kccnceu2023.sched.com/event/1HyUe/state-of-the-mop-cloud-custodian-in-2023-jorge-castro-kapil-thangavelu-stacklet-inc
- Busca YouTube: https://www.youtube.com/results?search_query=State+of+the+Mop%3A+Cloud+Custodian+in+2023+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre State of the Mop: Cloud Custodian in 2023.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUe/state-of-the-mop-cloud-custodian-in-2023-jorge-castro-kapil-thangavelu-stacklet-inc
- YouTube search: https://www.youtube.com/results?search_query=State+of+the+Mop%3A+Cloud+Custodian+in+2023+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Lx5f-0WOFrA
- YouTube title: State of the Mop: Cloud Custodian in 2023 - Jorge Castro & Kapil Thangavelu, Stacklet Inc.
- Match score: 0.75
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/state-of-the-mop-cloud-custodian-in-2023/Lx5f-0WOFrA.txt
- Transcript chars: 16111
- Keywords: providers, policies, policy, resources, looking, source, support, provider, directly, terraform, actually, currently, against, security, trying, across, additional, around

### Resumo baseado na transcript

um my co-presenter George Castro unfortunately could not be here today but I wanted to go through some of the things that have happened since uh we last presented on the state of the project and our roadmap in Detroit at kubecon um in October and also present some of our roadmap for 2023. do a little bit of a demo around some of our new capabilities around doing infrastructure as code governance directly against Source assets and then I'll walk you through the contribution process for those that might be interested in that so I had a curiosity

### Excerpt da transcript

um my co-presenter George Castro unfortunately could not be here today but I wanted to go through some of the things that have happened since uh we last presented on the state of the project and our roadmap in Detroit at kubecon um in October and also present some of our roadmap for 2023. do a little bit of a demo around some of our new capabilities around doing infrastructure as code governance directly against Source assets and then I'll walk you through the contribution process for those that might be interested in that so I had a curiosity quick show of hands uh who here doesn't has not used clock custodian okay well this is to provide a quick overview of it it is an open source rules engine for cloud management it's simple yaml policy dsls it allows you to find interesting resources of by doing arbitrary filtering on them so taking ec2 and set of ec2 instances in AWS find those that are on the available to the public internet that have iron rolls attached that allow them to create IM users that don't have encrypted disks and you can sort of chain these filters together in arbitrary ways and then you can take a set of actions on them uh and actions could be something like stop an instance or take a snapshot of it or change its role or security groups and you can combine those filters and actions sort of to create arbitrary policies so you might Target it towards um doing um security you might Target towards doing better operations clicking automatic backups you might Target it towards cost optimization under utilize things and so it's trying designed to be a sort of a Swiss army knife around your Cloud management and additionally it also binds into event-based execution so now you're able to as API calls are happening in your cloud provider actually introspect what's happening with those API calls and if the resulting resources are compliant to your policies so that said what's happened since last October we've had about 70 authors contribute about 280 different commits across different resources and providers we've added two new core maintainers Darren Dao from Intuit and Patrice Michelle from Capital One and we've added a few new providers providers in custodian are sort of like what you expressed your policies against we've added a terraform provider for being able to evaluate terraform source code inside of your pipeline and additional capabilities around that and I'll actually do a deep dive demo on that and then we've had the contribution of the
