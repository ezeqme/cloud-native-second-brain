---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "SRE Reliability", "Community Governance"]
speakers: ["Stefan Prodan"]
sched_url: https://kccnceu2024.sched.com/event/1YhhG/gitops-continuous-delivery-at-scale-with-flux-stefan-prodan
youtube_search_url: https://www.youtube.com/results?search_query=GitOps+Continuous+Delivery+at+Scale+with+Flux+CNCF+KubeCon+2024
slides: []
status: parsed
---

# GitOps Continuous Delivery at Scale with Flux - Stefan Prodan

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Stefan Prodan
- Schedule: https://kccnceu2024.sched.com/event/1YhhG/gitops-continuous-delivery-at-scale-with-flux-stefan-prodan
- Busca YouTube: https://www.youtube.com/results?search_query=GitOps+Continuous+Delivery+at+Scale+with+Flux+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre GitOps Continuous Delivery at Scale with Flux.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhhG/gitops-continuous-delivery-at-scale-with-flux-stefan-prodan
- YouTube search: https://www.youtube.com/results?search_query=GitOps+Continuous+Delivery+at+Scale+with+Flux+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JFLNFJT59DY
- YouTube title: GitOps Continuous Delivery at Scale with Flux - Stefan Prodan
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/gitops-continuous-delivery-at-scale-with-flux/JFLNFJT59DY.txt
- Transcript chars: 30338
- Keywords: flux, controller, events, source, cluster, controllers, deploy, hundreds, release, little, another, everything, thousands, single, control, upgrade, releases, clusters

### Resumo baseado na transcript

hello everyone my name is Stefan pran I'm a fluxcore maintainer for many years now and very happy to be here with you uh I have some exciting news about the flux project Ro map included in this presentation so half of it will be we talking about uh scaling flux and the different ways of doing that and hopefully the other half I'll have enough time to go over the um road map for this year so let's get started with what's uh flux every year I'm changing a

### Excerpt da transcript

hello everyone my name is Stefan pran I'm a fluxcore maintainer for many years now and very happy to be here with you uh I have some exciting news about the flux project Ro map included in this presentation so half of it will be we talking about uh scaling flux and the different ways of doing that and hopefully the other half I'll have enough time to go over the um road map for this year so let's get started with what's uh flux every year I'm changing a little bit the definition flux is so many things so this is what uh what I'm going to say today uh the idea I'm trying to send here with you know flag for foundation layer for continuous delivery platforms is that flux is not the platform uh it's not an end product it's not something you go there and you know use it directly it's best when you integrate flux with your own things and you build your own abstractions on top of flux um from a pure technical perspective flux is a kubernetes extension and extends kubernetes in many many ways it's 13 crds I don't know maybe we should stop but I don't don't like 30 so it will watch just one next year and yeah six controllers uh that doesn't mean you have to use all of this or the the minimum let's say flux deployment requires you to understand uh two crds you have to create two custom resources let's say uh get repo customization and you can use only from the six controllers two controllers but given that almost all of you are using Helm you'll definitely need a third controller which is Helm controller and you should probably be interested when flux fails so then you'll need notification controller and maybe you want to fully automate your pipelines and when you deploy a new Helm chart your container registry or or when you build a new uh app image a new container image maybe you want to fully automate that on your staging clusters and when you are doing that you'll need the image automation controller so that's how you get to the hall of flux but flux was designed to be extensible so it's not only these controllers you can add more things to it for example now there is called the tofu controllers there is a cloud formation controller uh and so on so we we've created an SDK which is called the gitops toolkit it's all written in go flux is all of go goang so you can use this SDK to write your own controllers from a security standpoint of view we we decided when we created uh flux version two 3 years ago that we are not going to build flux around the idea of plugins
