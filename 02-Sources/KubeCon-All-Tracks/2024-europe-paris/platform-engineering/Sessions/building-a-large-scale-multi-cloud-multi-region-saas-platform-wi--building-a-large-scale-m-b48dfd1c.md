---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sébastien Guilloux", "Elastic"]
sched_url: https://kccnceu2024.sched.com/event/1YeML/building-a-large-scale-multi-cloud-multi-region-saas-platform-with-kubernetes-controllers-sebastien-guilloux-elastic
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Large+Scale+Multi-Cloud+Multi-Region+SaaS+Platform+with+Kubernetes+Controllers+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building a Large Scale Multi-Cloud Multi-Region SaaS Platform with Kubernetes Controllers - Sébastien Guilloux, Elastic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Sébastien Guilloux, Elastic
- Schedule: https://kccnceu2024.sched.com/event/1YeML/building-a-large-scale-multi-cloud-multi-region-saas-platform-with-kubernetes-controllers-sebastien-guilloux-elastic
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Large+Scale+Multi-Cloud+Multi-Region+SaaS+Platform+with+Kubernetes+Controllers+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building a Large Scale Multi-Cloud Multi-Region SaaS Platform with Kubernetes Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeML/building-a-large-scale-multi-cloud-multi-region-saas-platform-with-kubernetes-controllers-sebastien-guilloux-elastic
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Large+Scale+Multi-Cloud+Multi-Region+SaaS+Platform+with+Kubernetes+Controllers+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AYNaaXlV8LQ
- YouTube title: Building a Large Scale Multi-Cloud Multi-Region SaaS Platform with Kubernetes Controllers
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-a-large-scale-multi-cloud-multi-region-saas-platform-with-kub/AYNaaXlV8LQ.txt
- Transcript chars: 30667
- Keywords: controller, controllers, elastic, cluster, clusters, server, little, priority, reconcile, basically, somewhere, objects, actually, object, global, another, desired, search

### Resumo baseado na transcript

so good afternoon everyone I'm Seb I work at elastic um in this session behind a very long title on the slides we're going to talk about how we've been redesigning our Cloud platform at elastic recently um and how we make heavy use of this controller pattern uh that kuet provides so just a little bit of context first so everybody sort of understands what I'm talking about um that's what I work on elastic Cloud so if you don't know where elastic we the company behind elastic search

### Excerpt da transcript

so good afternoon everyone I'm Seb I work at elastic um in this session behind a very long title on the slides we're going to talk about how we've been redesigning our Cloud platform at elastic recently um and how we make heavy use of this controller pattern uh that kuet provides so just a little bit of context first so everybody sort of understands what I'm talking about um that's what I work on elastic Cloud so if you don't know where elastic we the company behind elastic search key and all those products um run a cloud service where you can basically create a nastic stack um as a service by clicking a few buttons uh we run around the world across three different Cloud providers um and across more than 50 regions and we've done that for quite some time now with our own sort of home brew orchestration system which is not kubernetes because it predates kubernetes and now we run more than 600,000 containers in production um so that's what I'm working on and I think at elastic we've been involved in the kinary space for a few years now um two things in particular I can highlight one is our observability solution uh that AR monitoring kubernetes and monitoring your services on kubernetes so we do metrics APM traces and things like that uh so we've been heavy users of kubernetes in that sense like for developing that solution but we've also invested into that project that we like to call the Eck operator so that's an operator that allows you to deploy elastic search uh very easily on your KU cluster I I don't know if people here have used dck yeah cool uh so I've worked on that one for I think the past few years um and so while we were working on that I think we realized that we would really benefit from also relying on communties internally and sort of slowly changing and redesigning our own clad platform to be based on communes because we gained that experience of working with kues working um on developing against kubernetes like building custom controllers and things like that um I think with that experience we also did a few presentations like this one from 2019 that is also about kubernetes controllers and operators if you want to have a look it's on YouTube now and so we kind of know how to use kubernetes now we we're used to it and that's why I think two years ago we made this sort of big decision that we would redesign entirely our Cloud platform and we would really Embrace communities fully like that's where we are headed and we we started to think ab
