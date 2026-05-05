---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Klaus Ma", "Huawei Cloud"]
sched_url: https://kccnceu2022.sched.com/event/ytky/volcano-intro-deep-dive-klaus-ma-huawei-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Volcano%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Volcano: Intro & Deep Dive - Klaus Ma, Huawei Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Klaus Ma, Huawei Cloud
- Schedule: https://kccnceu2022.sched.com/event/ytky/volcano-intro-deep-dive-klaus-ma-huawei-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Volcano%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Volcano: Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytky/volcano-intro-deep-dive-klaus-ma-huawei-cloud
- YouTube search: https://www.youtube.com/results?search_query=Volcano%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=a76CajRhsX0
- YouTube title: Volcano: Intro & Deep Dive - Klaus Ma, Huawei Cloud
- Match score: 0.756
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/volcano-intro-deep-dive/a76CajRhsX0.txt
- Transcript chars: 20804
- Keywords: volcano, scheduling, results, workload, support, resource, training, cluster, common, another, management, performance, requirement, several, feature, utilization, product, tenants

### Resumo baseado na transcript

this is klaus i'm the founder of volcano and cool batch and i used to be the co-leader of sixth gathering and taking the lead of cncf tagalong time volcano is a cloud native batch system for intelligent workload such as hpc ai and big data it was promoted to sincere fingerprinting project earlier this year so it's my pleasure to give a introduction and deep dive on this project here is the background on why we would like to have volcano project at the beginning we build a batch

### Excerpt da transcript

hello everyone welcome to kubecon and cloudnation europe 2022. this is klaus i'm the founder of volcano and cool batch and i used to be the co-leader of sixth gathering and taking the lead of cncf tagalong time volcano is a cloud native batch system for intelligent workload such as hpc ai and big data it was promoted to sincere fingerprinting project earlier this year so it's my pleasure to give a introduction and deep dive on this project here is the background on why we would like to have volcano project at the beginning we build a batch system for traditional hpc workload and then we have big data platform to handle data and after that we leverage cloud native technical for ai platform but the problem is that this probe this all this platform are using different technical stack building different ecosystem this will make it hard to share results between the different workloads the resource utilization is is really low so more and more organizations are leveraging cloud native technical to build a unified platform for our workloads but there's still some gap in the cloud native ecosystem so we built a cool batch at 2017 to handle scattering gap the then we build the volcano based on the cool batch to handle all the other related gaps here is a major gap in the cloud native ecosystem for batch workload the first one is the job management it's a common requirement to have different product template and a fun green lifecycle management in a job it's a complex and hard to maintain to build a cr to build crd for different type of job the second gap is about the scheduling such as the priority functioning gun capability resolution and backfill and so on the third gap is to support a different workload in common drop of crd to reduce the complexity complexity and material effort the next one is dynamic resource scheduling dynamic resource sharing between the different attendant tenants such as queue the last gap is the board performance most of the intelligent workload required hazard put for example without a requirement to dispatch eight thousand poles per second for spark drop as we know the throughput of default schedule is about 100 per uh per second yeah here is the overview of volcano project volcano includes several components for multi-cloud scenario we have a federation sub-project in pipeline to balance the results between between the different cluster in in each individual cluster we have introduced several series such as the job for common batch wo
