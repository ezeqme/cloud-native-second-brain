---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Hiromu Asahina", "Kentaro Ogawa", "NTT Corporation"]
sched_url: https://kccnceu2024.sched.com/event/1YeR9/testing-k8s-cluster-and-vnfs-in-telco-staging-environments-hiromu-asahina-kentaro-ogawa-ntt-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Testing+K8s+Cluster+and+VNFs+in+Telco+Staging+Environments+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Testing K8s Cluster and VNFs in Telco Staging Environments - Hiromu Asahina & Kentaro Ogawa, NTT Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Hiromu Asahina, Kentaro Ogawa, NTT Corporation
- Schedule: https://kccnceu2024.sched.com/event/1YeR9/testing-k8s-cluster-and-vnfs-in-telco-staging-environments-hiromu-asahina-kentaro-ogawa-ntt-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Testing+K8s+Cluster+and+VNFs+in+Telco+Staging+Environments+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Testing K8s Cluster and VNFs in Telco Staging Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeR9/testing-k8s-cluster-and-vnfs-in-telco-staging-environments-hiromu-asahina-kentaro-ogawa-ntt-corporation
- YouTube search: https://www.youtube.com/results?search_query=Testing+K8s+Cluster+and+VNFs+in+Telco+Staging+Environments+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=v3Iusd20Cv0
- YouTube title: Testing K8s Cluster and VNFs in Telco Staging Environments - Hiromu Asahina & Kentaro Ogawa
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/testing-k8s-cluster-and-vnfs-in-telco-staging-environments/v3Iusd20Cv0.txt
- Transcript chars: 17464
- Keywords: environment, staging, design, cluster, development, scenario, little, production, trying, running, change, configuration, testing, source, introduce, repository, single, network

### Resumo baseado na transcript

uh okay uh hello everyone uh thank you for coming our presentation uh testing kuet cluster and B who in staging environment uh I'm K research engineer from n d and my colleague here asahina uh he's the most skillful engineer related to combin the open infra uh open stack infra and kuet infra with gtps in current NTT so uh NTT is the Japanese uh biggest and oldest Tero in uh in short of the uh Japanese uh version of 18 andt actually yeah and or a mission is

### Excerpt da transcript

uh okay uh hello everyone uh thank you for coming our presentation uh testing kuet cluster and B who in staging environment uh I'm K research engineer from n d and my colleague here asahina uh he's the most skillful engineer related to combin the open infra uh open stack infra and kuet infra with gtps in current NTT so uh NTT is the Japanese uh biggest and oldest Tero in uh in short of the uh Japanese uh version of 18 andt actually yeah and or a mission is uh at npt is to uh contribute to open source uh that may help us in the future and to propose the use of Open Source to other department or doing real business in our company like the uh development team of the 5gc and for the last two year as uh we have worked for the open Stock taka project to introduce uh kues uh into T and help migration from open stock based BM to kubernetes based containers now kubernetes has become quite common uh so more important thing is not using kubernetes but or how kubernetes is used Al so we think gtps uh provides a good answer to this question so now we focus on uh proposing it UPS to our 5G Development Department or but since our system U still has Legacy part and we cannot change everything at once uh so after internal interviews we decided that the staging environment would be our first Target so if we s Ed or in changing our staging environment or we can uh we we believe we can easily apply it or to the production environment or in the near future okay now as will go on to explain our uh challenges okay uh thank you go again I I'm her from NTI um I am a software engineer and uh like he said uh we are trying to introduce gups to our um 5D Department let's say I see you see what I mean and uh originally um I didn't plan uh do any live demo but uh after watching this cubicon um I think we have to try it so because like he said we are trying to do G up so maybe this is a easy as demo you ever seen so um we have a configuration maybe you see the krm like thing and uh I'm going to change just uh kubernetes version here okay okay okay so something happen behind here and uh you can can see the current version of the Ku is 1.2 124 it's a little bit too old but uh if it's succeeded maybe we can see it will be upgraded so I'll check it later it's going to take um s minutes so maybe we run out of time okay um let's go back to my slide okay like he said uh we we worked for uh open stack but uh nowadays you know open stack is a little bit too um it's it's kind of legacy and we are
