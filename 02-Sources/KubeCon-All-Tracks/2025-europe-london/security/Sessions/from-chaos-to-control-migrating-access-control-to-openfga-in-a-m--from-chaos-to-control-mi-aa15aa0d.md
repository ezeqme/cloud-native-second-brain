---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security"]
speakers: ["Jo Guerreiro", "Grafana Labs", "Poovamraj Thanganadar Thiagarajan", "Okta"]
sched_url: https://kccnceu2025.sched.com/event/1txIJ/from-chaos-to-control-migrating-access-control-to-openfga-in-a-multi-tenant-world-jo-guerreiro-grafana-labs-poovamraj-thanganadar-thiagarajan-okta
youtube_search_url: https://www.youtube.com/results?search_query=From+Chaos+To+Control%3A+Migrating+Access+Control+To+OpenFGA+in+a+Multi-Tenant+World+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Chaos To Control: Migrating Access Control To OpenFGA in a Multi-Tenant World - Jo Guerreiro, Grafana Labs & Poovamraj Thanganadar Thiagarajan, Okta

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Jo Guerreiro, Grafana Labs, Poovamraj Thanganadar Thiagarajan, Okta
- Schedule: https://kccnceu2025.sched.com/event/1txIJ/from-chaos-to-control-migrating-access-control-to-openfga-in-a-multi-tenant-world-jo-guerreiro-grafana-labs-poovamraj-thanganadar-thiagarajan-okta
- Busca YouTube: https://www.youtube.com/results?search_query=From+Chaos+To+Control%3A+Migrating+Access+Control+To+OpenFGA+in+a+Multi-Tenant+World+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Chaos To Control: Migrating Access Control To OpenFGA in a Multi-Tenant World.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txIJ/from-chaos-to-control-migrating-access-control-to-openfga-in-a-multi-tenant-world-jo-guerreiro-grafana-labs-poovamraj-thanganadar-thiagarajan-okta
- YouTube search: https://www.youtube.com/results?search_query=From+Chaos+To+Control%3A+Migrating+Access+Control+To+OpenFGA+in+a+Multi-Tenant+World+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZOG1J1Niuh0
- YouTube title: From Chaos To Control: Migrating Access Control... Jo Guerreiro & Poovamraj Thanganadar Thiagarajan
- Match score: 0.77
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-chaos-to-control-migrating-access-control-to-openfga-in-a-multi-t/ZOG1J1Niuh0.txt
- Transcript chars: 24471
- Keywords: actually, authorization, access, control, folder, graphana, search, dashboards, tenant, viewer, permissions, having, resources, represent, resource, finally, started, basically

### Resumo baseado na transcript

Uh well, I hope everyone's like feeling comfortable like not too tired like on your last basically slot session of CubeCon. Uh well, thank you for choosing to be here like I know it's somewhat of a stretch after like these days and well thank you for choosing our talk when there's actually other like two simultaneous like authorization talks going like on others. This leads to silos, specialized patterns and both knowledge and security gaps. This caused tight coupling, redundancy and in solving the same problem, it caused inconsistency due to lack of standardization. In their paper they explain how their system solves all the problem we have as an industry need a authorization system that's generic for all applications. It should go without saying we provide first classapo support for Kubernetes.

### Excerpt da transcript

Let's get this started. Uh well, I hope everyone's like feeling comfortable like not too tired like on your last basically slot session of CubeCon. Uh well, thank you for choosing to be here like I know it's somewhat of a stretch after like these days and well thank you for choosing our talk when there's actually other like two simultaneous like authorization talks going like on others. So, by the way, this is your cue if you just realize you're in the wrong one. Like, just just saying. Uh, so my name is John. Uh, but actually everyone calls me Joe. So, call me Joe. Uh, I work at Graphana for the identity and access team. Uh, we actually provide like um like a application platform for other teams to build features on. So let's say like having like the authorization checks like uh having like resources that are like instrumented so let's say protected with arbback and actually our journey kind of starts like in 2024 at cubecon in Paris uh there we saw a presentation about open FGA uh we actually were really excited and we contacted the open FGA team afterwards uh like they were great like uh we were like really excited to get like an integration or like a partial migration going.

Uh but after this like initial excitement, we noticed that like something was missing. Uh we couldn't find a lot of like real world examples of moving multi-tenant systems like ours on cloud to open FGA. Uh and well there's a lot of examples like for new projects and even like for new multi-tenant projects. And if you are starting like a new project in that case save yourself the trouble and like start integrating like with like access control engine like from the start. Uh but on our side we have a lot of like legacy like let's say baggage like almost like 14 years of uh access control features and so we wanted to know like how are other people like handling this transition. So this is a bit what we want to share today uh and hopefully answer like questions like that you have like well would open FJ fit my use case like what hurdles might I expect like in this migration and I think to start like the best thing is to give it over to Puamraj hey all I'm purajangati rajin I'm the technical lead in the fa team we do everything from integrating open into CM platforms identity platforms and observability and uh yeah let's get into the presentation.

If you start a new project today would you build a login for it from scratch? There are so many great libraries frameworks and services ou
