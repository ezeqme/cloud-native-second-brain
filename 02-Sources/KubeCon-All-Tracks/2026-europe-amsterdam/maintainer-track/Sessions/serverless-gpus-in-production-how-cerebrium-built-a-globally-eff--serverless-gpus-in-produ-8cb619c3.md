---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Dave Protasowski", "Dave's Consulting Company", "Elijah Roussos", "Cerebrium"]
sched_url: https://kccnceu2026.sched.com/event/2EF62/serverless-gpus-in-production-how-cerebrium-built-a-globally-efficient-low-latency-ai-platform-with-knative-dave-protasowski-daves-consulting-company-elijah-roussos-cerebrium
youtube_search_url: https://www.youtube.com/results?search_query=Serverless+GPUs+in+Production%3A+How+Cerebrium+Built+a+Globally+Efficient+Low-Latency+AI+Platform+with+Knative+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Serverless GPUs in Production: How Cerebrium Built a Globally Efficient Low-Latency AI Platform with Knative - Dave Protasowski, Dave's Consulting Company & Elijah Roussos, Cerebrium

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Dave Protasowski, Dave's Consulting Company, Elijah Roussos, Cerebrium
- Schedule: https://kccnceu2026.sched.com/event/2EF62/serverless-gpus-in-production-how-cerebrium-built-a-globally-efficient-low-latency-ai-platform-with-knative-dave-protasowski-daves-consulting-company-elijah-roussos-cerebrium
- Busca YouTube: https://www.youtube.com/results?search_query=Serverless+GPUs+in+Production%3A+How+Cerebrium+Built+a+Globally+Efficient+Low-Latency+AI+Platform+with+Knative+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Serverless GPUs in Production: How Cerebrium Built a Globally Efficient Low-Latency AI Platform with Knative.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF62/serverless-gpus-in-production-how-cerebrium-built-a-globally-efficient-low-latency-ai-platform-with-knative-dave-protasowski-daves-consulting-company-elijah-roussos-cerebrium
- YouTube search: https://www.youtube.com/results?search_query=Serverless+GPUs+in+Production%3A+How+Cerebrium+Built+a+Globally+Efficient+Low-Latency+AI+Platform+with+Knative+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QqApwTinlUk
- YouTube title: Serverless GPUs in Production: How Cerebrium Built a Globally... Dave Protasowski & Elijah Roussos
- Match score: 0.794
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/serverless-gpus-in-production-how-cerebrium-built-a-globally-efficient/QqApwTinlUk.txt
- Transcript chars: 28071
- Keywords: native, deploy, activator, container, functions, actually, gpu, typically, instead, platform, serving, developer, requests, targets, running, eventing, request, traffic

### Resumo baseado na transcript

>> Eli, >> good thing I asked um uh we're going to talk about how Cereum uses K Native to deliver serless GPUs on their platform. I'm the serving lead, which is sort of like the serverless runtime that's there. I'm not going to go into too detail because I'll add a link to a talk where I did in Atlanta that has like details on this and like a demo for each thing. like hey just give me run WordPress and then we come back with like a URL that has a certificate that was provisioned and then this if you hit this URL it will scale up from zero scale down to zero we do request change All these components need to have performance criteria that matches but they have different requirements in terms of scaling in terms of resource needs but the core tenant surrounding most of these workloads is very similar. If you overprovision, typically you need to because otherwise you can't you can't scale over.

### Excerpt da transcript

Uh yeah, let's get started. Welcome to the talk. This is uh gonna be talk about uh serless GPUs in production. So this is how um Cerebrim, that's Ellie over here or Eli. >> Eli, >> good thing I asked um uh we're going to talk about how Cereum uses K Native to deliver serless GPUs on their platform. And quick intro about us. >> Uh yeah, so I'm Eli or Elijah. I'm the founding engineer at uh Cerebrum. I'll explain more about what we do later, but check out Cereum. Uh check me out if you want. Uh yeah, that was awesome to you. >> Hey, my name is Dave. I'm a K Native maintainer. Um I'll get into K Native. Uh a few roles in the project. I'm the serving lead, which is sort of like the serverless runtime that's there. I'm also on the steering committee. That's the SC here. Um, these are the handles. I still use the Twitter logo because that's what I like, but I don't really use Twitter. Uh, just you can message me on LinkedIn if you have questions for things. And then I'm going to do a quick uh what is K native run through, but um I have a link to a demo that goes into more and you can visit our website kative.dev for everything else.

Um so the big trouble with Kubernetes and I guess to clarify what Kative is it kind of targets the app developer persona and when you present Kubernetes to app developers it's super overwhelming because it con essentially like the podsp spec when you want to deploy an app and deployment models like app operator app developer concerns with platform engineer concerns about like topology node scheduling and all these things and all an app developer really cares about is um here's my container run it I don't really care how it works. So we try to um simplify Kubernetes for app developers in three ways. We have simplifying development with K native functions, simplifying running your apps in K serving and connecting your apps with K native eventing. This is kind of like the life cycle. I'm not going to go into too detail because I'll add a link to a talk where I did in Atlanta that has like details on this and like a demo for each thing. Uh but a quick thing functions lets you bootstrap functions and this is like a local tool that helps you build containers.

Uh we bootstrap in like an HP server and we can handle HP events and cloud events. Cloud events is sort of the CNCF deacto standard for uh payload messaging that has special headers to let you do routing and filtering and you don't need docker to do the container building. Uh servin
