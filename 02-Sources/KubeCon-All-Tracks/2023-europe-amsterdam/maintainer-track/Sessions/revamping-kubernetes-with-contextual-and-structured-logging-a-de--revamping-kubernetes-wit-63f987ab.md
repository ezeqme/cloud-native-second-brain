---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Kubernetes Core", "Community Governance"]
speakers: ["Shivanshu Raj Shrivastava", "Independent"]
sched_url: https://kccnceu2023.sched.com/event/1HyS8/revamping-kubernetes-with-contextual-and-structured-logging-a-deep-dive-shivanshu-raj-shrivastava-independent
youtube_search_url: https://www.youtube.com/results?search_query=Revamping+Kubernetes+with+Contextual+and+Structured+Logging%2C+a+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Revamping Kubernetes with Contextual and Structured Logging, a Deep Dive - Shivanshu Raj Shrivastava, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shivanshu Raj Shrivastava, Independent
- Schedule: https://kccnceu2023.sched.com/event/1HyS8/revamping-kubernetes-with-contextual-and-structured-logging-a-deep-dive-shivanshu-raj-shrivastava-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Revamping+Kubernetes+with+Contextual+and+Structured+Logging%2C+a+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Revamping Kubernetes with Contextual and Structured Logging, a Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyS8/revamping-kubernetes-with-contextual-and-structured-logging-a-deep-dive-shivanshu-raj-shrivastava-independent
- YouTube search: https://www.youtube.com/results?search_query=Revamping+Kubernetes+with+Contextual+and+Structured+Logging%2C+a+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=njoyvh07i4s
- YouTube title: Revamping Kubernetes with Contextual and Structured Logging, a Deep Dive - Shivanshu Shrivastava
- Match score: 0.946
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/revamping-kubernetes-with-contextual-and-structured-logging-a-deep-div/njoyvh07i4s.txt
- Transcript chars: 22062
- Keywords: logging, logs, actually, context, structure, migration, contextual, structured, object, communities, around, logger, function, format, message, write, contributing, achieve

### Resumo baseado na transcript

so today we are going to talk about uh what we are essentially doing in communities to make it uh the logs like to make the logs machine readable like right now they are human readable but they are not machine readable so as we uh take a step forward in the observative space we need some automation on top of communities to be able to uh manage kubernetes in a better way so this is what uh we're gonna cover today about what we have done to make it

### Excerpt da transcript

so today we are going to talk about uh what we are essentially doing in communities to make it uh the logs like to make the logs machine readable like right now they are human readable but they are not machine readable so as we uh take a step forward in the observative space we need some automation on top of communities to be able to uh manage kubernetes in a better way so this is what uh we're gonna cover today about what we have done to make it possible a short introduction about me um shivanshu and uh yeah so I work at UH tetrate and I've been contributing to WG structured logging which is a part of C instrumentation and yeah I'm also contributing to kubernetes and istio yep if you have any questions you can uh reach out to me on Twitter and yeah we can talk about and shout out to uh Patrick and Mark so they have been investing their time uh they have been editing on few things to make it possible so it don't be possible because of these guys I mean if they were not here so we are glad for their help so today's agenda involves uh a brief introduction about what is structured logging and what is contextual logging and then we're gonna dive a bit deep into what we have done to actually achieve this in communities and then like what are like for kubernetes contributors what are the migration instructions for them to actually write code when when they are so as a developer we ignore the importance of logs when writing the code but it becomes a bottleneck when let's say a platform engine is debugging some things so that's that's why we have created a migration guide so that people can actually use it and then questions are welcome at the end and I would like to welcome the target audience so anyone who is contributing to communities is uh is yeah it's they're welcome and uh people who are contributing to logging agents uh they are mostly playing around the Melt data all day long so yeah they are also welcome and uses of communities who are interested in managing communities and we are probably so for example gke or or any managed Community solution you need uh some sort of automation so that if something goes wrong like we can do something about it so that's where end users of units are welcome so that they can build something on top of restructured and contextual logs and it's very good for new contributors to get started because uh we have a lot of work which revolves around migrating the logs the existing logs and then there is beginning a friendly work w
