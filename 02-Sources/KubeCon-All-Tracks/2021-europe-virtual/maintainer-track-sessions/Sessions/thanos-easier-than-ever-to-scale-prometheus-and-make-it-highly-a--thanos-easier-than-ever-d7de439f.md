---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Observability", "SRE Reliability", "Community Governance"]
speakers: ["Giedrius Statkevičius", "Vinted", "Prem Saraswat", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE6O/thanos-easier-than-ever-to-scale-prometheus-and-make-it-highly-available-giedrius-statkevicius-vinted-prem-saraswat-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Thanos%3A+Easier+Than+Ever+to+Scale+Prometheus+and+Make+It+Highly+Available+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Thanos: Easier Than Ever to Scale Prometheus and Make It Highly Available - Giedrius Statkevičius, Vinted & Prem Saraswat; Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Observability]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Giedrius Statkevičius, Vinted, Prem Saraswat, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE6O/thanos-easier-than-ever-to-scale-prometheus-and-make-it-highly-available-giedrius-statkevicius-vinted-prem-saraswat-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Thanos%3A+Easier+Than+Ever+to+Scale+Prometheus+and+Make+It+Highly+Available+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Thanos: Easier Than Ever to Scale Prometheus and Make It Highly Available.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE6O/thanos-easier-than-ever-to-scale-prometheus-and-make-it-highly-available-giedrius-statkevicius-vinted-prem-saraswat-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Thanos%3A+Easier+Than+Ever+to+Scale+Prometheus+and+Make+It+Highly+Available+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mtwwUqeIHAw
- YouTube title: Thanos: Easier Than Ever to Scale Prometheus and Make It Highly Ava... G. Statkevičius & P. Saraswat
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/thanos-easier-than-ever-to-scale-prometheus-and-make-it-highly-availab/mtwwUqeIHAw.txt
- Transcript chars: 14826
- Keywords: thanos, prometheus, storage, object, metrics, blocks, instance, sidecar, component, called, contributor, companies, engine, single, support, easier, retention, issues

### Resumo baseado na transcript

so hello everyone welcome to our talk in this cube con it's called thanos these are the number to scale prometheus and to make it highly available uh my name is guedras and with me i have brown and we will talk about thanos which is a global scalable highly available prometheus solution which provides you unlimited metrics retention so at first we will do a short introduction about what prometheus is what scaling issues it has and then uh we are gonna talk about what has been added to

### Excerpt da transcript

so hello everyone welcome to our talk in this cube con it's called thanos these are the number to scale prometheus and to make it highly available uh my name is guedras and with me i have brown and we will talk about thanos which is a global scalable highly available prometheus solution which provides you unlimited metrics retention so at first we will do a short introduction about what prometheus is what scaling issues it has and then uh we are gonna talk about what has been added to tana since the last presentation at kubecon so at first let's we will introduce ourselves hello my name is prem i am currently a software engineer intern at red hat i'm working with the observability platform team uh i have been an oss contributor like with thanos like from quite some time like uh last year when i uh when i started my gsoc project with them yeah that's all and my name is gadgets i'm a central liability engineer at visited that might not be such a familiar name to you it's just essentially a secondhand fashion marketplace i am part of the observability team there i work on metrics traces blogging and i'm also uh open source software can be turned contributor and a fan so i started in the finance project a few years ago uh as part of my work at my previous workplace and yeah ever since then i am involved in the project and also i contribute and maintain a goal library for and for interacting with grafana so it permits you to uh automate various graphand actions in that type safe manner so if you are ever if you ever want to do such a thing then go to github.com grafana sdk and finally i write about software engineering worthy related topics on my blog at gearhears.com and now we will jump to the site about the pandas project so to give you a short history lesson it's the project started in 2017 at improvable in november of 2017 by bartek and fabian and that was open source from the get-go so over the years it has grown quite a lot nowadays it's a cncf incompetent project just one step away from being a graduated project and being an incubating project means that thanos follows certain standards so for example we are vendor neutral we have a public roadmap uh we review pull requests quite quickly and so on and on top of that we have a quite a vibrant community so since the last cubecon presentation we've gained about 2000 new github stars we've gained 75 new contributors uh since last crypto presentation which means that we've grown about two times since 2019 wh
