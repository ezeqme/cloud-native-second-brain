---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Networking"]
speakers: ["Alex Leong", "Buoyant"]
sched_url: https://kccncna2025.sched.com/event/27FXR/its-2025-why-are-you-ok-with-an-insecure-network-alex-leong-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=It%E2%80%99s+2025%3B+Why+Are+You+OK+With+an+Insecure+Network%3F+%F0%9F%A4%AF+CNCF+KubeCon+2025
slides: []
status: parsed
---

# It’s 2025; Why Are You OK With an Insecure Network? 🤯 - Alex Leong, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Alex Leong, Buoyant
- Schedule: https://kccncna2025.sched.com/event/27FXR/its-2025-why-are-you-ok-with-an-insecure-network-alex-leong-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=It%E2%80%99s+2025%3B+Why+Are+You+OK+With+an+Insecure+Network%3F+%F0%9F%A4%AF+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre It’s 2025; Why Are You OK With an Insecure Network? 🤯.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXR/its-2025-why-are-you-ok-with-an-insecure-network-alex-leong-buoyant
- YouTube search: https://www.youtube.com/results?search_query=It%E2%80%99s+2025%3B+Why+Are+You+OK+With+an+Insecure+Network%3F+%F0%9F%A4%AF+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J_Cf9TTOW98
- YouTube title: It’s 2025; Why Are You OK With an Insecure Network? - Alex Leong, Buoyant
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/its-2025-why-are-you-ok-with-an-insecure-network/J_Cf9TTOW98.txt
- Transcript chars: 24232
- Keywords: network, security, connection, authentication, mesh, talking, identity, access, policy, authorization, cost, application, private, connections, cluster, running, typically, allowed

### Resumo baseado na transcript

Um uh but this talk is going to be about network security kind of in general and service mesh can be one part of that or one potential solution to that. So, I'll try to keep my service mesh bias uh to a minimum, but I'll also try to bring you along and show you kind of why I think service mesh is maybe a good choice here, at least in certain circumstances. Um, I'm going to talk about these three pillars of of network security, confidentiality and integrity, authentication and authorization and how what are some different ways we can implement these and make sure that our network is secure in these various different ways. Um, and then I'm going to wrap up by talking about operational concerns because you know unfortunately we live in a reality and we can't just have the perfect security for free. you know, there's always some kind of trade-off or cost benefit we have to think about. Um but when we're talking talking about um an application that's running in Kubernetes, it's behaves very differently than kind of a monolithic single process you know architecture where you have different parts of your application which are calling other parts of your application through

### Excerpt da transcript

Thanks for being here. Uh my name is Alex Leong. I'm a software engineer at a company called Buoyant. We're the creators of the linkd service mesh. Um I've been one of the core link maintainers since the beginning. So I'm a little bit of a service mesh enthusiast. Um uh but this talk is going to be about network security kind of in general and service mesh can be one part of that or one potential solution to that. So, I'll try to keep my service mesh bias uh to a minimum, but I'll also try to bring you along and show you kind of why I think service mesh is maybe a good choice here, at least in certain circumstances. Um, you can find me on GitHub or on the link Slack if you want to uh come chat with me or I'm going to be here at KubeCon all week. I'll be at the link kiosk in the project pavilion if you want to come and chat. Um, so this talk is called it's 2025. Why are you okay with an insecure network exploding head emoji? Uh this is kind of a weird and long name for a talk. And in retrospect, I think maybe what would have been a better name is an even longer one.

Uh which is should you be worried about security and what can you realistically do about it? And what I like about this title instead is that the different parts of the title kind of map to the different parts of the talk. Uh so I'm going to start by talking about the insecure network and what does it mean for a network to be insecure and what kind of things should we be worried about? Uh, one more thing about network security. Um, I'm going to talk about these three pillars of of network security, confidentiality and integrity, authentication and authorization and how what are some different ways we can implement these and make sure that our network is secure in these various different ways. Um, and then I'm going to wrap up by talking about operational concerns because you know unfortunately we live in a reality and we can't just have the perfect security for free. you know, there's always some kind of trade-off or cost benefit we have to think about. Okay, so starting off, we'll talk about the insecure network.

Like, should you be worried about network security? Spoiler alert, yes, you should. Um but when we're talking talking about um an application that's running in Kubernetes, it's behaves very differently than kind of a monolithic single process you know architecture where you have different parts of your application which are calling other parts of your application through things like
