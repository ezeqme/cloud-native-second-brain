---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Zach Loafman", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7lD/better-pod-availability-a-survey-of-the-many-ways-to-manage-workload-disruptions-zach-loafman-google
youtube_search_url: https://www.youtube.com/results?search_query=Better+Pod+Availability%3A+A+Survey+of+the+Many+Ways+to+Manage+Workload+Disruptions+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Better Pod Availability: A Survey of the Many Ways to Manage Workload Disruptions - Zach Loafman, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Zach Loafman, Google
- Schedule: https://kccncna2024.sched.com/event/1i7lD/better-pod-availability-a-survey-of-the-many-ways-to-manage-workload-disruptions-zach-loafman-google
- Busca YouTube: https://www.youtube.com/results?search_query=Better+Pod+Availability%3A+A+Survey+of+the+Many+Ways+to+Manage+Workload+Disruptions+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Better Pod Availability: A Survey of the Many Ways to Manage Workload Disruptions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lD/better-pod-availability-a-survey-of-the-many-ways-to-manage-workload-disruptions-zach-loafman-google
- YouTube search: https://www.youtube.com/results?search_query=Better+Pod+Availability%3A+A+Survey+of+the+Many+Ways+to+Manage+Workload+Disruptions+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XN1vJmrdhpA
- YouTube title: Better Pod Availability: A Survey of the Many Ways to Manage Workload Disruptions - Zach Loafman
- Match score: 1.005
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/better-pod-availability-a-survey-of-the-many-ways-to-manage-workload-d/XN1vJmrdhpA.txt
- Transcript chars: 24287
- Keywords: actually, disruption, cluster, period, workloads, servers, termination, automation, little, seconds, yielding, running, upgrade, particular, autoscaler, server, anything, workload

### Resumo baseado na transcript

good afternoon uh my name is Zach loffman and realized I was going to be talking to such a packed house I'm glad to see you all here this afternoon hopefully you're not in a too much of a food coma uh I am a staff fesser at Google I've been working on gke for about a decade now um and here I'm going to talk to you about better pod availability this is a pretty nebulous topic um but we're going to go over several ways to manage workload

### Excerpt da transcript

good afternoon uh my name is Zach loffman and realized I was going to be talking to such a packed house I'm glad to see you all here this afternoon hopefully you're not in a too much of a food coma uh I am a staff fesser at Google I've been working on gke for about a decade now um and here I'm going to talk to you about better pod availability this is a pretty nebulous topic um but we're going to go over several ways to manage workload disruptions many of which are familiar to you some of which may be new so what is POD disruption anything that interrupts a pod before the application exits can be considered disruption now that's a super nebulous uh that's a super nebulous definition there's so many things that are actually in this envelope and in fact the kubernetes documentation even has uh a taxonomy of these splitting it up into involuntary and voluntary disrupture disruption um by the way I have uploaded these slides to sked so if uh you see me putting links in here uh you can follow those or you can just take pictures uh most of these things are googleable pretty quickly um so let's go through these in just broad terms I Loosely categorize these on the the left uh which is where the kubernetes documentation calls them involuntary disruptions into things like Halt and Catch Fire events uh they are Hardware failure uh OS failure Network failure anything that just stops your pod suddenly um another thing in that involuntary category is out is also out of resource evictions and we'll talk about that in just a minute in the voluntary category uh on the other end of the spectrum are various app owner disruptions so you have a roll out you delete the deployment you restart the deployment Etc and in the middle there's an interesting category that's voluntary but it really depends on your provider as to how voluntary it is uh that includes cluster administrative actions so this is anything that incurs a node drain so evicted by upgrade scale down node repair and we're actually going to spend a chunk of time talking about this category so that's categorizing it into voluntary and involuntary and a lot of that has to do with um how the Pod uh how all of the communties Machinery reacts uh to that particular disruptor but we can also talk about is this good disruption or bad disruption now this is of course a qualitative definition but anything that's uh the Pod is interrupted when you want it to be interrupted is good disruption most of you are wining workloads t
