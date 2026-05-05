---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Aditya Soni", "Forrester Research", "Hrittik Roy", "vCluster"]
sched_url: https://kccncna2025.sched.com/event/27Feq/help-my-llm-is-a-resource-hog-how-we-tamed-inference-with-kubernetes-and-open-source-muscle-aditya-soni-forrester-research-hrittik-roy-vcluster
youtube_search_url: https://www.youtube.com/results?search_query=Help%21+My+LLM+Is+a+Resource+Hog%3A+How+We+Tamed+Inference+With+Kubernetes+and+Open+Source+Muscle+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Help! My LLM Is a Resource Hog: How We Tamed Inference With Kubernetes and Open Source Muscle - Aditya Soni, Forrester Research & Hrittik Roy, vCluster

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Aditya Soni, Forrester Research, Hrittik Roy, vCluster
- Schedule: https://kccncna2025.sched.com/event/27Feq/help-my-llm-is-a-resource-hog-how-we-tamed-inference-with-kubernetes-and-open-source-muscle-aditya-soni-forrester-research-hrittik-roy-vcluster
- Busca YouTube: https://www.youtube.com/results?search_query=Help%21+My+LLM+Is+a+Resource+Hog%3A+How+We+Tamed+Inference+With+Kubernetes+and+Open+Source+Muscle+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Help! My LLM Is a Resource Hog: How We Tamed Inference With Kubernetes and Open Source Muscle.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Feq/help-my-llm-is-a-resource-hog-how-we-tamed-inference-with-kubernetes-and-open-source-muscle-aditya-soni-forrester-research-hrittik-roy-vcluster
- YouTube search: https://www.youtube.com/results?search_query=Help%21+My+LLM+Is+a+Resource+Hog%3A+How+We+Tamed+Inference+With+Kubernetes+and+Open+Source+Muscle+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=z9yK5W6whQI
- YouTube title: Help! My LLM Is a Resource Hog: How We Tamed Inference With Kubernetes... Aditya Soni & Hrittik Roy
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/help-my-llm-is-a-resource-hog-how-we-tamed-inference-with-kubernetes-a/z9yK5W6whQI.txt
- Transcript chars: 24578
- Keywords: gpu, inference, actually, across, request, cost, trying, together, architecture, around, response, training, better, issues, particular, performance, caching, always

### Resumo baseado na transcript

So today we're going to have a talk on how you can make your alm team for inference and when it's having more resource hog before starting uh let me just go through with like what's how the agenda look like for today. So we'll be starting with very basic like how the what are the LLMs then we're going to move to why maybe we go through the history of it. So it's implemented in your research cycles, revenue gains, cost savings for sure when you are optimizing costs around different sectors. And the basic architecture of LMS is mostly like where we have couple of things. So whenever we want to train or fine-tune something we want massive parallel computation and for that uh there is high dimensional data matrix multiplications which we are doing and transforms out of different form of architecture which helps you to build those and reduce your training time so that you have better and faster training and inference loop in comparison to other architectures which were there.

### Excerpt da transcript

Okay. Um, good afternoon everyone. Welcome you all to the last sessions of for today. So today we're going to have a talk on how you can make your alm team for inference and when it's having more resource hog before starting uh let me just go through with like what's how the agenda look like for today. So we'll be starting with very basic like how the what are the LLMs then we're going to move to why maybe we go through the history of it. We will jump to the transformers and then we going to move towards like uh what make your alum resource hog and then how we need to fix it. Later on we going to move towards the three focus area that we have analyzed and we going to break them down later on like we do have some architecture some good benchmarks and results for you and key takeaways. Before starting let me introduce myself. Uh I'm Sunni. I'm one of the SREs working at Forester. Uh apart from that I'm one of the CN ambassador before this I worked at Red Hat and more with me I have Ryik. >> So hi everyone I'm Ryik Roy and I'm a platform advocate at Vcluster apart from that I'm a CNCF ambassador and a Google banget scholar.

So I've done couple of certification and most of my times are focus on figuring around Kubernetes elements and all. So elements are everywhere right now and it is called the brain behind modern AI. So every time every day we interact with them in various ways like if you are using a chat w if you are talking with a lot of uh chat GBD and all those things. So LMS are everywhere and they have a lot of more common use cases over the hype. So it's implemented in your research cycles, revenue gains, cost savings for sure when you are optimizing costs around different sectors. And the basic architecture of LMS is mostly like where we have couple of things. So as you see the client and response. So whenever you go interact with charg you just add a text or something and get a reply. Maybe it's a video token or a audio token or a text token. It can be anything but what you expecting from LLM is a response but it is very simple to think that it's giving but at the background there is so many things happening including there is a tokenizer which breaks down your text and queries into tokens.

Then we have router batcher and then all those KV caches are stored and at the end there's inference happening and the pros of inference is like you are getting a response through LLMs where they are going through their previous batch data and trying to find s
