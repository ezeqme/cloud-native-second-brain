---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Xavier Avrillier", "Antonia von den Driesch", "Giant Swarm"]
sched_url: https://kccncna2025.sched.com/event/27FZl/kubernetes-at-the-edge-come-see-it-in-action-xavier-avrillier-antonia-von-den-driesch-giant-swarm
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+at+the+Edge+%E2%80%93+Come+See+It+in+Action%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes at the Edge – Come See It in Action! - Xavier Avrillier & Antonia von den Driesch, Giant Swarm

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Xavier Avrillier, Antonia von den Driesch, Giant Swarm
- Schedule: https://kccncna2025.sched.com/event/27FZl/kubernetes-at-the-edge-come-see-it-in-action-xavier-avrillier-antonia-von-den-driesch-giant-swarm
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+at+the+Edge+%E2%80%93+Come+See+It+in+Action%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes at the Edge – Come See It in Action!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZl/kubernetes-at-the-edge-come-see-it-in-action-xavier-avrillier-antonia-von-den-driesch-giant-swarm
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+at+the+Edge+%E2%80%93+Come+See+It+in+Action%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-9ijsskqp2E
- YouTube title: Kubernetes at the Edge – Come see It In Action! | Cloud Native Denmark 2025 Aarhus
- Match score: 0.827
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-at-the-edge-come-see-it-in-action/-9ijsskqp2E.txt
- Transcript chars: 29540
- Keywords: device, little, devices, running, mapper, factory, cluster, already, couple, custom, computing, pretty, protocol, instance, actually, mappers, install, camera

### Resumo baseado na transcript

Uh hello, my name is Antonia and this is my friend Savier and we want to talk to you about Kubernetes at the edge today. Um so we're going to start with a bit of an introduction to edge computing for those of you who may not be that familiar yet. So we had a look at um edge computing and now let's see why we might need kubernetes at the edge over there. So there are a number of challenges when we work with edge computing and the main ones are scale connectivity and um updates. And Kubernetes already solves most of these challenges um in traditional IT environments by being declarative as you know. U so we reduce manual operations for our operators and you get the same um familiar Kubernetes API that we already know and love.

### Excerpt da transcript

It's so nice to see you. Uh hello, my name is Antonia and this is my friend Savier and we want to talk to you about Kubernetes at the edge today. Uh we also going to show it to you in action. Let's all hope that it will work. Um so we're going to start with a bit of an introduction to edge computing for those of you who may not be that familiar yet. And then we want to talk about how it is used in the industry today and we will dive into a specific project which is called cube edge and we will look at the architecture and then we are going to demo it for you. So um after the demo we want to anchor everything a little bit back to the real world and hopefully we can have a little discussion at the end. Uh so edge computing what is that? Um according to Gardner's glossery edge computing is part of a distributed computing topology where information processing is located close to the edge where things and people produce or consume that information. Now how does that look like in practice? If you take a little look at this slide here, you can see a factory at the bottom and then you can also see a couple of clouds.

Um, a factory can be a place where information obviously among other things is produced or some sort of data. And usually the machinery that produces this data in a factory will be things such as sensors or robots or other machines that are used in the factory. And we can refer to these as IoT devices. And IoT stands for industrial internet of things. Now, traditionally, all this data produced by our devices is going to go up to the cloud, right? However, this can be extremely slow sometimes or it can be very expensive. Um, and also sometimes it can be impossible. So in that case uh we introduce this additional layer which is between the device and the cloud which we refer to as the edge. Um you can see the edge here in green and you can see a couple machines in there as well and you have to think about these as servers which are placed within the network of the factory. So they are physically close to the machines that we're working with. Now why would you want to do this? There are a couple of reasons for this and here's four.

So um the first one latency. So if your edge device is a self-driving car for example, you don't need any latency, right? You need to make really quick decisions. Then you also have bandwidth problems. So if you have a lot of raw data, it can be beneficial if you pre-process it somehow and then later have less data that you
