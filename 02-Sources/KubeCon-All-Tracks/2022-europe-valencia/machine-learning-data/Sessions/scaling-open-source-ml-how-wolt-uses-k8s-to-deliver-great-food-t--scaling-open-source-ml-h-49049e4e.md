---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Stephen Batifol", "Wolt", "Ed Shee", "Seldon"]
sched_url: https://kccnceu2022.sched.com/event/ytkp/scaling-open-source-ml-how-wolt-uses-k8s-to-deliver-great-food-to-millions-stephen-batifol-wolt-ed-shee-seldon
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Open+Source+ML%3A+How+Wolt+Uses+K8s+To+Deliver+Great+Food+to+Millions+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Scaling Open Source ML: How Wolt Uses K8s To Deliver Great Food to Millions - Stephen Batifol, Wolt & Ed Shee, Seldon

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Stephen Batifol, Wolt, Ed Shee, Seldon
- Schedule: https://kccnceu2022.sched.com/event/ytkp/scaling-open-source-ml-how-wolt-uses-k8s-to-deliver-great-food-to-millions-stephen-batifol-wolt-ed-shee-seldon
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Open+Source+ML%3A+How+Wolt+Uses+K8s+To+Deliver+Great+Food+to+Millions+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Scaling Open Source ML: How Wolt Uses K8s To Deliver Great Food to Millions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytkp/scaling-open-source-ml-how-wolt-uses-k8s-to-deliver-great-food-to-millions-stephen-batifol-wolt-ed-shee-seldon
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Open+Source+ML%3A+How+Wolt+Uses+K8s+To+Deliver+Great+Food+to+Millions+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-TsTDaGrjBM
- YouTube title: Scaling Open Source ML: How Wolt Uses K8s To Deliver Great Food to Mill... Stephen Batifol & Ed Shee
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/scaling-open-source-ml-how-wolt-uses-k8s-to-deliver-great-food-to-mill/-TsTDaGrjBM.txt
- Transcript chars: 32578
- Keywords: running, deploy, learning, machine, actually, models, create, pretty, everything, deployment, production, platform, shadow, usually, access, metrics, already, scientists

### Resumo baseado na transcript

all right so yeah today today we're here to talk about how we scale open source machine learning and how we use communities to deliver food to millions of people i'm stephen buttiful i'm a machine learning engineer at walt and i'm here with i'm edgy i'm head of developer relations at company called selden so yeah so maybe for the people that don't know walt we are we started as a food delivery company in helsinki in 2016 and we are now in 23 countries going from norway to

### Excerpt da transcript

all right so yeah today today we're here to talk about how we scale open source machine learning and how we use communities to deliver food to millions of people i'm stephen buttiful i'm a machine learning engineer at walt and i'm here with i'm edgy i'm head of developer relations at company called selden so yeah so maybe for the people that don't know walt we are we started as a food delivery company in helsinki in 2016 and we are now in 23 countries going from norway to japan and then we have millions of users that's like the boring part but the fun part is that we have machine learning and we have a lot of different use cases the first one is supply and demand forecasting the second one is recommended systems then we have logistic optimization then we also have fraud detection and the last one with the longest title situation monitoring inbox prioritization so with a lot of different machine learning use cases we have a lot of different needs and we have to address those needs and the first one the biggest need that you can have usually when you train machine learning is data access how do you access your data how do you make sure that you access it in a secure way but it has to be simple as well we don't want our data scientists to be struggling and to be like okay i need access to that table or that table or that database but struggling for like i don't know days and days and we also don't want them to have access to the whole database that we have and all the all the tables that we have so yeah we want to have that simple and yet secure and then infrastructure as well has it has been told you know scaling is quite hard and then you need infrastructure to scale usually and when you train a model you need some resources you need some computer resources so you're gonna need cpu usually memory as well and then you might also need gpus and you might need one gpu or five gpus or even more so how do you have access to those i'm a big believer that if you need something it should be easy to have access to it so if you need one gpu you should just say okay i want one gpu you should not have to think about all the drivers and everything so yeah we have a whole infrastructure for that and then one part that is very important is fast deployment you know you machine learning is very iterative and if you make it slow for your data scientist to deploy something then usually the whole process is becoming very slow and then instead of taking three months to deploy mo
