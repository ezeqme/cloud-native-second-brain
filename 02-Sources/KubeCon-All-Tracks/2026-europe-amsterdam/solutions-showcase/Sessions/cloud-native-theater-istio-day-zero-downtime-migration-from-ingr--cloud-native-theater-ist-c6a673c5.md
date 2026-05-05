---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Platform Engineering", "Networking", "Kubernetes Core"]
speakers: ["Joe Abellard", "Bloomberg"]
sched_url: https://kccnceu2026.sched.com/event/2EG0q/cloud-native-theater-istio-day-zero-downtime-migration-from-ingress-nginx-to-istio-in-a-multi-cluster-kubernetes-platform-at-bloomberg-joe-abellard-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Zero-Downtime+Migration+from+ingress-nginx+to+Istio+in+a+Multi-Cluster+Kubernetes+Platform+at+Bloomberg+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Istio Day: Zero-Downtime Migration from ingress-nginx to Istio in a Multi-Cluster Kubernetes Platform at Bloomberg - Joe Abellard, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Platform Engineering]], [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joe Abellard, Bloomberg
- Schedule: https://kccnceu2026.sched.com/event/2EG0q/cloud-native-theater-istio-day-zero-downtime-migration-from-ingress-nginx-to-istio-in-a-multi-cluster-kubernetes-platform-at-bloomberg-joe-abellard-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Zero-Downtime+Migration+from+ingress-nginx+to+Istio+in+a+Multi-Cluster+Kubernetes+Platform+at+Bloomberg+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Istio Day: Zero-Downtime Migration from ingress-nginx to Istio in a Multi-Cluster Kubernetes Platform at Bloomberg.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0q/cloud-native-theater-istio-day-zero-downtime-migration-from-ingress-nginx-to-istio-in-a-multi-cluster-kubernetes-platform-at-bloomberg-joe-abellard-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Zero-Downtime+Migration+from+ingress-nginx+to+Istio+in+a+Multi-Cluster+Kubernetes+Platform+at+Bloomberg+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wix_PfQ61jY
- YouTube title: Cloud Native Theater | Istio Day: Zero-Downtime Migration from ingress-nginx to Isti... Joe Abellard
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-istio-day-zero-downtime-migration-from-ingress-ng/wix_PfQ61jY.txt
- Transcript chars: 16226
- Keywords: cluster, clusters, traffic, ingress, multicluster, metrics, running, migration, platform, engineext, control, prometheus, orchestration, across, server, topology, bloomberg, managed

### Resumo baseado na transcript

Um, and in this talk, I'll walk you through how we executed a zero downtime migration from the now retired um Angress EngineX um to our multicluster platform built at top commada um at Bloomberg. Um this is a very timely talk because the ingress engineext repo actually got archived earlier today. Um a common pattern for solving these type of problems is by using multicluster orchestration. Um and ideally to avail of the existing Kubernetes tool chain that the central component in that orchestration layer should be the cube API server. So Kada is a CNCF project for um Kubernetes native multicluster management um that enables you to run your workloads across entire fleets of clusters. Um architecturally a comma setup looks very similar to a Kubernetes cluster setup that all of you are familiar with.

### Excerpt da transcript

Okay, welcome everyone. I'm Joe. I work as a senior software engineer at Bloomberg. Um, and in this talk, I'll walk you through how we executed a zero downtime migration from the now retired um Angress EngineX um to our multicluster platform built at top commada um at Bloomberg. Um this is a very timely talk because the ingress engineext repo actually got archived earlier today. So, it's officially dead. This is our agenda for today. So I'll start by um talking about the need for multicluster orchestration at Bloomberg and how multicluster orchestration has evolved as a key enabler for achieving um data center redundancy at scale. Um then I'll talk about comma and how we built a fully managed platform at top kada to fulfill our use cases for multicluster orchestration. Um and at this point everyone should have a very good understanding of our managed platform. So then I'll dive into um ingress traffic semantics our use cases for ingress traffic. Um then I'll talk about the migration strategies we explored as well as how we preserve routing semantics as we executed that migration.

Um and lastly I'll talk about future um work ahead. So let's get started. So at Bloomberg many of our platform teams run a top Kubernetes. Um so for a second let's just assume that this Kubernetes cluster is a cluster powering one of our platforms and then in a disaster scenario um it goes down at Bloomberg um data center redundancy to ensure continuity of service in these type of disaster scenarios is mission critical. So this is a huge problem that we have to solve. Um a common pattern for solving these type of problems is by using multicluster orchestration. Um and the way that works is you start by building multiple clusters that are strategically placed across multiple data centers or failure domains. Um and once you have those clusters set up, you then need a multicluster orchestrator or orchestration layer that can make placement decisions across that fleet of clusters. Um and ideally to avail of the existing Kubernetes tool chain that the central component in that orchestration layer should be the cube API server.

Um, and in that control plane, you should also have a scheduler that at a bare minimum can make intelligent placement decisions across your fleet of clusters. An added bonus would be something like support for automated um, failover in a disaster scenario. Um, and at Bloomberg um, we've converged on the CNCF um, commada project as our multicluster orchestrator.
