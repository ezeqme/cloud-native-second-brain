---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Marina Moore", "Edera"]
sched_url: https://kccnceu2026.sched.com/event/2CW26/why-security-of-kubernetes-comes-down-to-linux-security-marina-moore-edera
youtube_search_url: https://www.youtube.com/results?search_query=Why+Security+of+Kubernetes+Comes+Down+to+Linux+Security+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Why Security of Kubernetes Comes Down to Linux Security - Marina Moore, Edera

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marina Moore, Edera
- Schedule: https://kccnceu2026.sched.com/event/2CW26/why-security-of-kubernetes-comes-down-to-linux-security-marina-moore-edera
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Security+of+Kubernetes+Comes+Down+to+Linux+Security+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Why Security of Kubernetes Comes Down to Linux Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW26/why-security-of-kubernetes-comes-down-to-linux-security-marina-moore-edera
- YouTube search: https://www.youtube.com/results?search_query=Why+Security+of+Kubernetes+Comes+Down+to+Linux+Security+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gaNCXj2j-0Q
- YouTube title: Why Security of Kubernetes Comes Down to Linux Security - Marina Moore, Edera
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/why-security-of-kubernetes-comes-down-to-linux-security/gaNCXj2j-0Q.txt
- Transcript chars: 25424
- Keywords: containers, container, kernel, actually, security, operating, around, little, running, access, processes, interesting, history, croups, inside, isolation, namespaces, boundary

### Resumo baseado na transcript

I'm going to talk to you today about a bit about Kubernetes security and why that actually means Linux security. I'm the head of research at ADA, a company that builds a harden runtime for containers. And really the point is that this kind of boundary that we've made around containers as I'm going to try and convince you of today is not really a security boundary. And we've kind of used it so much that we've come to think of it as a security boundary. um these but this was one of the first ones that was actually designed to separate customer workloads which is kind of interesting. Um these containers had the ability to assign storage and resources to a container.

### Excerpt da transcript

Hi everybody. I think we're just about at time. I know people are still walking in, but we will get go get going. Hi everyone. I'm Marina. I'm going to talk to you today about a bit about Kubernetes security and why that actually means Linux security. So a little bit about me. Um I'm Marina. I'm the head of research at ADA, a company that builds a harden runtime for containers. Um and I'm also very involved in the CNCF. one of the co-chairs of the CNCF tag security and compliance which is a technical advisory group that advises projects on security and compliance. Um I'm also a maintainer of the CNCF graduated project tough or the update framework and I'm coming to you from New York. So let's get into it. What are we going to talk about today? So I want to talk a bit about um container scapes to kind of frame the talk then go into the history of containers. I think that really helps us understand what containers do today. um to understand kind of where they come from, what they do. Then we're going to dive in a little bit into croups and namespaces, have a bit of a demo, and then wrap it up.

So, let's get into this. Um just, you know, I know you're all at KubeCon, but just in case you didn't know, this is this these are containers. Um this is a very simplified view of some containers running on top of a node. Um what you have really and and this is kind of the point here is you have um a bunch of containers that all sit on top of the shared a shared kernel with all the hardware and all those components underneath and the kernel kind of mediates access to all of those components. There's a bunch of mechanisms in place um kind of between and around these containers things like namespaces croups set comp etc that kind of provide this sort of barrier so that you when you're writing your application can pretend your container is kind of its own space. But fundamentally what we have is a is a bunch of containers that are acting kind of like processes on a kernel which is responsible for interfacing with all of that hardware. So what is a container escape? So a container escape is when that boundary we were just talking about um is violated.

So when um those assumptions that we make about these different containers being their own you know independent little areas are um are no longer true. And this enables unauthorized operations on the host system from processes running in a container. This includes things like code execution, privilege escalation, um access
