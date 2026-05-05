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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Ekin Karabulut", "Ronen Dar", "Run:ai"]
sched_url: https://kccnceu2025.sched.com/event/1txAc/optimizing-model-serving-on-kubernetes-with-model-streaming-ekin-karabulut-ronen-dar-runai
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+Model+Serving+on+Kubernetes+With+Model+Streaming+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Optimizing Model Serving on Kubernetes With Model Streaming - Ekin Karabulut & Ronen Dar, Run:ai

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Ekin Karabulut, Ronen Dar, Run:ai
- Schedule: https://kccnceu2025.sched.com/event/1txAc/optimizing-model-serving-on-kubernetes-with-model-streaming-ekin-karabulut-ronen-dar-runai
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+Model+Serving+on+Kubernetes+With+Model+Streaming+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Optimizing Model Serving on Kubernetes With Model Streaming.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAc/optimizing-model-serving-on-kubernetes-with-model-streaming-ekin-karabulut-ronen-dar-runai
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+Model+Serving+on+Kubernetes+With+Model+Streaming+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qH5djJlbodY
- YouTube title: Optimizing Model Serving on Kubernetes With Model Streaming - Ekin Karabulut & Ronen Dar, Run:ai
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/optimizing-model-serving-on-kubernetes-with-model-streaming/qH5djJlbodY.txt
- Transcript chars: 16570
- Keywords: storage, inference, gpu, streamer, tensor, models, replicas, loading, concurrency, memory, bandwidth, process, usually, weights, support, second, parameters, multiple

### Resumo baseado na transcript

So, this talk will be about optimizing model serving inference on a Kubernetes um with model weight streaming. Runai was acquired by Nvidia last year and now we're part of the Nvidia team. So in traditional applications with web web applications common practice is to use autoscalers right and there are users queries getting in and there are instances replicas of of of applications running on maybe on in a container on a CPU and when traffic goes up new uh replicas are spawn up right um to serve those requests and when traffic goes down those replicas are being spawned down right to save costs So that's with traditional applications but with AI it's much much more difficult uh because of few reasons but one of the biggest reasons is the cold start problem what we call the cold start problem it takes a long time to spin up a new replica right so first of all the process of spinning up a new replica it involves Just downloading the model weights from a storage location into the GPU and it can take a long time, right?

### Excerpt da transcript

Okay, cool. So, this talk will be about optimizing model serving inference on a Kubernetes um with model weight streaming. Um so, I'm happy to be here. Um I was I'm from the Ranai team. I was I was the co-founder and CTO of Ranai. We started in 2018. Um, RAI, we're doing what we call AI infrastructure orchestration. Runai was acquired by Nvidia last year and now we're part of the Nvidia team. Before that, I did my PhD and and postto in information theory and Aken is here with me. Yes. So, I am the developer advocate from the runai team now in media. Uh I also did my masters in robotics cognition intelligence uh in Munich. Uh so today we are going to talk about uh model inference. Yes. So model inference and and we got this uh um rani model weight streamer. It's an open source project that we published last year. And this is the work of Noah and Omar who couldn't be here but we're presenting their work. So great work by them. Um so let's start. So inference in theory right there is a training data set and a model is being trained on that data set.

It's being evaluated after the training and if results are good then it it moves to inference right and inference new data or users queries are getting into the model being processed and new predictions or generated right and this is what's the the the topic of this talk right about inference how how models can serve new requests in a cloudnative space on on GPUs. So in traditional applications with web web applications common practice is to use autoscalers right and there are users queries getting in and there are instances replicas of of of applications running on maybe on in a container on a CPU and when traffic goes up new uh replicas are spawn up right um to serve those requests and when traffic goes down those replicas are being spawned down right to save costs So that's with traditional applications but with AI it's much much more difficult uh because of few reasons but one of the biggest reasons is the cold start problem what we call the cold start problem it takes a long time to spin up a new replica right so first of all the process of spinning up a new replica it involves provisioning a new machine right but with GPU machines it takes longer than provisioning a CPU machine usually because there are less GPUs out there in the cloud and because there are software libraries like CUDA drivers and and and and CUDA kernels and libraries that that wait a lot and it takes time to install them.

Second thing is
