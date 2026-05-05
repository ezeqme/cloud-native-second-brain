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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Gulcan Topcu", "Daniele Polencic", "LearnKube"]
sched_url: https://kccnceu2026.sched.com/event/2CW1Q/gpus-on-kubernetes-what-actually-happens-when-you-request-nvidiacomgpu-1-gulcan-topcu-daniele-polencic-learnkube
youtube_search_url: https://www.youtube.com/results?search_query=GPUs+on+Kubernetes%3A+What+Actually+Happens+When+You+Request+Nvidia.com%2Fgpu%3A+1+CNCF+KubeCon+2026
slides: []
status: parsed
---

# GPUs on Kubernetes: What Actually Happens When You Request Nvidia.com/gpu: 1 - Gulcan Topcu & Daniele Polencic, LearnKube

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Gulcan Topcu, Daniele Polencic, LearnKube
- Schedule: https://kccnceu2026.sched.com/event/2CW1Q/gpus-on-kubernetes-what-actually-happens-when-you-request-nvidiacomgpu-1-gulcan-topcu-daniele-polencic-learnkube
- Busca YouTube: https://www.youtube.com/results?search_query=GPUs+on+Kubernetes%3A+What+Actually+Happens+When+You+Request+Nvidia.com%2Fgpu%3A+1+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre GPUs on Kubernetes: What Actually Happens When You Request Nvidia.com/gpu: 1.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1Q/gpus-on-kubernetes-what-actually-happens-when-you-request-nvidiacomgpu-1-gulcan-topcu-daniele-polencic-learnkube
- YouTube search: https://www.youtube.com/results?search_query=GPUs+on+Kubernetes%3A+What+Actually+Happens+When+You+Request+Nvidia.com%2Fgpu%3A+1+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nu6bLhuvlWM
- YouTube title: GPUs on Kubernetes: What Actually Happens When You Request Nvidia... Gulcan Topcu & Daniele Polencic
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/gpus-on-kubernetes-what-actually-happens-when-you-request-nvidia-com-g/nu6bLhuvlWM.txt
- Transcript chars: 21236
- Keywords: gpu, basically, kernel, actually, memory, driver, container, running, inside, process, hardware, create, context, happens, interface, control, snorts, instead

### Resumo baseado na transcript

One of the one on on the basics of GPUs and how they work and why they are so difficult in Kubernetes and another on optimizations for yield in GPUs. So today we're going to take a sort of a look at both of them perhaps a little bit more about the the basics of of GPUs. And this design choice comes with some consequences that we will talk about in a second. >> [applause] >> We look at the hardware or how GPU works, but how does this translate to what we do in Kubernetes, right? And then to look at this, we need to basically have a um go back and sort of understand what is the life cycle of uh of of creating a pod in Kubernetes. The container runtime interface, container network interface, and the container storage interface.

### Excerpt da transcript

Thank you very much for joining. Hopefully you starting starting the day with GPUs. That's a very very tough day, I guess. So welcome welcome everybody. So my name is Daniele. I'm one of the instructors at learn Q. Um and with me today I've got Gutcha. Um we're going to talk about GPUs. So we wrote two books. One of the one on on the basics of GPUs and how they work and why they are so difficult in Kubernetes and another on optimizations for yield in GPUs. Again in in Kubernetes. So today we're going to take a sort of a look at both of them perhaps a little bit more about the the basics of of GPUs. We're going to see how those actually plug into Kubernetes, why they are so difficult to manage. Um and and and you know the challenges you might face with with this kind of hardware. Okay. Without further ado >> [laughter] >> Thank you for the introduction then. Thank you everyone for um joining us today. I'm really excited um to be sharing the stage with Dan. Meeting my team for the first time and having you all in this room today.

Okay. So to get to the good stuff actually we need to start from the bottom like way before Kubernetes even enters the picture. This begs the question and this is how does Linux run things? So when you write an app it needs to do things like reading a file, sending a network packet but it has no idea what the hardware what hardware is actually there. Is it an SSD, a spinning disk? It doesn't know and it doesn't care. Instead it just talks to the Linux kernel and the kernel figures out the rest. So we call this interface between your app and the kernel as system calls. Everything your app does goes through the system calls through the Linux kernel and to reach the actual hardware. If it wants to open a network connection still the same. There are no shortcuts and the kernel map is massive like there are hundreds of system calls. So naturally people started asking if everything passes through here can we actually do something with that? Like can we group processes together or limit how much resources they use?

Turns out yes and that's exactly what control groups are. You can think of them like rate limiting on an HTTP API except instead of limiting the calls the number of calls we are limiting [snorts] how much resource like memory, CPU, network bandwidth we use. And we can create as many C groups as we want each with different processes and different limits. But C groups get us halfway there because containers need something else t
