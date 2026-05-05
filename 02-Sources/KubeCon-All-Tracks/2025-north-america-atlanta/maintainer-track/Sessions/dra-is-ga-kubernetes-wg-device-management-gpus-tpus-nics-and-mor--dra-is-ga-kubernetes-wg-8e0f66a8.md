---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Kevin Klues", "NVIDIA", "Patrick Ohly", "Intel"]
sched_url: https://kccncna2025.sched.com/event/27Nu0/dra-is-ga-kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra-kevin-klues-nvidia-patrick-ohly-intel
youtube_search_url: https://www.youtube.com/results?search_query=DRA+is+GA%21+Kubernetes+WG+Device+Management+-+GPUs%2C+TPUs%2C+NICs+and+More+With+DRA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# DRA is GA! Kubernetes WG Device Management - GPUs, TPUs, NICs and More With DRA - Kevin Klues, NVIDIA & Patrick Ohly, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Kevin Klues, NVIDIA, Patrick Ohly, Intel
- Schedule: https://kccncna2025.sched.com/event/27Nu0/dra-is-ga-kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra-kevin-klues-nvidia-patrick-ohly-intel
- Busca YouTube: https://www.youtube.com/results?search_query=DRA+is+GA%21+Kubernetes+WG+Device+Management+-+GPUs%2C+TPUs%2C+NICs+and+More+With+DRA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre DRA is GA! Kubernetes WG Device Management - GPUs, TPUs, NICs and More With DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nu0/dra-is-ga-kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra-kevin-klues-nvidia-patrick-ohly-intel
- YouTube search: https://www.youtube.com/results?search_query=DRA+is+GA%21+Kubernetes+WG+Device+Management+-+GPUs%2C+TPUs%2C+NICs+and+More+With+DRA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Op4DNDTij1U
- YouTube title: DRA is GA! Kubernetes WG Device Management - GPUs, TPUs, NICs and More... Kevin Klues & Patrick Ohly
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dra-is-ga-kubernetes-wg-device-management-gpus-tpus-nics-and-more-with/Op4DNDTij1U.txt
- Transcript chars: 27715
- Keywords: resource, device, driver, devices, drivers, working, scheduleuler, cluster, available, actually, resources, features, hardware, dynamic, allocation, autoscaling, support, request

### Resumo baseado na transcript

This is the CubeCon North America update meeting of the working group device management and yes this is the place and talk where we are going to cover dynamic resource allocation. A small thing that you might have heard about and yeah we have done more on it. Network devices are covered by existing drivers, and we have an overall design that is supposed to be flexible enough to cover everything that we want to do with special hardware in Kubernetes going forward. working group where we are also going to cover uh advanced scheduling topics in general like gang scheduling but stay tuned I think we will branch out and we will just continue discussing all the work all the problems that you people have and try It is GA in cord Kubernetes the basic functionality and people have been waiting for that because it means that they can now start using it in DRA drivers. So I what I described so far is the the core part what we support in Kubernetes but Kubernetes itself doesn't manage any hardware that is what we need drivers for like we did with device plugins before uh we do have a bunch of

### Excerpt da transcript

Welcome everyone. This is the CubeCon North America update meeting of the working group device management and yes this is the place and talk where we are going to cover dynamic resource allocation. A small thing that you might have heard about and yeah we have done more on it. Uh we do these update meetings pretty much every CubeCon or at least the CubeCons that we go to. So the last one was at CubeCon Europe and we are going to cover new content that went into Kubernetes uh 134 and the one that we just almost finished with 135. My name is Patrick. I work for Intel on cloud native. I've been doing dynamic resource allocation for a while. With me on stage is Kevin Grizz from Nvidia. And in the front row we have John Bellame kicking it back and enjoying that he's not talking and we're here. Uh but he will be available for questions. Um if you get the slides later on all of these are links to our working group. Um we'll also have it on the slide later on again. So what is a working group and why do we have it in the first place?

So as I as I mentioned we have done the array dynamic resource allocation for a while even before the working group was formed but it became fairly popular at some point and we decided that we really need to have a place to discuss it and a working group in Kubernetes is cutting across multiple six. In this case we have pretty much all of the major ones in fact included. It's an architectural change for Kubernetes. It changes what Kubernetes is good for. It affects uh the node part where we actually have devices. That's where it came from originally. But it became very scheduling heavy because we need to make very difficult decisions uh in the scheduling part that also affects then autoscaling and we've branched out in terms of what kind of devices we are supporting. in reality today with drivers. So sick no s networking is involved because they want to make sure that the devices that are network hardware also work well. Um, I've mentioned hardware. It's started out as focusing on GPUs, but it's certainly not limited to that.

Network devices are covered by existing drivers, and we have an overall design that is supposed to be flexible enough to cover everything that we want to do with special hardware in Kubernetes going forward. Um so DRA as I mentioned is a is a large part of what we've been focusing on but we kept discussing other things in the scheduling space just this week and I think we kind of have a tentative agreement that
