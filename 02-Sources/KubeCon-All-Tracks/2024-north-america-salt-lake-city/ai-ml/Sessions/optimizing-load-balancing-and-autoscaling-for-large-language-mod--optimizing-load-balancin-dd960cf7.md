---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["David Gray", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7lb/optimizing-load-balancing-and-autoscaling-for-large-language-model-llm-inference-on-kubernetes-david-gray-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+Load+Balancing+and+Autoscaling+for+Large+Language+Model+%28LLM%29+Inference+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Optimizing Load Balancing and Autoscaling for Large Language Model (LLM) Inference on Kubernetes - David Gray, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: David Gray, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7lb/optimizing-load-balancing-and-autoscaling-for-large-language-model-llm-inference-on-kubernetes-david-gray-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+Load+Balancing+and+Autoscaling+for+Large+Language+Model+%28LLM%29+Inference+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Optimizing Load Balancing and Autoscaling for Large Language Model (LLM) Inference on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lb/optimizing-load-balancing-and-autoscaling-for-large-language-model-llm-inference-on-kubernetes-david-gray-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+Load+Balancing+and+Autoscaling+for+Large+Language+Model+%28LLM%29+Inference+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TSEGAh1bs4A
- YouTube title: Optimizing Load Balancing and Autoscaling for Large Language Model (LLM) Inference on Kub... D. Gray
- Match score: 1.016
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/optimizing-load-balancing-and-autoscaling-for-large-language-model-llm/TSEGAh1bs4A.txt
- Transcript chars: 39613
- Keywords: requests, basically, balancing, replicas, performance, replica, native, llm, inference, latency, scaling, better, tokens, request, running, results, custom, number

### Resumo baseado na transcript

my talk is called optimizing load balancing and auto scaling for llm inference on kubernetes I know that's kind of a mouthful U but let's just get right into it um first uh personal introduction I'm David um I work for Red Hat I'm a performance engineer I'm based out of Toronto Canada in the past like a couple years ago I was working mostly on kuber kubernetes operator development um for out of tree kernel driver enablement and node tuning uh but then for the last like almost two

### Excerpt da transcript

my talk is called optimizing load balancing and auto scaling for llm inference on kubernetes I know that's kind of a mouthful U but let's just get right into it um first uh personal introduction I'm David um I work for Red Hat I'm a performance engineer I'm based out of Toronto Canada in the past like a couple years ago I was working mostly on kuber kubernetes operator development um for out of tree kernel driver enablement and node tuning uh but then for the last like almost two years now I've been just focused on on llm inference performance on kubernetes part of the performance and scale for AI platforms team at Red Hat um and our kind of mission is to make AI applications run better and faster on Linux and containers and kubernetes um so in this talk I'm going to start with a little bit of background information about llm inference and llm inference performance Concepts if you're in here for the previous talk there might be a tiny bit of review here um but I'll try to keep it brief um then I'm going to talk about different ways to deploy LM on kubernetes so I'll show sort of the vanilla way um and then I'll introduce the kerve project um then I'm going to show some comparisons of load balancing performance when you're deploying multiple replicas of a model uh the vanilla way versus with kerve um and then I'm also going to show some results with custom load balancing um and then lastly I'll discuss some issues involved in autoscaling and share some techniques to speed up the scaleup process of new model replicas um and I hope to leave some time for Q&A at the end I have lot to get through so we'll see how that goes but please hold your questions till the end um okay so first the background so yeah by now I think most of us are pretty familiar with how llms work at a high level it's been kind of hard to ignore but just looking at this diagram on the left I want to highlight first how llms are de or llms process text as tokens so the incoming text is decomposed into tokens which map to words or subw pieces of text um I also want to note how text generation is an autor regressive process so the next token is based on the previous tokens in the sequence so basically to generate a long string of output the model needs to be run over and over again um each time kind of adding the previous output token into the input sequence to generate the next token um and this occurs until either a max number of tokens is reached or the model predicts the stop token uh whi
