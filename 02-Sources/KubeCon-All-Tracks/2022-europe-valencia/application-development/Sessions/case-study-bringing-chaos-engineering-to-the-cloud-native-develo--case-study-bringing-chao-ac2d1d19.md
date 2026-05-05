---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["Application + Development"]
speakers: ["Uma Mukkara", "ChaosNative", "Ramiro Berrelleza", "Okteto"]
sched_url: https://kccnceu2022.sched.com/event/ytoA/case-study-bringing-chaos-engineering-to-the-cloud-native-developers-uma-mukkara-chaosnative-ramiro-berrelleza-okteto
youtube_search_url: https://www.youtube.com/results?search_query=Case+Study%3A+Bringing+Chaos+Engineering+to+the+Cloud+Native+Developers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Case Study: Bringing Chaos Engineering to the Cloud Native Developers - Uma Mukkara, ChaosNative & Ramiro Berrelleza, Okteto

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[Application + Development]]
- País/cidade: Spain / Valencia
- Speakers: Uma Mukkara, ChaosNative, Ramiro Berrelleza, Okteto
- Schedule: https://kccnceu2022.sched.com/event/ytoA/case-study-bringing-chaos-engineering-to-the-cloud-native-developers-uma-mukkara-chaosnative-ramiro-berrelleza-okteto
- Busca YouTube: https://www.youtube.com/results?search_query=Case+Study%3A+Bringing+Chaos+Engineering+to+the+Cloud+Native+Developers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Case Study: Bringing Chaos Engineering to the Cloud Native Developers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoA/case-study-bringing-chaos-engineering-to-the-cloud-native-developers-uma-mukkara-chaosnative-ramiro-berrelleza-okteto
- YouTube search: https://www.youtube.com/results?search_query=Case+Study%3A+Bringing+Chaos+Engineering+to+the+Cloud+Native+Developers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KSl-oKk6TPA
- YouTube title: Case Study: Bringing Chaos Engineering to the Cloud Native Develo... Uma Mukkara & Ramiro Berrelleza
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/case-study-bringing-chaos-engineering-to-the-cloud-native-developers/KSl-oKk6TPA.txt
- Transcript chars: 27100
- Keywords: engineering, litmus, experiment, application, actually, testing, running, development, getting, experiments, environment, developers, remote, native, workflow, database, production, started

### Resumo baseado na transcript

hello everyone good morning thank you for taking time to be here great to see all of you today we are going to talk about a new topic of interest chaos engineering for developers i am um head of chaos engineering at harness and i'm also co-creator and maintainer of the litmus project which is a cncf incubating project and here we also have ramiro hi everyone happy to be here my name is ramiro verayesa the founder and maintainer of octeto which is a cli tool for remote devon

### Excerpt da transcript

hello everyone good morning thank you for taking time to be here great to see all of you today we are going to talk about a new topic of interest chaos engineering for developers i am um head of chaos engineering at harness and i'm also co-creator and maintainer of the litmus project which is a cncf incubating project and here we also have ramiro hi everyone happy to be here my name is ramiro verayesa the founder and maintainer of octeto which is a cli tool for remote devon vitamins on kubernetes we are here for the next 30 minutes going to talk about how can you apply chaos engineering for the cloud native development ecosystem so before we do that let's quickly talk about what's chaos engineering and a brief introduction to litmus project what can you use litmus project for and then ramiro is going to talk about how some of the developers on their development ecosystem or the cloud platform are using litmus to actually do chaos testing while doing development right so first of all we all know that outages are expensive right we've seen they cause reputational damage financial damage and also you know cause a very hard experience in terms of a user experience network motors code so service reliability is very key for all of us in this era of digital transformation but we all know that services are always built with redundancy and still failures happen that's something that's unavoidable and they cause irreparable damage sometimes so some of the key metrics for all the businesses are how fast you can recover from a fault and how can you delay a potential failure right so you need to be doing continuously whatever possible to get a better reliability out of your code that you are building and you're going to ship so what's the solution a definite a good solution to do this in a very organic way use chaos engineering chaos engineering is the science of breaking things willfully proactively and trying to find weaknesses and fix them you know on an iterative ongoing process and why is chaos engineering more important for cloud native right we know chaos engineering has been there for quite some time uh we've been using but chaos engineering is more relevant uh for cloud native because of two things one you are really looking at a very small tip of the pyramid when you're building code right there are a lot of microservices that you're now dealing with uh underneath your stack and they're also changing very dynamically so just to summarize you're looking at a c
