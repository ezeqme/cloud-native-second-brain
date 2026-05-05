---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: []
sched_url: https://kccncna2023.sched.com/event/1R2mf/harnessing-argo-flux-the-quest-to-scale-add-ons-beyond-10k-clusters-joaquin-rodriguez-microsoft-priyanka-ravi-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Harnessing+Argo+%26+Flux%3A+The+Quest+to+Scale+Add-Ons+Beyond+10k+Clusters-+Joaquin+Rodriguez%2C+Microsoft+%26+Priyanka+Ravi%2C+Weaveworks+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Harnessing Argo & Flux: The Quest to Scale Add-Ons Beyond 10k Clusters- Joaquin Rodriguez, Microsoft & Priyanka Ravi, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: N/A
- Schedule: https://kccncna2023.sched.com/event/1R2mf/harnessing-argo-flux-the-quest-to-scale-add-ons-beyond-10k-clusters-joaquin-rodriguez-microsoft-priyanka-ravi-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Harnessing+Argo+%26+Flux%3A+The+Quest+to+Scale+Add-Ons+Beyond+10k+Clusters-+Joaquin+Rodriguez%2C+Microsoft+%26+Priyanka+Ravi%2C+Weaveworks+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Harnessing Argo & Flux: The Quest to Scale Add-Ons Beyond 10k Clusters- Joaquin Rodriguez, Microsoft & Priyanka Ravi, Weaveworks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mf/harnessing-argo-flux-the-quest-to-scale-add-ons-beyond-10k-clusters-joaquin-rodriguez-microsoft-priyanka-ravi-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Harnessing+Argo+%26+Flux%3A+The+Quest+to+Scale+Add-Ons+Beyond+10k+Clusters-+Joaquin+Rodriguez%2C+Microsoft+%26+Priyanka+Ravi%2C+Weaveworks+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IPySUmNKbcA
- YouTube title: Harnessing Argo & Flux: The Quest to Scale Add-Ons Beyond 10k C... Joaquin Rodriguez & Priyanka Ravi
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/harnessing-argo-flux-the-quest-to-scale-add-ons-beyond-10k-clusters-jo/IPySUmNKbcA.txt
- Transcript chars: 24112
- Keywords: cluster, add-ons, argo, flux, flamingo, clusters, install, already, production, manage, application, target, dashboard, labels, installed, applications, wanted, manager

### Resumo baseado na transcript

hey everybody uh Welcome to our talk um my name is Hakim Rodriguez I'm a software engineer at uh Microsoft I live in Austin Texas I'm prianka Ravi I also go by Pinky and I am a developer experienc engineer at weor we're the ones that created the um flux project and then donated it to the cncf I'm also um a member of the giops working group so come join us and chat get Ops anytime you want okay so today we'll be talking about cluster add-ons uh we

### Excerpt da transcript

hey everybody uh Welcome to our talk um my name is Hakim Rodriguez I'm a software engineer at uh Microsoft I live in Austin Texas I'm prianka Ravi I also go by Pinky and I am a developer experienc engineer at weor we're the ones that created the um flux project and then donated it to the cncf I'm also um a member of the giops working group so come join us and chat get Ops anytime you want okay so today we'll be talking about cluster add-ons uh we will be providing an introduction about what cluster add-ons are uh we will also be talking about some of the challenges around these uh cluster add-ons and how gitops uh it's a solution uh for maintaining these cluster add-ons and how aroflux and Flamingo Flamingo uh can help us uh scale these add-ons uh we'll be providing a solution diagram and also we'll be doing a quick demo and then we talk about you know scaling and some some other other things so to get started uh uh what's cluster add-ons you might have heard this term uh cluster add-ons are tools um or applications or services that expand the functionality of kubernetes so you can think about a vanilla kubernetes cluster or cluster add-ons are enhancements to these cluster that allows you to do really uh cool things um like I'm mentioning here they are not part of the core kinary system um but they provide essential capabilities um when you think about add-ons there are different uh types of add-ons um for example monitoring and logging uh think about grafana um Prometheus tanos for example um Network and communication uh think about the service measures sto Etc uh security you have your policies uh Opa cerno uh and storage an example could be like grook um why are these important uh they extend the capabilities of kubernetes um they adapt to different use cases so depending what you're doing um you might not need you know certain add-ons so it all really depends uh for example if you're trying to solve a problem around security right and then you want to focus on security related add-ons um or if you care about insights of course you will be looking into the insides uh add-ons such as you know monitoring and and logging um when you're implementing add-ons or um there's some things that you want to consider um the first thing is compat compatibility so you want to make sure that the add-on is compatible uh with your version of kubernetes or if two add-ons are working with each other um that those versions are matching so something to keep in mind uh of co
