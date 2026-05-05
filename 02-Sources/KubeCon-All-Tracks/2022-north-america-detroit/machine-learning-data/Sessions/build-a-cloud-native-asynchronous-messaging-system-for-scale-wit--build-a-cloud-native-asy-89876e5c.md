---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Madelyn Olson", "Amazon Web Services (AWS)"]
sched_url: https://kccncna2022.sched.com/event/182Hv/build-a-cloud-native-asynchronous-messaging-system-for-scale-with-redis-madelyn-olson-amazon-web-services-aws
youtube_search_url: https://www.youtube.com/results?search_query=Build+a+Cloud+Native+Asynchronous+Messaging+System+For+Scale+With+Redis+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Build a Cloud Native Asynchronous Messaging System For Scale With Redis - Madelyn Olson, Amazon Web Services (AWS)

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Madelyn Olson, Amazon Web Services (AWS)
- Schedule: https://kccncna2022.sched.com/event/182Hv/build-a-cloud-native-asynchronous-messaging-system-for-scale-with-redis-madelyn-olson-amazon-web-services-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Build+a+Cloud+Native+Asynchronous+Messaging+System+For+Scale+With+Redis+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Build a Cloud Native Asynchronous Messaging System For Scale With Redis.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Hv/build-a-cloud-native-asynchronous-messaging-system-for-scale-with-redis-madelyn-olson-amazon-web-services-aws
- YouTube search: https://www.youtube.com/results?search_query=Build+a+Cloud+Native+Asynchronous+Messaging+System+For+Scale+With+Redis+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QnwAITEkvVs
- YouTube title: Build a Cloud Native Asynchronous Messaging System For Scale With Redis - Madelyn Olson
- Match score: 0.99
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/build-a-cloud-native-asynchronous-messaging-system-for-scale-with-redi/QnwAITEkvVs.txt
- Transcript chars: 35271
- Keywords: actually, message, basically, everything, messages, memory, stream, little, consumers, second, talking, ephemeral, capacity, events, called, consuming, consume, authoritative

### Resumo baseado na transcript

uh so hello uh my name is Madeline Olsen I'm a member of the redis open source project I'm also a engineer at AWS and today I'm going to be talking a little bit about how to use redis in Cloud native architectures to build an asynchronous messaging system and before I talk too much about the agenda I like the motivation for this talk is I know a lot of people use radius just kind of like quick show Advance who here is aware of what redis is it's

### Excerpt da transcript

uh so hello uh my name is Madeline Olsen I'm a member of the redis open source project I'm also a engineer at AWS and today I'm going to be talking a little bit about how to use redis in Cloud native architectures to build an asynchronous messaging system and before I talk too much about the agenda I like the motivation for this talk is I know a lot of people use radius just kind of like quick show Advance who here is aware of what redis is it's like everyone who here thinks rice is just a cash so those like it's really tailored for you guys um which is that a lot of people know just like they don't know what else Reds can do and they often think about it's just like an ephemeral data store you throw data in it and it can go away so um the specific use case I'm going to dive deep into today um is the event broker kind of design pattern so I'll start kind of introducing that explain how it works in traditional service oriented architectures fan I'll kind of give a pseudo introduction to redis it seems like most people know so I won't go too deep but kind of talk a little bit about why it's good at what it does um not talk too much about what it is and then kind of put Radisson to this architecture we're talking about and see how it actually kind of fits the that role and then I'll show kind of a simple toy application kind of putting everything together um and I'll close off with some best practices and then we'll hopefully have some time for some q a if people have questions great so um why like what why do people need message Brokers So In traditional service oriented architectures you basically have a lot of different services and they're all talking to each other with tightly coupled apis um this works pretty well um some people I know Amazon is well known for having this very complex service oriented architecture because they used to have this big monolith had lots of problems so they broke everything up so service oriented architecture is great the problem starts to stem when that starts to get very complex right when you have one service calling lots of other services you end up with you know dependency hell and a very high latency as all these services start chaining together um you also start seeing issues with being able to maintain slas as when one of these microservices fail the whole architecture might stop working so the idea behind that um to solve this is like uh either a message brokering architecture so the idea behind here is you do all y
