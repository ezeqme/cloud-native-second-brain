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
themes: ["Keynote Sessions"]
speakers: []
sched_url: https://kccnceu2026.sched.com/event/2HgW4/keynote-live-demo-showcase
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Live+Demo+Showcase+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Keynote: Live Demo Showcase

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Keynote Sessions]]
- País/cidade: Netherlands / Amsterdam
- Speakers: N/A
- Schedule: https://kccnceu2026.sched.com/event/2HgW4/keynote-live-demo-showcase
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Live+Demo+Showcase+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Keynote: Live Demo Showcase.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgW4/keynote-live-demo-showcase
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Live+Demo+Showcase+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cTXlkhKXgyE
- YouTube title: Keynote: Live Demo Showcase
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/keynote-live-demo-showcase/cTXlkhKXgyE.txt
- Transcript chars: 13753
- Keywords: backstage, perses, dashboards, applause, catalog, actions, installed, prometheus, everyone, gpu, support, actually, another, thanks, access, claude, llm, memory

### Resumo baseado na transcript

Hi everyone, I'm Dimotion and I'm the co-founder and the CTO of the Dynamia and also the maintainer of Hami project. So Hami is a GPU orchestration solution that allows you to slice GPUs into virtual devices and therefore allowing you to run more workloads in parallel and also reducing cost and time to market. The first one is as you have you have seen in the demo, we have the dynamic MIG partitioning. And also we since we are Kubernetes native, we we we have completely transparent to the user task and we have implemented in the DAI way as well, yeah. So if we look at the logs here, the LLM is almost done, so we should get an output in a second. Well, at Spotify, we're collecting usage metrics for both AI and our internal Backstage UI and we have seen an increase in UI usage over the last few months.

### Excerpt da transcript

Hey everyone, this is Reza, solution engineer at Hami. Hi everyone, I'm Dimotion and I'm the co-founder and the CTO of the Dynamia and also the maintainer of Hami project. So Hami is a GPU orchestration solution that allows you to slice GPUs into virtual devices and therefore allowing you to run more workloads in parallel and also reducing cost and time to market. So simple use case, for example, you have a PyTorch notebook user, some support chat, both of them requesting two GPUs, one of them with 10G, the other one with 20G each. Before Hami, you would basically fill up a four-node GPU cluster. After Hami, Hami packs them nicely together and you get two extra GPUs for free. Um We have five case studies on the CNCF website right now. One of them, Baidu, actually their inference tasks were starving out LLM and training jobs and after using Hami, they they reduced their cost by 2/3. Another one is SF Express that actually needed our custom memory isolation to have their workloads more stable. With that, I'm going to switch to the demo.

Uh sorry. Um what you see is basically three GPU three GPU clusters, um two A100s each. One of them is configured for um One of them is configured for MIG and I'm going to run two extra LLM workloads. One on the MIG node and cannot see actually. One on the MIG node and one uh on the on the normal one. So what's going to happen is you see I'm allocating 25 gigs for the normal one, I'm allocating 10 gigs for the MIG node, which is going to do the MIG partitions automatically itself here. And then up here you see the custom memory isolation where you have one NVIDIA SMI output with 25G. And if I reload this, you'll see that these are now scheduled here. And with that, Motion. Thanks Reza. Since there are theoretical some time for the VM module to warm up, so I will give a brief introduction to the core capabilities of Hami. So I think the most two most intriguing things about Hami is the first we have a heterogeneous system management. It means that besides NVIDIA GPU, we also support Huawei Ascend NPU, Cambricon MLU and AWS Neuron devices and as well as Meta X, Innova her and many other sorts of accelerators.

They all can be partitioned by the Hami project. And the another is how we handle the hard resource isolation inside the container. We can do this in two ways. The first one is as you have you have seen in the demo, we have the dynamic MIG partitioning. The other is we have a self-implemented CUDA access layer, which can
