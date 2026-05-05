---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccncna2023.sched.com/event/1R2vg/ux-matters-switching-to-gamma-without-ruining-your-reputation-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=UX+Matters%3A+Switching+to+GAMMA+Without+Ruining+Your+Reputation+CNCF+KubeCon+2023
slides: []
status: parsed
---

# UX Matters: Switching to GAMMA Without Ruining Your Reputation - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Flynn, Buoyant
- Schedule: https://kccncna2023.sched.com/event/1R2vg/ux-matters-switching-to-gamma-without-ruining-your-reputation-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=UX+Matters%3A+Switching+to+GAMMA+Without+Ruining+Your+Reputation+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre UX Matters: Switching to GAMMA Without Ruining Your Reputation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vg/ux-matters-switching-to-gamma-without-ruining-your-reputation-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=UX+Matters%3A+Switching+to+GAMMA+Without+Ruining+Your+Reputation+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vMSmLVaVRT0
- YouTube title: UX Matters: Switching to GAMMA Without Ruining Your Reputation - Flynn, Buoyant
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/ux-matters-switching-to-gamma-without-ruining-your-reputation/vMSmLVaVRT0.txt
- Transcript chars: 33743
- Keywords: controller, policy, gateway, profiles, linker, profile, actually, routes, routing, questions, talking, probably, outbound, updates, retries, trying, linkerd, mostly

### Resumo baseado na transcript

the observant among you will notice that I do not look much like mate um mate could not make it so I am covering this talk for him I'm Flynn I'm a tech evangelist mate is the linkerd maintainer I am a tech evangelist that means I work in marketing which means that if you have complex questions about this presentation that matate did a lot of the heavy lifting for I will absolutely be able to make up answers and they might be correct or they might not but can confirm there are lots of them and I'm probably being really obnoxious to them um but overall we do believe it's possible to do this without completely ruining ruining your reputation we think that's a good thing the user Centric design process is key

### Excerpt da transcript

the observant among you will notice that I do not look much like mate um mate could not make it so I am covering this talk for him I'm Flynn I'm a tech evangelist mate is the linkerd maintainer I am a tech evangelist that means I work in marketing which means that if you have complex questions about this presentation that matate did a lot of the heavy lifting for I will absolutely be able to make up answers and they might be correct or they might not but let me know you know sing out if you have questions we'll we'll figure out what's up um the short summary of this talk about switching to gamma without ruining your reputation is that as of linardy 2.12 we started switching away from some of our custom Linker specific crds to things from Gateway API and this turns out to be hard uh I will leave the question for whether we succeeded in not ruining our reputation for later and we're mostly going to be talking at this point about kind of the nuts and bolts of how we went about it uh again if you're familiar with linkerd you will know that we just shipped 2.14 most of what we're talking about in this talk happened in 2.13 because that's when most of the heavy lifting for the shift happened between 2.13 and 2.14 it was much more incremental stuff as opposed to let's just rip out the underpinnings and put it all back together while we're still supporting everybody so setting the stage uh raise your hand if you don't know what Linker is you are lying Rob okay all right Linker is a service mesh if you imagine your typical kubernetes cluster where you've got microservices all talking to each other then the point of a service mesh is to go in kind of underneath your application and provide you security and reliability and observability uniformally without having to change your application link in does this by sticking sidecars next to each of your application pods the side cars then ruthlessly take over all of your network communication and that allows them to force it to B mtls and to mediate a bunch of things and do retries and cool stuff like that and measure a bunch of things and provide the information to you so you have uniform observability across the whole call graph it's pretty cool most of the time I do this the control plane is an afterthought and I say oh yeah it's the thing that manages all the proxies we're actually going to be talking about some of the details of the control plane in this talk because that's where a lot of the magic happens when you'r
