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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Yao Weng", "Leon Zhou", "Bloomberg"]
sched_url: https://kccncna2024.sched.com/event/1i7qk/bloombergs-journey-to-improve-resource-utilization-in-a-multi-cluster-platform-yao-weng-leon-zhou-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Bloomberg%E2%80%99s+Journey+to+Improve+Resource+Utilization+in+a+Multi-Cluster+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Bloomberg’s Journey to Improve Resource Utilization in a Multi-Cluster Platform - Yao Weng & Leon Zhou, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Yao Weng, Leon Zhou, Bloomberg
- Schedule: https://kccncna2024.sched.com/event/1i7qk/bloombergs-journey-to-improve-resource-utilization-in-a-multi-cluster-platform-yao-weng-leon-zhou-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Bloomberg%E2%80%99s+Journey+to+Improve+Resource+Utilization+in+a+Multi-Cluster+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Bloomberg’s Journey to Improve Resource Utilization in a Multi-Cluster Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qk/bloombergs-journey-to-improve-resource-utilization-in-a-multi-cluster-platform-yao-weng-leon-zhou-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Bloomberg%E2%80%99s+Journey+to+Improve+Resource+Utilization+in+a+Multi-Cluster+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lMtCSaHI9Uk
- YouTube title: Bloomberg’s Journey to Improve Resource Utilization in a Multi-Cluster Platform- Yao Weng, Leon Zhou
- Match score: 0.971
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/bloombergs-journey-to-improve-resource-utilization-in-a-multi-cluster/lMtCSaHI9Uk.txt
- Transcript chars: 22738
- Keywords: cluster, resource, scheduler, clusters, gpu, workload, kamada, priority, utilization, schedule, machine, learning, resources, member, bloomberg, commod, estimator, platform

### Resumo baseado na transcript

hello everyone how are we doing thank you for coming to in Friday afternoon session um today we'll be talking about Bloomberg's journey to improve resour utilization in multicluster platform my name is Leon and I I am a software engineer on the data science platform team at Bloomberg uh hi uh I am Yao I'm a senior software de uh developer at Bloomberg data science platform team yeah cool so for today agenda we'll first be talking about some common challenges with managing large GPU clusters and then we'll

### Excerpt da transcript

hello everyone how are we doing thank you for coming to in Friday afternoon session um today we'll be talking about Bloomberg's journey to improve resour utilization in multicluster platform my name is Leon and I I am a software engineer on the data science platform team at Bloomberg uh hi uh I am Yao I'm a senior software de uh developer at Bloomberg data science platform team yeah cool so for today agenda we'll first be talking about some common challenges with managing large GPU clusters and then we'll talk about how we can solve these challenges by bending the GPU growth curve with a scheduler and then we'll talk about how we can use kamada scheduler for the data science platform team uh data science platform at Bloomberg and lastly we'll wrap everything up with the future project roadmap for kamada our data science platform is an onp parameter beer metal kubernetes cluster and a One-Stop shop uh kubernetes infrastructure and a One-Stop shop for every stage of the machine learning life cycle from running experiments to batch training workloads to deploying inference applications in production and when it comes to challenges in managing a large GPU cluster you will hear all about them today and how we overcome these challenges with each new generation of large models the resource needed for training increases significantly along with the need to serve more inference applications and both of these requirements are calling for new generation of gpus to handle more data in larger models further raising the bar for machine learning infrastructure requirements additionally today's GPU nodes consumes a lot more power than the average CPU node or previous gener ation of the GPU nodes meaning more power capacity is needed in order to grow the GPU cluster capacity as well as the GPU demand curve is accelerating we need to be Innovative and bend the demand curve by improving the resource utilization rate so that our GPU cluster growth can keep up with the GPU demand so top of our list of challenges we found that our resour realization rate is held down by over budgeting so in this diagram it illustrates the resource utilization of batch workload Illustrated in green and long running Services utilization in Orange with respect to the static quota drawn in the blue line so our for long running Services the resour utilization is relatively stable in static res in a static kuber netics resource Coda however does not quite work well with the machine learning training
