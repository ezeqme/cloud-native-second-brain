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
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Lance Ball", "Naina Singh", "Red Hat", "Mauricio Salatino", "Evan Anderson", "VMware"]
sched_url: https://kccncna2022.sched.com/event/182N0/knative-more-than-just-serverless-containers-lance-ball-naina-singh-red-hat-mauricio-salatino-evan-anderson-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Knative%3A+More+Than+Just+Serverless+Containers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Knative: More Than Just Serverless Containers - Lance Ball & Naina Singh, Red Hat; Mauricio Salatino & Evan Anderson, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Lance Ball, Naina Singh, Red Hat, Mauricio Salatino, Evan Anderson, VMware
- Schedule: https://kccncna2022.sched.com/event/182N0/knative-more-than-just-serverless-containers-lance-ball-naina-singh-red-hat-mauricio-salatino-evan-anderson-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Knative%3A+More+Than+Just+Serverless+Containers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Knative: More Than Just Serverless Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182N0/knative-more-than-just-serverless-containers-lance-ball-naina-singh-red-hat-mauricio-salatino-evan-anderson-vmware
- YouTube search: https://www.youtube.com/results?search_query=Knative%3A+More+Than+Just+Serverless+Containers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6rm_-9-30KA
- YouTube title: Knative: More Than Just Serverless Cont...Lance Ball, Naina Singh, Mauricio Salatino & Evan Anderson
- Match score: 0.722
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/knative-more-than-just-serverless-containers/6rm_-9-30KA.txt
- Transcript chars: 33126
- Keywords: function, native, container, cluster, functions, deploy, little, requests, events, create, actually, connection, request, language, containers, question, write, running

### Resumo baseado na transcript

hello everybody and thanks for joining this maintainer track so we're going to talk really about next 35 minutes k more than just sub as container my name is Daniel o I'm not more than happy to be here in a modeling this session I'm also CNF Ambassador I've been a long time the like a uh session tracking and then uh cncf Ambassador and then like a track chair some of stuff of cncf So today we're going to have four great speaker from vmir uh Mario and Ivan demog goods bet us a little bit but I hope that um helped you get a sense of of the function CLI and how that works and how it ties all of the pieces of K native together in some way right we use cloud

### Excerpt da transcript

hello everybody and thanks for joining this maintainer track so we're going to talk really about next 35 minutes k more than just sub as container my name is Daniel o I'm not more than happy to be here in a modeling this session I'm also CNF Ambassador I've been a long time the like a uh session tracking and then uh cncf Ambassador and then like a track chair some of stuff of cncf So today we're going to have four great speaker from vmir uh Mario and Ivan and from redhead and Nina and Lance please Welcome to our great speaker you take the first hello everyone it's good to see so many faces here and as excited as we are about K native so today we are going to talk about more than just sever less containers K native why is K native and I'm going to give it to Evan so so um n also pointed out that we should give you a little preview of what this is going to be because there's kind of three different things that we've squeezed into one um so I'm going to spend five or 10 minutes explaining to you why you might want to use K native then Lance is going to show you for five or 10 minutes how you would use it and how easy it is and then we're going to spend like the remaining time which I guess is probably about 15 or 20 minutes um answering some questions either questions that you've got or we've pre-prepared a list if everyone is so floored by our performance that they haven't thought of anything at all to ask yeah don't expect that will be the case but we going to start with the qu essential question is why is K native so right Evan go ahead oh yeah so next next slide you so the question is why why do you care you know why do we make K native and the really short answer is um so you want to deploy a service on KU look at all the stuff you have to learn on the left hand side if you're building a standard application using best practices if you're building a 12 Factor app you better understand labels you better understand services and deployments and pods and containers and ingresses and you probably want a horizontal pod Auto scaler and maybe there's a couple other resources in there that we haven't talked about um that you're going to need to understand as a developer what is in learning those you have to push something else out of your brain that's probably your business domain Concepts the stuff that gives you value so how can for these common cases we make it simple and easy to run a web application and to build um event driven applications because if you go
