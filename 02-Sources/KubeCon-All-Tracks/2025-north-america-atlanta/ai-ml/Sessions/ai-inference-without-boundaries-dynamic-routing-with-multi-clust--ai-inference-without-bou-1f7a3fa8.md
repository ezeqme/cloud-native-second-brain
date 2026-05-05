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
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Rob Scott", "Google", "Daneyon Hansen", "Solo.io"]
sched_url: https://kccncna2025.sched.com/event/27FeP/ai-inference-without-boundaries-dynamic-routing-with-multi-cluster-inference-gateway-rob-scott-google-daneyon-hansen-soloio
youtube_search_url: https://www.youtube.com/results?search_query=AI+Inference+Without+Boundaries%3A+Dynamic+Routing+With+Multi-Cluster+Inference+Gateway+CNCF+KubeCon+2025
slides: []
status: parsed
---

# AI Inference Without Boundaries: Dynamic Routing With Multi-Cluster Inference Gateway - Rob Scott, Google & Daneyon Hansen, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Rob Scott, Google, Daneyon Hansen, Solo.io
- Schedule: https://kccncna2025.sched.com/event/27FeP/ai-inference-without-boundaries-dynamic-routing-with-multi-cluster-inference-gateway-rob-scott-google-daneyon-hansen-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=AI+Inference+Without+Boundaries%3A+Dynamic+Routing+With+Multi-Cluster+Inference+Gateway+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre AI Inference Without Boundaries: Dynamic Routing With Multi-Cluster Inference Gateway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FeP/ai-inference-without-boundaries-dynamic-routing-with-multi-cluster-inference-gateway-rob-scott-google-daneyon-hansen-soloio
- YouTube search: https://www.youtube.com/results?search_query=AI+Inference+Without+Boundaries%3A+Dynamic+Routing+With+Multi-Cluster+Inference+Gateway+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UJy8n8uX8G4
- YouTube title: AI Inference Without Boundaries: Dynamic Routing With Multi-Cluster In... Rob Scott & Daneyon Hansen
- Match score: 0.889
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ai-inference-without-boundaries-dynamic-routing-with-multi-cluster-inf/UJy8n8uX8G4.txt
- Transcript chars: 27177
- Keywords: gateway, inference, cluster, multicluster, endpoint, picker, traffic, request, backend, clusters, import, routing, metrics, gateways, extension, decision, server, within

### Resumo baseado na transcript

Uh really appreciate you coming to to listen to us talk about uh multicluster inference gateways. Uh I work on all kinds of gateway API things and GK networking things at Google. model servers uh with uh scraping metrics from those backend model servers uh to help it determine what is the best model server to route the request to right and when a request comes in the gateway would typically go ahead and route that request So I want to configure all traffic matching this path or query pram or header to go to this specific backend. uh when you add in inference well you just switch out one of those backends instead of them all being service you have an inference pool there right so uh inference pool is a different kind of backend inside Kubernetes and inference pool is where Uh and this is because each endpoint picker as as Dian already mentioned is very frequently getting metrics from each endpoint in inference pool to understand what is the best endpoint at this very specific point in time to serve this request and that requires

### Excerpt da transcript

Great. Thank you everyone for making it to one of the last talks of KubeCon. I really appreciate you sticking around. I know there's been a lot. It's been a long week. Uh really appreciate you coming to to listen to us talk about uh multicluster inference gateways. Uh my name is Rob Scott. Uh I work on all kinds of gateway API things and GK networking things at Google. Uh and I've got Dian with me >> and I'm Damian Hansen. I'm a principal software engineer at Solo IO and uh have been involved in Kubernetes networking pretty much from uh from the start and I'm a maintainer of the gateway API inference extension project and excited to get into multicluster inference gateways with you. Uh so before we dive into multicluster inference gateways, we thought it'd be a good idea to kind of build a a foundation uh knowledge. Uh and so let's start from the beginning in a sense and that is why do we even talk about inference gateways? Why did we create inference gateways? And at its core, the reason for that is is we're dealing with a very different traffic type than what we usually deal with, right?

With web requests, they're small. We're measuring them in in a matter of milliseconds. We could run them in parallel. And with Gen AI traffic, very different traffic type, right? We're typically dealing with much larger requests, especially when we're talking about multimodal models or multi-turn chat um uh traffic. And so, because we have a different type of traffic, we need a different type of solution. And that brings us to inference gateways. And so what is an inference gateway? An inference gateway is a gateway like a proxy or a load balancer that is coupled with an endpoint picker extension or what we call an EP. Uh the project gateway API inference extension has a reference EP. But as long as the EP follows this EP protocol specification that we defined, you can develop your own EP if you wanted to. And uh as part of the gateway it needs to understand gateway API and of course it also needs to implement the EP protocol specification. And let's dive a little bit into the EP. At the heart of the EP is the scheduler.

This is the brain of the EP that makes the the decision on where to route the request to uh across my fleet of model server replicas. And it is extensible and at the heart of theuler is these plugins that either filter out requests or score the requests. So if I have multiple replicas of my model server and I need to make a decision which is the best r
