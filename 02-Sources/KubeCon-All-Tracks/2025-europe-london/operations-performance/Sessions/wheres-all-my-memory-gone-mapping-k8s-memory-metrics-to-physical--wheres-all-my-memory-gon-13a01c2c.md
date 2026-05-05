---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["Observability", "SRE Reliability"]
speakers: ["Mahé Tardy", "Isovalent at Cisco"]
sched_url: https://kccnceu2025.sched.com/event/1tx8C/wheres-all-my-memory-gone-mapping-k8s-memory-metrics-to-physical-resources-mahe-tardy-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Where%E2%80%99s+All+My+Memory+Gone%3F+Mapping+K8s+Memory+Metrics+To+Physical+Resources+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Where’s All My Memory Gone? Mapping K8s Memory Metrics To Physical Resources - Mahé Tardy, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Mahé Tardy, Isovalent at Cisco
- Schedule: https://kccnceu2025.sched.com/event/1tx8C/wheres-all-my-memory-gone-mapping-k8s-memory-metrics-to-physical-resources-mahe-tardy-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Where%E2%80%99s+All+My+Memory+Gone%3F+Mapping+K8s+Memory+Metrics+To+Physical+Resources+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Where’s All My Memory Gone? Mapping K8s Memory Metrics To Physical Resources.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8C/wheres-all-my-memory-gone-mapping-k8s-memory-metrics-to-physical-resources-mahe-tardy-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Where%E2%80%99s+All+My+Memory+Gone%3F+Mapping+K8s+Memory+Metrics+To+Physical+Resources+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zLHdgl2qxbg
- YouTube title: Where’s All My Memory Gone? Mapping K8s Memory Metrics To Physical Resources - Mahé Tardy
- Match score: 1.017
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/wheres-all-my-memory-gone-mapping-k8s-memory-metrics-to-physical-resou/zLHdgl2qxbg.txt
- Transcript chars: 25495
- Keywords: memory, process, container, actually, running, physical, advisor, metrics, kernel, containers, cluster, cublet, croups, inactive, working, thingy, concept, object

### Resumo baseado na transcript

So today we are going to talk about memory and with uh where all my memory is gone. So today we are trying to map the Kubernetes memory matrix to actual physical resource. So let's try to understand where this metrics come from and how it's it's built. I I I think I could be uh fairly right to say that the main memory metrics that is tracked in the communities world for pods is container memory working set byes. In the documentation on the website you can see a bunch of uh um descript description of like the resource metrics pipeline and these kind of things. But one uh good idea is was to look at the Prometheus dashboard itself.

### Excerpt da transcript

All right, welcome everyone. Thank you for joining Marty talk. So today we are going to talk about memory and with uh where all my memory is gone. So today we are trying to map the Kubernetes memory matrix to actual physical resource. I hope you you will learn something. So um I'm I'm May. I'm working as a software engineer at isalent at Cisco. Um I'm working on tetragonon which is an ebpf based runtime security project. It's and it's part of selium and this is not a picture of me. So it it it all started with something like that for me. So um a memory dashboard. So uh you might end up in the same situation and um I was quite confused that like uh what was the number I was actually looking at. So here you have like an application running a bunch of pods of this application in your cluster and they are like consuming an amount of memory but what is this memory about and how can I actually understand what is this about so if you are checking the uh this this dashboard in particular you might see something like this and in your case it might be the same.

So the memory metric that is actually used behind the scene is this thing called uh container memory working set bite. So it's it's a pretty long name and um for me it wasn't very clear what it was about. So let's try to understand where this metrics come from and how it's it's built. So this is the first conclusion very early conclusion. I I I think I could be uh fairly right to say that the main memory metrics that is tracked in the communities world for pods is container memory working set byes. So uh the thing I wanted to do next is trying to understand where it comes from. So um the one one idea was just to read the documentation. In the documentation on the website you can see a bunch of uh um descript description of like the resource metrics pipeline and these kind of things. But one uh good idea is was to look at the Prometheus dashboard itself. So I just wanted to show you how it works. um because primitives might be running uh as part of your cluster you can just like port forward the service the primitive server and then you will have access to the dashboard so I'll try to zoom in and from the dashboard you can see uh a bunch of information and among is like the target elf and uh here you can see that promeuse is scrapping a various number of endpoints uh here you have like the API server the nodes and a bunch of uh service endpoints So by gathering all this information plus uh a very nice blog po
