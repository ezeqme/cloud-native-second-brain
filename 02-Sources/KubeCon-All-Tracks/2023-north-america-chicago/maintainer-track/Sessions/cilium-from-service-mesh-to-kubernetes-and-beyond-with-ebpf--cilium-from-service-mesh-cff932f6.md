---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["James McShane", "SuperOrbital", "Hemanth Malla", "Datadog", "Liz Rice", "Thomas Graf", "Isovalent"]
sched_url: https://kccncna2023.sched.com/event/1R2ux/cilium-from-service-mesh-to-kubernetes-and-beyond-with-ebpf-james-mcshane-superorbital-hemanth-malla-datadog-liz-rice-thomas-graf-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Cilium%3A+From+Service+Mesh+to+Kubernetes+and+Beyond+with+eBPF+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cilium: From Service Mesh to Kubernetes and Beyond with eBPF - James McShane, SuperOrbital; Hemanth Malla, Datadog; Liz Rice & Thomas Graf, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: James McShane, SuperOrbital, Hemanth Malla, Datadog, Liz Rice, Thomas Graf, Isovalent
- Schedule: https://kccncna2023.sched.com/event/1R2ux/cilium-from-service-mesh-to-kubernetes-and-beyond-with-ebpf-james-mcshane-superorbital-hemanth-malla-datadog-liz-rice-thomas-graf-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Cilium%3A+From+Service+Mesh+to+Kubernetes+and+Beyond+with+eBPF+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cilium: From Service Mesh to Kubernetes and Beyond with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ux/cilium-from-service-mesh-to-kubernetes-and-beyond-with-ebpf-james-mcshane-superorbital-hemanth-malla-datadog-liz-rice-thomas-graf-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Cilium%3A+From+Service+Mesh+to+Kubernetes+and+Beyond+with+eBPF+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xJ_Jiv7y6N0
- YouTube title: Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF - Panel
- Match score: 0.766
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cilium-from-service-mesh-to-kubernetes-and-beyond-with-ebpf/xJ_Jiv7y6N0.txt
- Transcript chars: 28819
- Keywords: celium, tetragon, actually, network, ebpf, networking, policies, security, cluster, kernel, number, technology, around, public, policy, maintainers, coming, observability

### Resumo baseado na transcript

uh welcome to the maintainers track session um I'm Bill Mulligan I work at isant and joining me on stage are ammed from New York Times Joe from Ascend and Anna also from isant uh thanks for coming today so just as a quick show of hands how many people in here use celium okay awesome that's great to see um and how many people have never heard of celium okay few hands to so hopefully this will be interesting for both groups so if you haven't heard of psyllium

### Excerpt da transcript

uh welcome to the maintainers track session um I'm Bill Mulligan I work at isant and joining me on stage are ammed from New York Times Joe from Ascend and Anna also from isant uh thanks for coming today so just as a quick show of hands how many people in here use celium okay awesome that's great to see um and how many people have never heard of celium okay few hands to so hopefully this will be interesting for both groups so if you haven't heard of psyllium before um psum began as a networking project uh providing layer three and layer four connectivity as a kubernetes cni uh once we kind of expanded beyond that we started to include network observability with the sub project Hubble and the project has expanded once again to also include security observability and runtime enforcement with tetragon so when you think about psyllium what it does is it provides Cloud native networking observability and security and all of this technology is built on top of ebpf and ebpf is a Linux kernel technology that allows you to flexibly and efficiently and safely modify what's happening in the Linux kernel and that's what makes the whole celium family of projects so powerful is being built on top of ebpf so a quick update from the project uh celium is now at 20,000 stars on GitHub I think that's pretty cool but this is actually a bit of a vanity metric you know all you have to do is like click the button there I think what's actually more exciting for me as one of the maintainers of the project is the contributors to the project so cncf just actually recently int uh released a San project Journey report and we can really see both the growth in the number of contributing companies and the number of contributors and really saying that companies all around the ecosystem are buying into and contributing to psyllium and this is really exciting for me because it means more contributions means we have a better project to give to all the people that are using it like you uh on top of that the velocity uh around celium is also increasing too so this is the number of authors the number of commits the number of PRS the number of issues that's increasing too so even though celium is almost 10 years old the energy the momentum behind the project is continuing to increase I think that's really exciting about the project too and besides just the contributors uh the important thing is all the end users who's used the project to and so right now pH celum uh if you go to the website right
