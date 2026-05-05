---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Abby Bangser", "Syntasso"]
sched_url: https://kccncna2022.sched.com/event/182F1/tutorial-becoming-a-kubernetes-developer-writing-your-first-operator-abby-bangser-syntasso
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Becoming+a+Kubernetes+Developer%3A+Writing+Your+First+Operator+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tutorial: Becoming a Kubernetes Developer: Writing Your First Operator - Abby Bangser, Syntasso

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Abby Bangser, Syntasso
- Schedule: https://kccncna2022.sched.com/event/182F1/tutorial-becoming-a-kubernetes-developer-writing-your-first-operator-abby-bangser-syntasso
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Becoming+a+Kubernetes+Developer%3A+Writing+Your+First+Operator+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tutorial: Becoming a Kubernetes Developer: Writing Your First Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182F1/tutorial-becoming-a-kubernetes-developer-writing-your-first-operator-abby-bangser-syntasso
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Becoming+a+Kubernetes+Developer%3A+Writing+Your+First+Operator+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fDkoxrz7BXw
- YouTube title: Tutorial: Becoming a Kubernetes Developer: Writing Your First Operator - Abby Bangser, Syntasso
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tutorial-becoming-a-kubernetes-developer-writing-your-first-operator/fDkoxrz7BXw.txt
- Transcript chars: 32834
- Keywords: foreign, started, operator, controller, questions, around, actually, website, question, controllers, application, course, please, operators, deployment, builder, access, framework

### Resumo baseado na transcript

thank you everyone for coming really excited to be here and to share a bit of my experience and also maybe help some of you get started with extending kubernetes and becoming a kubernetes developer I've been to a few talks so far here that have been talking about some of the more advanced aspects of creating controllers and creating operators and I think from my perspective not long ago I hadn't even gotten started so I didn't know what that all was and I'd like to lower that barrier

### Excerpt da transcript

thank you everyone for coming really excited to be here and to share a bit of my experience and also maybe help some of you get started with extending kubernetes and becoming a kubernetes developer I've been to a few talks so far here that have been talking about some of the more advanced aspects of creating controllers and creating operators and I think from my perspective not long ago I hadn't even gotten started so I didn't know what that all was and I'd like to lower that barrier of Entry through this tutorial today so I talk about becoming a kubernetes developer but that's not a common term I don't think I mean I think some people might use it but not sure what the definition is right now and I think about that because I think of three different interaction models that you might have with kubernetes you might be a user you might be someone who has their application deployed to kubernetes and you have access to cube CTL on the CLI or maybe you don't maybe you have a user interface in some way that you access your deployment and your logs and look at things you may even be an advanced user just to say but you're still someone who considers kubernetes a place to run your software you may be in the room and you may be an administrator an administrator might be someone who creates clusters on demand for their organization they might do some configuration of those clusters and may run some software themselves this would be software that would support the organization so things like monitoring applications Prometheus other tools that you might need this is likely to be someone who's a bit more advanced within cubectl but and other techniques but someone who's really focused on the infrastructure side of kubernetes and what we're going to be focusing on today is the developer side so this is someone who may or may not also be or used to be a user and administrator but it's someone who thinks about kubernetes as an API and a framework and a way to solve problems and so what they do is they use kubernetes native aspects to extend that API and use that API to solve their business problems and that's what we're going to be looking at a bit today and so you might wonder which one am I I've been and am all three I started my career in test engineering and was very much on the user side of things I went into platform engineering and was a part of infrastructure teams for a few years there and I was very much an administrator and I'm now building a controller running
