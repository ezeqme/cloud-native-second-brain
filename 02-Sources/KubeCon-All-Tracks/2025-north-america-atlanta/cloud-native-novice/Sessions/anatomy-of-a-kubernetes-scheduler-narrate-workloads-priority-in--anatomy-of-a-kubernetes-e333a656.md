---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Novice"
themes: ["Kubernetes Core"]
speakers: ["Hoon Jo", "Megazone"]
sched_url: https://kccncna2025.sched.com/event/27FUp/anatomy-of-a-kubernetes-scheduler-narrate-workloads-priority-in-sequence-hoon-jo-megazone
youtube_search_url: https://www.youtube.com/results?search_query=Anatomy+of+a+Kubernetes+Scheduler%3A+Narrate+Workloads+Priority+in+Sequence+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Anatomy of a Kubernetes Scheduler: Narrate Workloads Priority in Sequence - Hoon Jo, Megazone

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Hoon Jo, Megazone
- Schedule: https://kccncna2025.sched.com/event/27FUp/anatomy-of-a-kubernetes-scheduler-narrate-workloads-priority-in-sequence-hoon-jo-megazone
- Busca YouTube: https://www.youtube.com/results?search_query=Anatomy+of+a+Kubernetes+Scheduler%3A+Narrate+Workloads+Priority+in+Sequence+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Anatomy of a Kubernetes Scheduler: Narrate Workloads Priority in Sequence.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FUp/anatomy-of-a-kubernetes-scheduler-narrate-workloads-priority-in-sequence-hoon-jo-megazone
- YouTube search: https://www.youtube.com/results?search_query=Anatomy+of+a+Kubernetes+Scheduler%3A+Narrate+Workloads+Priority+in+Sequence+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9BjX9SFOqRE
- YouTube title: Anatomy of a Kubernetes Scheduler: Narrate Workloads Priority in Sequence - Hoon Jo, Megazone
- Match score: 0.974
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/anatomy-of-a-kubernetes-scheduler-narrate-workloads-priority-in-sequen/9BjX9SFOqRE.txt
- Transcript chars: 19547
- Keywords: reason, scoring, choose, actually, though, junior, little, working, purpose, probably, scheduleuler, powerful, waiting, already, prepared, workload, ignore, explain

### Resumo baseado na transcript

Uh thank you for joining the session for this um uh kind of Navi session actually that so you may know that this Navi session is one of the some beginners level but uh even though this I'm prepared a really good uh infographic after maybe the three minute or five minutes so please keep it in state this in five minute after that probably you can choose that this uh you going to go out or not and yeah was really thanks for joining this my sessions Actually you So the per is really uh working well and then really designed well for smartly working because we have a limited resource. I will focus on Kubernetes as I said because it's the the title is a narration for Kubernetes. the show the demo that's the reason why I'm preparing in here uh here's the node like this there is a version 1.34 because the we are not December we are currently this uh yeah November November so December will be the 1.35 so is I can show that this demo here is the stage three demo yeah there's really lots of thing but yes it's a simple to work and then I going to be the script for the taint things uh this one is for the scoring as

### Excerpt da transcript

Uh thank you for joining the session for this um uh kind of Navi session actually that so you may know that this Navi session is one of the some beginners level but uh even though this I'm prepared a really good uh infographic after maybe the three minute or five minutes so please keep it in state this in five minute after that probably you can choose that this uh you going to go out or not and yeah was really thanks for joining this my sessions Actually you know what this AI is really popular all of them is talk about AI but in my personal opinion that there some we or your junior your team's junior or your team member need to know about this uh the essential rev because essential re is really important to to further go AI workload AI is just for one of the tool I think it's not yeah technology is included any of this kinds of the productivity tool so I think it essentially is really important okay I'm going to start that. So first you may notice this this kinds of is really old generations pictures probably this the I'm not sure that the one months ago two months ago is a change that but it is a little bit looks like it's modern type but anyhow the purpose is same there are communities cluster and control plane in node and this kinds of some diagram I'm going to show up to that a little bit change that because there are component communication each other like this they are communication each other in the kubernetes cluster But I focus on and also you may notice that my some uh my topic is the Kubernetes itself.

So I'm just want to be the focus on Kubernetes. Yeah, that's what I want to know say that or uh actually that so I'm just throw by myself not for AI. I do not use it any AI in here even uh one of the some some this pictures all of them some I'm searching that and print that I'm just throw that. So three thing is very important thing uh in this diagram. One thing is that stage number one actually the stage number one and two is a pure rebel but even though the stage one there is a node name is their working is a little different maybe you are most of them is very professional but in your junior or even this my team's junior doesn't know about the what the node name is exactly work so I'm just put it uh isolated the supporter because the node name you can see that is it bypass a scheduleuler the name do not use the scheduleuler to assign this node there are really powerful so I'm going to read it this there are some n name others thing yeah I want
