---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Surya Seetharaman", "Red Hat", "Girish Moodalbail", "NVIDIA Inc"]
sched_url: https://kccncna2024.sched.com/event/1i7rA/thousands-of-gamers-one-kubernetes-network-surya-seetharaman-red-hat-girish-moodalbail-nvidia-inc
youtube_search_url: https://www.youtube.com/results?search_query=Thousands+of+Gamers%2C+One+Kubernetes+Network+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Thousands of Gamers, One Kubernetes Network - Surya Seetharaman, Red Hat & Girish Moodalbail, NVIDIA Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Surya Seetharaman, Red Hat, Girish Moodalbail, NVIDIA Inc
- Schedule: https://kccncna2024.sched.com/event/1i7rA/thousands-of-gamers-one-kubernetes-network-surya-seetharaman-red-hat-girish-moodalbail-nvidia-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Thousands+of+Gamers%2C+One+Kubernetes+Network+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Thousands of Gamers, One Kubernetes Network.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rA/thousands-of-gamers-one-kubernetes-network-surya-seetharaman-red-hat-girish-moodalbail-nvidia-inc
- YouTube search: https://www.youtube.com/results?search_query=Thousands+of+Gamers%2C+One+Kubernetes+Network+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=76tfwAvDWX8
- YouTube title: Thousands of Gamers, One Kubernetes Network - Surya Seetharaman, Red Hat & Girish Moodalbail
- Match score: 0.736
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/thousands-of-gamers-one-kubernetes-network/76tfwAvDWX8.txt
- Transcript chars: 32622
- Keywords: bandwidth, network, traffic, storage, streaming, maximum, gpu, interface, uplink, reverse, egress, control, packet, coming, ingress, stream, minimum, basically

### Resumo baseado na transcript

We're going to be talking about how to achieve end-to-end QoS in Kubernetes networks. We're going to be using the cloud gaming environment production clusters, you know, where we run Kubernetes at Nvidia as our use case to explain some of the challenges in networking and how we overcame them. And there is a Kubernetes CPU node also here, which is hosting your infrastructure components, API server, and other ingress and etc., which I've abstracted here. And then you have the storage network, which is the green network, like I mentioned. And the game stream, infra, the storage, they're all part of the OVN Kubernetes CNI is what we run underneath it. And before they log out, they have to save the data, their scores, their ranking, everything back into the storage network.

### Excerpt da transcript

Hey everyone. How's everyone doing? How many of you are going back today home? Well, we appreciate you coming to our talk. I know it's Friday. It's afternoon. It's one of the last sessions. Uh Thank you for being here. Thank you for the taking the time. We're going to be talking about how to achieve end-to-end QoS in Kubernetes networks. We're going to be using the cloud gaming environment production clusters, you know, where we run Kubernetes at Nvidia as our use case to explain some of the challenges in networking and how we overcame them. I'm Surya Sitaraman. I'm an engineer working at Red Hat in the OpenShift networking team. I'm also contributor to the SIG network upstream and also an OVN Kubernetes maintainer. Hey all, my name is Girish. I'm a distinguished engineer at Nvidia. I'm also one of the OVN Kubernetes maintainers. So, let's have some fun, right? How many of you play games? Raise hands. Yeah. Woah, hold on. A lot. So, you're the in the right talk, in the right room. How many of you play the games that you see here?

That is awesome. How many of you have GeForce accounts at Nvidia? A few of your hands, but that's a quite a lot, right? So, we're going to basically So, the the fun fact, I don't play games. Girish does not play games. But but we're doing the networking behind all these games that you play on the cloud, right? So, So, you can blame us. Yeah. So, let's imagine a scenario. You have an ongoing Dota game, right? You have some players in your cloud who are playing the game. We have a second game, which is also parallelly happening. So, this is going to be our case scenario here. We have two games, game one and game two. Let's map that to a Kubernetes cluster, which is why we're all here, right? So, imagine the players one, two, and three are part of your ongoing game one. And players eight and nine are part of your ongoing game two. All of these five player pods are part of the same Kubernetes GPU node. They're all sharing the same 25 GB uplink. And they're all sharing the resources on this node for bandwidth, right?

And there is a Kubernetes CPU node also here, which is hosting your infrastructure components, API server, and other ingress and etc., which I've abstracted here. So, that's a CPU node and there's a reverse proxy that's running in the CPU node. And any data that is coming from the player pod to this game stream network is reverse proxied back to the internet. So, external connections from pods inside the cluster to the i
