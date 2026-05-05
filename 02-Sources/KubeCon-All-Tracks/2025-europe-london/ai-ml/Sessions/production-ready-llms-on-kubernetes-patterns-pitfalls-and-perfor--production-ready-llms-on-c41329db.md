---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Priya Samuel", "Elsevier", "Luke Marsden", "MLOps Consulting"]
sched_url: https://kccnceu2025.sched.com/event/1tx94/production-ready-llms-on-kubernetes-patterns-pitfalls-and-performance-priya-samuel-elsevier-luke-marsden-mlops-consulting
youtube_search_url: https://www.youtube.com/results?search_query=Production-Ready+LLMs+on+Kubernetes%3A+Patterns%2C+Pitfalls%2C+and+Performance+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Production-Ready LLMs on Kubernetes: Patterns, Pitfalls, and Performance - Priya Samuel, Elsevier & Luke Marsden, MLOps Consulting

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Priya Samuel, Elsevier, Luke Marsden, MLOps Consulting
- Schedule: https://kccnceu2025.sched.com/event/1tx94/production-ready-llms-on-kubernetes-patterns-pitfalls-and-performance-priya-samuel-elsevier-luke-marsden-mlops-consulting
- Busca YouTube: https://www.youtube.com/results?search_query=Production-Ready+LLMs+on+Kubernetes%3A+Patterns%2C+Pitfalls%2C+and+Performance+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Production-Ready LLMs on Kubernetes: Patterns, Pitfalls, and Performance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx94/production-ready-llms-on-kubernetes-patterns-pitfalls-and-performance-priya-samuel-elsevier-luke-marsden-mlops-consulting
- YouTube search: https://www.youtube.com/results?search_query=Production-Ready+LLMs+on+Kubernetes%3A+Patterns%2C+Pitfalls%2C+and+Performance+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KIRUbaUjEKw
- YouTube title: Production-Ready LLMs on Kubernetes: Patterns, Pitfalls, and Performa... Priya Samuel & Luke Marsden
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/production-ready-llms-on-kubernetes-patterns-pitfalls-and-performance/KIRUbaUjEKw.txt
- Transcript chars: 24816
- Keywords: llm, running, models, cluster, vector, response, context, question, issues, answer, actually, knowledge, document, environment, gpu, called, images, database

### Resumo baseado na transcript

This talk is for you if you're interested in in running really uh generative AI models on your own infrastructure in a secure way. Uh across the number of companies we're talking to, we're seeing that lots of businesses are becoming more wary of putting their data on uh proprietary uh hosted AI platforms. um over the number of years I've worked um on building u machine learning pipelines as well as automating these pipelines and um so this is quite an exciting area to be uh working and over to Luke for an introduction. Uh I started out um doing a startup that did storage for Docker and Kubernetes back in the early Docker and Kubernetes days. And so I f I saw firsthand working with those clients um the opportunity to take open source models that were getting better really quickly um and run them locally in Kubernetes clusters for improved kind of security and reliability. Uh so yeah it's a it's an interesting topic and happy to share some of our learnings today.

### Excerpt da transcript

Welcome everyone and thank you for coming to our talk. This talk is for you if you're interested in in running really uh generative AI models on your own infrastructure in a secure way. Uh across the number of companies we're talking to, we're seeing that lots of businesses are becoming more wary of putting their data on uh proprietary uh hosted AI platforms. And what we're going to do today is show you an alternative solution where you can host your own LLMs on your own infrastructure. And um every time you you blink and you realize the AI landscape has changed quite a bit. And uh we're seeing also that lots of people look at this as this is quite complex. And what we're trying to do today is peel back that complexity and start this um this journey from very very basic building blocks and take you through how uh sort of our experiences building AI platforms out of um Kubernetes and uh open source LLMs. We want to talk about um patterns that we've used, pitfalls that we stumbled into, and really talk about our mistakes as well, so you don't have to do them yourselves.

And uh we'll also talk about the layers that we built on top of um uh a basic open LLM running on Kubernetes. Uh before we move on, I'm going to take a moment to introduce ourselves. So my name is Priya Samuel. I'm a technology architect. I've worked in many small and large businesses and uh most of my background is in DevOps as well as consulting and um my current um uh environment I work in is around building identity and access layer on top of uh genai applications and um over the number of years I've worked um on building u machine learning pipelines as well as automating these pipelines and um so this is quite an exciting area to be uh working and over to Luke for an introduction. Cool. Hi everyone. Um yeah, I'm I'm Luke Marsden. Um I've worked in DevOps pretty much my whole career. Uh I started out um doing a startup that did storage for Docker and Kubernetes back in the early Docker and Kubernetes days. Um I was involved in SIG cluster life cycle at the time that we created Kubadm. So if anyone's used Cub Cubeadm here, you can blame me.

Um and then um I've done yeah like a string of startups. We we then did a an endto-end MLOps platform uh before uh AI was cool. And then I did consulting for a few years while um during the time that the chat GPT moment happened. And so I f I saw firsthand working with those clients um the opportunity to take open source models that were getting bette
