---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Madhav Jivrajani", "Kartik Ramesh", "UIUC"]
sched_url: https://kccncna2025.sched.com/event/27FVM/cafegpt-serving-llms-like-coffee-with-kubernetes-madhav-jivrajani-kartik-ramesh-uiuc
youtube_search_url: https://www.youtube.com/results?search_query=CafeGPT%3A+Serving+LLMs+Like+Coffee+With+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# CafeGPT: Serving LLMs Like Coffee With Kubernetes - Madhav Jivrajani & Kartik Ramesh, UIUC

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Madhav Jivrajani, Kartik Ramesh, UIUC
- Schedule: https://kccncna2025.sched.com/event/27FVM/cafegpt-serving-llms-like-coffee-with-kubernetes-madhav-jivrajani-kartik-ramesh-uiuc
- Busca YouTube: https://www.youtube.com/results?search_query=CafeGPT%3A+Serving+LLMs+Like+Coffee+With+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre CafeGPT: Serving LLMs Like Coffee With Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVM/cafegpt-serving-llms-like-coffee-with-kubernetes-madhav-jivrajani-kartik-ramesh-uiuc
- YouTube search: https://www.youtube.com/results?search_query=CafeGPT%3A+Serving+LLMs+Like+Coffee+With+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zMArlA0rPsM
- YouTube title: CafeGPT: Serving LLMs Like Coffee With Kubernetes - Madhav Jivrajani & Kartik Ramesh, UIUC
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/cafegpt-serving-llms-like-coffee-with-kubernetes/zMArlA0rPsM.txt
- Transcript chars: 25869
- Keywords: request, requests, coffee, gpu, prefill, workload, decode, memory, inference, machine, actually, serving, latency, better, second, barista, single, resource

### Resumo baseado na transcript

Uh and I'm I do research in in the area of distributed systems and I also contribute and maintain some parts of the Kubernetes project. I'm also a grad student at University of Illinois where I research ML systems and really excited to be here and see all of you today. Well, the answer as is the answer to most computer science problems is through caching. And since we want to serve these at a low cost, we want high machine utilization. And this results in a problem because if there are more requests that come in, they can't do any work on them until the entire first request is finished. And again, due to our workload, this is a problem because we don't know when that is going to happen.

### Excerpt da transcript

Hi, welcome welcome to our talk. Uh first of all, I hope you had a good CubeCon. I hope you made a couple new friends. If in case you haven't, please meet us after the talk. We'd love to be your friend. Uh so, welcome to our talk, Cafe GPT. My name is Madav. I'm a grad student at UIU. Uh and I'm I do research in in the area of distributed systems and I also contribute and maintain some parts of the Kubernetes project. >> Hi, my name is Karthik. I'm also a grad student at University of Illinois where I research ML systems and really excited to be here and see all of you today. So before we get into it, we'd like to start by talking about what this talk isn't right. This isn't a deep dive into LLM inference or the internals of how Kubernetes enables uh enables serving such workloads. There's many many more wells suited talks on that topic at this conference and many others. What this talk is rather is that we've been trying to educate ourselves on how many of these different parts of the ecosystem sort of fit in together.

And this is us trying to share that picture with you. So that said, welcome to Cafe GBD. Cafe GBD is probably the best cafe at CubeCon 2025. There's this thing called AI that you might have heard of, you know, a couple million times in the keynotes. We have a new customer with a drink request, an ice latte with oat milk. We have we have a manager and a barista to help fulfill that request to make sure that all of our attendees are sufficiently caffeinated. The manager directs the request to the barista. The barista has access to coffee machines to help fulfill that said request. Each coffee machine has many many moving parts that has the grinder, the steamer, the pressure valve and so on. The barista uses a coffee machine to make the drink and finally serves the drink back to the customer via the manager. Our customer loves the coffee and more importantly loves cafe GPT because the coffee was served in a timely manner and it wasn't very expensive to begin with. So with that out of the way, let's draw some analogies here.

Let's make things a little more concrete. What does serving in cafeter are going to call the router that is responsible for delegating requests to appropriate baristas. The barista to draw a fat analogy is the LLM inference engine using resources available to it and then converting requests to coffee. The coffee machines are our GPUs that actually brew the responses. Let's continue making things a little more concrete. Wh
