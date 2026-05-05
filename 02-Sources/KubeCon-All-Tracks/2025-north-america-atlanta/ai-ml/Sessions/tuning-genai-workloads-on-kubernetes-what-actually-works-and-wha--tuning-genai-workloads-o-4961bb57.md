---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Ishaan Sehgal", "Omnara", "Brian Lockwood", "NVIDIA"]
sched_url: https://kccncna2025.sched.com/event/27Fa9/tuning-genai-workloads-on-kubernetes-what-actually-works-and-what-doesnt-ishaan-sehgal-omnara-brian-lockwood-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Tuning+GenAI+Workloads+on+Kubernetes%3A+What+Actually+Works+%28and+What+Doesn%E2%80%99t%29%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Tuning GenAI Workloads on Kubernetes: What Actually Works (and What Doesn’t)? - Ishaan Sehgal, Omnara & Brian Lockwood, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Ishaan Sehgal, Omnara, Brian Lockwood, NVIDIA
- Schedule: https://kccncna2025.sched.com/event/27Fa9/tuning-genai-workloads-on-kubernetes-what-actually-works-and-what-doesnt-ishaan-sehgal-omnara-brian-lockwood-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Tuning+GenAI+Workloads+on+Kubernetes%3A+What+Actually+Works+%28and+What+Doesn%E2%80%99t%29%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Tuning GenAI Workloads on Kubernetes: What Actually Works (and What Doesn’t)?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fa9/tuning-genai-workloads-on-kubernetes-what-actually-works-and-what-doesnt-ishaan-sehgal-omnara-brian-lockwood-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Tuning+GenAI+Workloads+on+Kubernetes%3A+What+Actually+Works+%28and+What+Doesn%E2%80%99t%29%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t5shPzCV53A
- YouTube title: Tuning GenAI Workloads on Kubernetes: What Actually Works (and Wha... Ishaan Sehgal & Brian Lockwood
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tuning-genai-workloads-on-kubernetes-what-actually-works-and-what-does/t5shPzCV53A.txt
- Transcript chars: 24301
- Keywords: actually, workloads, skyhook, settings, running, specify, workload, package, reboot, custom, inference, carpenter, container, tuning, agents, getting, parameters, working

### Resumo baseado na transcript

Hey everyone, we are going to talk about tuning Genai workloads on Kubernetes. So, first I want to just give some background for what we're going to be talking about. Um, the reason why you'd want to use Kubernetes is if you want to own your own infrastructure, right? Okay, so we make it as easy as possible to run an AI workload on Kubernetes. Like this talk is not meant to be like in-depth ML concepts or anything, but this is just a high level to show you how you'd run different ML workloads in Kubernetes here using Kaido. Uh, this is an example of how you'd run a rag deployment using Kaido and Kubernetes.

### Excerpt da transcript

Okay. Hey everyone, we are going to talk about tuning Genai workloads on Kubernetes. So what works and what doesn't. Let's go to the next. So yeah, just to introduce ourselves, I'm Ean. I used to work at Microsoft. I I worked on Kaido, which we're going to be talking about. Um I left Microsoft about 5 months ago and now I started a company. We run coding agents on your phone. and I'm the CEO and co-founder. And this is Brian. He's a senior engineer at NVIDIA. And we're going to be so let's continue here. So, okay. So, first I want to just give some background for what we're going to be talking about. We Yeah. So, let's talk about generative AI. The first thing that I want to talk about to set the stage is what are the implications of running LLMs? Okay. Um model sizes are getting really really big. Okay. Um last year I remember GPT4 for example was about a trillion parameters. It was rumored to be about a trillion parameters and GBT 5 is 10 times the number of parameters. Okay. Um so model sizes are getting massive and as models get larger and larger the amount of tokens you need to train them actually goes up exponentially.

Okay. And dealing with such large models, this is a this is very expensive. It's very costly. It's a resource problem. And essentially why we're all here today is it's an infrastructure problem. Okay. Um and we think that Kubernetes is the best way to solve it. So that brings us to the next topic here. Why run LLMs on Kubernetes? Okay. Um there are hosted solutions out there, right? There is Azure ML, there's AWS SageMaker, there's a bunch of startups building hosted solutions for serverless endpoints. Um, the reason why you'd want to use Kubernetes is if you want to own your own infrastructure, right? You want to own your own data. And so what that means is like let's say you want to use a custom ML framework or serving engine. you want to use deep speed or onyx or uh you know nvidia trident or you want to set quotas and and permissions or networking. So any sort of advanced use cases, you want to own your own infrastructure, right? Um on top of that, the cherry on top is that the community is like really really supportive right now.

I mean the tooling is super robust. Um I mean Hugging Face is not only providing the the models for you to download, but you also have I mean all the libraries to get up and running. So it really is like the best time ever to run LLMs on Kubernetes. That said, uh I think no one here is a stranger to thi
