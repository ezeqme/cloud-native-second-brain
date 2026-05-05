---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Thomas Graf", "Isovalent"]
sched_url: https://kccnceu2023.sched.com/event/1HydA/surviving-day-2-how-to-troubleshoot-kubernetes-networking-thomas-graf-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Surviving+Day+2+-+How+to+Troubleshoot+Kubernetes+Networking+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Surviving Day 2 - How to Troubleshoot Kubernetes Networking - Thomas Graf, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Thomas Graf, Isovalent
- Schedule: https://kccnceu2023.sched.com/event/1HydA/surviving-day-2-how-to-troubleshoot-kubernetes-networking-thomas-graf-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Surviving+Day+2+-+How+to+Troubleshoot+Kubernetes+Networking+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Surviving Day 2 - How to Troubleshoot Kubernetes Networking.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HydA/surviving-day-2-how-to-troubleshoot-kubernetes-networking-thomas-graf-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Surviving+Day+2+-+How+to+Troubleshoot+Kubernetes+Networking+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=920BZXvQpVs
- YouTube title: Surviving Day 2 - How to Troubleshoot Kubernetes Networking - Thomas Graf, Isovalent
- Match score: 0.918
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/surviving-day-2-how-to-troubleshoot-kubernetes-networking/920BZXvQpVs.txt
- Transcript chars: 41954
- Keywords: actually, psyllium, network, policy, running, hubble, application, observability, cluster, latency, networking, simple, namespace, calico, implementation, available, course, understand

### Resumo baseado na transcript

hello kubecon for this last day and Friday my name is Thomas I'm one of the creators and maintainers of psyllium and psyllium is one of the popular kubernetes networking implementations and based on what we have learned creating psyllium and working with many of you I would like to share how to survive day two and how to troubleshoot kubernetes networking so a bit of context I'm one of the maintainers of psyllium so what I'm sharing today of course has a bit of psyllium context because I've been

### Excerpt da transcript

hello kubecon for this last day and Friday my name is Thomas I'm one of the creators and maintainers of psyllium and psyllium is one of the popular kubernetes networking implementations and based on what we have learned creating psyllium and working with many of you I would like to share how to survive day two and how to troubleshoot kubernetes networking so a bit of context I'm one of the maintainers of psyllium so what I'm sharing today of course has a bit of psyllium context because I've been mostly working with psyllium the past few years but the exercises or the best practices and how to approach this is of course not at all specific to cilia and can be applied regardless of what kubernetes networking implementation you are using for those who have never heard about psyllium psyllium is a cni plugin among other things it is a cncf project at incubation stage but cylinder does not only provide networking or cni functionality which is what we will focus on today it also provides service mesh and hobble and a lot of what we will hear about today is made possible by Hubble or tools Cinema to hobble hobble is the observability layer of psyllium then we also have in the sodium family tetragon which is providing runtime security and security observability all aspects of psyllium are being done using a technology called evpf and that's actually what's enabling a lot of the observability that we will see today which will assist you in troubleshooting for some in particular in the last part of the talk we'll also look at layer 7 latency or HTTP latency some of that work is done through Envoy the envoy proxy which is also a cncf project so let's jump into kubernetes networking or how some people call it the Dark Side of kubernetes how many of you are familiar with the Core Concepts of kubernetes networking excellent almost everybody so this will probably be a repetition for for most of you but if you've never heard about or have never seen how kubernetes networking works this may help you understand the rest of this talk first of all kubernetes networking is very simple and basic all parts have an IP address which means every individual part has an IP address they can directly talk to each other there is no specific Network topology required kubernetes makes a simple assumption that we have a flat so-called flat layer 3 Network port side if I have IPS and thus Parts can talk to each other this is sometimes implemented differently depending on whether you're runn
