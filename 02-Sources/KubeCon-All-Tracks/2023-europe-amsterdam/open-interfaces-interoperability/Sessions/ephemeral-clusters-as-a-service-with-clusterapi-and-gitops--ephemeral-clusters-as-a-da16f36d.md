---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Open Interfaces + Interoperability"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Alessandro Vozza", "Solo.io", "Joaquin Rodriguez", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HyXe/ephemeral-clusters-as-a-service-with-clusterapi-and-gitops-alessandro-vozza-soloio-joaquin-rodriguez-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Ephemeral+Clusters+as+a+Service+with+ClusterAPI+and+GitOps+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Ephemeral Clusters as a Service with ClusterAPI and GitOps - Alessandro Vozza, Solo.io & Joaquin Rodriguez, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alessandro Vozza, Solo.io, Joaquin Rodriguez, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HyXe/ephemeral-clusters-as-a-service-with-clusterapi-and-gitops-alessandro-vozza-soloio-joaquin-rodriguez-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Ephemeral+Clusters+as+a+Service+with+ClusterAPI+and+GitOps+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Ephemeral Clusters as a Service with ClusterAPI and GitOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXe/ephemeral-clusters-as-a-service-with-clusterapi-and-gitops-alessandro-vozza-soloio-joaquin-rodriguez-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Ephemeral+Clusters+as+a+Service+with+ClusterAPI+and+GitOps+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cXIo8C7yWvg
- YouTube title: Ephemeral Clusters as a Service with ClusterAPI and GitOps - Alessandro Vozza & Joaquin Rodriguez
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/ephemeral-clusters-as-a-service-with-clusterapi-and-gitops/cXIo8C7yWvg.txt
- Transcript chars: 22216
- Keywords: cluster, clusters, course, management, actually, classes, prometheus, application, argo, metrics, create, little, thanos, workload, install, deploy, everything, minions

### Resumo baseado na transcript

all right and welcome everybody uh let's get started really quick hi so uh my name is Joaquin Rodriguez I'm a software engineer at Microsoft and I'm here with Alessandro hi welcome it's my first time Mr Speaker so please be be nice to me about developeration at uh okay so let's get started uh with a small intro so uh why are we doing this so it all started with Punch Cards right and you know things have changed since then uh we start looking into terminals Linux you

### Excerpt da transcript

all right and welcome everybody uh let's get started really quick hi so uh my name is Joaquin Rodriguez I'm a software engineer at Microsoft and I'm here with Alessandro hi welcome it's my first time Mr Speaker so please be be nice to me about developeration at uh okay so let's get started uh with a small intro so uh why are we doing this so it all started with Punch Cards right and you know things have changed since then uh we start looking into terminals Linux you know uh app development was a lot different and then we reached kubernetes all right and then we started doing the um like the pushing directly using group CTL apply Etc and then we reached get UPS just I'm just curious by a show of hands how many of you have used get UPS nice Okay now what's next we don't know yet it could be open AI chat GPT we don't know yet but it's kind of cool to be in a place that things are changing things are evolving and you know um yeah so a lot of good things going on right so just to recap with the historical context like I was saying you know back in the day we're doing manual deployments we're doing Cube CTO apply you know this at the time you know it will be there'll be a lot of issues with it right like you know you'll be a lot of human uh errors and inconsistencies things will not scale up this leads into the development of cicd tools like Jenkins and it was good I mean it's still good even these days you know a lot of people use tools like you know Jenkins and workflows and it helped with you know consistency and speed and reliability but it was not enough so now you know we have get Ops we have tools like Argo or flux both of them are great um and yeah so it's you know you have a git-centric approach for doing deployments and you know enhanced collaboration versioning rollbacks you know what what you see is what you get you know doing auditing logging like it's it's just really great so and also because now we have get Ops you know there's a the this evolved into having like an organization like open getups to make sure that there's you know standards and practices and you know it's like a Community Driven approach uh and yeah no this this is this is awesome so um again even with Git Ops you might have some challenges uh some of these challenges are related to scaling observability and deployment Automation and it seems like it's like a like a vicious cycle that the more you scale the more you care about observability and then how do you automate that so tod
