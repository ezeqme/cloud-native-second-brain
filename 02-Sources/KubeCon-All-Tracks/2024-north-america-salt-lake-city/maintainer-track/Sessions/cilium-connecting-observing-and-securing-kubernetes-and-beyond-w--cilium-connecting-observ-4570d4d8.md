---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Kubernetes Core", "Community Governance"]
speakers: ["Ahmed Bebars", "The New York Times", "Joe Stevens", "Ascend.io", "Bill Mulligan", "Anna Kapuscinska", "Isovalent at Cisco"]
sched_url: https://kccncna2024.sched.com/event/1howZ/cilium-connecting-observing-and-securing-kubernetes-and-beyond-with-ebpf-ahmed-bebars-the-new-york-times-joe-stevens-ascendio-bill-mulligan-anna-kapuscinska-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Cilium%3A+Connecting%2C+Observing%2C+and+Securing+Kubernetes+and+Beyond+with+eBPF+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF - Ahmed Bebars, The New York Times; Joe Stevens, Ascend.io; Bill Mulligan & Anna Kapuscinska, Isovalent at Cisco;

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Ahmed Bebars, The New York Times, Joe Stevens, Ascend.io, Bill Mulligan, Anna Kapuscinska, Isovalent at Cisco
- Schedule: https://kccncna2024.sched.com/event/1howZ/cilium-connecting-observing-and-securing-kubernetes-and-beyond-with-ebpf-ahmed-bebars-the-new-york-times-joe-stevens-ascendio-bill-mulligan-anna-kapuscinska-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Cilium%3A+Connecting%2C+Observing%2C+and+Securing+Kubernetes+and+Beyond+with+eBPF+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howZ/cilium-connecting-observing-and-securing-kubernetes-and-beyond-with-ebpf-ahmed-bebars-the-new-york-times-joe-stevens-ascendio-bill-mulligan-anna-kapuscinska-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Cilium%3A+Connecting%2C+Observing%2C+and+Securing+Kubernetes+and+Beyond+with+eBPF+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xJ_Jiv7y6N0
- YouTube title: Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF - Panel
- Match score: 1.04
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cilium-connecting-observing-and-securing-kubernetes-and-beyond-with-eb/xJ_Jiv7y6N0.txt
- Transcript chars: 28819
- Keywords: celium, tetragon, actually, network, ebpf, networking, policies, security, cluster, kernel, number, technology, around, public, policy, maintainers, coming, observability

### Resumo baseado na transcript

uh welcome to the maintainers track session um I'm Bill Mulligan I work at isant and joining me on stage are ammed from New York Times Joe from Ascend and Anna also from isant uh thanks for coming today so just as a quick show of hands how many people in here use celium okay awesome that's great to see um and how many people have never heard of celium okay few hands to so hopefully this will be interesting for both groups so if you haven't heard of psyllium

### Excerpt da transcript

uh welcome to the maintainers track session um I'm Bill Mulligan I work at isant and joining me on stage are ammed from New York Times Joe from Ascend and Anna also from isant uh thanks for coming today so just as a quick show of hands how many people in here use celium okay awesome that's great to see um and how many people have never heard of celium okay few hands to so hopefully this will be interesting for both groups so if you haven't heard of psyllium before um psum began as a networking project uh providing layer three and layer four connectivity as a kubernetes cni uh once we kind of expanded beyond that we started to include network observability with the sub project Hubble and the project has expanded once again to also include security observability and runtime enforcement with tetragon so when you think about psyllium what it does is it provides Cloud native networking observability and security and all of this technology is built on top of ebpf and ebpf is a Linux kernel technology that allows you to flexibly and efficiently and safely modify what's happening in the Linux kernel and that's what makes the whole celium family of projects so powerful is being built on top of ebpf so a quick update from the project uh celium is now at 20,000 stars on GitHub I think that's pretty cool but this is actually a bit of a vanity metric you know all you have to do is like click the button there I think what's actually more exciting for me as one of the maintainers of the project is the contributors to the project so cncf just actually recently int uh released a San project Journey report and we can really see both the growth in the number of contributing companies and the number of contributors and really saying that companies all around the ecosystem are buying into and contributing to psyllium and this is really exciting for me because it means more contributions means we have a better project to give to all the people that are using it like you uh on top of that the velocity uh around celium is also increasing too so this is the number of authors the number of commits the number of PRS the number of issues that's increasing too so even though celium is almost 10 years old the energy the momentum behind the project is continuing to increase I think that's really exciting about the project too and besides just the contributors uh the important thing is all the end users who's used the project to and so right now pH celum uh if you go to the website right
