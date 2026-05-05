---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Zbynek Roubalik", "Kedify"]
sched_url: https://kccncna2023.sched.com/event/1R2nn/exploring-kedas-graduation-and-advancements-in-event-driven-scaling-zbynek-roubalik-kedify
youtube_search_url: https://www.youtube.com/results?search_query=Exploring+KEDA%27s+Graduation+and+Advancements+in+Event-Driven+Scaling+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Exploring KEDA's Graduation and Advancements in Event-Driven Scaling - Zbynek Roubalik, Kedify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Zbynek Roubalik, Kedify
- Schedule: https://kccncna2023.sched.com/event/1R2nn/exploring-kedas-graduation-and-advancements-in-event-driven-scaling-zbynek-roubalik-kedify
- Busca YouTube: https://www.youtube.com/results?search_query=Exploring+KEDA%27s+Graduation+and+Advancements+in+Event-Driven+Scaling+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Exploring KEDA's Graduation and Advancements in Event-Driven Scaling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nn/exploring-kedas-graduation-and-advancements-in-event-driven-scaling-zbynek-roubalik-kedify
- YouTube search: https://www.youtube.com/results?search_query=Exploring+KEDA%27s+Graduation+and+Advancements+in+Event-Driven+Scaling+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wYQ2cvSj6os
- YouTube title: Exploring KEDA's Graduation and Advancements in Event-Driven Scaling - Zbynek Roubalik, Kedify
- Match score: 0.934
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/exploring-kedas-graduation-and-advancements-in-event-driven-scaling/wYQ2cvSj6os.txt
- Transcript chars: 35448
- Keywords: scaling, basically, application, metrics, metrix, object, external, replicas, coming, actually, messages, useful, operator, solution, metric, specify, trying, cluster

### Resumo baseado na transcript

uh hello everybody uh I'm glad to see you uh here in this room uh today we're going to spend next half an hour talking about K and uh you know we should probably get to each other a little bit more so uh I would like to ask are there any K users that are using K in production I can see a bunch of people cool and uh is there anybody who doesn't know what K is or maybe just you know know the name Auto scaring whatever

### Excerpt da transcript

uh hello everybody uh I'm glad to see you uh here in this room uh today we're going to spend next half an hour talking about K and uh you know we should probably get to each other a little bit more so uh I would like to ask are there any K users that are using K in production I can see a bunch of people cool and uh is there anybody who doesn't know what K is or maybe just you know know the name Auto scaring whatever but you know don't know the details okay okay some also some newcomers this is great so uh now it's my turn so my name is balik I know the name is pretty hard to pronounce so don't feel bad about it uh I'm based in Czech Republic Europe uh I've been around kubernetes and open source for many years I'm Microsoft MVP uh and uh while I'm here today I'm longtime K maintainer so basically I'm with the with the project since the beginning uh and finally uh just a few weeks ago we started a company around K called kifi so I'm the CTO there and you know and we try to support the project and help our customers but today I'm not going to talk about the company I would like to talk about the project so uh you know today I'm wearing my maintainers head so uh I should probably take off this this one right uh and uh let's get started so first I will uh you know maybe wa wait a little bit because there are more people coming but basically I will try to explain what K is what we are trying to achieve what is what is the vision what is the idea maybe talk about like some Advanced features about some you know interesting features that are in K so and uh then I will cover some tips and best practices so you can use ska like the best way uh best way it could be so it is you know working well your environment uh short demo and uh I will also quickly talk about about the future of the project and we trying to trying to do in the future so I can see that the people are coming okay this is great so actually let me start with a short story so we are in this room and uh imagine that there is a bar in this room so probably somewhere around here I'm the bartender uh I like beer you know so I'm serving a good beer uh and so I have a few few tabs at the bar and I'm serving one Tab and uh you know giving you uh good beer so maybe you know this guy in the in the front row would like to have a beer so he's coming to the to the bar I'm giving him the the beer this is great maybe after some time you all of you will learn that okay this beer is very great so I would like to have
