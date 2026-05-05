---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Rohit Ghumare", "Taikun", "Joinal Ahmed", "NTG"]
sched_url: https://kccnceu2025.sched.com/event/1txCb/securing-ai-workloads-building-zero-trust-architecture-for-llm-applications-rohit-ghumare-taikun-joinal-ahmed-ntg
youtube_search_url: https://www.youtube.com/results?search_query=Securing+AI+Workloads%3A+Building+Zero-Trust+Architecture+for+LLM+Applications+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Securing AI Workloads: Building Zero-Trust Architecture for LLM Applications - Rohit Ghumare, Taikun & Joinal Ahmed, NTG

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Rohit Ghumare, Taikun, Joinal Ahmed, NTG
- Schedule: https://kccnceu2025.sched.com/event/1txCb/securing-ai-workloads-building-zero-trust-architecture-for-llm-applications-rohit-ghumare-taikun-joinal-ahmed-ntg
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+AI+Workloads%3A+Building+Zero-Trust+Architecture+for+LLM+Applications+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Securing AI Workloads: Building Zero-Trust Architecture for LLM Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txCb/securing-ai-workloads-building-zero-trust-architecture-for-llm-applications-rohit-ghumare-taikun-joinal-ahmed-ntg
- YouTube search: https://www.youtube.com/results?search_query=Securing+AI+Workloads%3A+Building+Zero-Trust+Architecture+for+LLM+Applications+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qXEvqZ_cY0o
- YouTube title: Securing AI Workloads: Building Zero-Trust Architecture for LLM Appl... Rohit Ghumare & Joinal Ahmed
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/securing-ai-workloads-building-zero-trust-architecture-for-llm-applica/qXEvqZ_cY0o.txt
- Transcript chars: 24647
- Keywords: llm, actually, access, security, gateway, similarly, models, control, happens, everyone, concern, prompt, talked, server, injection, architecture, nothing, request

### Resumo baseado na transcript

So yeah uh we will be talking about uh securing AI workloads and how you can build zerorust architecture in LLM applications. uh because you know like nowadays everyone wants to implement LLM applications they just go download that dips package and try to implement so it doesn't work like that right so we will try to see what we can do and all and also we So according to feedback by uh technical team of PTEC who governs this uh they found like software packages uploaded by this users mainly involve uh your information collection then environment variable which talked about then also S3 object object uh storage access so it was a big concern. this uh one of them is really popular hugging face then there is GPDJ uh bloom open llama these are the some of the examples which people try similarly everyone's favorite year containerization with the Kubernetes. Similarly, cloud APIs which we talked about is like one a few of the examples is like open AI API, SageMaker, then your Vert.x AI but it is easy to deploy and all but scalable but really costly and uh you you lack your control. Similarly, there is onremise onremise where you can provide highest control and privacy but uh that comes with the high infra cost.

### Excerpt da transcript

Hello everyone. So yeah uh we will be talking about uh securing AI workloads and how you can build zerorust architecture in LLM applications. uh because you know like nowadays everyone wants to implement LLM applications they just go download that dips package and try to implement so it doesn't work like that right so we will try to see what we can do and all and also we will go Gibli style because quite a trending nowadays right so here I am so I'm Rohit and I am also CNCF ambassador as well as CNCF marketing chair and currently working this consultancy uh devel service and I'm also organizing KCD UK and CNC best met so yeah this will be this year we we are doing KCD UK Edinra so if you are there please attend so uh what we are going to cover today so we are going to cover like how you can uh how uh LLMs are there and overview of what LLMs are and uh how uh how the deployment of LLMs work then as well as what AI gateways are and how they can help as well as we will talk about implementing uh security in LLMs.

Then we will also uh show you like uh opensource landscape which I built for the zero trust security. So let's go forward and at the end I will show you little demo of something I built for the kubernetes and which uh I guess CNCF and all of the uh heads are also promoting it. So let's see what it is. So what are LLM? So if you I guess everyone knows here. So not going in depth into it but yeah LLM is just nothing but your intelligent m intelligent mechanism of like artificial intelligence but uh it is used for your natural language processing task and all and if you are coming from the background like me for like uh training the engram models and llm's using lm pdz and all so this is quite trending world now right so yeah let's go forward and also I don't want your company to be here. So please bear with me at the end and we will see how it goes. So these are the some security uh incidents uh I would like to share. Uh one of them is a vis research. Uh so v research discovered that uh there was a critical container uh escape uh uh vulnerability CV we talk about right uh in Nvidia container toolkit and it is used by a lot of companies right and discovering it is like really big concern and it is been discussed all over in different different papers.

So attacker take control of the host from a container and this shows that when the underlying your infra inside the LLMs uh they are also not reliable in this case they are they can be also vulnerable ri
