---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["Kubernetes Core"]
speakers: ["Thomas Vitale", "Systematic", "Kevin Dubois", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1txGo/from-0-to-production-grade-with-kubernetes-native-development-thomas-vitale-systematic-kevin-dubois-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=From+0+To+Production-Grade+With+Kubernetes+Native+Development+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From 0 To Production-Grade With Kubernetes Native Development - Thomas Vitale, Systematic & Kevin Dubois, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Thomas Vitale, Systematic, Kevin Dubois, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1txGo/from-0-to-production-grade-with-kubernetes-native-development-thomas-vitale-systematic-kevin-dubois-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=From+0+To+Production-Grade+With+Kubernetes+Native+Development+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From 0 To Production-Grade With Kubernetes Native Development.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGo/from-0-to-production-grade-with-kubernetes-native-development-thomas-vitale-systematic-kevin-dubois-red-hat
- YouTube search: https://www.youtube.com/results?search_query=From+0+To+Production-Grade+With+Kubernetes+Native+Development+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=07RnkzSc6Jg
- YouTube title: From 0 To Production-Grade With Kubernetes Native Development - Thomas Vitale & Kevin Dubois
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-0-to-production-grade-with-kubernetes-native-development/07RnkzSc6Jg.txt
- Transcript chars: 29385
- Keywords: application, development, running, developer, container, developers, containers, cluster, native, actually, deploy, production, database, experience, environment, function, source, course

### Resumo baseado na transcript

We're going to talk about, uh, Kubernetes, Kubernetes native, uh, development. But our traditional way of development has typically or traditionally been like, yeah, I'm going to develop my code and it works great on my local machine, package it up, maybe throw it over the wall, and somebody's going to deploy it on these uh kind of big application servers. Wrote a book about it uh a couple of years ago and now I'm working with my friend Mauricio Salatino on a new book called Developer Experience on Kubernetes. So Kubernetes native development at least as a minimum we want to work with containers somehow. It will be designed and built in a way that is uh performant that is secure. So you don't have to deal with port forwarding and understand all the uh low-level details of how Kubernetes networking works.

### Excerpt da transcript

I think we can get started. So, uh, welcome to this session. We're going to talk about, uh, Kubernetes, Kubernetes native, uh, development. And, um, I don't know if you you're familiar with this term. Um, it's kind of, I mean, it's still software development, right? But our traditional way of development has typically or traditionally been like, yeah, I'm going to develop my code and it works great on my local machine, package it up, maybe throw it over the wall, and somebody's going to deploy it on these uh kind of big application servers. Especially if you're like us and you're Java developers and uh you know, use as many resources as you want. It doesn't matter. You know, we have these big servers. Kubernetes native development is kind of different, right? you need to think about uh the way that your applications are going to live on Kubernetes in a different way because on these clusters what you want is applications that start up fast because they can be kind of rescheduled or maybe scale up or whatever, excuse me.

And um you want to make sure that the resource usage is going to be lower, right? because the smaller your application is, the more you're going to be able to make the most of these clusters uh in terms of density and you know out of your money as well, right? So that's kind of what we need to think about as application developers and that's what we're going to try to focus on a little bit in this session. um you know some tools that we can use in the CNCF landscape and a little bit out of that in the open source space to help application developers work with Kubernetes without being Kubernetes experts. So uh my name is Kevin Dubois. I'm a developer advocate at uh at Red Hat. Um I've been uh writing software for the last 20 years. Um so I went from that more traditional world to the cloudnative world. It's been uh it's been an interesting journey and with me here is uh is Thomas. Yeah. Hi everyone. I'm Thomas Vital. I work at systematic software company passionate about anything cloud native and Java related.

Wrote a book about it uh a couple of years ago and now I'm working with my friend Mauricio Salatino on a new book called Developer Experience on Kubernetes. We're really excited. We just announced it yesterday. Uh so the first few chapters are available out there. But let's get started. So Kubernetes native development at least as a minimum we want to work with containers somehow. So the first ingredient is we need a container runtim
