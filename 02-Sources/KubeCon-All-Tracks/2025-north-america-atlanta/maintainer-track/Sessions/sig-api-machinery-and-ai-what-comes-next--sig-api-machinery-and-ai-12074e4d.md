---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Joe Betz", "Google", "David Eads", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27Nnf/sig-api-machinery-and-ai-what-comes-next-joe-betz-google-david-eads-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=SIG+API+Machinery+and+AI%3A+What+Comes+Next%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# SIG API Machinery and AI: What Comes Next? - Joe Betz, Google & David Eads, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Joe Betz, Google, David Eads, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27Nnf/sig-api-machinery-and-ai-what-comes-next-joe-betz-google-david-eads-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+API+Machinery+and+AI%3A+What+Comes+Next%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre SIG API Machinery and AI: What Comes Next?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nnf/sig-api-machinery-and-ai-what-comes-next-joe-betz-google-david-eads-red-hat
- YouTube search: https://www.youtube.com/results?search_query=SIG+API+Machinery+and+AI%3A+What+Comes+Next%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yW7QRpUUSFs
- YouTube title: SIG API Machinery and AI: What Comes Next? - Joe Betz, Google & David Eads, Red Hat
- Match score: 0.776
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sig-api-machinery-and-ai-what-comes-next/yW7QRpUUSFs.txt
- Transcript chars: 26994
- Keywords: actually, cluster, resource, information, version, question, client, imagine, server, spaces, instead, access, sensitive, requests, change, looking, common, another

### Resumo baseado na transcript

Uh I'm a TL for SIG API machinery and joining me today is David Eids who is a chair and lead for API machinery. The focus of this talk today is about how to use AI to interact with Kubernetes. Um, the next one that is quite common is people looking to optimize their cost and resource utilization. Um, and then also a little bit more reactive when you go to execute that plan and you're actually rolling out change to your Kubernetes cluster. So, let's start by looking at the data gathering problem because I actually think this is really important when we think about how AIS are interacting with the Kubernetes cluster. Um, and when I think about data gathering, you could you could imagine there is if you gave a Kubernetes expert that knows a lot about your cluster, access your cluster and ask them a hard problem.

### Excerpt da transcript

Thank you for coming. Thank you for finding your way over to building C. Um this is uh API machinery and AI what comes next. My name is Joe Betts. Uh I'm a TL for SIG API machinery and joining me today is David Eids who is a chair and lead for API machinery. The focus of this talk today is about how to use AI to interact with Kubernetes. So this is not a talk about how to build AI systems on top of Kubernetes. Instead, we're going to be focusing on interacting directly with the coupe API. Um, this is also not a talk with fully formed proposals to change API machinery. Instead, what we're going to be focusing on today is ideas that we think are worth exploring um, but haven't been fully formed yet. Um, so hopefully that is interesting and fun and um, sparks ideas uh, with the audience. Um, I'm going to go ahead and start with a couple motivating examples. So, I had gone and spent a little bit of time looking at different use cases of the um systems interacting with the coupube API um that were using AI and I found a couple kind of major patterns.

This isn't all of them, but they seem to be some common ones. Um, one of the first is um triage and diagnostics. So, this is basically my Kubernetes cluster is broken in some way. AI, please help me fix it. Um, the next one that is quite common is people looking to optimize their cost and resource utilization. Um, so they're maybe have noticed that they're sold a lot of slack in their cluster and they're asking an AI, hey, please help me figure out um what I could do to be more efficient when you see my cluster. Um, a third major category is more proactive. So maybe you have a plan change to your cluster. Uh, maybe you're changing your work um load. Maybe you're adding in some new policies, um, something like that, and you want AI to help analyze your plan before you execute it. This is actually fairly common now. Um, and then also a little bit more reactive when you go to execute that plan and you're actually rolling out change to your Kubernetes cluster. AI can be useful in doing canary analysis to make sure that roll out is going good before you roll it all the way out.

And then the last one which I think is really interesting um and I think David brought up was um you don't know what you don't know sometimes. And so figuring out what the best practices are for your cluster uh making sure that not only do you have your workload working today but you're set up for the day two operations in the future that can b
