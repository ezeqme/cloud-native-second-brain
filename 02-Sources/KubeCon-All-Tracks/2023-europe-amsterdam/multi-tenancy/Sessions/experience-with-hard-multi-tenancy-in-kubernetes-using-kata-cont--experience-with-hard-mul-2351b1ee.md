---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Multi-tenancy"
themes: ["AI ML", "Storage Data", "Runtime Containers", "Kubernetes Core"]
speakers: ["Shuo Chen", "Databricks"]
sched_url: https://kccnceu2023.sched.com/event/1Hydz/experience-with-hard-multi-tenancy-in-kubernetes-using-kata-containers-shuo-chen-databricks
youtube_search_url: https://www.youtube.com/results?search_query=Experience+with+%E2%80%9CHard+Multi-Tenancy%E2%80%9D+in+Kubernetes+Using+Kata+Containers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Experience with “Hard Multi-Tenancy” in Kubernetes Using Kata Containers - Shuo Chen, Databricks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[AI ML]], [[Storage Data]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shuo Chen, Databricks
- Schedule: https://kccnceu2023.sched.com/event/1Hydz/experience-with-hard-multi-tenancy-in-kubernetes-using-kata-containers-shuo-chen-databricks
- Busca YouTube: https://www.youtube.com/results?search_query=Experience+with+%E2%80%9CHard+Multi-Tenancy%E2%80%9D+in+Kubernetes+Using+Kata+Containers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Experience with “Hard Multi-Tenancy” in Kubernetes Using Kata Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hydz/experience-with-hard-multi-tenancy-in-kubernetes-using-kata-containers-shuo-chen-databricks
- YouTube search: https://www.youtube.com/results?search_query=Experience+with+%E2%80%9CHard+Multi-Tenancy%E2%80%9D+in+Kubernetes+Using+Kata+Containers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hVUqqEGO2-Q
- YouTube title: Experience with “Hard Multi-Tenancy” in Kubernetes Using Kata Containers - Shuo Chen, Databricks
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/experience-with-hard-multi-tenancy-in-kubernetes-using-kata-containers/hVUqqEGO2-Q.txt
- Transcript chars: 20618
- Keywords: container, performance, single, inside, customer, infrastructure, multiple, basically, memory, network, machine, customers, boundary, additional, however, access, runtime, virtual

### Resumo baseado na transcript

okay so uh hello guys my name is I am a software engineer from daily bricks and today my topic is uh experience with heart multi-tennessee in kubernetes using Color container um so starting from some introduction of Who We Are so database provides a unified and open platform for data and Analytics so we have our own data storage solution which combines the data warehouse and the data Lighthouse as a single concept and we call it lake house and meanwhile many of our services are built on top

### Excerpt da transcript

okay so uh hello guys my name is I am a software engineer from daily bricks and today my topic is uh experience with heart multi-tennessee in kubernetes using Color container um so starting from some introduction of Who We Are so database provides a unified and open platform for data and Analytics so we have our own data storage solution which combines the data warehouse and the data Lighthouse as a single concept and we call it lake house and meanwhile many of our services are built on top of spark for data analyzing and we also have our own machine learning products for AI and data model training so you know we're classic infrastructure model we separate our own services and customers infrastructure infrastructure so we integrate with cloud storage compute and Security in our customer's cloud account and we manage and deploy those cloud infrastructures and customers we have and also we always provide services on top of multiple Cloud providers such as like AWS Azure or gcp for example so that's the traditional way that we provide our services and recently one of our revolutionary aspects of our products is moving our services to a serverless mode so what is Thrill is mode uh the meaning of the server list is we migrate all the info infrastructure management to our own account instead of like inside a customer account so that it eliminates that over has to manage those core providers assets from the customer account meanwhile there are a lot of benefits for surveys such as the service provisioning time will be super fast and the service will be super elastic so with serverless we usually can provide our spark cluster to customer in less than five seconds also since we take the ownership of the new fraud management we would have some more flexibility to play with it and lower customer's infrastructure cost so with these serverless mode we want to use kubernetes as our infrastructure infrastructure due to its great portability and accessibility for continuous workflows and the kubernetes is cloud and agnostic and it has a rapid growing ecosystem so we mark it as our number one candidate each customer's workloads will be a single pod or a set of PODS basically a deployment or a demon set in um you know or kubernetes cluster however like one of the main difference with traditional kubernetes cluster is requires the hard money tenancy so what is hormon tendency it means that basically the tenants within a single querness cluster might comes from different comp
