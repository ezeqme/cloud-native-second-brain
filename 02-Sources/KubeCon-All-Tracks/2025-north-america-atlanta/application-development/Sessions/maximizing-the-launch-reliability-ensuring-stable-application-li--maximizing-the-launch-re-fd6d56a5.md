---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Hiroshi Hayakawa", "LY Corporation"]
sched_url: https://kccncna2025.sched.com/event/27FXp/maximizing-the-launch-reliability-ensuring-stable-application-lift-off-and-orbit-on-kubernetes-hiroshi-hayakawa-ly-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Maximizing+the+Launch+Reliability%3A+Ensuring+Stable+Application+Lift-off+and+Orbit+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Maximizing the Launch Reliability: Ensuring Stable Application Lift-off and Orbit on Kubernetes - Hiroshi Hayakawa, LY Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Hiroshi Hayakawa, LY Corporation
- Schedule: https://kccncna2025.sched.com/event/27FXp/maximizing-the-launch-reliability-ensuring-stable-application-lift-off-and-orbit-on-kubernetes-hiroshi-hayakawa-ly-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Maximizing+the+Launch+Reliability%3A+Ensuring+Stable+Application+Lift-off+and+Orbit+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Maximizing the Launch Reliability: Ensuring Stable Application Lift-off and Orbit on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXp/maximizing-the-launch-reliability-ensuring-stable-application-lift-off-and-orbit-on-kubernetes-hiroshi-hayakawa-ly-corporation
- YouTube search: https://www.youtube.com/results?search_query=Maximizing+the+Launch+Reliability%3A+Ensuring+Stable+Application+Lift-off+and+Orbit+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vTmImF_mibY
- YouTube title: Maximizing the Launch Reliability: Ensuring Stable Application Lift-off and Orbi... Hiroshi Hayakawa
- Match score: 0.954
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/maximizing-the-launch-reliability-ensuring-stable-application-lift-off/vTmImF_mibY.txt
- Transcript chars: 18185
- Keywords: application, startup, applications, container, memory, request, limits, tuning, initialization, launch, resources, performance, resource, reliability, important, traffic, feature, maximum

### Resumo baseado na transcript

I'm a product owner of one of our internal developer platform working for corporations private cloud division. LY Corporation is one of the largest internet companies in Japan offering a wide variety of services such as communication apps, internet portals, news media, e-commerce and so on. Then I'll discuss about the recent Kubernetes feature called impress resize which let you change the amount of resources to container without restarting. When the port resource is registered with the Kubernetes API server, the scheduleuler decides which node will run the port. Once the application has been running for a while, it eventually reaches a stable state where it can work with maximum performance. For example, crashes caused by slight performance degration from minor code changes or library updates or by unusually high amounts of traffic on newly starting ports.

### Excerpt da transcript

So good afternoon everyone and welcome to my presentation. So let me start the session and first let me introduce myself. I'm Hiroshi. I'm a product owner of one of our internal developer platform working for corporations private cloud division. LY Corporation is one of the largest internet companies in Japan offering a wide variety of services such as communication apps, internet portals, news media, e-commerce and so on. So we have been operating a large scale Kubernetes based plat Kubernetes based platform for many years and today's presentation is based on the experiences we've gained through running a lot of applications on the platform and and I contribute to CNC platforming committee group and in addition I have written books on Kubernetes in Japanese and my top priority in this presentation is to introduce my DIY keyboard to global audience. Yeah, this is uh my current desk desktop setup. [laughter] Thank you. So anyway, today [sighs] I'll talk about how to launch applications with greater stability and reliability on Kubernetes.

I've organized my presentation into three key sections and conclusion. First, I will introduce what I mean with launch reliability and explain why it's important for production applications. And next, I'll share practical techniques for improving launch reliability. This includes tuning strategies for both container and application itself and ensuring proper application initialization before accepting traffic. Then I'll discuss about the recent Kubernetes feature called impress resize which let you change the amount of resources to container without restarting. and we'll explore how this can help with launch reliability. And finally, we'll lap things up with a conclusion and key takeaways. All right, so let's get started with the introduction. First, let me explain how application start on Kubernetes. When the port resource is registered with the Kubernetes API server, the scheduleuler decides which node will run the port. Each node has a cublet that handles the preparations to launch the port. The preparations include setting up networking and data volumes for the port.

And after that the process of the application starts inside the container. Then the application performs various initializations. The application then reaches a state where it can execute its domain logic. For typical web applications, this means accepting traffic, processing requests, and returning responses. Once the application has been running for a
