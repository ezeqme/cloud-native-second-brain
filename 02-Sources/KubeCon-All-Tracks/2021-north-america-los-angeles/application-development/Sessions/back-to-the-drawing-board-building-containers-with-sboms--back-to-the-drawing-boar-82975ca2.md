---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Nisha Kumar", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lUzg/back-to-the-drawing-board-building-containers-with-sboms-nisha-kumar-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Back+to+the+Drawing+Board%3A+Building+Containers+with+SBoMs+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Back to the Drawing Board: Building Containers with SBoMs - Nisha Kumar, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Nisha Kumar, VMware
- Schedule: https://kccncna2021.sched.com/event/lUzg/back-to-the-drawing-board-building-containers-with-sboms-nisha-kumar-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Back+to+the+Drawing+Board%3A+Building+Containers+with+SBoMs+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Back to the Drawing Board: Building Containers with SBoMs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzg/back-to-the-drawing-board-building-containers-with-sboms-nisha-kumar-vmware
- YouTube search: https://www.youtube.com/results?search_query=Back+to+the+Drawing+Board%3A+Building+Containers+with+SBoMs+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-vcJdjbZ2rw
- YouTube title: Back to the Drawing Board: Building Containers with SBoMs - Nisha Kumar, VMware
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/back-to-the-drawing-board-building-containers-with-sboms/-vcJdjbZ2rw.txt
- Transcript chars: 15370
- Keywords: container, debian, s-bomb, software, artifacts, generate, python, containers, s-bombs, dependencies, registry, static, metadata, package, distribution, components, providers, expect

### Resumo baseado na transcript

hello and welcome to my talk back to the drawing board building containers with s-bombs i'm nisha kumar and i'm a senior open source engineer at vmware so i'm hoping i'm hoping you got enough messaging about s-bombs and why we need them but if you haven't here are a couple of analogies if you've ever looked at the ingredients on a product's packaging you may be surprised at what you find for example twinkies are not vegetarian and coconut milk conditioner does not have coconut milk as with these that's the end of my demo let's see i have 20 more minutes and i can switch back here hopefully there we go okay so there are certainly a lot of gaps that we need to fill out for this to become a viable or run such that you get the same uh set or similar set of files at the end of it every time you run it and this is a problem that's already solved by linux distro tools and these are good places to look for ideas a lot about these this ecosystem and how turn can help you can read up on the update framework which is the backbone of six door and cosign and of course there's a link to our friends at sixdo okay some resources this demo is

### Excerpt da transcript

hello and welcome to my talk back to the drawing board building containers with s-bombs i'm nisha kumar and i'm a senior open source engineer at vmware so i'm hoping i'm hoping you got enough messaging about s-bombs and why we need them but if you haven't here are a couple of analogies if you've ever looked at the ingredients on a product's packaging you may be surprised at what you find for example twinkies are not vegetarian and coconut milk conditioner does not have coconut milk as with these ingredients a software bill of materials helps you make informed decisions about the distribution and maintenance of the software you consume either as a tool or as a dependency included in the software you distribute you may be asking yourself why do i need to generate s-pumps for containers specifically well this is a picture of a node.js container as you can see there are plenty of components included that may not even be needed by a node.js application one of the my friends on twitter noted that there was a libra office hanging around there somewhere why would node.js require libreoffice who knows now think about the several hundred node.js applications comprising your sas offering the number of software components being consumed becomes exponentially large and it gets very hard to keep track of so many components so naturally they are hidden behind many layers of abstractions a kubernetes distribution consists of hundreds of components but it is a dependency in and of itself for a number of services the abstractions are needed as we cannot keep track of so many components and so many moving parts as developers we focus just on the thing that we are building we know we need certain top level dependencies but those dependencies need dependencies it's turtles all the way down as they say the tools we use to build containers are not repeatable and they're not hermetic building a typical container requires downloading many artifacts from all over the internet and several configuration steps not to mention the volume mounts to the host and copying files from the host into the container many of these steps are not repeatable they are dependent upon the state of the network and the state of the internet and the state of your host machine you may not be able to rebuild the same container a few months ago from when you originally built it s bombs help bring some transparency to the container ecosystem even highlighting what the known unknowns are and what the unknown un
