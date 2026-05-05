---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Platform Engineering", "SRE Reliability"]
speakers: ["Antti Kervinen", "Intel", "Dixita Narang", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7m0/platform-performance-optimization-for-ai-a-resource-management-perspective-antti-kervinen-intel-dixita-narang-google
youtube_search_url: https://www.youtube.com/results?search_query=Platform+Performance+Optimization+for+AI+-+a+Resource+Management+Perspective+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Platform Performance Optimization for AI - a Resource Management Perspective - Antti Kervinen, Intel & Dixita Narang, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Antti Kervinen, Intel, Dixita Narang, Google
- Schedule: https://kccncna2024.sched.com/event/1i7m0/platform-performance-optimization-for-ai-a-resource-management-perspective-antti-kervinen-intel-dixita-narang-google
- Busca YouTube: https://www.youtube.com/results?search_query=Platform+Performance+Optimization+for+AI+-+a+Resource+Management+Perspective+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Platform Performance Optimization for AI - a Resource Management Perspective.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7m0/platform-performance-optimization-for-ai-a-resource-management-perspective-antti-kervinen-intel-dixita-narang-google
- YouTube search: https://www.youtube.com/results?search_query=Platform+Performance+Optimization+for+AI+-+a+Resource+Management+Perspective+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=__mh4txajIM
- YouTube title: Platform Performance Optimization for AI - a Resource Management Perspective- A. Kervinen, D. Narang
- Match score: 0.961
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/platform-performance-optimization-for-ai-a-resource-management-perspec/__mh4txajIM.txt
- Transcript chars: 23051
- Keywords: inference, running, inferences, resource, latency, function, socket, actually, llm, library, number, threats, physical, policy, python, container, performance, experiment

### Resumo baseado na transcript

Welcome to our session on platform performance optimization for AI we are going to optimize model inference here and this is now from the resource management perspective inside a node my name is AE kin and I work for Intel and I've been dealing with this Resource Management not Resource Management topic for a couple of years now and here's Dix my name is Dix you can call me Dixie I go by that Alas and I work for Google and I'm an active contributor to signote community so for CPUs and that's what how we get the CPU pinning and that's how we can control are we using both hyper threats or one hyper threat per physical core for instance okay now let's start visualizing the data short reminder this is performance data if

### Excerpt da transcript

Welcome to our session on platform performance optimization for AI we are going to optimize model inference here and this is now from the resource management perspective inside a node my name is AE kin and I work for Intel and I've been dealing with this Resource Management not Resource Management topic for a couple of years now and here's Dix my name is Dix you can call me Dixie I go by that Alas and I work for Google and I'm an active contributor to signote community so for this session I want to point out that running AI workloads can get expensive really fast specifically the llm uh inference models so these workloads can have uh different resource usage patterns for example some could be CPU bound while the others could be Memory bound and while some could just have uh spiky resource needs so in this session we are going to walk over how you can utilize the maximum out of your Hardware how you can unlock the maximum potential so if you understand the resource usage patterns of your workloads you can place them strategically such that there is minimum to no uh resource contention for example you could just place your workloads to uh to be allocated CPUs from different cores such that there is no interference and that could would help you um unlock the maximum Potential from your Hardware so for our experiment uh we are using this chatbot it's just a rack pipeline which has all these typical components uh the query component embedding Vector database llm relevant data and so on so these components can be uh kubernetes microservices in themselves we are specifically focusing on the llm uh inference component so you could have multiple replicas of of this component running and in the experiment we'll see how placing the replicas on the Node strategically can help you uh optimize the hardware potential so in our experiment the goal is to balance the latency throughput and the resource usage such that everything is optimal as much as possible um the first step of our experiment is we are preparing the data collection we have a third party uh python Library which we are using to collect the data and we are also augmenting it modifying it a bit to add some instrumentation that's useful for our U experiment results analysis the next step is we run the tests on the instrumented data and we visualize these uh in the middle of the show because we want to see if there is anything that needs to be corrected or if there is any strategy that is giving us poor benchma
