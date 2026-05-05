---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Connectivity"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Benoit Entzmann", "Feesh"]
sched_url: https://kccnceu2026.sched.com/event/2CW5p/an-immersive-and-visual-journey-into-kubernetes-networking-benoit-entzmann-feesh
youtube_search_url: https://www.youtube.com/results?search_query=An+Immersive+and+Visual+Journey+Into+Kubernetes+Networking+CNCF+KubeCon+2026
slides: []
status: parsed
---

# An Immersive and Visual Journey Into Kubernetes Networking - Benoit Entzmann, Feesh

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Benoit Entzmann, Feesh
- Schedule: https://kccnceu2026.sched.com/event/2CW5p/an-immersive-and-visual-journey-into-kubernetes-networking-benoit-entzmann-feesh
- Busca YouTube: https://www.youtube.com/results?search_query=An+Immersive+and+Visual+Journey+Into+Kubernetes+Networking+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre An Immersive and Visual Journey Into Kubernetes Networking.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5p/an-immersive-and-visual-journey-into-kubernetes-networking-benoit-entzmann-feesh
- YouTube search: https://www.youtube.com/results?search_query=An+Immersive+and+Visual+Journey+Into+Kubernetes+Networking+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xtjpdy8OmQQ
- YouTube title: An Immersive and Visual Journey Into Kubernetes Networking - Benoit Entzmann, Feesh
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/an-immersive-and-visual-journey-into-kubernetes-networking/Xtjpdy8OmQQ.txt
- Transcript chars: 22410
- Keywords: packet, destination, inside, mesh, tunnel, information, another, number, address, interface, program, routting, ebpf, cluster, traffic, everything, process, application

### Resumo baseado na transcript

So, I wanted to show you something different than PowerPoint, but obviously it's not as easy to to set up as a basic PowerPoint. And uh I have a background of two decades in networking and telecommunication. It's not you seldium doesn't use that for rooting inside of Kubernetes. backend.be be that's what you see on the on the layer 7 that's a name and inside of the Kubernetes cluster you have um a DNS resolution and this component is called the core DNS so when I want to reach uh any destination and It's it's an object, a Kubernetes object that lives inside of the cluster and it has an IP address or a number here in on three digits. So you can see four digit that's the the building somewhere in my Kubernetes and that's the IP address of the external IP of the service that is going to receive my packet.

### Excerpt da transcript

All right. So, thank you. It was I was just on time to set up the the screen. Um, thank you all for for coming. It's amazing to to have so much uh so much of you here today. So, I wanted to show you something different than PowerPoint, but obviously it's not as easy to to set up as a basic PowerPoint. So, I'm Benoman. I'm a dev secup consultant for fish in Switzerland. And uh I have a background of two decades in networking and telecommunication. And I can tell you that when I was starting with Kubernetes a few years ago, um it was I was as confused as anybody uh with the networking. So I had this idea to develop a 3D games just to explain the basics and go up to more advanced scenario. And this is what I'm going to to show you today. Uh just for me for for the information who is beginner who consider beginner with the networking. All right. Good. So a part of you. So that's good. So I hope I will explain it um to you with my uh with my game and you will get it a bit better. So uh four four level today. um two with pselium and two with ITO.

Both are graduated um uh project from the CNCF and uh so we will see how they operate and the the idea is to uh see the the the packet exactly how it goes from one point to another point. So let me bring you into my uh underwater world. So consider imagine you jump into the water. You you are diving and then you see some buildings. The buildings are the node into Kubernetes and you can see in some of the room there are some light that's the pod up and running. That's what we like. And so uh why not uh start from the pod from the room and see how the packet is processed from one room to another room. So that will be the first scenario and hopefully the Yeah. So the screen looks good now. So I will explain to you. So the fish is the packet. The packet is the the layer one is the physical. On the top you see the information it carries. So you see also the the fish has a backpack uh with four colors. That's the four colors of the layer. The information are layered organized into layer uh in the in the packet and the the color match what you see on the top.

So layer two uh that's the we traditionally is the the MAC address and everything. Uh that that's um but that's not used by selium. So I will show you selium inside kubernetes. Layer three is the rooting the IP address. So instead of an IP address, I will use some room number. So it's going to be easier to to understand and layer four uh that's the transportation layer.
