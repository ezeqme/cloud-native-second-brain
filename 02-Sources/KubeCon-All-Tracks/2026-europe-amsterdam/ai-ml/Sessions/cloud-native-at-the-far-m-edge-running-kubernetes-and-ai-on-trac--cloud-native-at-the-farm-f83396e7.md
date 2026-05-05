---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Mauro Morales", "Spectro Cloud", "Jordan Karapanagiotis", "Aurea Imaging"]
sched_url: https://kccnceu2026.sched.com/event/2CW75/cloud-native-at-the-farm-edge-running-kubernetes-and-ai-on-tractors-mauro-morales-spectro-cloud-jordan-karapanagiotis-aurea-imaging
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+at+the+Far%28m%29+Edge%3A+Running+Kubernetes+and+AI+on+Tractors+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native at the Far(m) Edge: Running Kubernetes and AI on Tractors - Mauro Morales, Spectro Cloud & Jordan Karapanagiotis, Aurea Imaging

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mauro Morales, Spectro Cloud, Jordan Karapanagiotis, Aurea Imaging
- Schedule: https://kccnceu2026.sched.com/event/2CW75/cloud-native-at-the-farm-edge-running-kubernetes-and-ai-on-tractors-mauro-morales-spectro-cloud-jordan-karapanagiotis-aurea-imaging
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+at+the+Far%28m%29+Edge%3A+Running+Kubernetes+and+AI+on+Tractors+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native at the Far(m) Edge: Running Kubernetes and AI on Tractors.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW75/cloud-native-at-the-farm-edge-running-kubernetes-and-ai-on-tractors-mauro-morales-spectro-cloud-jordan-karapanagiotis-aurea-imaging
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+at+the+Far%28m%29+Edge%3A+Running+Kubernetes+and+AI+on+Tractors+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qCyDeCGavB8
- YouTube title: Cloud Native at the Far(m) Edge: Running Kubernetes and AI... Mauro Morales & Jordan Karapanagiotis
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-at-the-far-m-edge-running-kubernetes-and-ai-on-tractors/qCyDeCGavB8.txt
- Transcript chars: 22180
- Keywords: basically, running, application, blossom, devices, chyros, actually, nvidia, course, tractor, device, machine, talking, imaging, cannot, someone, upgrades, everything

### Resumo baseado na transcript

Uh so today we're going to be talking about cloud native at the farm edge. Uh it's an interesting topic for me because we're going to be talking about Kubernetes AI tractors. uh we learn we we run machine learning model uh models on the edge and then we send uh more lightweight uh more lightweight data to the cloud and of course uh yeah AI on the edge is quite a new domain quite a niche uh Spectre cloud is doing uh different uh management of uh clusters of Kubernetes on the cloud uh on edge on prem uh basically uh solving the complexity that you might have there. And the problem is that the edge can look like uh you're running in a tractor like uh Arya imaging is doing it. But the difference is that we uh many of the features that we designed on Chyros uh start on the drawing board uh thinking of the edge problems uh that they can solve because uh if you need it well you use it uh on

### Excerpt da transcript

Hello everyone. Thanks for joining us. How is your CubeCon going so far? I hope uh it's a good one. >> Awesome. Awesome. That's period. Uh so today we're going to be talking about cloud native at the farm edge. Uh you can credit that bad joke to me. Thank you. Uh it's an interesting topic for me because we're going to be talking about Kubernetes AI tractors. We're going to be talking about immutable systems. Um, so, uh, I find it very exciting. If you like it, it was because of me. If you didn't, it was because of Jordan. No, I'm just kidding. So, okay. Uh, why don't you get started, Jordan? >> Sure. Thanks, Moto. Uh, yeah, before, uh, diving into AI and Kubernetes, uh, on the edge and on tractors. Uh, I'm going to introduce a little bit what is, uh, precision farming and why do we do it. Uh, yeah, starting with some statistics. Uh basically it's estimated that uh about 25% of uh global crop production and that's a moderate estimate uh is uh affected by uh posth harvest losses and the reasons are usually spoilage uh labor shortage or uh size and shape irregularities of the fruits.

Uh now to give you some context in the Netherlands uh the average farm is producing about 10 million fruits per year. Uh that's usually apples and pears and if you think about it 2 and a half million um either don't make it to the market at competitive prices uh or don't make it to the market at all and most of it ends up in waste. Um at Ara Imaging uh we are trying to make a more sustainable uh orchard uh for the farmer for the environment and uh to reduce this waste. And how do we do it? Uh we use common techniques used by aronomists um there are quite uh quite some techniques there but um a common one and it's part of our core application is called uh blossom thinning or uh precision thinning. Uh how it works, you basically uh spray your orchards with um a salty solution early on in the blossom season, and that causes some of the flowers to dry out. And then the tree uh uses its energy to the remaining uh flowers, causing um less fruit to grow, but larger in size, more uniform in size, and often of better quality.

In terms of our application, this is how it looks like. First, the tractor is driving in the field. We are doing computer vision uh in real time. We are detecting blossoms on the trees. We create a blossom map. Basically, a map showing the flower level of each of every tree and we give that to the grower. Then the grower validates this map, adjusts some thresholds
