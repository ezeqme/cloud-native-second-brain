---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Jorge Turrado Ferrero", "SCRM Lidl International Hub", "Zbynek Roubalik", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HyTF/unlocking-the-potential-of-keda-new-features-and-best-practices-jorge-turrado-ferrero-scrm-lidl-international-hub-zbynek-roubalik-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+the+Potential+of+KEDA%3A+New+Features+and+Best+Practices+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Unlocking the Potential of KEDA: New Features and Best Practices - Jorge Turrado Ferrero, SCRM Lidl International Hub & Zbynek Roubalik, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jorge Turrado Ferrero, SCRM Lidl International Hub, Zbynek Roubalik, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HyTF/unlocking-the-potential-of-keda-new-features-and-best-practices-jorge-turrado-ferrero-scrm-lidl-international-hub-zbynek-roubalik-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+the+Potential+of+KEDA%3A+New+Features+and+Best+Practices+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Unlocking the Potential of KEDA: New Features and Best Practices.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyTF/unlocking-the-potential-of-keda-new-features-and-best-practices-jorge-turrado-ferrero-scrm-lidl-international-hub-zbynek-roubalik-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+the+Potential+of+KEDA%3A+New+Features+and+Best+Practices+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Db3UcxXbsvw
- YouTube title: Unlocking the Potential of KEDA: New Features and Best Practices - Jorge Ferrero & Zbynek Roubalik
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/unlocking-the-potential-of-keda-new-features-and-best-practices/Db3UcxXbsvw.txt
- Transcript chars: 28848
- Keywords: metrics, scaling, basically, object, another, deployment, application, metric, external, matrix, operator, rabbit, imagine, trigger, certificate, number, actually, messages

### Resumo baseado na transcript

uh we will be talking about Project Era and uh let's start with interactions okay I'm gonna introduce myself I'm Jorge turado the first one obviously doesn't match with my face I'm SRI expert at a little the international Hub AKA smart group I'm Keda maintainer and also I'm cncf Ambassador and Microsoft MVP in developer Technologies and Azure and you have there my connection or my my handle for Twitter GitHub and Linkedin you can send a fire request or write me whatever you want and the state is

### Excerpt da transcript

uh we will be talking about Project Era and uh let's start with interactions okay I'm gonna introduce myself I'm Jorge turado the first one obviously doesn't match with my face I'm SRI expert at a little the international Hub AKA smart group I'm Keda maintainer and also I'm cncf Ambassador and Microsoft MVP in developer Technologies and Azure and you have there my connection or my my handle for Twitter GitHub and Linkedin you can send a fire request or write me whatever you want and the state is yours thank you so my name is robotic I'm from Czech Republic I'm engineer working at redhead in openg serverless team and a long time kind of maintainer I'm also acted in a native community so I'm a member of the creative DLC and let's start it right so uh we will quickly tell you what what is Keda we will describe some new features that we have some best practices and it will see a demo hopefully and before we start actually I would like to ask you a question so who knows Keda in this in his room can you please raise your hand users are you interested on being listed so uh and who are the users of kid actually from Israel okay that's less and is there anybody who is considering using Keda okay cool I will ask after the presentation did a great job so what is so let's describe this on a problem so we have an application this application is some consumer of some data so in this case it could be like a rabbit mqmq consumer it consume messages from an epidemq and I have a problem I would like to Auto scale this application because the application is not doing well with during my setup so what are my options if you use kubernetes there is HPA right so you can Auto scale the kubernetes deployment with HPA but this has some kind of problem in this car in this setup because if you would like to Auto scale our application based on CPU or memory which are the only metrics that HPA provides this might not correlate with the actual needs for our application because our application is consuming messages from some external service in this case from the rabbit so we would like to Auto scale this application based on the based on some metrics from this external service so let's let's see the solution the solution is very simple you plug together in this in this in the setup and what kind of does it just creates metrics from the external endpoint from the rapidm queue and based on those metrics the decision on on actual Auto scaling the this this application deployment let's see
