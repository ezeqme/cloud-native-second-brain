---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Networking"]
speakers: ["Kevin Wang", "Huawei"]
sched_url: https://kccncna2025.sched.com/event/27Fe7/intelligent-topology-for-ai-power-network-aware-scheduling-optimization-with-volcano-hypernode-kevin-wang-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Intelligent+Topology+for+AI+Power%3A+Network-Aware+Scheduling+Optimization+With+Volcano+HyperNode+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Intelligent Topology for AI Power: Network-Aware Scheduling Optimization With Volcano HyperNode - Kevin Wang, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Kevin Wang, Huawei
- Schedule: https://kccncna2025.sched.com/event/27Fe7/intelligent-topology-for-ai-power-network-aware-scheduling-optimization-with-volcano-hypernode-kevin-wang-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Intelligent+Topology+for+AI+Power%3A+Network-Aware+Scheduling+Optimization+With+Volcano+HyperNode+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Intelligent Topology for AI Power: Network-Aware Scheduling Optimization With Volcano HyperNode.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fe7/intelligent-topology-for-ai-power-network-aware-scheduling-optimization-with-volcano-hypernode-kevin-wang-huawei
- YouTube search: https://www.youtube.com/results?search_query=Intelligent+Topology+for+AI+Power%3A+Network-Aware+Scheduling+Optimization+With+Volcano+HyperNode+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KwPHDI4qusc
- YouTube title: Intelligent Topology for AI Power: Network-Aware Scheduling Optimization With Volcano... Kevin Wang
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/intelligent-topology-for-ai-power-network-aware-scheduling-optimizatio/KwPHDI4qusc.txt
- Transcript chars: 17773
- Keywords: topology, network, basically, define, actually, volcano, cluster, implementation, labels, scheduling, always, trying, performance, discovery, another, details, support, product

### Resumo baseado na transcript

Uh today I'm going to introduce uh some of the work of uh I have been working on and also with a lot of uh maintainers within the uh uh volcano community. I have been uh working on uh Kubernetes as well as uh scheduling relevant stuff for uh 10 years. For example, uh in the early days we may use PCIe but the bandwidth of PCIe got some bottleneck right when we are trying to load uh large scale model and also for the uh the orchestrator layer layer perspectively uh uh you know that Kubernetes default is kind of part of the scheduleuler and uh we have seen a lot of kind of uh challenge when trying to support uh both uh batch workloads uh training and [snorts] as well as the uh inference and which would result in So uh there are some of uh kind of example of the uh big AI clusters network architecture. Some of the company they prefer to design uh the network by themselves like uh still reuse the uh span leaf idea and to integrate with infinib band and also uh uh over ethernet roi.

### Excerpt da transcript

Hello everyone. Uh thank you for joining my talk. Uh today I'm going to introduce uh some of the work of uh I have been working on and also with a lot of uh maintainers within the uh uh volcano community. Uh so I I will brief briefly introduce myself. So I'm Kevin Wan. I work for Huawei. I have been uh working on uh Kubernetes as well as uh scheduling relevant stuff for uh 10 years. Yeah. Um I have multiple roles in the uh community including vice chair on the technical oversight committee of CNCF and I am also co-founder and maintainer for uh multiple uh CNCF projects. Uh but today uh my talk is all about the scheduling thing. So I'm uh wearing my uh hat of uh volcano maintainer. Okay. So uh this talk I will just uh introduce our uh understanding of the uh modern especially the AI cluster uh network thing and why we need a hyperodera concept and how we deal with the uh uh implementation perspective. So uh maybe for uh the background that we don't need to go through too much details uh we just we have seen there are uh the scale of uh the model especially the LM has becoming larger and the lar larger and we have seen a lot of um big players uh spinning up with their own uh AI cluster to better support uh including training as well like um uh inference and uh some of the latest investment also starting working on the uh AI agent.

So uh we can see that like uh for trending uh more and more people you know running the uh distributed uh parallelism uh madam uh pattern including like data pipeline model pipeline and a lot of other uh sorry uh data parallelism uh model parallelism and also pipeline paralism for example and also like uh more and more uh LM deployment would prefer like per few decode disagregation uh deployment pattern to improve the end to end uh throughput and also trying to get lower latency. Uh but we all know that uh the uh there are kind of a lot of uh advanced uh requirement for the underlying uh network trying to you know to uh uh deal with the uh bottleneck. For example, uh in the early days we may use PCIe but the bandwidth of PCIe got some bottleneck right when we are trying to load uh large scale model and also for the uh the orchestrator layer layer perspectively uh uh you know that Kubernetes default is kind of part of the scheduleuler and uh we have seen a lot of kind of uh challenge when trying to support uh both uh batch workloads uh training and [snorts] as well as the uh inference and which would result in like if your uh basic
