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
themes: ["Platform Engineering", "Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sung Yun", "Antoine Marthey", "Bloomberg LP"]
sched_url: https://kccnceu2026.sched.com/event/2CW5I/disaster-resilient-trino-on-kubernetes-multi-cluster-setup-with-karmada-and-trino-gateway-sung-yun-antoine-marthey-bloomberg-lp
youtube_search_url: https://www.youtube.com/results?search_query=Disaster+Resilient+Trino+on+Kubernetes%3A+Multi-Cluster+Setup+With+Karmada+and+Trino+Gateway+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karmada and Trino Gateway - Sung Yun & Antoine Marthey, Bloomberg LP

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sung Yun, Antoine Marthey, Bloomberg LP
- Schedule: https://kccnceu2026.sched.com/event/2CW5I/disaster-resilient-trino-on-kubernetes-multi-cluster-setup-with-karmada-and-trino-gateway-sung-yun-antoine-marthey-bloomberg-lp
- Busca YouTube: https://www.youtube.com/results?search_query=Disaster+Resilient+Trino+on+Kubernetes%3A+Multi-Cluster+Setup+With+Karmada+and+Trino+Gateway+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karmada and Trino Gateway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5I/disaster-resilient-trino-on-kubernetes-multi-cluster-setup-with-karmada-and-trino-gateway-sung-yun-antoine-marthey-bloomberg-lp
- YouTube search: https://www.youtube.com/results?search_query=Disaster+Resilient+Trino+on+Kubernetes%3A+Multi-Cluster+Setup+With+Karmada+and+Trino+Gateway+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vGjiXGdax98
- YouTube title: Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karma... Sung Yun & Antoine Marthey
- Match score: 0.954
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/disaster-resilient-trino-on-kubernetes-multi-cluster-setup-with-karmad/vGjiXGdax98.txt
- Transcript chars: 24172
- Keywords: cluster, gateway, deployment, platform, server, center, endpoint, queries, controller, actually, question, clusters, single, availability, disaster, architecture, resource, deploy

### Resumo baseado na transcript

I'm S and I lead the manageo and iceberg platform engineering team at Bloomberg. >> Um I'm Antoine and I'm a engineer in the manage uh Trino and iceberg team uh at Bloomberg. On the other side, we have the query user who are the analysts, engineers or applications that connect to a query endpoint and submit SQL queries. Trina service owners expect predictable life cycle management and query users expect a reliable query endpoint. In our previous architecture, meeting those expectations required those personas to coordinate those failures. The core challenge with Trino is that queries are stateful and tied to a specific coordinator.

### Excerpt da transcript

All right. Hello everyone. I'm S and I lead the manageo and iceberg platform engineering team at Bloomberg. >> Um I'm Antoine and I'm a engineer in the manage uh Trino and iceberg team uh at Bloomberg. >> All right. Nice to meet you all. Thanks. Thank you all for coming at this late hour today. >> All right. So last year at KubeCon we shared how we built a secure govern platform on Kubernetes by leveraging open policy agent a CNCF project. Over the past year as adoption grew the next set of challenges became very clear. Data governance was no longer our bottleneck. The real challenge had shifted to building a highly available data platform on top of our trainer clusters. That shift pushed us to evolve the platform from a single cluster governed a governance focused architecture to a multicluster deploymentbased design where high availability and data disaster resilience are first class concerns. So today I'll set the context for that evolution and Antoine will walk us through how we built uh and designed this next generation Tuno platform.

Our managed Truno platform serves two primary personas. On one side, we have the Truna service owners, which is typically an engineering team that is defining and managing a Truno service, configuring the cataloges that they want to attach and the resource limits they want to launch the pods with. On the other side, we have the query user who are the analysts, engineers or applications that connect to a query endpoint and submit SQL queries. For both personas, the expectations are very clear. Trina service owners expect predictable life cycle management and query users expect a reliable query endpoint. In our previous architecture, meeting those expectations required those personas to coordinate those failures. The core challenge with Trino is that queries are stateful and tied to a specific coordinator. If that coordinator fails, the query doesn't transparently fail over. It is simply lost. So availability isn't something we can make perfect within the Trina system. But what we can do is to make failures predictable and make recovery and failover of responsibility of the platform instead of leaving it to the users.

Let's briefly recap the single cluster architecture we shared last year. On a high level, Trino service owners express their intent to deploy Trino onto a cluster through an API. And within our platform, that intent is represented at two levels. The Trinos service owners interact with a simplified abstracti
