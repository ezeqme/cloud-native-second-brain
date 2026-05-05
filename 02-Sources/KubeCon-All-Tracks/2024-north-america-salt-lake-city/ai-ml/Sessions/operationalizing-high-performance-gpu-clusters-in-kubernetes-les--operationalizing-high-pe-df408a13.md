---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Will Gleich", "Wai Wu", "Databricks"]
sched_url: https://kccncna2024.sched.com/event/1i7kj/operationalizing-high-performance-gpu-clusters-in-kubernetes-lessons-learned-from-training-databricks-dbrx-will-gleich-wai-wu-databricks
youtube_search_url: https://www.youtube.com/results?search_query=Operationalizing+High-Performance+GPU+Clusters+in+Kubernetes%3A+Lessons+Learned+from+Training+Databricks+DBRX+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Operationalizing High-Performance GPU Clusters in Kubernetes: Lessons Learned from Training Databricks DBRX - Will Gleich & Wai Wu, Databricks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Will Gleich, Wai Wu, Databricks
- Schedule: https://kccncna2024.sched.com/event/1i7kj/operationalizing-high-performance-gpu-clusters-in-kubernetes-lessons-learned-from-training-databricks-dbrx-will-gleich-wai-wu-databricks
- Busca YouTube: https://www.youtube.com/results?search_query=Operationalizing+High-Performance+GPU+Clusters+in+Kubernetes%3A+Lessons+Learned+from+Training+Databricks+DBRX+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Operationalizing High-Performance GPU Clusters in Kubernetes: Lessons Learned from Training Databricks DBRX.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kj/operationalizing-high-performance-gpu-clusters-in-kubernetes-lessons-learned-from-training-databricks-dbrx-will-gleich-wai-wu-databricks
- YouTube search: https://www.youtube.com/results?search_query=Operationalizing+High-Performance+GPU+Clusters+in+Kubernetes%3A+Lessons+Learned+from+Training+Databricks+DBRX+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DPVFqvkIo5M
- YouTube title: Operationalizing High-Performance GPU Clusters in Kubernetes: Lessons Learned fr... W. Gleich, W. Wu
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/operationalizing-high-performance-gpu-clusters-in-kubernetes-lessons-l/DPVFqvkIo5M.txt
- Transcript chars: 35119
- Keywords: gpu, training, nickel, nvidia, network, errors, production, actually, health, across, workload, issues, switch, fabric, memory, checks, clusters, failure

### Resumo baseado na transcript

we're going to be talking about operationalizing high performance GPU clusters in kubernetes we're going to take lessons learned from train training data Brick's dbrx this was a state-of-the-art model released in March of 2024 um yeah we'll start with some introductions here my name is will glake I'm a devops engineer focused on kubernetes infrastructure and machine learning operations and we have I'm wwu I'm a software engineer focused on free trading yeah both why and myself were part of the Mosaic ml acquisition into Data breaks so we

### Excerpt da transcript

we're going to be talking about operationalizing high performance GPU clusters in kubernetes we're going to take lessons learned from train training data Brick's dbrx this was a state-of-the-art model released in March of 2024 um yeah we'll start with some introductions here my name is will glake I'm a devops engineer focused on kubernetes infrastructure and machine learning operations and we have I'm wwu I'm a software engineer focused on free trading yeah both why and myself were part of the Mosaic ml acquisition into Data breaks so we came uh part of we joined data breaks last year so we'll start with a slide or we'll start with we'll start with a talk overview here first we'll be talking about the problem space regarding GPU clusters for Gen training why we use gpus what makes gpus different from CPUs then we'll go into the solution space regarding passive monitoring for single node jobs then an overview of GD RDMA as and how we consume it within data breaks no we are consumers of the public Cloud so this will all be like a cloud Focus talk so there won't be much there won't be any on Prem kind of logistics yeah then finally we'll look at the Active Health checks and auto mitigation that we implemented for active for fabric Health checking so we'll look at llm training as a whole right here data bricks is in the business of customizing llms and you really have three starting points when you're when you're looking into this space first you can create your own pre-training data set pick a new model architecture and pre-train the model from scratch this is foundation model training this is what dbrx was this is uh llama GPT Gemini Claud all of these you know big foundational models but you don't have to pre-train a model you can do continued training or continued pre-training this allows you to take one of those base models presuming the licensing uh supports that then you can continually or you can continue training it on your domain data this allows the model to generalize even further into your domain into your spectrum lastly and what generally happens for kind of uh App application implementation is fine-tuning this specializes a model for a particular task and reduces generalizability you really are trying to tune for input output um ml pre-training workloads shift the scale to you know thousands or even tens of thousands of gpus in some some cases at such scale failure is not a matter of if but when you know these gpus are yeah um anyway fine-tunin
