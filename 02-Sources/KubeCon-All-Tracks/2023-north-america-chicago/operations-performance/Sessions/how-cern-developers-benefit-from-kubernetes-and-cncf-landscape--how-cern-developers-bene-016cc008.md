---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Antonio Nappi", "CERN"]
sched_url: https://kccncna2023.sched.com/event/1R2pF/how-cern-developers-benefit-from-kubernetes-and-cncf-landscape-antonio-nappi-cern
youtube_search_url: https://www.youtube.com/results?search_query=How+CERN+Developers+Benefit+from+Kubernetes+and+CNCF+Landscape+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How CERN Developers Benefit from Kubernetes and CNCF Landscape - Antonio Nappi, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Antonio Nappi, CERN
- Schedule: https://kccncna2023.sched.com/event/1R2pF/how-cern-developers-benefit-from-kubernetes-and-cncf-landscape-antonio-nappi-cern
- Busca YouTube: https://www.youtube.com/results?search_query=How+CERN+Developers+Benefit+from+Kubernetes+and+CNCF+Landscape+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How CERN Developers Benefit from Kubernetes and CNCF Landscape.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pF/how-cern-developers-benefit-from-kubernetes-and-cncf-landscape-antonio-nappi-cern
- YouTube search: https://www.youtube.com/results?search_query=How+CERN+Developers+Benefit+from+Kubernetes+and+CNCF+Landscape+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vexXq0_eJl4
- YouTube title: How CERN Developers Benefit from Kubernetes and CNCF Landscape - Antonio Nappi, CERN
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-cern-developers-benefit-from-kubernetes-and-cncf-landscape/vexXq0_eJl4.txt
- Transcript chars: 27420
- Keywords: basically, cluster, application, actually, everything, infrastructure, developers, started, clusters, running, another, argo, update, production, deploy, working, version, change

### Resumo baseado na transcript

hello everyone first of all thank you all for joining uh today to the session how s developers benefit from kubernetes and sanf Landscape uh my name is Antonio nappi I'm computer engineer at s since 2015 I work daily with the kubernetes and Java as you can probably understand from my accent I'm Italian particular from the place where the pizza was born even though I promis to myself that I will try the Chicago one uh so for the people that don't know what is s s is

### Excerpt da transcript

hello everyone first of all thank you all for joining uh today to the session how s developers benefit from kubernetes and sanf Landscape uh my name is Antonio nappi I'm computer engineer at s since 2015 I work daily with the kubernetes and Java as you can probably understand from my accent I'm Italian particular from the place where the pizza was born even though I promis to myself that I will try the Chicago one uh so for the people that don't know what is s s is the European Organization for nuclear research what we do we study fundamental particle how they interact in order to understand the fundamental laws of uh of nature in order to do that we build the largest particle accelerator in the world we call it lhcc that large ad collider is a 27 kilomet ring underground in average more or less 100 meter depth and it's also the place where the worldwide web was invented and we like to say that is a place where we do science for for pece because people from different country different cultural background different religion they all work together in a respectful uh environment and what we don't do we don't do black holes uh as maybe you you could see in in movies or YouTube videos um I mean the agenda of today I'm just going to uh first say what I do atern uh what was our services running on VM models where were which were which were our challenges uh which is now the architecture and all the techniques that we started to adopt since we moved to kubernetes so uh what what I do said uh I'm in a team that is basically um in charge of Hosting critical Java application for the send daily life in particular in different fields so Finance Administration Engineering also we host the single sonon infrastructure of the Wern uh that is based on klook uh so our users are mostly developers from different uh Department as I said and uh identity and access management Engineers um we run more or less more than 80 uh applications mostly Java uh we have more than 3,000 pods more than 400 notes kubernetes notes and around 35 clusters uh how was our life when we were running these services on top of VMS uh everything was working there was not really reason or motivation because something was breaking that we had to move to kubernetes but I mean the M can explain you easily why we we decide to move to kubernetes we were wasting a lot of time in repetitive and easy tasks uh in order also to upgrade and provisioning new infrastructure and also to maintain custom scripts and pupp
