---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Zhang Zhen", "Yuxing Yuan", "Alibaba Cloud"]
sched_url: https://kccncna2025.sched.com/event/27FVA/unleash-the-power-of-inplace-pod-resource-resizing-for-startup-and-cost-optimization-zhang-zhen-yuxing-yuan-alibaba-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Unleash+the+Power+of+Inplace+Pod+Resource+Resizing+for+Startup+and+Cost+Optimization+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Unleash the Power of Inplace Pod Resource Resizing for Startup and Cost Optimization - Zhang Zhen & Yuxing Yuan, Alibaba Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Zhang Zhen, Yuxing Yuan, Alibaba Cloud
- Schedule: https://kccncna2025.sched.com/event/27FVA/unleash-the-power-of-inplace-pod-resource-resizing-for-startup-and-cost-optimization-zhang-zhen-yuxing-yuan-alibaba-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Unleash+the+Power+of+Inplace+Pod+Resource+Resizing+for+Startup+and+Cost+Optimization+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Unleash the Power of Inplace Pod Resource Resizing for Startup and Cost Optimization.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVA/unleash-the-power-of-inplace-pod-resource-resizing-for-startup-and-cost-optimization-zhang-zhen-yuxing-yuan-alibaba-cloud
- YouTube search: https://www.youtube.com/results?search_query=Unleash+the+Power+of+Inplace+Pod+Resource+Resizing+for+Startup+and+Cost+Optimization+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Hod4UPoMUPE
- YouTube title: Unleash the Power of Inplace Pod Resource Resizing for Startup and Cost... Zhang Zhen & Yuxing Yuan
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/unleash-the-power-of-inplace-pod-resource-resizing-for-startup-and-cos/Hod4UPoMUPE.txt
- Transcript chars: 27754
- Keywords: resizing, actually, memory, resource, application, change, resources, scaling, workload, container, another, cruise, possible, vertical, advanced, startup, controller, checkpoint

### Resumo baseado na transcript

Uh hello guys uh good morning I'm J from Alibaba clouds and I'm also the maintainer of open cruise project. Uh welcome to my speech and this talk is about the various interesting use cases about in place board resizing. there are still a chance that weak service can be the bottleneck and we have to scale the service quickly in place port resizing help us to scale the service up immediately as much as possible before our horizontal port scaling can finish uh scale The application startup problem is quite common and especially serious for Java based application. However, comparing to the compiler just in time, it is often comes with a cost of a degraded peak throughput and latency. Well, using in place resizing, one can increase the application CPU in the web hook and when the startup finish one can scale the CPU down in the controller.

### Excerpt da transcript

Uh hello guys uh good morning I'm J from Alibaba clouds and I'm also the maintainer of open cruise project. Uh welcome to my speech and this talk is about the various interesting use cases about in place board resizing. It is actually the first debut of open cruise in Kubicon North America. So just a simple questions uh have you guys ever have heard or just use open cruise project please just raise your hand okay a few well u maybe that's because the result of lack of maintainers from North America maybe that's a good starting point just a little quick spec uh recap for those who are not yet familiar with implant port resizing it It is a a controversial and powerful feature that enable non-disruptive for the vertical autoscaling and it open up many possibility. Now it has graduate to beta and then it is enabled in recent kubernetes. Uh the kubernetes community first discussed in place resizing in the context of in place update. So we go one step further to enable in place image update in open cruise project before the native resizing API in Alibaba.

We take a quite programmatic method and implement in-house API for in place resource resizing. Uh it is the use case of the emergency scaling in the grid promotion. uh the grid promotion which is quite similar to black Friday but in in China and and it has a much larger traffic uh in the grid promotion the traffic search uh search to very high level and even though even through careful low testing there are still a chance that weak service can be the bottleneck and we have to scale the service quickly in place port resizing help us to scale the service up immediately as much as possible before our horizontal port scaling can finish uh scale the ports here uh my speech will contain just three parts first I will guide you through the very use case and the tools for in place port resizing which is the major part and we will I will continue with some guidelines about the Java Spark application which uh which will help you to help the Java application adapt to the uh changing resource requirements.

And the last I will conclude with some future works. Uh first of all one common use case and actually the most widely used cases from my experience is the application startup. The application startup problem is quite common and especially serious for Java based application. When the Java application start JVM need to load bunch of Java classes and compile them into a machine code which is quite resource consuming and ac
