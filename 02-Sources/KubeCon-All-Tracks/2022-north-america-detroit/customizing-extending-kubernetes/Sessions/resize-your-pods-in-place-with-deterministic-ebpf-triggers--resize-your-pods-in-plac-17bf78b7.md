---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Pablo Chico de Guzman", "Okteto", "Vinay Kulkarni", "Futurewei Technologies"]
sched_url: https://kccncna2022.sched.com/event/182HU/resize-your-pods-in-place-with-deterministic-ebpf-triggers-pablo-chico-de-guzman-okteto-vinay-kulkarni-futurewei-technologies
youtube_search_url: https://www.youtube.com/results?search_query=Resize+Your+Pods+In-Place+With+Deterministic+eBPF+Triggers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Resize Your Pods In-Place With Deterministic eBPF Triggers - Pablo Chico de Guzman, Okteto & Vinay Kulkarni, Futurewei Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Pablo Chico de Guzman, Okteto, Vinay Kulkarni, Futurewei Technologies
- Schedule: https://kccncna2022.sched.com/event/182HU/resize-your-pods-in-place-with-deterministic-ebpf-triggers-pablo-chico-de-guzman-okteto-vinay-kulkarni-futurewei-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=Resize+Your+Pods+In-Place+With+Deterministic+eBPF+Triggers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Resize Your Pods In-Place With Deterministic eBPF Triggers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HU/resize-your-pods-in-place-with-deterministic-ebpf-triggers-pablo-chico-de-guzman-okteto-vinay-kulkarni-futurewei-technologies
- YouTube search: https://www.youtube.com/results?search_query=Resize+Your+Pods+In-Place+With+Deterministic+eBPF+Triggers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jjfa1cVJLwc
- YouTube title: Resize Your Pods In-Place With Deterministic eBPF Triggers - Pablo Chico de Guzman & Vinay Kulkarni
- Match score: 0.838
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/resize-your-pods-in-place-with-deterministic-ebpf-triggers/jjfa1cVJLwc.txt
- Transcript chars: 27547
- Keywords: container, resize, memory, resources, status, request, containers, environments, development, running, developer, requests, ebpf, working, update, feature, environment, application

### Resumo baseado na transcript

hello everyone thanks for coming my name is Pablo I'm one of the founders and the CDO adotedo is a development platform to deploy remote development environments and kubernetes and we will talk about that a little bit later and hi I'm vinay I work for future Bay Technologies it's the research armor for parent company Huawei and I've been working on kubernetes my interests are in kubernetes network and compute and lately ebpf and we hope to have a good talk with you today thank you cool so this magic of ebpf for you thank you [Applause] okay let me take a moment to thank the demo Gods here for saving the surprises for another day and uh so what did we what did we see today we saw that uh we have this

### Excerpt da transcript

hello everyone thanks for coming my name is Pablo I'm one of the founders and the CDO adotedo is a development platform to deploy remote development environments and kubernetes and we will talk about that a little bit later and hi I'm vinay I work for future Bay Technologies it's the research armor for parent company Huawei and I've been working on kubernetes my interests are in kubernetes network and compute and lately ebpf and we hope to have a good talk with you today thank you cool so this is the agenda of the talk um we are going to introduce the idea of cloud native development environments uh the problems that they solve and also some of their challenges one of them is to make them cost effective so we will analyze the different challenges there and then we will introduce a feature coming soon it's in place but resize and the idea with this feature is that you can modify that request and the limits of a running Pod without restarting the bottom uh after that we will see a demo using in place battery size and evpf to optimize the infrastructure utilization of cloud native development environments and we will finalize with some takeaways okay so let's talk about Cloud native development environments and first let's see the current state of the Earth so most companies are moving to kubernetes and microservices for the library actually okay so most companies are moving to kubernetes and microservices for the right research right they solve many problems in production environments but they also come with some challenges and one of them is that they make make it harder to mimic your production environment in your local deaf environment um even with tools like Docker local kubernetes distributions like mini Cube you need to install this software run all these micro services so there are several issues there one of them is that you may run out of CPU and memory in your laptop so things go very slow or even stop working um you need to maintain local configuration so if there is something wrong in your Dev environment it's very difficult to replicate the same problem in other laptop or it's very hard for anyone else to troubleshoot what is the issue and if you are using for example multi-repo it's not trivial to orchestrate the build pools and deploy of all these containers running locally so what most people do is to assume an environment disparity between deaf environments and production and I think this is wrong because at the end what you are doing is Shi
