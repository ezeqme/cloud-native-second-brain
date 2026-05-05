---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Joel Studler", "Swisscom", "Ashan Senevirathne", "Telstra"]
sched_url: https://kccnceu2026.sched.com/event/2CW0G/why-is-it-so-hard-to-run-a-5g-core-on-kubernetesand-what-needs-to-change-for-6g-joel-studler-swisscom-ashan-senevirathne-telstra
youtube_search_url: https://www.youtube.com/results?search_query=Why+Is+It+So+Hard+to+Run+a+5G+Core+on+Kubernetes%E2%80%94And+What+Needs+to+Change+for+6G+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Why Is It So Hard to Run a 5G Core on Kubernetes—And What Needs to Change for 6G - Joel Studler, Swisscom & Ashan Senevirathne, Telstra

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joel Studler, Swisscom, Ashan Senevirathne, Telstra
- Schedule: https://kccnceu2026.sched.com/event/2CW0G/why-is-it-so-hard-to-run-a-5g-core-on-kubernetesand-what-needs-to-change-for-6g-joel-studler-swisscom-ashan-senevirathne-telstra
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Is+It+So+Hard+to+Run+a+5G+Core+on+Kubernetes%E2%80%94And+What+Needs+to+Change+for+6G+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Why Is It So Hard to Run a 5G Core on Kubernetes—And What Needs to Change for 6G.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0G/why-is-it-so-hard-to-run-a-5g-core-on-kubernetesand-what-needs-to-change-for-6g-joel-studler-swisscom-ashan-senevirathne-telstra
- YouTube search: https://www.youtube.com/results?search_query=Why+Is+It+So+Hard+to+Run+a+5G+Core+on+Kubernetes%E2%80%94And+What+Needs+to+Change+for+6G+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=duYk-FjcKAg
- YouTube title: Why Is It So Hard to Run a 5G Core on Kubernetes—And What Needs... Joel Studler & Ashan Senevirathne
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/why-is-it-so-hard-to-run-a-5g-core-on-kubernetes-and-what-needs-to-cha/duYk-FjcKAg.txt
- Transcript chars: 37649
- Keywords: network, cloud-native, platform, configuration, question, please, networking, running, industry, mentioned, netconf, already, second, vendors, standard, operators, applications, future

### Resumo baseado na transcript

And behind that icon, there's a large distributed system which runs our mobile mobile core. And increasingly, this this mobile core, it's it's running on Kubernetes. And um we want to fundamentally think and sort of challenge how we operate and life cycle this network. Uh before we share our insights on what went well and what should be improved with with 5G and and Telco and Kubernetes, we would love to hear your insights. Um We really would love your insights to to hear what you think about 5G core and Kubernetes. On on this left side, you see what went well with 5G core and Kubernetes.

### Excerpt da transcript

Good afternoon, everyone. So, let's let's start our presentation. Hands up those who have a 5G connection on the on your mobile phones. Oh, that's good. Most Most of you have it. So, on your smartphone, you have a small 5G icon. And behind that icon, there's a large distributed system which runs our mobile mobile core. And increasingly, this this mobile core, it's it's running on Kubernetes. And we are here to share some of the challenges we see running and life cycling that that mobile core. So, we are representing two different operators, similar challenges. And some of you are from the Telco, some of you are not from the Telco, but I think most of the learnings will applicable be to to most of you. So, before we jump to the the technical details, I want to set the scene. Um So, the mobile mobile data traffic, it's predicted to grow three times in by by 2031. And that's not a not just a prediction. It's already in in the motion. Every network device that we bring in, every use case, every application that we run, it lands on the network.

Um also, the complexity, um it's predicted to increase uh because we we we do use multiple technologies. There's there's 4G, there's 5G, 5G standalone, um edge use cases, network slicing, etc. So, all of these adds up the operational like the surface. So, every operator here has been asked to maintain these networks. So, that's the third [clears throat] item. So, so the ask is um maintain and operate this this complex network with the with the same amount of people we have. Um So, you've got the traffic growing on one hand, the complexity complexity is increasing, but how do you maintain this this network with with with with with a very lean um like a team and an organization? And that that gap somehow needs to close. And um we want to fundamentally think and sort of challenge how we operate and life cycle this network. So, with that, my name is Ashan Seniviratna. I'm a product owner at Telstra. And my name is Joel Studler. I'm a lead engineer at Swisscom. Uh very happy to be here. Nice that you made it to our talk.

Uh before we share our insights on what went well and what should be improved with with 5G and and Telco and Kubernetes, we would love to hear your insights. This is a QR code that leads to a retro board. I'm going to show it very quickly. Um We really would love your insights to to hear what you think about 5G core and Kubernetes. On on this left side, you see what went well with 5G core and Kubernetes. If
