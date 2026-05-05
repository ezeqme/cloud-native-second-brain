---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["AI ML"]
speakers: ["Mukund Muralikrishnan", "Staff Engineer", "Wayve"]
sched_url: https://kccnceu2026.sched.com/event/2HgE0/keynote-rules-of-the-road-for-shared-gpus-ai-inference-scheduling-at-wayve-mukund-muralikrishnan-staff-engineer-wayve
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Rules+of+the+Road+for+Shared+GPUs%3A+AI+Inference+Scheduling+at+Wayve+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Keynote: Rules of the Road for Shared GPUs: AI Inference Scheduling at Wayve - Mukund Muralikrishnan, Staff Engineer, Wayve

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mukund Muralikrishnan, Staff Engineer, Wayve
- Schedule: https://kccnceu2026.sched.com/event/2HgE0/keynote-rules-of-the-road-for-shared-gpus-ai-inference-scheduling-at-wayve-mukund-muralikrishnan-staff-engineer-wayve
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Rules+of+the+Road+for+Shared+GPUs%3A+AI+Inference+Scheduling+at+Wayve+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Keynote: Rules of the Road for Shared GPUs: AI Inference Scheduling at Wayve.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgE0/keynote-rules-of-the-road-for-shared-gpus-ai-inference-scheduling-at-wayve-mukund-muralikrishnan-staff-engineer-wayve
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Rules+of+the+Road+for+Shared+GPUs%3A+AI+Inference+Scheduling+at+Wayve+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uZeHADfumCU
- YouTube title: Keynote: Rules of the Road for Shared GPUs: AI Inference Scheduling at Wayve - Mukund Muralikrishnan
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/keynote-rules-of-the-road-for-shared-gpus-ai-inference-scheduling-at-w/uZeHADfumCU.txt
- Transcript chars: 2890
- Keywords: across, gpu, workloads, clusters, highly, scheduler, everyone, inferencing, driving, vehicles, regions, including, thousands, process, operate, running, snorts, source

### Resumo baseado na transcript

AI inferencing seems to be the theme for the day, but I'm going to be talking about that as well, but just not about text. One AI model that can learn from vast amounts of data and generalize across vehicles and regions. Kubernetes is incredible, but we lack the granular controls to ensure fairness in a highly competitive multi-tenant environment. During periods of high churn, tens of thousands of pending pods cause degradation in performance in the Kueue scheduler. Kueue is a Kubernetes-native job queuing system with advanced controls for resource management. Even during heavy bursts, Kubernetes scheduler stayed highly performant because it only sees the pods that can actually be allocated on the nodes.

### Excerpt da transcript

Hello everyone, it's great to be here this morning. AI inferencing seems to be the theme for the day, but I'm going to be talking about that as well, but just not about text. At Wave, we build end-to-end AI for autonomous driving. One AI model that can learn from vast amounts of data and generalize across vehicles and regions. Our fleet of vehicles, including from our partners in dashcam OEM and taxis, collect thousands of hours of driving data every day. And to process that requires massive compute. We operate Kubernetes clusters across multiple Azure regions, each running more than 1,000 GPU nodes. >> [snorts] >> These clusters process a huge variety of workloads across different teams, GPU hardware, priorities, and SLAs. At peak, we we handle about 100,000 concurrent workloads. We rely heavily on open source to operate at this scale. I want to thank all the contributors here and the broader open source community for building the technologies that make this possible. Today, I want to highlight our recent adoption of Kueue to schedule our AI inferencing workloads.

It has helped us improve the utilization of one of our most expensive and scarce GPU clusters from 85% to over 95%. Kubernetes is incredible, but we lack the granular controls to ensure fairness in a highly competitive multi-tenant environment. During periods of high churn, tens of thousands of pending pods cause degradation in performance in the Kueue scheduler. That's where Kueue came in. Kueue is a Kubernetes-native job queuing system with advanced controls for resource management. It complements Kueue scheduler rather than trying to replace it. It's highly scalable. We have scaled tested it up to 100,000 pods. And it required no code changes to integrate with our existing workloads. >> [snorts] >> Each team gets a guaranteed allocation, and when they don't use it, other teams can burst into that capacity, and Kueue ensures it's distributed in a fair manner. Soon after the launch, we saw average wait times drop across all the teams. Especially for the smaller teams which used to get starved, the wait times came down by almost 70%.

Even during heavy bursts, Kubernetes scheduler stayed highly performant because it only sees the pods that can actually be allocated on the nodes. As a result, the utilization of our GPU cluster jumped from 85% to 97%. But the best part is that we went from desiring to implement Kueue and having it running at full production scale in less than a month, including a
