---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Zbynek Roubalik", "Red Hat", "Jeff Hollan", "Snowflake"]
sched_url: https://kccncna2022.sched.com/event/182Ml/keda-real-time-and-serverless-scaling-in-kubernetes-zbynek-roubalik-red-hat-jeff-hollan-snowflake
youtube_search_url: https://www.youtube.com/results?search_query=KEDA+-+Real+Time+And+Serverless+Scaling+In+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# KEDA - Real Time And Serverless Scaling In Kubernetes - Zbynek Roubalik, Red Hat & Jeff Hollan, Snowflake

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Zbynek Roubalik, Red Hat, Jeff Hollan, Snowflake
- Schedule: https://kccncna2022.sched.com/event/182Ml/keda-real-time-and-serverless-scaling-in-kubernetes-zbynek-roubalik-red-hat-jeff-hollan-snowflake
- Busca YouTube: https://www.youtube.com/results?search_query=KEDA+-+Real+Time+And+Serverless+Scaling+In+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre KEDA - Real Time And Serverless Scaling In Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ml/keda-real-time-and-serverless-scaling-in-kubernetes-zbynek-roubalik-red-hat-jeff-hollan-snowflake
- YouTube search: https://www.youtube.com/results?search_query=KEDA+-+Real+Time+And+Serverless+Scaling+In+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vjKLbfEZ7MU
- YouTube title: KEDA - Real Time And Serverless Scaling In Kubernetes - Zbynek Roubalik & Jeff Hollan
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keda-real-time-and-serverless-scaling-in-kubernetes/vjKLbfEZ7MU.txt
- Transcript chars: 36710
- Keywords: scaling, metrics, object, rabbitmq, cluster, application, container, messages, events, basically, actually, trying, scaled, external, questions, server, target, already

### Resumo baseado na transcript

okay we are at 2 30 on the dot so I assume we're good to go we are good to go oh hey there's the sign begin hello everyone thank you so much for coming uh I'm very excited to be here today with savionik as well talking about Keda which is the real time and serverless scaling solution for kubernetes a cncf incubations project we'll jump right into it we only have half an hour plus a little bit and we want to leave plenty of time for Q

### Excerpt da transcript

okay we are at 2 30 on the dot so I assume we're good to go we are good to go oh hey there's the sign begin hello everyone thank you so much for coming uh I'm very excited to be here today with savionik as well talking about Keda which is the real time and serverless scaling solution for kubernetes a cncf incubations project we'll jump right into it we only have half an hour plus a little bit and we want to leave plenty of time for Q a thank you to all of you who might be joining virtually hello to you as well I can feel your strength through that little camera in the back can you feel it too oh all right well maybe after we get through intros so very quickly who are we and why are we so excited about Keda so I'm Jeff Holland I am a director of product right now it's snowflake the data Cloud company and prior to snowflake though I worked at Microsoft for about 10 years and part of my time at Microsoft involved a partnership with red hat uh when we created and founded cada is a project this would have been I don't know three or four years ago at this point you can find me on the socials at Twitter or LinkedIn if you have any questions or just want to connect more than happy to chat with you there that Microsoft I was working on a bunch of the serverless tech like Azure functions Azure container apps and so scale was a key part of that which is part of what inspired us to be like oh how could we make scale better in kubernetes all up yeah thanks Jeff uh hello everyone again I'm very happy to be here on stage Jeff he's great and to talk about keraso my name is binyak rubarik I'm based in bernocheck Republic which is in Central Europe in case you don't know uh I'm software engineer working on red hat and as Jeff mentioned we are quite cooperating on Keda for some time uh so I'm kind of maintainer and also active in a commutative Community I'm part of the TOC board and my main focus is kinetic functions is a good project so you should check it out definitely but now let's talk about era great and it's crazy that you flew halfway around the world and are facing jet lag but you were here plenty of time in advance for the session I flew from Seattle and I ran in here five minutes ago so credit to you I guess you did a great job so yeah uh yes uh you can imagine how good of a PM I am if I can't even show up if I like what if what is it PM if not somebody who creates slides and speaking of sites we'll jump right into it so we're going to talk a little bit about what
