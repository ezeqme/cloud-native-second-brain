---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Wei-Cheng Lai", "Bloomberg", "Han-Ju Chen", "Anyscale"]
sched_url: https://kccnceu2026.sched.com/event/2CW5v/achieving-resilient-multi-cluster-ai-inference-on-kubernetes-with-karmada-and-kuberay-wei-cheng-lai-bloomberg-han-ju-chen-anyscale
youtube_search_url: https://www.youtube.com/results?search_query=Achieving+Resilient+Multi-Cluster+AI+Inference+on+Kubernetes+With+Karmada+and+KubeRay+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Karmada and KubeRay - Wei-Cheng Lai, Bloomberg & Han-Ju Chen, Anyscale

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Wei-Cheng Lai, Bloomberg, Han-Ju Chen, Anyscale
- Schedule: https://kccnceu2026.sched.com/event/2CW5v/achieving-resilient-multi-cluster-ai-inference-on-kubernetes-with-karmada-and-kuberay-wei-cheng-lai-bloomberg-han-ju-chen-anyscale
- Busca YouTube: https://www.youtube.com/results?search_query=Achieving+Resilient+Multi-Cluster+AI+Inference+on+Kubernetes+With+Karmada+and+KubeRay+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Karmada and KubeRay.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5v/achieving-resilient-multi-cluster-ai-inference-on-kubernetes-with-karmada-and-kuberay-wei-cheng-lai-bloomberg-han-ju-chen-anyscale
- YouTube search: https://www.youtube.com/results?search_query=Achieving+Resilient+Multi-Cluster+AI+Inference+on+Kubernetes+With+Karmada+and+KubeRay+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SEBoBbyUdz0
- YouTube title: Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Kar... Wei-Cheng Lai & Han-Ju Chen
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/achieving-resilient-multi-cluster-ai-inference-on-kubernetes-with-karm/SEBoBbyUdz0.txt
- Transcript chars: 22784
- Keywords: cluster, serving, gpu, inference, resource, single, policy, reserve, python, clusters, requests, workloads, learning, distributed, production, failover, autoscaling, replica

### Resumo baseado na transcript

Uh due to visa issues, my partner won't be able to give the talk with me in person, but he will record a video to explain the commod related part of the presentation. Today we will share a practical approach for running AI serving reliably at scale on Kubernetes under uneven GPU capacity and regional failure risks. Next, I will explain why a single cluster with standard Kubernetes primitives becomes a bottleneck. Given these production requirements, single cluster Kubernetes and standard primitives fall short in two areas. Second is the venina kernetes gap standard service and deployments are not designed for inference serving features such as multi-node and multi-GPU execution. A normal HPA scale down or raw can interrupt inflight requests and token strings.

### Excerpt da transcript

Hello everyone and welcome to KubeCon Europe. My name is Hanuch Chen and my partner my co-presenter is Wan Lai. I work at any scale and any scale is the company behind Ray. The open source standard for distributed computing in Python. Uh due to visa issues, my partner won't be able to give the talk with me in person, but he will record a video to explain the commod related part of the presentation. Today we will share a practical approach for running AI serving reliably at scale on Kubernetes under uneven GPU capacity and regional failure risks. Here is a plan. We will start the production challenges including bursty traffic, strict P95 and P99 latency targets and GPU scarcity and explain why these push single cluster coronetes to its limits. We will then present a two-layer blueprint. The first layer is fleet orchestration across clusters. The second layer is inference serving inside each cluster. Wan and I will split the session. Wan will cover the flea layer and show how commada applies policy for placement replicas spreading per cluster overrides and automated failover.

I will cover the sering layer and show how reserve by kra ray service including requestdriven autoscaling safe upgrades and advanced feature racer provides. By the end, you will have a vendor neutral reference architecture you can adapt. Now, let's start with the challenge. To start, I want to set a clear baseline. At scale, air serving has production requirements that are strict stricter than most dataless microser. First, we need predictable service level objects. That makes tight P95 and P99 latency targets, strong availability and controlled error rates. Even when traffic is bursty. Second, we need elastic capacity and GPU efficiency. Traffic can spike quickly but scaling serving is not instantaneous. Models need one time including loading large weights and inocite initializing GPU memory. We need absorb spikes without building large cues while also avoiding overprovisioning and leaving expensive GPUs idle. That makes right sizing and utilization critical. Third, we need regional locality to meet latency budgets and comply with data residency boundaries.

especially relevant here in Europe. Inference often needs to run close to users and within specific regions. Finally, we need safe operations and visibility. We need rollouts that are gated by health signals, clear rollback paths and model level telemetry such as tail latency, Q depths, and error rates. Many inference requests are
