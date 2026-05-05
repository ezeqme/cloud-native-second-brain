---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Vishakha Ramani", "Sara Kokkila-Schumacher", "IBM Research"]
sched_url: https://kccncna2023.sched.com/event/1R2pf/best-practices-improving-batch-scheduling-performance-at-scale-using-mcad-and-kwok-vishakha-ramani-sara-kokkila-schumacher-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=Best+Practices%3A+Improving+Batch+Scheduling+Performance+at+Scale+Using+MCAD+and+KWOK+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Best Practices: Improving Batch Scheduling Performance at Scale Using MCAD and KWOK - Vishakha Ramani & Sara Kokkila-Schumacher, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Vishakha Ramani, Sara Kokkila-Schumacher, IBM Research
- Schedule: https://kccncna2023.sched.com/event/1R2pf/best-practices-improving-batch-scheduling-performance-at-scale-using-mcad-and-kwok-vishakha-ramani-sara-kokkila-schumacher-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=Best+Practices%3A+Improving+Batch+Scheduling+Performance+at+Scale+Using+MCAD+and+KWOK+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Best Practices: Improving Batch Scheduling Performance at Scale Using MCAD and KWOK.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pf/best-practices-improving-batch-scheduling-performance-at-scale-using-mcad-and-kwok-vishakha-ramani-sara-kokkila-schumacher-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=Best+Practices%3A+Improving+Batch+Scheduling+Performance+at+Scale+Using+MCAD+and+KWOK+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VM6sIo6vFN0
- YouTube title: Best Practices: Improving Batch Scheduling Performance... Vishakha Ramani & Sara Kokkila-Schumacher
- Match score: 0.766
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/best-practices-improving-batch-scheduling-performance-at-scale-using-m/VM6sIo6vFN0.txt
- Transcript chars: 23560
- Keywords: seconds, resource, cluster, scheduling, training, simulate, performance, testing, running, resources, offers, management, simulated, observe, completion, latency, working, scheduler

### Resumo baseado na transcript

hello everyone uh thank you for joining us this morning uh my name is Sarah and this is faka and we are here today to talk to you about best practices improving batch scheduling performance at scale using MCAT and qua MCAT is the multicluster app dispatcher and quac is the kubernetes without KET tool to give you an idea of what we're going to cover today uh I'm going to give some background on the motivation and existing challenges we see uh the potential solution kubernetes without kuet or

### Excerpt da transcript

hello everyone uh thank you for joining us this morning uh my name is Sarah and this is faka and we are here today to talk to you about best practices improving batch scheduling performance at scale using MCAT and qua MCAT is the multicluster app dispatcher and quac is the kubernetes without KET tool to give you an idea of what we're going to cover today uh I'm going to give some background on the motivation and existing challenges we see uh the potential solution kubernetes without kuet or qua and then I'm going to hand it over to vishaka who's um going to give you some insight into best practices and getting started with tools like qua some things you might want to look out for when you're doing this sort of testing and then walk you through some uh example use cases that hopefully you'll be able to take uh away and an understanding of how you might adapt this approach to suit your resource management and uh performance testing needs so to give you some motivation and uh cover some of the existing challenges uh we're coming from IBM research uh where we've been working a lot with Foundation models uh so you may have heard about large language models such as chat GPT this is part of a broader class of AI that we refer to as Foundation models uh because you can use a lot of the same ideas and techniques to represent different modalities and train these very large models to sort of give some background on the the different uh areas that uh we see often in AI uh there's this sort of life cycle of model creation to deployment where one of the major steps is actually data preparation how do you process accumulate uh make sure you have high quality data and then we go into the more of the distributed training which is going to be uh sort of our use case Focus for this talk uh which is often long running jobs that have massive uh infrastructure requirements and heavy GPU utilization and then you can go into other stages of the the life cycle development here such as uh model adaptation or fine-tuning and then all the way to uh inferencing but here as our use case uh we we work a lot with the distri uted training teams and so that's going to be um what we're going to focus on and so as part of IBM research we really believe in applying the open- source first approach to enable and scale these Foundation model workloads uh so here we highlight our training and validation stack all running on kubernetes or redhead open shift um and so at the top level uh we have th
