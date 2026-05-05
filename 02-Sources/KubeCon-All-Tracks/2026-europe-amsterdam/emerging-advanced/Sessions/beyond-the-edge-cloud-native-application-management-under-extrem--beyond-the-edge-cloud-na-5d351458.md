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
themes: ["Networking"]
speakers: ["Tobias Nöthlich", "Maximilian Nitsch", "D3TN GmbH"]
sched_url: https://kccnceu2026.sched.com/event/2CW6e/beyond-the-edge-cloud-native-application-management-under-extreme-network-conditions-tobias-nothlich-maximilian-nitsch-d3tn-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Edge%3A+Cloud+Native+Application+Management+Under+Extreme+Network+Conditions+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Beyond the Edge: Cloud Native Application Management Under Extreme Network Conditions - Tobias Nöthlich & Maximilian Nitsch, D3TN GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tobias Nöthlich, Maximilian Nitsch, D3TN GmbH
- Schedule: https://kccnceu2026.sched.com/event/2CW6e/beyond-the-edge-cloud-native-application-management-under-extreme-network-conditions-tobias-nothlich-maximilian-nitsch-d3tn-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Edge%3A+Cloud+Native+Application+Management+Under+Extreme+Network+Conditions+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Beyond the Edge: Cloud Native Application Management Under Extreme Network Conditions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6e/beyond-the-edge-cloud-native-application-management-under-extreme-network-conditions-tobias-nothlich-maximilian-nitsch-d3tn-gmbh
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Edge%3A+Cloud+Native+Application+Management+Under+Extreme+Network+Conditions+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9YjpYZVz6_4
- YouTube title: Beyond the Edge: Cloud Native Application Management Under Ex... Tobias Nöthlich & Maximilian Nitsch
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/beyond-the-edge-cloud-native-application-management-under-extreme-netw/9YjpYZVz6_4.txt
- Transcript chars: 23017
- Keywords: cluster, application, gateway, connection, clusters, management, obviously, ingress, applications, connected, solution, tolerant, microdtn, protocol, network, stable, minutes, registry

### Resumo baseado na transcript

Um before starting with our presentation, uh maybe a short introduction is in order. And uh we are R&D engineers at a small Dston based company uh that tries to push the boundaries of communication forward every day uh a little bit at a time. with this we have a few problems um the first problem I briefly mentioned before um deep space links are not continuous and they're also very frequent for disruptions very delayed very low bandwidth uh so we do not have the continuous network connectivity like But uh just for now, it's basically impossible to have a Kubernetes cluster span Earth and Mars. Now let's tackle these problems one by one and uh since we're at CubeCon let's start with the execution environment and ask ourselves the question why can't we just use standard Kubernetes on the satellite. To do so, they have to buffer the data in their internal memory or on persistent storage to deal with power outages for a potential arbitrary amount of time.

### Excerpt da transcript

All right. Uh thank you very much for coming today. Uh it's the last day. We're happy to see such a turnout. Um before starting with our presentation, uh maybe a short introduction is in order. So my name is Tubius. This is my colleague Maximan. And uh we are R&D engineers at a small Dston based company uh that tries to push the boundaries of communication forward every day uh a little bit at a time. And uh this is why we are here today to try and bring cloudnative application management to space and to you and obviously also to other extreme network environments. Now a quick view of the agenda. Um I'll give a short motivation on why we're doing this. Uh then I'll pass the stage to my colleague Maxan who's our resident DTN expert. Um to briefly introduce to you the background uh why we not just use Kubernetes. Uh what we use instead, how we make all of this work in space before I'll take over again and um well we'll get deep into the nitty-gritty of how we implemented all these things in Kubernetes in Helm and uh how we got it to work in the end.

Uh then there's a slide on key takeaways and future work. And on the last slide, there's going to be a few QR codes. Uh one for rating our session and a few for following us on LinkedIn and yeah the project website. Now without further ado, let's get started. Um maybe with a bit of a provocative question. Um who even cares about cloudnative applications in space? Well, it turns out quite a few people do actually. Now why don't we see any cloudnative deployments in space? Uh it's a bit harder than it sounds. Uh especially if we look into the deep space context there. Um I've brought an example use case as you can see here on the slide. Um very simplistic. We have a cluster on earth uh which is used by some researchers and operator and is connected to a ground station via well stable links as we have them on Earth usually. And then this cluster is connected to a cluster on Mars uh quite far away. The link is not as stable. uh there's quite a bit of one-way delay 13 minutes on average to be exact and then we have a satellite which is on around Mars orbits is connected to a ground station there and we have a rover which runs some research applications now with this we have a few problems um the first problem I briefly mentioned before um deep space links are not continuous and they're also very frequent for disruptions very delayed very low bandwidth uh so we do not have the continuous network connectivity like we ha
