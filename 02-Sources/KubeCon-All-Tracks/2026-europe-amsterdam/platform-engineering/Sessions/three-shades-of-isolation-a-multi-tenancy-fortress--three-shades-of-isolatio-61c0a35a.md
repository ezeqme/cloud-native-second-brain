---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Braulio Dumba", "Paolo Dettori", "IBM"]
sched_url: https://kccnceu2026.sched.com/event/2CW7T/three-shades-of-isolation-a-multi-tenancy-fortress-braulio-dumba-paolo-dettori-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Three+Shades+of+Isolation%3A+A+Multi-tenancy+Fortress+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Three Shades of Isolation: A Multi-tenancy Fortress - Braulio Dumba & Paolo Dettori, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Braulio Dumba, Paolo Dettori, IBM
- Schedule: https://kccnceu2026.sched.com/event/2CW7T/three-shades-of-isolation-a-multi-tenancy-fortress-braulio-dumba-paolo-dettori-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Three+Shades+of+Isolation%3A+A+Multi-tenancy+Fortress+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Three Shades of Isolation: A Multi-tenancy Fortress.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7T/three-shades-of-isolation-a-multi-tenancy-fortress-braulio-dumba-paolo-dettori-ibm
- YouTube search: https://www.youtube.com/results?search_query=Three+Shades+of+Isolation%3A+A+Multi-tenancy+Fortress+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=24E4LDWThAE
- YouTube title: Three Shades of Isolation: A Multi-tenancy Fortress - Braulio Dumba & Paolo Dettori, IBM
- Match score: 0.838
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/three-shades-of-isolation-a-multi-tenancy-fortress/24E4LDWThAE.txt
- Transcript chars: 26258
- Keywords: control, tenant, cluster, network, isolation, environment, tenants, kubernet, second, workload, running, traffic, workloads, provide, multi-tenency, approach, overhead, source

### Resumo baseado na transcript

So today we are presenting three shade of fisolation and this is really about multi-tenency and our approach to multi-tenency. This combines control plane, data plane and networking isolation using opensource technologies. Fourth, we like to provide a user experience that looks like a Kubernetes experience, a vania kubernetes experience. Tenants should be able to manage their own CRDs, cluster roles, and storage classes. There is always the noisy enable problem to keep in mind in a shared cluster. One tenant highuling throughput or resource intensive workload can degrade performance for others.

### Excerpt da transcript

Hello everyone. How's everyone doing? I hope you're having good time in Amsterdam. Thank you. Okay. So my name is Paulo Detorii. I work for IBM research and this is I'm Dumba. So I work for IBM research. >> Okay. So today we are presenting three shade of fisolation and this is really about multi-tenency and our approach to multi-tenency. This combines control plane, data plane and networking isolation using opensource technologies. First of all, let's talk about the multi-tenency in Kubernetes. What do we mean by multi-tenency? So multi-tenency means sharing a single cluster resources, compute, storage, networking among multiple tenants. What is a tenant? A tenant can be a user, can be a team, can be an application. As Kubernetes adoption becoming more mature, workloads are moving to production. The demand for multi-tenency is growing very rapidly. Organization want to have efficiency and share infrastructure without compromising on isolation. And there are four key requirements for isolation that we have identified.

First of all, we want to have data plane isolation. Tenants should not share compute nodes preventing side channel attacks and resource interference. Second, we have to think about access boundaries, logical segregation through network policies and name spaces. Third, control plane isolation. Each tenant needs their own API server and control plane to manage cluster scope resources independently. Fourth, we like to provide a user experience that looks like a Kubernetes experience, a vania kubernetes experience. Tenants should be able to manage their own CRDs, cluster roles, and storage classes. Why do we need workload isolation? There are three main motivations. Security is the first and is probably the most important. Without proper isolation, one tenant could potentially access other tenants pods, deployments, and secrets. We need to enforce both logical and physical segregation between tenants. Performance is the second concern. There is always the noisy enable problem to keep in mind in a shared cluster.

One tenant highuling throughput or resource intensive workload can degrade performance for others. This especially problematic for latency sensitive AI inferencing workloads. Third, cluster scope resources conflicts in Kubernetes. Objects like CRDs, cluster roles, storage classes exist at the cluster level and cannot be name spaced. When you have multiple A platforms for example Kajenti for agent orchestration, LLD for distribute LLM inf
