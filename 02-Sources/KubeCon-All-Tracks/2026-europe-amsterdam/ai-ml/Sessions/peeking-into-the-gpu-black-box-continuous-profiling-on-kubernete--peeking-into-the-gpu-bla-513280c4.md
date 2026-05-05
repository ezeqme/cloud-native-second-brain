---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Observability", "Kubernetes Core"]
speakers: ["Zahari Dichev", "Buoyant"]
sched_url: https://kccnceu2026.sched.com/event/2CW3J/peeking-into-the-gpu-black-box-continuous-profiling-on-kubernetes-with-ebpf-zahari-dichev-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Peeking+Into+the+GPU+Black+Box%3A+Continuous+Profiling+on+Kubernetes+With+eBPF+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Zahari Dichev, Buoyant
- Schedule: https://kccnceu2026.sched.com/event/2CW3J/peeking-into-the-gpu-black-box-continuous-profiling-on-kubernetes-with-ebpf-zahari-dichev-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Peeking+Into+the+GPU+Black+Box%3A+Continuous+Profiling+on+Kubernetes+With+eBPF+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3J/peeking-into-the-gpu-black-box-continuous-profiling-on-kubernetes-with-ebpf-zahari-dichev-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Peeking+Into+the+GPU+Black+Box%3A+Continuous+Profiling+on+Kubernetes+With+eBPF+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J61kV92bSt0
- YouTube title: Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev
- Match score: 0.995
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/peeking-into-the-gpu-black-box-continuous-profiling-on-kubernetes-with/J61kV92bSt0.txt
- Transcript chars: 22358
- Keywords: gpu, metrics, actually, device, essentially, hardware, kernel, ebpf, looking, demand, happening, process, pressure, observability, workloads, functions, another, memory

### Resumo baseado na transcript

Good afternoon everyone and uh welcome to my talk titled peeking into the GPU blackbox. So quick intro right my name is Zahari and I work uh for buoyant as a software engineer where I work on the linkd service mesh. You scale that to a node of eight of these devices and you're suddenly looking at more than $30 an hour. A cluster consisting of eight nodes would then cost you more than $250. You scale that to a day and all of a sudden your cluster costs more than $6,000. All of these great tools that can give you a lot of details about how your processes interact with the underlying hardware and to diagnose any problems.

### Excerpt da transcript

Good afternoon everyone and uh welcome to my talk titled peeking into the GPU blackbox. So quick intro right my name is Zahari and I work uh for buoyant as a software engineer where I work on the linkd service mesh. Um now today we're not going to be talking about service meshes or networking. We're going to be talking about GPUs and how we can use ebpf in order to profile the interactions between our applications and the GPU devices uh on Kubernetes clusters. So here is the plan. We are going to first look um at why GPU introspection is important in Kubernetes and specifically why it's important in this DNA day day and age. We're going to do a quick overview of the existing tools and approaches of how we can gain observability into GPUs and Kubernetes and we'll see what they are good for and where they actually fall short. Then after that we're going to try and see how ebpf can help with uh all of that and to what degree. And then we're going to propose a simple monitoring framework that consists just of a handful of highle metrics that can help us gain more insight into what workloads are doing with the GPU in our clusters.

And then we'll substitute that with a couple of concrete example of of incidents and see how we can uh how how this framework can help diagnose them and hopefully at the end we have some time for some easy questions. So first of all a couple of uncomfortable truths. We are actually living in a GPU gold rush at the moment. There are cases where uh cloud providers have weight lists for GPU hardware. Teams across companies are hoarding their GPU budgets because uh it's really hard to get your hands on these expensive pieces of hardware. Why is this the case? Well, it's very simple. A single H100 costs nearly $4 an hour on a major cloud provider. You scale that to a node of eight of these devices and you're suddenly looking at more than $30 an hour. A cluster consisting of eight nodes would then cost you more than $250. And that's just for an hour. You scale that to a day and all of a sudden your cluster costs more than $6,000. That's a figure. But for a month, you'd have to pay more than $126,000. And you know, this is just compute alone.

You don't factor in traffic and storage costs into that. So this is all getting worse as teams grow and projects fill in the pipeline, right? So the question comes when you're paying all of that money, what kind of observability do you get into what's happening with these incredibly expensive devices?
