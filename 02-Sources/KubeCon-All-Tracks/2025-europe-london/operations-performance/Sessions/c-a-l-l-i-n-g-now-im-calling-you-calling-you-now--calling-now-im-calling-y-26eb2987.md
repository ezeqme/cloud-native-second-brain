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
themes: ["SRE Reliability"]
speakers: ["Mario Macías", "Terra Tauri", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1txDH/calling-now-im-calling-you-calling-you-now-mario-macias-terra-tauri-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=C.A.L.L.I.N.G.+Now+I%27m+Calling+You%2C+Calling+You+Now+CNCF+KubeCon+2025
slides: []
status: parsed
---

# C.A.L.L.I.N.G. Now I'm Calling You, Calling You Now - Mario Macías & Terra Tauri, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Mario Macías, Terra Tauri, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1txDH/calling-now-im-calling-you-calling-you-now-mario-macias-terra-tauri-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=C.A.L.L.I.N.G.+Now+I%27m+Calling+You%2C+Calling+You+Now+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre C.A.L.L.I.N.G. Now I'm Calling You, Calling You Now.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txDH/calling-now-im-calling-you-calling-you-now-mario-macias-terra-tauri-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=C.A.L.L.I.N.G.+Now+I%27m+Calling+You%2C+Calling+You+Now+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2BIhTXQd0CI
- YouTube title: C.A.L.L.I.N.G. Now I'm Calling You, Calling You Now - Mario Macías & Terra Tauri, Grafana Labs
- Match score: 0.796
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/c-a-l-l-i-n-g-now-im-calling-you-calling-you-now/2BIhTXQd0CI.txt
- Transcript chars: 17862
- Keywords: metadata, information, kernel, metrics, cluster, ebpf, everything, instance, requests, network, request, source, snapshot, utilization, calling, connect, deployed, destination

### Resumo baseado na transcript

Uh, and thank you so much to the organizers for putting on this incredible conference. And if you're not lucky enough to be a '9s pop fan, that is a lyric from a song from Aqua's debut album, Aquarium, where the song is about a lover who's trying to connect with their love, and they're trying to call and they're just getting a busy signal. Um, but kernel data by itself, especially in Kubernetes, is really not that useful. And especially when you're doing this at scale across an entire fleet of machines, it gets very tedious. And in in Kubernetes, every single node in a standard deployment has its own kernel. In Kubernetes, we care about Kubernetes objects like services and pods, nodes.

### Excerpt da transcript

Hello everyone, welcome. Thank you so much for coming. Uh, and thank you so much to the organizers for putting on this incredible conference. I hope everyone has enjoyed themselves. Um, today our talk is called C A L L I N G. Now I'm calling you calling you now. And if you're not lucky enough to be a '9s pop fan, that is a lyric from a song from Aqua's debut album, Aquarium, where the song is about a lover who's trying to connect with their love, and they're trying to call and they're just getting a busy signal. So, they're calling to an operator and saying, "Hey, can you please connect me?" Um, today we're going to tell a story about some pods running in Kubernetes that were crushing a little too hard on the Kubernetes API. Um, I'm Terara Tori. I'm a staff software engineer at Grafana Labs and I'm joined today by my co-presenter Mario Matias. Uh, also staff software engineer at Graphfana Labs. So today you're going to learn a little bit about EVPF. We're just going to go into the basics of eBPF. If you want to know more and the nitty-gritty details, Mario has a talk just after this in this auditorium that you should definitely come and check out.

Uh we're going to talk about how in in enriching Kuberneting eBPF data, we broke the Kubernetes API. Uh how we uh why we needed to enrich that data and what we do to to to do that in BA and then how we ended up scaling that uh enrichment process. So uh oh uh before I go on uh can I get a show of hands? Who here is familiar with EVPF? Okay, so about half the people. Um who has written an ebpf program? Okay, fewer hands. And who has deployed that ebpf program into production in Kubernetes? Okay, awesome. Thank you. Um so before I go on I need to set the stage and start and tell you a little bit about ebpf. So ebpf if you don't know it enables safe and efficient extension of the Linux kernel. Now you might say we already have kernel modules. Why do we need ebpf? Well if you've ever run a kernel module you know that if the kernel module crashes crashes the whole system. Everything goes down. Um what ebpf does is it introduces a virtual machine the ebpf virtual machine and that enforces uh halting as well as a few other safety properties that enables you to run these kernel modu these kernel extensions in a safe way.

Um now the for I think a lot of people when they think of ebpf they think it's sort of a a new fangled technology. Um, but actually the stuff that we're talking about was added to the Linux kernel in 20
