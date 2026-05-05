---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Tiancheng Yin", "Yao Lin", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1txDx/reliable-k8s-resource-submission-bookkeeping-tiancheng-yin-yao-lin-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Reliable+K8s+Resource+Submission+%26+Bookkeeping+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Reliable K8s Resource Submission & Bookkeeping - Tiancheng Yin & Yao Lin, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Tiancheng Yin, Yao Lin, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1txDx/reliable-k8s-resource-submission-bookkeeping-tiancheng-yin-yao-lin-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Reliable+K8s+Resource+Submission+%26+Bookkeeping+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Reliable K8s Resource Submission & Bookkeeping.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txDx/reliable-k8s-resource-submission-bookkeeping-tiancheng-yin-yao-lin-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Reliable+K8s+Resource+Submission+%26+Bookkeeping+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NCkHrvqFMl8
- YouTube title: Reliable K8s Resource Submission & Bookkeeping - Tiancheng Yin & Yao Lin, Bloomberg
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/reliable-k8s-resource-submission-bookkeeping/NCkHrvqFMl8.txt
- Transcript chars: 13640
- Keywords: cluster, resources, resource, workflow, available, message, inventory, config, database, consumer, record, delete, deployables, actually, historical, transactions, highly, clusters

### Resumo baseado na transcript

Uh welcome everyone to our session about reliable uh Kubernetes resource submission and bookkeeping. Um so we work in the workflow orchestration team in cloudnative compute services along with uh other similar Kubernetes based platforms inside Bloomberg. So it's of a similar concept of other things like kubernetes native jobs or any other um customized jobs and the other things because they are expected to be available on the applicable clusters. If all those requests actually land on the Kubernetes API survey itself, then that's too much load. It may even downgrade the performance of the cluster in terms of orchestrating the workflow itself. So in practice you can actually implement a push mode just like what we demonstrate in the last slides.

### Excerpt da transcript

Uh welcome everyone to our session about reliable uh Kubernetes resource submission and bookkeeping. Um so let's introduce oursel first. I'm Yaoin. I'm Ken. Um so we work in the workflow orchestration team in cloudnative compute services along with uh other similar Kubernetes based platforms inside Bloomberg. Um yeah we have a few dedicated team Kubernetes based and we're interested in in this whole ecosystem. We maintain a highly available container archeration that platform for our internal engineers in Bloomberg. Uh the platform itself execute users run to completion workload for uh general use cases. Um so typical use case includes like machine learning pipelines uh CI/CD pipelines machine learn uh machine maintenance routines and uh financial analysis or any general data processing. Um so for these use cases uh we uh have uh both some functional and non-functional requirements. The functional part may be easier. Um there's observability, scheduling or eventing. Approval process needs to be integrated into the whole platform to make sure things are properly revealed before taking effect.

Um but the non-functional can be less obvious, but that is probably the most difficult part in the whole system. Um yeah, so in Bloomberg, we value the data center resiliency seriously. So what does that mean? That means uh if one data center goes down, our platform should be seeming still working uh to our users because um everything should be highly available um by what's available on the other side of the uh system. Um another healthy data center. So before diving into technical diagrams, we can first understand what our user is doing with our platform. Uh to the basic, they need to run their workflows. Uh if you are not familiar with Argo workflows, Argo workflow is something you can define your steps like in deck. Uh they depend they can be depends on each other or span from each other. uh execute containers in particular sequence. For example, uh I can generate a report first and then persist somewhere and then finally it notifies me when everything is finished. Um for that to happen we need a few other resources available on the cluster is executed on uh such as config map and secrets and for workflow specifically um there's argo workflow template and cluster workflow template for the workflow itself to refer to.

So let me put a abstraction layer on these things. So for workflow we just put it as runnables. So it's of a similar concept of other things like kub
