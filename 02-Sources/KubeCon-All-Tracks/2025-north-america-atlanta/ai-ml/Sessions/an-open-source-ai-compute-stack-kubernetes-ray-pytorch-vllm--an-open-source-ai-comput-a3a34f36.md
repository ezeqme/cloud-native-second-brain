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
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Robert Nishihara", "Anyscale"]
sched_url: https://kccncna2025.sched.com/event/27Few/an-open-source-ai-compute-stack-kubernetes-+-ray-+-pytorch-+-vllm-robert-nishihara-anyscale
youtube_search_url: https://www.youtube.com/results?search_query=An+Open+Source+AI+Compute+Stack%3A+Kubernetes+%2B+Ray+%2B+PyTorch+%2B+VLLM+CNCF+KubeCon+2025
slides: []
status: parsed
---

# An Open Source AI Compute Stack: Kubernetes + Ray + PyTorch + VLLM - Robert Nishihara, Anyscale

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Robert Nishihara, Anyscale
- Schedule: https://kccncna2025.sched.com/event/27Few/an-open-source-ai-compute-stack-kubernetes-+-ray-+-pytorch-+-vllm-robert-nishihara-anyscale
- Busca YouTube: https://www.youtube.com/results?search_query=An+Open+Source+AI+Compute+Stack%3A+Kubernetes+%2B+Ray+%2B+PyTorch+%2B+VLLM+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre An Open Source AI Compute Stack: Kubernetes + Ray + PyTorch + VLLM.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Few/an-open-source-ai-compute-stack-kubernetes-+-ray-+-pytorch-+-vllm-robert-nishihara-anyscale
- YouTube search: https://www.youtube.com/results?search_query=An+Open+Source+AI+Compute+Stack%3A+Kubernetes+%2B+Ray+%2B+PyTorch+%2B+VLLM+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4o2amJxMHUc
- YouTube title: An Open Source AI Compute Stack: Kubernetes + Ray + PyTorch + VLLM - Robert Nishihara, Anyscale
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/an-open-source-ai-compute-stack-kubernetes-ray-pytorch-vllm/4o2amJxMHUc.txt
- Transcript chars: 31608
- Keywords: learning, inference, running, workload, actually, workloads, training, source, reinforcement, systems, container, pytorch, little, question, working, processing, foundation, models

### Resumo baseado na transcript

I'm going to talk a little bit about the uh, so I've been working on an open source project called Ray. And I'm going to talk a little bit about the open-source software stack that we see emerging for uh, supporting today's AI workloads. Um, so this Philip and Yan and myself, we were or Philip and I were um doing reinforcement learning research and deep learning training research. And it became pretty clear early on that the existing distributed systems that people had at the time um weren't really designed for reinforcement learning, weren't really designed for large scale AI workloads. Um, but everyone in machine learning at the time was kind of building their own distributed systems in order to run their experiments. And everyone was excited about reinforcement learning at the time for gaming um and you know Atari and Alph Go and things like that.

### Excerpt da transcript

All right. Um, thank you guys. Thank you all for coming. So, I'm Robert. I'm going to talk a little bit about the uh, so I've been working on an open source project called Ray. And I'm going to talk a little bit about the open-source software stack that we see emerging for uh, supporting today's AI workloads. And that involves Kubernetes plus Ray plus PyTorch and VLM. And I'll talk a little bit more about how they relate to each other, you know, how they get used to with each other. Um, kind of the different responsibilities that each of these and different problems that each of these solve. But, uh, I'm going to start by trying to motivate this a little bit with how AI workloads have changed because the, um, AI workloads that we see people running today look very different from say 5 years ago. I'm going to talk a little bit about what Ray is because actually can you raise your hand if you've heard of Ray before for what about if you've used Ray personally. Okay, so smaller number. Um I'm going to share a little bit about just Ray's uh actor abstraction because I think that's um one of the things that uh well that I really like about Ray and then I'll talk a little bit about the how it fits into the rest of the tech stack.

Um so this is an open source project we started back at Berkeley actually we were doing originally not working on systems. Um, so this Philip and Yan and myself, we were or Philip and I were um doing reinforcement learning research and deep learning training research. And it became pretty clear early on that the existing distributed systems that people had at the time um weren't really designed for reinforcement learning, weren't really designed for large scale AI workloads. You know, we tried building some of this stuff on top of Spark, we tried using various HPC systems. Um, but everyone in machine learning at the time was kind of building their own distributed systems in order to run their experiments. And so we got started building tools not because our goal is to build tools, but actually uh we just thought we needed it for ourselves. And everyone was excited about reinforcement learning at the time for gaming um and you know Atari and Alph Go and things like that. And of course, um, so it's very interesting to see things coming full circle and everyone, uh, you know, reinforcement learning really being used now to build reasoning models and agents and and being so impactful.

Um, but at the time it wasn't that big of a community
