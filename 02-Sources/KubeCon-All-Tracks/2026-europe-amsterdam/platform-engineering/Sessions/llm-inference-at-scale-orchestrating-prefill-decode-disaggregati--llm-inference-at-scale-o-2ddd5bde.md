---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "SRE Reliability"]
speakers: ["Zhonghu Xu", "Huawei Technologies Co.", "Ltd"]
sched_url: https://kccnceu2026.sched.com/event/2CW01/llm-inference-at-scale-orchestrating-prefill-decode-disaggregation-zhonghu-xu-huawei-technologies-co-ltd
youtube_search_url: https://www.youtube.com/results?search_query=LLM+Inference+at+Scale%3A+Orchestrating+Prefill-Decode+Disaggregation+CNCF+KubeCon+2026
slides: []
status: parsed
---

# LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu, Huawei Technologies Co., Ltd

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Zhonghu Xu, Huawei Technologies Co., Ltd
- Schedule: https://kccnceu2026.sched.com/event/2CW01/llm-inference-at-scale-orchestrating-prefill-decode-disaggregation-zhonghu-xu-huawei-technologies-co-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=LLM+Inference+at+Scale%3A+Orchestrating+Prefill-Decode+Disaggregation+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW01/llm-inference-at-scale-orchestrating-prefill-decode-disaggregation-zhonghu-xu-huawei-technologies-co-ltd
- YouTube search: https://www.youtube.com/results?search_query=LLM+Inference+at+Scale%3A+Orchestrating+Prefill-Decode+Disaggregation+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KtnD-wILqb0
- YouTube title: LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/llm-inference-at-scale-orchestrating-prefill-decode-disaggregation/KtnD-wILqb0.txt
- Transcript chars: 18021
- Keywords: decode, inference, actually, serving, gpu, scheduling, prefill, routing, router, prefer, disagregation, request, define, casina, experts, represent, volcano, deploy

### Resumo baseado na transcript

Today I'm going to talk about LM inference at scale especially how to orchestrate uh PD disagregation LM. Currently I will serve as the Sinc tech infra tech leader and also represent the east steering committee as a member as a maintainer of volcano and also kimsh and I have spent many years contributing to the uh modern orchestration. orchestration problems we have to look inside the model and inference happens in two distinct stages I mean the language model. Okay, in the AI world user user experience is defined by the two metrics uh TTFT actually is the time to first token and also the TPOT time put output token. Because of the interference we just discussed, a coupled architecture forces a painful trait trade-off. The indust industries answer to the interfer interference problem is prefail decode uh disagregation.

### Excerpt da transcript

Today I'm going to talk about LM inference at scale especially how to orchestrate uh PD disagregation LM. I'm Juni from Haw Club. Uh actually my name is a little bit hard to pronounce. Uh in Chinese who means tiger actually. Yeah. Uh first let's talk about my myself. My name is Junhu. Currently I will serve as the Sinc tech infra tech leader and also represent the east steering committee as a member as a maintainer of volcano and also kimsh and I have spent many years contributing to the uh modern orchestration. I'm very delighted dedicated to the open source. Yeah, you can find me with this GitHub. Yeah. Uh today we are going to explore the evolving landscape of AI infrastructure. Our discussion will center on how to move beyond traditional deployment patterns to build more efficient and cloud native system for large language models especially for distributed inference. Yeah, let's get to the first part. Uh, what's the current status of AM inference in Kubernetes? To understand why Cina exist, we first have to look at the last mile of AI production inference.

For many years, Kubernetes have has excelled at orchestrating statelessly microservices. But IM are completely different. They require gigabit. They require gigabit of waste to be loaded. They generate they generate massive skater in the form of k cache and they require strict gun scheduling for GPU resources. If you try to so if you try to manage LM using uh standard Kubernetes deployment or like u project lead set you actually fall into a D loop you would need to manage specific um resources one by Uh next uh to understand the orchestration problems we have to look inside the model and inference happens in two distinct stages I mean the language model. Yeah. First the prefill stage where the model injects your entire prompt. This is very highly parallel and extremely compute bound. Second, it is the decode st. Uh this is a very memory bandwide spawn. It is a procedure of generate tokens one by one. So it it is a very different stages. Uh so if we deploy the preail and decode in the same instance they may interference each other.

Yeah. May many times people run them in the same uh GPU instance. This cause the interfer interference problem problem. Image request A is a a very long prompt and it requires very high commute resources and suddenly request B arrives with a massive prompt. It also needs to use the uh compute resources and then sorry uh sorry I think from the picture left is prefer right
