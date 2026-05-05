---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["AI ML", "Security", "SRE Reliability", "Community Governance"]
speakers: ["Greg Kroah-Hartman", "Linux Kernel Maintainer", "Fellow", "The Linux Foundation"]
sched_url: https://kccnceu2025.sched.com/event/1xBJR/keynote-rust-in-the-linux-kernel-a-new-era-for-cloud-native-performance-and-security-greg-kroah-hartman-linux-kernel-maintainer-fellow-the-linux-foundation
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Rust+in+the+Linux+Kernel%3A+A+New+Era+for+Cloud+Native+Performance+and+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Rust in the Linux Kernel: A New Era for Cloud Native Performance and Security - Greg Kroah-Hartman, Linux Kernel Maintainer & Fellow, The Linux Foundation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Greg Kroah-Hartman, Linux Kernel Maintainer, Fellow, The Linux Foundation
- Schedule: https://kccnceu2025.sched.com/event/1xBJR/keynote-rust-in-the-linux-kernel-a-new-era-for-cloud-native-performance-and-security-greg-kroah-hartman-linux-kernel-maintainer-fellow-the-linux-foundation
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Rust+in+the+Linux+Kernel%3A+A+New+Era+for+Cloud+Native+Performance+and+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Rust in the Linux Kernel: A New Era for Cloud Native Performance and Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1xBJR/keynote-rust-in-the-linux-kernel-a-new-era-for-cloud-native-performance-and-security-greg-kroah-hartman-linux-kernel-maintainer-fellow-the-linux-foundation
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Rust+in+the+Linux+Kernel%3A+A+New+Era+for+Cloud+Native+Performance+and+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kQ4X6-mPHqw
- YouTube title: Keynote: Rust in the Linux Kernel: A New Era for Cloud Native Performance and... Greg Kroah-Hartman
- Match score: 0.968
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-rust-in-the-linux-kernel-a-new-era-for-cloud-native-performanc/kQ4X6-mPHqw.txt
- Transcript chars: 10445
- Keywords: kernel, important, maintainers, compiler, security, number, unlock, developers, remember, return, memory, enforce, access, million, common, easier, maintainer, changes

### Resumo baseado na transcript

Hi, I'm Greg, kernel maintainer, developer, one of many thousands of kernel people. But first, it's really about C and Rust and Linux because C is what runs the world and C is still very important, but Rust is doing good things, too. So Rust can prevent a huge majority of security issues at build time, which is much much more important than review time.

### Excerpt da transcript

Hi, I'm Greg, kernel maintainer, developer, one of many thousands of kernel people. I'm talking about Rust and Linux. But first, it's really about C and Rust and Linux because C is what runs the world and C is still very important, but Rust is doing good things, too. But I was told that many of you don't really know what Linux is. This is a Linux Foundation conference. Um, Linux is that little thing at the bottom that hides the hardware from you. It's our job as a kernel, an operating system to isolate different processes, to make it so that you have a fast, secure system, and to make the hardware look agnostic. You don't care what disc controller you're using. You don't care what network controller you're using. You don't care what processor you're using. It just works. That's Linux's job. We get out of the way. We let you go and do whatever you want to do. We're a tool to let you achieve your task. Um, our community is big. It's really, really big. Uh, almost double the size of Kubernetes. Sorry, you're number two.

We're still number one. Um, this was just last year. At least 355 different companies. We don't really count them all. We kind of get close. Um, we also go fast, really, really fast. This is the number of changes accepted. It takes on average at least three tries to get a change accepted. So that change at 76,000 changes has been reviewed two other times before it got accepted. Our maintainers do a lot a lot of work. We have about three maybe 200 maintainers that do the majority of the work. 700 total. Um so the ratio of developers to maintainers is still quite large. Um we're going really really fast. That's almost eight nine changes an hour for the past decade. 24 hours a day, 7 days a week. Small percentage of those go into the stable trees. And 13 CVEes a day. Sounds like a lot. We're actually about half the size of number CVES per day than the other operating systems. So if you count CVEs as being security issues as it matters, I don't. Um, we're still better than the other people. And number of releases 8 to nine weeks like clockwork for the past 15 years.

New release like clockwork. you can just depend on us. I gave a longer talk about how all this works. You can just Google that and look at that if you're curious. Uh turns out we run the world. Um Android 4 billion devices. Everything else is a rounding error. You guys and servers with maybe 200 million. Again, rounding error. Chromebooks 25 30 million a year for the past decade. Sti
