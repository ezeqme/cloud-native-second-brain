---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Jian Li", "SK Telecom"]
sched_url: https://kccnceu2026.sched.com/event/2CW7f/virtualizing-large-scale-gpu-cluster-for-sovereign-ai-petasus-ai-cloud-journey-with-kubernetes-jian-li-sk-telecom
youtube_search_url: https://www.youtube.com/results?search_query=Virtualizing+Large+Scale+GPU+Cluster+for+Sovereign+AI%3A+Petasus+AI+Cloud+Journey+with+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Virtualizing Large Scale GPU Cluster for Sovereign AI: Petasus AI Cloud Journey with Kubernetes - Jian Li, SK Telecom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jian Li, SK Telecom
- Schedule: https://kccnceu2026.sched.com/event/2CW7f/virtualizing-large-scale-gpu-cluster-for-sovereign-ai-petasus-ai-cloud-journey-with-kubernetes-jian-li-sk-telecom
- Busca YouTube: https://www.youtube.com/results?search_query=Virtualizing+Large+Scale+GPU+Cluster+for+Sovereign+AI%3A+Petasus+AI+Cloud+Journey+with+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Virtualizing Large Scale GPU Cluster for Sovereign AI: Petasus AI Cloud Journey with Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7f/virtualizing-large-scale-gpu-cluster-for-sovereign-ai-petasus-ai-cloud-journey-with-kubernetes-jian-li-sk-telecom
- YouTube search: https://www.youtube.com/results?search_query=Virtualizing+Large+Scale+GPU+Cluster+for+Sovereign+AI%3A+Petasus+AI+Cloud+Journey+with+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m1buNUEmXTg
- YouTube title: Virtualizing Large Scale GPU Cluster for Sovereign AI: Petasus AI Cloud Journey with Kube... Jian Li
- Match score: 1.017
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/virtualizing-large-scale-gpu-cluster-for-sovereign-ai-petasus-ai-cloud/m1buNUEmXTg.txt
- Transcript chars: 24657
- Keywords: gpu, topology, infrastructure, somehow, performance, switch, virtualizing, provide, partition, nvidia, virtualize, actually, fabric, storage, virtualization, without, cluster, already

### Resumo baseado na transcript

Nice to see you and uh yeah today I would like to give a talk about the virtualizing the large scale GPU uh cluster for so I uh this basically target to our in-house build solution called the pto cloud journey with the uh uh kubernetes so I'm from uh SK telecom from South Korea and I'm Jen and currently working as a principal engineer at SKT so this is a just brief overview that u about our slide Right. So the first uh challenge what we had is a GPU resource fragmentation and waste. to virtualize the ambulink first also we need to virtualize the GPU fabric and for the regular purpose like a north south traffic is dealing with the BPC so it's been virtualized already and the last one is uh the storage fabric And the typically the training job require very high speed like a storage fabric as long as the IOPS for the storage storage appliance perspective. So somehow when we start to virtualize the storage fabric as well the storage we some we also need to care a lot about the performance.

### Excerpt da transcript

Nice to see you and uh yeah today I would like to give a talk about the virtualizing the large scale GPU uh cluster for so I uh this basically target to our in-house build solution called the pto cloud journey with the uh uh kubernetes so I'm from uh SK telecom from South Korea and I'm Jen and currently working as a principal engineer at SKT so this is a just brief overview that u about our slide Right. So first of all I just want to uh provide some background of today's talk. First of all, just from the last year uh around July uh we started our GPU as a service at the South Korea uh with the over 1,000 Blackwell GPUs uh which is fully managed by the Pasi cloud and uh we call this cluster as a H cluster uh which has been uh fully uh constructed and designed and by the SKT uh with some partners like Penguin Solutions and the Super Micro. Um we are using the HGX type uh like a server scale uh GPU servers uh in our production and uh in this uh environment we fully virtualize the entire AI infrastructure uh using our solution and uh but uh now there are two end customers are using our solution to train their uh RLM model and actually the HANE cluster the name HANE is inspired by the Hannes hub which is one of the very famous temple in South Korea and we position ourself as a core element of the Korea's sovereign AI infrastructure.

So uh before I go dive deep into our my my talk I want to just want to address uh the several uh issues what we faced uh when we start to operate the large scale like AI uh data center especially the infrastructure specifically. So the first uh challenge what we had is a GPU resource fragmentation and waste. So as you know the HSGX or uh DJX type observer uh by default equipped with the eight GPUs uh in each node and statically um allocate those GPUs to a specific team and uh it leaves the low overall utilization and uh which in turn can increase the TCO. So for example, some team or maybe some user just need two GPUs just run their uh ARM like inference workload for example. In that case we cannot just provide such a infrastructure without virtualizing the entire infrastructure. Somehow we need to split the uh ATGX node into several parts especially the GPU perspective. And the second uh address uh the issue what we address want to address here is uh uh AI uh environment provisioning delays.

Actually uh once we provide for example like you know uh provide the biome type of services to end user somehow the user need to be dealing
