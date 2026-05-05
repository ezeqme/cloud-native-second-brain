---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["Storage Data", "GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Marcelo Costa", "Banco Mercantil"]
sched_url: https://kccncna2025.sched.com/event/27FWi/unveiling-automation-how-mercantil-transformed-data-streaming-with-strimzi-argo-and-kubernetes-marcelo-costa-banco-mercantil
youtube_search_url: https://www.youtube.com/results?search_query=Unveiling+Automation%3A+How+Mercantil+Transformed+Data+Streaming+With+Strimzi%2C+Argo%2C+and+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Unveiling Automation: How Mercantil Transformed Data Streaming With Strimzi, Argo, and Kubernetes - Marcelo Costa, Banco Mercantil

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Marcelo Costa, Banco Mercantil
- Schedule: https://kccncna2025.sched.com/event/27FWi/unveiling-automation-how-mercantil-transformed-data-streaming-with-strimzi-argo-and-kubernetes-marcelo-costa-banco-mercantil
- Busca YouTube: https://www.youtube.com/results?search_query=Unveiling+Automation%3A+How+Mercantil+Transformed+Data+Streaming+With+Strimzi%2C+Argo%2C+and+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Unveiling Automation: How Mercantil Transformed Data Streaming With Strimzi, Argo, and Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWi/unveiling-automation-how-mercantil-transformed-data-streaming-with-strimzi-argo-and-kubernetes-marcelo-costa-banco-mercantil
- YouTube search: https://www.youtube.com/results?search_query=Unveiling+Automation%3A+How+Mercantil+Transformed+Data+Streaming+With+Strimzi%2C+Argo%2C+and+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tWpspU_9ClE
- YouTube title: Unveiling Automation: How Mercantil Transformed Data Streaming With Strimzi, Argo... Marcelo Costa
- Match score: 0.968
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/unveiling-automation-how-mercantil-transformed-data-streaming-with-str/tWpspU_9ClE.txt
- Transcript chars: 11447
- Keywords: architecture, connector, process, automation, solution, connectors, business, create, running, integration, working, connect, powerful, platform, brazil, single, everything, simple

### Resumo baseado na transcript

Many people believe that running Kafka is complex, expensive and painful. We can see numerous linking post discussing the challenges of manage a self-hosted Kafka cluster. We then decide to implement a solution we call integration hub a data architecture capable of connecting our onrem systems such as the main frame here and it's built on Kafka at its core and not that this architecture has everything needs to make governance and the administration of this environment easy, simple and standard but setup and architecture like that is not simple and you need to concern about some characterist. Note that this architecture has lots of components that make everything working together to make Kafka simple. But with this architecture we have some challenges and one of them is to administrate Kafka connect and make easy the use of Kafka and create connectors.

### Excerpt da transcript

Hi everyone, good afternoon. It's an honor to be here at Kubon. Thank you for being here. My name is Marcelo Costa. I am head of data at Mechanu Bank in Brazil. Many people believe that running Kafka is complex, expensive and painful. We can see numerous linking post discussing the challenges of manage a self-hosted Kafka cluster. But as engineers, our job is to fix business problems with software. My talk today is to demonstrate how we at Mechanu Bank in Brazil utilize software engineering to simplify our operations by efficiently moving data across the company. Mechan Bank is a 80-year-old mediumsiz bank in Brazil growing quarter after quarter. But with growth comes new challenges and the one of them providing real time access to data. Imagine now dozens of business teams asking for data and those requests are hitting legacies directly. This is a common situation that companies worldwide face. previously this strategy that I show here. A single data request could take up to seven business days. We have been on a growth traitor for the past five years.

Our previous method to moving data was not keeping pace with your growth needs. Business leaders complying access to data to make decision is too slow and in many case they are correct. We then decide to implement a solution we call integration hub a data architecture capable of connecting our onrem systems such as the main frame here and it's built on Kafka at its core and not that this architecture has everything needs to make governance and the administration of this environment easy, simple and standard but setup and architecture like that is not simple and you need to concern about some characterist. Note that this architecture has lots of components that make everything working together to make Kafka simple. But with this architecture we have some challenges and one of them is to administrate Kafka connect and make easy the use of Kafka and create connectors. Kafka connect in this contest when you set up a first version of this architecture need to be manually managed with high risk of human errors.

Lead time to create a connector is between seven and 10 days. Lack of versioning, traceability and scalability. High operational depness and how low standardization. Sometimes just one misconfigured parameters could block the entire process and we had to call in expert firefight to fix it. This create bottleneck and to complicate this architecture. Here we have the main frame as uh stood the main frame.
