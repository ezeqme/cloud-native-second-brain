---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Zbynek Roubalik", "Red Hat", "Jorge Turrado", "Docplanner Tech"]
sched_url: https://kccnceu2022.sched.com/event/ytmZ/kubernetes-event-driven-autoscaling-with-keda-zbynek-roubalik-red-hat-jorge-turrado-docplanner-tech
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Event-driven+Autoscaling+with+KEDA+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes Event-driven Autoscaling with KEDA - Zbynek Roubalik, Red Hat & Jorge Turrado, Docplanner Tech

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Zbynek Roubalik, Red Hat, Jorge Turrado, Docplanner Tech
- Schedule: https://kccnceu2022.sched.com/event/ytmZ/kubernetes-event-driven-autoscaling-with-keda-zbynek-roubalik-red-hat-jorge-turrado-docplanner-tech
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Event-driven+Autoscaling+with+KEDA+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes Event-driven Autoscaling with KEDA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytmZ/kubernetes-event-driven-autoscaling-with-keda-zbynek-roubalik-red-hat-jorge-turrado-docplanner-tech
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Event-driven+Autoscaling+with+KEDA+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vDMLswzc9tI
- YouTube title: Kubernetes Event-driven Autoscaling with KEDA - Zbynek Roubalik & Jorge Turrado
- Match score: 0.83
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-event-driven-autoscaling-with-keda/vDMLswzc9tI.txt
- Transcript chars: 29515
- Keywords: basically, scaling, deployment, metrics, application, object, metric, rabbit, already, trigger, important, another, messages, external, custom, cluster, server, specify

### Resumo baseado na transcript

hello everybody uh we're gonna get starting our next session so hi everybody my name is danielle i'm cncf ambassador i'm so happy to be here as a moderate this session today so i'm really happy i mean uh back to the return i mean in person event since pandemi so today uh we're gonna talk a little bit about next session as you can see the kubernetes evangelion auto scary cater so please welcome our next great speaker uh jorge from uh dark planner i'm sorry my bad pronunciation

### Excerpt da transcript

hello everybody uh we're gonna get starting our next session so hi everybody my name is danielle i'm cncf ambassador i'm so happy to be here as a moderate this session today so i'm really happy i mean uh back to the return i mean in person event since pandemi so today uh we're gonna talk a little bit about next session as you can see the kubernetes evangelion auto scary cater so please welcome our next great speaker uh jorge from uh dark planner i'm sorry my bad pronunciation spanish and there's v-neck from the red head and the principal software engineer and a please welcome okay first of all thanks to all for staying here we will try to teach us to be funny and just share the knowledge we are gonna talk about kubernetes event drive and auto scaling aka keda and first of all who am i i'm jorge dorado i'm an experiment of planner tech i'm one of kedah maintainer board and also microsoft mvp in developer technologies and you can see my social media networks there yes if you want to write me make me any question you want no problem at all and now my fault spinyek will introduce pizza hey my name is vinayak robotic i know the name is pretty hard to pronounce but both guys did a pretty good job so that's fine i'm from czech republic i'm a software internet third hat and i'm working on openshift serverless which is native stuff and i'm also kidding maintainer and yeah we can go ahead so today we will talk about kedar so this is the agenda and we can start so basically what is kedar what is the project what is the main goal of the project if there is just one sentence one thing that you need to know after this presentation is that we are really trying to make kubernetes even driven auto scaling that simple so probably maybe we can finish the presentation what do you think okay we have a lot of attendees please work a bit more they want to learn a bit more let's continue i don't know let's try to do it okay okay okay so i'll try something so what is the use case so let's say that you have very simple application it's a consumer application that consume messages from some external service let's say you have a kafka consumer application that consume messages from kafka topic and you would like to auto scale this application so how you can do that on kubernetes you have hpa right but with hpa the options are you can scale the application based on cpu or scaled application based on memory but now it is even driven world right everything is 7-driven so this might not
