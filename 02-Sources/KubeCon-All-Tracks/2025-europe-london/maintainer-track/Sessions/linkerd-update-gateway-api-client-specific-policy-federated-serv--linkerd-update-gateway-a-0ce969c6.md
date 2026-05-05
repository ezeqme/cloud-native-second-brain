---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Networking", "Kubernetes Core", "Community Governance"]
speakers: ["Alex Leong", "Buoyant"]
sched_url: https://kccnceu2025.sched.com/event/1tczg/linkerd-update-gateway-api-client-specific-policy-federated-services-multicluster-rust-more-alex-leong-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Linkerd+Update%3A+Gateway+API%2C+Client-Specific+Policy%2C+Federated+Services%2C+Multicluster%2C+Rust%2C+%26+More%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Linkerd Update: Gateway API, Client-Specific Policy, Federated Services, Multicluster, Rust, & More! - Alex Leong, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Alex Leong, Buoyant
- Schedule: https://kccnceu2025.sched.com/event/1tczg/linkerd-update-gateway-api-client-specific-policy-federated-services-multicluster-rust-more-alex-leong-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Linkerd+Update%3A+Gateway+API%2C+Client-Specific+Policy%2C+Federated+Services%2C+Multicluster%2C+Rust%2C+%26+More%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Linkerd Update: Gateway API, Client-Specific Policy, Federated Services, Multicluster, Rust, & More!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczg/linkerd-update-gateway-api-client-specific-policy-federated-services-multicluster-rust-more-alex-leong-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Linkerd+Update%3A+Gateway+API%2C+Client-Specific+Policy%2C+Federated+Services%2C+Multicluster%2C+Rust%2C+%26+More%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aYGGnDDGX-Q
- YouTube title: Linkerd Update: Gateway API, Client-Specific Policy, Federated Services, Multicluster... Alex Leong
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/linkerd-update-gateway-api-client-specific-policy-federated-services-m/aYGGnDDGX-Q.txt
- Transcript chars: 30018
- Keywords: protocol, traffic, mesh, linkerd, linkerty, gateway, clusters, multicluster, release, federated, whatever, cluster, called, detection, policy, talking, metrics, install

### Resumo baseado na transcript

I'm a software engineer at Buoyant and I'm happy to be giving this update on kind of all the things that are new and going on with the link project. Uh the pace of execution on this project has just been like through the roof. Uh but you should kind of have to scale up the config that you uh is required based on what your needs are and easy things should be easy. And so, you know, at that scale, it's very easy, you know, as software developers to be like, well, computers are powerful, memory is cheap, you know, who cares? Uh, we call it a micro proxy because it is designed to be as lightweight and out of the way as possible. Uh maybe most notable was that we took a lot of the functionality that was in linkerd for per routeout behavior uh like per routeout retries, per route timeouts, per route metrics, um all of the stuff that was previously configured in linkd using something called service profiles.

### Excerpt da transcript

All right, welcome everyone. Hi, thank you for coming. This is the uh linkery project update. Um my name is Link My name is Linkerty. My name is Alex Leang. I'm a project maintainer on linkerty. I'm a software engineer at Buoyant and I'm happy to be giving this update on kind of all the things that are new and going on with the link project. It's been a really busy year for us. Uh the pace of execution on this project has just been like through the roof. So there's a lot to talk about. Um there have been in fact a lot of things uh going on with linker at this uh KubeCon. So we're kind of towards the end of the week now, but we've had a whole bunch of talks all through the week. We had a great uh linker day uh back on Tuesday. Uh a lot of really really cool talks there. Um on Wednesday there were a couple of talks. I gave one. Uh William Morgan gave the other. Uh those recordings, if you weren't able to make it to those, I highly recommend you check those out when the recordings are available. Um, and then here we are on Thursday.

This is the linkery update where I'm just going to give kind of a overview of where the project is at, what's new, what's going on, what's coming up. Um, of course, we're also in the uh the expo hall. So, if you have more questions about LinkerDert, come find us there and uh happy to chat about all all things service mesh. Um, if you don't already know what link is, um, it is a service mesh. So it's ultra light, ultra fast security first is our positioning. Um it's built specifically for Kubernetes. So it's Kubernetes native. Um it's been in production for eight years now at a variety of different companies at various different scales and in various different environments. Um so it's it's definitely battle tested and battle hardened. Um we're a CNCF project. We're graduated and uh I'm really proud of the work that we do on it. Um and to kind of summarize like in a nutshell where we think uh linkd is positioned as a service mesh, we wanted to give every platform engineer in the world the tools they need to create a secure, reliable and observable cloudnative platform.

And all three of those pieces are kind of critical. You can't compromise on one uh to get another. So the design philosophy for link is that it should just work. um you should just be able to install it without using your brain and uh and it should just kind of work right right away. Um there's a lot of tools out there that require a lot of configuration and licorit
