---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Tomer Patel", "Akamai Technologies Inc."]
sched_url: https://kccncna2024.sched.com/event/1i7nh/from-chaos-to-calm-building-a-unified-and-scalable-cicd-pipeline-at-akamai-tomer-patel-akamai-technologies-inc
youtube_search_url: https://www.youtube.com/results?search_query=From+Chaos+to+Calm%3A+Building+a+Unified+and+Scalable+CI%2FCD+Pipeline+at+Akamai+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Chaos to Calm: Building a Unified and Scalable CI/CD Pipeline at Akamai - Tomer Patel, Akamai Technologies Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Tomer Patel, Akamai Technologies Inc.
- Schedule: https://kccncna2024.sched.com/event/1i7nh/from-chaos-to-calm-building-a-unified-and-scalable-cicd-pipeline-at-akamai-tomer-patel-akamai-technologies-inc
- Busca YouTube: https://www.youtube.com/results?search_query=From+Chaos+to+Calm%3A+Building+a+Unified+and+Scalable+CI%2FCD+Pipeline+at+Akamai+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Chaos to Calm: Building a Unified and Scalable CI/CD Pipeline at Akamai.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nh/from-chaos-to-calm-building-a-unified-and-scalable-cicd-pipeline-at-akamai-tomer-patel-akamai-technologies-inc
- YouTube search: https://www.youtube.com/results?search_query=From+Chaos+to+Calm%3A+Building+a+Unified+and+Scalable+CI%2FCD+Pipeline+at+Akamai+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RFVB9CEEn1I
- YouTube title: From Chaos to Calm: Building a Unified and Scalable CI/CD Pipeline at Akamai - Tomer Patel
- Match score: 1.006
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-chaos-to-calm-building-a-unified-and-scalable-ci-cd-pipeline-at-a/RFVB9CEEn1I.txt
- Transcript chars: 28930
- Keywords: performance, engineers, application, talked, configuration, itself, course, production, deployment, process, configurations, deploy, afterwards, environment, talking, ticket, automated, akamai

### Resumo baseado na transcript

okay so hello everyone um today we're going to talk about how we built in Akamai anied and scalable cicd um my name is tomar Patel I'm at Akamai for four years now as senior engineering manager in charge of devops Team uh Big Data team and fullstack um please raise your hand if you like you like Turles or snails in general okay nice me too but it depends how because this is how it looked like our cicd up until an year ago uh which was very tedious

### Excerpt da transcript

okay so hello everyone um today we're going to talk about how we built in Akamai anied and scalable cicd um my name is tomar Patel I'm at Akamai for four years now as senior engineering manager in charge of devops Team uh Big Data team and fullstack um please raise your hand if you like you like Turles or snails in general okay nice me too but it depends how because this is how it looked like our cicd up until an year ago uh which was very tedious very uh very slow didn't work well and until the production came up um it took a lot of time and effort so what is our agenda our main agenda is to talk about who we are as Akamai um we're not just CDN so you'll see it uh our cicd the flow itself and of course what are the take uh the takeovers and action items that you can take out of here so what is Akamai as I said Akamai is not only in CDN um this Akamai is also a security uh company and akami connected Cloud we have we're also a cloud company um this is our Global uh spread you can see that we're all across the board uh with the edge and the CL the AC my connected Cloud as well as um as well as in the application security um you can see we're really scalable we're talking about 40 billion Bots a day attacks and 780 million uh app attacks and even more than that and it's increasing all the time uh each day and day and even uh during um every year so what is our DNA when I'm talking about the DNA is my group's DNA uh we all we have over 97 million lines of code we're talking about 120 uh Engineers uh we're working in uh spark Java um Scala python OJs uh we all the team is complex out of uh developers QA uh operations uh performance Engineers because because of the scalability uh and we run uh on Multi regions multic clouds and in different Cloud uh resources such such as the postgress Kafka uh data breaks uh all all all of this so what what were our problems when we first launched and went into this uh thinking of the new cicd uh because we didn't have any um we had long deployments we we're talking about deployments that took over uh weeks and this is like an Enterprise company so this is why a lot of headaches uh we had a lot of bugs during this deployments uh we worked a lot manually and communicated with other team members and this was a difficult one um and we didn't have history so for example when I deployed something to production I didn't know what was deployed what what happened and so on and so forth so when talking about the solutions on how we wan
