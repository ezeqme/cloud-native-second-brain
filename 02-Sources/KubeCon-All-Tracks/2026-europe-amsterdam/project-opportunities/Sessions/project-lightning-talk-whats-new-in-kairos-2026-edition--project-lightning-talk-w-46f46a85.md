---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Mauro Morales", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFx4/project-lightning-talk-whats-new-in-kairos-2026-edition-mauro-morales-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%E2%80%99S+New+In+Kairos%2C+2026+Edition+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: What’S New In Kairos, 2026 Edition - Mauro Morales, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mauro Morales, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFx4/project-lightning-talk-whats-new-in-kairos-2026-edition-mauro-morales-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%E2%80%99S+New+In+Kairos%2C+2026+Edition+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What’S New In Kairos, 2026 Edition.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFx4/project-lightning-talk-whats-new-in-kairos-2026-edition-mauro-morales-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%E2%80%99S+New+In+Kairos%2C+2026+Edition+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6MM2LpqDCTI
- YouTube title: Project Lightning Talk: What’s New In Kairos, 2026 Edition - Mauro Morales, Maintainer
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-whats-new-in-kairos-2026-edition/6MM2LpqDCTI.txt
- Transcript chars: 4598
- Keywords: chyros, systems, images, immutable, distributions, thursday, basically, container, focused, moment, distribution, operations, whether, network, devices, access, operating, feature

### Resumo baseado na transcript

Uh my name is Mar Morales and uh I am one of the maintainers at uh the project Kyros. We're currently at version 43 and I bring you some of the updates that have happened. And last but not least, the Chyros operator, which allows you to uh perform system operations from your Kubernetes cluster. So the uh operating system within uh your node can be all done through um Kubernetes. I don't have the time to share that right now, but if you want to come to the booth, uh uh we're definitely um have some time there to tell you why we've uh created this uh minimal upstream uh focused uh system that uh is meant to run uh Kubernetes but uh do it in an image based immutable way.

### Excerpt da transcript

Hello everyone. Yeah. Uh my name is Mar Morales and uh I am one of the maintainers at uh the project Kyros. We are a sandbox project. We're currently at version 43 and I bring you some of the updates that have happened. But first of all uh let me share a little bit what Chyros is. Basically you take Linux systems and you uh through Chyros you transform them into immutable imagebased systems. You can get an Ubuntu and open Zuzi and make them uh immutable. Um it's uh declarative and container based. So you keep using the same tools that you're already using with uh Kubernetes. Um and it's focused on Linux and Kubernetes workloads. Uh at the moment you can pick between K3s and KES by default, but there's also community uh providers that allow you to do also other uh Kubernetes distributions. So if you can see we're very flexible uh in terms of Linux distribution, Kubernetes distributions um and uh the main goal of Chyros is to make uh day2 operations very easy. That means upgrades uh roll backs uh if you need to reset a node uh so that you can do it whether you're on edge, whether you're um on cloud etc.

U two examples that I have uh to share of what our uh community is using Kyros for. Uh on the bottom you can see uh deep network. They uh sell these devices that give you access to their network and you can imagine that if you're giving a device uh with that much access to someone, you really want to make sure that they cannot just uh tamper with the operating system. they are using uh one feature that we call uh trusted boot that uses through TPM measured uh the kernel the infest ensuring that you really only can have the systems that you have signed with your own keys and that's what gives them the um safety to sleep at night you know uh knowing they're not going to get their systems uh attacked u and another example that I have up there is Arya imaging they are uh putting these devices on tractors to uh um analyze uh trees and know where to spray them. And they are using Kyros to be able to uh deliver um on Nvidia uh boards uh to be sure that they always have the same images that they can roll back easily and and do these kind of uh things.

We have a session uh on Thursday if you want to know more about that. I'll have more details later. Uh what's uh kind of newish in the project? Uh first of all, Chyros in it. It's oneliner. You take your docker file, just put what you want uh on this system and it helps you convert that image into a chyros ready image
