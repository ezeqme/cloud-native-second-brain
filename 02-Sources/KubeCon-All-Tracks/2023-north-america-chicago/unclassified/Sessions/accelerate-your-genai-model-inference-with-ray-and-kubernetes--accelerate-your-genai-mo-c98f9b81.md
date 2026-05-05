---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Richard Liu", "Google Cloud"]
sched_url: https://kccncna2023.sched.com/event/1R2vH/accelerate-your-genai-model-inference-with-ray-and-kubernetes-richard-liu-google-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Accelerate+Your+GenAI+Model+Inference+with+Ray+and+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Accelerate Your GenAI Model Inference with Ray and Kubernetes - Richard Liu, Google Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Richard Liu, Google Cloud
- Schedule: https://kccncna2023.sched.com/event/1R2vH/accelerate-your-genai-model-inference-with-ray-and-kubernetes-richard-liu-google-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Accelerate+Your+GenAI+Model+Inference+with+Ray+and+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Accelerate Your GenAI Model Inference with Ray and Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vH/accelerate-your-genai-model-inference-with-ray-and-kubernetes-richard-liu-google-cloud
- YouTube search: https://www.youtube.com/results?search_query=Accelerate+Your+GenAI+Model+Inference+with+Ray+and+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FZ9XML4KaiY
- YouTube title: Accelerate Your GenAI Model Inference with Ray and Kubernetes - Richard Liu, Google Cloud
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/accelerate-your-genai-model-inference-with-ray-and-kubernetes/FZ9XML4KaiY.txt
- Transcript chars: 18828
- Keywords: cluster, models, allows, single, worker, deploy, inference, topology, diffusion, deployed, stable, application, generative, running, library, request, endpoint, performance

### Resumo baseado na transcript

hi everyone my name is Richard I am a senior software engineer at Google cloud and today I'm excited to talk to you about how you can accelerate your gen model inference with Ray and kubernetes over the past year we're seeing a lot of growth in large models in the field of uh generative Ai and this has enabled organizations to apply Ai and solve problems that they weren't able to solve before and this in turn is uh driving larger and lar larger models and over the past

### Excerpt da transcript

hi everyone my name is Richard I am a senior software engineer at Google cloud and today I'm excited to talk to you about how you can accelerate your gen model inference with Ray and kubernetes over the past year we're seeing a lot of growth in large models in the field of uh generative Ai and this has enabled organizations to apply Ai and solve problems that they weren't able to solve before and this in turn is uh driving larger and lar larger models and over the past few years we're seeing orders of magnitude growth in the size of these models uh so this uh basically means that the organizations have to adopt technologies that allows them to serve models in a performant and um coste effective manner so uh Google has been an industry leader in the field of AI and uh with products like Maps search YouTube Etc there are a lot of large models running underneath these services so over the past uh decades Google has uh built a lot of uh specialized Hardware uh specifically tatered for machine learning applications uh now one of these is uh tensor processing units which is uh tpus we recently introduced a V5 of tpus which is the latest generations of tpus and in doing so we want to um allow our customers to have the same access to the transformative technologies that has enabled Google in its uh products and services so the two main benefits of tpus are efficiency and scalability so let's like take a look at the efficiency uh in this graph we're comparing the V5 tpus with their previous generation the V4 tpus and over the horizontal axis we're seeing how the V5 tpus perform on various uh generative AI models and in the hor in the vertical axis we're seeing the U relative inference performance per dollar so as you can see uh over the range of these models the v5s tpus are demonstrating up to 2.5 times more throughput per dollar for generative AI model next we're going to look at scalability as a main benefit uh tpus have a special topology and as well as a high bandwidth memory which allows them to work either in unison or in combination with other TP sizes uh so in this table we're demonstrating how this uh relates to uh how it serves the different kinds of models um you can see that U with a one V5 dpu chip you can serve a 13 billion llama 2 model uh however you can scale that up you can scale up to 256 chips which allows you to serve up to uh two parameter models um in addition uh multi slice technology allows near linear scaling with these models so you can
