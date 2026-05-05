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
themes: ["AI ML", "Community Governance"]
speakers: ["Roland Huss", "Naina Singh", "Red Hat", "Paul Schweigert", "IBM", "David Protasowski", "VMware", "Mauricio Salatino", "Diagrid"]
sched_url: https://kccnceu2023.sched.com/event/1HyT3/knatives-road-ahead-a-project-update-roland-huss-naina-singh-red-hat-paul-schweigert-ibm-david-protasowski-vmware-mauricio-salatino-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Knative%27s+Road+Ahead%3A+A+Project+Update+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Knative's Road Ahead: A Project Update - Roland Huss & Naina Singh, Red Hat; Paul Schweigert, IBM; David Protasowski, VMware; Mauricio Salatino, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Roland Huss, Naina Singh, Red Hat, Paul Schweigert, IBM, David Protasowski, VMware, Mauricio Salatino, Diagrid
- Schedule: https://kccnceu2023.sched.com/event/1HyT3/knatives-road-ahead-a-project-update-roland-huss-naina-singh-red-hat-paul-schweigert-ibm-david-protasowski-vmware-mauricio-salatino-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Knative%27s+Road+Ahead%3A+A+Project+Update+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Knative's Road Ahead: A Project Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyT3/knatives-road-ahead-a-project-update-roland-huss-naina-singh-red-hat-paul-schweigert-ibm-david-protasowski-vmware-mauricio-salatino-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Knative%27s+Road+Ahead%3A+A+Project+Update+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kjMjOJqg80A
- YouTube title: Knative's Road Ahead: A Project Update - Roland & Naina, Paul, David, Mauricio
- Match score: 0.766
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/knatives-road-ahead-a-project-update/kjMjOJqg80A.txt
- Transcript chars: 35168
- Keywords: function, functions, actually, create, events, native, serving, broker, deploy, eventing, running, cluster, container, little, course, working, developer, pretty

### Resumo baseado na transcript

good to see you all here um I think I'll start with have you all are you anyone using K native can we show a hand okay not you're not using but you have heard of connective ah okay so well this is maintenance track so we would be talking about what K native project has been up to and we'll also talk a little bit about what k-native project is and I'm on stage with my esteemed colleague here I'm Naina Singh I work for Red Hat Paul schweigert

### Excerpt da transcript

good to see you all here um I think I'll start with have you all are you anyone using K native can we show a hand okay not you're not using but you have heard of connective ah okay so well this is maintenance track so we would be talking about what K native project has been up to and we'll also talk a little bit about what k-native project is and I'm on stage with my esteemed colleague here I'm Naina Singh I work for Red Hat Paul schweigert IBM uh Dave produsowski from VMware from Red Hat Maurices and I work for a company called diagram Okay so let's start with what and why K native so the short answer is it makes kubernetes simple and the long answer is it is an open source platform that enables developers to create build deploy and manage workload over kubernetes through an abstraction layer and it can do that in serverless fashion it's just icing on cake so now next question is how so with k-native functions well let me start that K native comprises of independent components that all work together really well so with K native function it lets you create a function in two steps and deploy it on your cloud or cluster um with the key native serving you you can manage your applications that that can scale Up and Down based on demand it also provides you traffic splitting that means you can test some particular new feature without disrupting your users and with connective Eventing it allows you to create the declarative event-driven apps that can respond in real time so to sum it up k-native provides developers or could be a go-to tool choice for developers to create build manage workload of container based applications so I gave a glimpse of what the independent components of K native are but here they are they're serving Eventing and client and we have a CLI that ties it all together and we are going to go a little bit more into what these components can do but serving is I call them that auto magic HTTP Services uh you give us a container in one step we give you the URL K native Eventing is basically a whole gamut of tools or infrastructure if you will that allows you to create event driven apps and creative functions that lets you bring your own code we provide the projects scaffolding the templates and we even take off the building of the container off of your list and gives you the URL directly K native is built on the plugin architecture so as you can see what it means is that you don't need to do something specific for K native it can work with the s
