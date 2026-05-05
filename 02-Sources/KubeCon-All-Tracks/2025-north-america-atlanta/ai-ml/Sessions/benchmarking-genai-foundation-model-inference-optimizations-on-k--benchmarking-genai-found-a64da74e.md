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
speakers: ["Sachin Mathew Varghese", "Capital One", "Brendan Slabe", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FVD/benchmarking-genai-foundation-model-inference-optimizations-on-kubernetes-sachin-mathew-varghese-capital-one-brendan-slabe-google
youtube_search_url: https://www.youtube.com/results?search_query=Benchmarking+GenAI+Foundation+Model+Inference+Optimizations+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Benchmarking GenAI Foundation Model Inference Optimizations on Kubernetes - Sachin Mathew Varghese, Capital One & Brendan Slabe, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Sachin Mathew Varghese, Capital One, Brendan Slabe, Google
- Schedule: https://kccncna2025.sched.com/event/27FVD/benchmarking-genai-foundation-model-inference-optimizations-on-kubernetes-sachin-mathew-varghese-capital-one-brendan-slabe-google
- Busca YouTube: https://www.youtube.com/results?search_query=Benchmarking+GenAI+Foundation+Model+Inference+Optimizations+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Benchmarking GenAI Foundation Model Inference Optimizations on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVD/benchmarking-genai-foundation-model-inference-optimizations-on-kubernetes-sachin-mathew-varghese-capital-one-brendan-slabe-google
- YouTube search: https://www.youtube.com/results?search_query=Benchmarking+GenAI+Foundation+Model+Inference+Optimizations+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_JhARfcw58A
- YouTube title: Benchmarking GenAI Foundation Model Inference Optimizations on Kubernetes - S.M. Varghese & B. Slabe
- Match score: 0.954
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/benchmarking-genai-foundation-model-inference-optimizations-on-kuberne/_JhARfcw58A.txt
- Transcript chars: 24697
- Keywords: inference, metrics, performance, output, tokens, models, request, prometheus, decode, benchmarking, prefill, results, latency, requests, quantization, single, throughput, serving

### Resumo baseado na transcript

Good morning everyone and welcome to our talk titled benchmarking foundation models um inference optimizations on kubernetes. I know it's a mouthful but we'll break it all down in the next 30 minutes. The two key metrics that we would use to measure the efficiency of this process would be the time to first token and the time per output token. These are the two latency metrics that we'll try to optimize in the next few slides. Now I'll pass it on to Brendan to talk about how we validate the performance gains from such techniques. Um the core challenge is that generative AI serving is generally a blackbox.

### Excerpt da transcript

Good morning everyone and welcome to our talk titled benchmarking foundation models um inference optimizations on kubernetes. I know it's a mouthful but we'll break it all down in the next 30 minutes. So about your speakers I'm Sachin Vargas. I'm a lead machine learning engineer at Capital One. I'm also a stream lead at the Linux Foundation's GI comce and I'm oh and I'm Brendan Slave. I'm a software engineer at Google on GK's AI inference team. So a disclaimer that this talk is not about proprietary models or optimizations at Capital One or Google but rather structured around an open source project that myself and Brendan have been working on. Um so with that let's get started. So uh the topics for today we'll talk about genai models an intro like a primer on model inference. We'll talk about a few different optimizations if you are deploying or hosting LM models on your own uh systems. Uh finally, an intro to um a benchmarking tool and for validating the performance gains from these techniques and also some example results and finally our path forward.

So foundational models are at the heart of generative AI. These models are trained on large data. u they learn complex patterns and generate content. This could be text, audio, images or any any other forms of data. This generated content then forms the solutions for many generalized problems like question answering, sentiment analysis or even automating agents. So let's understand how these foundation models work under the hood. Um here we consider textbased auto reggressive models. So text in text out. These models usually generate one token at a time. For simplicity, we can imagine uh these tokens to be equivalent to an English uh word in this graphic. The model inference itself has two stages. The prefill stage and the decode stage. The prefill process all your input text or tokens and generates a single output token. um and the decode state generates subsequent tokens one at a time in an auto reggressive manner. This entire process is hugely accelerated by the usage of a KV cache that stores results from previous computations for the next token generation step.

The two key metrics that we would use to measure the efficiency of this process would be the time to first token and the time per output token. These are the two latency metrics that we'll try to optimize in the next few slides. Now let's consider the same inference process in a real-time production system handling multiple concurrent requests
