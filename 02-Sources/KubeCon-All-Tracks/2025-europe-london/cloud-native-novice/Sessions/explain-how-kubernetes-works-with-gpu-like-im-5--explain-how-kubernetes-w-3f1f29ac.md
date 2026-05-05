---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Carlos Santana", "AWS"]
sched_url: https://kccnceu2025.sched.com/event/1txFq/explain-how-kubernetes-works-with-gpu-like-im-5-carlos-santana-aws
youtube_search_url: https://www.youtube.com/results?search_query=Explain+How+Kubernetes+Works+With+GPU+Like+I%E2%80%99m+5+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Explain How Kubernetes Works With GPU Like I’m 5 - Carlos Santana, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Carlos Santana, AWS
- Schedule: https://kccnceu2025.sched.com/event/1txFq/explain-how-kubernetes-works-with-gpu-like-im-5-carlos-santana-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Explain+How+Kubernetes+Works+With+GPU+Like+I%E2%80%99m+5+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Explain How Kubernetes Works With GPU Like I’m 5.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFq/explain-how-kubernetes-works-with-gpu-like-im-5-carlos-santana-aws
- YouTube search: https://www.youtube.com/results?search_query=Explain+How+Kubernetes+Works+With+GPU+Like+I%E2%80%99m+5+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bQvrutQO3-c
- YouTube title: Explain How Kubernetes Works With GPU Like I’m 5 - Carlos Santana, AWS
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/explain-how-kubernetes-works-with-gpu-like-im-5/bQvrutQO3-c.txt
- Transcript chars: 27444
- Keywords: device, gpu, driver, container, jetson, install, nvidia, feature, devices, version, running, actually, discovery, plug-in, toolkit, basically, runtime, operating

### Resumo baseado na transcript

If you want to learn more about being a CNCF ambassador, check uh with me or any other CNCF ambassador here that we are here in this week and we can tell you about the program. And today's talk is on the no uh novice track uh on explain how Kubernetes works with GPUs. So I I taught myself that I know Kubernetes enough um to get Kubernetes running at home. But with the late um trending of like LLMs and chat GPT running GPUs just for playing around or learning on the cloud or from a vendor is kind of quite expensive if you're not doing you don't know what you're doing. so I wanted to learn how actually what are the components of kubernetes or the minimum things to get kubernetes working with my GPU that is sitting on my desk so I thought about doing this talk in terms of how I did my learning doing this and in Amazon we have a leadership principle called learn and be curious.

### Excerpt da transcript

My name is Carlos Santana. I'm a CNCF ambassador. Uh that's a volunteer uh position. If you want to learn more about being a CNCF ambassador, check uh with me or any other CNCF ambassador here that we are here in this week and we can tell you about the program. Um I also have to make a living. So I work on AWS as a solutions architect for the EKS um uh service. That means Kubernetes uh using AWS. And today's talk is on the no uh novice track uh on explain how Kubernetes works with GPUs. Uh who's here because they search the word GPU on the schedule and just show up. Okay. So that that strategy worked. Um who here has a home lab of like trying to install Kubernetes at home? Okay. So maybe at the end of this talk everybody will raise your hand. Um this talk is an introduction of a story about running Kubernetes at home and some of the basics are applicable running GPUs workloads on the cloud. But for for this people are new to Kubernetes or maybe like myself I thought I was an expert on Kubernetes um uh I was doing this at home.

So let's start with the scenario. So the scenario is that I want to learn at home. I want to learn uh with machines or computers all computers that I have at home about uh Linux for example and then Kubernetes. There's some sound coming from the other side. It's kind of annoying. Um so we start what's the recipe? So you get yourself a maybe a fiveyear Kubernetes expert. So we was talking about five year expert and then you combine that. So that's for me for example work have worked with Kubernetes since 2016 in another cloud provider. Now I work for AWS working with EKS for the last three years. So I I taught myself that I know Kubernetes enough um to get Kubernetes running at home. So at home I have a different devices and my wife hates that I bring or buy another cable in my house. Who has that problem? So she asked me like why do you need another cable? Well, because I might need it at some point, right? Um, but in this case, I have all these little devices. So, I have uh things that run Linux. I have Espirinos, I have Raspberry Pies, I have Nuks, I have O laptops, I have laptops that don't have a screen.

And I try to like learn and just boot up Linux and boot Kubernetes. But with the late um trending of like LLMs and chat GPT running GPUs just for playing around or learning on the cloud or from a vendor is kind of quite expensive if you're not doing you don't know what you're doing. So in that case I thought myself oh let's get
