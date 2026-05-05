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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["William Wang", "Hongcai Ren", "Huawei"]
sched_url: https://kccnceu2024.sched.com/event/1YeSM/maximizing-gpu-utilization-over-multi-cluster-challenges-and-solutions-for-cloud-native-ai-platform-william-wang-hongcai-ren-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Maximizing+GPU+Utilization+Over+Multi-Cluster%3A+Challenges+and+Solutions+for+Cloud-Native+AI+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Maximizing GPU Utilization Over Multi-Cluster: Challenges and Solutions for Cloud-Native AI Platform - William Wang & Hongcai Ren, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: William Wang, Hongcai Ren, Huawei
- Schedule: https://kccnceu2024.sched.com/event/1YeSM/maximizing-gpu-utilization-over-multi-cluster-challenges-and-solutions-for-cloud-native-ai-platform-william-wang-hongcai-ren-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Maximizing+GPU+Utilization+Over+Multi-Cluster%3A+Challenges+and+Solutions+for+Cloud-Native+AI+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Maximizing GPU Utilization Over Multi-Cluster: Challenges and Solutions for Cloud-Native AI Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSM/maximizing-gpu-utilization-over-multi-cluster-challenges-and-solutions-for-cloud-native-ai-platform-william-wang-hongcai-ren-huawei
- YouTube search: https://www.youtube.com/results?search_query=Maximizing+GPU+Utilization+Over+Multi-Cluster%3A+Challenges+and+Solutions+for+Cloud-Native+AI+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Tmo5EUsxLac
- YouTube title: Maximizing GPU Utilization Over Multi-Cluster: Challenges and Solutions for Cloud-Native AI Platform
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/maximizing-gpu-utilization-over-multi-cluster-challenges-and-solutions/Tmo5EUsxLac.txt
- Transcript chars: 15743
- Keywords: cluster, gpu, resource, resources, command, application, multiple, policy, clusters, utilization, scheduling, another, scheduler, schedule, component, workload, commander, available

### Resumo baseado na transcript

good afternoon everyone my name is William one a Mainer of volcano Community this is my partner today h m h Kai from huawe today we will share our thinking about Maxim maximizing GPU utilization over multicluster for cognitive AI so firstly let's have a look at why GPU utilization is so important to us firstly the high price of GPU leads to higher cost and secondly as AI model becomes larger and larger the demands for GPU explode and the GPU is in shortage from time to time thirdly

### Excerpt da transcript

good afternoon everyone my name is William one a Mainer of volcano Community this is my partner today h m h Kai from huawe today we will share our thinking about Maxim maximizing GPU utilization over multicluster for cognitive AI so firstly let's have a look at why GPU utilization is so important to us firstly the high price of GPU leads to higher cost and secondly as AI model becomes larger and larger the demands for GPU explode and the GPU is in shortage from time to time thirdly it takes long time for us from making order to get GPU cluster ready for production maybe s several weeks or even more there are there are several CH challenges for improving the GPU resource utilization the first challenge is is that the GPU devices are scattered among local areas the IDC and Cloud window so it making it difficult to manage them uniformly secondly when different teams share the GP resources so they are different GPU GPU Generations different versions so it's hard to share them fully finally the different GPU models and GPU versions make it difficult to unify so how do we build a platform to consolidate these distributed GPU Resources with different models different versions to make full use of them from my from our perspective I think an ideal platform should have the following functions first the plat the platform can uniform management manage the GPU resources the resources are from the different idcs different regions even from different Cloud providers at the same time the platform can nor normalize the GPU power computing power with different Generations secondly the ideal platform should have an intelligent scheduler that can schedule task to most most matching the resources based on the Glo Global resource view these scheduling Strate strategies have full have a lot of policies such as the minimum cost First the the highest performance first something like that so we propose to Leverage the colon cncf project commanda and volano to provide a multicluster AF solution the commander is uh responsible for the multic cluster access and and unify the resource management as mentioned earlier this resources is dist distributed in different regions also the command VI covers the scenarios scenarios like the high AV availability for f tolerance and job mreg so volcano volcano Global component is responsible for the life cycle management for the AI jobs and also cover the scheduling the global scheduler will Co coordinate with the in cluster scheduler so there will
