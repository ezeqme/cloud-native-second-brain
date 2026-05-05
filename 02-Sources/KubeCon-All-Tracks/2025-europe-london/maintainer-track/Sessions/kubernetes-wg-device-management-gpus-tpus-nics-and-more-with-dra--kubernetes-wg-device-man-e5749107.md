---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Kevin Klues", "NVIDIA", "Patrick Ohly", "Intel"]
sched_url: https://kccnceu2025.sched.com/event/1tczm/kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra-kevin-klues-nvidia-patrick-ohly-intel
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+WG+Device+Management+-+GPUs%2C+TPUs%2C+NICs+and+More+With+DRA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes WG Device Management - GPUs, TPUs, NICs and More With DRA - Kevin Klues, NVIDIA & Patrick Ohly, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Kevin Klues, NVIDIA, Patrick Ohly, Intel
- Schedule: https://kccnceu2025.sched.com/event/1tczm/kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra-kevin-klues-nvidia-patrick-ohly-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+WG+Device+Management+-+GPUs%2C+TPUs%2C+NICs+and+More+With+DRA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes WG Device Management - GPUs, TPUs, NICs and More With DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczm/kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra-kevin-klues-nvidia-patrick-ohly-intel
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+WG+Device+Management+-+GPUs%2C+TPUs%2C+NICs+and+More+With+DRA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z_15EyXOnhU
- YouTube title: Kubernetes WG Device Management - GPUs, TPUs, NICs and More With DRA - Kevin Klues & Patrick Ohly
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-wg-device-management-gpus-tpus-nics-and-more-with-dra/Z_15EyXOnhU.txt
- Transcript chars: 26928
- Keywords: device, resource, driver, devices, working, nvidia, hardware, basically, mentioned, support, forward, available, called, features, update, attributes, gpu, plugin

### Resumo baseado na transcript

So, welcome to this update session of the working group device management in Kubernetes, also known as what the heck is going on with DRA nowadays. And the reason why I am in that role is because I started kind of DRA in Kubernetes along with a few other folks long before it became a working group. The work that we've been doing affects overall Kubernetes architecture, autoscaling, networking, node uh interaction on the on with devices and and to a large extent also scheduling decisions. AI training and also figure out how to handle all the other hardware that traditionally has been perhaps not so well supported in Kubernetes. One of the key changes that we did to get to where we are is that we moved all the logic into the scheduleuler and that's a key change to the original design uh and that that basically unblocked us from going to beta as you will see soon. Then um small change perhaps but relevant if it gets up picked up in downstream Kubernetes distributions.

### Excerpt da transcript

So, welcome to this update session of the working group device management in Kubernetes, also known as what the heck is going on with DRA nowadays. Um, my name is Patrick Oie. I'm one of the co-chairs of this working group. And the reason why I am in that role is because I started kind of DRA in Kubernetes along with a few other folks long before it became a working group. Um I'm I'm Kevin Clues. I was also one of the people that started working on it way early on. Um and I just want to reiterate for those that um are here that this is this really is an update on what's going on in the working group. If you're here to learn about the details of DRRA and how it works under the hood and things like that, come talk to us afterwards because we're not going to give a primer on that in this in this talk. So, and and the third person who is not on the stage today because we are the official presenters is John Bellame. He's also here. We can discuss anything what comes up afterwards in the hallway track.

So, the three of us we are organizing the working group. It started out as an effort to have a more formal uh way of of driving dynamic resource allocation forward and uh that was the main focus but it's not the only thing. So overall our mission statement is to enable simple and efficient configuration sharing and allocation of accelerators and other specialized devices. So it it formed around GPUs but it's certainly not limited to that. We started the working group uh after CubeCon Europe almost almost a year ago because at that time interest really picked up and we figured that the the smaller team that had been working on it definitely needed to reach out to lots of different SIGs across Kubernetes. The work that we've been doing affects overall Kubernetes architecture, autoscaling, networking, node uh interaction on the on with devices and and to a large extent also scheduling decisions. So these six then decided to sponsor the working group. We set up regular meetings and yeah that's what we've been doing ever since.

We're trying to figure out how Kubernet is going forward can get out of or well get go beyond its original roots as as a service for mic as a management system for microservices towards what we all do today like running AI inference perhaps AI training and also figure out how to handle all the other hardware that traditionally has been perhaps not so well supported in Kubernetes. So as I said this is mostly about dynamic resource allocation at
