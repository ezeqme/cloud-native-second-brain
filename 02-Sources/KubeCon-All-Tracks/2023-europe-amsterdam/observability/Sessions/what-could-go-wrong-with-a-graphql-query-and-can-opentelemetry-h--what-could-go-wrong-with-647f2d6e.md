---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability"]
speakers: ["Sonja Chevre", "Ahmet Soormally", "Tyk Technologies"]
sched_url: https://kccnceu2023.sched.com/event/1HyVc/what-could-go-wrong-with-a-graphql-query-and-can-opentelemetry-help-sonja-chevre-ahmet-soormally-tyk-technologies
youtube_search_url: https://www.youtube.com/results?search_query=What+Could+Go+Wrong+with+a+GraphQL+Query+and+Can+OpenTelemetry+Help%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# What Could Go Wrong with a GraphQL Query and Can OpenTelemetry Help? - Sonja Chevre & Ahmet Soormally, Tyk Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sonja Chevre, Ahmet Soormally, Tyk Technologies
- Schedule: https://kccnceu2023.sched.com/event/1HyVc/what-could-go-wrong-with-a-graphql-query-and-can-opentelemetry-help-sonja-chevre-ahmet-soormally-tyk-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=What+Could+Go+Wrong+with+a+GraphQL+Query+and+Can+OpenTelemetry+Help%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre What Could Go Wrong with a GraphQL Query and Can OpenTelemetry Help?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVc/what-could-go-wrong-with-a-graphql-query-and-can-opentelemetry-help-sonja-chevre-ahmet-soormally-tyk-technologies
- YouTube search: https://www.youtube.com/results?search_query=What+Could+Go+Wrong+with+a+GraphQL+Query+and+Can+OpenTelemetry+Help%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ykFvRoe8xzo
- YouTube title: What Could Go Wrong with a GraphQL Query and Can OpenTelemetry Help? - Budhaditya Bhattacharya, Tyk
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/what-could-go-wrong-with-a-graphql-query-and-can-opentelemetry-help/ykFvRoe8xzo.txt
- Transcript chars: 19070
- Keywords: graphql, little, application, actually, hopefully, specific, couple, information, looking, getting, metrics, graphel, challenges, gateway, typically, multiple, response, performance

### Resumo baseado na transcript

we're starting a couple of minutes early because this is after all the last session of the day so um I am expecting the loudest Applause at the end of it but hopefully you'll be with me on this journey over the next 15 to 20 minutes so thank you everyone for being here um this has been a great open tary Community this was my first time speaking in Seattle uh and meeting a lot of the folks that I've seen over LinkedIn or YouTube videos or guub issues

### Excerpt da transcript

we're starting a couple of minutes early because this is after all the last session of the day so um I am expecting the loudest Applause at the end of it but hopefully you'll be with me on this journey over the next 15 to 20 minutes so thank you everyone for being here um this has been a great open tary Community this was my first time speaking in Seattle uh and meeting a lot of the folks that I've seen over LinkedIn or YouTube videos or guub issues in person which is great um so with all that being said um I'm here to talk a little bit about what could go wrong with graphel queries and can open Telemetry help us um I assure you it's not going to be a bummer off a topic at all even though the name might suggest it that way um but um if murph's law suggests that uh whatever can go wrong would potentially go wrong or whatever can happen will happen so let's just be prepared uh when that happens I'm not here I'm not going to be evangelizing graph Cur as a technology so just as a caveat to this uh I'm not trying to sell you on using graphql but if you are already sold onto that or considering doing it then uh there are a couple of things and challenges that you might encounter and we'll go through some of those uh and hopefully we'll see how open Telemetry um can solve or address some of those things either out of the box or potentially with certain manual instrumentations associated with it so with that being said I am Buddha I am a developer Advocate at Ty Ty for those who do not know is a cloud native API management platform powered by and uh an open source API Gateway we are otel native as well as um we are graphical aware as an API Gateway um and I can tell you all about that later on but the idea is we kind of know a little bit more about both of these different worlds some of the challenges some of the solutions associated with it um I'm originally from India um lived most of my life in Singapore currently living in Durham North Carolina big big fan of horror movies but I like my horror on screen and in literature not so much in software as you would see with craft Q today um additionally I'm the chairperson of the open API um open API initiatives business governance board in case you're working in there as well so um just to set the scene for today um I'm looking at two sides of when and how you are sort of promoting or or or deploying an application in this case a graph application to production uh on one side obviously is the development side of thin
