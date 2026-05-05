---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Vinay Suryadevara", "Jianfei Hu", "ClickHouse Cloud"]
sched_url: https://kccnceu2024.sched.com/event/1YeNr/cloud-agnostic-approach-to-bin-packing-pods-in-managed-kubernetes-in-aws-gcp-and-azure-vinay-suryadevara-jianfei-hu-clickhouse-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Agnostic+Approach+to+Bin-Packing+Pods+in+Managed+Kubernetes+in+AWS%2C+GCP+and+Azure+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cloud-Agnostic Approach to Bin-Packing Pods in Managed Kubernetes in AWS, GCP and Azure - Vinay Suryadevara & Jianfei Hu, ClickHouse Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Vinay Suryadevara, Jianfei Hu, ClickHouse Cloud
- Schedule: https://kccnceu2024.sched.com/event/1YeNr/cloud-agnostic-approach-to-bin-packing-pods-in-managed-kubernetes-in-aws-gcp-and-azure-vinay-suryadevara-jianfei-hu-clickhouse-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Agnostic+Approach+to+Bin-Packing+Pods+in+Managed+Kubernetes+in+AWS%2C+GCP+and+Azure+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cloud-Agnostic Approach to Bin-Packing Pods in Managed Kubernetes in AWS, GCP and Azure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNr/cloud-agnostic-approach-to-bin-packing-pods-in-managed-kubernetes-in-aws-gcp-and-azure-vinay-suryadevara-jianfei-hu-clickhouse-cloud
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Agnostic+Approach+to+Bin-Packing+Pods+in+Managed+Kubernetes+in+AWS%2C+GCP+and+Azure+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3podlIoxwyI
- YouTube title: Cloud-Agnostic Approach to Bin-Packing Pods in Managed Kubernetes in AWS, GCP and Azure
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cloud-agnostic-approach-to-bin-packing-pods-in-managed-kubernetes-in-a/3podlIoxwyI.txt
- Transcript chars: 35180
- Keywords: cluster, utilization, scheduler, schedule, resource, allocated, solution, server, cost, scoring, packing, scheduling, default, actually, process, update, policy, across

### Resumo baseado na transcript

hey everyone uh let's get started uh welcome to the session on bin packing pods and managed kubernetes thank you for being here I'm Vin Sur and I'm a senior software engineer at click house uh my co-presenter is Jan who he also works as a senior software engineer at click house so on the agenda today um we'll start with a short introduction to what is Click house and click house Cloud then we'll talk about the like overview of the problem that we fac in with our infrastructure

### Excerpt da transcript

hey everyone uh let's get started uh welcome to the session on bin packing pods and managed kubernetes thank you for being here I'm Vin Sur and I'm a senior software engineer at click house uh my co-presenter is Jan who he also works as a senior software engineer at click house so on the agenda today um we'll start with a short introduction to what is Click house and click house Cloud then we'll talk about the like overview of the problem that we fac in with our infrastructure and why used bin packing to solve it uh then we'll get into the details of what is our how infrastructure is set up what were the various approaches we used to solve our node utilization problem and then we'll also talk about like the roll out we did for our across our Fleet uh what were the savings we achieved and some of the learnings uh that we realized uh during this whole exercise um and then we'll end with Q&A at the very end so what is click house click house is an olap database uh it's used mainly for analytics use cases um it's used to generate aggregations and visualizations on your data U and it works best with mostly immutable data it's been in development since 2009 and it was open sourced in 2016 and it's gained a lot of popularity since then and it's one of the fastest growing GitHub communities click house is a fully distributed database so it supports replication sharding uh multimaster and cross region setup so it is production ready last and the most important thing about click house is that is extremely fast using various techniques such as column oriented storage and state-of-the-art data compression click house provides insights into uh the customer data in milliseconds which makes it one of the fastest databases out there so now that we have an idea about what is Click house what is Click house Cloud click house cloud is the serverless offering of click house uh it has various features such as idling and auto scaling so that you can bring down your compute when there are no uh when there's no activity on the cluster and similarly autos auto scale U the cluster when there are workload spikes we also have compute and storage separation so that you can scale compute independently of storage this is how a click house Cloud instance looks under the hood we use kubernetes as a compute layer and we use object storage uh for the data persistence um we currently still use PVCs for some metadata but we are in the process of moving away from that we're currently available
