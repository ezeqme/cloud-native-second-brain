---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Lukáš Hejtmánek", "Viktória Spišaková", "Masaryk University"]
sched_url: https://kccncna2021.sched.com/event/lV1B/implementation-challenges-from-hpc-to-containers-in-the-academy-lukas-hejtmanek-viktoria-spisakova-masaryk-university
youtube_search_url: https://www.youtube.com/results?search_query=Implementation+Challenges%3A+From+HPC+to+Containers+in+the+Academy+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Implementation Challenges: From HPC to Containers in the Academy - Lukáš Hejtmánek & Viktória Spišaková, Masaryk University

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Lukáš Hejtmánek, Viktória Spišaková, Masaryk University
- Schedule: https://kccncna2021.sched.com/event/lV1B/implementation-challenges-from-hpc-to-containers-in-the-academy-lukas-hejtmanek-viktoria-spisakova-masaryk-university
- Busca YouTube: https://www.youtube.com/results?search_query=Implementation+Challenges%3A+From+HPC+to+Containers+in+the+Academy+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Implementation Challenges: From HPC to Containers in the Academy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1B/implementation-challenges-from-hpc-to-containers-in-the-academy-lukas-hejtmanek-viktoria-spisakova-masaryk-university
- YouTube search: https://www.youtube.com/results?search_query=Implementation+Challenges%3A+From+HPC+to+Containers+in+the+Academy+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AoKul-5E1BM
- YouTube title: Implementation Challenges: From HPC to Containers in the Academy - Lukáš Hejtmánek & V Spišaková
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/implementation-challenges-from-hpc-to-containers-in-the-academy/AoKul-5E1BM.txt
- Transcript chars: 14780
- Keywords: infrastructure, storage, containers, resources, access, container, running, shared, challenge, compute, interact, systems, provide, fairness, somehow, computation, utilize, scheduling

### Resumo baseado na transcript

Today we are going to talk about implementation challenges from HPC to containers in the academy. I am IT architect of our infrastructure which consists of both storage and compute nodes. However, storage resources are spread among various Czech cities and this creates confusion for users because they have to take care about compute and data affinity. Another problem is caused by time-limited access to Kerberized storage. In a shared infrastructure, Docker is mostly prohibited due to security issues. We operate several Kubernetes clusters that are built on Rancher Kubernetes Engine second version together with Rancher dashboard.

### Excerpt da transcript

Hi. Today we are going to talk about implementation challenges from HPC to containers in the academy. And who we are? Hello. I am Lukáš Hroněk. I am from Masaryk University and assistant from the Czech Republic. I am IT architect of our infrastructure which consists of both storage and compute nodes. And I am Victoria. I'm also from Masaryk University where I work as an IT specialist, but essentially I take care about our Kubernetes infrastructure. So, our Czech national research and education network is called e-infra.cz and it operates HPC environment. We have approximately 20,000 CPU cores, 200 GPUs, and 60 petabytes of storage. And the computational resources are accessible mostly through batch system PBS Pro. And storage resources are accessible through Kerberized NFS version 4. Storage can be also accessed by S3 or Ceph RBD, but just a minority of users choose this way. And we have about 1,000 active users. So, in HPC, we have two types of resources, compute resources and storage resources. Users interact with compute resources via creating shell scripts and running them in a batch system PBS Pro.

They have to have SSH experience because these batch systems do not provide any graphical user interface. We try to change this by implementing Open OnDemand. That was our attempt to provide some graphical user interface. And secondly, storage storages are directly available on worker nodes. However, storage resources are spread among various Czech cities and this creates confusion for users because they have to take care about compute and data affinity. On the other side, these storages can be mounted to users' computers. HPC brings some troubles. First of all, there is no straightforward way to monitor running computations, so users can't easily check the state of their jobs. Secondly, older scripts are not compatible with today's technology. I bet most of you know Python 2 versus Python 3 issues. Furthermore, every user must possess at least average Unix skills because they have to interact with batch systems that are run via command line. Another problem is caused by time-limited access to Kerberized storage.

After certain time, users have to renew their access token. Last but not least, setting up NFS client is a hard task for every user when he or she wants to access their data from their own computer. So far, I have been talking only about HPC, but as we are at KubeCon, I will move to containers now. Uh I think that majority of you have already hea
