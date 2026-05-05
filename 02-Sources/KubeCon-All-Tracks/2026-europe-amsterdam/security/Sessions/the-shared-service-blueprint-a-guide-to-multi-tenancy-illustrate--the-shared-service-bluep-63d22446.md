---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "Networking"]
speakers: ["Aya Igarashi", "Preferred Networks", "Inc."]
sched_url: https://kccnceu2026.sched.com/event/2CW6n/the-shared-service-blueprint-a-guide-to-multi-tenancy-illustrated-with-keda-aya-igarashi-preferred-networks-inc
youtube_search_url: https://www.youtube.com/results?search_query=The+Shared+Service+Blueprint%3A+A+Guide+to+Multi-Tenancy%2C+Illustrated+With+KEDA+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Shared Service Blueprint: A Guide to Multi-Tenancy, Illustrated With KEDA - Aya Igarashi, Preferred Networks, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Aya Igarashi, Preferred Networks, Inc.
- Schedule: https://kccnceu2026.sched.com/event/2CW6n/the-shared-service-blueprint-a-guide-to-multi-tenancy-illustrated-with-keda-aya-igarashi-preferred-networks-inc
- Busca YouTube: https://www.youtube.com/results?search_query=The+Shared+Service+Blueprint%3A+A+Guide+to+Multi-Tenancy%2C+Illustrated+With+KEDA+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Shared Service Blueprint: A Guide to Multi-Tenancy, Illustrated With KEDA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6n/the-shared-service-blueprint-a-guide-to-multi-tenancy-illustrated-with-keda-aya-igarashi-preferred-networks-inc
- YouTube search: https://www.youtube.com/results?search_query=The+Shared+Service+Blueprint%3A+A+Guide+to+Multi-Tenancy%2C+Illustrated+With+KEDA+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=krOs-eKeH24
- YouTube title: The Shared Service Blueprint: A Guide to Multi-Tenancy, Illustrated With KEDA - Aya Igarashi
- Match score: 1.0
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-shared-service-blueprint-a-guide-to-multi-tenancy-illustrated-with/krOs-eKeH24.txt
- Transcript chars: 14979
- Keywords: tenant, server, operator, namespace, authentication, network, shared, resource, single, isolation, design, traffic, metric, boundary, router, policy, multi-tenency, identity

### Resumo baseado na transcript

Today I'll be talking about reality of providing shared service in multi-tenant Kubernetes cluster. I'll use Keta as a case study to show how we can achieve namespace tenant isolation even when the service wasn't originally designed for it. When we build an in-house component, we can design for our own platform from the beginning. Also, KA touches many boundary at once both internal Kubernetes cluster and external cloud integrations. Before we dive into the design, let's do a quick recap of how Keta works. Kai extend horizontal autocaler called HPA using Kubernetes external matrix.

### Excerpt da transcript

Hi everyone, thank you for joining. I'm Aaya Garash, software engineer at Preferred Networks. Today I'll be talking about reality of providing shared service in multi-tenant Kubernetes cluster. I'll use Keta as a case study to show how we can achieve namespace tenant isolation even when the service wasn't originally designed for it. Here's our road map for today. First, I'll explain why multi-tenency is needed for our platform and why we choose our specific isolation model. Then we'll dive into KA and look at why we choose the pertinent deployment model. the main part of this talk on four kubernetes constraints which we have to solve at the end I'll come back to the full architecture and design lessons a bit preferred network is a full stack AI company we build everything from research motor down to custom AI chips called M& core we deliver this computing power through the our preferred computing platform a kubernetes based environment serving both internal and external researchers. PFCP is not an anonymous pro public service where anyone can sign up and create workloads but still we share clusters across different organizations.

So multi-tenency is our business requirement. They give us two constraints. Tenant credential must stay separated and fader must stay contained. If something goes wrong, this unlike simple misconfiguration, it should never become another tenants problem. That's why keeping a small blast radius is key to our design. Here's a major Kubernetes multi-tenency patterns. Kubernetes multi-tenency is a spectrum. On the local side, you have a shared control plane with names based isolation. As you move to the stronger isolation, you pay more for virtual clusters, dedicated nodes or physically fully separated classes. Of course, there's no single correct answers here. It all depends on your requirements. And for our perform, we combine two levels. default namespace isolation for everyone and optional node level isolation for those who need it. This give us a balance of flexibility within a single cluster and this is our actual tenency model. Each tenant owner root namespace and its owner can manage its child name spaces.

We use hier h high hierarchical name spaces called h and c to handle that structure and ensure things like resource quarter something like that consistency as some of you might know the kubernetus or hnc project has already been archived but it's essential for our platform so we keep developing our fk version The important
