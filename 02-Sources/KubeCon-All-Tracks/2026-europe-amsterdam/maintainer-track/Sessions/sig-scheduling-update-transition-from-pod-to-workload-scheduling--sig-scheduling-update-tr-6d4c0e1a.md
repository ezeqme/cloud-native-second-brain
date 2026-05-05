---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Kensei Nakada", "Independent", "Maciej Skoczeń", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF5V/sig-scheduling-update-transition-from-pod-to-workload-scheduling-kensei-nakada-independent-maciej-skoczen-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Scheduling+Update%3A+Transition+From+Pod+To+Workload+Scheduling+CNCF+KubeCon+2026
slides: []
status: parsed
---

# SIG Scheduling Update: Transition From Pod To Workload Scheduling - Kensei Nakada, Independent & Maciej Skoczeń, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kensei Nakada, Independent, Maciej Skoczeń, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF5V/sig-scheduling-update-transition-from-pod-to-workload-scheduling-kensei-nakada-independent-maciej-skoczen-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Scheduling+Update%3A+Transition+From+Pod+To+Workload+Scheduling+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre SIG Scheduling Update: Transition From Pod To Workload Scheduling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5V/sig-scheduling-update-transition-from-pod-to-workload-scheduling-kensei-nakada-independent-maciej-skoczen-google
- YouTube search: https://www.youtube.com/results?search_query=SIG+Scheduling+Update%3A+Transition+From+Pod+To+Workload+Scheduling+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-5TIJrVvmsQ
- YouTube title: SIG Scheduling Update: Transition From Pod To Workload Scheduling - Kensei Nakada & Maciej Skoczeń
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sig-scheduling-update-transition-from-pod-to-workload-scheduling/-5TIJrVvmsQ.txt
- Transcript chars: 21530
- Keywords: scheduling, algorithm, workload, basically, preeemption, scheduleuler, extension, future, actually, placement, schedule, cluster, binding, topology, resource, points, filter, groups

### Resumo baseado na transcript

Uh, transition from part to rock wall scheduling like fancy fancier title than I than usual I guess. So we are going through all the updates that we made in the last release. Uh so this air for started around last week uh which is 1.35 actually we had uh this like kind of design uh from before but uh we actually like implemented some yeah those uh gang and API at the at 1.35 and then we So basically uh until we see all members to be scheduable we basically stop all parts here and then once we see okay we have three parts scheduable then we release them like admits them to uh binding cycle and binding cycle we were going to make API calls but there's some challenges that new. So as Kenz showed you in 135 we had only the workload API which was a grouping object for the whole like workload entity and it had the problems for example with replicated like jobs or anything because each of those was like separate scheduling object so the port instance but it was consisted in one API object what was the workload API and we had for example problems how to introduce the workload status and other things.

### Excerpt da transcript

All right, let's start it. Uh, hi everyone. This is six scheduling maintainer session. Uh, transition from part to rock wall scheduling like fancy fancier title than I than usual I guess. So we are going through all the updates that we made in the last release. I mean actually this release as well. And then like we see how the future looks like. So I'm can say Nakada >> and I'm Mati Scott. >> So we are presenting today. All right. So and yeah we have a lot things to present. So most likely we don't have enough time for Q&A but we're going to you know be around this room after the session. So you can like please feel free to come to us and ask question after that. All right. So s scheduling uh we are maintaining components that makes uh power placement decision uh basically scheduling. So the schedule recommended schedule is the biggest part of us. Uh it's the viewing component making a power placement decision based on some you know n condition or whatever and then we have sub project we have actually a lot more but uh like three like I would say popular sub projects right now as desk schedule rock.

uh Q is uh fancy job queuing system like other mission mechanism with C and sharing and other feature as well and then uh the scheduleuler it's the component to reschedu the parts quark it's the fake cluster with some quark is actually kubernetes without cub right yeah I think so uh it's like you can create whatever amount of nodes was uh on your laptop and simulate what happens in the in that scale. So yeah and the scheduleuler is the component. Yeah we explained it and we implement like for example resource request port affinity node affinity some other scheduling preferences and then those features are implemented as plugins internally. So basically like for resource request we have resource feed program it's like you know each program has a dedicated responsibility on it and we also have another concept called extension points. So this is where program is one on so basically one on any extension points that they want. So first line is filter. Uh I mean these two are like major extential points.

Uh filter is like if for example if nodes don't have enough resources you shouldn't run part on it right. So like basically filter is the extension point to exclude such nodes that shouldn't run this part and then like after future we get the list of nodes that that can run run this part. So after that we get this score extension point that uh like each plugin says
