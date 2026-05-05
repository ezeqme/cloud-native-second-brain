---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Alexander Matyushentsev", "Akuity"]
sched_url: https://kccncna2024.sched.com/event/1hovt/mastering-applicationset-advanced-argo-cd-automation-alexander-matyushentsev-akuity
youtube_search_url: https://www.youtube.com/results?search_query=Mastering+ApplicationSet%3A+Advanced+Argo+CD+Automation+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Mastering ApplicationSet: Advanced Argo CD Automation - Alexander Matyushentsev, Akuity

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Alexander Matyushentsev, Akuity
- Schedule: https://kccncna2024.sched.com/event/1hovt/mastering-applicationset-advanced-argo-cd-automation-alexander-matyushentsev-akuity
- Busca YouTube: https://www.youtube.com/results?search_query=Mastering+ApplicationSet%3A+Advanced+Argo+CD+Automation+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Mastering ApplicationSet: Advanced Argo CD Automation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hovt/mastering-applicationset-advanced-argo-cd-automation-alexander-matyushentsev-akuity
- YouTube search: https://www.youtube.com/results?search_query=Mastering+ApplicationSet%3A+Advanced+Argo+CD+Automation+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9RvDczVIiS0
- YouTube title: Mastering ApplicationSet: Advanced Argo CD Automation - Alexander Matyushentsev, Akuity
- Match score: 0.85
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/mastering-applicationset-advanced-argo-cd-automation/9RvDczVIiS0.txt
- Transcript chars: 26212
- Keywords: application, applications, create, cluster, generator, clusters, argo, basically, repository, approach, delete, changes, simple, actually, generate, experience, environment, available

### Resumo baseado na transcript

so this is a maintainance talk for Argo project and today we're going to talk about application set so that presentation title is mastering application set and advanced Argo CD Automation and uh I would like to do a quick introduction so my name is Alexander MV I'm a co-founder and Chief Architect at a company called AC and also I maintain Argo CD for like seven years and I'm a lead of Argo CD project and so uh today we are going to talk uh about application set so cross all the requirements that we have for a good management application management solution for argd so um application set is fully G opsed it's literally a custom kubernetes resource stored in a argd namespace it's fully declarative it produces applications reliably uh based on

### Excerpt da transcript

so this is a maintainance talk for Argo project and today we're going to talk about application set so that presentation title is mastering application set and advanced Argo CD Automation and uh I would like to do a quick introduction so my name is Alexander MV I'm a co-founder and Chief Architect at a company called AC and also I maintain Argo CD for like seven years and I'm a lead of Argo CD project and so uh today we are going to talk uh about application set so uh not sure how many of you are argocd administrators and run Argo for your company if you are doing that that talk is for you uh and others can learn about application set and decide if you should use it or not and so here is uh today's agenda I will first describe why application set even exist and what problem is it trying to solve and next I want to introduce solutions that uh we maintainance team and end users created to solve this problem and my main goal here is to give you options and kind of give you a heads up so you can decide if application set is applicable for your case or maybe you should consider a different option or maybe a combination of possible solutions and then finally uh very very quick uh brief overview of application set features and uh real life applications set to give you a taste of what are you going to get into if you decide to use this tool and uh with that we can start from explaining why application set exist and what it does so if you are platform administrator and you install Aro CD for the first time for your organization that's usually how Argo CD UI looks like so it's shiny and new it has one sample application that works and you give it to your end users developers and they start playing with it and uh in a couple months it looks like that so I'm not sure if you can see you know the screenshot but it's actually real screenshot where I just replaced the URL and application names for security reasons but this instance has close to 8,000 applications and some applications are broken because of misconfiguration some actually working and deploying uh infrastructure to production and this is not abnormal so what we learn from our own experience of using cargo CD and uh from end users that applications are very convenient uh because they give this nice grouping logical grouping of pieces of infrastructure that we manage and the more applications we have usually it translates to more kind of usability and predict predictability of Chang es in infrastructure so on
