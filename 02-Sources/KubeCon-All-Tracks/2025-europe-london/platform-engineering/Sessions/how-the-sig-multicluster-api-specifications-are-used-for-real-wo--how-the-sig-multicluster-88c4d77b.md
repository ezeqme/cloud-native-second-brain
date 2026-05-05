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
speakers: ["August Simonelli", "Red Hat", "Ryan Zhang", "Microsoft"]
sched_url: https://kccnceu2025.sched.com/event/1txHL/how-the-sig-multicluster-api-specifications-are-used-for-real-world-multicluster-management-august-simonelli-red-hat-ryan-zhang-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=How+the+SIG-Multicluster+API+Specifications+Are+Used+for+Real+World+Multicluster+Management+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How the SIG-Multicluster API Specifications Are Used for Real World Multicluster Management - August Simonelli, Red Hat & Ryan Zhang, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: August Simonelli, Red Hat, Ryan Zhang, Microsoft
- Schedule: https://kccnceu2025.sched.com/event/1txHL/how-the-sig-multicluster-api-specifications-are-used-for-real-world-multicluster-management-august-simonelli-red-hat-ryan-zhang-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=How+the+SIG-Multicluster+API+Specifications+Are+Used+for+Real+World+Multicluster+Management+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How the SIG-Multicluster API Specifications Are Used for Real World Multicluster Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHL/how-the-sig-multicluster-api-specifications-are-used-for-real-world-multicluster-management-august-simonelli-red-hat-ryan-zhang-microsoft
- YouTube search: https://www.youtube.com/results?search_query=How+the+SIG-Multicluster+API+Specifications+Are+Used+for+Real+World+Multicluster+Management+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I9GV4N23dvE
- YouTube title: How the SIG-Multicluster API Specifications Are Used for Real World... August Simonelli & Ryan Zhang
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-the-sig-multicluster-api-specifications-are-used-for-real-world-mu/I9GV4N23dvE.txt
- Transcript chars: 38272
- Keywords: cluster, clusters, actually, placement, properties, multicluster, called, namespace, profile, basically, another, running, question, probably, deployment, managed, deployed, across

### Resumo baseado na transcript

This is how the SIG multicluster API specifications are used for real world multicluster management. I work with the open cluster management project and I work for Red Hat. So probably if uh if uh I assume most of you are Kubernetes practitioners you know that there's actually no single ID for a cluster there's there just not there. Uh if you want to identify a cluster it doesn't exist in the Kubernetes world. It see looks simple but that actually is something that kubernetes doesn't have and we are actually in the process of if you uh we are going to upload our our deck so that click into the link you will see we are actually having So we have a a API called work API basically allows you to from the control plane side it's kind of again think of that as Kubernetes right on the control plane side you can place uh resources onto clusters just like when on the

### Excerpt da transcript

Welcome to our talk. This is how the SIG multicluster API specifications are used for real world multicluster management. My name is August Simonelli. I work with the open cluster management project and I work for Red Hat. And this is Ryan. And I'm Ryan. I am a maintainer for the newly contributed CNCF project called Kubby Fleet and I work for Microsoft Azure. Cool. So let's talk a little bit about what we're going to speak about today. So we've done our intro. So, that's one thing down. Um, we want to kind of go over the SIG multicluster standards. I'm sure many in the room know them, but it's always good to recap them and to sort of baseline where we are with those things. Then, we're going to demo some multicluster because that's the fun stuff. Uh, we've got a mix of a a recorded demo, that's me, and a live demo from Ryan, that's him sweating over there. And then we can do some Q&A. So the first thing I want to call out and again I know there are members of SIG multicluster here but the idea behind this is that we want to define APIs and not implementations.

We're not trying to say this is exactly how you do it. We want to define standards. We want to define ways that you can work within uh a multicluster space and be able to add your stuff to it easily. So to do that there are four basic APIs that Ryan will cover. uh the about API, the multicluster services API, the work API, and the cluster profile API. And you're going to see those demoed today as well. And why do we do this? Because by adopting standards, it makes it easier for the projects you work for and and add to contribute and to be part of this. So whether it's something like Cappy or Couple Fleet or whatever it is you're working with, we make it by using the standard, we make it easier for you to fill those empty boxes. So you can come along and say hey my project wants to be part of multicluster and this is the way that we can do that and the idea again is that once we have these standards the agreed upon community standards it's not about bringing your standard in and dropping it on and it's about finding something that works for everyone.

So that is sort of the basics on how we do this. I'll hand over to Ryan now to take you through a quick overview. Thank you Alex. Um yeah so let's first talk about the the oldest one simplest one is called about API. So what it is really about it's about uh define some properties well-known properties for a cluster. So probably if uh if uh I assume mos
