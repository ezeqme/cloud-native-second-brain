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
themes: ["Networking", "Kubernetes Core"]
speakers: ["Masaharu Kanda", "NTT", "Inc.", "Lionel Jouin", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CW67/multi-network-step-by-step-enabling-sr-iov-support-from-kubernetes-network-dra-drivers-masaharu-kanda-ntt-inc-lionel-jouin-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Network+Step-by-Step%3A+Enabling+SR-IOV+Support+From+Kubernetes+Network+%28DRA%29+Drivers+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Multi-Network Step-by-Step: Enabling SR-IOV Support From Kubernetes Network (DRA) Drivers - Masaharu Kanda, NTT, Inc. & Lionel Jouin, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Masaharu Kanda, NTT, Inc., Lionel Jouin, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CW67/multi-network-step-by-step-enabling-sr-iov-support-from-kubernetes-network-dra-drivers-masaharu-kanda-ntt-inc-lionel-jouin-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Network+Step-by-Step%3A+Enabling+SR-IOV+Support+From+Kubernetes+Network+%28DRA%29+Drivers+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Multi-Network Step-by-Step: Enabling SR-IOV Support From Kubernetes Network (DRA) Drivers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW67/multi-network-step-by-step-enabling-sr-iov-support-from-kubernetes-network-dra-drivers-masaharu-kanda-ntt-inc-lionel-jouin-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Multi-Network+Step-by-Step%3A+Enabling+SR-IOV+Support+From+Kubernetes+Network+%28DRA%29+Drivers+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vINwfpvvpKI
- YouTube title: Multi-Network Step-by-Step: Enabling SR-IOV Support From Kubernetes... Masaharu Kanda & Lionel Jouin
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/multi-network-step-by-step-enabling-sr-iov-support-from-kubernetes-net/vINwfpvvpKI.txt
- Transcript chars: 26042
- Keywords: network, bandwidth, driver, device, resource, devices, capacity, multiple, config, hardware, request, second, deploy, configuration, interface, question, support, working

### Resumo baseado na transcript

Um, welcome to this talk about multi network and SRV using the new model Kubernetes network driver. I was working on network service mesh before and I've been I'm also a CNI maintainer. And this is very critical for high performance and and advanced features at scale. We have um uh large scale simula for example with the large scale simulation that require massive IO and and a IML training and inference with a large distributed uh node exchange uh and large volume of data. Um now now let's take a or let's zoom out and what we are doing in kubernetes itself to support multi network configuration through the multi network sub project that is a a sig network sub project. So DRA allows uh us in Kubernetes to manage hardware and virtual devices more flexibly including network interfaces.

### Excerpt da transcript

Hello everyone. Um, welcome to this talk about multi network and SRV using the new model Kubernetes network driver. Um, I'm Lo. Um, I'm working on Red Hat. Uh, I'm a multi network project lead. I've been involved in uh this area for a while. I was working on network service mesh before and I've been I'm also a CNI maintainer. And here is Masar. >> Yeah, I'm Masar. I'm from entity. I'm developing the disagregated computing infrastructure controller. So today we're talking about SRV in Kubernetes. So let's start really at the basic things the foundation. So what is SRV? So uh the device to try to represent and cover in Kubernetes are this V2 function that are provided by SRV capabilics and SRV is a PCI express standard that allows a single physical network card to expose multiple logical function or uh interfaces called virtual function or VF. So this is not uh software virtualization it's it's a hardware level virtualization done directly by the nick. So this comes with some limitation. So the first is like um you need requirement you need the requirement or you need to to have a you need you require the hardware support itself.

You also have a uh amount of for example VF that can be configured by the next that is fixed by the hardware itself. But from the so so what's the idea with the SRV is from the operating uh system perspective is the idea is to have each VF to look like completely independent PCI uh devices with its own PCI configuration space its own MAC address and a lot of a lot of uh different configuration but in reality a lot of this uh or or this VF will share the same underlying physical nick So for example the the bandwidths will be shared between all the VF and this becomes very relevant for what we will talk about today uh uh with the the bandwidth guarantee for example so now we understand what's quickly what a VF is why do they matter so SRV is typically for and uh highend nicks that includes advanced capabilities like hardware lowloading Um so you can run RDMA, traffic steering, encryption offload and more. So having the ability to duplicate this uh physical nick uh into multiple sub interfaces allows each workloads to to get what they would get as a their own dedicated nick.

So you can save money by having one nick and using it like multiple times. And this is very critical for high performance and and advanced features at scale. So this um hardware level enable deterministic low latency networking. So we bypass the kernel and and we
