---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers", "SRE Reliability"]
speakers: ["Agathe Blaise", "Thales", "Jacopo Bufalino", "CNAM"]
sched_url: https://kccnceu2025.sched.com/event/1txFb/enhancing-software-composition-analysis-resilience-against-container-image-obfuscation-agathe-blaise-thales-jacopo-bufalino-cnam
youtube_search_url: https://www.youtube.com/results?search_query=Enhancing+Software+Composition+Analysis+Resilience+Against+Container+Image+Obfuscation+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Enhancing Software Composition Analysis Resilience Against Container Image Obfuscation - Agathe Blaise, Thales & Jacopo Bufalino, CNAM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Agathe Blaise, Thales, Jacopo Bufalino, CNAM
- Schedule: https://kccnceu2025.sched.com/event/1txFb/enhancing-software-composition-analysis-resilience-against-container-image-obfuscation-agathe-blaise-thales-jacopo-bufalino-cnam
- Busca YouTube: https://www.youtube.com/results?search_query=Enhancing+Software+Composition+Analysis+Resilience+Against+Container+Image+Obfuscation+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Enhancing Software Composition Analysis Resilience Against Container Image Obfuscation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFb/enhancing-software-composition-analysis-resilience-against-container-image-obfuscation-agathe-blaise-thales-jacopo-bufalino-cnam
- YouTube search: https://www.youtube.com/results?search_query=Enhancing+Software+Composition+Analysis+Resilience+Against+Container+Image+Obfuscation+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=G24upbAXVd8
- YouTube title: Enhancing Software Composition Analysis Resilience Against Contai... Agathe Blaise & Jacopo Bufalino
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/enhancing-software-composition-analysis-resilience-against-container-i/G24upbAXVd8.txt
- Transcript chars: 26769
- Keywords: container, package, software, content, obuscation, actually, vulnerabilities, containers, offiscation, techniques, docker, packages, information, basically, source, images, question, analyze

### Resumo baseado na transcript

So welcome to this talk which is about analyzing the resilience of software composition analyszis against the container image opuscation. I'm a PhD candidate at AL University and at the same time I'm working as a researcher at the Senam Institute in in Paris. So in this work we wanted to analyze how the landscape evolved over the past two years and we proposed an academic approach to the problem that we will detail right after. So when designing the docker file the docker file in such a way that the installed software is partially or even totally undetected by the container vulnerability scanners and this can arise for several reasons. So this is a good recommendation that uh we can say to um increase uh the the performance of the tools and the only difference is that or can also uh analyze the URL downloaded compared to sift all. Then of course there are problems also there because there's incompatibility between uh uh bomb sbomb formats but we made it sure that it was compatible at least with the sift so that you you can use it with the with se.

### Excerpt da transcript

Hello everyone. So welcome to this talk which is about analyzing the resilience of software composition analyszis against the container image opuscation. So today with me there is Yakopo. Um hello everyone. I'm Yakopo. I'm a PhD candidate at AL University and at the same time I'm working as a researcher at the Senam Institute in in Paris. Uh my research revolves around container and network security. And my name is Agad BL. I'm a research engineer working at Tales in France and I'm especially working on the security or virtualiz network environments. So very brief advertisement before we dive into the technical content. So this project was partially funded by a project which is named SE for Y for sec. It is a European project. So I put the link and QR code here. If you're interested in what we are doing, uh please check it out. We are always looking for collaborations. So now diving into the content of this talk which is obuscation in container in image. Why should we care in the first place? So two years ago at CubeCon 2023, a talk introduced the concept of what we call malicious compliance and container opuscation.

So starting from a base container, the presenters progressively introduced some modification to a docker file and ultimately reduce the number of vulnerabilities that were found by open source tools. So they actually fooled the container vulnerability scanners and uh which are in charge of detecting package and vulnerabilities in the container image. So in this work we wanted to analyze how the landscape evolved over the past two years and we proposed an academic approach to the problem that we will detail right after. So I will first give a short overview of the tools that exist for container vulnerability analysis and scanning. So there are typically two main steps when we want to scan for vulnerabilities in a container image. So first the tool will index the content of the container image. So they will analyze the container file systems and try to find installed software. So it can be the operating system, the operating system packages, the programming language, the dependencies and libraries and finally the binaries.

And at the end of this process they will generate a software bill of materials or sbomb that is a list of components all of packages uh running into that container. Then the second step is to search for vulnerabilities in this software. So they will match uh those package against the base of non vulnerabilities and typically
