---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Alex Leong", "Buoyant"]
sched_url: https://kccncna2022.sched.com/event/182OJ/overview-and-state-of-linkerd-alex-leong-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Overview+And+State+Of+Linkerd+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Overview And State Of Linkerd - Alex Leong, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Alex Leong, Buoyant
- Schedule: https://kccncna2022.sched.com/event/182OJ/overview-and-state-of-linkerd-alex-leong-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Overview+And+State+Of+Linkerd+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Overview And State Of Linkerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182OJ/overview-and-state-of-linkerd-alex-leong-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Overview+And+State+Of+Linkerd+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BufQKvH6K1Q
- YouTube title: Overview And State Of Linkerd - Alex Leong, Buoyant
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/overview-and-state-of-linkerd/BufQKvH6K1Q.txt
- Transcript chars: 33029
- Keywords: policy, linker, traffic, control, gateway, security, mesh, coming, identity, authorization, little, anything, called, natural, server, routes, question, requests

### Resumo baseado na transcript

hi everyone uh this is overview and state of liberty so welcome um so I'm going to start with show hands sorry to do this but who here has heard the word service mesh before should be everyone because I just said it uh who who could explain what a service mesh is about half the people maybe who has used a service mesh before more people somehow uh who's using a service mesh in production that's still a good number what about who's using Linker D in production still

### Excerpt da transcript

hi everyone uh this is overview and state of liberty so welcome um so I'm going to start with show hands sorry to do this but who here has heard the word service mesh before should be everyone because I just said it uh who who could explain what a service mesh is about half the people maybe who has used a service mesh before more people somehow uh who's using a service mesh in production that's still a good number what about who's using Linker D in production still still pretty good I have to ask this to stroke my ego uh yeah so speaking of my ego my name is Alex I am a Lincoln maintainer I've been working on Linker D since the beginning of Liberty I'm very proud to be part of the project uh liquidy is a very cool project it's used by a lot of different organizations all over the world and has been for a long time uh it's uh we have a very vibrant open source community so if you ever pop into the Lincoln slack or go onto GitHub you'll see lots of issues lots of pull requests lots of activity people helping each other in slack it's uh it's really it's really nice we're a cncf project we are a graduated project um and we're very proud to be there uh so what does Linker D2 so link ready is a service mesh for for those who were uh said they were not able to explain what a service mesh is uh a service mesh or in our case or as we use the term means that there is a sidecar proxy in every pod or in every pod that's part of the service mesh and all Network traffic uh for that pod that is either leaving the Pod or coming in is redirected and intercepted by that proxy and that proxy handles that traffic and is able to add a bunch of functionality there like observability so you can get things like golden metrics for request rate success rate latency Etc you can see your uh service topology because you know who is calling who you can get reliability features like retries and timeouts load balancing traffic shifting a b deploys latency aware load balancing which is a really neat feature so you can shift traffic automatically to replicas that are being faster and shifted away from replicas that are being slower um and then perhaps the most important thing uh transparent mtls between all services on by default so this is the thing that people are usually uh most interested in or or a lot of people kind of come to linkerty or service mesh for first is they want mtls and they don't want to work for it they just want to install ingridi and have it work which is which is wh
