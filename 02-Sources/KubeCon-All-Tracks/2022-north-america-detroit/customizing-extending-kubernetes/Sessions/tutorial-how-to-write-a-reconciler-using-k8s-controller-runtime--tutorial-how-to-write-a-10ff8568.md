---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Runtime Containers", "Kubernetes Core"]
speakers: ["Scott Rigby", "Somtochi Onyekwere", "Niki Manoledaki", "Soulé Ba", "Weaveworks", "Amine Hilaly", "Amazon Web Services"]
sched_url: https://kccncna2022.sched.com/event/182Hg/tutorial-how-to-write-a-reconciler-using-k8s-controller-runtime-scott-rigby-somtochi-onyekwere-niki-manoledaki-soule-ba-weaveworks-amine-hilaly-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+How+To+Write+a+Reconciler+Using+K8s+Controller-Runtime%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tutorial: How To Write a Reconciler Using K8s Controller-Runtime! - Scott Rigby, Somtochi Onyekwere, Niki Manoledaki & Soulé Ba, Weaveworks; Amine Hilaly, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Scott Rigby, Somtochi Onyekwere, Niki Manoledaki, Soulé Ba, Weaveworks, Amine Hilaly, Amazon Web Services
- Schedule: https://kccncna2022.sched.com/event/182Hg/tutorial-how-to-write-a-reconciler-using-k8s-controller-runtime-scott-rigby-somtochi-onyekwere-niki-manoledaki-soule-ba-weaveworks-amine-hilaly-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+How+To+Write+a+Reconciler+Using+K8s+Controller-Runtime%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tutorial: How To Write a Reconciler Using K8s Controller-Runtime!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Hg/tutorial-how-to-write-a-reconciler-using-k8s-controller-runtime-scott-rigby-somtochi-onyekwere-niki-manoledaki-soule-ba-weaveworks-amine-hilaly-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+How+To+Write+a+Reconciler+Using+K8s+Controller-Runtime%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Npvz84HpO3o
- YouTube title: Tutorial: How To Write a Reconciler Using K8s Controller-Runtime!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tutorial-how-to-write-a-reconciler-using-k8s-controller-runtime/Npvz84HpO3o.txt
- Transcript chars: 62551
- Keywords: speaker, controller, object, create, proposal, controllers, condition, delete, actually, update, reconcile, finalizer, reconciliation, function, conditions, builder, status, server

### Resumo baseado na transcript

hello everyone it's now after 4:30 so we are going to go ahead and get started um if you're I hope you saw the first slide or actually this one says it right so if you're looking for this tutorial for the reconciler you're definitely in the right room um and uh you know so I'll just introduce myself first um I'm Scott Rigby I'm in the developer experience I'm a developer experience engineer at we Works um I um I am one of the maintainers of Helm um I Loop is this is this law this Loop right here right that we see on the screen but in practice things are not that simple um today we have built-in controllers for the default kubernetes resources deployments Etc the scheduler is a controller um an

### Excerpt da transcript

hello everyone it's now after 4:30 so we are going to go ahead and get started um if you're I hope you saw the first slide or actually this one says it right so if you're looking for this tutorial for the reconciler you're definitely in the right room um and uh you know so I'll just introduce myself first um I'm Scott Rigby I'm in the developer experience I'm a developer experience engineer at we Works um I um I am one of the maintainers of Helm um I co I maintain I co- maintain the flux community and uh repo and I um uh co-chair the giops working group and I work with open get UPS so that's just a little bit about me I'm really excited to be presenting um with these fine pillows hello everyone um my name is am um and is the the uh AWS I work on ETS and uh open source and kubernetes on my daily work I write controllers or I write generators for controllers at maybe if you've been at the previous stock um so yeah um hi everyone I'm Nikki I'm a software engineer at weave works I'm was also a maintainer of eks CTL you know if you used it um that's really cool and I also write controllers currently also um so I would also say um uh if you're not familiar with the environmental sustainability technical advisory the tag within cncf please check that out Nikki Super Active in there and yes please ask her or any of us questions about that if you're interested in the energy optimization carbon optimization for kubernetes reach out to me anytime hello uh my name is sule I work for vbx as well uh I'm also a flex maintainers I'm the I yeah I'm working on the controllers for Flex hello everyone uh my name isi I'm a developer experien engineer at we Works um I'm also a mainten of notification controller one of the controllers that make up BL CD so for most of this stuff I'll be walking around and if you're following along and you have any issues you could reach out to me and I'll help out thank you best one yeah so just I think the thing to do probably raise your hand or whatever if you need any kind of like hey this didn't set up correctly or whatever and one of us will come back um great so okay so um this is just a very quick overview of like what's happening today um we're going to start with uh we're starting with like a quick set expectation set you know just to let you know like hey what what are we going to go through what are you going to learn um uh and we are that includes a very practical and memorable challenge that this demo has set up around um and also l
