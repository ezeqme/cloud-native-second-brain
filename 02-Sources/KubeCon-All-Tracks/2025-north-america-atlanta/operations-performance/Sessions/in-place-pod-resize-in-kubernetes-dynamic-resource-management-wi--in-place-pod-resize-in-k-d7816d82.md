---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Tim Allclair", "Mofi Rahman", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FdF/in-place-pod-resize-in-kubernetes-dynamic-resource-management-without-restarts-tim-allclair-mofi-rahman-google
youtube_search_url: https://www.youtube.com/results?search_query=In-Place+Pod+Resize+in+Kubernetes%3A+Dynamic+Resource+Management+Without+Restarts+CNCF+KubeCon+2025
slides: []
status: parsed
---

# In-Place Pod Resize in Kubernetes: Dynamic Resource Management Without Restarts - Tim Allclair & Mofi Rahman, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Tim Allclair, Mofi Rahman, Google
- Schedule: https://kccncna2025.sched.com/event/27FdF/in-place-pod-resize-in-kubernetes-dynamic-resource-management-without-restarts-tim-allclair-mofi-rahman-google
- Busca YouTube: https://www.youtube.com/results?search_query=In-Place+Pod+Resize+in+Kubernetes%3A+Dynamic+Resource+Management+Without+Restarts+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre In-Place Pod Resize in Kubernetes: Dynamic Resource Management Without Restarts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FdF/in-place-pod-resize-in-kubernetes-dynamic-resource-management-without-restarts-tim-allclair-mofi-rahman-google
- YouTube search: https://www.youtube.com/results?search_query=In-Place+Pod+Resize+in+Kubernetes%3A+Dynamic+Resource+Management+Without+Restarts+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HuC4k7fmTBk
- YouTube title: In-Place Pod Resize in Kubernetes: Dynamic Resource Management Without... Tim Allclair & Mofi Rahman
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/in-place-pod-resize-in-kubernetes-dynamic-resource-management-without/HuC4k7fmTBk.txt
- Transcript chars: 27273
- Keywords: resize, resources, memory, resource, actually, application, running, restart, limits, autoscaler, change, cublet, request, currently, container, changes, pending, controller

### Resumo baseado na transcript

>> So we're going to talk to you about what in place pod resize is all about and why potentially it would help you and why we should care. The basic idea is you have a deployment that has some number of pods and some signal happens. Anybody have application written in something like Java running on Kubernetes right so anything that is just in time compiled or just in time runtime. But today in Kubernetes you kind of have to give the resource it needs to start because otherwise you're going to get OM killed before you even start your application. Being able to scale your application down after the application is in running state is very useful. So for solving all of those problems and more introducing in place pod resize.

### Excerpt da transcript

So this talk is titled in place pod resize and my name is MPHI. I have here >> Tim Olair. >> So we're going to talk to you about what in place pod resize is all about and why potentially it would help you and why we should care. All of us know what HPA is. Yes. HPA more or less. Yeah. Yeah. HPA horizontal pod autoscaler. The basic idea is you have a deployment that has some number of pods and some signal happens. It could be you're using too much CPU, too much RAM, external resources like Kada telling you that you need more pods and the controller then spins up more pods. You have more copies of the same pods are in the request. Great. There's another one, right? You you have heard of in the past potentially called vertical pod autoscaler. Uh VPA is the same idea, but instead of saying I need more copies of the pod, you are saying I need this same pot that is serving request to be bigger. Right? So how many of you use VPA in production today? All right, fantastic. Do you like using VPA in production? >> Good.

Uh, if you do, that's good. But if you don't, the reason you might not like using VPA in production, the challenge with VPA there is when VPA scales up the pod, it kills the old pod and spins up a new pod, right? So, if you have any application that requires the pod to stick around during the resize, VP at this like as of like last month, VP did not actually do the thing you wanted it to do. There are other use cases, for example, like game servers. people are connected to your game. If you just kill that pod to make a bigger pod, some people might be angry, right? Like playing their games. Uh efficient bin packing. If you have a node, you want to use the node to the fullest capacity. If you could fit the right amount of resource just by sizing it bigger, fantastic. You can get more out of your resources. Prem worker. So you have a worker that is, let's say, using some resources and then when they're not being used, you can shrink them down. And when they're getting used again, you can scale them back up.

So that way you don't have to use the resource all the time but only when you need them. And finally start a boost. Anybody have application written in something like Java running on Kubernetes right so anything that is just in time compiled or just in time runtime. What happens is during startup it requires more resources because it has to do some calculation then but once the application is in fully running state it actually does not require as m
