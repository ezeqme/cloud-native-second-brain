---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Esteban Rey", "Microsoft", "Yifan Yuan", "AlibabaCloud"]
sched_url: https://kccnceu2025.sched.com/event/1txEv/streamlined-efficiency-unshackling-kubernetes-image-volumes-for-rapid-ai-model-and-dataset-loading-esteban-rey-microsoft-yifan-yuan-alibabacloud
youtube_search_url: https://www.youtube.com/results?search_query=Streamlined+Efficiency%3A+Unshackling+Kubernetes+Image+Volumes+for+Rapid+AI+Model+and+Dataset+Loading+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Streamlined Efficiency: Unshackling Kubernetes Image Volumes for Rapid AI Model and Dataset Loading - Esteban Rey, Microsoft & Yifan Yuan, AlibabaCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Esteban Rey, Microsoft, Yifan Yuan, AlibabaCloud
- Schedule: https://kccnceu2025.sched.com/event/1txEv/streamlined-efficiency-unshackling-kubernetes-image-volumes-for-rapid-ai-model-and-dataset-loading-esteban-rey-microsoft-yifan-yuan-alibabacloud
- Busca YouTube: https://www.youtube.com/results?search_query=Streamlined+Efficiency%3A+Unshackling+Kubernetes+Image+Volumes+for+Rapid+AI+Model+and+Dataset+Loading+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Streamlined Efficiency: Unshackling Kubernetes Image Volumes for Rapid AI Model and Dataset Loading.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEv/streamlined-efficiency-unshackling-kubernetes-image-volumes-for-rapid-ai-model-and-dataset-loading-esteban-rey-microsoft-yifan-yuan-alibabacloud
- YouTube search: https://www.youtube.com/results?search_query=Streamlined+Efficiency%3A+Unshackling+Kubernetes+Image+Volumes+for+Rapid+AI+Model+and+Dataset+Loading+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nHGzMmstR0E
- YouTube title: Streamlined Efficiency: Unshackling Kubernetes Image Volumes for Rapid AI Model... E. Rey & Y. Yuan
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/streamlined-efficiency-unshackling-kubernetes-image-volumes-for-rapid/nHGzMmstR0E.txt
- Transcript chars: 17143
- Keywords: reference, streaming, actually, access, registries, registry, artifact, images, packaging, remote, already, package, create, loading, object, volume, container, performance

### Resumo baseado na transcript

Welcome everybody to the streamlined efficiency and shackling Kubernetes image volumes for rapid AI model and data set loading presentation. Today we're going to talk a little bit about how we can go about speeding up um volume loading when using image volume specifically. We want to be able to load data at a scale, but at the same time, we don't want to necessarily pay the upfront cost of packaging this data and putting it in our container registries. This data parallelism presents a lot of challenges and means that we actually need to be able to simultaneously access lots of data across multiple places at the same time. Additionally, because we're dealing with Kubernetes clusters, we obviously need to be able to scale up our access. If we're not able to scale up to thousands of nodes, then we're not going to be able to use this data effectively when training AI models or any other thing that requires large data sets.

### Excerpt da transcript

Welcome everybody to the streamlined efficiency and shackling Kubernetes image volumes for rapid AI model and data set loading presentation. Today we're going to talk a little bit about how we can go about speeding up um volume loading when using image volume specifically. So to start us off uh I'm Essen Ree. I am a software engineer from Microsoft. I specifically work on Ashure container registry. My oh one second um my main area of expertise is OCI conformance as well as artifact streaming. My co-presenter over there is Yan Yuan from Alibaba cloud. He's a senior software engineer there and a researcher who's done many many contributions to the overlay BD project. Um so to start us off I want to speak about the current state of efficiency when it comes to starting up images and how we can deal with accelerating those. So the first thing to note is that today we have achieved a lot of progress on image startup. The first thing is we have artifact streaming. However, artifact streaming helps us solve one problem which is how do we optimize uh workloads that are specifically applicationbased.

But when we start to deal with we need to have these large data sets along with this we start to encounter some problems. Packaging our information into our current images and then streaming them is not necessarily efficient. We want to be able to load data at a scale, but at the same time, we don't want to necessarily pay the upfront cost of packaging this data and putting it in our container registries. So, when we're dealing with large language model training or just AI in general, we sometimes need to load data in parallel. This data parallelism presents a lot of challenges and means that we actually need to be able to simultaneously access lots of data across multiple places at the same time. Uh this presents a number of challenges. Um the first of which is we need to be able to have data that can be accessible all the time. So if we don't have continuous data access, we're going to end up paying a lot of money for GPUs that are not in use. We're going to be unable to actually load all the data when we need it as we need it.

We also need to make sure that when we do access the data, it's actually fast to access. Additionally, because we're dealing with Kubernetes clusters, we obviously need to be able to scale up our access. If we're not able to scale up to thousands of nodes, then we're not going to be able to use this data effectively when training AI models or
