---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Stefan Prodan", "Hidde Beydals", "Weaveworks"]
sched_url: https://kccnceu2023.sched.com/event/1HySr/flux-beyond-git-harnessing-the-power-of-oci-stefan-prodan-hidde-beydals-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Flux+Beyond+Git%3A+Harnessing+the+Power+of+OCI+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Flux Beyond Git: Harnessing the Power of OCI - Stefan Prodan & Hidde Beydals, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Stefan Prodan, Hidde Beydals, Weaveworks
- Schedule: https://kccnceu2023.sched.com/event/1HySr/flux-beyond-git-harnessing-the-power-of-oci-stefan-prodan-hidde-beydals-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Flux+Beyond+Git%3A+Harnessing+the+Power+of+OCI+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Flux Beyond Git: Harnessing the Power of OCI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HySr/flux-beyond-git-harnessing-the-power-of-oci-stefan-prodan-hidde-beydals-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Flux+Beyond+Git%3A+Harnessing+the+Power+of+OCI+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gKR95Kmc5ac
- YouTube title: Flux Beyond Git: Harnessing the Power of OCI - Stefan Prodan & Hidde Beydals, Weaveworks
- Match score: 0.768
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/flux-beyond-git-harnessing-the-power-of-oci/gKR95Kmc5ac.txt
- Transcript chars: 28911
- Keywords: flux, container, cluster, artifact, controller, everything, registry, repository, source, whatever, github, terraform, working, inside, instead, changes, change, install

### Resumo baseado na transcript

I'm Stefan for that I'm here with hidea we are both maintainers of flux we both work at weworks and today we are going to talk about Flags the project how is it composed of how we develop it and we are going to talk about the New Direction of where we are taking flux to and that is oci and container Registries without CRT effects and so on so we'll get that started so first an overview of the flux project so flux is split into multiple controllers um

### Excerpt da transcript

I'm Stefan for that I'm here with hidea we are both maintainers of flux we both work at weworks and today we are going to talk about Flags the project how is it composed of how we develop it and we are going to talk about the New Direction of where we are taking flux to and that is oci and container Registries without CRT effects and so on so we'll get that started so first an overview of the flux project so flux is split into multiple controllers um we have this architecture where you can pick and choose flux components based on what you want to do for example if you want to deploy hem releases you'll need Helm controller if you want to do image automation you need to deploy the image automation controller if you want to do for example Progressive delivery and ship traffic from one side to another and have a a better way of safer way of deploying user-facing apps you'll you could use Flagger and so on so flux is not one thing it's made out of many controllers and we have a architecture in place where others can extend flux without modifying its source code so if you want flux if you want to add a new functionality to flux if you want flux to do something else you can use our go SDK build a controller according to our documentation and specification and that's how we can extend flux so flux is kind of different from other Solutions where you have this concept of plugins or you have you change something in how how the main execution happens in flux we don't do that we all these controls are very specialized we don't touch the disk we work on in memory and we we build them with a security first concept and that's why you can't just you know put a back script somewhere or write some python script or whatever and extend flux like that we also have a terraform provider for those that are for example provisioning clusters with terraform after you create your cluster you can also set up flux in a GitHub sway using our terraform provider and of course we have the fluxilli which can't do anything can you can use it to install flux bootstrap flux monitor it debug it and so on so so next I want to share with you some ecosystem news from for the flux project we are very happy to welcome gitlab and orange to our ecosystem gitlab joins Asia AWS and others who are offering Flags to their end users So currently flux is in beta in in gitlab in all the gitlab editions and we are working closely with the giddler team to add great feature to flux and have offered a great expe
