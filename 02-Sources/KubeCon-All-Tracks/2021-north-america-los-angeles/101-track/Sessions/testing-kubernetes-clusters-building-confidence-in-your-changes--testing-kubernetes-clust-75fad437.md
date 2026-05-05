---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Guy Templeton", "Matteo Ruina", "Skyscanner"]
sched_url: https://kccncna2021.sched.com/event/lV2L/testing-kubernetes-clusters-building-confidence-in-your-changes-guy-templeton-matteo-ruina-skyscanner
youtube_search_url: https://www.youtube.com/results?search_query=Testing+Kubernetes+Clusters+-+Building+Confidence+in+Your+Changes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Testing Kubernetes Clusters - Building Confidence in Your Changes - Guy Templeton & Matteo Ruina, Skyscanner

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Guy Templeton, Matteo Ruina, Skyscanner
- Schedule: https://kccncna2021.sched.com/event/lV2L/testing-kubernetes-clusters-building-confidence-in-your-changes-guy-templeton-matteo-ruina-skyscanner
- Busca YouTube: https://www.youtube.com/results?search_query=Testing+Kubernetes+Clusters+-+Building+Confidence+in+Your+Changes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Testing Kubernetes Clusters - Building Confidence in Your Changes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2L/testing-kubernetes-clusters-building-confidence-in-your-changes-guy-templeton-matteo-ruina-skyscanner
- YouTube search: https://www.youtube.com/results?search_query=Testing+Kubernetes+Clusters+-+Building+Confidence+in+Your+Changes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5YjCjI63gTk
- YouTube title: Testing Kubernetes Clusters - Building Confidence in Your Changes - Guy Templeton & Matteo Ruina
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/testing-kubernetes-clusters-building-confidence-in-your-changes/5YjCjI63gTk.txt
- Transcript chars: 25842
- Keywords: running, clusters, cluster, custom, solution, changes, wanted, options, production, write, framework, images, change, actually, testing, components, scaling, number

### Resumo baseado na transcript

hello everyone and welcome to our talk on testing kubernetes clusters and building confidence in your changes um in terms of what we're going to cover today uh we'll cover a little about us um then we'll go over the problems that we faced and that prompted us to go down this investigation rate and building our own solution and then give an overview of the potential solutions that we looked at uh give you a deep dive into our solution how it works and the the components that we

### Excerpt da transcript

hello everyone and welcome to our talk on testing kubernetes clusters and building confidence in your changes um in terms of what we're going to cover today uh we'll cover a little about us um then we'll go over the problems that we faced and that prompted us to go down this investigation rate and building our own solution and then give an overview of the potential solutions that we looked at uh give you a deep dive into our solution how it works and the the components that we brought together to make it work and then finally cover some dutch's tips and other options for you so in terms of who we are um i'm a guy i'm a principal software engineer at scott scanner um i work um on the teams responsible for uh our shared container platform so and for the most part that's kubernetes um and enabling the rest of the business to build applications on top of that and that operate reliably at scale um in addition to that i'm also a co-chair of kubernetes auto scaling and it could be found on most places on the internet under the handle gj templeton hello everyone thank you for joining us my name is mattel i'm a senior software engineer here at stress camera where i work with guy on keeping our kubernetes infrastructure up and running in the production platform tribe uh you can find me technically on twitter but yeah please look for me on github so um we both write for skyscanner um who are the sky scanner um so we're the travel company that puts you first um we help millions of people millions of people in 52 countries over 30 languages find best travel options for not only flights but also hotels and carhart each month and work with over 1200 travel partners to enable that in terms of kubernetes at skyscannerville um we've been running the case since um 1.6 release and we over that time we have built up the the number of clusters we have to more than 35 production clusters at this point and spread across four different aws regions and then on those clusters we've got 475 and more services and most of them running in multiple clusters multiple regions for improved resilience um to a number of different uh potential scenarios um and in terms of scaling the clusters underneath them we've currently we currently run about 40 000 plus cpu cores across the clusters with about 150 terabytes of ram at any one time as well so what do we want to talk about today well uh if you run kubernetes you're probably aware that it's it's a complex platform let's be honest there are li
