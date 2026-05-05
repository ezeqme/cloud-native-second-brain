---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Application + Development"
themes: ["Kubernetes Core"]
speakers: ["Jerry Lozano", "RX-M LLC"]
sched_url: https://kccnceu2021.sched.com/event/iE4Y/kubernetes-on-windows-a-journey-jerry-lozano-rx-m-llc
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+on+Windows+-+A+Journey+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes on Windows - A Journey - Jerry Lozano, RX-M LLC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Application + Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Jerry Lozano, RX-M LLC
- Schedule: https://kccnceu2021.sched.com/event/iE4Y/kubernetes-on-windows-a-journey-jerry-lozano-rx-m-llc
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+on+Windows+-+A+Journey+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes on Windows - A Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4Y/kubernetes-on-windows-a-journey-jerry-lozano-rx-m-llc
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+on+Windows+-+A+Journey+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=As2u-xT-i_c
- YouTube title: Kubernetes on Windows - A Journey - Jerry Lozano, RX-M LLC
- Match score: 0.818
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-on-windows-a-journey/As2u-xT-i_c.txt
- Transcript chars: 21308
- Keywords: windows, worker, cluster, server, running, journey, container, microservice, familiar, docker, install, application, environment, command, interface, authorize, ccauth, control

### Resumo baseado na transcript

We are an enterprise cloud native development, training, and consulting firm. I carry the title of senior consultant, but I am a software developer who specializes in system level and operating system development. Well, the control plane of Kubernetes does not and it may never run outside of Linux. There is a ton of code on Windows that faces the same challenges that any application moving forward faces. At some high level, the problems we face, I think, will fall into two categories. AWS networking options present problems of their own when you work with uh a mixed cluster.

### Excerpt da transcript

Welcome to the session Kubernetes on Windows, a journey. My name is Jerry Lozano. I am a software developer and I work for RXM. We are an enterprise cloud native development, training, and consulting firm. I carry the title of senior consultant, but I am a software developer who specializes in system level and operating system development. My work over the years has led me through Unix, Linux, and Windows. I developed device drivers for all operating systems and I have focused on application framework and related software. Architecting applications that are microservice oriented, cloud hosted, it was a somewhat natural migration for my interests and skill set. So, thank you for attending. The title of this presentation is a little misleading, but we seem to be attracted to intriguing titles, so here we are. Kubernetes on Windows. Kubernetes is designed to run Linux containers in an orchestrated environment. Kates is built upon Linux concepts such as C groups and IP tables, but CubeCon itself is hosted by CNCF, which is part of the Linux Foundation.

So, the obvious questions to start this presentation, when did Windows enter the world of Kates and why does anyone or should anyone care about Windows in the world of Kates? Both are very good questions. So, does Kubernetes even run on Windows? Well, the control plane of Kubernetes does not and it may never run outside of Linux. The official documents of Kates state that there are no plans to support a Windows only Kates cluster. But for some time now, since 1.14, Kates has permitted mixed clusters with Windows worker nodes running side-by-side with them Linux worker nodes. Today, mixed cluster requires Kubernetes 1.17 or later. I understand for many people attending today, the idea of a mixed cluster can be unsettling. But the idea of including Windows worker node environments is powerful and makes perfect sense for many scenarios. So, why Windows? The data shows that for the popular and important sites, Windows is doing quite well, thank you. W3Techs shows that Windows is used on more of the top 1,000 websites than is Unix or Linux.

Statista shows that over 70% of the global server market is Windows based. But look, we're not here to argue about statistics or the different ways to look at market penetration. The point here is clear. There is a ton of code on Windows that faces the same challenges that any application moving forward faces. That includes scalability, availability, you know, including robustne
