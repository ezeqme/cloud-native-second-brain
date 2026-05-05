---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core"]
speakers: ["James Sturtevant", "Mark Rossetti", "Microsoft"]
sched_url: https://kccncna2022.sched.com/event/182Fe/windows-hostprocess-containers-for-configuration-and-beyond-james-sturtevant-mark-rossetti-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Windows+HostProcess+Containers+For+Configuration+And+Beyond+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Windows HostProcess Containers For Configuration And Beyond - James Sturtevant & Mark Rossetti, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: James Sturtevant, Mark Rossetti, Microsoft
- Schedule: https://kccncna2022.sched.com/event/182Fe/windows-hostprocess-containers-for-configuration-and-beyond-james-sturtevant-mark-rossetti-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Windows+HostProcess+Containers+For+Configuration+And+Beyond+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Windows HostProcess Containers For Configuration And Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fe/windows-hostprocess-containers-for-configuration-and-beyond-james-sturtevant-mark-rossetti-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Windows+HostProcess+Containers+For+Configuration+And+Beyond+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LcXT9pVkwvo
- YouTube title: Windows HostProcess Containers For Configuration And Beyond - James Sturtevant & Mark Rossetti
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/windows-hostprocess-containers-for-configuration-and-beyond/LcXT9pVkwvo.txt
- Transcript chars: 30371
- Keywords: windows, containers, access, container, process, running, security, networking, feature, inside, logs, server, network, config, around, cluster, information, interested

### Resumo baseado na transcript

all right welcome can you hear me great uh So today we're going to talk about Windows containers and uh host process containers for configuration and Beyond and so before we get too deep into the details of how Windows containers host process containers work we're going to show you a quick demo get right into it and show you how this works who here has used Windows containers before all right and who has had to debug and get onto the node like SSH or RDP onto the node there and make a pretty significant contribution that enables the ecosystem oh yeah so this this feature and all of the like the things that we've demoed here were really developed in conjunction with Sig windows so we wanted to take a minute to highlight some other upcoming talks related to Sig Windows um there's a Windows operational Readiness talk tomorrow there's a Sig Windows maintainer track talk tomorrow and then there's a interesting Lessons Learned From scheduling 20 million Windows containers in a month talk on Friday so if

### Excerpt da transcript

all right welcome can you hear me great uh So today we're going to talk about Windows containers and uh host process containers for configuration and Beyond and so before we get too deep into the details of how Windows containers host process containers work we're going to show you a quick demo get right into it and show you how this works who here has used Windows containers before all right and who has had to debug and get onto the node like SSH or RDP onto the node all right so only one or two folks but you know how painful that is and so for everybody else SSH sshing into the node usually requires doing a proxy jump or already like setting up a VM inside the network so you can RDP then you need to know that the password to that VM and it's difficult challenging and so what I'm going to show you here today is uh we're gonna use a cube CTL plugin to connect to the node and get direct access to the node no SSH no um no passwords none of that and so we're going to get just easy access and so in the demo things to look for are how fast this container boots up and um and the tools we get to use such as vim and other things so I'm going to start the demo here first thing we're going to do is take a quick look at the the nodes so you're going to see a Linux node and a Windows node and then we're going to install the plugin so we're going to use crew to do that crew install Windows debug uh crew if you have not familiar with crew it installs a plug-in so you can start to use that tool directly with cubectl next I'm going to run Cube CTL Windows debug and it's so fast that I can barely say it we just got connected to the windows node and we have access to the root file system there and we can run programs on the application we can see all the logs and there was no SSH or RDP I've also got access to Vim uh which is typically not something you install on the on the machines but now I can edit the config files kind of poke around do some searching with inside the error logs or anything else there and so uh this is all hosted inside this HPC folder here and inside there you're going to see we have um Vim but we also have some networking scripts that we ship out of the box so that you can collect traces and packets and all sorts of other things there and the best part about that is it all goes away when the um when the container gets killed so that's a quick demo hopefully that gets you excited uh I'm James Sturdivant I'm a software engineer at Microsoft I've been wo
