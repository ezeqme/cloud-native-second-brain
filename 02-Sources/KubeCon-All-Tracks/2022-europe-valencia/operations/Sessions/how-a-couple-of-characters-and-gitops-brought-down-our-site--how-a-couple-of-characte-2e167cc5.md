---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Operations"
themes: ["GitOps Delivery"]
speakers: ["Guy Templeton", "Stuart Davidson", "Skyscanner"]
sched_url: https://kccnceu2022.sched.com/event/ytr1/how-a-couple-of-characters-and-gitops-brought-down-our-site-guy-templeton-stuart-davidson-skyscanner
youtube_search_url: https://www.youtube.com/results?search_query=How+a+Couple+of+Characters+%28and+GitOps%29+Brought+Down+Our+Site+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How a Couple of Characters (and GitOps) Brought Down Our Site - Guy Templeton & Stuart Davidson, Skyscanner

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Operations]]
- Temas: [[GitOps Delivery]]
- País/cidade: Spain / Valencia
- Speakers: Guy Templeton, Stuart Davidson, Skyscanner
- Schedule: https://kccnceu2022.sched.com/event/ytr1/how-a-couple-of-characters-and-gitops-brought-down-our-site-guy-templeton-stuart-davidson-skyscanner
- Busca YouTube: https://www.youtube.com/results?search_query=How+a+Couple+of+Characters+%28and+GitOps%29+Brought+Down+Our+Site+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How a Couple of Characters (and GitOps) Brought Down Our Site.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytr1/how-a-couple-of-characters-and-gitops-brought-down-our-site-guy-templeton-stuart-davidson-skyscanner
- YouTube search: https://www.youtube.com/results?search_query=How+a+Couple+of+Characters+%28and+GitOps%29+Brought+Down+Our+Site+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FiEm2zOuHsg
- YouTube title: How a Couple of Characters (and GitOps) Brought Down Our Site - Guy Templeton & Stuart Davidson
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-a-couple-of-characters-and-gitops-brought-down-our-site/FiEm2zOuHsg.txt
- Transcript chars: 43290
- Keywords: cluster, actually, clusters, failure, skyscanner, architecture, change, outage, trying, started, region, traffic, incident, argo, templating, everything, rather, deploy

### Resumo baseado na transcript

it's working hello hello hello gosh there's a lot of you welcome thank you thank you for attending obviously this is the last one between between you and beer so we're trying to keep this as short as possible um welcome to our talk so today uh guy and i we we were talking about how we might uh pitch our talk about cube to kubecon um and we kind of agreed that the vendor talks are great right they're they're good you learn a lot but actually the thing

### Excerpt da transcript

it's working hello hello hello gosh there's a lot of you welcome thank you thank you for attending obviously this is the last one between between you and beer so we're trying to keep this as short as possible um welcome to our talk so today uh guy and i we we were talking about how we might uh pitch our talk about cube to kubecon um and we kind of agreed that the vendor talks are great right they're they're good you learn a lot but actually the thing that brings us to conferences is the war stories right we like to hear from customers we like to hear from companies um who actually talk about the things that they do in production and and the failure states that they've seen in production because we learn from it they learn from it it's great so that that was our pitch we decided to take the second biggest outage revenue-wise of skyscanner and present it to you all right bare bones and everything we're just going to talk about it we're going to talk about how we got there uh we're going to talk about the actual technical failures the the cultural failures all the big mock-ups um with the idea that this is essentially three free therapy for us right we're yeah we've got 20 minutes of you guys just you guys got just sitting listening to us and uh we get to talk about it and if you learn something from it then it means uh it's less of a failure right you've got something from it we've got something from it it's a data point rather than a failure but before we go any further ah i need this thanks okay um we should introduce ourselves i'm the top one my name is stuart davidson i'm a director of engineering at skyscanner i run the production platform tripe which is an entity a group of squads that run almost like a platform as a service so we run all the interest the kind of compute traffic routing observability um incident management everything everything that our product teams use to get their product across the globe and we we do all the kind of heavy lifting underneath uh and i'm guy templeton can you can you hear a guy no all right this is guy templeton he is the the lead kubernetes engineer for skyscanner he's also the the co-lead of um the sig auto scaling um here so that's him there oh no there you go all right this is sky scanner now some of you might not know what sky scanner is skyscanner is a website that puts together a bunch of flights hotels and car hire from about 1200 travel partners across the globe and you want to go somewhere maybe multiple pla
