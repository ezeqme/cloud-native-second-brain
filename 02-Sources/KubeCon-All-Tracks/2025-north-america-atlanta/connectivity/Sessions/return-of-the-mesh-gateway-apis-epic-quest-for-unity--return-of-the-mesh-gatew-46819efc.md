---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Henrik Rexed", "Dynatrace"]
sched_url: https://kccncna2025.sched.com/event/27FYA/return-of-the-mesh-gateway-apis-epic-quest-for-unity-henrik-rexed-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Return+of+the+Mesh%3A+Gateway+API%27s+Epic+Quest+for+Unity+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Return of the Mesh: Gateway API's Epic Quest for Unity - Henrik Rexed, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Henrik Rexed, Dynatrace
- Schedule: https://kccncna2025.sched.com/event/27FYA/return-of-the-mesh-gateway-apis-epic-quest-for-unity-henrik-rexed-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Return+of+the+Mesh%3A+Gateway+API%27s+Epic+Quest+for+Unity+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Return of the Mesh: Gateway API's Epic Quest for Unity.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FYA/return-of-the-mesh-gateway-apis-epic-quest-for-unity-henrik-rexed-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Return+of+the+Mesh%3A+Gateway+API%27s+Epic+Quest+for+Unity+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tgs6Wq5UlBs
- YouTube title: Return of the Mesh: Gateway API's Epic Quest for Unity - Henrik Rexed, Dynatrace
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/return-of-the-mesh-gateway-apis-epic-quest-for-unity/tgs6Wq5UlBs.txt
- Transcript chars: 28466
- Keywords: mesh, ambient, getaway, support, gateway, traffic, control, linkerd, policies, envoy, metrics, course, ingress, feature, couple, routing, define, policy

### Resumo baseado na transcript

So, welcome everyone to the return of the mesh, the getaways API epic quest for Unity. I am a cloud le advocate working at DRA a bit more than four years now. So we have the one hands the gateway which is going to be owned by the platform with all the security aspects and then you have the routing who could be owned by the teams itself. And then recently the gateway API introduced a gateway inference support which is very exciting for every machine learning workload that you may have. The request mirroring so for layer 7s uh request timeout and if you want to do backend timeout, they have a security called uh backend traffic policy which is exactly what we need. So we look at every service mesh compare their design experience uh what are the component we require if you want to run those meshes in our cluster the observity because of again observer is a feature of the service mesh how can we enable

### Excerpt da transcript

All right. So, welcome everyone to the return of the mesh, the getaways API epic quest for Unity. So, first of all, how are you today? >> Good. All right. So, do you like Star Wars? >> Yeah. So, I'm going to try to uh bring that theme. How much of you are using service meshes here? Few hands. Who doesn't know anything about service mesh? Okay. So, I'll try to answer a few questions. And who is using the ghetto API? Few hands. Who knows anything who doesn't know what is Gateway API? Couple of hands. All right. So let's start. My name is Henrik Cruxed. I am a cloud le advocate working at DRA a bit more than four years now. And I'm also a CNCF ambassador. Um and I'm very excited to be uh involved interacting with this amazing community. The cloud native community I think is just just amazing. But pure to that I've sp I spent my career as a performance engineer. So testing, braking, tuning, optimizing systems. Um, and you'll see that this presentation is pretty much with my performance engineering hat. Um, so that's why I when I have time, oh interesting, uh, when I have time, I try to produce content on a YouTube channel called Perf Bites, which is should be displayed somewhere.

Okay. Ah, much better. All right. So, I lost couple of minutes. Great. So, I try to produce content on a YouTube channel called Proof Bites. If you up into the performance world, check it out. It's out there with Cherry Mythology. And otherwise, uh, since four years, I have a YouTube channel called is it observable? Covering topics about security, observability of course, and Kubernetes. All right. So, let's start. a long time ago far far away in the galaxy we had couple of machines in the CNCF landscape fighting each other. So Kuma is ambient and all those they were all fighting it together but a whole new hope arise in the galaxy and it was the ghetto API and you look at it and say oh it's so promising let's try to figure out if it's going to actually resolve our pain when we are in a journey of using service meshes. So for this I had done some tests and I can guarantee I was very very nice with each of those solutions. Um and the intention of this solution is not to blame any other project in the opposite.

I love each of those projects. It's more about giving you some feedback and then give you maybe some tips on which solution make would be the best for you guys. So let me introduce the clang. So we have first Kuma Kuma from Kong uh one of the service mesh from the CNCF landscap
