---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Storage Data", "Community Governance"]
speakers: ["Tabitha Sable", "Datadog", "Tim Allclair", "Apple"]
sched_url: https://kccncna2021.sched.com/event/lV9A/podsecuritypolicy-replacement-past-present-and-future-tabitha-sable-datadog-tim-allclair-apple
youtube_search_url: https://www.youtube.com/results?search_query=PodSecurityPolicy+Replacement%3A+Past%2C+Present%2C+and+Future+CNCF+KubeCon+2021
slides: []
status: parsed
---

# PodSecurityPolicy Replacement: Past, Present, and Future - Tabitha Sable, Datadog & Tim Allclair, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Tabitha Sable, Datadog, Tim Allclair, Apple
- Schedule: https://kccncna2021.sched.com/event/lV9A/podsecuritypolicy-replacement-past-present-and-future-tabitha-sable-datadog-tim-allclair-apple
- Busca YouTube: https://www.youtube.com/results?search_query=PodSecurityPolicy+Replacement%3A+Past%2C+Present%2C+and+Future+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre PodSecurityPolicy Replacement: Past, Present, and Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9A/podsecuritypolicy-replacement-past-present-and-future-tabitha-sable-datadog-tim-allclair-apple
- YouTube search: https://www.youtube.com/results?search_query=PodSecurityPolicy+Replacement%3A+Past%2C+Present%2C+and+Future+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HsRRmlTJpls
- YouTube title: PodSecurityPolicy Replacement: Past, Present, and Future - Tabitha Sable & Tim Allclair
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/podsecuritypolicy-replacement-past-present-and-future/HsRRmlTJpls.txt
- Transcript chars: 27500
- Keywords: security, admission, actually, create, cluster, control, namespace, controller, restricted, version, everybody, policy, little, feature, default, meeting, together, replace

### Resumo baseado na transcript

hi um i'm tabitha sable unfortunately tim was not able to make it but his his contribution will be here he'll be he'll be here with us by video in a moment so i want to start by showing you one of my favorite tweets which is this tweet and the thing that i love so much about this tweet is on one hand it's like a big pile of line noise on the other hand if you have kubernetes api access then you can paste this tweet in and

### Excerpt da transcript

hi um i'm tabitha sable unfortunately tim was not able to make it but his his contribution will be here he'll be he'll be here with us by video in a moment so i want to start by showing you one of my favorite tweets which is this tweet and the thing that i love so much about this tweet is on one hand it's like a big pile of line noise on the other hand if you have kubernetes api access then you can paste this tweet in and then you become root so that is super fun and let's let's actually do that we're going to do this blind so here we are and now i now i think we're root we can get in here we can etsy kubernetes well anyway um there's a bunch of stuff in here like trust me we're we're really rude and that's and that's creepy that's not super good so what can we do about that is the question that i have and uh we have an answer to that and the answer to that is that i can put this label over here onto this onto this thing and i am changing things this is also bad all right we are just going to get away from that completely the point is that without admission control bad things are going to happen and so therefore we want to have admission control and so i'll clean up my windows here for you so yeah we want to have admission control we don't have admission control bad things are going to happen and so now we actually have admission control i can label a namespace and it will block me from being able to create that pod so yeah thank you so much for for joining me here virtually or in person for pod security policy replacement past present and future like i said yeah tim wasn't able to join us physically but he'll be here with us virtually in a couple of minutes he and i have prepared the session to show how we came together as a community to make the demo that you couldn't see because it was hidden from may happen so we'll start with the problem that we're trying to solve like what what does this even mean why do we need an emission controller and the easiest way to describe that is because without an admission controller kubernetes is a system administration tool everybody who can use it as a system administrator which means everybody who can create a pub is rude on every note in the cluster and if that's what you want you're perfect out of the box everything is golden but that's not really the way that we think about kubernetes if we think about kubernetes as being for scaling workloads and and things we we tend to think in terms of the pods and like we wan
