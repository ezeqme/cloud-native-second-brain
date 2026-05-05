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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Shaun Hopper", "Meta", "Navarre Pratt", "CoreWeave"]
sched_url: https://kccncna2025.sched.com/event/27FWE/metas-kubernetes-based-portable-ai-research-environment-shaun-hopper-meta-navarre-pratt-coreweave
youtube_search_url: https://www.youtube.com/results?search_query=Meta%E2%80%99s+Kubernetes-based+Portable+AI+Research+Environment+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Meta’s Kubernetes-based Portable AI Research Environment - Shaun Hopper, Meta & Navarre Pratt, CoreWeave

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Shaun Hopper, Meta, Navarre Pratt, CoreWeave
- Schedule: https://kccncna2025.sched.com/event/27FWE/metas-kubernetes-based-portable-ai-research-environment-shaun-hopper-meta-navarre-pratt-coreweave
- Busca YouTube: https://www.youtube.com/results?search_query=Meta%E2%80%99s+Kubernetes-based+Portable+AI+Research+Environment+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Meta’s Kubernetes-based Portable AI Research Environment.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWE/metas-kubernetes-based-portable-ai-research-environment-shaun-hopper-meta-navarre-pratt-coreweave
- YouTube search: https://www.youtube.com/results?search_query=Meta%E2%80%99s+Kubernetes-based+Portable+AI+Research+Environment+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ts7bI51gRCo
- YouTube title: Meta’s Kubernetes-based Portable AI Research Environment - Shaun Hopper, Meta & Navarre Pratt
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/metas-kubernetes-based-portable-ai-research-environment/ts7bI51gRCo.txt
- Transcript chars: 31226
- Keywords: running, cluster, everything, logs, pretty, deploy, usually, metrics, environment, training, clusters, compute, provider, customer, getting, control, container, information

### Resumo baseado na transcript

Hi everyone, welcome to our talk on Meta's Kubernetes-based portable AI research environment. Uh but one of those is work with the meta team starting about a few years ago after some conversations at KubeCon uh to deploy their infrastructure and use a large scale uh core cluster for research done by their fair team. Um, and we'll show sort of how that works on top of Kubernetes in a bit. uh before we get to how things like sort of look today on Kubernetes and our multicloud uh there's a little bit of history we have to go through. So as I mentioned before we were sort of locked into doing things a specific way depending on the cloud provider we were running in um because we were not using Kubernetes. So in this design, we didn't have the containerized SLMD, but we did when we moved to Kubernetes.

### Excerpt da transcript

Hi everyone, welcome to our talk on Meta's Kubernetes-based portable AI research environment. My name is Navar Pratt. I'm a software engineer at Core on our applied training team. I'm joined today by Sean Hopper, a production engineer at Meta. I've done a few different things throughout my years at Cororeweave. Uh but one of those is work with the meta team starting about a few years ago after some conversations at KubeCon uh to deploy their infrastructure and use a large scale uh core cluster for research done by their fair team. So I'm sure a lot of you in this crowd know who Meta is. Uh maybe more more people nowadays know what Corore is, but if not I'll give a little description. So Cororee is a cloud provider. Some people call us a neocloud. We like to call ourselves the essential cloud for AI. Um, marketing aside, what exactly does that mean? It means that we deploy very large scale uh bare metal Kubernetes clusters with a lot of GPUs. So, AI infrastructure used for training uh used for inference.

So, we're running a lot lot of large scale Kubernetes clusters for a lot of large scale customers like Meta. Um, so customers aren't running single GPU or single node workloads. often time they're running training jobs of you know thousands of GPUs or tens of thousands of GPUs. So when you're working with customers like that uh it's very common for them to have footprints in other places. We don't expect many large scale customers to only be a core reef cloud customer again because they're only focused on AI workloads and not necessarily any workload you'd use a cloud for. So [clears throat] uh when we're working with people like Meta, we need to be able to support them uh bringing a stack uh from an on-prem location or another cloud provider to uh running on Coreave. And that's what we'll talk today about what Meta has done with Core and how they've extended that across different providers. >> Cool. Uh okay, it's working. Uh yeah, so I'm Sean. I'm a production engineer at Meta and um for us like uh the the story kind of begins with like chat GBT becoming super popular and then GPUs getting like super hard to find.

Um so we started you know trying to find it where we could. Um but we had a training platform that was um sort of locked into existing cloud providers and not at all portable. So like as the supply of GPUs became somewhat available, we wanted to invest in a platform that we could uh move across these cloud providers. Just for everyone's like me
