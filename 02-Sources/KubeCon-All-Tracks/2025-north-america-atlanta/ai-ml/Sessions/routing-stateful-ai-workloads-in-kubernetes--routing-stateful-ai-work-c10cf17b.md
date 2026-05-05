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
speakers: ["Maroon Ayoub", "IBM", "Michey Mehta", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27FX6/routing-stateful-ai-workloads-in-kubernetes-maroon-ayoub-ibm-michey-mehta-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Routing+Stateful+AI+Workloads+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Routing Stateful AI Workloads in Kubernetes - Maroon Ayoub, IBM & Michey Mehta, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Maroon Ayoub, IBM, Michey Mehta, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27FX6/routing-stateful-ai-workloads-in-kubernetes-maroon-ayoub-ibm-michey-mehta-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Routing+Stateful+AI+Workloads+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Routing Stateful AI Workloads in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FX6/routing-stateful-ai-workloads-in-kubernetes-maroon-ayoub-ibm-michey-mehta-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Routing+Stateful+AI+Workloads+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-C76naL3PRc
- YouTube title: Routing Stateful AI Workloads in Kubernetes - Maroon Ayoub, IBM & Michey Mehta, Red Hat
- Match score: 0.774
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/routing-stateful-ai-workloads-in-kubernetes/-C76naL3PRc.txt
- Transcript chars: 24634
- Keywords: tokens, pretty, prefix, memory, important, inference, standard, question, prompt, workload, workloads, disagregation, attention, precise, queuing, particular, replica, bottom

### Resumo baseado na transcript

I lead the KV disagregation SIG in LMD a project you'll hear about in this talk. So what you'll get today in this talk, you'll learn the single most important metric in inference in AI production. And in one of their blogs they wrote the KV cache hit it is the single most important metric for production stage AI. And this talk will will show you how these how Kubernetes or standard Kubernetes destroys these savings and why it doesn't work out of the box for AI inference. So we now briefly we now understand Kevy cache slightly and its its applications in in a single instance and we'll talk about where Kubernetes or standard Kubernetes load balancing fails. So you get a real-time global view of KV cache across all your instances uh in a Kubernetes native implementation that builds on top of uh the Kubernetes gateway API inference extension in what we call the LMD inferenceuler which implements precise prefix cache aware

### Excerpt da transcript

Uh hello everyone. Thank you for coming to our talk. We'll be presenting route routing stateful AI workloads in Kubernetes. Uh what's stateful in EI where Kubernetes fails and show some data. I'm Aruna Yub. I work at IBM research. I lead the KV disagregation SIG in LMD a project you'll hear about in this talk. >> And hi, I'm Mishi Ma. I work on performance at Red Hat. >> Okay. So what you'll get today in this talk, you'll learn the single most important metric in inference in AI production. You'll understand why standard Kubernetes load balancing fails to deliver in in for AI uh inference. You'll understand what LMD is and how LMD solves this problem in a Kubernetes native manner. and you'll see real world data showing uh how LMD unlocks uh the potential of your hardware. We'll start with a joke. So, two LMs walk into a bar. The first orders a beer. The bartender goes, "Uh, that will be three bucks." The second say, "Same for me, but I'm paying cash." This joke captures part of the essence of what we we'll be talking about.

We'll dive into what paying cash means and why it's super important for inference. So we're starting with the 10x cost problem. Uh what we're presenting really affects your bottom line inference production. Without these optimizations, you'll be pretty much paying 10x than you have to and you'll be under utilizing your resources. So I'm starting with a with a quote from a Manus blog. Manus is an an agent uh startup that popped a while ago. And in one of their blogs they wrote the KV cache hit it is the single most important metric for production stage AI. It directly affects your latency and cost. And you you really see this theme around in uh mainstream API mainstream AI such as open AIS, Antropic uh Google's if you check the pricing pages you can see for GPT5 uh you pay uh back end a quarter for per 1 million uncashed tokens and 10x less for 1 million cash tokens. The same can be seen in cloet and pretty much all uh mainstream AI pricing. And this talk will will show you how these how Kubernetes or standard Kubernetes destroys these savings and why it doesn't work out of the box for AI inference.

So some background to get the idea the most important factor here is the KV cache. So what is the KV cache really? So to start there I'll go about I'll go over self attention in high level. Self attention is how transformers or transformer models understand context. Attention captures relations between different topics in different possessi
