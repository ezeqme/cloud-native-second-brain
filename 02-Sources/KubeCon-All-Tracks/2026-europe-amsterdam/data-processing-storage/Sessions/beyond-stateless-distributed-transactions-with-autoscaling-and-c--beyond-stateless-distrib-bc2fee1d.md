---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Jumpei Nishitani", "Hitachi"]
sched_url: https://kccnceu2026.sched.com/event/2CW5R/beyond-stateless-distributed-transactions-with-autoscaling-and-consistency-on-kubernetes-jumpei-nishitani-hitachi
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Stateless%3A+Distributed+Transactions+with+Autoscaling+and+Consistency+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Beyond Stateless: Distributed Transactions with Autoscaling and Consistency on Kubernetes - Jumpei Nishitani, Hitachi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jumpei Nishitani, Hitachi
- Schedule: https://kccnceu2026.sched.com/event/2CW5R/beyond-stateless-distributed-transactions-with-autoscaling-and-consistency-on-kubernetes-jumpei-nishitani-hitachi
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Stateless%3A+Distributed+Transactions+with+Autoscaling+and+Consistency+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Beyond Stateless: Distributed Transactions with Autoscaling and Consistency on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5R/beyond-stateless-distributed-transactions-with-autoscaling-and-consistency-on-kubernetes-jumpei-nishitani-hitachi
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Stateless%3A+Distributed+Transactions+with+Autoscaling+and+Consistency+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Lq-nQ8iTnrQ
- YouTube title: Beyond Stateless: Distributed Transactions with Autoscaling and Consistency on K... Jumpei Nishitani
- Match score: 0.982
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/beyond-stateless-distributed-transactions-with-autoscaling-and-consist/Lq-nQ8iTnrQ.txt
- Transcript chars: 17267
- Keywords: transaction, machine, business, distributed, architecture, processing, response, contract, important, concept, consensus, online, failure, change, result, reactive, consistency, scalability

### Resumo baseado na transcript

Uh how many of you have ever had a choice between the strong consistency and scalability? We will explore the practical way to get the both distributed transactions and seamless autoscaling on Kubernetes. Here I will explain how transaction monitor integrates with the HPA horizon scaler to allow status business application to the scale efficiently while retaining a sheet property based on the real world experience and example. This session will offer the actionable insight in the system design and deployment. Here online sh rem means interactively or synchronous but OLTP has a building challenges. To understand the problem better, let's establish a common understanding of the typical three tire architecture we often seen in the enterprise system.

### Excerpt da transcript

Hello everyone and welcome to CubeCom. Uh let me start with a question. Uh how many of you have ever had a choice between the strong consistency and scalability? How many of you have been told you can have one but not both? For year uh we've told this is a fundamental trade off. We just have to accept. Well, today I'm here to tell you that this is the first choice. My name is Jere Nishani and today we will go beyond stateless. We will explore the practical way to get the both distributed transactions and seamless autoscaling on Kubernetes. This is a story of how we challenged one of the hardest program in modern architecture. A little about me. Uh I am a software engineer at Hitachi and I focused on the distributed system and transaction processing and I have worked for years on the challenge of the building reliability large scale system. This experience led me to the work I will present today. And here is a roadmark for our session today. We will proceed in three main steps to discuss a pra practical method for achieve strong consistency and seamless autoscaling on kubernetes.

First we will take a deep dive into the online transaction needs and the painoint structure of its state machine. To solve the problem, we must of course first deeply understanding it. We will build a shared understanding of why traditional system are so fragile and why they are so difficult to scale. And next once that problem structure is clear, we reframe our central question how to overcome the state machine scaling problem. And this question was a starting point for all of our research and development. And finally uh I will present our answer the transaction processing mechanism of the Paxoscom transaction orchestrator. Here I will explain how transaction monitor integrates with the HPA horizon scaler to allow status business application to the scale efficiently while retaining a sheet property based on the real world experience and example. This session will offer the actionable insight in the system design and deployment. So let's start with the first item on our agenda. Online transaction needs and the painoint structure of state machine.

Online transaction processing is an IT system that interactively update data for things like a payment contract or settlement. Here online sh rem means interactively or synchronous but OLTP has a building challenges. A failure in update control can cause the loss or corruption of the business data especially that involved money. This can
