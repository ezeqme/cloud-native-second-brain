---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Lucy Sweet", "Uber", "Dawn Chen", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1txGf/taming-the-beast-advanced-resource-management-with-kubernetes-lucy-sweet-uber-dawn-chen-google
youtube_search_url: https://www.youtube.com/results?search_query=Taming+the+Beast%3A+Advanced+Resource+Management+With+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Taming the Beast: Advanced Resource Management With Kubernetes - Lucy Sweet, Uber & Dawn Chen, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Lucy Sweet, Uber, Dawn Chen, Google
- Schedule: https://kccnceu2025.sched.com/event/1txGf/taming-the-beast-advanced-resource-management-with-kubernetes-lucy-sweet-uber-dawn-chen-google
- Busca YouTube: https://www.youtube.com/results?search_query=Taming+the+Beast%3A+Advanced+Resource+Management+With+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Taming the Beast: Advanced Resource Management With Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGf/taming-the-beast-advanced-resource-management-with-kubernetes-lucy-sweet-uber-dawn-chen-google
- YouTube search: https://www.youtube.com/results?search_query=Taming+the+Beast%3A+Advanced+Resource+Management+With+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AYxjk8ZZclo
- YouTube title: Taming the Beast: Advanced Resource Management With Kubernetes - Lucy Sweet & Dawn Chen
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/taming-the-beast-advanced-resource-management-with-kubernetes/AYxjk8ZZclo.txt
- Transcript chars: 32819
- Keywords: resource, actually, memory, feature, container, change, resources, application, workload, better, awesome, another, cluster, support, workloads, introduce, machine, restart

### Resumo baseado na transcript

Uh, for most of this presentation, I'm going to be playing uh, more of a role as a user of Kubernetes who uh, has a uh, what is it? I'm the software engineer from Google and also I'm the tech lead of the Kubernetes signal since its inception. is need about the class level or node level of the resource visiting and or you are going to risk your under provisioning of the critical for application and impact their performance right so so this is kind of the current approach with the introduction advance of the uh uh applications you want for example for the machine learning of the workload which has the one data process uh pre prepile of container and which require a lot of the resource spec at the beginning and but also we need to ensure about the uh machine learning main app and have the enough of the uh CPU and the memory can uh do the training jobs. Uh right now we're trying to run stateful workloads on Kubernetes, databases, uh things that are more tough to disrupt as well.

### Excerpt da transcript

Okay, everyone. Uh, welcome to uh, Taming the Beast on the, uh, last day of KubeCon. It's great to see such a good turnout considering, uh, last days. Typically, it's not really like this. Uh, my name's Lucy. I'm an engineer working Uber and I'm a contributor to Kubernetes. Uh, for most of this presentation, I'm going to be playing uh, more of a role as a user of Kubernetes who uh, has a uh, what is it? Who has a lot of struggles with uh, resource management. I'm thrilled to be joined here today by Dorm. Hello everyone. My name is Don Chen. I'm the software engineer from Google and also I'm the tech lead of the Kubernetes signal since its inception. And I'm thrilled here together with the Lucy and together with us uh we are going to show you folks uh a lot of the new tricks we development uh last one year and or couple years and to help you to management resources better and help you gain better control and also management the Kubernetes resource a little bit less and tend. Yeah. Awesome. So, uh, oh, can I borrow the clicker?

Ah, yes. So, uh, Dawn, uh, I've been using Kubernetes a lot at work, uh, recently, and it's been quite useful, especially for more basic stateless, uh, workloads and, uh, the more basic stuff we have, but we've really struggled with, uh, more advanced uh, workloads and more advanced resource usage. I uh, thought that uh, for to show my artistic creativity, I would draw and uh, how it feels like to me. It's almost like uh t trying to tame this wild beast uh to work with our platform. There's a few things in particular that I'm uh really uh really having uh trouble with. I was wondering if we could maybe step through them and see if we can work out uh whether we can do anything better. Yeah, go ahead. Absolutely. Let's tame this let's tame the beast. Okay, which is the forward one. That one. So, first off, um it's really it's uh setting resources at per container level. It's sometime sometimes it makes sense sometimes though it's a bit of a struggle. I don't really want to dedicate an entire slice of my CPU just to some site logging cycle.

I just wanted to share it with the main application. Uh there's also a few applications we have where we have one container normally has high utilization at the time another container has a low utilization and then it flips on the inverse and really we have to reserve all of space for both containers uh in order to use it. There's no real concept of sharing. um you know you could maybe do stuff in t
