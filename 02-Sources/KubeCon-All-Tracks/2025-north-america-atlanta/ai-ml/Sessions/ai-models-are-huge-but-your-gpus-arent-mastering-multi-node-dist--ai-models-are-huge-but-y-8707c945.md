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
speakers: ["Ernest Wong", "Microsoft", "Jiaxin Shan", "Bytedance"]
sched_url: https://kccncna2025.sched.com/event/27FdL/ai-models-are-huge-but-your-gpus-arent-mastering-multi-node-distributed-inference-on-kubernetes-ernest-wong-microsoft-jiaxin-shan-bytedance
youtube_search_url: https://www.youtube.com/results?search_query=AI+Models+Are+Huge%2C+but+Your+GPUs+Aren%E2%80%99t%3A+Mastering+Multi-Node+Distributed+Inference+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# AI Models Are Huge, but Your GPUs Aren’t: Mastering Multi-Node Distributed Inference on Kubernetes - Ernest Wong, Microsoft & Jiaxin Shan, Bytedance

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Ernest Wong, Microsoft, Jiaxin Shan, Bytedance
- Schedule: https://kccncna2025.sched.com/event/27FdL/ai-models-are-huge-but-your-gpus-arent-mastering-multi-node-distributed-inference-on-kubernetes-ernest-wong-microsoft-jiaxin-shan-bytedance
- Busca YouTube: https://www.youtube.com/results?search_query=AI+Models+Are+Huge%2C+but+Your+GPUs+Aren%E2%80%99t%3A+Mastering+Multi-Node+Distributed+Inference+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre AI Models Are Huge, but Your GPUs Aren’t: Mastering Multi-Node Distributed Inference on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FdL/ai-models-are-huge-but-your-gpus-arent-mastering-multi-node-distributed-inference-on-kubernetes-ernest-wong-microsoft-jiaxin-shan-bytedance
- YouTube search: https://www.youtube.com/results?search_query=AI+Models+Are+Huge%2C+but+Your+GPUs+Aren%E2%80%99t%3A+Mastering+Multi-Node+Distributed+Inference+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MQR8jyTR5QE
- YouTube title: AI Models Are Huge, but Your GPUs Aren’t: Mastering Multi-Node Distributed Infe... E. Wong & J. Shan
- Match score: 0.966
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ai-models-are-huge-but-your-gpus-arent-mastering-multi-node-distribute/MQR8jyTR5QE.txt
- Transcript chars: 27980
- Keywords: gpu, decode, parallelism, models, single, memory, network, multiple, pipeline, within, workers, inference, deployment, strategy, attention, worker, latency, second

### Resumo baseado na transcript

Uh we're here to talk about a problem that many of us starting to face. In this talk, we're going to share how the industry is tackling this challenge with Kubernetes. We're going to show you uh architecture special deployment strategy for prefield decode disagregations and a benchmark in Kubernetes to prove it works. I I recommend you guys to go check out the LMD talks tomorrow which will talk about why EP with VLM and Kubernetes. Okay, let's double click on step two, model fitting, because this is where we hit our first two big problems. This has very low communication overheads comparing to tensor parallelism, but it can lead to problems like pipeline bubbles where GPUs are sitting idles waiting for previous pipeline stage, which means you might not be able to maximize your GPU utilizations.

### Excerpt da transcript

Hey everyone, I'm Ernest. I'm a software engineer at Microsoft and I'm joined by Joshin. Uh we're here to talk about a problem that many of us starting to face. Our AI models are getting huge, but our GPUs aren't. In this talk, we're going to share how the industry is tackling this challenge with Kubernetes. Now, to make sure we're on the same page, we're going to structure this talk in two halves. The first 15 minutes or so will be less about Kubernetes, but more about giving the basic context on how to serve these large language model in general. We'll cover the fundamental concepts and challenges. The context is really important because it'll give you the foundations you need to understand the second half of the talk where we'll deep dive into the Kubernetes strategies, architectures, and benchmarks. Now, before we deep dive, I want to give a special shout out to Professor Ha Jang from UCSD. He generously allowed us to use some of his slides and diagrams from his previous talks which do a fantastic jobs of illustrating some of the core concepts we're going to talk about today.

Okay, in this talk we're going to start with the why, the motivations for taking on this challenge in the first place. Then we're going to break down the how into a four-step process. And after that we're going to look at strategies based on model size because a billion parameters model has very different needs than a 100 billion parameters model. And finally part four we're going to get practical. We're going to show you uh architecture special deployment strategy for prefield decode disagregations and a benchmark in Kubernetes to prove it works. We'll also cover the critical topics of fault tolerance. All right let's start at the beginning. Why go through all this trouble? As you all know, GPU nodes are super expensive and requires a dedicated team of platform engineers to maintain. But self-hosting on Kubernetes give you three main advantage. First, full control over data and privacy. When you use thirdparty API, your sensitive data leaves your environment and by self-hosting, your data stay in-house and you know it's not being used by someone else training.

Second, model customization. You can fine-tune these models on your own proprietary data. You get to optimize the entire inference pipeline for your exact business needs, not just what the API providers decide to offer. And third, predictable costs. Those per tokens and per request charges from managed service can be un u
