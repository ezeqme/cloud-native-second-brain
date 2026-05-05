---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Kevin Wang", "Huawei"]
sched_url: https://kccnceu2025.sched.com/event/1tx7c/balancing-cost-and-efficiency-day2-optimization-of-multi-cluster-ai-infrastructure-kevin-wang-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Balancing+Cost+and+Efficiency%3A+Day2+Optimization+of+Multi-Cluster+AI+Infrastructure+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Balancing Cost and Efficiency: Day2 Optimization of Multi-Cluster AI Infrastructure - Kevin Wang, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Kevin Wang, Huawei
- Schedule: https://kccnceu2025.sched.com/event/1tx7c/balancing-cost-and-efficiency-day2-optimization-of-multi-cluster-ai-infrastructure-kevin-wang-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Balancing+Cost+and+Efficiency%3A+Day2+Optimization+of+Multi-Cluster+AI+Infrastructure+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Balancing Cost and Efficiency: Day2 Optimization of Multi-Cluster AI Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7c/balancing-cost-and-efficiency-day2-optimization-of-multi-cluster-ai-infrastructure-kevin-wang-huawei
- YouTube search: https://www.youtube.com/results?search_query=Balancing+Cost+and+Efficiency%3A+Day2+Optimization+of+Multi-Cluster+AI+Infrastructure+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4pBhVVrCHyM
- YouTube title: Balancing Cost and Efficiency: Day2 Optimization of Multi-Cluster AI Infrastructure - Kevin Wang
- Match score: 1.017
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/balancing-cost-and-efficiency-day2-optimization-of-multi-cluster-ai-in/4pBhVVrCHyM.txt
- Transcript chars: 17967
- Keywords: cluster, actually, scheduling, workloads, workload, resource, eviction, federated, volcano, clusters, status, priority, multicluster, multiple, incluster, sharing, basically, resources

### Resumo baseado na transcript

I am Kevin Juan uh currently working on uh multiple projects on the CNCF and my personal background is more uh about uh scheduling and uh actually I started uh contributing to Kubernetes in the early days and during recent years I have been working on the volcano project as well as uh Kamala project. So today I would like to share uh my thoughts and my uh experience working on the uh multicluster AI uh infrastructure especially for you know a lot of uh day2 optimization. And uh uh during my uh uh discussion and collaboration with a lot of uh end users, we found that actually there are some of the assumptions and the design uh principles very important and that's uh being kind of proven multiple times from multiple users. So with that the layered uh architecture need to have specific f uh focus loosely coupled. So uh for the federated control plan we are kind of not able to store the whole uh the full detail of the uh member cluster status because otherwise why not we just have a hypers scale cluster right uh and also like the federated Um so with the limited time uh I will just cover three uh major challenges I've have been working on.

### Excerpt da transcript

Um hello everyone thanks for joining the talk today. I am Kevin Juan uh currently working on uh multiple projects on the CNCF and my personal background is more uh about uh scheduling and uh actually I started uh contributing to Kubernetes in the early days and during recent years I have been working on the volcano project as well as uh Kamala project. So today I would like to share uh my thoughts and my uh experience working on the uh multicluster AI uh infrastructure especially for you know a lot of uh day2 optimization. So uh a little bit background of uh the talk why we need a multicluster actually uh we all know that there are kind of multiple backgrounds. Some of the company they have uh multiple uh regional uh business it results in physically uh divided distributed clusters and also some of the users may run into the you know hardware procurement uh cycle issue. So they have to kind of extend their workload to the public cloud so they can uh rapidly uh rapidly get some of the uh uh uh resources and also uh during my experience I have met a lot of end users they are kind of restructuring their uh resource pools as their uh business grows.

So previously a lot of business teams they would uh independently uh build and uh manage their own uh cluster and later on they went to the uh structure that have a uh shared infra team to you know uh uh provide the uh order maintenance and also share the technology and also why not a few just a hypers scale uh clusters a lot of users said they are It's just very hard to rebuild and also you know maintaining a large scale clusters can be very hard. So that's how the story begins right. So um uh this is just a very uh brief architecture of the uh multicluster AI platform. So uh actually for the incluster scheduling incluster workload management uh we know that uh uh the volcano project has done a very good job uh it help provide a lot of functionality uh to support uh AI batch workload friendly struggling uh uh scheduling features as well as uh Q features and like uh resource sharing among cues and also uh priority based on cues and the capacity management sort of things at the multicluster uh actually we can call it just a federated layer uh we can use uh commada to manage the uh cluster uh healthy state and also uh propagate the workloads to the clusters according to your uh preference uh whether you would like to uh whether you would like the workload to be kind divided or just scheduled to some of the cluster o
