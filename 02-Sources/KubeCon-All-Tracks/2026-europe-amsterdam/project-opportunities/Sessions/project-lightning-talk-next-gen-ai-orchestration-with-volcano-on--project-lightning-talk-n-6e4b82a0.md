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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Zhonghu Xu", "Principal Engineer"]
sched_url: https://kccnceu2026.sched.com/event/2EFy5/project-lightning-talk-next-gen-ai-orchestration-with-volcano-on-kubernetes-zhonghu-xu-principal-engineer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Next-Gen+AI+Orchestration+With+Volcano+On+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Next-Gen AI Orchestration With Volcano On Kubernetes - Zhonghu Xu, Principal Engineer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Zhonghu Xu, Principal Engineer
- Schedule: https://kccnceu2026.sched.com/event/2EFy5/project-lightning-talk-next-gen-ai-orchestration-with-volcano-on-kubernetes-zhonghu-xu-principal-engineer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Next-Gen+AI+Orchestration+With+Volcano+On+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Next-Gen AI Orchestration With Volcano On Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFy5/project-lightning-talk-next-gen-ai-orchestration-with-volcano-on-kubernetes-zhonghu-xu-principal-engineer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Next-Gen+AI+Orchestration+With+Volcano+On+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0vYUzJ7eO8M
- YouTube title: Project Lightning Talk: Next-Gen AI Orchestration With Volcano On Kubernetes - Zhonghu Xu
- Match score: 1.012
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-next-gen-ai-orchestration-with-volcano-on-kuber/0vYUzJ7eO8M.txt
- Transcript chars: 5476
- Keywords: volcano, scheduling, support, topology, native, workloads, network, training, inference, currently, unified, switch, already, workflows, platform, framework, performances, called

### Resumo baseado na transcript

Uh I'm from Huawei technology and this is currently one of the volcano maintainer. Uh today my topic is nextg AI orchestration with volcano on kubernetes. So different workload characters uh pose challenge to theuler uh and volcano has been uh widely used in AI training uh since in incubation. a training a inference agent workflows and collaborate uh with other more communities such as uh reinforcement uh learning areas inference framework and agent work agent frameworks. So and and at the bottom volcano will support uh more hoggenous uh devices uh as a unified hogenous uh device alloc allocated pore and and support more features in the network architecture uh topology aware scheduling uh to improve the AI workloads performances. What we saw is that large scale AI clusters uh lacks unified topology abstraction uh requiring uh requiring multi uh optimize the intra and the internal configuration for uh maximum performances.

### Excerpt da transcript

Uh I'm from Huawei technology and this is currently one of the volcano maintainer. Um so let's begin. Uh today my topic is nextg AI orchestration with volcano on kubernetes. So let's get a quick overview of volcano. Some listeners might have uh listen uh already been familiar with the volcano before uh but others may not. So let's quick get a quick look look at the volcano project. Uh volcano was originated from the cub badge uh and has been work as a cloud cloud native batch system. Uh it can perform uh queue management and GA scheduling and and do has a lots of reach for ecosystem and support a lot of heterogeneous uh device. A few years ago, most clusters uh were dominated by the batch scal uh training. But in 2023, more and more large language models are emerging uh and OM training uh is experienced uh explosive growth. So now we run also into the uh disagregated uh OM inferences uh where prefer and decode have different resource requirement and currently we also have the agent workloads which is uh bursty sure leave.

So different workload characters uh pose challenge to theuler uh and volcano has been uh widely used in AI training uh since in incubation. So can we will continue to evolve uh and to support uh AOM inference and agent workflows to build as a unified scheduling platform. So here the volcano technical uh road map for this year and uh beyond from so the front top level volcano will uh not only support the VC job uh the no native uh will also support more uh native workloads to support massi uh a training a inference agent workflows and collaborate uh with other more communities such as uh reinforcement uh learning areas inference framework and agent work agent frameworks. So and and at the bottom volcano will support uh more hoggenous uh devices uh as a unified hogenous uh device alloc allocated pore and and support more features in the network architecture uh topology aware scheduling uh to improve the AI workloads performances. So let's follow the road map to introduce what we update in in the last year.

Uh one of is that uh what kind is originated from the batchuler uh can do the batch workflows uh scheduling uh but the its framework is to schedule batch workloads uh per second. So the but the aging workloads uh may be sensit latency sensitive and and need to burst it. So uh we uh build build a a new a uhuler called agentuler uh in the uh previous version uh to coordinated it with the uh existing batchuler uh to courrenly uh scheduling
