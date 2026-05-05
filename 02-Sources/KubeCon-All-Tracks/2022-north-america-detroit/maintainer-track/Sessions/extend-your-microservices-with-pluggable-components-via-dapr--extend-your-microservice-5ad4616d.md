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
themes: ["AI ML", "Community Governance"]
speakers: ["Artur Souza", "Microsoft", "Yaron Schneider", "Diagrid"]
sched_url: https://kccncna2022.sched.com/event/182P8/extend-your-microservices-with-pluggable-components-via-dapr-artur-souza-microsoft-yaron-schneider-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Extend+Your+Microservices+With+Pluggable+Components+Via+Dapr+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Extend Your Microservices With Pluggable Components Via Dapr - Artur Souza, Microsoft & Yaron Schneider, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Artur Souza, Microsoft, Yaron Schneider, Diagrid
- Schedule: https://kccncna2022.sched.com/event/182P8/extend-your-microservices-with-pluggable-components-via-dapr-artur-souza-microsoft-yaron-schneider-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Extend+Your+Microservices+With+Pluggable+Components+Via+Dapr+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Extend Your Microservices With Pluggable Components Via Dapr.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182P8/extend-your-microservices-with-pluggable-components-via-dapr-artur-souza-microsoft-yaron-schneider-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Extend+Your+Microservices+With+Pluggable+Components+Via+Dapr+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j0MXonE3G18
- YouTube title: Extend Your Microservices With Pluggable Components Via Dapr - Artur Souza & Yaron Schneider
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/extend-your-microservices-with-pluggable-components-via-dapr/j0MXonE3G18.txt
- Transcript chars: 32155
- Keywords: dapper, basically, components, component, plugable, socket, application, discord, actually, adapter, message, reflection, messages, running, writing, secret, feature, discover

### Resumo baseado na transcript

my name is Ron Schneider I'm CTO co-founder of diagram and a Dapper maintainer and stream Committee Member hello can I hear me okay my name is Arthur I'm engineering manager for the adapter team at Microsoft also maintainer and SCC member and today we're going to talk to you about a few updates that we've been seeing for the Dapper project that we'd like to share with the broader community and everyone and also talk about pluggable components in the upper which were recently introduced in adapter 1.9 and okay so you didn't make any typo we should work there you go now I'm going to open my browser I keep forgetting where my browser is that's my usual problem here There You Go hose there we go so now if people want to try it out just send some messages we can see them here so please be nice no send angry messages there you go so you still see the Twitter logo because that's how the demos are going to be built for but it's all coming

### Excerpt da transcript

my name is Ron Schneider I'm CTO co-founder of diagram and a Dapper maintainer and stream Committee Member hello can I hear me okay my name is Arthur I'm engineering manager for the adapter team at Microsoft also maintainer and SCC member and today we're going to talk to you about a few updates that we've been seeing for the Dapper project that we'd like to share with the broader community and everyone and also talk about pluggable components in the upper which were recently introduced in adapter 1.9 and before we go into all the details I really want to thank our amazing Community contributors who really helped Drive plugable components into Dapper this is something we've been talking about I think since the very first versions of the operator um how we want to basically extend the apron and make it pluggable so that people can bring in their own components so thank you to all of our amazing contributors and so let's talk a little bit about what Dapper is and what Dapper does um as a another application developer writing a distributed system or a micro service architecture on top of kubernetes or anywhere really you might be writing something like this right you might have a bunch of services that communicate with each other they might have a queue or a database they're writing to you might have a secret story configuration store you know the underlying infrastructure for all of your applications and it looks simple on the surface but when you get into the nitty-gritty details of it there are many many distributed systems challenges that developers have to solve each and every day really with every new feature also so things like how do you do State Management from multiple replicas writing to the same record how do you do conflict management at scale how do you do error handling and fault resiliency when you talk to your message bus how do you delay messages being sent over an event-driven system how do you secure messages not just between your service to service calls but to your database and encrypt those connections and rotate these keys so so lots of these distributed systems challenges are meeting developers and as complexity Rises these challenges rise too and so the Opera comes in as the set of apis distributed systems apis that allow developers to focus under code under business logic and really remove the boilerplate code associated with all of these hard problems so the Opera can be invoked by HTTP or grpc so it's very inclusive to the two deve
