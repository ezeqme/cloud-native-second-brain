---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Tutorials"
themes: ["Observability", "Security", "Networking"]
speakers: ["Tracy P Holmes", "Duffie Cooley", "Isovalent"]
sched_url: https://kccnceu2023.sched.com/event/1HyZg/tutorial-getting-familiar-with-security-observability-using-ebpf-and-cilium-tetragon-tracy-p-holmes-duffie-cooley-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Getting+Familiar+with+Security+Observability+Using+eBPF+and+Cilium+Tetragon+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Getting Familiar with Security Observability Using eBPF and Cilium Tetragon - Tracy P Holmes & Duffie Cooley, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Tutorials]]
- Temas: [[Observability]], [[Security]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tracy P Holmes, Duffie Cooley, Isovalent
- Schedule: https://kccnceu2023.sched.com/event/1HyZg/tutorial-getting-familiar-with-security-observability-using-ebpf-and-cilium-tetragon-tracy-p-holmes-duffie-cooley-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Getting+Familiar+with+Security+Observability+Using+eBPF+and+Cilium+Tetragon+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Getting Familiar with Security Observability Using eBPF and Cilium Tetragon.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZg/tutorial-getting-familiar-with-security-observability-using-ebpf-and-cilium-tetragon-tracy-p-holmes-duffie-cooley-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Getting+Familiar+with+Security+Observability+Using+eBPF+and+Cilium+Tetragon+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kTGU-Nc2Db0
- YouTube title: Tutorial: Getting Familiar with Security Observability Using eBPF &Cilium Tetragon - Holmes & Cooley
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-getting-familiar-with-security-observability-using-ebpf-and-c/kTGU-Nc2Db0.txt
- Transcript chars: 60958
- Keywords: actually, tetragon, psyllium, kernel, ebpf, running, container, namespace, events, policy, cluster, process, context, tracing, network, inside, control, started

### Resumo baseado na transcript

good afternoon my name is Duffy Cooley I'm the field CTO at eye surveillance today we're going to be conducting a workshop on getting familiar with security observability using ebbf and psyllium tetricon I want to try using these ones and my name is Solutions architect and I'll be yeah doing it with you awesome so to get started I'm going to actually take you through a presentation kind of describing the concepts and the and what we're going to be covering in the lab today and then I'm going

### Excerpt da transcript

good afternoon my name is Duffy Cooley I'm the field CTO at eye surveillance today we're going to be conducting a workshop on getting familiar with security observability using ebbf and psyllium tetricon I want to try using these ones and my name is Solutions architect and I'll be yeah doing it with you awesome so to get started I'm going to actually take you through a presentation kind of describing the concepts and the and what we're going to be covering in the lab today and then I'm going to turn it over to Raphael to drive the lab but we're all going to be able to go through a Hands-On lab together so I hope you brought your laptops you should only need internet access nothing special we're going to be using the and we're going to be using instruct to host the labs and that's going to be how we go about that part of it so our agenda for today is uh psyllium and evpf introduction we're going to talk a little bit about like what we've been building at isabellent as part of the open source psyllium project we're going to talk a little bit about tetragon and then we're going to jump into like some examples here and then we're going to go into the lab so first the open source projects that we work on at ISO valence are psyllium and evpf we are actually have a lot of Kernel maintainers in working at isovalent directly working in ebpf in the kernel pretty exciting and isobalant is the company behind it we also provide a product that's called psyllium Enterprise I'm not going to spend a lot of time talking about that today but if you'd like to know more there's definitely a booth that we'll be happy to tell you all about it so ebpf is that how here has heard of ebpf I like seeing the number of hands go up higher and higher like every time you know it's great love to see it so evpf basically makes the Linux kernel programmable in a secure and efficient way and it's one of the analogs here is to say that it is like JavaScript in the browser but ebpf is to the kernel another way to think about this I'm probably drifting it out of the microphone and I'm sorry about that but I move around a lot when I talk but um another way to think about that is if you consider that's probably a good idea do you want to switch to this microphone please not hear me okay um another way to think about that is if you think about the Linux kernel as an API right and when I want to open a file when I want to open a socket whenever I want to do anything else like that I'm actually going
