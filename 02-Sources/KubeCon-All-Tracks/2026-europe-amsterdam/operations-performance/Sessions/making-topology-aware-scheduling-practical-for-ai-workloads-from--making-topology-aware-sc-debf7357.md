---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Weizhou Lan", "Daocloud"]
sched_url: https://kccnceu2026.sched.com/event/2CW7K/making-topology-aware-scheduling-practical-for-ai-workloads-from-discovery-to-simulation-at-scale-weizhou-lan-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=Making+Topology-Aware+Scheduling+Practical+for+AI+Workloads%3A+From+Discovery+to+Simulation+at+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simulation at Scale - Weizhou Lan, Daocloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Weizhou Lan, Daocloud
- Schedule: https://kccnceu2026.sched.com/event/2CW7K/making-topology-aware-scheduling-practical-for-ai-workloads-from-discovery-to-simulation-at-scale-weizhou-lan-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=Making+Topology-Aware+Scheduling+Practical+for+AI+Workloads%3A+From+Discovery+to+Simulation+at+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simulation at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7K/making-topology-aware-scheduling-practical-for-ai-workloads-from-discovery-to-simulation-at-scale-weizhou-lan-daocloud
- YouTube search: https://www.youtube.com/results?search_query=Making+Topology-Aware+Scheduling+Practical+for+AI+Workloads%3A+From+Discovery+to+Simulation+at+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Jj8DNLA5hYc
- YouTube title: Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simula... Weizhou Lan
- Match score: 0.982
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/making-topology-aware-scheduling-practical-for-ai-workloads-from-disco/Jj8DNLA5hYc.txt
- Transcript chars: 15006
- Keywords: topology, network, scheduling, switch, workloads, within, cluster, labels, constraints, scheduleuler, nvidia, communication, traffic, domain, affinity, volcano, automatically, builder

### Resumo baseado na transcript

Thank you for joining my session and today I would like to give a talk give a session about uh making topology aware scheduling practical for AI workloads from discovery to simulation at scale. Uh I'm Wulan and a senior tech lead at docloud and today I what I discussed goes beyond the scheduleuler. uh workloads from different tenants uh must be free to dynamically scale across all nodes. Uh therefore the flexibility comes with a challenge if loads scale without topology awareness. uh network contention becomes inevitable uh or it can lead to unfair allocation of res network resources uh within certain parts of the topology among tenants to address this challenges we've discussed in in the past slides we need intelligence topologies scheduling it's no longer As the cluster grows, static partitions can cause conflicts between applications and operational costs quickly um uh escalates.

### Excerpt da transcript

Thank you for joining my session and today I would like to give a talk give a session about uh making topology aware scheduling practical for AI workloads from discovery to simulation at scale. Uh I'm Wulan and a senior tech lead at docloud and today I what I discussed goes beyond the scheduleuler. It includes network topology discovery and cost effective approaches for function validations. So let's get started. As we know in model chaining scenarios uh networking communication volume is enormous. uh for conventional dance models such as llama or reduce communication uh uh dominates uh in this pattern data exchange typically occurs among the GPUs uh within each single network re as a result most traffic can be handled locally by leave switches in contrast models like deepseek roots data to different experts and generate intensive all-to-out communication. This traffic frequently traverses the appetire switches to reach destination across different rails. Uh consequently uh in a large scale cluster uh workloads must be placed in an orderly manner according to the topology to avoid the network con congestion.

In inference scenarios, a complex RDMA traffic uh patterns are also unavoidable. A typical example is PD disagregation, a prefilled and decoded workloads. Um needed to synchronize KV cache data. Uh so they must be placed on topologically closed nodes. uh this shortens the switch uh forwarding path and helps avoid uh traffic conflicts uh with other jobs. In addition, MOE model uh inference also invoice all toall communication often requiring traffic to traverse multiple layers of network topology. So related tasks should be placed uh close together within the same network domain and unrelated workloads should be uh spread out to uh minimize pass level traffic contention. Network traffic is further challenged by multi-tenant workloads. In a multi-tenant environment nothing is static. uh we are constantly driven by requirements like uh canary releases and SLA to maximize GPU utilization. We cannot afford to isolate resources for each tenant. Instead, um the cluster is treated as a single full pole. uh workloads from different tenants uh must be free to dynamically scale across all nodes.

Uh therefore the flexibility comes with a challenge if loads scale without topology awareness. uh network contention becomes inevitable uh or it can lead to unfair allocation of res network resources uh within certain parts of the topology among tenants to address this
