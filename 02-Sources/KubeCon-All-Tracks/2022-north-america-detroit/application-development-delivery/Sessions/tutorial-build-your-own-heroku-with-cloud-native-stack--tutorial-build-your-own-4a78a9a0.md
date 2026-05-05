---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Application + Development + Delivery"
themes: ["GitOps Delivery"]
speakers: ["Muvaffak Onus", "Upbound", "Sidarta Aguiar de Oliveira", "Grupo Boticário"]
sched_url: https://kccncna2022.sched.com/event/182FG/tutorial-build-your-own-heroku-with-cloud-native-stack-muvaffak-onus-upbound-sidarta-aguiar-de-oliveira-grupo-boticario
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Build+Your+Own+Heroku+With+Cloud+Native+Stack+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tutorial: Build Your Own Heroku With Cloud Native Stack - Muvaffak Onus, Upbound & Sidarta Aguiar de Oliveira, Grupo Boticário

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Muvaffak Onus, Upbound, Sidarta Aguiar de Oliveira, Grupo Boticário
- Schedule: https://kccncna2022.sched.com/event/182FG/tutorial-build-your-own-heroku-with-cloud-native-stack-muvaffak-onus-upbound-sidarta-aguiar-de-oliveira-grupo-boticario
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Build+Your+Own+Heroku+With+Cloud+Native+Stack+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tutorial: Build Your Own Heroku With Cloud Native Stack.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182FG/tutorial-build-your-own-heroku-with-cloud-native-stack-muvaffak-onus-upbound-sidarta-aguiar-de-oliveira-grupo-boticario
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Build+Your+Own+Heroku+With+Cloud+Native+Stack+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3Aw60VXVMu8
- YouTube title: Tutorial: Build Your Own Heroku With Cloud... - Muvaffak Onus, & Sidarta Oliveira, Grupo Boticário
- Match score: 0.798
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tutorial-build-your-own-heroku-with-cloud-native-stack/3Aw60VXVMu8.txt
- Transcript chars: 51584
- Keywords: create, backstage, application, template, github, bucket, argo, templates, infrastructure, created, cluster, heroku, essentially, actions, platform, actually, developers, change

### Resumo baseado na transcript

hello everyone um we're getting started slowly so this presentation is about we're going to build our own hiroku with Cloud native stack which is essentially like cross-playing backstage and Argo CD and some bit of like you know git repository of course um so this is kind of like what we're going what we're going to go through the first we're going to talk about like you know the Heroku experience and like you know what they give you and then architecture of our solution that will do like and again we try to get as minimal information required you see there's no VPC ID nurse no even Security Group anything so they choose the engine type so let's say I want to say I create a postgres and the version and I can

### Excerpt da transcript

hello everyone um we're getting started slowly so this presentation is about we're going to build our own hiroku with Cloud native stack which is essentially like cross-playing backstage and Argo CD and some bit of like you know git repository of course um so this is kind of like what we're going what we're going to go through the first we're going to talk about like you know the Heroku experience and like you know what they give you and then architecture of our solution that will do like you know that will give you a similar experience and then we have this Hands-On tutorial that we will write code and like you know write yaml see it all in action and then a Grupo butchicario who is a big company they have this setup in their production with lots of like you know Crosman resources and different configurations and they will they're going to do a demo as a he's going to do the demo as well cool um yeah well I'm wafak I am an engineer at upbound and maintain a cross plane I'm the tech lead of the control plane Squad that maintains cross-bit and providers I'm director of infrastructure and Cloud at group yep cool um so the Heroku experience right so hiroku is you know even hiroku was there even before Ducker uh he came out and like you know their concept of like you know that is like you have just have a git repo you make code changes kid push and everything is live right and on top of that they've got this like you know metrics and activity and like you know you just write code comment and watch it live and what you get from them is like deployment and then scaling and monitoring and some of the security guard rails that they have in place however it's it's not as flexible like the more opinionated you get the more like you know the less flexible the flexibility you can provide to your users and customers so a lot of companies they start with hiroku but everyone knows like you know they're going to have grown Heroku right um so what you don't get from Heroku and one of the some of the reasons that you would not continuously get is that they don't deploy stuff in your own internal Network because like you know it's all in the in their accounts and like they're essentially a hosting service right a cloud service some extent and they don't allow you to use their own cloud accounts and complex applications developed by multiple teams for example if you want to have like lots of microservices some like Auto scaling with AWS like Advanced scenarios essentially wit
