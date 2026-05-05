---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Runtime Containers", "SRE Reliability", "Community Governance"]
speakers: ["Alexander Jung", "Unikraft"]
sched_url: https://kccncna2022.sched.com/event/182OM/beyond-orchestration-the-cloud-native-runtimes-ecosystem-for-performance-and-security-alexander-jung-unikraft
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Orchestration%3A+The+Cloud+Native+Runtimes+Ecosystem+for+Performance+and+Security+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Beyond Orchestration: The Cloud Native Runtimes Ecosystem for Performance and Security - Alexander Jung, Unikraft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Alexander Jung, Unikraft
- Schedule: https://kccncna2022.sched.com/event/182OM/beyond-orchestration-the-cloud-native-runtimes-ecosystem-for-performance-and-security-alexander-jung-unikraft
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Orchestration%3A+The+Cloud+Native+Runtimes+Ecosystem+for+Performance+and+Security+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Beyond Orchestration: The Cloud Native Runtimes Ecosystem for Performance and Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182OM/beyond-orchestration-the-cloud-native-runtimes-ecosystem-for-performance-and-security-alexander-jung-unikraft
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Orchestration%3A+The+Cloud+Native+Runtimes+Ecosystem+for+Performance+and+Security+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=h-Il4OBW5aI
- YouTube title: Beyond Orchestration: The Cloud Native Runtimes Ecosystem for Performance and... - Alexander Jung
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/beyond-orchestration-the-cloud-native-runtimes-ecosystem-for-performan/h-Il4OBW5aI.txt
- Transcript chars: 25926
- Keywords: kernel, application, container, virtual, security, actually, machine, unicraft, runtime, number, libraries, basically, binary, performance, course, unicorn, compile, process

### Resumo baseado na transcript

all right hello um good afternoon uh thank you all for coming to this presentation today um so today I'd like to talk about the titles beyond orchestration the cloud native runtimes ecosystem for performance and security uh my name is Alexander um I'm from a project called unicraft we're an open source uh Library operating system today I'm going to make a comparison between existing run times for the cloud what they look like what it kind of looks like to deploy a runtime in the cloud what it

### Excerpt da transcript

all right hello um good afternoon uh thank you all for coming to this presentation today um so today I'd like to talk about the titles beyond orchestration the cloud native runtimes ecosystem for performance and security uh my name is Alexander um I'm from a project called unicraft we're an open source uh Library operating system today I'm going to make a comparison between existing run times for the cloud what they look like what it kind of looks like to deploy a runtime in the cloud what it means for security and performance and how unicraft is trying to change the status quo of what it is to have a performant and a secure application in the cloud so the themes that I've noticed over the last few days here at kubecon going down booze and going at lots of different uh talks is that there's a lot of cve scanning package scanning there's applications that are you know we look at a particular item and then we have some system to introspect it and we can do this in a number of different ways and so there's also a number of Open Source projects that are doing this but there are also a number of you know companies that are offering this as a service and this is sort of the idea here is we're going to step back and kind of what's the problem here uh in overall right in the sense that we are looking at a traditional system and the other one is performance and how we tackle this and again it's a lot of introspection it's a lot of you know there's some different themes here like we have ai models to look at traffic detection and then we optimize that way or we look at inside and we change the libraries we compile them to make them more Specialized or we have like slimmers like there's darker slim slim AI out of this there are a number of ways that we can reduce what we have already to make it smaller and therefore more performant and so overall in general what we're doing is we're introspecting and we're looking at something and we're trying to find out ways to make it more secure and ways to make it more performant and when we look at how we approach the runtime of things in the cloud there are a number of different sort of solutions that are lightweight if you look at some projects K3 Os from Rancher Venture RS of course this Linux kit and this from VMware photon sort of a container runtime platform and these projects they basically still rely on the traditional kernel stack and they still run on top of a hypervisor and so what I'm trying to get at here is that b
