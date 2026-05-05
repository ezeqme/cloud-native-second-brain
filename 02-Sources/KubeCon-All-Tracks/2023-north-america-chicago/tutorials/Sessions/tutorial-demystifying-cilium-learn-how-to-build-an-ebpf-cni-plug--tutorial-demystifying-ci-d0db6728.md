---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Tutorials"
themes: ["Networking"]
speakers: ["Adam Sayah", "Solo.io"]
sched_url: https://kccncna2023.sched.com/event/1R2on/tutorial-demystifying-cilium-learn-how-to-build-an-ebpf-cni-plugin-from-scratch-adam-sayah-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Demystifying+Cilium%3A+Learn+How+to+Build+an+eBPF+CNI+Plugin+from+Scratch+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Demystifying Cilium: Learn How to Build an eBPF CNI Plugin from Scratch - Adam Sayah, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Adam Sayah, Solo.io
- Schedule: https://kccncna2023.sched.com/event/1R2on/tutorial-demystifying-cilium-learn-how-to-build-an-ebpf-cni-plugin-from-scratch-adam-sayah-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Demystifying+Cilium%3A+Learn+How+to+Build+an+eBPF+CNI+Plugin+from+Scratch+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Demystifying Cilium: Learn How to Build an eBPF CNI Plugin from Scratch.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2on/tutorial-demystifying-cilium-learn-how-to-build-an-ebpf-cni-plugin-from-scratch-adam-sayah-soloio
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Demystifying+Cilium%3A+Learn+How+to+Build+an+eBPF+CNI+Plugin+from+Scratch+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3cqCmtg-TOo
- YouTube title: Tutorial: Demystifying Cilium: Learn How to Build an eBPF CNI Plugin from Scratch - Adam Sayah
- Match score: 1.015
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-demystifying-cilium-learn-how-to-build-an-ebpf-cni-plugin-fro/3cqCmtg-TOo.txt
- Transcript chars: 66617
- Keywords: actually, basically, certain, create, container, traffic, network, packet, configuration, bridge, plugin, ebpf, couple, interface, define, source, created, address

### Resumo baseado na transcript

hey thank you guys for joining this session a technical session at 4M the afternoon I hope you guys are ready for that um how was the day today how's the talks and you guys awesome amazing all right so let me try to close it with like a good note I guess um today we're going to do a workshop on how to build an ebpf uh a cni plugin that uses abpf uh it's going to be a tutorial for about an hour and a half I'm going

### Excerpt da transcript

hey thank you guys for joining this session a technical session at 4M the afternoon I hope you guys are ready for that um how was the day today how's the talks and you guys awesome amazing all right so let me try to close it with like a good note I guess um today we're going to do a workshop on how to build an ebpf uh a cni plugin that uses abpf uh it's going to be a tutorial for about an hour and a half I'm going to try to make it actually shorter just for you guys to to rest a bit from this long day all right you guys ready amazing let's do it all right a bit by myself my name is Adam saiya I work at solo um in the past couple years I've been very focused on what we call application networking in general so I deal with API getways and service mesh every day and kind of the focus there is to secure the traffic and secure the network in general now thing I'm one thing I'm very much uh interested in these days is how can I do more and instead of operating at L7 on the layer seven where it's kind application uh layer I want to see how many policies and how much we can get from doing controlling the traffic way earlier on the network stack and that's basically where the cni and ABF operates right it's very much networking at a very low level so today um again we are going to do a cni APF Workshop up but we are not going to recreate San right we're not going to do something anything complicated I think the goal of this session is mainly um you know to solve this curiosity that everyone have right for example for me when I was a kid I always been asking my dad like hey how things work and he gave me like the the Quick Pitch right for example for us today is like opening a car and you know opening the hood and saying hey this is the engine and this is the battery and you know that's pretty much it as long if we can understand kind of the underlying mechanism being used in these Technologies like cium and other a big project that use EF then it's a good it's a good day all right all right so let's get started what we are going to do today couple things we're going to start with a small presentation around what's a cni okay a very few slides going on talking about the B Basics we're not going to Deep dive too much into it but at least just to get the main idea of how things work after that we are going to uh use our laptops I don't know if you guys are ready for that you guys can follow with me too uh to create our own first cni after that we're going to talk abou
