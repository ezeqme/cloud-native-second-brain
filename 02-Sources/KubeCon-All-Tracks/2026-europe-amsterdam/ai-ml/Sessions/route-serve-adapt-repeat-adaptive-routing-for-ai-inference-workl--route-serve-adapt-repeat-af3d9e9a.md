---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Nir Rozenbaum", "Red Hat", "Kellen Swain", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW2C/route-serve-adapt-repeat-adaptive-routing-for-ai-inference-workloads-in-kubernetes-nir-rozenbaum-red-hat-kellen-swain-google
youtube_search_url: https://www.youtube.com/results?search_query=Route%2C+Serve%2C+Adapt%2C+Repeat%3A+Adaptive+Routing+for+AI+Inference+Workloads+in+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workloads in Kubernetes - Nir Rozenbaum, Red Hat & Kellen Swain, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nir Rozenbaum, Red Hat, Kellen Swain, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW2C/route-serve-adapt-repeat-adaptive-routing-for-ai-inference-workloads-in-kubernetes-nir-rozenbaum-red-hat-kellen-swain-google
- Busca YouTube: https://www.youtube.com/results?search_query=Route%2C+Serve%2C+Adapt%2C+Repeat%3A+Adaptive+Routing+for+AI+Inference+Workloads+in+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workloads in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2C/route-serve-adapt-repeat-adaptive-routing-for-ai-inference-workloads-in-kubernetes-nir-rozenbaum-red-hat-kellen-swain-google
- YouTube search: https://www.youtube.com/results?search_query=Route%2C+Serve%2C+Adapt%2C+Repeat%3A+Adaptive+Routing+for+AI+Inference+Workloads+in+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DxWAsFl9EAA
- YouTube title: Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workl... Nir Rozenbaum & Kellen Swain
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/route-serve-adapt-repeat-adaptive-routing-for-ai-inference-workloads-i/DxWAsFl9EAA.txt
- Transcript chars: 18290
- Keywords: inference, routing, gateway, adaptive, imbalance, request, scores, detector, control, server, prefix, endpoint, config, signal, specifically, prompt, prefill, wanted

### Resumo baseado na transcript

Today we'll be talking about adaptive routing for AI inference, specifically in inference gateway or the gateway inference extension as it's also known. My co-speaker Near was un unavailable to attend, but we'll hear from him in a recording in just a minute. Well uh I will mention and people probably here know that uh inference and specifically inference routing is not a solved problem. Well, we can treat this like a dynamic programming problem because of the way that the KV cache is generated and how attention works. So basically your L4 load balancer or a Kubernetes service that you would just deploy naively. The waiting is manually tuned and with if it's not tuned correctly with your prefix scoring you can have the thundering herd problem as as people who are load balancing uh experts would know and that can often cause your model server a single model server to be overloaded.

### Excerpt da transcript

All right. Hello. Hello. Thanks for coming to my talk today. Today we'll be talking about adaptive routing for AI inference, specifically in inference gateway or the gateway inference extension as it's also known. For an introduction, I'm Kellen. I'm a software engineer at Google. I specifically work on the inference team on GKE. My co-speaker Near was un unavailable to attend, but we'll hear from him in a recording in just a minute. So, first things first, uh I hope that you all figure out how inference gateway works. Uh what makes it great and useful today, some of the shortcomings we found, why what we're doing today, the adaptive routing can help, some other ways we're also exploring this problem, and then if you want to join, want to help, uh please do. And I'll give you links there. So, what is this? Why do you care? Uh this this talk is intended to be to be targeted to anyone at KubeCon. So my quick elevator pitch is that inference routing requires looking at the body specifically for things like prompt content or the model name if you're doing uh PEFT routing like Laura.

So to do that we wanted to leverage existing L7 proxies specifically envoy in this case due to its uh capabilities with XROC and we wanted that because we want a global view of the model server state so that we can do this efficient routing. So how did we integrate? Well the yellow if if you've seen inference gateway you've seen this picture before the yellow is what is existing today or existed before inference gateway came into being. Uh so we have our L7 proxy. Wrong button, sorry. We have our L7 proxy here. The request comes in. Uh assuming the green doesn't exist, the request comes in to the model server. Uh and then it's sent back all the all with the L7 managing the connection. Uh typically this is going to be through gateway API. What we add is using the extension protocol provided by envoy supported by by other gateways. We treat the endpoint picker service as an advisory role. So it can take a look at the the contents of the body like we mentioned earlier and it can provide routing hints that the L7 will use and route to the model server that the endpoint picker suggests.

So how does the endpoint picker select? Well uh I will mention and people probably here know that uh inference and specifically inference routing is not a solved problem. So to combat an unknown future, we built a pluggable framework that allows us to make decisions, create routing algorithms, and uh b
