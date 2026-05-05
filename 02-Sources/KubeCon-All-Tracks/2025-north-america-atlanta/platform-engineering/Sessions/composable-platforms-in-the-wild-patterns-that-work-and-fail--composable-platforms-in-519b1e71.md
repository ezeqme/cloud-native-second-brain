---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Daniel Bryant", "Syntasso"]
sched_url: https://kccncna2025.sched.com/event/27FcK/composable-platforms-in-the-wild-patterns-that-work-and-fail-daniel-bryant-syntasso
youtube_search_url: https://www.youtube.com/results?search_query=Composable+Platforms+in+the+Wild%3A+Patterns+That+Work+%28and+Fail%29+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Composable Platforms in the Wild: Patterns That Work (and Fail) - Daniel Bryant, Syntasso

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Daniel Bryant, Syntasso
- Schedule: https://kccncna2025.sched.com/event/27FcK/composable-platforms-in-the-wild-patterns-that-work-and-fail-daniel-bryant-syntasso
- Busca YouTube: https://www.youtube.com/results?search_query=Composable+Platforms+in+the+Wild%3A+Patterns+That+Work+%28and+Fail%29+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Composable Platforms in the Wild: Patterns That Work (and Fail).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcK/composable-platforms-in-the-wild-patterns-that-work-and-fail-daniel-bryant-syntasso
- YouTube search: https://www.youtube.com/results?search_query=Composable+Platforms+in+the+Wild%3A+Patterns+That+Work+%28and+Fail%29+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=05AxSXIQz6w
- YouTube title: Composable Platforms in the Wild: Patterns That Work (and Fail) - Daniel Bryant, Syntasso
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/composable-platforms-in-the-wild-patterns-that-work-and-fail/05AxSXIQz6w.txt
- Transcript chars: 34868
- Keywords: platform, platforms, developers, product, safety, engineering, actually, efficiency, components, infrastructure, composable, scalability, blocks, patterns, talking, terraform, everyone, pretty

### Resumo baseado na transcript

It's it's getting pretty late and I know the parties are kicking off soon as well. Uh so I'll introduce myself in just a moment, but we're going to be talking about composable platforms and patterns that uh work and patterns that don't. First I was using um Heroku, then I was doing raw compute kind of primitives, went to MSOS and ultimately to Kubernetes. I've made a bunch of mistakes building platforms, leading teams building platforms, and I've learned a few things hopefully along the way. There's three key layers to the architecture and this is kind of how I hope it comes out right how I overlay them. freaking amazing tool but for certain organizations where we scaled too large we we couldn't customize it in the way we needed to so we moved off again Heroku fantastic tool but there was kind of rigidity there I I couldn't you know at some

### Excerpt da transcript

Welcome everyone. I make that 5:30 and welcome officially to the late shift. I do appreciate everyone turning out. It's it's getting pretty late and I know the parties are kicking off soon as well. Uh so I'll introduce myself in just a moment, but we're going to be talking about composable platforms and patterns that uh work and patterns that don't. I like to start my talks with kind of high level takeaways. Also this time of night kind of primes you what I'm going to be talking about. If you're not interested, I will not be offended if you walk out as well. This will give you an overview. I'm going to pitch the composition is valuable in all three layers of building platforms. The app kind of the UX layer, the portal layer, the core platform, and the infrastructure layer. I'm going to say that each layer or each team teams looking after the layer must own their flow of value. This is key in composition. And when we come to look at sort of metrics around how this is going to work, how good a platform is, we're going to think about speed, safety, efficiency, and scalability.

comp composability, composition is all about APIs, abstraction, and automation. I've got a software engineering background. This comes naturally. I think for many platform engineers, many ops folks I work with, uh, this doesn't come naturally. But again, I've learned much from them. It's a two-way street, right? And finally, I'm going to argue many times, build your platform as a product. This is my my core pitch today really and something I, you know, my career I've really seen the benefit of doing. Just very quickly, this is me at Daniel Bryant UK on most of the interwebs, LinkedIn, GitHub, all the places. Uh, I've had a 20 or so year career starting as a Java developer back in the day for the UK government, hence the accent. Uh, I've gone through all different roles, architect, CTO, built a few platforms. First I was using um Heroku, then I was doing raw compute kind of primitives, went to MSOS and ultimately to Kubernetes. I've made a bunch of mistakes building platforms, leading teams building platforms, and I've learned a few things hopefully along the way.

I love writing. love sharing my knowledge, written a few books, worked some open source projects. Just recently with the awesome team at Cintaso, where I'm currently working, we have published an O'Reilly report about platform as a product. I'll mention a few few sort of things from it along the way, but come along to the boo
