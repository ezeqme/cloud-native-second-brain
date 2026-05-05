---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Kevin Klues", "NVIDIA", "Patrick Ohly", "Intel"]
sched_url: https://kccnceu2024.sched.com/event/1Yhgp/dracon-demystifying-dynamic-resource-allocation-from-myths-to-facts-kevin-klues-nvidia-patrick-ohly-intel
youtube_search_url: https://www.youtube.com/results?search_query=DRAcon%3A+Demystifying+Dynamic+Resource+Allocation+-+from+Myths+to+Facts+CNCF+KubeCon+2024
slides: []
status: parsed
---

# DRAcon: Demystifying Dynamic Resource Allocation - from Myths to Facts - Kevin Klues, NVIDIA & Patrick Ohly, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Kevin Klues, NVIDIA, Patrick Ohly, Intel
- Schedule: https://kccnceu2024.sched.com/event/1Yhgp/dracon-demystifying-dynamic-resource-allocation-from-myths-to-facts-kevin-klues-nvidia-patrick-ohly-intel
- Busca YouTube: https://www.youtube.com/results?search_query=DRAcon%3A+Demystifying+Dynamic+Resource+Allocation+-+from+Myths+to+Facts+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre DRAcon: Demystifying Dynamic Resource Allocation - from Myths to Facts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhgp/dracon-demystifying-dynamic-resource-allocation-from-myths-to-facts-kevin-klues-nvidia-patrick-ohly-intel
- YouTube search: https://www.youtube.com/results?search_query=DRAcon%3A+Demystifying+Dynamic+Resource+Allocation+-+from+Myths+to+Facts+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=u7CktFEJbS8
- YouTube title: DRAcon: Demystifying Dynamic Resource Allocation - from Myths to Facts - Kevin Klues & Patrick Ohly
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/dracon-demystifying-dynamic-resource-allocation-from-myths-to-facts/u7CktFEJbS8.txt
- Transcript chars: 35187
- Keywords: resource, parameters, driver, gpu, resources, device, specific, scheduler, vendor, opaque, basically, actually, support, object, built-in, information, mentioned, selection

### Resumo baseado na transcript

these slides may be familiar to you if you have been in the keynote this morning I can go through them in two and a half minutes but I think you are all here to get more information about Dynamic resource allocation so we will do a lot more talking go more into details than we could in the keynote my name is Patrick Olie I work for Intel I'm one of the key Architects behind this new feature that you have been hearing about this is Kevin G from

### Excerpt da transcript

these slides may be familiar to you if you have been in the keynote this morning I can go through them in two and a half minutes but I think you are all here to get more information about Dynamic resource allocation so we will do a lot more talking go more into details than we could in the keynote my name is Patrick Olie I work for Intel I'm one of the key Architects behind this new feature that you have been hearing about this is Kevin G from Nvidia he's one of our biggest users of it and also contributing to a lot of content the example drivers so he will talk about how to use this feature with gpus which is what you all care about if you're running AI worklow so let's let's talk a little bit about what Dr does how it's designed uh it started out as an attempt to overcome the limitations of the device plug-in interface we took Inspirations from the volume management if you're familiar with the volume handling in kubernetes this new API is very similar we have something called a resource class that can be created by an administrator users create resource claims these resource claims get matched to specific hardware and then in a pot and in a container we reference this resource instance to give a container access to that allocated Hardware uh we designed it so that uh a resource can be local to a node that was what you could be doing with a device plugin interface but it can also be Network ATT attached um then I mentioned the API allows flexible sharing between ports and containers just because it's more it does have a standalone concept of something that you're referencing and then we also added a new concept for defining parameters for your resource claim these parameters are uh affecting their scheduling you may request something of a certain size but you can also in the same object Define parameters that configure your hardware and that becomes relevant when we have a complex piece of Hardware that needs to be initialized in a certain way in a vendor specific format so I've already mentioned vendors uh once now the key Point really is that Dr in kubernetes is just a framework in and it enables Hardware vendors to extend kubernetes by writing Dr drivers and these Dr drivers are then responsible for the hardware and also for user facing interface how to specify parameters depends on the hardware that you are asking for it has been an alpha for a while and we've been trying to get it to beer got some feedback from the community and to clarify why that h
