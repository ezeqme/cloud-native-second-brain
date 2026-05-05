---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Jorge Palma", "Principal PM Lead for Azure Kubernetes Services", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27dCv/sponsored-keynote-scaling-smarter-simplifying-multicluster-ai-with-kaito-and-kubefleet-jorge-palma-principal-pm-lead-for-azure-kubernetes-services-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Scaling+Smarter%3A+Simplifying+Multicluster+AI+with+KAITO+and+KubeFleet+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sponsored Keynote: Scaling Smarter: Simplifying Multicluster AI with KAITO and KubeFleet - Jorge Palma, Principal PM Lead for Azure Kubernetes Services, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Jorge Palma, Principal PM Lead for Azure Kubernetes Services, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27dCv/sponsored-keynote-scaling-smarter-simplifying-multicluster-ai-with-kaito-and-kubefleet-jorge-palma-principal-pm-lead-for-azure-kubernetes-services-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Scaling+Smarter%3A+Simplifying+Multicluster+AI+with+KAITO+and+KubeFleet+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Scaling Smarter: Simplifying Multicluster AI with KAITO and KubeFleet.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dCv/sponsored-keynote-scaling-smarter-simplifying-multicluster-ai-with-kaito-and-kubefleet-jorge-palma-principal-pm-lead-for-azure-kubernetes-services-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Scaling+Smarter%3A+Simplifying+Multicluster+AI+with+KAITO+and+KubeFleet+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SHG6T-8HIX8
- YouTube title: Sponsored Keynote: Scaling Smarter: Simplifying Multicluster AI with KAITO and KubeFl... Jorge Palma
- Match score: 1.008
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sponsored-keynote-scaling-smarter-simplifying-multicluster-ai-with-kai/SHG6T-8HIX8.txt
- Transcript chars: 5200
- Keywords: inferencing, models, clusters, gateway, deepseek, running, gpu, question, efficiently, capacity, projects, together, workspace, anywhere, across, cluster, deploy, routing

### Resumo baseado na transcript

For most companies and most of us, the question is no longer if we're going to use AI, but how we're going to do it in a responsible and scalable manner. But as history tells us, it's really with open-source that technology can be democratized and where innovation truly accelerates. CubeFleet allows you to intelligently place workloads anywhere in the world across Kubernetes clusters. If you pair these two projects together with things like an inferencing gateway, you can now serve models, place them anywhere in the world and route to them efficiently based on metrics like performance for example. So today I have for you an architecture that has three Kubernetes clusters and the first two we're going to be running for inferencing and the last one will run our inferencing gateway and our application. Then we're going to be deploying the inferencing pool, which in a nutshell is a specialized Kubernetes service that allows our inferencing gateways to point to the right models.

### Excerpt da transcript

Good morning, CubeCon. For most companies and most of us, the question is no longer if we're going to use AI, but how we're going to do it in a responsible and scalable manner. Proprietary and fragmented solutions really dominate today. But as history tells us, it's really with open-source that technology can be democratized and where innovation truly accelerates. We're able to build common frameworks. We're able to iterate faster and go from development to production much quicker. Today, this week, uh even you've already seen the announcement of the AI conformance program on Tuesday, really setting up a technical standard for running AI applications in Kubernetes clusters. But where do you really start? You've already seen, you know, adding GPUs is not really the only thing you must do if you can find them in this the gold nuggets of the AI rush era, but you also still need to set them up. You need to efficiently use them. Often times you have different GPUs, very hetrogenous environments and how do you set them up and make them be performant for your applications?

How do you efficiently use your capacity throughout the world? And how do you keep your costs in check? Today I'm here to talk to you about two sandbox projects that have been working tirelessly together. The first one is Kao, the Kubernetes AI tool chain operator, possibly the simplest way to run and serve AI inferencing in Kubernetes. It does so via a workspace construct where you can pass on your model and then defer all the GPU provisioning tasks to its GPU provisioner. You can also ground your model using fine-tuning and rack capabilities and parameters that it provides. The second one is CubeFleet. CubeFleet allows you to intelligently place workloads anywhere in the world across Kubernetes clusters. In the context of AI, it helps you find GPU capacity and place your models there wherever they are running. If you pair these two projects together with things like an inferencing gateway, you can now serve models, place them anywhere in the world and route to them efficiently based on metrics like performance for example.

But let's take a look at what this looks like in action. So today I have for you an architecture that has three Kubernetes clusters and the first two we're going to be running for inferencing and the last one will run our inferencing gateway and our application. All of this is managed by a cube fleet hub cluster. Let me break it down a bit more for you. The first two we'r
