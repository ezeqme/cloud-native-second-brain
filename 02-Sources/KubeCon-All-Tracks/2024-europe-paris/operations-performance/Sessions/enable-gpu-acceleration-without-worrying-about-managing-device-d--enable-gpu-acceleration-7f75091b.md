---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Christopher Desiniotis", "NVIDIA"]
sched_url: https://kccnceu2024.sched.com/event/1YePS/enable-gpu-acceleration-without-worrying-about-managing-device-drivers-christopher-desiniotis-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Enable+GPU-Acceleration+Without+Worrying+About+Managing+Device+Drivers+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Enable GPU-Acceleration Without Worrying About Managing Device Drivers - Christopher Desiniotis, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Christopher Desiniotis, NVIDIA
- Schedule: https://kccnceu2024.sched.com/event/1YePS/enable-gpu-acceleration-without-worrying-about-managing-device-drivers-christopher-desiniotis-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Enable+GPU-Acceleration+Without+Worrying+About+Managing+Device+Drivers+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Enable GPU-Acceleration Without Worrying About Managing Device Drivers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePS/enable-gpu-acceleration-without-worrying-about-managing-device-drivers-christopher-desiniotis-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Enable+GPU-Acceleration+Without+Worrying+About+Managing+Device+Drivers+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zYZ0zXWDH00
- YouTube title: Enable GPU-Acceleration Without Worrying About Managing Device Drivers - Christopher Desiniotis
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/enable-gpu-acceleration-without-worrying-about-managing-device-drivers/zYZ0zXWDH00.txt
- Transcript chars: 35043
- Keywords: driver, drivers, upgrade, gpu, kernel, container, nvidia, running, operator, device, cluster, actually, controller, deploy, upgrades, version, install, already

### Resumo baseado na transcript

I think I'm going to get started so um hi everyone thanks for joining um me today welcome to my session uh enable uh GPU acceleration without worrying about managing device drivers I know it's a mouthful sorry about that uh my name is Chris deso I work at um as a software engineer at Nvidia uh I work on our Cloud native team uh we work on enabling gpus and containers and kubernetes so in this talk I'm going to be strictly discussing Linux device drivers right I'll give

### Excerpt da transcript

I think I'm going to get started so um hi everyone thanks for joining um me today welcome to my session uh enable uh GPU acceleration without worrying about managing device drivers I know it's a mouthful sorry about that uh my name is Chris deso I work at um as a software engineer at Nvidia uh I work on our Cloud native team uh we work on enabling gpus and containers and kubernetes so in this talk I'm going to be strictly discussing Linux device drivers right I'll give a quick definition of what I mean by a device driver and what are some methods for installing them in kubernetes today or typical methods for installing them um I'll Focus the latter half of my talk on some of the day two challenges with managing drivers especially with a larger cluster um I'll present some solutions we've built especially for for NVIDIA gpus um and then I'll end with a demo so what is a device driver we'll simply put a a driver abstracts a piece of Hardware right on a Linux system typically it's a kernel space component which is a loadable kernel module that you build uh against your kernel and have to recompile on on kernel updates um and then you also have along with it some user space driver libraries that provide abstractions in user space right and so these are usually versioned together and you need both of these to to leverage uh your device or accelerator so for my talk when I say device driver I mean both the user space uh libraries Shar libraries and the the kernel module so what are some if we were to install drivers and on your local system you would just you know either build from Source or for your respected distribution go to your package manager and install a package right invid a driver package um but you can't do that in kubernetes we need to install this on lots of machines so what are some strategies uh the first you can use SSH right so you can use some common tool or some familiar familiar tools like ansible or puppet um have a common recipe and go one by one on your nodes and install drivers right directly on the host uh this is simple it's maybe familiar to your team or tooling that's familiar to your team but obviously we're not using kubernetes to manage our drivers so I'm not going to focus on the for the rest of my talk right you need separate tooling you need to maintain it um and you know separate tooling for monitoring and logging right your your your drivers second approach is to build your own operating system image for your GPU work ER node
