---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Steven Wong", "VMware", "Dejan Bosanac", "Red Hat", "Kilton Hopkins", "Edgeworx"]
sched_url: https://kccncna2021.sched.com/event/lV6q/kubernetes-on-edge-bringing-your-code-to-constrained-places-steven-wong-vmware-dejan-bosanac-red-hat-kilton-hopkins-edgeworx
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+on+Edge%3A+Bringing+Your+Code+to+Constrained+Places+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes on Edge: Bringing Your Code to Constrained Places - Steven Wong, VMware; Dejan Bosanac, Red Hat; Kilton Hopkins, Edgeworx

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Steven Wong, VMware, Dejan Bosanac, Red Hat, Kilton Hopkins, Edgeworx
- Schedule: https://kccncna2021.sched.com/event/lV6q/kubernetes-on-edge-bringing-your-code-to-constrained-places-steven-wong-vmware-dejan-bosanac-red-hat-kilton-hopkins-edgeworx
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+on+Edge%3A+Bringing+Your+Code+to+Constrained+Places+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes on Edge: Bringing Your Code to Constrained Places.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6q/kubernetes-on-edge-bringing-your-code-to-constrained-places-steven-wong-vmware-dejan-bosanac-red-hat-kilton-hopkins-edgeworx
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+on+Edge%3A+Bringing+Your+Code+to+Constrained+Places+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KBFh_X2N2vA
- YouTube title: Kubernetes on Edge: Bringing Your Code to Constraine... Steven Wong, Dejan Bosanac & Kilton Hopkins,
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-on-edge-bringing-your-code-to-constrained-places/KBFh_X2N2vA.txt
- Transcript chars: 29456
- Keywords: assembly, container, webassembly, docker, actually, running, access, containers, environment, interface, runtime, kilton, similar, payload, little, basically, workload, camera

### Resumo baseado na transcript

hi welcome to cubecon 2021 in los angeles this session is about running workloads at edge in a new way using webassembly with kubernetes you're about to get updates from uh i'm steve wong with vmware representing the kubernetes iot edge working group i'm joined by dan bosinek of red hat and kilton hopkins of edgeworks but they couldn't be here physically but they graciously prepared recordings which will be patching in and they're going to be online for the q a section the agenda we're going to do a like to avoid the big network transport cost but a lot of this is about latency and resilience and web assembly looks like a good way to bring compute close to sources that are dealing with data sensors and data generation and event generation um

### Excerpt da transcript

hi welcome to cubecon 2021 in los angeles this session is about running workloads at edge in a new way using webassembly with kubernetes you're about to get updates from uh i'm steve wong with vmware representing the kubernetes iot edge working group i'm joined by dan bosinek of red hat and kilton hopkins of edgeworks but they couldn't be here physically but they graciously prepared recordings which will be patching in and they're going to be online for the q a section the agenda we're going to do a brief intro to what web assembly is why and where it might be useful then dion and kilton jumped hands on and tried out webassembly with kubernetes and they're going to give a report on what the current experience and future potential is like we'll wrap up with links on how you can join the working group of people trying to apply kubernetes at edge what is web assembly well it's an open standard for portable programs that can be written in almost any language they are extremely portable a web assembly can be run unchanged on arm x86 and other cpus and they're also not locked into an os web assembly was originally designed to run inside of a web browser in a safe way but people discovered that it was also useful as a portable and efficient way to run sandbox code in other places far beyond the browser contacts these r the runtimes that uh support web assembly range down to support tiny os less microcontrollers you know the kinds of things that might cost eight dollars and run for two years on a on a coin cell battery um all these aspects make them attractive for running on devices with constrained resources uh so how does webassembly compare to docker well solomon hikes uh who's often credited as being the inventor of docker has been quoted as saying that if web assembly existed in 2008 docker wouldn't have been needed now docker is much more mature and perhaps at this point [Music] you know locked into some decisions and use cases but people have found issues with attempting to run docker containers at edge on low resource devices web assembly has a few attributes that position it behind docker it's less mature it doesn't have the supporting landscape but it's also got these attributes that you can read on the slide that potentially position it ahead of docker for these edge use cases i'll tell you that i got in here at kubecon on saturday for the rejects conference and by my read the hallway track here has pretty much a third of the cool kids talking about web
