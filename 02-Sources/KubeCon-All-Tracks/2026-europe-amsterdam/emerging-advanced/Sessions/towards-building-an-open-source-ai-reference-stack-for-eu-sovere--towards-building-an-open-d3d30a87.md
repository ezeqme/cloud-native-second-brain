---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Emerging + Advanced"
themes: ["AI ML", "Community Governance"]
speakers: ["Madhav Bhargava", "SAP Labs", "Sanjay Chatterjee", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2CVzj/towards-building-an-open-source-ai-reference-stack-for-eu-sovereign-cloud-madhav-bhargava-sap-labs-sanjay-chatterjee-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Towards+Building+an+Open+Source+AI+Reference+Stack+for+EU+Sovereign+Cloud+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Towards Building an Open Source AI Reference Stack for EU Sovereign Cloud - Madhav Bhargava, SAP Labs & Sanjay Chatterjee, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Madhav Bhargava, SAP Labs, Sanjay Chatterjee, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2CVzj/towards-building-an-open-source-ai-reference-stack-for-eu-sovereign-cloud-madhav-bhargava-sap-labs-sanjay-chatterjee-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Towards+Building+an+Open+Source+AI+Reference+Stack+for+EU+Sovereign+Cloud+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Towards Building an Open Source AI Reference Stack for EU Sovereign Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzj/towards-building-an-open-source-ai-reference-stack-for-eu-sovereign-cloud-madhav-bhargava-sap-labs-sanjay-chatterjee-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Towards+Building+an+Open+Source+AI+Reference+Stack+for+EU+Sovereign+Cloud+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WdcIOOyJaDI
- YouTube title: Towards Building an Open Source AI Reference Stack for EU Sov... Madhav Bhargava & Sanjay Chatterjee
- Match score: 0.842
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/towards-building-an-open-source-ai-reference-stack-for-eu-sovereign-cl/WdcIOOyJaDI.txt
- Transcript chars: 25365
- Keywords: actually, essentially, cluster, nvidia, called, extension, garden, dynamo, kernel, network, operator, reference, sovereign, provides, application, scheduling, modules, particular

### Resumo baseado na transcript

Welcome to our talk towards building an open-source AI reference stack on U sovereign cloud. I'm Sanji Chari from Nvidia and my colleague >> Hi, I'm Madav Bharu from SAP. some some are latency bound and they all can run on you know not just homogeneous architectures but also heterogeneous architectures with CPUs, GPUs, LPUs, TPUs etc. How to orchestrate multi-node multicomponent AI with disagregated architectures on heterogeneous compute at scale. So in this in this talk we are going to explore how to build the an AI reference stack on Kubernetes that satisfies all of the above requirements in the context of the EU sovereign cloud. So we start we stand on the shoulders of U CNCF and and and Kubernetes.

### Excerpt da transcript

Welcome to our talk towards building an open-source AI reference stack on U sovereign cloud. I'm Sanji Chari from Nvidia and my colleague >> Hi, I'm Madav Bharu from SAP. >> Let's get started. We are entering the era of sovereign AI and opensource software is the foundation of EU sovereign infrastructure because it is builds trust through transparency. What it really means for the U sovereign cloud is that this infrastructure needs to be rooted with European values such as GDPR compliance, data sovereignty, u you know data being processed locally. So when you build the AI reference stack on top of this infrastructure, it'll include sovereign models that have been trained with sovereign data. Um and data being processed by LM chatbots or AI uh agents will need to be localized within EU sovereign boundaries. So we want to understand the AI landscape a little bit today. So we can see that AI workloads are rapidly evolving. For example, the traditional single node serving model is slowly shifting towards complex multi-node multicomponent systems.

For example, disagregated inference architectures are typically composed of a mix of different kinds of tasks like computebound tasks which are memory bound. some some are latency bound and they all can run on you know not just homogeneous architectures but also heterogeneous architectures with CPUs, GPUs, LPUs, TPUs etc. So now Kubernetes has a new challenge. How to orchestrate multi-node multicomponent AI with disagregated architectures on heterogeneous compute at scale. And this enforces quite a few requirements for example hierarchical gang scheduling multi-level autoscaling topology placement and startup dependencies between these tasks. So in this in this talk we are going to explore how to build the an AI reference stack on Kubernetes that satisfies all of the above requirements in the context of the EU sovereign cloud. Thanks Sanjay. So we start we stand on the shoulders of U CNCF and and and Kubernetes. So SAP has created a foundation called Neoforce Foundation under the EU um under the uh which is funded through the uh European Union is an initiative called the important project of common European interest or IPSI.

This is public money and it unlocks quote unquote somewhere around 8 billion euros of investment. So with the goal of building a multi cloud multi-provider cloud to edge continum. So the participating companies and organizations are collaborating to power cloudnative in a fungeible fashion for c
