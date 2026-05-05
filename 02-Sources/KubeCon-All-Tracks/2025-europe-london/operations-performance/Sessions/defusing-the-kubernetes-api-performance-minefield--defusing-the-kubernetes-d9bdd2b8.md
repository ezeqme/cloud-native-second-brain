---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Madhav Jivrajani", "UIUC", "Marek Siarkowicz", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tx9P/defusing-the-kubernetes-api-performance-minefield-madhav-jivrajani-uiuc-marek-siarkowicz-google
youtube_search_url: https://www.youtube.com/results?search_query=Defusing+the+Kubernetes+API+Performance+Minefield+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Defusing the Kubernetes API Performance Minefield - Madhav Jivrajani, UIUC & Marek Siarkowicz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Madhav Jivrajani, UIUC, Marek Siarkowicz, Google
- Schedule: https://kccnceu2025.sched.com/event/1tx9P/defusing-the-kubernetes-api-performance-minefield-madhav-jivrajani-uiuc-marek-siarkowicz-google
- Busca YouTube: https://www.youtube.com/results?search_query=Defusing+the+Kubernetes+API+Performance+Minefield+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Defusing the Kubernetes API Performance Minefield.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9P/defusing-the-kubernetes-api-performance-minefield-madhav-jivrajani-uiuc-marek-siarkowicz-google
- YouTube search: https://www.youtube.com/results?search_query=Defusing+the+Kubernetes+API+Performance+Minefield+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SdLLOcNZN5E
- YouTube title: Defusing the Kubernetes API Performance Minefield - Madhav Jivrajani & Marek Siarkowicz
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/defusing-the-kubernetes-api-performance-minefield/SdLLOcNZN5E.txt
- Transcript chars: 25712
- Keywords: version, server, resource, request, memory, client, response, default, performance, allocations, storage, update, everything, change, basically, scalability, gigabytes, gigabyte

### Resumo baseado na transcript

Hello everyone and welcome to my talk about uh Kubernetes API performance. Uh so the plan for today is explain what is the uh the minefield in the title. So for last year I've been looking into the API server performance and hopefully we can we can diffuse some of the problems to uh today. So the problem that I want to talk about to you is the uh problematic usage or abusive usage or of CRDs and operators. So since 1.6, six, Kubernetes runs uh a weekly test that has 5,000 nodes, 15,000 pots or 150,000 pots, 10,000 services and everything. Uh the problem is Kubernetes tests its own scalability focusing its own main pipelines and its own concerns.

### Excerpt da transcript

Okay. Hello everyone and welcome to my talk about uh Kubernetes API performance. Uh I'm Marik Sharkovich. I'm the SIG lead of ATC and uh and I contribute to also API machinery. Unfortunately, Maddaf was not able to to join us today. So I will be hope I'm enough to talk about the performance of API. Uh so the plan for today is explain what is the uh the minefield in the title. We will try to understand on example why um why you can easily uh get hurt if you don't understand the API performance. We'll try to propose couple of ideas how we can navigate and hopefully maybe we could uh diffuse it. Uh at the end I have couple of results uh from performance metrics so we we could see how it turns out. So overall Kubernetes is awesome like you can take your containers, you can ship it. I it it works really well like we have pretty big conference. I think it's testament to that but not always it can turn out how you can think. Um, some things are harder, sometimes there are incidents, but I think in my experience there are something there are some areas that you're just destined to fail unfortunately that are not well documented that are still a tribal knowledge that is spent between maintainers and if you don't ask them uh you might get uh hurt.

So for last year I've been looking into the API server performance and hopefully we can we can diffuse some of the problems to uh today. So the problem that I want to talk about to you is the uh problematic usage or abusive usage or of CRDs and operators. So uh in one of the incidents uh that uh I I was working on uh on GKE, we we had a pretty small cluster. Uh it seemed pretty pretty small relatively to every the things that we run but still customer upgraded as a operator and everything worked for two weeks and just when everyone want you already thought that we are done uh the memory spiked 20 times. So what happened like how and how why why did did it spike every every like couple of days and totally took down the control plane? Uh and how at like 50 node cluster can can go down? Well, Kubernetes apparently supports 5,000 nodes. So since 1.6, six, Kubernetes runs uh a weekly test that has 5,000 nodes, 15,000 pots or 150,000 pots, 10,000 services and everything. So, it should work, right? Uh the problem is Kubernetes tests its own scalability focusing its own main pipelines and its own concerns.

So when you go into CRDs, you might find that the project that you have picked from the shelf never tested anything beyond l
