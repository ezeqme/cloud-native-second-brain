---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["John Belamaric", "Google", "Patrick Ohly", "Intel", "Kevin Klues", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1hovp/kubernetes-wg-device-management-advancing-k8s-support-for-gpus-john-belamaric-google-patrick-ohly-intel-kevin-klues-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+WG+Device+Management+-+Advancing+K8s+Support+for+GPUs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes WG Device Management - Advancing K8s Support for GPUs - John Belamaric, Google; Patrick Ohly, Intel; Kevin Klues, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: John Belamaric, Google, Patrick Ohly, Intel, Kevin Klues, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1hovp/kubernetes-wg-device-management-advancing-k8s-support-for-gpus-john-belamaric-google-patrick-ohly-intel-kevin-klues-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+WG+Device+Management+-+Advancing+K8s+Support+for+GPUs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes WG Device Management - Advancing K8s Support for GPUs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hovp/kubernetes-wg-device-management-advancing-k8s-support-for-gpus-john-belamaric-google-patrick-ohly-intel-kevin-klues-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+WG+Device+Management+-+Advancing+K8s+Support+for+GPUs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zpFj7ZA6E14
- YouTube title: Kubernetes WG Device Management - Advancing K8s Support for GPUs - J. Belamaric, P. Ohly, K. Klues
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-wg-device-management-advancing-k8s-support-for-gpus/zpFj7ZA6E14.txt
- Transcript chars: 32721
- Keywords: gpu, device, devices, resource, driver, request, nvidia, called, support, actually, drivers, nvidia.com, associated, working, within, reference, sharing, requests

### Resumo baseado na transcript

all right well thank you all for joining us today um uh this is a discussion of the a new working group we've created in the kubernetes open source uh Community uh and we're focused on device management um my name is John bamer I'm from Google and uh um these are my two co-chairs yeah my name is Patrick Uli I work for Intel I've been the original author and architect if you want of dynamic resource allocation before it became a working group I've been driving it forward

### Excerpt da transcript

all right well thank you all for joining us today um uh this is a discussion of the a new working group we've created in the kubernetes open source uh Community uh and we're focused on device management um my name is John bamer I'm from Google and uh um these are my two co-chairs yeah my name is Patrick Uli I work for Intel I've been the original author and architect if you want of dynamic resource allocation before it became a working group I've been driving it forward for a few years now and I'm Kevin Clues I work for NVIDIA uh and I started working with Patrick in the early days on this as well uh mostly to push forward the Nvidia use cases for for Dr so what is uh the working group device management and why are we why do we exist I mean the the the short answer this is our sort of mission statement it's enabling um simple and efficient configuration sharing and allocation of accelerators and other specialized devices so this grew out of uh discussions Dr has been worked on for a few years as Patrick was saying but we realized that we we needed a place in the community um to kind of bring together all the use cases and all the different vendors and all the different stakeholders so back in um cucon EU um earlier this year uh after those discussions we decided to form a working group um and the primary thing we're working on is Dr right now and we may disband after Dr is complete but there are potentially other um areas that are within scope so we'll make that decision uh in a year or two when we've finished what we're working on um in any case uh it's a joint effort between a bunch of different sigs and um I do want to emphasize that Although our primary use cases because of where our uh Market is today is around gpus um this also includes NX fpgas even network attached devices um mental model is usually cards in a in a not in a in a in a box but it actually can be other things as well so as I said Dr is the main thing we've been focusing on and what exactly is is this Dynamic resource allocation I think the easiest way to conceive of it is sort of these these four parts that are on the screen here one is an API a new kubernetes API which vendors and uh can use to describe their devices so rather than just saying this is we have five Nvidia gpus which is how we would do it say today with Device plug-in um we have a much richer uh API for describing the devices adding a bunch of metadata and um other information about about the devices and how they're co
