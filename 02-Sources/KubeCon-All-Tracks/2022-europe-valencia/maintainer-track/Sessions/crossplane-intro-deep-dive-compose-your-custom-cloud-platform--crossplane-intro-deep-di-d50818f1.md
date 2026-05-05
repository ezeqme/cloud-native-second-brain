---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Jared Watts", "Steven Borreli", "Yury Tsarev", "Upbound", "Christopher Haar", "DKB AG"]
sched_url: https://kccnceu2022.sched.com/event/ytuY/crossplane-intro-deep-dive-compose-your-custom-cloud-platform-jared-watts-steven-borreli-yury-tsarev-upbound-christopher-haar-dkb-ag
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+Intro+%26+Deep+Dive+-+Compose+Your+Custom+Cloud+Platform+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Crossplane Intro & Deep Dive - Compose Your Custom Cloud Platform - Jared Watts, Steven Borreli & Yury Tsarev, Upbound; Christopher Haar, DKB AG

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Jared Watts, Steven Borreli, Yury Tsarev, Upbound, Christopher Haar, DKB AG
- Schedule: https://kccnceu2022.sched.com/event/ytuY/crossplane-intro-deep-dive-compose-your-custom-cloud-platform-jared-watts-steven-borreli-yury-tsarev-upbound-christopher-haar-dkb-ag
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+Intro+%26+Deep+Dive+-+Compose+Your+Custom+Cloud+Platform+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Crossplane Intro & Deep Dive - Compose Your Custom Cloud Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuY/crossplane-intro-deep-dive-compose-your-custom-cloud-platform-jared-watts-steven-borreli-yury-tsarev-upbound-christopher-haar-dkb-ag
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+Intro+%26+Deep+Dive+-+Compose+Your+Custom+Cloud+Platform+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xECc7XlD5kY
- YouTube title: Crossplane Intro & Deep Dive - Compose Your Custom Cloud Platform
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/crossplane-intro-deep-dive-compose-your-custom-cloud-platform/xECc7XlD5kY.txt
- Transcript chars: 30050
- Keywords: resource, control, resources, cluster, crossplane, custom, provider, create, providers, managed, platform, composition, manage, remote, created, anything, actually, controller

### Resumo baseado na transcript

yeah i think first of all the thing to say is that i am absolutely shocked uh and grateful as well if the number of people that showed up to this is literally the last session of kubecon eu so thank you very much for showing you must not have a plane that's leaving soon you're probably leaving after one of our speakers who has a plane at seven so let's get this thing going and get get out of here all right so this is the introduction and deep resource right so what a managed resource is it's a kubernetes version of something that's external to the cluster it could be anything in our demos today we're going to talk about cloud resources but if you've been to some of the other talks people

### Excerpt da transcript

yeah i think first of all the thing to say is that i am absolutely shocked uh and grateful as well if the number of people that showed up to this is literally the last session of kubecon eu so thank you very much for showing you must not have a plane that's leaving soon you're probably leaving after one of our speakers who has a plane at seven so let's get this thing going and get get out of here all right so this is the introduction and deep dive session for the cross plane project we are all maintainers and contributors on the project uh we're going to share some of our knowledge and experience with you so first of all what is crossplane just a quick introduction to it you can think of crossplane as being a framework that you can use for building your own cloud native control plane or platform you can do it declaratively where you don't have to write any code to make this happen but then let's also take a step back and say what is a control plane so a lot of good examples of control planes are things like aws or gcp they've been using control planes for years if you ask for a cloud resource in in their backend services they've got a control plane running to do all the orchestration of the machines the storage compute etc to provision and dynamically give you services so that's a control plane kubernetes obviously a control plane as well orchestrating your applications containers pods etc but there's a lot more resources than that right uh so crossplane is something that will help you build your own control plane but with all sorts of resources beyond just you know containers and applications databases caches buckets all sorts of things uh it allows you also to put your own opinion into that control plan we're going to get into a lot of details on that as this is just the first slide but let's think about crossblade as two points of extension so when you're building your control plane on the back end there's all sorts of ways with providers you can extend the control plane and basically anything with an api you can now manage with crossplane you know all the cloud providers on premises services etc then on the front-end side you know you can aggregate these resources together and declaratively say hey this is an api or a you know abstraction that i want to give to my developers to be able to access my control plane so we'll go into the more details about the back end and front end extensions of crossplane as we get into more slides here so right this is p
