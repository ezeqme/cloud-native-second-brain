---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Olivier Tardieu", "Yue Zhu", "IBM"]
sched_url: https://kccncna2024.sched.com/event/1i7oh/load-aware-gpu-fractioning-for-llm-inference-on-kubernetes-olivier-tardieu-yue-zhu-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Load-Aware+GPU+Fractioning+for+LLM+Inference+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Load-Aware GPU Fractioning for LLM Inference on Kubernetes - Olivier Tardieu & Yue Zhu, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Olivier Tardieu, Yue Zhu, IBM
- Schedule: https://kccncna2024.sched.com/event/1i7oh/load-aware-gpu-fractioning-for-llm-inference-on-kubernetes-olivier-tardieu-yue-zhu-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Load-Aware+GPU+Fractioning+for+LLM+Inference+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Load-Aware GPU Fractioning for LLM Inference on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oh/load-aware-gpu-fractioning-for-llm-inference-on-kubernetes-olivier-tardieu-yue-zhu-ibm
- YouTube search: https://www.youtube.com/results?search_query=Load-Aware+GPU+Fractioning+for+LLM+Inference+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HwWYb15wpOc
- YouTube title: Load-Aware GPU Fractioning for LLM Inference on Kubernetes - Olivier Tardieu & Yue Zhu, IBM
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/load-aware-gpu-fractioning-for-llm-inference-on-kubernetes/HwWYb15wpOc.txt
- Transcript chars: 35544
- Keywords: gpu, performance, models, actually, memory, number, showing, latency, essentially, throughput, request, fraction, possible, figure, slides, concurrent, attention, layers

### Resumo baseado na transcript

good afternoon um welcome to a session my name is Olivia T I'm a principal research scientist at IBM research and today I'm joined by yeah hi I'm y I'm the staff research scientist at IBM research and this afternoon we're going to talk about uh large language models and how we can try to better understand how they perform right these these problems comes from essentially what we've observed on our clusters right like I'm sure many of you we've observed that GP utilization is not as good as

### Excerpt da transcript

good afternoon um welcome to a session my name is Olivia T I'm a principal research scientist at IBM research and today I'm joined by yeah hi I'm y I'm the staff research scientist at IBM research and this afternoon we're going to talk about uh large language models and how we can try to better understand how they perform right these these problems comes from essentially what we've observed on our clusters right like I'm sure many of you we've observed that GP utilization is not as good as we' like it to be right and when we look at the reasons for that there's a number of reasons one is you know how do you get your cud kernel to perform as as well as we would like but the other one is simply that people don't quite know how to share gpus right they know how to share GP maybe in time uh this is not good maybe in time because you know I run for five minutes you run for five minutes and so on but when they have long running workloads and these workloads don't quite require an entire GPU we don't really have the mechanisms and the mental model yes to do this sharing so um there are really two problems there the first one is that act as of today kubernetes doesn't really help sharing gpus right and the second one is people don't really know how much of a GPU they need for their workloads right because again we have not really started this process of trying to understand how much we need and internalize as we have for CPU and memory consumption and and and these kind of things so in in in the platform side of things in fact we already had a talk on Tuesday at the cloud Aid where we describ how we're trying to make it easier on kubernetes to share gpus so I'm I'm not really going to Touch Too Much on that today what we're here to talk about is how do we know how much of uh uh how big a piece of a GPU how much of a fraction of a GPU we need to run a particular Model A large language model uh and an INF server on on a particular GPU so uh to briefly to to the talk I'm going to tell you a little bit more about the motivation why why why is it not entirely trivial to know how the per the the system is going a large language model is going to perform I'll briefly touch on how we can go after GPU fractioning I should mention here that this is the technique we're going to use in the demo but fundamentally the the the modeling the the the profiling approach we're discussing here has nothing to do with the particulars of how we're going to fraction GPU you could use that
