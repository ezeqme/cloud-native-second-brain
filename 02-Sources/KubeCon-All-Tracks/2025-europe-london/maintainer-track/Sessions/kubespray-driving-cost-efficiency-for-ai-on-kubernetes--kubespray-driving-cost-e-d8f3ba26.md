---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Antoine Legrand", "Conny GmbH", "Mohamed Zaian", "New Work SE"]
sched_url: https://kccnceu2025.sched.com/event/1td0D/kubespray-driving-cost-efficiency-for-ai-on-kubernetes-antoine-legrand-conny-gmbh-mohamed-zaian-new-work-se
youtube_search_url: https://www.youtube.com/results?search_query=Kubespray%3A+Driving+Cost-Efficiency+for+AI+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubespray: Driving Cost-Efficiency for AI on Kubernetes - Antoine Legrand, Conny GmbH & Mohamed Zaian, New Work SE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Antoine Legrand, Conny GmbH, Mohamed Zaian, New Work SE
- Schedule: https://kccnceu2025.sched.com/event/1td0D/kubespray-driving-cost-efficiency-for-ai-on-kubernetes-antoine-legrand-conny-gmbh-mohamed-zaian-new-work-se
- Busca YouTube: https://www.youtube.com/results?search_query=Kubespray%3A+Driving+Cost-Efficiency+for+AI+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubespray: Driving Cost-Efficiency for AI on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td0D/kubespray-driving-cost-efficiency-for-ai-on-kubernetes-antoine-legrand-conny-gmbh-mohamed-zaian-new-work-se
- YouTube search: https://www.youtube.com/results?search_query=Kubespray%3A+Driving+Cost-Efficiency+for+AI+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SqKqB-q_m8E
- YouTube title: Kubespray: Driving Cost-Efficiency for AI on Kubernetes - Antoine Legrand & Mohamed Zaian
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubespray-driving-cost-efficiency-for-ai-on-kubernetes/SqKqB-q_m8E.txt
- Transcript chars: 9620
- Keywords: cluster, manage, mentioned, provider, thanks, upgrade, having, choose, infrastructure, deploy, communities, thousand, gpu, automatically, hardware, always, enible, everyone

### Resumo baseado na transcript

I'm Antoan Lron situ at Connie uh Gmbbh in Germany uh initial uh quarter of cupspray and I should have been with Moham today but unfortunately have to go back uh home yesterday. Um he's a senior engineer at New York I see and a cube spray maintainer. So how did we uh manage the cost of it and yeah two two main way one is to write better code uh more efficient uh uh code so can choose things or another way also is to um focus on the infrastructure. It's if you build everything on top of Kubernetes and using cube spray to manage your Kubernetes cluster then that's become your uh common denominator for every every every cluster you you manage. I think there is other many why you should do that for for scalability and so we not cover uh that you run this stack on top of kubernetes that is managed via cubestray as mentioned and that's allow you to write to run basically necessarily about focusing on the cost necessarily of like a provider but having removing the vendor lock in uh situation that's that has a biggest impact.

### Excerpt da transcript

Hi everyone, thank you for joining the session. I'm Antoan Lron situ at Connie uh Gmbbh in Germany uh initial uh quarter of cupspray and I should have been with Moham today but unfortunately have to go back uh home yesterday. Um he's a senior engineer at New York I see and a cube spray maintainer. So first quickly if you don't know what's cub spray it's an orchestrator for kubernetes so to install uh and and upgrade and all the life cycle of managing kubernetes cluster it's been there for 10 years since uh the first version of it and I've seen like a large adoption so far it's focusing on production uh environment so not necessarily like for development there is better tool for that and focus on maintenance and stability So having safe uh safe upgrade and so on. One thing that is uh very important is the uh flexibility. So we try really to meet uh where you are in term of configuration and that means it can run basically everywhere. So on the cloud on bare metal um private data center there is integration with uh most of of cloud provider.

It's uh works on every uh operating system uh nearly and and then you can yeah keep uh getting option choose the container runtime you want uh the networking interface calico selium uh any of them that's been around and so on. So that's uh very compensible and choose the option or the requirement you have and yeah there will be a pass uh can afford it. So once to use a containerd with sky code that's that's feasible and with the quickly how do we uh keep it stable mainly we have yeah a CI infrastructure that we deploy about 10 to 15,000 cluster that we try that we test test on uh every month so for every PR we will deploy about 20 to 50 cluster so that means we create yeah uh VM for let's say want to by Ubuntu with Calico will deploy three VM uh of them and deploy cube spray on it, test the cluster, test the networking and and and kill the kill the VM. So at times sometimes we have like yeah we can spin up depending of the of the workload two to 300 VM at once just to test uh PR from the communities.

Of course that's that's expensive. So how did we uh manage the cost of it and yeah two two main way one is to write better code uh more efficient uh uh code so can choose things or another way also is to um focus on the infrastructure. So today will be more talking about the infrastructure part and what's kind of best to lower price is to start to shop around. And if you look at the at the market actually there's a wide ra
