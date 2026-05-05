---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Dixita Narang", "Google", "Peter Hunt", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7pN/pod-power-liberating-kubernetes-users-from-container-resource-micromanagement-dixita-narang-google-peter-hunt-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Pod+Power%3A+Liberating+Kubernetes+Users+from+Container+Resource+Micromanagement+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Pod Power: Liberating Kubernetes Users from Container Resource Micromanagement - Dixita Narang, Google & Peter Hunt, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Dixita Narang, Google, Peter Hunt, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7pN/pod-power-liberating-kubernetes-users-from-container-resource-micromanagement-dixita-narang-google-peter-hunt-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Pod+Power%3A+Liberating+Kubernetes+Users+from+Container+Resource+Micromanagement+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Pod Power: Liberating Kubernetes Users from Container Resource Micromanagement.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pN/pod-power-liberating-kubernetes-users-from-container-resource-micromanagement-dixita-narang-google-peter-hunt-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Pod+Power%3A+Liberating+Kubernetes+Users+from+Container+Resource+Micromanagement+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-yyLsXTrrSY
- YouTube title: Pod Power: Liberating Kubernetes Users from Container Resource Micromanagement - D. Narang, P. Hunt
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/pod-power-liberating-kubernetes-users-from-container-resource-microman/-yyLsXTrrSY.txt
- Transcript chars: 30841
- Keywords: container, limits, containers, resources, memory, request, requests, specify, resource, feature, question, values, amount, little, basically, actually, within, specified

### Resumo baseado na transcript

welcome everyone in this session we are talking about part power an exciting new feature that will most likely go Alpha and 132 which will help uh simplify the kubernetes resource management as we are trying to move the resource management from the container level to the Pod level um my name is dsh and I work for Google and I'm an active contributor to signote community and with me is my friend hello my name is Peter I'm a uh senior software engineer at Red Hat I am a

### Excerpt da transcript

welcome everyone in this session we are talking about part power an exciting new feature that will most likely go Alpha and 132 which will help uh simplify the kubernetes resource management as we are trying to move the resource management from the container level to the Pod level um my name is dsh and I work for Google and I'm an active contributor to signote community and with me is my friend hello my name is Peter I'm a uh senior software engineer at Red Hat I am a cryo maintainer and a signno chair and I'm excited to be here and talking with you all so thank you for joining um so today we're going to be talk talking about one of the foundational aspects of multi- tennessy in kubernetes requests and limits um and I presume the majority of people are familiar but I'm going to go over for those of us that may be new here um a request is a way for a pod to specify um to the kubernetes uh system I would like to have at least this much of a resource today the resources we're going to be talking about are CPU and memory there are other ones you can request but those aren't relevant here and then a limit is saying I'm prepared to be punished if I used more than this amount I say this in this particular way and I'll explain a little bit later because you're not always punished of use more than it sometimes you can be so the way specifically that this works for uh memory because they work a little bit different between CPU and memory a memory request is used by the scheduler basically saying like so when the Pod is created you know the API server will give that to the schedule and schedule will be like ah I need to find a node with this much memory available the CRI does not use uh memory that's requested uh there is a memory qos kep which will change this but that's in this Perma Alpha State because uh it's there are some other issues with it so we're not doing that right now A Memory limit on the other hand scheduler doesn't use scheduler doesn't really pay attention to limits at all and the container runtime will map the limits uh specified to memory.

Max which is a file in the cgroup hierarchy cgroups are the way that U uh limits work in some requests as well um and this is sometimes enforced by the kernel by oom killing so if if a container uses more than its allotted amount of memory then it may be oom killed with the uh kernel is feeling memory pressure we can see a pod here as an example of uh you know what it looks like to specify memory requests and l
