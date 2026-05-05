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
speakers: ["John Coyne", "Capital One"]
sched_url: https://kccncna2025.sched.com/event/27Fd9/autoscaling-spring-boot-apps-in-kubernetes-with-keda-john-coyne-capital-one
youtube_search_url: https://www.youtube.com/results?search_query=Autoscaling+Spring+Boot+Apps+in+Kubernetes+With+KEDA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Autoscaling Spring Boot Apps in Kubernetes With KEDA - John Coyne, Capital One

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: John Coyne, Capital One
- Schedule: https://kccncna2025.sched.com/event/27Fd9/autoscaling-spring-boot-apps-in-kubernetes-with-keda-john-coyne-capital-one
- Busca YouTube: https://www.youtube.com/results?search_query=Autoscaling+Spring+Boot+Apps+in+Kubernetes+With+KEDA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Autoscaling Spring Boot Apps in Kubernetes With KEDA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fd9/autoscaling-spring-boot-apps-in-kubernetes-with-keda-john-coyne-capital-one
- YouTube search: https://www.youtube.com/results?search_query=Autoscaling+Spring+Boot+Apps+in+Kubernetes+With+KEDA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=41jPTzrUX4I
- YouTube title: Autoscaling Spring Boot Apps in Kubernetes With KEDA - John Coyne, Capital One
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/autoscaling-spring-boot-apps-in-kubernetes-with-keda/41jPTzrUX4I.txt
- Transcript chars: 29873
- Keywords: metrics, prometheus, application, seconds, scaling, replicas, number, metric, average, scaled, around, second, requests, endpoint, spring, called, configuration, desired

### Resumo baseado na transcript

I'm a distinguished engineer of application engineering at Discover, which is now part of Capital One. And today I'm hoping to provide some insight on how you can efficiently scale a Spring Boot application in Kubernetes by using its application metrics. If your public cloud provider were to say go down in the east region on a Monday morning whenever your traffic is receiving a high amount of volume, could you scale up in the west? And there's horizontal scaling in which you scale out the number of instances to your existing workloads. So Kubernetes has a built-in or horizontal pod autoscaler or HPA and it basically offers the ability to scale up or down the number of pods based on your demand. Um so it currently what it offers is scaling on metric targets of either CPU or memory and uh when it first came out it just supported pod uh the pod metrics but now starting with Kubernetes 1.30 it does support container level metrics and

### Excerpt da transcript

All right, we'll go and get started here. Good morning. Hope everybody's been having a great KubeCon so far. Um, thanks for sticking around to the last day and coming to my talk. My name is John Coin. I'm a distinguished engineer of application engineering at Discover, which is now part of Capital One. And today I'm hoping to provide some insight on how you can efficiently scale a Spring Boot application in Kubernetes by using its application metrics. So a quick look at the agenda for today. I'm first going to do a little bit of a deep dive into the built-in functionality in Kubernetes for the autoscaler before I'll dive into KADA, which stands for Kubernetes event-driven autoscaling, and we'll see how that can augment the built-in HPA. I'll then showcase how Spring Boot can use a Java library called micrometer to expose metrics to a metric provider called Prometheus, which can help us to scale our application. And I'll wrap things all up the end, tie it together in a demo. So the first question I want to answer is why do we want to implement autoscaling in the first place?

Now I think the first the the first and most obvious reason is to save money. If you're deploying your workloads to the public cloud then obviously the less resources you use the more money you're going to save. The second is disaster recovery. If you're deploying your application to multiple clusters across multiple regions it's probably for a good reason for high availability and resiliency. If your public cloud provider were to say go down in the east region on a Monday morning whenever your traffic is receiving a high amount of volume, could you scale up in the west? And last is just to be a good steward of energy. You know, making sure that you're only using the resources that you need to run your application. Now, when we talk about scaling, there's really kind of two highle types. You have vertical scaling in which you add resources like CPU or memory to your existing instances. And there's horizontal scaling in which you scale out the number of instances to your existing workloads. So the topic of today we're going to be discussing is going to be horizontal scaling.

So Kubernetes has a built-in or horizontal pod autoscaler or HPA and it basically offers the ability to scale up or down the number of pods based on your demand. It currently works with either a deployment or a stateful set. And like many things in Kubernetes, it works in a control loop. every 15 seconds it tries t
