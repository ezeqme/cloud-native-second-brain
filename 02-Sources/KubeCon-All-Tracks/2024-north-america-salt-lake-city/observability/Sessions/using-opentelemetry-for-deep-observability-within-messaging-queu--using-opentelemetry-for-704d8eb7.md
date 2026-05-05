---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Shivanshu Raj Shrivastava", "Ekansh Gupta", "SigNoz"]
sched_url: https://kccncna2024.sched.com/event/1i7li/using-opentelemetry-for-deep-observability-within-messaging-queues-shivanshu-raj-shrivastava-ekansh-gupta-signoz
youtube_search_url: https://www.youtube.com/results?search_query=Using+OpenTelemetry+for+Deep+Observability+Within+Messaging+Queues+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Using OpenTelemetry for Deep Observability Within Messaging Queues - Shivanshu Raj Shrivastava & Ekansh Gupta, SigNoz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Shivanshu Raj Shrivastava, Ekansh Gupta, SigNoz
- Schedule: https://kccncna2024.sched.com/event/1i7li/using-opentelemetry-for-deep-observability-within-messaging-queues-shivanshu-raj-shrivastava-ekansh-gupta-signoz
- Busca YouTube: https://www.youtube.com/results?search_query=Using+OpenTelemetry+for+Deep+Observability+Within+Messaging+Queues+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Using OpenTelemetry for Deep Observability Within Messaging Queues.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7li/using-opentelemetry-for-deep-observability-within-messaging-queues-shivanshu-raj-shrivastava-ekansh-gupta-signoz
- YouTube search: https://www.youtube.com/results?search_query=Using+OpenTelemetry+for+Deep+Observability+Within+Messaging+Queues+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IuOurlfAYhI
- YouTube title: Using OpenTelemetry for Deep Observability Within Messaging Queues - S.R. Shrivastava, E. Gupta
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/using-opentelemetry-for-deep-observability-within-messaging-queues/IuOurlfAYhI.txt
- Transcript chars: 19409
- Keywords: consumer, matrix, messaging, producer, message, partition, messages, receiver, probably, correlation, client, broker, metrics, multiple, correlations, attributes, consumers, brokers

### Resumo baseado na transcript

hi everyone good afternoon and welcome to cubec con North America 2024 I hope everyone is doing well and having fun and have gone through a lot of presentations till now uh and gained some valuable insights so today we are going to talk about messaging cues and uh how we are using open tele for deep insights and observability within messaging cues uh hi I am aans I am a software engineer with signos hello everyone this is shanu I'm a founding engineer at signos and also a cncf

### Excerpt da transcript

hi everyone good afternoon and welcome to cubec con North America 2024 I hope everyone is doing well and having fun and have gone through a lot of presentations till now uh and gained some valuable insights so today we are going to talk about messaging cues and uh how we are using open tele for deep insights and observability within messaging cues uh hi I am aans I am a software engineer with signos hello everyone this is shanu I'm a founding engineer at signos and also a cncf Ambassador also I a member and contributor to open project yeah so just to give a shout out to signos Once uh sigos is a open- source unified observability tool to help each and everyone of you uh yeah let's start so we are going through the talk outline uh we are going to talk about what are messaging cues uh and I am pretty sure that most of you have already used some kind of messaging cues uh such as either Kafka or rabbit mq or stmy or something like that and uh we are also going to talk about where uh all we use it why do we actually use it uh what are the common problems that we face while we are using Kafka or rabbit mq uh why do we think messaging cues are complex and and we will Deep dive into one of the messaging cues which is one of my favorites but not a part of the cncf landscape which is Kafka uh and what we do not see with the Kafka metric although Kafka exposes a lot of metrics but uh we do not have a lot of actual in insights from Kafka metric uh so let's start with what are messaging cues and where do we use it so a general architecture of a messaging cues look like this uh we have a produc producer or multiple producers uh and we have consumers or multiple consumers and in between that we have a Q so what is the producer doing here the producer is doing nothing but sending in messages for the consumer to consume but right now back yeah but right now the consumer is probably not ready to consume these messages uh yeah so there is a queue which stores all these messages uh so that once the conser is ready to uh process these messages the consumer can take a message from the que and process it uh let me give you an example uh so let's say you go to an e-commerce site you do all the payment and then uh the messenger uh just sends in a message to the Quee that yes this is out this should be out for delivery now uh but the consumer is already processing some kind of event due to which it's not able to take in that particular message at that point of time so that uh it wi
