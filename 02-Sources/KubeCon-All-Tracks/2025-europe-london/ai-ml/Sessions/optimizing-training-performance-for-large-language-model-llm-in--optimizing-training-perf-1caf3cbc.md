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
speakers: ["Klaus Ma", "NVIDIA", "Peng Gu", "Tech Starup"]
sched_url: https://kccnceu2025.sched.com/event/1tx9A/optimizing-training-performance-for-large-language-modelllm-in-kubernetes-klaus-ma-nvidia-peng-gu-tech-starup
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+Training+Performance+for+Large+Language+Model%28LLM%29+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Optimizing Training Performance for Large Language Model(LLM) in Kubernetes - Klaus Ma, NVIDIA & Peng Gu, Tech Starup

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Klaus Ma, NVIDIA, Peng Gu, Tech Starup
- Schedule: https://kccnceu2025.sched.com/event/1tx9A/optimizing-training-performance-for-large-language-modelllm-in-kubernetes-klaus-ma-nvidia-peng-gu-tech-starup
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+Training+Performance+for+Large+Language+Model%28LLM%29+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Optimizing Training Performance for Large Language Model(LLM) in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9A/optimizing-training-performance-for-large-language-modelllm-in-kubernetes-klaus-ma-nvidia-peng-gu-tech-starup
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+Training+Performance+for+Large+Language+Model%28LLM%29+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JXcQcofGzrA
- YouTube title: Optimizing Training Performance for Large Language Model(LLM) in Kubernetes - Klaus Ma & Peng Gu
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/optimizing-training-performance-for-large-language-model-llm-in-kubern/JXcQcofGzrA.txt
- Transcript chars: 21987
- Keywords: volcano, network, topology, feature, scheduling, gpu, training, basically, several, support, networking, performance, actually, running, define, instead, resource, discovery

### Resumo baseado na transcript

So we want to give introduction about our work uh to optimize optimize the training performance for uh large language model uh increment. So we want to give introduction about this part uh about uh about ourself who we are here. topological where scheduling this is major for the task topologic such as the PS worker mode in test and flow part we have performance and when you check the history of volcano you can get the performance report about this part and today topic is I will give a quick introduction and the P will give a demo for the what we have done uh in last year and the third one is I think is in pipeline for in our pipeline the right for for example we have dataware scheduling for example we have all information about the scheduling so we will try to do the something like data preloading to save the effort or save the improve the performance of the work the whole workload Right. For example, we keep the backward compatibility in the uh in the upstream and we import all the things from the Kubernetes default and we also build our own differentation uh scheduling part such as list in the previous uh slides for example DRF and

### Excerpt da transcript

This is Claus and this is Pong. So we want to give introduction about our work uh to optimize optimize the training performance for uh large language model uh increment. We did lots of work for this in the in the last year. So we want to give introduction about this part uh about uh about ourself who we are here. Uh this is Claus from Nvidia. I am the founder uh co-founder of Volcano. Currently, I joined the Avida for about three years focus on the network part you know uh for this this one. Yeah, I'm Pong. I'm from a technical startup. Uh we're still in sales mode. So that's why I'm not showing my company name on there. Okay, great. Yeah. So we are talking about uh um L one uh performance enhancement. But before that uh I want to some kind of discussion about what when we talking about I think in K uh this group conf we have lots of discussion about batch system right so at least in my point that batch system is trying to help us to manage the workload right including the workload life cycle fing and several things.

The the other important thing related to this topic is that our major task is to match the design performance of hardware right for the hardware we including the computing results right GPU DPO we incrementing several things and the other thing is the networking part I think this is the today's topic so what we have done about this part for networking resource we have infinite band we have rocky and bund wise healthy and also the latency is also important for large language modeling. And the third one I think is also storage things right. We have cache, we have local disk and we also have you know distri distributed a storage future for some processor data also several important things right this is a common things of badge system every badge system should handle related stuff for this brand. The another thing is that based on the batch system define what uh we want to build for batch system we have a volcano here right for volcano this is a how to say banner or the description of volcano parts of volcano project so volcano is a cf incubating project and it is the first batch scheduling system in CNCF it's start from cool batch since uh uh 2017 this is the long time ago we build lots of features and based on the badge system what we want to build now the first one is the computing resource we build lots of feature to enhance GPU and CPU resource usage now the first one we we list lots of feature here such as the dominator resource fair fair s
