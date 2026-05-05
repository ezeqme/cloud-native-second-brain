---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["AI ML", "Observability", "Security", "Runtime Containers", "Kubernetes Core"]
speakers: ["Brandon Kang", "Akamai Technologies"]
sched_url: https://kccnceu2026.sched.com/event/2CW1N/hacking-gpu-observability-ebpf-ephemeral-containers-in-action-on-kubernetes-brandon-kang-akamai-technologies
youtube_search_url: https://www.youtube.com/results?search_query=Hacking+GPU+Observability%3A+eBPF+%26+Ephemeral+Containers+in+Action+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Hacking GPU Observability: eBPF & Ephemeral Containers in Action on Kubernetes - Brandon Kang, Akamai Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Observability]], [[Security]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Brandon Kang, Akamai Technologies
- Schedule: https://kccnceu2026.sched.com/event/2CW1N/hacking-gpu-observability-ebpf-ephemeral-containers-in-action-on-kubernetes-brandon-kang-akamai-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=Hacking+GPU+Observability%3A+eBPF+%26+Ephemeral+Containers+in+Action+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Hacking GPU Observability: eBPF & Ephemeral Containers in Action on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1N/hacking-gpu-observability-ebpf-ephemeral-containers-in-action-on-kubernetes-brandon-kang-akamai-technologies
- YouTube search: https://www.youtube.com/results?search_query=Hacking+GPU+Observability%3A+eBPF+%26+Ephemeral+Containers+in+Action+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mkH38O3wLog
- YouTube title: Hacking GPU Observability: eBPF & Ephemeral Containers in Action on Kubernetes - Brandon Kang
- Match score: 1.0
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/hacking-gpu-observability-ebpf-ephemeral-containers-in-action-on-kuber/mkH38O3wLog.txt
- Transcript chars: 21602
- Keywords: gpu, ebpf, kernel, source, security, metrics, observability, monitoring, happening, hardware, application, another, running, memory, performance, runtime, cluster, visibility

### Resumo baseado na transcript

So, today I want to talk about a simple question regarding the GPU monitoring. So, in this talk, I will show you and how we use eBPF and ephemeral containers to understand and debug GPU workload without any breaking production. So, I would say that the the traditional GPU monitoring tools, they just show hardware metrics, and then they let you know that something happens, but you cannot find any root causes. It gives you a wider range of hardware level metrics including GPU utilization, which is very crucial for your GPU cost optimization. So, because the most performance problems we cannot see the real the reason of why this happens from using this tool. So, another case, if we break down a typical element AI inference stacks, we can use we can see where the problem is hiding.

### Excerpt da transcript

Okay, thank you. Thank you for coming. My name is Brandon. I'm from Akamai. So, today I want to talk about a simple question regarding the GPU monitoring. So, how do we observe the GPU workload in Kubernetes? And I will talk about how do we debug them safely in production. So, GPUs don't fail like CPU. So, they fail very silently. And they often fail at the worst time. So, in this talk, I will show you and how we use eBPF and ephemeral containers to understand and debug GPU workload without any breaking production. So, if you ever worked with the GPU workload, you've probably seen that some strange behavior that the GPU Sometimes you hit out of memory. And sometimes the performance suddenly drops. And sometimes the things just slow down without any evidences. So, if you see the the left picture, CPU workloads can be predictable. But the but but the in the the right corner, the GPU workload I would say it's a kind of the alien landscape. So, CPU workloads are very different from CPUs. So, we have many issues like the thermal throttling from the GPU or the kernel stores.

And they don't always show clearly. So, they just reduce the performance quietly. And that's the real problem. So, we often don't notice anything is wrong. So, that's why I designed this presentation and this session for the GPU observability using the eBPF. So, some naturally we turn to tools like the DCGM, NVIDIA DCGM, or NVIDIA-SMI to see what what are happening right now from my GPU. They give us some metrics like the GPU utilization, temperature, and memory usage. And at the first glance, they seems very useful. But then when you run into a situation like um you have the same GPU running the same model, but one this instance is running at 80% GPU utilization, but another is a stuck at 20% only. And the tools don't tell you why. So, I would say that the the traditional GPU monitoring tools, they just show hardware metrics, and then they let you know that something happens, but you cannot find any root causes. So, this is what I call the visibility illusion. So, I think that we can see what's going on um if we using the eBPF and then all the best tools with some algorithms.

So, let's talk about the DCGM first. Actually, it means the data center GPU monitor. But not only data center, but also your the GPU instances on the cloud, your DGX on frame basic GPU machine that you can install this open source, and then you can utilize this for very basic level of the GPU monitoring. So, it is ac
