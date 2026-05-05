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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Justin Santa Barbara", "Google", "Ciprian Hacman", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1YeSj/seamless-multi-cloud-kubernetes-a-practical-guide-justin-santa-barbara-google-ciprian-hacman-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Seamless+Multi-Cloud+Kubernetes%3A+A+Practical+Guide+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Seamless Multi-Cloud Kubernetes: A Practical Guide - Justin Santa Barbara, Google & Ciprian Hacman, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Justin Santa Barbara, Google, Ciprian Hacman, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1YeSj/seamless-multi-cloud-kubernetes-a-practical-guide-justin-santa-barbara-google-ciprian-hacman-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Seamless+Multi-Cloud+Kubernetes%3A+A+Practical+Guide+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Seamless Multi-Cloud Kubernetes: A Practical Guide.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSj/seamless-multi-cloud-kubernetes-a-practical-guide-justin-santa-barbara-google-ciprian-hacman-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Seamless+Multi-Cloud+Kubernetes%3A+A+Practical+Guide+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D0KfsaqLc48
- YouTube title: Seamless Multi-Cloud Kubernetes: A Practical Guide - Justin Santa Barbara & Ciprian Hacman
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/seamless-multi-cloud-kubernetes-a-practical-guide/D0KfsaqLc48.txt
- Transcript chars: 25683
- Keywords: cluster, clusters, traffic, multiple, application, problems, multicluster, clouds, single, region, across, basically, leader, working, running, tooling, everything, probably

### Resumo baseado na transcript

we'll get started uh this is a seamless multicloud kubernetes a practical guide uh I am Justin Santa Barbara I've been a contributor for kuber to kuberar um basically since the start uh and I work at Google hi everyone um my name is cyprien uh I'm a software engineer at Microsoft I'm a contributor for kubernetes and various project linked to it uh since long time ago also um and we're happy to have you here awesome so um one of the things that we're celebrating this year at

### Excerpt da transcript

we'll get started uh this is a seamless multicloud kubernetes a practical guide uh I am Justin Santa Barbara I've been a contributor for kuber to kuberar um basically since the start uh and I work at Google hi everyone um my name is cyprien uh I'm a software engineer at Microsoft I'm a contributor for kubernetes and various project linked to it uh since long time ago also um and we're happy to have you here awesome so um one of the things that we're celebrating this year at at cucon and the various cucon is is 10 years of kubernetes and from the very start kubernetes set out to give application portability um and that means you should be able to take a working application that works on a kubernetes cluster in Cloud a and you should be able to take that same yaml basically and move it over and run it on Cloud B and 10 years in we've basically achieved that you know of course we're still aiming to expand the set of applications that do work well in kubernetes at all and there are still some rough edges but broadly it works um but there's an important detail in that like what we're talking about is one application running on one cluster and so one cloud and one region um it was not really part of the original Mandate of kubernetes to run on Multi one run one application on multiple clusters or on multiple clouds and but what we are going to talk about today is how to effectively climb that pyramid of complexity so that you can get to real multicloud we'll talk about why you might want to and just as importantly why you might not want to do this um I also have a confession like I at least I don't know how you feel thought it was going to be easier to climb this mountain I I think we all in the kubernetes project thought it would be easier like you know the idea was we'd start with one cluster and we would get to multicluster and everything would be joy and happiness and simplicity and and it's proven tougher um so we have recorded a few videos today to like get through all this faster but it's all live if we have more time oring questions afterwards uh we can sort of share you some more stuff um but as we go through this uh this this I think bearing in mind the complexity think about where that complexity line is for you like at what point do you pull the ejection handle and say you know what this is just too complicated and I want to stop for me there's an obvious Sweet Spot um where I think it makes a lot of sense but everyone will have their own you know re
