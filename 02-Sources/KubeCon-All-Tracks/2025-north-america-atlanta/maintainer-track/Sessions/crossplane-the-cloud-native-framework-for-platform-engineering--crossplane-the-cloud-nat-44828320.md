---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Jared Watts", "Nic Cope", "Upbound"]
sched_url: https://kccncna2025.sched.com/event/27NmP/crossplane-the-cloud-native-framework-for-platform-engineering-jared-watts-nic-cope-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+-+The+Cloud+Native+Framework+for+Platform+Engineering+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Crossplane - The Cloud Native Framework for Platform Engineering - Jared Watts & Nic Cope, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Jared Watts, Nic Cope, Upbound
- Schedule: https://kccncna2025.sched.com/event/27NmP/crossplane-the-cloud-native-framework-for-platform-engineering-jared-watts-nic-cope-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+-+The+Cloud+Native+Framework+for+Platform+Engineering+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Crossplane - The Cloud Native Framework for Platform Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NmP/crossplane-the-cloud-native-framework-for-platform-engineering-jared-watts-nic-cope-upbound
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+-+The+Cloud+Native+Framework+for+Platform+Engineering+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XKUi8xxkyjM
- YouTube title: Crossplane - The Cloud Native Framework for Platform Engineering - Jared Watts & Nic Cope, Upbound
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/crossplane-the-cloud-native-framework-for-platform-engineering/XKUi8xxkyjM.txt
- Transcript chars: 33878
- Keywords: crossplane, resource, basically, resources, install, python, operations, manage, composite, function, composed, circuit, control, actually, provider, pretty, platform, developers

### Resumo baseado na transcript

Today we're going to go through what crossplane is for the first half of this talk. And then Jared here is going to dive into some of the more advanced and up andcoming features in crossplane. You get this closed loop control where Kubernetes or crossplane or operators look at the observed state of the world. And if I think back to those days before crossplane before Kubernetes there was two to three ways that you could enable your developers uh to get stuff done as a platform team. uh the teams with the most bandwidth which was simply roll your own control plane from scratch right build a web portal build a backend build an API build automation that does this right since Kubernetes has come around uh with the invention of CRDs and the popularization of the controller and APIdriven pattern this self-service with guardrails has become much more accessible to people right projects like Kubernetes and crossplane allow you to define an API that is what your platform team wants the developers to interact with.

### Excerpt da transcript

Hi everyone, welcome to the twice annual update on crossplane. Today we're going to go through what crossplane is for the first half of this talk. And then Jared here is going to dive into some of the more advanced and up andcoming features in crossplane. By the way, hi, I'm Nick. I'm a maintainer of crossplane. This is Jared. He's also a crossplane maintainer. >> Hello. All right, so what is crossplane? I like to think of crossplane as a framework for building control planes, a way to build custom Kubernetes APIs without having to write controllers. So here we've got an example of an app custom resource in Kubernetes. This is not an API that crossplane has built into it. This is an API that you can create yourself using crossplane. So why would you want to do this? I think that today a lot of platform engineering teams what they're trying to do is enable their developers to self-service and often the way that they're enabling developers to self-service is basically building abstractions on top of lower level concepts right so if you're building these abstractions today you might be reaching for things like Helm charts or Terraform modules as a way to take complex apps and infrastructure concepts like services deployments RDS instances and wrap those up into a simpler abstraction that your developers can work with more easily.

Another way that you could do this is by writing a Kubernetes controller, defining a Kubernetes custom resource, building an operator, teaching it how to do that. This gets you a lot of the benefits of control planes that we'll go into later, but that is challenging to do it. It there's a lot of foot guns. It takes a niche skill set to write a controller for Kubernetes. And so this is what crossblade helps with. We're trying to make this easier for you to do, try to open it up to more people. So before we go into talking more about what crossplane is, I just want to celebrate for a minute that we are now a CNCF graduated project. [applause] Yeah. Thank you so much to our community. Uh we it's been about seven years that the project's been around, right? I think >> I thought you meant how long we're working on. >> And us also >> felt like that. >> Yeah. Um uh but we we were looking into some of the numbers while we were applying for graduation and we are now in the top 10% of CNCF projects for number of contributors.

We have thousands of contributors from hundreds of organizations widely adopted at household names in production. So
