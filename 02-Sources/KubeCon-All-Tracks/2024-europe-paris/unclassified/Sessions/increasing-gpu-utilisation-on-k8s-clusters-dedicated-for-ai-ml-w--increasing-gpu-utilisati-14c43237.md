---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Maciej Mazur", "Canonical / Ubuntu", "Andreea Munteanu", "Canonical"]
sched_url: https://kccnceu2024.sched.com/event/1YeR2/increasing-gpu-utilisation-on-k8s-clusters-dedicated-for-aiml-workloads-maciej-mazur-canonical-ubuntu-andreea-munteanu-canonical
youtube_search_url: https://www.youtube.com/results?search_query=Increasing+GPU+Utilisation+on+K8s+Clusters+Dedicated+for+AI%2FML+Workloads+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Increasing GPU Utilisation on K8s Clusters Dedicated for AI/ML Workloads - Maciej Mazur, Canonical / Ubuntu & Andreea Munteanu, Canonical

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Maciej Mazur, Canonical / Ubuntu, Andreea Munteanu, Canonical
- Schedule: https://kccnceu2024.sched.com/event/1YeR2/increasing-gpu-utilisation-on-k8s-clusters-dedicated-for-aiml-workloads-maciej-mazur-canonical-ubuntu-andreea-munteanu-canonical
- Busca YouTube: https://www.youtube.com/results?search_query=Increasing+GPU+Utilisation+on+K8s+Clusters+Dedicated+for+AI%2FML+Workloads+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Increasing GPU Utilisation on K8s Clusters Dedicated for AI/ML Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeR2/increasing-gpu-utilisation-on-k8s-clusters-dedicated-for-aiml-workloads-maciej-mazur-canonical-ubuntu-andreea-munteanu-canonical
- YouTube search: https://www.youtube.com/results?search_query=Increasing+GPU+Utilisation+on+K8s+Clusters+Dedicated+for+AI%2FML+Workloads+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vKfCl3x_Xes
- YouTube title: Increasing GPU Utilisation on K8s Clusters Dedicated for AI/ML Workloads
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/increasing-gpu-utilisation-on-k8s-clusters-dedicated-for-ai-ml-workloa/vKfCl3x_Xes.txt
- Transcript chars: 20242
- Keywords: gpu, basically, multiple, actually, cluster, typically, clusters, projects, important, scheduling, standard, bigger, performance, especially, training, networking, resources, network

### Resumo baseado na transcript

okay hello and welcome everyone uh this will be a talk about increasing GPU utilization on kubernetes clusters and I wanted to starts from thanking you for still being here after this exhausting week I hope you are not as tired as I am and will stay with me through the talk uh so my name is machek mazur I'm the principal AI engineer in canonical that's the company behind Ubuntu and I'm typically working on the other side of the fence I know that you guys are mostly SS

### Excerpt da transcript

okay hello and welcome everyone uh this will be a talk about increasing GPU utilization on kubernetes clusters and I wanted to starts from thanking you for still being here after this exhausting week I hope you are not as tired as I am and will stay with me through the talk uh so my name is machek mazur I'm the principal AI engineer in canonical that's the company behind Ubuntu and I'm typically working on the other side of the fence I know that you guys are mostly SS admins devops engineers people working on kubernetes clusters I'm the user of the great stuff that you guys build and do and I wanted to tell you a little bit uh about how we are actually using it what are our goals and how we build couple of projects last year with infrastructures which varies from like 7,000 to 12,000 gpus in one project setup or a cluster so why we are even interested in kubernetes for AIML from the ml engineer perspective like power life is typically super structured there is a process that we are following called mlops and basically there are lot of small steps that needs to happen using various types of compute and from our experience we saw that kubernetes gives us a lot of repeatability gives us all the pipelines portability scaling so all the standard stuff that you guys realized already 10 years ago it took us a little bit more time but we now uh started using it properly as well I think but why this talk is about gpus and why we do even need them in the cluster so the actual things that we are doing is mostly matrix multiplication a lot of things will show ml as something very complicated but mathematically these are uh sort of a standard computations and why gpus because it's very similar to this this would be your screen with RGB and it's also Matrix so all the Silicon being built by Nvidia by AMD by Intel is basically the tool that was used to do a lot of similar computations and that's why uh in machine learning gpus become super popular and that's why we are uh using it very heavily during our processes so typically what you would do in any kubernetes cluster you need your GPU operator something that will enable the device to be visible uh if the cluster is bigger you would also go with a network operator to connect the gpus together so that's like a fairly standard example of a stack from Nvidia but uh okay so we want to use gpus which ones and is there really any difference and uh with gpus you can go with the setup from Nvidia that's the most popular one th
