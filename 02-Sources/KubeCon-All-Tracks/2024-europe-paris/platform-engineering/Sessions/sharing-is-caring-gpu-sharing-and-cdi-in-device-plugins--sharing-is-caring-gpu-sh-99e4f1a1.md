---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Evan Lezar", "NVIDIA", "David Porter", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YeQ7/sharing-is-caring-gpu-sharing-and-cdi-in-device-plugins-evan-lezar-nvidia-david-porter-google
youtube_search_url: https://www.youtube.com/results?search_query=Sharing+Is+Caring%3A+GPU+Sharing+and+CDI+in+Device+Plugins+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sharing Is Caring: GPU Sharing and CDI in Device Plugins - Evan Lezar, NVIDIA & David Porter, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Evan Lezar, NVIDIA, David Porter, Google
- Schedule: https://kccnceu2024.sched.com/event/1YeQ7/sharing-is-caring-gpu-sharing-and-cdi-in-device-plugins-evan-lezar-nvidia-david-porter-google
- Busca YouTube: https://www.youtube.com/results?search_query=Sharing+Is+Caring%3A+GPU+Sharing+and+CDI+in+Device+Plugins+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sharing Is Caring: GPU Sharing and CDI in Device Plugins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQ7/sharing-is-caring-gpu-sharing-and-cdi-in-device-plugins-evan-lezar-nvidia-david-porter-google
- YouTube search: https://www.youtube.com/results?search_query=Sharing+Is+Caring%3A+GPU+Sharing+and+CDI+in+Device+Plugins+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4YS8mQuI_-Y
- YouTube title: Sharing Is Caring: GPU Sharing and CDI in Device Plugins - Christopher Desiniotis & David Porter
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sharing-is-caring-gpu-sharing-and-cdi-in-device-plugins/4YS8mQuI_-Y.txt
- Transcript chars: 41108
- Keywords: gpu, device, actually, container, slicing, devices, sharing, running, plugin, workload, workloads, memory, nvidia, resource, access, runtime, resources, clients

### Resumo baseado na transcript

uh hello everyone um Welcome to our session uh sharing is caring uh GPU sharing and CDI and device plugins uh my name is David Porter uh I'm from Google I work on the Google kubernetes engine team uh where I work on uh node and kind of our integration with accelerators and uh this is Chris yeah I'm Chris desis um I'm a software engineer at Nvidia I work on our Cloud native engineering team that works on enabling gpus in the container runtime ecosystem and in kubernetes cool

### Excerpt da transcript

uh hello everyone um Welcome to our session uh sharing is caring uh GPU sharing and CDI and device plugins uh my name is David Porter uh I'm from Google I work on the Google kubernetes engine team uh where I work on uh node and kind of our integration with accelerators and uh this is Chris yeah I'm Chris desis um I'm a software engineer at Nvidia I work on our Cloud native engineering team that works on enabling gpus in the container runtime ecosystem and in kubernetes cool so to get started let me just kind of set the landscape uh so the landscape as everyone is well aware during this coupon uh devices are becoming increasingly important in kubernetes right so we have all these new workloads uh things like inference training uh fine-tuning Etc and all of them are requiring devices uh so it's important that devices and accelerators are kind of well integrated in kubernetes uh just like uh other resources are today so uh what we're going to cover today um we're going to start by talking a little bit about uh how devices are integrated in kubernetes today uh then we're going to kind of go one level lower at the container runtime level and take a look at how container runtimes integrate with devices uh and how CDI is a new technology uh that's going to help enable that uh then we'll we're going to go up the stack a little bit and look at kind of resource management uh with some of these devices and we're going to focus on gpus and how uh GPU sharing can be enabled and lastly we'll kind of end with a little bit about uh the future of devices and device sharing uh in kubernetes so I think uh when we think about it kind of from the kubernetes perspective right I think one of the big reasons kubernetes is so successful and everybody uh you know really loves running kubernetes is because it's really good at Resource Management uh what kubernetes allows you to do is take you know your whole Fleet of nodes right with all different types of resources like CPU memory dis space and really allow you uh to be able to manage them under one control plane with one API and devices are now becoming increasingly important in that Resource Management space and we want to enable you to manage them just as effectively as you do with CPU memory and disk today so what we're trying to do from the community perspective is we're trying to build uh Open Standards here and common resource models both to actually consume and interact with these devices and uh to share their resources so
