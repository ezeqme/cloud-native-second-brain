---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Kevin Klues", "NVIDIA", "Alexey Fomenko", "Intel"]
sched_url: https://kccnceu2023.sched.com/event/1HyWy/device-plugins-20-how-to-build-a-driver-for-dynamic-resource-allocation-kevin-klues-nvidia-alexey-fomenko-intel
youtube_search_url: https://www.youtube.com/results?search_query=Device+Plugins+2.0%3A+How+to+Build+a+Driver+for+Dynamic+Resource+Allocation+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Device Plugins 2.0: How to Build a Driver for Dynamic Resource Allocation - Kevin Klues, NVIDIA & Alexey Fomenko, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kevin Klues, NVIDIA, Alexey Fomenko, Intel
- Schedule: https://kccnceu2023.sched.com/event/1HyWy/device-plugins-20-how-to-build-a-driver-for-dynamic-resource-allocation-kevin-klues-nvidia-alexey-fomenko-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Device+Plugins+2.0%3A+How+to+Build+a+Driver+for+Dynamic+Resource+Allocation+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Device Plugins 2.0: How to Build a Driver for Dynamic Resource Allocation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWy/device-plugins-20-how-to-build-a-driver-for-dynamic-resource-allocation-kevin-klues-nvidia-alexey-fomenko-intel
- YouTube search: https://www.youtube.com/results?search_query=Device+Plugins+2.0%3A+How+to+Build+a+Driver+for+Dynamic+Resource+Allocation+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_fi9asserLE
- YouTube title: Device Plugins 2.0: How to Build a Driver for Dynamic Resource Allocation - K Klues & Alexey Fomenko
- Match score: 0.942
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/device-plugins-2-0-how-to-build-a-driver-for-dynamic-resource-allocati/_fi9asserLE.txt
- Transcript chars: 39519
- Keywords: resource, driver, allocation, resources, controller, plugin, actually, device, access, gpu, claims, parameters, allocate, available, devices, object, scheduler, basically

### Resumo baseado na transcript

so my name is Kevin kluz I'm from Nvidia and my colleague Alexei fomenko here from Intel we're going to be giving a joint talk on device plugins 2.0 how to build a driver for dynamic resource allocation otherwise known as dra so what exactly is dynamic resource allocation well it's a new way of requesting access to resources available in kubernetes 126 and Beyond it provides an alternative to the count based interface of for example asking for nvidia.com gpu2 and using this alternative interface it puts full control

### Excerpt da transcript

so my name is Kevin kluz I'm from Nvidia and my colleague Alexei fomenko here from Intel we're going to be giving a joint talk on device plugins 2.0 how to build a driver for dynamic resource allocation otherwise known as dra so what exactly is dynamic resource allocation well it's a new way of requesting access to resources available in kubernetes 126 and Beyond it provides an alternative to the count based interface of for example asking for nvidia.com gpu2 and using this alternative interface it puts full control of the API to request resources in the hands of third-party party developers so if you you know if you have simple devices you can continue to use the existing device plugin interface but for more complex devices this new mechanism exists to give you a much more powerful interface one can think of dynamic resource allocation as sort of a generalization of the persistent volume API for all types of resources not just volumes and the key Concepts that you want to have in mind when you're thinking about Dynamic resource allocation is that of the resource class and its Associated class parameters which help you define the API for resource classes as well as resource claims and resource claim templates and their Associated claim parameters which I'll go into a little bit more detail as we go through the talk so before I talk about those I want to just go through a really quick example and show you you know demonstrate kind of how you would move from a user's perspective of requesting access to a device via the traditional device plugin API and what that same request would look like under dra so our traditional device plugin if you were to ask for a single GPU under your limits section of your resources spec in your in your pod spec you could ask for something like nvidia.com GPU one and you would get access to that GPU at runtime under Dynamic resource allocation that a similar similar allocation would be would be done using what you see here on the right so the things to note here are that I have this object this separate object for my pod called a resource claim template inside that resource claim template I give reference to a specific resource class in this case the resource class name is called Nvidia gpu.nvidia.com and this is something that's associated with the driver that I'm going to you know talk through today how you can develop one of these but this name gets associated with your driver is installed by the cluster admin and is kind of a
