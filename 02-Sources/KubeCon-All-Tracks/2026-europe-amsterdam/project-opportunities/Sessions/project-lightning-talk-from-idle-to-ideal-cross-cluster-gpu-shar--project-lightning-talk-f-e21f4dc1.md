---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Takao Indoh", "Contributor"]
sched_url: https://kccnceu2026.sched.com/event/2GjrE/project-lightning-talk-from-idle-to-ideal-crosscluster-gpu-sharing-with-cohdi-takao-indoh-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+From+Idle+to+Ideal%3A+Cross%E2%80%91Cluster+GPU+Sharing+with+CoHDI+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: From Idle to Ideal: Cross‑Cluster GPU Sharing with CoHDI - Takao Indoh, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Takao Indoh, Contributor
- Schedule: https://kccnceu2026.sched.com/event/2GjrE/project-lightning-talk-from-idle-to-ideal-crosscluster-gpu-sharing-with-cohdi-takao-indoh-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+From+Idle+to+Ideal%3A+Cross%E2%80%91Cluster+GPU+Sharing+with+CoHDI+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: From Idle to Ideal: Cross‑Cluster GPU Sharing with CoHDI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2GjrE/project-lightning-talk-from-idle-to-ideal-crosscluster-gpu-sharing-with-cohdi-takao-indoh-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+From+Idle+to+Ideal%3A+Cross%E2%80%91Cluster+GPU+Sharing+with+CoHDI+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=v6TlA7PNOR4
- YouTube title: Project Lightning Talk: From Idle to Ideal: Cross‑Cluster GPU Sharing with CoHDI - Takao Indoh
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-from-idle-to-ideal-cross-cluster-gpu-sharing-wi/v6TlA7PNOR4.txt
- Transcript chars: 2543
- Keywords: cluster, gpu, clusters, hardware, devices, inference, detach, infrastructure, memory, attach, composable, compose, sharing, cannot, across, shared, attached, training

### Resumo baseado na transcript

Today I will talk about uh from idle to ideal crosscluster GPU sharing with Kodi. At the same time, GPUs and memory are getting more expensive and scarcer. This is this reduce idle time and lower infrastructure cost and scale effect efficiently. Composable infrastructure let us create softwaredefined bare metal systems with codi GPU can can be dynamically attached and decide detached to kubernetes nodes. We are currently tracing uh tracking kubernetes scheduleuler uh changes in version 1.36 as beta.

### Excerpt da transcript

Hello everyone. Uh thank you for joining. My name is Taka Indoor from Fujitu. Today I will talk about uh from idle to ideal crosscluster GPU sharing with Kodi. Today AI workloads keep increasing. At the same time, GPUs and memory are getting more expensive and scarcer. Many organization cannot can no longer buy dedicated CPUs for every team or every cluster. So the key question is uh what if we could maximize device utilization across multiple Kubernetes clusters. On the left in the picture, some clusters have idle GPUs and other clusters are GPU stabbed. So we want to balance this. However, there is a challenge. Traditionally, Cubantis manages hardware only inside each cluster boundary. There is no straightforward and safe way to lend devices across the cluster. So idle capacity in cluster A cannot easily help cluster B. This is the problem we want to solve. This is an idea to resolve this problem. Here is how it works dayto day. We keep a shared GPU and memory pool. During the day, inference traffic is heavy.

So, we attached more GPUs to inference clusters. At night, training and batch jobs could dominate. So, we detach the inference cluster uh detach devices from inference cluster and attach it to training cluster. So that mean attach when needed and detach when not needed. This is this reduce idle time and lower infrastructure cost and scale effect efficiently. The main idea is simple. GPU are allocated to where we they create the most value at the right time. Our approach is codi that means composable hardware in disagregated infrastructure. Composable infrastructure let us create softwaredefined bare metal systems with codi GPU can can be dynamically attached and decide detached to kubernetes nodes. We use a resource pool of hardware, GPUs, memory and other devices and a management layer to compose the right bare metal at the right time. In short, put devices in shared pool and compose compose node you need attach or detach GPUs on on demand. This make the hardware flexible and flexible not fixed. Cody works with Kubernetes scheduleuler and dr.

We are currently tracing uh tracking kubernetes scheduleuler uh changes in version 1.36 as beta. We have just released kodi version 0.0.1.1. We have provided composable infrastructure emulator. You can uh try this. If you want to talk more, please visit us at the project pavilion and you can also scan the QR code on the screen and to see the code and docs and join the project. So that is it. Thank you for li
