---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Runtimes"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Daniel Mangum", "Upbound", "Jason Hall", "Chainguard"]
sched_url: https://kccnceu2022.sched.com/event/ytqs/registries-after-dark-part-2-distributed-random-access-merkledags-daniel-mangum-upbound-jason-hall-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Registries+After+Dark%2C+Part+2%3A+Distributed+Random+Access+Merkledags+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Registries After Dark, Part 2: Distributed Random Access Merkledags - Daniel Mangum, Upbound & Jason Hall, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Runtimes]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Spain / Valencia
- Speakers: Daniel Mangum, Upbound, Jason Hall, Chainguard
- Schedule: https://kccnceu2022.sched.com/event/ytqs/registries-after-dark-part-2-distributed-random-access-merkledags-daniel-mangum-upbound-jason-hall-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Registries+After+Dark%2C+Part+2%3A+Distributed+Random+Access+Merkledags+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Registries After Dark, Part 2: Distributed Random Access Merkledags.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqs/registries-after-dark-part-2-distributed-random-access-merkledags-daniel-mangum-upbound-jason-hall-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Registries+After+Dark%2C+Part+2%3A+Distributed+Random+Access+Merkledags+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xt_G-pUArTM
- YouTube title: Registries After Dark, Part 2: Distributed Random Access Merkledags - Daniel Mangum & Jason Hall
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/registries-after-dark-part-2-distributed-random-access-merkledags/Xt_G-pUArTM.txt
- Transcript chars: 32272
- Keywords: memory, instruction, actually, instructions, registries, pointer, registry, program, little, access, components, operations, storing, execute, registers, computers, computing, architecture

### Resumo baseado na transcript

all right hello folks and thank you for coming to this talk i know i'm the last thing standing between you and uh a bunch of awesome gatherings this evening so it means a lot that you're here um also before we start um just wanted to mention uh when you're leaving i'd appreciate if you give a thank you to the av folks in this room they have been doing a great job uh and all the folks in all the rooms so definitely give them a shout out

### Excerpt da transcript

all right hello folks and thank you for coming to this talk i know i'm the last thing standing between you and uh a bunch of awesome gatherings this evening so it means a lot that you're here um also before we start um just wanted to mention uh when you're leaving i'd appreciate if you give a thank you to the av folks in this room they have been doing a great job uh and all the folks in all the rooms so definitely give them a shout out uh when you're leaving today um this talk is called registries after dark part two distributed random access merkle dags my name is dan mangum i work at upbound and i'm a maintainer of the crossplane project and unfortunately jason is unable to be here this week but he worked with me on preparing this and definitely had a large part in it i think he might be actually watching virtually so if you're also watching virtually feel free to bug him about anything i get wrong in this presentation um like i said this is part two and hopefully the clicker works yep it looks like it does so the first part of this was given at kubecon north america a few months ago with john johnson and in that presentation we talked about really how to get things out of container registries we specifically focused on the advantages of pulling by digest and kind of the general structure of how a registry works in this talk we're going to be focusing a lot more on how to get things into the registry specifically some things that you may not expect to put into a registry and why or why not different things would be a good idea to store in a container registry i'm going to be moving pretty fast there's a lot of content in this so stick with me and i'll try to make it interactive as well so feel free to pull out your laptop if you're interested in that so we're going to take a bit of an interesting pattern in this talk we're gonna start off uh back at the very beginning if you will and talk about how computers work in general so if you're sitting in this room or you're watching virtually uh you probably have a laptop in your bag or maybe you're watching this on a laptop um and even you know a laptop which is a pretty similar machine between all the ones we have uh is very different in the internals right there's different components that make up the machine you have discrete processors you might have a cpu a gpu if you have maybe an m1 mac you have a number of processors as well as memory all integrated on the same chip if you have a pc like me you have mo
