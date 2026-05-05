---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Tutorials"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Claudia Misale", "IBM Research", "Olivier Tardieu", "David Grove", "IBM"]
sched_url: https://kccnceu2025.sched.com/event/1tx6h/tutorial-build-operate-and-use-a-multi-tenant-ai-cluster-based-entirely-on-open-source-claudia-misale-ibm-research-olivier-tardieu-david-grove-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Build%2C+Operate%2C+and+Use+a+Multi-Tenant+AI+Cluster+Based+Entirely+on+Open+Source+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Tutorial: Build, Operate, and Use a Multi-Tenant AI Cluster Based Entirely on Open Source - Claudia Misale, IBM Research; Olivier Tardieu & David Grove, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Claudia Misale, IBM Research, Olivier Tardieu, David Grove, IBM
- Schedule: https://kccnceu2025.sched.com/event/1tx6h/tutorial-build-operate-and-use-a-multi-tenant-ai-cluster-based-entirely-on-open-source-claudia-misale-ibm-research-olivier-tardieu-david-grove-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Build%2C+Operate%2C+and+Use+a+Multi-Tenant+AI+Cluster+Based+Entirely+on+Open+Source+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Tutorial: Build, Operate, and Use a Multi-Tenant AI Cluster Based Entirely on Open Source.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx6h/tutorial-build-operate-and-use-a-multi-tenant-ai-cluster-based-entirely-on-open-source-claudia-misale-ibm-research-olivier-tardieu-david-grove-ibm
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Build%2C+Operate%2C+and+Use+a+Multi-Tenant+AI+Cluster+Based+Entirely+on+Open+Source+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ab7mRoJYsMo
- YouTube title: Tutorial: Build, Operate, and Use a Multi-Tenant AI Cluster Base... C. Misale, O. Tardieu & D. Grove
- Match score: 0.816
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tutorial-build-operate-and-use-a-multi-tenant-ai-cluster-based-entirel/Ab7mRoJYsMo.txt
- Transcript chars: 73133
- Keywords: cluster, running, workloads, gpu, actually, resources, workload, quotas, create, storage, wrapper, particular, little, everything, training, number, created, autopilot

### Resumo baseado na transcript

I'm a principal research scientist and manager at IBM Research and today I'm joined with my by my IBM Research colleague, Dave Grove, and and Claudia Missaglia. And we're going to talk about how to build, operate, and use GPU clusters for AI, right? So, uh, because we're going to talk about GPUs and I don't typically travel with a 2,000 GPUs in my backpack, uh, this is all going to be recorded demos, but uh, you know, on a real GPU cluster. Everything starting from things like data preparation, even, you know, like when we do hate and profanity filtering for instance on on our data before we train models, we actually use already machine learning models to do that, so we need GPUs, we need a So, they have eight GPUs in both of these pictures and then lots of compute, you know, CPUs, memory, local storage, uh, high performance network, and so on. I think yesterday in Cloud AI Day, we had somebody bold enough to ask the question, why Kubernetes?

### Excerpt da transcript

Uh, good afternoon. Uh, welcome to a session. So, my name is Olivier Tardieu. I'm a principal research scientist and manager at IBM Research and today I'm joined with my by my IBM Research colleague, Dave Grove, and and Claudia Missaglia. And we're going to talk about how to build, operate, and use GPU clusters for AI, right? So, uh, by now we've all heard about AI and GenAI. We are all probably excited about it, but we're also sometimes a little bit anxious about it for lots of reasons. And as an organization, maybe the first reason to be anxious about AI is to actually procure GPU to do AI, right? It's both time-consuming, expensive, slow, you know, whether we rent them from a cloud provider, whether we buy them, whether we lease them, whether we want a dozen of them or thousand GPUs, it's a big problem. But someday we'll get them. And and then the second panic arises, right? It's how can we take these GPUs, this pool of resources, and somehow share it across all the teams, all the users we have in our organization, all the projects that need access to these resources, so that we can manage them and we can maximize utilization and we can maximize the return on investment.

So, this is something we've been working on on IBM Research on our own cluster for several years now and we've essentially built a point of view, uh, incrementally refined uh, methodology, uh, a setup, and we're going to try to share this with you today uh, with the hope that we can help you with your own, uh, you know, AI journey and also that you will tell us everything we could do better. So, let's get started. So, um, in uh, what we're going to show you today is entirely open-source. Uh, everything is available online including this tutorial. So, if you go to this QR code and this URL, you'll find uh, all the comments, all the scripts, all the uh, YAMLs that we're going to use today and you can you conceivably follow along and and or, you know, replay that at home, right? So, uh, because we're going to talk about GPUs and I don't typically travel with a 2,000 GPUs in my backpack, uh, this is all going to be recorded demos, but uh, you know, on a real GPU cluster. So, I'm going to start by a brief background on AI/ML workload, on the kind of hardware we target, on what exactly are the key components and maybe the key goals of the platform we've been developing at IBM Research, and then we'll get into the the the the the deep dive of the tutorial, how do we set up a cluster, how do w
