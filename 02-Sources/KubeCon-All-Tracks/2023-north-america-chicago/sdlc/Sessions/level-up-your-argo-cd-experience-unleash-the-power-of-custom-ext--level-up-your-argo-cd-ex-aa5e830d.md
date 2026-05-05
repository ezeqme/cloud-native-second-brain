---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "SDLC"
themes: ["GitOps Delivery"]
speakers: ["Remington Breeze", "Akuity", "Leonardo Luz Almeida", "Intuit"]
sched_url: https://kccncna2023.sched.com/event/1R2tS/level-up-your-argo-cd-experience-unleash-the-power-of-custom-extensions-remington-breeze-akuity-leonardo-luz-almeida-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Level+up+Your+Argo+CD+Experience%3A+Unleash+the+Power+of+Custom+Extensions+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Level up Your Argo CD Experience: Unleash the Power of Custom Extensions - Remington Breeze, Akuity & Leonardo Luz Almeida, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Chicago
- Speakers: Remington Breeze, Akuity, Leonardo Luz Almeida, Intuit
- Schedule: https://kccncna2023.sched.com/event/1R2tS/level-up-your-argo-cd-experience-unleash-the-power-of-custom-extensions-remington-breeze-akuity-leonardo-luz-almeida-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Level+up+Your+Argo+CD+Experience%3A+Unleash+the+Power+of+Custom+Extensions+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Level up Your Argo CD Experience: Unleash the Power of Custom Extensions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tS/level-up-your-argo-cd-experience-unleash-the-power-of-custom-extensions-remington-breeze-akuity-leonardo-luz-almeida-intuit
- YouTube search: https://www.youtube.com/results?search_query=Level+up+Your+Argo+CD+Experience%3A+Unleash+the+Power+of+Custom+Extensions+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mRF4cEEMtAg
- YouTube title: Level up Your Argo CD Experience: Unleash the Power of Cu... Remington Breeze & Leonardo Luz Almeida
- Match score: 0.844
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/level-up-your-argo-cd-experience-unleash-the-power-of-custom-extension/mRF4cEEMtAg.txt
- Transcript chars: 31459
- Keywords: extension, argo, application, extensions, resource, request, server, cluster, interface, little, metrix, configuration, backend, timeline, metrics, actually, called, specific

### Resumo baseado na transcript

today we're going to be talking about uh how you can improve your argd experience uh with UI extensions uh but before I get to that I'd like to introduce myself uh my name is Remington Breeze I'm a software engineer at a uh and I'm also an argd uh project maintainer Leo would you like to introduce yourself sure hi everyone uh my name is leonarda I usually go by Leo I am a staff software developer add into it and I am one of the uh Main engers

### Excerpt da transcript

today we're going to be talking about uh how you can improve your argd experience uh with UI extensions uh but before I get to that I'd like to introduce myself uh my name is Remington Breeze I'm a software engineer at a uh and I'm also an argd uh project maintainer Leo would you like to introduce yourself sure hi everyone uh my name is leonarda I usually go by Leo I am a staff software developer add into it and I am one of the uh Main engers in the Argo C and Argo rollouts projects thanks Leo all right um so before we get started I think uh it's important to understand why we decided to make the Argos CD user interface uh more extensible in the first place um so one of the core tenets of our development philosophy uh for the Argo CD product um has always been Focus um so we want to prioritize core functionality um without adding a lot of unnecessary Cru and bloat um but over time we kind of noticed that more and more people adopted argd and some more unique use cases arose that needed uh unique solutions that we couldn't just put into the main project um so one of these use cases that we found ourselves in a pretty unique situation to solve was a lot of folks run Argo CD with Argo rollouts um and they wanted more information about their Argo rollouts at a glance uh in the user interface um but we didn't want to tightly couple Argo CD with Argo rollouts uh so to solve this we built extensions uh to try to keep delivering what we think is a worldclass uh developer experience to folks that just want to use Argos CD by itself um but also allowing users uh with those more complex needs uh an option to adapt the user interface to meet those needs um so there are two sections of today's talk um I'm going to be discussing the first uh that's going to that's uh standard UI extensions and then Leo's going to go over the second part which is is proxy extensions uh a different type of extension uh so first I want to briefly go over uh each type of extension so that you know what to look for when I give my demo uh and then in that demo uh I'm going to first show you where each type of extension gets installed to uh and how you can use them and then I'll move to the main uh main subjects of my my part of the presentation so the first is rollets extension uh and the timeline extension so I'm I'm pretty excited to show you the uh timeline extension today uh it's in develop M and will be released soon um and it takes advantage of an improvement to the extension extensions
