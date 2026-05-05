---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Ed Warnicke", "Cisco", "Lee Calcote", "Layer5"]
sched_url: https://kccncna2022.sched.com/event/1BZJl/the-state-of-the-cloud-native-network-deep-dive-from-tag-network-ed-warnicke-cisco-lee-calcote-layer5
youtube_search_url: https://www.youtube.com/results?search_query=The+State+of+the+Cloud+Native+Network%3A+Deep-dive+from+TAG-Network+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The State of the Cloud Native Network: Deep-dive from TAG-Network - Ed Warnicke, Cisco & Lee Calcote, Layer5

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Ed Warnicke, Cisco, Lee Calcote, Layer5
- Schedule: https://kccncna2022.sched.com/event/1BZJl/the-state-of-the-cloud-native-network-deep-dive-from-tag-network-ed-warnicke-cisco-lee-calcote-layer5
- Busca YouTube: https://www.youtube.com/results?search_query=The+State+of+the+Cloud+Native+Network%3A+Deep-dive+from+TAG-Network+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The State of the Cloud Native Network: Deep-dive from TAG-Network.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/1BZJl/the-state-of-the-cloud-native-network-deep-dive-from-tag-network-ed-warnicke-cisco-lee-calcote-layer5
- YouTube search: https://www.youtube.com/results?search_query=The+State+of+the+Cloud+Native+Network%3A+Deep-dive+from+TAG-Network+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JrGQmbOjPkA
- YouTube title: The State of the Cloud Native Network: Deep-dive from TAG-Network - Ed Warnicke & Lee Calcote
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-state-of-the-cloud-native-network-deep-dive-from-tag-network/JrGQmbOjPkA.txt
- Transcript chars: 33534
- Keywords: network, cluster, mesh, actually, networking, clusters, questions, envoy, running, meshes, question, native, interesting, ingress, traffic, single, interface, workloads

### Resumo baseado na transcript

welcome so for those of you who've been in talks that I've given before at cubecon at other venues no I like to do a very interactive talk and interact with the audience a great deal partially because it makes it more fun for everyone involved it's more fun for me it's more fun for you but also because there's a lot to be learned from what's actually going on with your audience and so I'll be asking you throughout for a bunch of questions that are out there sometimes

### Excerpt da transcript

welcome so for those of you who've been in talks that I've given before at cubecon at other venues no I like to do a very interactive talk and interact with the audience a great deal partially because it makes it more fun for everyone involved it's more fun for me it's more fun for you but also because there's a lot to be learned from what's actually going on with your audience and so I'll be asking you throughout for a bunch of questions that are out there sometimes for specific answers sometimes just for a sense of the room but like any good scientist I like to calibrate my measurements before we begin so quick question how many of you actually expected to be in the state of the cloud networking talk today okay and how many of you were lost okay good that's always a good start law stragglers are welcome certainly but but usually not expected so when you look at the state of the cloud native networking Cloud native as a secular movement has largely been about dropping the representations of the physical world that we all dealt with in Cloud 1.0 right so we no longer build virtual interfaces and virtual routers and virtual load you know everything we're no longer reconstructing the physical artifacts just slapping a v in front of them instead we're stopping to ask ourselves what actually serves developers in terms of enabling them to actually function and this is incredibly liberating in many ways but it does have a few side effects that can cause confusion so for how many of you is this slide clear okay all right so some of you are just pulling my leg I see that no I don't expect this to be clear for anyone this is a giant collection of logos of projects in the cloud native networking space as an amorphous jumble you should be confused by this but confusion is actually not something you're seeking in a cloud native environment what are the central maxims of cloud native is minimal toil and minimal toil is not just the amount of work that you have to do to get what you want it also includes the cognitive toil involved in understanding what to do if I give you an interface with two buttons A and B but you're gonna have to spend six weeks to decide which one to press that is not a minimal toil interface so what I'm going to do for you here today is I'm going to actually take this amorphous blob of things and break them down into a structure where you can understand relatively simply the options and choices available to you as you try and solve your problems
