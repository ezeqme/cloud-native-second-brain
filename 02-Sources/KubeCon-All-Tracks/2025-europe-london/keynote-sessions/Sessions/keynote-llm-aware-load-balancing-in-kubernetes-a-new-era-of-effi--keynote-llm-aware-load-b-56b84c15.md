---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Clayton Coleman", "Distinguished Engineer", "Google", "Jiaxin Shan", "Software Engineer", "Bytedance"]
sched_url: https://kccnceu2025.sched.com/event/1txC7/keynote-llm-aware-load-balancing-in-kubernetes-a-new-era-of-efficiency-clayton-coleman-distinguished-engineer-google-jiaxin-shan-software-engineer-bytedance
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+LLM-Aware+Load+Balancing+in+Kubernetes%3A+A+New+Era+of+Efficiency+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: LLM-Aware Load Balancing in Kubernetes: A New Era of Efficiency - Clayton Coleman, Distinguished Engineer, Google & Jiaxin Shan, Software Engineer, Bytedance

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Clayton Coleman, Distinguished Engineer, Google, Jiaxin Shan, Software Engineer, Bytedance
- Schedule: https://kccnceu2025.sched.com/event/1txC7/keynote-llm-aware-load-balancing-in-kubernetes-a-new-era-of-efficiency-clayton-coleman-distinguished-engineer-google-jiaxin-shan-software-engineer-bytedance
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+LLM-Aware+Load+Balancing+in+Kubernetes%3A+A+New+Era+of+Efficiency+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: LLM-Aware Load Balancing in Kubernetes: A New Era of Efficiency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txC7/keynote-llm-aware-load-balancing-in-kubernetes-a-new-era-of-efficiency-clayton-coleman-distinguished-engineer-google-jiaxin-shan-software-engineer-bytedance
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+LLM-Aware+Load+Balancing+in+Kubernetes%3A+A+New+Era+of+Efficiency+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=X01DgDpFdYI
- YouTube title: Keynote: LLM-Aware Load Balancing in Kubernetes: A New Era of Efficiency- C. Coleman & J. Shan (ISL)
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-llm-aware-load-balancing-in-kubernetes-a-new-era-of-efficiency/X01DgDpFdYI.txt
- Transcript chars: 14406
- Keywords: models, production, inference, llm, requests, traffic, serving, gpu, request, gateway, routing, latency, ecosystem, platform, servers, balancing, workloads, output

### Resumo baseado na transcript

We're here today to talk about a new project in the Kubernetes ecosystem sponsored by the serving working group called the gateway API inference extension. It takes any Kubernetes gateway and turns it into an inference gateway. So we expect everyone hopefully will eventually need to serve open models for efficiency at scale while still continue to depend on cutting edge models for time to market. That's exactly the question that we started the serving working group in Kubernetes to answer a year ago at CubeConu. And just like in the beginning of Kubernetes, we depend on experienced platform teams looking to build the next generation of their platforms to guide us. Running LLM in Kubernetes sounds simple in theory, but in practice is still challenging.

### Excerpt da transcript

Good morning. We're here today to talk about a new project in the Kubernetes ecosystem sponsored by the serving working group called the gateway API inference extension. It takes any Kubernetes gateway and turns it into an inference gateway. And an inference gateway helps large platform teams, small platform teams self-host large language models efficiently in production. It's informed by our experiences at Google and Bite Dance. and we're very excited to talk to you today about it. 10 years ago, someone told me that Kubernetes wasn't going to be relevant to the majority of users. We'd all be using functions as a service or maybe 12 factor managed platform as a service uh in the cloud. Now, obviously, as judging by all of us here, they were wrong. But there was a seat of truth in that. It wasn't yet clear that the majority of large platform teams would have a diverse range of workloads and that they would need and demand the flexibility from of Kubernetes as well as depend on a rich ecosystem of composable automation.

There's a similar timeline going on in AI today. Two years ago, it seemed that all models would be proprietary. In the last year, open models have dramatically closed the gap because larger models are more flexible and smaller models are more efficient to serve. We believe there is a meaningful and durable trade-off between very smart frontier models and smaller predictable building block open models. So we expect everyone hopefully will eventually need to serve open models for efficiency at scale while still continue to depend on cutting edge models for time to market. What flexibility and composable automation will we all need when models are a fundamental part of our applications? That's exactly the question that we started the serving working group in Kubernetes to answer a year ago at CubeConu. And just like in the beginning of Kubernetes, we depend on experienced platform teams looking to build the next generation of their platforms to guide us. We were very fortunate that Bite Dance was ready to build the next version of their platform.

They chose to do it in the open with us. Running LLM in Kubernetes sounds simple in theory, but in practice is still challenging. Let's dive into several production issues that shows LLM inference challenges are truly unique. The first plot is from a bidance production LM service capturing the daily request distribution. So as we can see the request valuation is spiking. The input prompt size vary wid
