---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Pablo Galego", "VMware"]
sched_url: https://kccnceu2022.sched.com/event/ytpK/digging-into-your-apps-container-image-layers-for-sneaky-vulnerabilities-pablo-galego-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Digging+Into+Your+App%27s+Container+Image+Layers+for+Sneaky+Vulnerabilities+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Digging Into Your App's Container Image Layers for Sneaky Vulnerabilities - Pablo Galego, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Spain / Valencia
- Speakers: Pablo Galego, VMware
- Schedule: https://kccnceu2022.sched.com/event/ytpK/digging-into-your-apps-container-image-layers-for-sneaky-vulnerabilities-pablo-galego-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Digging+Into+Your+App%27s+Container+Image+Layers+for+Sneaky+Vulnerabilities+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Digging Into Your App's Container Image Layers for Sneaky Vulnerabilities.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpK/digging-into-your-apps-container-image-layers-for-sneaky-vulnerabilities-pablo-galego-vmware
- YouTube search: https://www.youtube.com/results?search_query=Digging+Into+Your+App%27s+Container+Image+Layers+for+Sneaky+Vulnerabilities+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Yxh3MBRDVBU
- YouTube title: Digging Into Your App's Container Image Layers for Sneaky Vulnerabilities - Pablo Galego, VMware
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/digging-into-your-apps-container-image-layers-for-sneaky-vulnerabiliti/Yxh3MBRDVBU.txt
- Transcript chars: 14349
- Keywords: vulnerabilities, version, docker, vulnerability, container, layers, plugin, containers, bringing, information, images, library, output, debian, working, source, scanning, critical

### Resumo baseado na transcript

hey so thank you for being here this is my first q com i've been to several amazing talks where the speaker said that it was their first time speaking in public after kobit this is my first time in speaking in public period so let's see how this goes thank you thank you thank you to the cncf um you clearly don't know what you're doing so a bit about me well we are going to see how you can explore the layers of your container images uh to

### Excerpt da transcript

hey so thank you for being here this is my first q com i've been to several amazing talks where the speaker said that it was their first time speaking in public after kobit this is my first time in speaking in public period so let's see how this goes thank you thank you thank you to the cncf um you clearly don't know what you're doing so a bit about me well we are going to see how you can explore the layers of your container images uh to find some sneaky vulnerabilities and previously we'll go through some more common mitigations um very quickly about me i'm pablo i'm a software engineer at vmware i joined like one year ago i started working on containers and helm charts and now i'm more on the java microservices world by the way i i've also studied law before computer engineering so if someone has a problem here in spain talk to me the story behind this talk um was in november of last year when i moved from the team maintaining the vietnamese open source catalogue for those that don't know bitnami offers a huge library of containers and help charts built tested and published by an internal pipeline i'm now part of the team that's developing the product that will supersede this internal pipeline and offer many of its features as a service so in this new team i was tasked to establish a vulnerability baseline for the java microservices under development we needed a way to tell if under a new circumstance we were worsening our security posture and a baseline is what allows you to to make that judgment so we had a very good starting point almost a lab environment we had very a very limited number of micro services built with up-to-date technologies most of them used build packs but as you may know build packs require your app to fit into a set of requirements and when that can happen the classic dockerfile approach is unavoidable so we also had already in place a vulnerability scanning facing ci running aquas tv but it was just informative and non-blocking all of that to achieve a sound goal to have no creative no fixable critical vulnerabilities in production why do i think this entry level talk might be relevant because as you know containers are an excellent tool to ease the [Music] deployment and to its deployment and development but they also bring their unique challenges when it comes to securing them to people that never had before a similar responsibility if you are working on a team that's similar to mine developers are now responsible for the patch
