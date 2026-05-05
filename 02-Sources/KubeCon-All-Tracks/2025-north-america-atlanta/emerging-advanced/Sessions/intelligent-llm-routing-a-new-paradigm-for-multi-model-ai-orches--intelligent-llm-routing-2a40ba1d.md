---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Emerging + Advanced"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Chen Wang", "IBM Research", "Huamin Chen", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27FaI/intelligent-llm-routing-a-new-paradigm-for-multi-model-ai-orchestration-in-kubernetes-chen-wang-ibm-research-huamin-chen-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Intelligent+LLM+Routing%3A+A+New+Paradigm+for+Multi-Model+AI+Orchestration+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Intelligent LLM Routing: A New Paradigm for Multi-Model AI Orchestration in Kubernetes - Chen Wang, IBM Research & Huamin Chen, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Chen Wang, IBM Research, Huamin Chen, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27FaI/intelligent-llm-routing-a-new-paradigm-for-multi-model-ai-orchestration-in-kubernetes-chen-wang-ibm-research-huamin-chen-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Intelligent+LLM+Routing%3A+A+New+Paradigm+for+Multi-Model+AI+Orchestration+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Intelligent LLM Routing: A New Paradigm for Multi-Model AI Orchestration in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FaI/intelligent-llm-routing-a-new-paradigm-for-multi-model-ai-orchestration-in-kubernetes-chen-wang-ibm-research-huamin-chen-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Intelligent+LLM+Routing%3A+A+New+Paradigm+for+Multi-Model+AI+Orchestration+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DIwlL5Z8v1o
- YouTube title: Intelligent LLM Routing: A New Paradigm for Multi-Model AI Orchestration... Chen Wang & Huamin Chen
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/intelligent-llm-routing-a-new-paradigm-for-multi-model-ai-orchestratio/DIwlL5Z8v1o.txt
- Transcript chars: 30977
- Keywords: models, router, semantic, reasoning, classification, routing, latency, cost, single, caching, gpu, queries, inference, accuracy, response, milliseconds, language, workloads

### Resumo baseado na transcript

Uh first of all, thank you for joining the session and uh uh so we have the QR code for our GitHub repo as well as our documentation websites and there's also a YouTube channel uh with only two uh videos so far. Um so if you really like the talk and you want to make a contributions or have your use cases, feel free to go GitHub repo uh open up issues. so so many models you want to choose how do you know which model is the best for your workloads uh with cost effectiveness so that's is uh top one of the top questions uh many of the developers are facing um so we want Um so this is core value as we are providing to the ecosystem uh is really as a opensource uh democracy for advanced uh AI gway features. So we are trying to make the democracy available for all the open source ecosystems by providing uh robust and rich features that everybody can use out of the box. So for classification so if you're working with machine learning and uh NLP this is the classic uh type of workloads that people will use giving me a prompt tell me what kind of a complexity this prompt is and what kind of a specialty

### Excerpt da transcript

All right. Uh let's just get started. Uh first of all, thank you for joining the session and uh uh so we have the QR code for our GitHub repo as well as our documentation websites and there's also a YouTube channel uh with only two uh videos so far. Um so if you really like the talk and you want to make a contributions or have your use cases, feel free to go GitHub repo uh open up issues. Um if you kind of make a contributions, you are welcome to do so. And uh if you really like our projects and want to tip is on your agenda, give us a GitHub star, right? Um so with us do let's just get started. Uh so the idea um is intelligent uh um routing uh within the Kubernetes. So what we are discussing at the moment we are submitting the talk. We have not finalized the project yet but we open sourced the project two months ago on end of VM projects and uh ever since then it's get a lot of attention. So um we probably need to change the topic but uh uh it's all about the project itself. So what's the use cases we are um you know talking about.

So if you are familiar with how you are using the uh open eye kind of a schema for interacting with large language models you have to be really careful what you're going to use for parameters. This just reminds us of the good old days of assembly language. You know every bit about your register your bus line and your you know um the details memory managements. This is the same case as you are using the open AI API uh for language model inference um uh kind of service. You have to know which model you're going to use especially when you are using the VM ecosystem. That's a you know so many hundreds of uh models available to use. You have to know whether you want to turn on the reasoning mode or not. You know the worst case is there's a three reasoning uh light, medium and heavy. uh you have to turn this on for specific purposes and potentially you also want to you uh pick up the you know the pricing tiers uh even for open AI there's a 40 uh four mini five and you know there are five things so so many models you want to choose how do you know which model is the best for your workloads uh with cost effectiveness so that's is uh top one of the top questions uh many of the developers are facing um so we want to make this experience smoother uh you use the same line of assembly language.

So we want to be the compiler for your um inference experience. So you do not have to know exactly how to use your register, how to use your memor
